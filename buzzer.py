import RPi.GPIO as GPIO
import time

# Set the GPIO mode and warning suppression
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the pin number
buzzer_pin = 21

# Setup the GPIO pin as an output
GPIO.setup(buzzer_pin, GPIO.OUT)

def buzzer():
    while True:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(0.5)

def buzzerStop():
    GPIO.output(buzzer_pin, GPIO.LOW)
    
def alert():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer_pin, GPIO.LOW)
    
    


