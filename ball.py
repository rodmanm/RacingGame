from BoundedObject import BoundedObject
from car import Car

ball = []

class Ball(BoundedObject):
    @staticmethod
    def location():
        for i in ball:
            xPos, yPos = i.position()
            pos = (xPos, yPos)
            return pos
        return -1, -1

    @staticmethod
    def destroy():
        for i in ball:
            i.ht()
            i.clear()

    def __init__(self, speed, xMax, yMax):
        super().__init__(speed, xMax, yMax)
        self.resizemode('user')
        self.color('black', 'white')
        self.shape('circle')
        self.up()
        self.turtlesize(1.5)
        self.goto(300, 300)
        self.setheading(0)
        self.getscreen().tracer(1)
        global ball
        ball.append(self)

    def move(self):
        self.forward(self.getSpeed())
        self.setSpeed(self.getSpeed()*.97)
        if self.outOfBounds():
            self.computeNewHeading()

    def computeNewHeading(self):
        xPos, yPos = self.position()
        oldHead = self.heading()
        newHead = oldHead
        if xPos < 0 or xPos > self.getXMax():
            newHead = 180 - oldHead
        if yPos < 0 or yPos > self.getYMax():
            newHead = 360 - oldHead

        self.setheading(newHead)

    def checkCollisions(self):
        for vehicle in Car.getCars():
            if self.distance(vehicle) < 30:
                self.setheading(vehicle.heading())
                self.setSpeed(2*vehicle.getSpeed()*vehicle.gof + self.getSpeed())

    def remove(self):
        pass

