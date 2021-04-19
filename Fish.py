import random
from BoundedObject import BoundedObject
from car import Car

class Fish(BoundedObject):
    def __init__(self, speed, xMax, yMax, xPlace, yPlace):
        super().__init__(speed, xMax, yMax)
        self.getscreen().tracer(0)
        self.up()
        self.resizemode('user')
        self.speed("fastest")
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
        if 270 > self.heading() % 360 > 90:
            self.shape("Resources/fish-left.gif")
        else:
            self.shape("Resources/fish-right.gif")

    def move(self):
        if self.__alive:
            self.forward(self.getSpeed()/2)
        if self.outOfBounds():
            self.computeNewHeading()

    def isAlive(self):
        return self.__alive

    def computeNewHeading(self):
        xPos, yPos = self.position()
        oldHead = self.heading()
        newHead = oldHead

        if xPos < 0 or xPos > self.getXMax():
            newHead = 180 - oldHead
        if yPos < 0 or yPos > self.getYMax():
            newHead = 360 - oldHead
        if 270 > newHead % 360 > 90:
            self.shape("Resources/fish-left.gif")
        else:
            self.shape("Resources/fish-right.gif")
        self.setheading(newHead)

    def checkCollisions(self):
        if self.__alive:
            for a in Car.getCars():
                if self.distance(a) < 60:
                    self.__alive = False
                    Car.fuel += 1
                    print("Score: ", Car.fuel)
                    self.ht()

    def remove(self):
        self.ht()
        self.clear()
        del self
