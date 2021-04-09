from math import sin, cos, pi
class Car:
    def __init__(self, pygame, xinit, yinit):
        self.x = xinit
        self.y = yinit
        self.Img = pygame.image.load(self.Img)
        self.width = self.Img.get_bounding_rect()[2]
        self.height = self.Img.get_bounding_rect()[3]
    x = 0
    y = 0
    angle = 0
    turning = 0
    Img = 'Resources\\racecar.png'
    width = 0
    currentWidth = 0
    height = 0
    currentHeight = 0
    speed = 0
    accelerating = 0
    logs = []
    logging = False
    tracerColor = (128, 128, 0)
    topSpeed = 25

    def update(self):
        if self.accelerating:
            if abs(self.speed) < self.topSpeed:
                self.speed += self.accelerating
        elif self.speed == 0:
            pass
        else:
            self.speed -= round(500*self.speed)/1000
        self.angle += self.turning/10
        self.x += self.speed*sin(self.angle)
        self.y += self.speed*cos(self.angle)
        self.currentWidth = abs(self.width*cos(self.angle))+abs(self.height*sin(self.angle))
        self.currentHeight = abs(self.width*sin(self.angle))+abs(self.height*cos(self.angle))

    def render(self, display, pygame):
        rotated_image = pygame.transform.rotate(self.Img, self.angle*180/pi)
        display.blit(rotated_image, (self.x, self.y))
        if len(self.logs) > 10 and self.logging:
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
            self.turning = 0    # x_change = 0
        if event == pygame.K_UP or event == pygame.K_DOWN:
            self.accelerating = 0
        if event == pygame.K_l:
            self.logging = False

    def wrap(self, window):
        if self.x + self.currentWidth >= window.winfo_width():
            self.x = 0
        elif self.x <= 0:
            self.x = window.winfo_width() - self.currentWidth
        elif self.y + self.currentHeight >= window.winfo_height():
            self.y = 0
        elif self.y <= 0:
            self.y = window.winfo_height() - self.currentHeight

    def tracer(self):
        self.logs.append((self.x, self.y))
