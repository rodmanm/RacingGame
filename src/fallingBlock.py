import random
class fallingBlock():
    #Create object
    x = 300
    y = -600
    maxspeed = 10
    width = 100
    yspeed = 7
    height = 100
    def reset(self, display):
        self.x = random.randrange(self.width, display.width-self.width)
        self.y = -self.height
        self.yspeed = random.randrange(3, self.maxspeed)
    def render(self, color, window, pygame):
        pygame.draw.rect(window, color, [self.x, self.y, self.width, self.height])
    def collide(self, car):
        if(car.x-self.x<self.width+car.width)&(car.y-self.y<self.height+car.height):
            print(1)
            car.speed = 0.5*car.speed
            self.yspeed += car.speed
        self.y += self.yspeed
        if(fallingBlock.y >= display.height) | (fallingBlock.y <= 0):
            fallingBlock.reset(display)
