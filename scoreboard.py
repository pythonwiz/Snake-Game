from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

    def increment(self):
        self.score += 1
        self.clear()
        self.update_score()
