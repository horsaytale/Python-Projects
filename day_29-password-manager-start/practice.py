from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
#--------------------------------
def add_info():
    website_input=website_entry.get()
    password_input = password_entry.get()
    email_input = email_entry.get()

    new_data={
        website_input:{
            "email":email_input,
            "password":password_input
        }
    }

    if len(website_input)==0 or len(password_input)==0:
        messagebox.showwarning(title="Error!", message="Please fill in the required input")
    else:
        is_ok=messagebox.askquestion(title=website_input, message=f"Are the following details correct?\nEmail: {email_input}\nPassword: {password_input}")

        if is_ok:
            # with open("data.txt",'a') as data:
            #     data.write(f"{website_input} | {email_input} | {password_input}")
            #
            # website_entry.delete(0, END)
            # password_entry.delete(0, END)
            try:
                with open("data.json") as data_file:
                    data=json.load(data_file)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data,data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0,END)
#--------------------------------
def info_search():
    website_input=website_entry.get()

    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error!", message="No Data File found")
    else:
        if website_input in data.keys():
            email_deet=data[website_input]["email"]
            password_deet=data[website_input]["password"]
            messagebox.showinfo(title=website_input, message=f"Email: {email_deet}\nPassword: {password_deet}")
            website_entry.delete(0, END)
        else:
            messagebox.showwarning(title="Error!", message="No such data found.")
            website_entry.delete(0, END)

#--------------------------------
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
image_1=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_1)
canvas.grid(row=0,column=1)

website=Label(text="Website")
website.grid(row=1,column=0)
email=Label(text="Email")
email.grid(row=2,column=0)
password=Label(text="Password")
password.grid(row=3,column=0)

website_entry=Entry()
website_entry.focus()
website_entry.grid(row=1,column=1)

email_entry=Entry()
email_entry.insert(0,"email@hotmail.com")
email_entry.grid(row=2,column=1, columnspan=2)

password_entry=Entry()
password_entry.grid(row=3,column=1)

search_button=Button(text="Search", command=info_search)
search_button.grid(row=1,column=2)

password_button=Button(text="Generate Password", width=20, command=generate_password)
password_button.grid(row=3,column=2)

add_button=Button(text="Add Info", width=40, command=add_info)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()