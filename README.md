# Circuit Python
### This is my engineering notebook for Junior Year

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Led_Blink_Remix](#Led_Blink_Remix)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [LedUltrasonic](#LedUltrasonic)
* [LCD](#LCD)

---

## Led_Blink_Remix

### Description and Code
* The code starts by setting a range from 0 to 100, and another range from 100 to 0.
* Every 0.01 seconds, the blue value changes by negative 5 from 100 to 0
* Each time the blue value reaches 0, the green value changes by positive 5 until it reaches 100
* Each time the green value reaches 100, the red value increases by 5 until it reaches 100.
* After 400 loops of the blue value going down to 0, the entire loop restarts.
* There is delay on each value change (It takes more than 0.01 seconds for each blue to decrease by 5)
I coded this on Mu.

``` python
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


---

### Wiring
The Metro plugs directly into the computer with USB.

### Evidence
<img src="Metro_Led.jpg" alt="ServoGif" width="400" height="200"/>

[Source](https://www.microcenter.com/product/503912/adafruit-industries-metro-m0-express)

### Reflection
* RGB is the integer values for red green and blue, in that order.
* Make sure that there are correct indentations when using if and for statements (press tab whenever putting a loop within a loop).

## CircuitPython_Servo

### Description & Code

This code makes the servo turn 180 degrees, wait 1.2 seconds, and then move back, and wait another 1.2 seconds.

[Link to full code](https://github.com/afriedm49/Circuit_Python_Asher/blob/main/servo_crong.py)

``` python
while True:
    Angle = Spinner.angle
    
    Spinner.angle = 0
    time.sleep(1.2)
    print(Angle)
    Spinner.angle = 180
    time.sleep(1.2)
    print(Angle)

```

### Evidence

<img src="ServoGif.gif" alt="ServoGif" width="400" height="200"/>

[Link to full video](https://github.com/afriedm49/Circuit_Python_Asher/blob/main/ServoVid.mp4)

### Wiring

<img src="servoCircuit.png" alt="ServoCircuit" width="400" height="200"/>
Credit:

[sfunk02](https://github.com/sfunk02/CircuitPython/blob/main/Images/servoCircuit.png)

### Reflection

* I didn't understand how the pwm function worked until finding [this website](https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html)
* I had a lot of mistakes working on it, including file managment, syntax, and missing lines. Learn to correctly format Python before, and put your files in the correct folder beforehand.

## LedUltrasonic

### Description & Code

This code makes an LED fade from green to blue to red, based on its distance from a surface:

``` python
if cm < 33:
            blue = simpleio.map_range(sonar.distance, 5, 33, 0, 255)
            green = simpleio.map_range(sonar.distance, 5, 33, 255, 0)
            g = int(green)
            b = int(blue)
            print(cm)
            led.fill((0, g, b))
```
[Full code](https://github.com/afriedm49/Circuit_Python_Asher/blob/main/ultrasonic_led_crong.py)

### Evidence
<img src="https://github.com/afriedm49/Circuit_Python_Asher/blob/main/Ultrasonic%20Gif.gif" alt="UltrasonicGif" width="400"/>

### Wiring
<img src="https://github.com/sfunk02/CircuitPython/blob/main/Images/ultrasonicCircuit.png" alt="UltrasonicCircuit" width="400" height="200"/>
Credit: 

[sfunk02](https://github.com/sfunk02/CircuitPython/blob/main/Images/ultrasonicCircuit.png)

### Reflection

* I had a couple syntax problems, and didn't get the serial monitor to work for a while. Before completing the code, use the auto-checker to see if the syntax is formatted correctly.
* I started off with a faulty sensor, which wasted a good amount of time, so it is important to check each thing that could be faulty in order to figure out which piece is the problem
* I learned how to use the round function as well, to tidy up the numbers. Round() turns a float into an integer, so it is very helpful for a clean code.

## LCD

### Description & Code
```
while True:
        if signswitch.value:
            positive = not positive
            if positive == True:
                lcd.print("Positive")
                time.sleep(1)
                lcd.clear()
            if positive == False:
                lcd.print("Negative")
                time.sleep(1)
                lcd.clear()

        if positive == True:
            if countchange.value:
                counter += 1
                lcd.print(str(counter))
                time.sleep(1)
                lcd.clear()
        if positive == False:
            if countchange.value:
                counter -= 1
                lcd.print(str(counter))
                time.sleep(1)
                lcd.clear()
```
### Evidence
### Wiring
### Reflection

## Photointerrupter

### Description and Code
```
import time

initial = time.monotonic()  # Time in seconds since power on

while True:
    now = time.monotonic()
    if now - initial > 4:  # If 3 milliseconds elapses
        print("I have been interrupted" + str(interrupts) + "time")
    else:
        initial = now

#### Code credit to https://github.com/gventre04/CircuitPython

from digitalio import DigitalInOut, Direction, Pull

import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0
interval = 4        # sets interal between each print in seconds

photo = False
state = False

max = interval
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
        counter += 1             # counts each time the photointerrupter is interrupted
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))  # prints counter value
        max = time.time() + interval
        counter = 0

```
### Evidence
### Wiring
### Reflection

## RGB_Classes_LED
### Description & Code
```

```
### Evidence

[Video](RGBClasses.mov)

### Wiring
### Reflection
* Using classes can help greatly when it comes to organization, as well as creating new instances of objects for efficiency.
* It is important to note that you cannot call a function using a variable to replace the function name. For instance: the function blinky.cyan, cannot be called as blinky.color, if you want to replace a certain color method in the function.



