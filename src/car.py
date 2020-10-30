from math import sin, cos, pi
class car:
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
    Img = 'D:\\Racing\\Resources\\racecar.png'
    width = 0
    currentWidth = 0
    height = 0
    currentHeight = 0
    speed = 0
    logs = []
    logging = False
    tracerColor = (128,128,0)
    def update(self):
        self.angle += self.turning/(10)
        self.x += self.speed*sin(self.angle)
        self.y += self.speed*cos(self.angle)
        self.currentWidth = abs(self.width*cos(self.angle))+abs(self.height*sin(self.angle))
        self.currentHeight = abs(self.width*sin(self.angle))+abs(self.height*cos(self.angle))


    def render(self,display, pygame):
        rotated_image = pygame.transform.rotate(self.Img, self.angle*180/pi)
        display.blit(rotated_image, (self.x,self.y))
        if len(self.logs)>10 and self.logging:
            pygame.draw.polygon(display, self.tracerColor, self.logs)

    def wrap(self, display):
        if(self.x+self.currentWidth>=display.width):
            self.x = 0
        elif(self.x<=0):
            self.x = display.width - self.currentWidth
        elif(self.y+self.currentHeight>=display.height):
            self.y = 0
        elif(self.y <= 0):
            self.y = display.height - self.currentHeight
    def tracer(self):
        self.logs.append((self.x,self.y))
