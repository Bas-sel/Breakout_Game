from turtle import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.old_score = 0
        self.hideturtle()
        self.penup()
        self.color('#408E91')
        self.best_score()
        self.update_score()

    def best_score(self):
        try:
            with open('score.txt', mode='r') as file:
                self.old_score = int(file.readline())
        except FileNotFoundError:
            pass

    def update_score(self):
        self.clear()
        self.setposition(100, 330)
        self.write(f'Score: {self.score}', font=('Arial', 20, 'normal'))
        self.setposition(-250, 330)
        self.write(f'Best Score: {self.old_score}', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.setposition(-280, 30)
        self.pencolor('#6D9886')
        self.write('GAME OVER', font=('Arial', 70, 'bold'))
        self.setposition(-140, -150)
        self.write('Press Enter To Play Again', font=('Arial', 20, 'italic'))

    def reset_score(self):
        self.__init__()
