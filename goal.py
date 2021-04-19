from BoundedObject import BoundedObject
from ball import Ball


class Goal(BoundedObject):
    def __init__(self, x=800, y=300, size=15):
        super().__init__()
        self.color('black', 'black')
        self.shape('square')
        self.up()
        self.turtlesize(size)
        self.ht()
        self.x = x
        self.y = y
        self.size = size * 10
        self.goto(self.x, self.y)
        self.setheading(0)
        self.getscreen().tracer(1)
        self.st()
        self.BallInGoal = False

    def remove(self):
        self.ht()
        self.clear()
        del self

    def move(self):
        pass

    def checkCollisions(self):
        x, y = Ball.location()
        if self.x + self.size > x > self.x - self.size \
                and self.y + self.size > y > self.y - self.size:
            self.BallInGoal = True
