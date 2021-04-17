from BoundedObject import BoundedObject
from time import time

class Car(BoundedObject):
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
        self.sec = time()
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
            if self.double:
                self.right(7*3)
            else:
                self.right(7)
        elif self.turnL:
            if self.double:
                self.left(3*7)
            else:
                self.left(7)

    def fwd(self):
        self.speed("fastest")
        self.gof = True

    def bkwd(self):
        self.speed("fastest")
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
            self.sec = time()
            self.__screen.onkey(None, " ")
            print("\nYeeesss!!")
            Car.fuel -= 2
            self.cooldowncount = 1000
            self.coolDown()

    def coolDown(self):
        if self.cooldowncount <= 1:
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

    def remove(self):
        self.ht()
        self.quit()