from pathlib import Path
from pyboy import PyBoy


pyboy = PyBoy("tobudx.gb",window="SDL2")
print("cartridge",pyboy.cartridge_title)

while pyboy.tick():
    pyboy.button("left")
    #pyboy.button("up")


pyboy.stop()








