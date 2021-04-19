from BoundedObject import BoundedObject
from time import time

class Car(BoundedObject):
    allCars = []
    fuel = 0

    @staticmethod
    def getCars():
        return [x for x in Car.allCars]

    def __init__(self, speed, xMax, yMax):
        super().__init__(speed, xMax, yMax)
        self.__ogSpeed = speed
        self.color('green')
        self.shape('turtle')
        self.turtlesize(3)
        self.setheading(0)
        self.size = 20
        Car.allCars = Car.getCars()
        Car.allCars.append(self)

        self.gof = False
        self.gob = False
        self.turnR = False
        self.turnL = False
        self.double = False
        self.contBkwd = True
        self.contFwd = True
        self.__timeMve = 0
        self.sec = time()
        self.cooldowncount = 0
        self.__screen = self.getscreen()
        self.setControls()

    def setControls(self):
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

    def move(self):
        if self.gof & self.contFwd:
            if self.double:
                self.forward((self.getSpeed()) * 3)
                self.__timeMve += 1
                if self.__timeMve >= 35:
                    self.double = False
            else:
                self.forward(self.getSpeed())
                self.__timeMve = max(0, self.__timeMve - 1)
        elif self.gob & self.contBkwd:
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
        if Car.fuel >= 2:
            self.double = True
            self.sec = time()
            self.__screen.onkey(lambda a: a, " ")
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

    def checkCollisions(self):
        angle = self.heading() % 360
        xPos, yPos = self.position()

        if xPos > self.getXMax() - self.size:
            self.contFwd = 90 < angle < 270
            self.contBkwd = not 90 < angle < 270
        elif xPos < 2*self.size:
            self.contFwd = not 90 < angle < 270
            self.contBkwd = 90 < angle < 270
        elif yPos > self.getYMax() - self.size:
            self.contFwd = angle > 180
            self.contBkwd = angle < 180
        elif yPos < self.size:
            self.contFwd = angle < 180
            self.contBkwd = angle > 180
        else:
            self.contFwd = True
            self.contBkwd = True

        if abs(xPos) + abs(yPos) > 3000:
            print("HOW DID YOU GET HERE?!?")

    def quit(self):
        self.__screen.bye()

    def remove(self):
        del self
