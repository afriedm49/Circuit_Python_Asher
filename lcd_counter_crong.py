# Write your code here :-)
import board
import touchio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

touch = board.A1
touch2 = board.A2

countchange = touchio.TouchIn(touch)
signswitch = touchio.TouchIn(touch2)

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

positive = True
counter = 0




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

