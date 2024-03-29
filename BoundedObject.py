from turtle import Turtle
from abc import abstractmethod
from threading import Thread

class BoundedObject(Turtle, Thread):
    def __init__(self, speed=0, xMax=800, yMax=800):
        super().__init__()
        Thread.__init__(self)
        self.size = 10
        self.__xMax = xMax
        self.__yMax = yMax
        self.__speed = speed

    def outOfBounds(self):
        xPos, yPos = self.position()
        out = False
        if xPos < self.size or xPos > self.__xMax - self.size:
            out = True
        if yPos < self.size or yPos > self.__yMax - self.size:
            out = True
        return out

    def getSpeed(self):
        return self.__speed

    def getXMax(self):
        return self.__xMax

    def getYMax(self):
        return self.__yMax

    def setSpeed(self, newSpeed):
        self.__speed = newSpeed

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def checkCollisions(self):
        pass

    @abstractmethod
    def move(self):
        pass
