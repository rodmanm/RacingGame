from PIL.Image import *
from os import listdir, system
for i in listdir("Resources"):
    img = open("Resources/" + i)
    new = i.replace(".jpg", ".gif").replace(".png", ".gif")
    img.save("Resources/" + new)
    system("del Resources/" + i)
