from math import sin, cos, pi
from PIL import Image, ImageTk
from tkinter import NW, PhotoImage, TclError
from turtle import RawTurtle, TurtleScreen
class Car(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.screen = TurtleScreen(canvas)
        self.x = canvas.winfo_width() * 0.45
        self.y = canvas.winfo_height() * 0.8
        self.turtle = RawTurtle(canvas)
        if self.Img not in self.getscreen().getshapes():
            self.getscreen().addshape(self.Img)
        self.turtle.shape(self.Img)
        self.width = self.Img.width()
        self.height = self.Img.height()

        # self.image = canvas.create_image(self.x, self.y, anchor=NW, image=self.Img)
    Img = 'Resources/racecar.gif'
    x = 0
    xspeed = 0
    y = 0
    yspeed = 0
    angle = 0
    turning = 0
    width = 10
    currentWidth = 0
    height = 10
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
        self.xspeed = self.speed*sin(self.angle)
        self.yspeed = self.speed*cos(self.angle)
        self.x += self.speed*sin(self.angle)
        self.y += self.speed*cos(self.angle)
        self.currentWidth = abs(self.width*cos(self.angle))+abs(self.height*sin(self.angle))
        self.currentHeight = abs(self.width*sin(self.angle))+abs(self.height*cos(self.angle))
        if self.x > window.winfo_width() - self.width:
            # self.wrap(window)
            self.x = window.winfo_width() - self.width
        elif self.x < 0:
            self.x = 0
        if self.y > window.winfo_height() - self.height:
            # self.wrap(window)
            self.y = window.winfo_height() - self.height
        elif self.y < 0:
            self.y = 0

    def render(self, canvas):
        # rotated_image = self.Img.rotate(self.angle*180/pi)
        # tkImage = PhotoImage(rotated_image)
        # canvas.move(self.image, self.xspeed, self.yspeed)
        self.turtle.setheading(self.angle*180/pi)
        self.turtle.forward(-self.speed)

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
            self.angle - pi
        elif self.x <= 0:
            self.xspeed = -self.xspeed
            self.angle - pi
        elif self.y + self.currentHeight >= window.winfo_height():
            self.y = 0
            self.angle - pi
        elif self.y <= 0:
            self.y = window.winfo_height() - self.currentHeight
            self.angle = self.angle - pi

    def tracer(self):
        self.logs.append((self.x, self.y))
