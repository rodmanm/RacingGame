import random
from BoundedObject import BoundedObject
from car import Car
from threading import Thread

class Fish(BoundedObject, Thread):
    def __init__(self, speed, xMin, xMax, yMin, yMax, xPlace, yPlace):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.getscreen().tracer(0)
        self.up()
        self.resizemode('user')
        # self.color('black', 'red')
        # self.shape('triangle')
        self.up()
        self.turtlesize(1.5)
        self.goto(xPlace, yPlace)
        self.setheading(random.randint(1, 358))
        self.getscreen().tracer(1)
        self.__screen = self.getscreen()
        self.__alive = True
        if "Resources/fish-left.gif" not in self.getscreen().getshapes():
            self.getscreen().addshape("Resources/fish-left.gif")
        if "Resources/fish-right.gif" not in self.getscreen().getshapes():
            self.getscreen().addshape("Resources/fish-right.gif")
        self.shape("Resources/fish-left.gif")
        self.turtlesize(0.125)

    def move(self):
        if self.__alive:
            self.forward(self.getSpeed())
        if self.outOfBounds():
            self.computeNewHeading()

    def isAlive(self):
        return self.__alive

    def computeNewHeading(self):
        xPos, yPos = self.position()
        oldHead = self.heading()
        newHead = oldHead

        if xPos < self.getXMin() or xPos > self.getXMax():
            newHead = 180 - oldHead
        if yPos < self.getYMin() or yPos > self.getYMax():
            newHead = 360 - oldHead

        self.setheading(newHead)

    def checkCollisions(self):
        if self.__alive:
            for a in Car.getCars():
                if self.distance(a) < 100:
                    self.__alive = False
                    Car.fuel += 1
                    print("Fuel: ", Car.fuel)
                    self.ht()

    def remove(self):
        self.ht()
        pass
