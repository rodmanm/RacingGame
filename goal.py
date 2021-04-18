from BoundedObject import BoundedObject

class Goal(BoundedObject):
    def __init__(self):
        super().__init__()
        self.color('black', 'black')
        self.shape('square')
        self.up()
        self.turtlesize(15)
        self.ht()
        self.goto(800, 300)
        self.setheading(0)
        self.getscreen().tracer(1)
        self.st()

    def remove(self):
        self.ht()
        self.clear()
        del self

    def move(self):
        pass

    def checkCollisions(self):
        # TODO CHECK IF BALL IS IN GOAL
        pass
