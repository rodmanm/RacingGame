import random
from math import pi
class FallingBlock:
    def __init__(self, canvas, FPS):
        self.FPS = FPS
        self.rect = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
    # Create object
    x = 300
    y = 0
    maxspeed = 10
    width = 100
    yspeed = 7
    xspeed = 0
    height = 100
    FPS = 60
    color = "black"

    def reset(self, canvas):
        self.x = random.randrange(self.width, int(canvas.winfo_width()-self.width))
        # TODO: Uncomment this line
        self.y = -self.height
        self.xspeed = 0
        self.yspeed = 1

    def render(self, canvas, FPS=60):
        self.FPS = FPS
        canvas.move(self.rect, self.x, self.y)

    def collide(self, car, window):
        if self.y >= window.winfo_height():  # We don't need to check for exceeding the top of the map
            self.reset(window)
        if self.x+self.width >= window.winfo_width():
            self.x = 0
        elif self.x <= 0:
            self.x = window.winfo_width() - self.width

        if(abs(car.x-self.x) < car.width+self.width/2) & (abs(car.y-self.y) < car.height+self.width/2):
            # This means the Hitboxes are colliding. However, the car's hitbox isn't accurate.
            if abs(car.y-self.y) > abs(car.x-self.x):
                # The car is mostly vertical to the block
                if car.y-self.y < 0:
                    # If the car is above the block
                    car.speed = 0.5*car.speed
                    self.yspeed += abs(car.speed)
                else:
                    # The car is below the block
                    car.speed = 0.5*(car.speed-self.yspeed)
                    self.yspeed += car.speed
                    car.angle = pi
                    # TODO: Proper Angle Changing
            else:
                # The car hit the side of the block
                if car.x > self.x:
                    # The car hit the right side of the block
                    car.speed = 0.5*car.speed
                    self.xspeed += car.speed
                else:
                    car.speed = 0.5*car.speed
                    self.xspeed += -car.speed
        self.x += self.xspeed
        self.yspeed += car.height/self.FPS/10
        self.y += self.yspeed
