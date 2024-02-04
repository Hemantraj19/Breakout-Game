import time
from turtle import Screen
from brick import Brick
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
# ---------------------------- Place Bricks --------------------------------------
screen.tracer(0)
brick = Brick()
screen.update()
# -------------------------------------------------------------------------------

ball = Ball()
paddle = Paddle()
screen.update()
screen.tracer(1)
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move_ball()

    # Detect collision with right wall
    if ball.xcor() > 400:
        ball.bounce_left()

    # Detect collision with right_wall
    if ball.xcor() < -400:
        ball.bounce_left()

    # Detect collision with upper wall
    if ball.ycor() > 280:
        ball.bounce_right()

    if ball.ycor() < -265:
        game_is_on = False

    # Detect collision with one of the brick
    for single_brick in brick.bricks_list:
        if ball.distance(single_brick) < 51:
            ball.bounce_left()
            ball.bounce_right()
            single_brick.hideturtle()
            brick.bricks_list.remove(single_brick)
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() == -240:
        ball.bounce_right()

screen.exitonclick()
