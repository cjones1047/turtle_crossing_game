from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.goto(-200, 270)
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    @staticmethod
    def game_over():
        game_over_sign = Turtle()
        game_over_sign.hideturtle()
        game_over_sign.color("black")
        game_over_sign.penup()
        game_over_sign.write("GAME OVER", align="center", font=FONT)
