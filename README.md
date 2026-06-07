# Breakout

A Breakout clone built with Python and Ursina Engine. Break all the bricks to win, but don't let the ball fall past your paddle.

## How to play

Run the game with:

python breakout.py

Controls:

- A: move paddle left
- D: move paddle right

Clear all 40 bricks to win. If the ball falls below your paddle the game ends.

## Features

- 8 by 5 grid of bricks
- Ball speeds up slightly after each brick hit
- Win condition when all bricks are cleared
- Game over screen when the ball is lost

## Requirements

Python 3 and Ursina Engine.

To install Ursina:

pip install ursina

## Notes

The ball bounces off the walls, ceiling, and paddle. Ball speed increases with each brick destroyed so the game gets harder as you progress.
