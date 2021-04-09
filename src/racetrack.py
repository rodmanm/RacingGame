import time
from fallingBlock import FallingBlock
from car import Car
from background import Background
from Track import Track
import tkinter as tk
# TODO: Add space to fire mah lazors
# TODO: Add networking
# Initialize Global Values

# Init game state
window = tk.Tk()
window.attributes('-fullscreen', True)
window.FPS = 60
canvas = tk.Canvas(master=window, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

def text_objects(text, font):
    textSurface = font.render(text, True, 'black')
    return textSurface, textSurface.get_rect()

def message_display(text):
    print(text)
    # largeText = pygame.font.Font('freesansbold.ttf', 115)
    # TextSurf, TextRect = text_objects(text, largeText)
    # TextRect.center = ((window.winfo_width()/2), (window.winfo_height()/2))
    # gameDisplay.blit(TextSurf, TextRect)

def crash():
    message_display('You Crashed')

def gameExit():
    window.FPS = 0

def controlsPressed(event):
    if event.char == 'c':
        gameExit()
        return 0
    car.inputs(event.keysym)

def controlsReleased(event):
    car.inputsEnd(event.keysym)
    background.speed = 0

def game_loop():
    realFPS = 0.01
    while window.FPS:
        window.update_idletasks()
        startTime = time.time()
        # Calculate Updates
        if background.Enabled:
            background.update(car)
        car.update(window)
        fallingBlock.collide(car, window)
        # Render Objects
        # Track.render(canvas)
        if background.Enabled:
            background.render(canvas)
        fallingBlock.render(canvas, realFPS)
        car.render(canvas)
        window.update()

        realFPS = 1/(time.time() - startTime + .000001)     # Small Epsilon to avoid /0
        if realFPS > window.FPS:
            time.sleep(1 / (realFPS - window.FPS))

window.bind("<KeyPress>", controlsPressed)
window.bind("<KeyRelease>", controlsReleased)
background = Background(canvas, 0, 0)
fallingBlock = FallingBlock(canvas, window.FPS)
car = Car(canvas)
Track = Track(window, car.width)
game_loop()
print("Good Game!")
# quit()
