from turtle import *
from abc import *
import time
import random

class boundedObject(Turtle):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__speed = speed

    def outOfBounds(self):
        xPos, yPos = self.position()
        out = False
        if xPos < self.__xMin or xPos > self.__xMax:
            out = True
        if yPos < self.__yMin or yPos > self.__yMax:
            out = True
        return out

    def getSpeed(self):
        return self.__speed

    def getXMin(self):
        return self.__xMin

    def getXMax(self):
        return self.__xMax

    def getYMin(self):
        return self.__yMin

    def getYMax(self):
        return self.__yMax

    def setSpeed(self, newSpeed):
        self.__speed = newSpeed

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def move(self):
        pass



class Ball(boundedObject):
    collisions = 0

    @staticmethod
    def location():
        xPos, yPos = Ball.position()
        pos = (xPos, yPos)
        return pos

    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.resizemode('user')
        self.color('black', 'white')
        self.shape('circle')
        self.up()
        self.turtlesize(1.5)
        self.goto(0, 300)
        self.setheading(0)
        self.getscreen().tracer(1)
        self.getscreen().ontimer(self.move, 1)
        self.getscreen().ontimer(self.checkCollisions, 1)


    def move(self):
        if Ball.collisions == 1:
            self.setSpeed(2)
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
        for a in Car.getCars():
            if self.distance(a) < 30:
                self.setheading(a.heading())
                Ball.collisions = Ball.collisions + 1
        self.getscreen().ontimer(self.checkCollisions, 1)


class Car(boundedObject):
    allCars = []
    fuel = 0


    @staticmethod
    def getCars():
        return [x for x in Car.allCars]

    def __init__(self, heading, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.__ogSpeed = speed
        # self.resizemode('user')
        self.color('green')
        self.shape('turtle')
        self.turtlesize(3)
        self.setheading(heading)
        Car.allCars = Car.getCars()
        Car.allCars.append(self)

        self.gof = False
        self.gob = False
        self.turnR = False
        self.turnL = False
        self.double = False
        self.__timeMve = 0
        self.cooldowncount = 0

        self.__screen = self.getscreen()
        self.__screen.onkeypress(self.fwd, "w")
        self.__screen.onkeyrelease(self.brake, "w")
        self.__screen.onkeypress(self.bkwd, "s")
        self.__screen.onkeyrelease(self.brake, "s")
        self.__screen.onkeypress(self.lft, "a")
        self.__screen.onkeyrelease(self.stpTurn, "a")
        self.__screen.onkeypress(self.rht, "d")
        self.__screen.onkeyrelease(self.stpTurn, "d")
        self.__screen.onkey(self.quit, "q")
        self.__screen.onkey(self.doubleSpeed, " ")
        self.getscreen().ontimer(self.move, 10)


    def move(self):
        if self.gof & self.boundsFGood():
            if self.double:
                self.forward((self.getSpeed()) * 3)
                self.__timeMve += 1
                if self.__timeMve >= 35:
                    self.double = False
            else:
                self.forward(self.getSpeed())
                self.__timeMve = max(0, self.__timeMve - 1)
        elif self.gob & self.boundsBGood():
            self.backward(self.getSpeed())


        if self.turnR:
            self.right(7)
        elif self.turnL:
            self.left(7)

        self.getscreen().ontimer(self.move, 10)


    def fwd(self):
        self.setSpeed(self.__ogSpeed)
        self.gof = True

    def bkwd(self):
        self.setSpeed(self.__ogSpeed)
        self.gob = True

    def lft(self):
        self.turnL = True

    def rht(self):
        self.turnR = True

    def brake(self):
        self.gof = False
        self.gob = False

    def stpTurn(self):
        self.turnR = False
        self.turnL = False

    def doubleSpeed(self):
        print("Boost?")
        if Car.fuel >= 2:
            self.double = True
            self.sec = time.time()
            self.__screen.onkey(None, " ")
            print("\nYeeesss!!")
            Car.fuel -= 2
            self.cooldowncount = 1000
            self.coolDown()

    def coolDown(self):
        if (self.cooldowncount <= 1):
            self.cooldowncount = 0
            self.__screen.onkey(self.doubleSpeed, " ")
        else:
            self.cooldowncount -= 1
            self.__screen.ontimer(self.coolDown, 10)

    def boundsFGood(self):
        contFwd = True
        angle = self.heading() % 360
        if self.outOfBounds():
            xPos, yPos = self.position()
            if (abs(xPos - self.getXMax()) < 20) and (angle < 90 or angle > 270):
                contFwd = False
            elif (abs(xPos - self.getXMin()) < 20) and (90 < angle < 270):
                contFwd = False
            if (abs(yPos - self.getYMax()) < 20) and angle < 180:
                contFwd = False
            elif (abs(yPos - self.getYMin()) < 20) and angle > 180:
                contFwd = False
        return contFwd

    def boundsBGood(self):
        contBkwd = True
        angle = self.heading() % 360
        if self.outOfBounds():
            xPos, yPos = self.position()
            if (abs(xPos - self.getXMax()) < 20) and (90 < angle < 270):
                contBkwd = False
            elif (abs(xPos - self.getXMin()) < 20) and (angle < 90 or angle > 270):
                contBkwd = False
            if (abs(yPos - self.getYMax()) < 20) and angle > 180:
                contBkwd = False
            elif (abs(yPos - self.getYMin()) < 20) and angle < 180:
                contBkwd = False
        return contBkwd

    def quit(self):
        self.__screen.bye()




class Fish(boundedObject):
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
                    self.hideturtle()
                    Fish.allFish -= 1
                    Car.fuel += 1
                    print("Fuel: ", Car.fuel)
                    self.clear()
            self.getscreen().ontimer(self.checkCollisions, 1)

