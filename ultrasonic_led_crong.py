# Distance Sensor

import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D6)

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = .25
color = str
cm = 0

while True:
    try:
        cm = round(sonar.distance)
        if cm < 33:
            blue = simpleio.map_range(sonar.distance, 5, 33, 0, 255)
            green = simpleio.map_range(sonar.distance, 5, 33, 255, 0)
            g = int(green)
            b = int(blue)
            print(cm)
            led.fill((0, g, b))
        if cm <= 66 and cm >= 33:
            blue = simpleio.map_range(sonar.distance, 33, 66, 255, 0)
            red = simpleio.map_range(sonar.distance, 33, 66, 0, 255)
            r = int(red)
            b = int(blue)
            print(cm)
            led.fill((r, 0, b))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)