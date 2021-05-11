import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#Initialize Global Values
class window:
    width = 1600
    height = 900
black = (0,0,0)
white = (255,255,255)
FPS = 60
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

import pygame
import time
from fallingBlock import fallingBlock
from car import car
from background import background
from Track import Track

#Init game state
game = pygame.init()
clock = pygame.time.Clock()

#Configure Window
gameDisplay = pygame.display.set_mode(size = (window.width,window.height),flags = pygame.RESIZABLE|pygame.SCALED, display = 0, vsync=1)
pygame.display.set_caption('A bit Racey')



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window.width/2),(window.height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def gameExit():
    pygame.quit()


def game_loop():
    #Initialize in game values
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit()

            # Accept Inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameExit()
                    return 0
                car.inputs(event.key, pygame)
            if event.type == pygame.KEYUP:
                car.inputsEnd(event.key, pygame)
                if event == pygame.K_UP or event == pygame.K_DOWN:
                    background.speed = 0

        if clock.get_time()%10 == 1:
            #TODO: add more block spawning!
            pass

        #Calculate Updates
        if background.Enabled:
            background.update(car)
        if(car.logging):
            car.tracer()
        car.update()
        fallingBlock.collide(car)
        if (car.x > window.width - car.width) or (car.x < 0):
                car.wrap(window)
        if (car.y > window.height - car.height) or (car.y < 0):
                car.wrap(window)
        #Render Objects
        gameDisplay.fill(background.color)
        for i in objects:
            i.render(pygame, gameDisplay)

        pygame.display.update()
        clock.tick(FPS)
objects = []
background = background(pygame,0,0)
fallingBlock = fallingBlock(FPS, window)
car = car(pygame,(window.width * 0.45),(window.height * 0.8))
Track = Track(window, car.width)
if background.Enabled:
    objects.append(background)
objects.append(fallingBlock)
objects.append(car)
objects.append(Track)
game_loop()
print("Good Game!")
#quit()
