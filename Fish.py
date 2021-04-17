import random
from BoundedObject import BoundedObject
from classes import Car

class Fish(BoundedObject):
    allFish = 0

    @staticmethod
    def getFish():
        return Fish.allFish

    def __init__(self, speed, xMin, xMax, yMin, yMax, xPlace, yPlace):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.getscreen().tracer(0)
        self.up()
        self.resizemode('user')
        self.color('black', 'red')
        self.shape('triangle')
        self.up()
        self.turtlesize(1.5)
        self.goto(xPlace, yPlace)
        self.setheading(random.randint(1, 358))
        self.getscreen().tracer(1)
        self.__screen = self.getscreen()
        Fish.allFish += 1
        self.__alive = True
        self.getscreen().ontimer(self.move, 1)
        self.getscreen().ontimer(self.checkCollisions, 1)

    def move(self):
        if self.__alive:
            self.forward(self.getSpeed())
        if self.outOfBounds():
            self.computeNewHeading()
        self.getscreen().ontimer(self.move, 2)

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
                if self.distance(a) < 30:
                    self.__alive = False
                    Fish.allFish -= 1
                    Car.fuel += 1
                    print("Fuel: ", Car.fuel)
                    self.clear()
            self.getscreen().ontimer(self.checkCollisions, 1)

    def remove(self):
        # TODO: Implement this
        pass
