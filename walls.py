from turtle import *
import random


class Walls:
    def __init__(self):
        self.walls = []
        self.colors = ['#F9F54B', '#8BF5FA', '#C92C6D', '#E96479', '#F5E9CF', '#AAE3E2', '#85CDFD',
                       '#00425A', '#E4C988', '#30E3DF']
        self.make()

    def make(self):
        x = -330
        y = 200
        for j in range(1, 8):
            for i in range(1, 12):
                wall = Turtle()
                wall.speed('fast')
                wall.shape('square')
                wall.shapesize(2, 3)
                wall.color(random.choice(self.colors))
                wall.penup()
                wall.setposition(x, y)
                self.walls.append(wall)

                x += 65
            x = -330
            y -= 45

    def refresh(self, wall):
        wall.hideturtle()
        wall.setpos(500, 1000)
        self.walls.remove(wall)

    def reset_walls(self):
        self.__init__()