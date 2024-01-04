from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_event, text="00:00")
    label_tick.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    reps+=1

    if reps%8==0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min=math.floor(count/60)
    count_sec=count%60
    if count_min<10:
        count_min = f"0{count_min}"
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_event, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
    # WINDOW.AFTER allows continuous repetition on the function you provided based on the number of
    # arguments you given (*args) and based on the amount of time you state (1000ms==1sec)
    # meaning after 1 sec, the function will be activated and the next 1 sec and next 1 sec, etc
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        label_tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_event=canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1,column=1)


label=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label.grid(row=0,column=1)

label_tick=Label(fg=GREEN, bg=YELLOW)
label_tick.grid(row=3,column=1)

start_button=Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2,column=2)


window.mainloop()



