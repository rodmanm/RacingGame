from math import sin, cos
from PIL import ImageTk, Image

class Background:
    def __init__(self, pygame, xinit, yinit):
        self.x = xinit
        self.y = yinit
        self.Img = Image.open(self.Img)
        self.width = self.Img.width
        self.height = self.Img.height
    x = 0
    y = 0
    angle = 0
    turning = 0
    Img = '../Resources/ship.jpg'
    width = 0
    currentWidth = 0
    height = 0
    currentHeight = 0
    speed = 0
    color = (40, 44, 52)
    Enabled = False

    def render(self, display):
        # rotated_image = pygame.transform.rotate(self.Img, self.angle*180/pi)
        display.blit(self.Img, (self.x, self.y))

    def update(self, car):
        self.speed += car.speed
        self.x -= self.speed*sin(car.angle)
        self.y -= self.speed*cos(car.angle)
        car.speed = 0
