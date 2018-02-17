import time
import RPi.GPIO as GPIO

ledpin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin , GPIO.OUT)
#GPIO.output(7 , GPIO.HIGH)
try:
    while True:
        GPIO.output(ledpin , GPIO.HIGH)
        print("On")
        time.sleep(1)
        GPIO.output(ledpin , GPIO.LOW)
        print("Off")
        time.sleep(1)
except KeyboardInterrupt:
        print("stopped")
        GPIO.cleanup()
