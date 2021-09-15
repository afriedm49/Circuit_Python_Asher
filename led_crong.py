# Asher's code - first metro project
import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it increase!")
led.brightness = .25
while True:

# generate some integers
    colors = range(0, 100, 5)
    negative = range(100, 0, -5)

    for r in colors:
        for g in colors:
            for b in negative:

                led.fill((r, g, b))
                time.sleep(0.01)