#!/usr/bin/python3  
 
import RPi.GPIO as GPIO  
import os
import time
import drivers

GPIO.setmode(GPIO.BCM)
display = drivers.Lcd()

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

print ("Waiting for falling edge on port 16")
display.lcd_display_string("Press the button",1)
display.lcd_display_string("To start",2)

# now the program will do nothing until the signal on port 23   
# starts to fall towards zero. This is why we used the pullup  
# to keep the signal high and prevent a false interrupt

try:
    while True:
        input_state = GPIO.input(16)
        if input_state == False:
        
            print('Button Pressed')
            display.lcd_clear()
            os.system('cd /home/pi/FYP && python3 main.py')
            #subprocess.call(speed.get_speed())
        

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)