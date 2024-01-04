import turtle
import pandas

screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_state=data.state.to_list()
guessed_states=[]
is_on=True

while is_on:
    answer_input=screen.textinput(title=f"{len(guessed_states)}/{len(all_state)} States Correct", prompt="What are the states of US?").title()
    if answer_input in all_state and not answer_input in guessed_states:
        guessed_states.append(answer_input)
        state_detail=data[data.state==answer_input]
        t=turtle.Turtle()
        t.hideturtle()
        t.up()
        t.goto(int(state_detail.x),int(state_detail.y))
        t.write(answer_input)
    if answer_input=='Exit':
        missing_states=[state for state in all_state if state not in guessed_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing_state.csv")
        is_on=False

screen.exitonclick()