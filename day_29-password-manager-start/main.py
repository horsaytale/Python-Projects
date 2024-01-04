from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list=[random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    website_input=website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    new_data={
        website_input:{
            "email":email_input,
            "password":password_input
        }
    }

    if len(website_input)==0 or len(password_input)==0:
        messagebox.showwarning(title="Error!", message="Please don't leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website_input, message=f"These are the details you entered: \nEmail: {email_input} "
                                                            f"\nPassword: {password_input} \nIs it ok to save?")

        if is_ok:
    #         with open("data.txt","a")as data:
    #             data.write(f"{website_input} | {email_input} | {password_input}\n")
    #
    #         website_entry.delete(0,END)
    #         password_entry.delete(0, END)
                try:
                    with open("data.json", 'r') as data_file:
                        # Read the old data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        # Saving the updated data
                        json.dump(new_data, data_file, indent=4)
                else:
                    # Update the old data with new data
                    data.update(new_data)

                    with open("data.json", "w") as data_file:
                        # Saving the updated data - NOTED that it is 'WRITE' mode
                        # This shows that this mode will rewrite all the contents in the JSON data
                        json.dump(data, data_file, indent=4)

                finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_input=website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    # try:
    #     with open("data.json", 'r') as data_file:
    #         # Read the old data
    #         data = json.load(data_file)
    #         for website in data.keys():
    #             email_details=data[website_input]["email"]
    #             password_details = data[website_input]["password"]
    #
    # except FileNotFoundError:
    #     messagebox.showwarning(title="Error", message="No Data File Found")
    # except KeyError:
    #     messagebox.showwarning(title="Error", message="No such details exist")
    # else:
    #     messagebox.showinfo(title=f"{website_input}", message=f"Email: {email_details}\nPassword: {password_details}")
    try:
        with open("data.json", 'r') as data_file:
            # Read the old data
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    else:
        if website_input in data:
            email_details = data[website_input]["email"]
            password_details = data[website_input]["password"]
            messagebox.showinfo(title=f"{website_input}", message=f"Email: {email_details}\nPassword: {password_details}")
        else:
            messagebox.showwarning(title="Error", message="No such details exist")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"email@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()