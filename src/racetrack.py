import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#Initialize Global Values
class display:
    width = 1600
    height = 900
black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

import pygame
import time
import fallingBlock
from car import car
from background import background
from Track import Track
# from os import system
# system("cd D:\\Racing")

#Init game state
game = pygame.init()
clock = pygame.time.Clock()

#Configure Window
#gameDisplay = pygame.display.set_mode((display.width,display.height))
gameDisplay = pygame.display.set_mode(size = (display.width,display.height),flags = pygame.RESIZABLE|pygame.SCALED, display = 1, vsync=1)
pygame.display.set_caption('A bit Racey')



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display.width/2),(display.height/2))
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
                if event.key == pygame.K_l:
                    car.logging = True
                if event.key == pygame.K_LEFT:
                    car.turning = 1
                elif event.key == pygame.K_RIGHT:
                    car.turning = -1
                if event.key == pygame.K_UP:
                    car.speed = -15
                elif event.key == pygame.K_DOWN:
                    car.speed = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car.turning = 0    #x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    car.speed = 0
                    background.speed = 0
                if event.key == pygame.K_l:
                    car.logging = False


        #Calculate Updates
        #background.update(car)
        if(car.logging):
            car.tracer()
        car.update()
        fallingBlock.collide(car)
        if(fallingBlock.y >= display.height):
            fallingBlock.reset(display)
        if (car.x > display.width - car.width) or (car.x < 0):
                car.wrap(display)
        if (car.y > display.height - car.height) or (car.y < 0):
                car.wrap(display)
        #Check for collisions

        #Render Objects
        gameDisplay.fill(background.color)
        Track.render(pygame, gameDisplay)
        fallingBlock.render(black,gameDisplay, pygame)
        #background.render(gameDisplay, pygame)
        car.render(gameDisplay, pygame)

        pygame.display.update()
        clock.tick(60)

#background = background(pygame,0,0)
fallingBlock = fallingBlock.fallingBlock()
car = car(pygame,(display.width * 0.45),(display.height * 0.8))
Track = Track(display, car.width)
game_loop()
print("Good Game!")
#quit()
