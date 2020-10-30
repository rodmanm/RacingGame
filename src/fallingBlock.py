import random
class fallingBlock():
    #Create object
    x = 300
    y = 0
    maxspeed = 10
    width = 100
    yspeed = 7
    xspeed = 0
    height = 100
    def reset(self, display):
        self.x = random.randrange(self.width, display.width-self.width)
        self.y = -self.height
        self.xspeed = 0
        self.yspeed = random.randrange(3, self.maxspeed)
    def render(self, color, window, pygame):
        pygame.draw.rect(window, color, [self.x, self.y, self.width, self.height])
    def collide(self, car, window):
        if(self.y >= window.height) | (self.y < -self.height):
            self.reset(window)
        #if(car.x-self.x<self.width+car.width)&(car.y-self.y<self.height+car.height):
        if(abs(car.x-self.x)<car.width+self.width/2)&(abs(car.y-self.y)<car.height+self.width/2):
            #This means the Hitboxes are colliding. However, the car's hitbox isn't accurate.
            if(abs(car.y-self.y)>abs(car.x-self.x)):
                #The car is mostly vertical to the block
                if(car.y-self.y<0):
                    #If the car is above the block
                    car.speed = 0.5*car.speed
                    self.yspeed += abs(car.speed)
                else:
                    #The car is below the block
                    car.speed = 0.5*car.speed
                    self.yspeed += car.speed
            else:
                #The car hit the side of the block
                if(car.x>self.x):
                    #The car hit the right side of the block
                    car.speed = 0.5*car.speed
                    self.xspeed += car.speed
                else:
                    car.speed = 0.5*car.speed
                    self.xspeed += -car.speed
        self.x += self.xspeed
        self.y += self.yspeed
