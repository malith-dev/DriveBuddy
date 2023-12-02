import RPi.GPIO as GPIO
import time

# Set the GPIO mode and warning suppression
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the pin number
green_pin = 20
red_pin = 16

# Setup the GPIO pin as an output
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)

def green():
    GPIO.output(green_pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(green_pin, GPIO.LOW)
    
def off():
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(red_pin, GPIO.LOW)
    


