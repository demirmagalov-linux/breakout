from ursina import *
import random
import time

app = Ursina()

paddle = Entity(model='quad', color=color.white, scale=(1.5, 0.2))
ball = Entity(model='sphere', color=color.white, scale=(0.25, 0.25))

game_over = False
paddle.y = -3
ball.x = -2
ball.speed_x = 5
ball.speed_y = 3


start_x = -5.25
start_y = 3.0

bricks = []
for row in range(5):
    for col in range(8):
        brick = Entity(model='quad', color=color.white, scale=(1.3, 0.3))
        brick.x = start_x + (col * 1.4)
        brick.y = start_y - (row * 0.4)
        bricks.append(brick)  

def update():
    global game_over
    if not bricks and not game_over:
        Text(text='YOU WIN!', scale=2, origin=(0, 0))
        game_over = True

    if game_over == True:
        return
    ball.x += ball.speed_x * time.dt
    ball.y += ball.speed_y * time.dt
    if held_keys['a']:
        paddle.x -= 0.05
    elif held_keys['d']:
        paddle.x += 0.05  


    if ball.x >= 7:
        ball.speed_x = -abs(ball.speed_x) 
        ball.x = 6.7
    elif ball.x <= -7:
        ball.speed_x = abs(ball.speed_x)
        ball.x = -6.7
    elif ball.y >= 4:
        ball.speed_y = -ball.speed_y
    elif paddle.x - 0.75 < ball.x < paddle.x + 0.75 and paddle.y - 0.2 < ball.y < paddle.y + 0.2:
        ball.speed_y = abs(ball.speed_y)
        ball.y = paddle.y + 0.25
    
    for brick in bricks[:]:
        if brick.x - 0.65 < ball.x < brick.x + 0.65 and brick.y - 0.2 < ball.y < brick.y + 0.2:
            bricks.remove(brick)
            destroy(brick)
            ball.speed_x *= 1.025
            ball.speed_y = -ball.speed_y
            break

    if ball.y < -4:
            Text(text='LOSER!', position=(0, 0.2), origin=(0, 0), scale=2)
            ball.speed_x = 0
            ball.speed_y = 0
            ball.x = 0
            ball.y = 0
            ball.speed_x = random.choice([-1, 1]) * 5
            ball.speed_y = random.choice([-1, 1]) * 3
            game_over = True
app.run()