from classes import Ball, Car
from turtle import *
from Fish import Fish
import turtle
from threading import Thread


class Soccer(Turtle, Thread):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__turtle = turtle.Turtle()
        self.__mainWin = turtle.Screen()
        self.__mainWin.bgcolor('light blue')
        self.__mainWin.setworldcoordinates(self.__xMin, self.__yMin, self.__xMax, self.__yMax)
        self.__turtle.hideturtle()

    def play(self):
        Car(0, 7, self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        for a in Car.allCars:
            a.up()
            a.goto(-150, 300)
        self.__mainWin.onkey(self.placeBall, "p")
        self.__mainWin.onclick(self.placeFish, 1, None)
        # Car(0, 10, self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        self.__mainWin.listen()
        mainloop()

    def placeBall(self):
        Ball(0, self.__xMin, self.__xMax, self.__yMin, self.__yMax)

    def placeFish(self, x, y):
        # if Fish.getFish() < 3:
        Fish(10, self.__xMin, self.__xMax, self.__yMin, self.__yMax, x, y)

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
