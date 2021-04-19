# khondicker
from ball import Ball
from car import Car
from turtle import Screen, mainloop
from Fish import Fish
from goal import Goal
from sys import exit

class Soccer:
    def __init__(self, xMax, yMax):
        self.__xMax = xMax
        self.__yMax = yMax
        self.__mainWin = Screen()
        self.__mainWin.bgcolor('light blue')
        self.__mainWin.setup(width=1.0, height=1.0, startx=None, starty=None)
        self.__mainWin.setworldcoordinates(0, 0, self.__xMax, self.__yMax)
        self.objects = []
        self.movement()

    def play(self):
        self.objects.append(Car(0, 7, self.__xMax, self.__yMax))
        self.objects.append(Goal())
        for a in Car.allCars:
            a.up()
            a.goto(400, 300)
        self.__mainWin.onkey(self.placeBall, "p")
        self.__mainWin.onkey(self.placeBall, "b")   # B for Ball
        self.__mainWin.onclick(self.placeFish, 1, None)
        self.__mainWin.onkey(exit, "c")
        self.__mainWin.listen()
        mainloop()

    def placeBall(self):
        self.objects.append(Ball(0, self.__xMax, self.__yMax))

    def placeFish(self, x, y):
        self.objects.append(Fish(10, self.__xMax, self.__yMax, x, y))

    def movement(self):
        for i in self.objects:
            i.checkCollisions()
            i.move()
        if len(self.objects) < 4:
            self.__mainWin.ontimer(self.movement, 2)
        else:
            self.movement()

if __name__ == '__main__':
    game = Soccer(800, 600)
    game.play()
