from turtle import *
from score import Score
from walls import Walls
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.tracer(0)

paddle = Paddle()
walls = Walls()
ball = Ball()
score = Score()

con = False


def again():
    global con
    screen.listen()
    screen.onkeypress(play, key='Return')
    con = True


def play():
    global con, score, screen, ball, walls
    if con:
        screen.clearscreen()
        screen.bgcolor('black')
        screen.tracer(0)

        paddle.reset_paddle()
        ball.reset_ball()
        walls.reset_walls()
        score.reset_score()

    screen.listen()
    screen.onkeypress(paddle.moving_right, 'Right')
    screen.onkeypress(paddle.moving_left, 'Left')

    while True:
        screen.update()
        ball.auto_moving()
        for wall in walls.walls:
            if ball.distance(wall) < 50:
                score.score += 10
                ball.x_move += 0.01
                ball.y_move += 0.01
                ball.color(wall.color()[0])
                walls.refresh(wall)
                ball.bounce_y()
                score.update_score()

        if ball.ycor() > 290:
            ball.bounce_y()
        elif ball.xcor() > 390 or ball.xcor() < -390:
            ball.bounce_x()
        elif ball.distance(paddle) < 70 and ball.ycor() < -270:
            ball.bounce_paddle()
        elif ball.ycor() < -290:
            score.game_over()
            if score.score > score.old_score:
                with open('score.txt', mode='w') as file:
                    file.write(f'{score.score}')
            again()
            # play(con=True)
            break


play()
screen.exitonclick()
