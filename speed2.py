import serial
import random
import time
import drivers
import buzzer
import RPi.GPIO as GPIO

# Define the serial port and baud rate
serial_port = '/dev/ttyS0'  # Replace with the correct COM port on your PC
baud_rate = 9600
display = drivers.Lcd()
speedLimit = False
exceed = False

def set_speed_limit(value):
    global speedLimit
    speedLimit = value

def get_speed():
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        try:
            while True:
                # Read a line of data from the GPS module
                random_value = random.randint(0,100)
                time.sleep(0.5)
                #print(line)

                # Check if the line starts with "$GPRMC" (recommended minimum GPS data)
                # Process the line for GPS data
                
                #print(speed_knots)
                try:
                    
                    print(random_value)
                    display.lcd_display_string(str(random_value), 1)
                    if random_value >= 50.0:
                        buzzer.buzzerContinue()
                    else:
                        buzzer.buzzerStop()
                            
                    #return speed_kmph
                        
                except ValueError:
                    print(f"Invalid speed data: {speed_knots}")
                    display.lcd_display_string("Invalid Data", 1)
                            
        except KeyboardInterrupt:
            display.lcd_clear()
            GPIO.cleanup()
            
            pass

if __name__ == "__main__":
    get_speed()



