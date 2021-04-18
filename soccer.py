# khondicker
from ball import Ball
from car import Car
from turtle import *
from Fish import Fish
import turtle
from sys import exit

class Soccer(Turtle):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__turtle = turtle.Turtle()
        self.__mainWin = turtle.Screen()
        self.__mainWin.bgcolor('light blue')
        self.window = turtle.Screen()
        self.window.setup(width=1.0, height=1.0, startx=None, starty=None)
        self.__mainWin.setworldcoordinates(self.__xMin, self.__yMin, self.__xMax, self.__yMax)
        self.__turtle.hideturtle()
        self.objects = []
        self.movement()

    def play(self):
        self.objects.append(Car(0, 7, self.__xMin, self.__xMax, self.__yMin, self.__yMax))
        for a in Car.allCars:
            a.up()
            a.goto(-150, 300)
        self.__mainWin.onkey(self.placeBall, "p")
        self.__mainWin.onclick(self.placeFish, 1, None)
        self.__mainWin.onkey(exit, "c")
        # Car(0, 10, self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        self.__mainWin.listen()
        mainloop()

    def placeBall(self):
        self.objects.append(Ball(0, self.__xMin, self.__xMax, self.__yMin, self.__yMax))

    def placeFish(self, x, y):
        self.objects.append(Fish(10, self.__xMin, self.__xMax, self.__yMin, self.__yMax, x, y))

    def movement(self):
        for i in self.objects:
            i.checkCollisions()
            i.move()
        # for i in range(len(self.fishies)):
        #     if not self.fishies[i].__alive:
        #         del self.fishies[i]
        self.__mainWin.ontimer(self.movement, 2)

    # def goal(self):
    #     pos = Ball.location()
    #     xPos = pos[0]
    #     yPos = pos[1]
    #     if (abs(xPos - self.__xMax) < 5):# and (250 < yPos < 350):
    #         self.reset()
    #     self.getscreen().ontimer(self.goal, 1)
    #
    # def reset(self):
    #     for a in Car.allCars:
    #         a.up()
    #         a.goto(-150, 300)
    #     self.__mainWin.onkey(self.placeBall, "p")


if __name__ == '__main__':
    game = Soccer(-800, 800, 0, 600)
    game.play()
