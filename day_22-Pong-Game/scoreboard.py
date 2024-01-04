from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.goto(-100, 240)
        self.update_score()

    def update_score(self):
        self.goto(-100, 240)
        self.write(self.l_score, font="Courier")
        self.goto(100, 240)
        self.write(self.r_score, font="Courier")


