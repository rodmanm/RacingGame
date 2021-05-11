import random
from math import log, pi
class fallingBlock():
    def __init__(self,FPS, window, car):
        self.window = window
        self.FPS = FPS
        self.car = car
        self.x = 300
        self.y = 0
        self.width = 100
        self.yspeed = 7
        self.xspeed = 0
        self.height = 100
        self.FPS = 60
        self.color = (0,0,0)
    #Create object
    maxspeed = 10
    def reset(self):
        self.x = random.randrange(self.width, self.window.width-self.width)
        self.y = -self.height
        self.xspeed = 0
        self.yspeed = 1
    def render(self, pygame, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.width, self.height])
    def update(self):
        if(self.y >= self.window.height):
            self.reset()
        if(self.x+self.width>=self.window.width):
            self.x = 0
        elif(self.x<=0):
            self.x = self.window.width - self.width

        if(abs(self.car.x-self.x)<self.car.width+self.width/2)&(abs(self.car.y-self.y)<self.car.height+self.width/2):
            #This means the Hitboxes are colliding. However, the car's hitbox isn't accurate.
            if(abs(self.car.y-self.y)>abs(self.car.x-self.x)):
                #The car is mostly vertical to the block
                if(self.car.y-self.y<0):
                    #If the car is above the block
                    self.car.speed = 0.5*self.car.speed
                    self.yspeed += abs(self.car.speed)
                else:
                    #The car is below the block
                    self.car.speed = 0.5*(self.car.speed-self.yspeed)
                    self.yspeed += self.car.speed
                    self.car.angle = pi
                    #TODO: Proper Angle Changing
            else:
                #The car hit the side of the block
                if(self.car.x>self.x):
                    #The car hit the right side of the block
                    self.car.speed = 0.5*self.car.speed
                    self.xspeed += self.car.speed
                else:
                    self.car.speed = 0.5*self.car.speed
                    self.xspeed += -self.car.speed
        self.x += self.xspeed
        self.yspeed += self.car.height/self.FPS/10
        self.y += self.yspeed

if __name__ == "__main__":
    import racetrack
