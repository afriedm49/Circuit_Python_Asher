# Engineering3
This is my engineering notebook for Junior Year

## First Code
_____________________________________________
import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it increase!")
led.brightness = .25
while True:

    colors = range(0, 100, 5)
    negative = range(100, 0, -5)
   
    for r in colors:
        for g in colors:
            for b in negative:
        
                led.fill((r, g, b))
                time.sleep(0.01)
_____________________________________________

### What does this code do?
* The code starts by setting a range from 0 to 100, and another range from 100 to 0.
* Every 0.01 seconds, the blue value changes by negative 5 from 100 to 0
* Each time the blue value reaches 0, the green value changes by positive 5 until it reaches 100
* Each time the green value reaches 100, the red value increases by 5 until it reaches 100.
* After 400 loops of the blue value going down to 0, the entire loop restarts.
* It takes more than 0.01 seconds for each value to change, so it the time is longer than it says in the code.
