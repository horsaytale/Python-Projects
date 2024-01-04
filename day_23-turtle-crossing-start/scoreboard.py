from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.score = 1
        self.score_written()

    def score_written(self):
        self.up()
        self.goto(-280, 250)
        self.write(f"Level {self.score}", font=FONT)

    def increase_level(self):
        self.clear()
        self.score+=1
        self.score_written()

    def game_over(self):
        self.home()
        self.write("Game Over", font=FONT, align="center")

