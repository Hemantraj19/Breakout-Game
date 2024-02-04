from turtle import Turtle
import random

COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
    "pink",
    "purple",
    "cyan",
    "magenta",
    "lime",
    "teal",
    "navy",
]


class Brick:
    def __init__(self):
        super().__init__()
        self.bricks_list = []
        self.create_bricks()

    def make_new_brick(self):
        brick = Turtle("square")
        brick.penup()
        brick.shapesize(stretch_len=4, stretch_wid=1)
        brick.color(random.choice(COLORS))
        brick.pencolor("black")
        self.bricks_list.append(brick)
        return brick

    def create_bricks(self):
        starting_point_x = -400
        starting_point_y = 280
        no_of_bricks = 11
        for i in range(11, 0, -1):
            for j in range(no_of_bricks):
                brick = self.make_new_brick()
                brick.goto(starting_point_x + j * 80, starting_point_y)
            starting_point_x += 40
            starting_point_y -= 20
            no_of_bricks -= 1
