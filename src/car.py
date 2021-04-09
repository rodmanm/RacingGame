from math import sin, cos, pi
from PIL import ImageTk, Image
class Car:
    def __init__(self, canvas, xinit, yinit):
        self.x = xinit
        self.y = yinit
        self.Img = Image.open(self.Img)
        self.width = self.Img.width
        self.height = self.Img.height
        tkImage = ImageTk.PhotoImage(self.Img)
        self.icon = canvas.create_image(self.x, self.y, image=tkImage)
    x = 0
    y = 0
    angle = 0
    turning = 0
    Img = '../Resources/racecar.png'
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

    def update(self, window):
        if self.accelerating:
            if abs(self.speed) < self.topSpeed:
                self.speed += self.accelerating
        elif self.speed == 0:
            pass
        else:
            self.speed -= round(500*self.speed)/1000
        if self.logging:
            self.tracer()
        self.angle += self.turning/10
        self.x += self.speed*sin(self.angle)
        self.y += self.speed*cos(self.angle)
        self.currentWidth = abs(self.width*cos(self.angle))+abs(self.height*sin(self.angle))
        self.currentHeight = abs(self.width*sin(self.angle))+abs(self.height*cos(self.angle))
        if (self.x > window.winfo_width() - self.width) or (self.x < 0):
            self.wrap(window)
        if (self.y > window.winfo_height() - self.height) or (self.y < 0):
            self.wrap(window)

    def render(self, canvas):
        rotated_image = self.Img.rotate(self.angle*180/pi)
        tkImage = ImageTk.PhotoImage(rotated_image)
        # canvas.configure(self.icon, image=tkImage)
        # if len(self.logs) > 10 and self.logging:
        #     pygame.draw.polygon(display, self.tracerColor, self.logs)
        # TODO: FIX THIS

    def inputs(self, key):
        if key == 'l':
            self.logging = True
        if key == 'Left':
            self.turning = 1
        elif key == 'Right':
            self.turning = -1
        if key == 'Up':
            self.accelerating = -1
        elif key == 'Down':
            self.accelerating = 1

    def inputsEnd(self, key):
        if key == 'Left' or key == 'Right':
            self.turning = 0    # x_change = 0
        if key == 'Up' or key == 'Down':
            self.accelerating = 0
        if key == 'l':
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
