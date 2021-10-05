from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-240, y=250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.update_level()

    def increase_level(self):
        self.level += 1

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=FONT)