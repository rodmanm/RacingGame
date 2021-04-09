import os
import pygame
import time
from fallingBlock import FallingBlock
from car import Car
from background import Background
from Track import Track

# TODO: Add space to fire mah lazors
# TODO: Port from pygame to turtle
# TODO: Add networking

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# Initialize Global Values
class Window:
    width = 1920
    height = 1080
black = (0, 0, 0)
white = (255, 255, 255)
FPS = 60
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# from os import system
# system("cd D:\\Racing")

# Init game state
game = pygame.init()
clock = pygame.time.Clock()

# Configure Window
gameDisplay = pygame.display.set_mode(size=(Window.width, Window.height), flags=pygame.RESIZABLE | pygame.SCALED,
                                      display=1, vsync=1)
pygame.display.set_caption('A bit Racey')

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((Window.width/2), (Window.height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def gameExit():
    pygame.quit()


def game_loop():
    # Initialize in game values

    while True:     # Event Loop
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

        # Calculate Updates
        if background.Enabled:
            background.update(car)
        if car.logging:
            car.tracer()
        car.update()
        fallingBlock.collide(car, Window)
        if fallingBlock.y >= Window.height:
            fallingBlock.reset(Window)
        if (car.x > Window.width - car.width) or (car.x < 0):
            car.wrap(Window)
        if (car.y > Window.height - car.height) or (car.y < 0):
            car.wrap(Window)
        # Check for collisions

        # Render Objects
        gameDisplay.fill(background.color)
        Track.render(pygame, gameDisplay)
        if background.Enabled:
            background.render(gameDisplay, pygame)
        fallingBlock.render(black, gameDisplay, pygame)
        car.render(gameDisplay, pygame)

        pygame.display.update()
        clock.tick(FPS)

background = Background(pygame, 0, 0)
fallingBlock = FallingBlock(FPS)
car = Car(pygame, (Window.width * 0.45), (Window.height * 0.8))
Track = Track(Window, car.width)
game_loop()
print("Good Game!")
# quit()
