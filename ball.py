from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('circle')
        self.color('#408E91')
        self.setposition(0, -270)
        self.showturtle()
        self.x_move = 2
        self.y_move = 2

    def auto_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_paddle(self):
        self.y_move *= -1

    def reset_ball(self):
        self.__init__()
