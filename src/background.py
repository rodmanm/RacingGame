from math import sin, cos
class background:
    def __init__(self,pygame,xinit,yinit):
        self.x = xinit
        self.y = yinit
        self.Img = pygame.image.load(self.Img)
        self.width = self.Img.get_bounding_rect()[2]
        self.height = self.Img.get_bounding_rect()[3]
    x =  0
    y = 0
    angle = 0
    turning = 0
    Img = 'D:\\Racing\\Resources\\The_Skeld.jpg'
    width = 0
    currentWidth = 0
    height = 0
    currentHeight = 0
    speed = 0
    color = (40,44,52)
    def render(self,display, pygame):
        #rotated_image = pygame.transform.rotate(self.Img, self.angle*180/pi)
        display.blit(self.Img, (self.x,self.y))
    def update(self, car):
        self.speed += car.speed
        self.x -= self.speed*sin(car.angle)
        self.y -= self.speed*cos(car.angle)
        car.speed = 0
