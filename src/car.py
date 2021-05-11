from math import sin, cos, pi
class car:
    def __init__(self,pygame,window, xinit=0.45,yinit=0.8):
        self.window = window
        self.x = xinit*self.window.width
        self.y = yinit*self.window.height
        self.Img = 'D:\\Racing\\Resources\\racecar.png'
        self.Img = pygame.image.load(self.Img)
        self.width = self.Img.get_bounding_rect()[2]
        self.height = self.Img.get_bounding_rect()[3]
        self.angle = 0
        self.turning = 0
        self.width = 0
        self.currentWidth = 0
        self.height = 0
        self.currentHeight = 0
        self.speed = 0
        self.accelerating = 0
        self.logs = []
        self.logging = False
        self.tracerColor = (128,128,0)
        self.topSpeed = 25
    def update(self):
        if(self.accelerating):
            if(abs(self.speed) < self.topSpeed):
                self.speed += self.accelerating
        elif(self.speed == 0):
            pass
        else:
            self.speed -= round(500*self.speed)/1000
        self.angle += self.turning/(10)
        self.x += self.speed*sin(self.angle)
        self.y += self.speed*cos(self.angle)
        self.currentWidth = abs(self.width*cos(self.angle))+abs(self.height*sin(self.angle))
        self.currentHeight = abs(self.width*sin(self.angle))+abs(self.height*cos(self.angle))
        if (self.x > self.window.width - self.width) or (self.x < 0):
                self.wrap()
        if (self.y > self.window.height - self.height) or (self.y < 0):
                self.wrap()


    def render(self, pygame, display):
        rotated_image = pygame.transform.rotate(self.Img, self.angle*180/pi)
        display.blit(rotated_image, (self.x,self.y))
        if len(self.logs)>10 and self.logging:
            pygame.draw.polygon(display, self.tracerColor, self.logs)

    def inputs(self, event, pygame):
        if event == pygame.K_l:
            self.logging = True
        if event == pygame.K_LEFT:
            self.turning = 1
        elif event == pygame.K_RIGHT:
            self.turning = -1
        if event == pygame.K_UP:
            self.accelerating = -1
        elif event == pygame.K_DOWN:
            self.accelerating = 1

    def inputsEnd(self, event, pygame):
        if event == pygame.K_LEFT or event == pygame.K_RIGHT:
            self.turning = 0    #x_change = 0
        if event == pygame.K_UP or event == pygame.K_DOWN:
            self.accelerating = 0
        if event == pygame.K_l:
            self.logging = False

    def wrap(self):
        if(self.x+self.currentWidth>=self.window.width):
            self.x = 0
        elif(self.x<=0):
            self.x = self.window.width - self.currentWidth
        elif(self.y+self.currentHeight>=self.window.height):
            self.y = 0
        elif(self.y <= 0):
            self.y = self.window.height - self.currentHeight
    def tracer(self):
        self.logs.append((self.x,self.y))
