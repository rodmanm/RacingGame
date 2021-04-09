import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
from fallingBlock import FallingBlock
from car import Car
from background import Background
from Track import Track
import tkinter as tk
# TODO: Add space to fire mah lazors
# TODO: Port from pygame to turtle
# TODO: Add networking
# Initialize Global Values
black = (0, 0, 0)
white = (255, 255, 255)
FPS = 60
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Init game state
game = pygame.init()
clock = pygame.time.Clock()

# Configure Window
window = tk.Tk()
window.attributes('-fullscreen', True)
canvas = tk.Canvas(master=window, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)
gameDisplay = pygame.display.set_mode(size=(window.winfo_width(), window.winfo_height()),
                                      flags=pygame.RESIZABLE | pygame.SCALED, display=1, vsync=1)
pygame.display.set_caption('A bit Racey')
pygame.display.toggle_fullscreen()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window.winfo_width()/2), (window.winfo_height()/2))
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

    while True:
        for event in pygame.event.get():    # Event Loop
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
        fallingBlock.collide(car, window)
        if fallingBlock.y >= window.winfo_height():
            fallingBlock.reset(window)
        if (car.x > window.winfo_width() - car.width) or (car.x < 0):
            car.wrap(window)
        if (car.y > window.winfo_height() - car.height) or (car.y < 0):
            car.wrap(window)
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
car = Car(pygame, (window.winfo_width() * 0.45), (window.winfo_height() * 0.8))
Track = Track(window, car.width)
game_loop()
print("Good Game!")
# quit()
