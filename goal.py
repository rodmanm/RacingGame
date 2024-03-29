from BoundedObject import BoundedObject
from ball import Ball

class Goal(BoundedObject):
    InGoal = False

    def __init__(self, x=800, y=300, size=15):
        super().__init__()
        self.color('black', 'black')
        self.shape('square')
        self.speed("fastest")
        self.up()
        self.turtlesize(size)
        self.ht()
        self.x = x
        self.y = y
        self.size = size * 5
        self.goto(self.x, self.y)
        self.setheading(0)
        self.getscreen().tracer(1)
        self.st()

    def remove(self):
        # self.clear()
        del self

    def move(self):
        pass

    def checkCollisions(self):
        x, y = Ball.location()
        if self.x + self.size > x > self.x - self.size:
            if self.y + self.size > y > self.y - self.size:
                Goal.InGoal = True
