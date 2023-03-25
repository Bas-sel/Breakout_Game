from turtle import *


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color('#408E91')
        self.shapesize(1, 7)
        self.starting_position()
        self.showturtle()
        self.speed('fastest')

    def starting_position(self):
        self.setposition(0, -290)

    def moving_right(self):
        self.fd(50)

    def moving_left(self):
        self.bk(50)

    def reset_paddle(self):
        self.__init__()
