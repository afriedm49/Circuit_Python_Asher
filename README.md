# Circuit Python
This is my engineering notebook for Junior Year, where I put documents of code.

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Led_Blink_Remix](#Led_Blink_Remix)
* [CircuitPython_Servo](#CircuitPython_Servo)
---

## Led_Blink_Remix

### Code
I coded this on Mu.

```
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
```

### What does this code do?
* The code starts by setting a range from 0 to 100, and another range from 100 to 0.
* Every 0.01 seconds, the blue value changes by negative 5 from 100 to 0
* Each time the blue value reaches 0, the green value changes by positive 5 until it reaches 100
* Each time the green value reaches 100, the red value increases by 5 until it reaches 100.
* After 400 loops of the blue value going down to 0, the entire loop restarts.
* There is delay on each value change (It takes more than 0.01 seconds for each blue to decrease by 5)
---
## CircuitPython_Servo

### Description & Code

This code makes the servo turn 180 degrees, by moving by 1 degree each step.

```python
Code goes here
#180 degrees servo code

from adafruit_motor import servo
import time
import pwmio
import board
import pulseio

pwm = pulseio.PWMOut(board.D8, frequency=50)


Spinner = servo.Servo(pwm, min_pulse = 750, max_pulse = 2250)

while True:
    if angle < 180:
        for degree in range(0, 180, 1)
        Spinner.angle = degree
        print(angle)
    else:
        Spinner.angle = 0
```

### Evidence

### Wiring

### Reflection

The coding was somewhat difficult to figure out at first. I didn't understand how the pwm function worked. I had a lot of mistakes working on it, including file managment, syntax, and missing lines.
