from BoundedObject import BoundedObject
from car import Car

class Ball(BoundedObject):
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

    def remove(self):
        pass

