# Brick Breaker Game

A simple Brick Breaker game implemented in Python using the Turtle graphics library.

## Description

This Python script creates a classic Brick Breaker game where a ball bounces around the screen, colliding with bricks and a paddle. The player controls the paddle to bounce the ball and break the bricks.

## Features

- Bricks are displayed on the screen using the `Brick` class.
- The ball is represented by the `Ball` class, and its movement is controlled by the `move_ball` method.
- The paddle is represented by the `Paddle` class, and its movement is controlled by the `go_left` and `go_right` methods.
- Collision detection is implemented for the ball with the walls, bricks, and paddle.
- When the ball collides with a brick, the brick is hidden, simulating its destruction.

## How to Play

- Use the "Left" and "Right" arrow keys to move the paddle left and right.
- The objective is to keep the ball in play by bouncing it off the paddle and breaking all the bricks.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/brick-breaker.git
   cd brick-breaker
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Play the game using the arrow keys.

## Dependencies

- Python 3.x
- Turtle graphics library

## Acknowledgments

- This game is inspired by the classic Brick Breaker arcade game.
- Special thanks to the Turtle graphics library for simplifying the graphics implementation.
