from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open(r"Day_20_21\data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def aumentar_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open(r"Day_20_21\data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
