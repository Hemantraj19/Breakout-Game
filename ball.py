from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        self.goto(0, -240)

    def move_ball(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_left(self):
        self.x_move *= -1

    def bounce_right(self):
        self.y_move *= -1
