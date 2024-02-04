from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=0.8)
        self.color("white")
        self.goto(0, -260)

    def go_left(self):
        if self.xcor() - 20 < -380:
            self.goto(-380, self.ycor())
        else:
            self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        if self.xcor() + 20 > 380:
            self.goto(380, self.ycor())
        else:
            self.goto(self.xcor() + 20, self.ycor())
