from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_words={}
translate_list={}
#------
try:
    french_data=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    translate_list = original_data.to_dict(orient="records")
else:
    translate_list=french_data.to_dict(orient="records")


#-----
def next_char():
    global random_words, flip_timer
    window.after_cancel(flip_timer)
    random_words = random.choice(translate_list)
    canvas.itemconfig(new_french, text="French", fill="black")
    canvas.itemconfig(new_english, text=random_words['French'], fill="black")
    canvas.itemconfig(card_background, image=main_pic)
    flip_timer=window.after(3000, flip_card)
#-----
def flip_card():
    canvas.itemconfig(new_french, text="English", fill="white")
    canvas.itemconfig(new_english, text=random_words['English'], fill="white")
    canvas.itemconfig(card_background, image=new_pic)
#-----
def is_known():
    translate_list.remove(random_words)
    print(len(translate_list))
    data=pandas.DataFrame(translate_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_char()
#-----
window=Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,flip_card)

canvas=Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
main_pic=PhotoImage(file="./images/card_front.png")
new_pic=PhotoImage(file="./images/card_back.png")
card_background=canvas.create_image(400,263, image=main_pic)
new_french=canvas.create_text(400,150, text="", fill="black", font=("Arial", 40, "italic"))
new_english=canvas.create_text(400,263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)
#-----

x_image=PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=x_image,highlightthickness=0, command=next_char)
wrong_button.grid(row=1,column=0)

u_image=PhotoImage(file="./images/right.png")
right_button=Button(image=u_image,highlightthickness=0, command=is_known)
right_button.grid(row=1,column=1)

next_char()

window.mainloop()

