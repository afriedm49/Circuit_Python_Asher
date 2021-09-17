#180 degrees servo code

from adafruit_motor import servo
import time
import pwmio
import board
import pulseio

pwm = pulseio.PWMOut(board.D8, frequency=50)


Spinner = servo.Servo(pwm, min_pulse = 750, max_pulse = 2250)

while True:
    Angle = Spinner.angle

    Spinner.angle = 0
    time.sleep(1.2)
    print(Angle)
    Spinner.angle = 180
    time.sleep(1.2)
    print(Angle)