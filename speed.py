import serial
import time
import drivers
import buzzer
import record

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
    global speedLimit
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        try:
            while True:
                # Read a line of data from the GPS module
                line = ser.readline().decode('utf-8').strip()
                #print(line)

                # Check if the line starts with "$GPRMC" (recommended minimum GPS data)
                if line.startswith("$GPRMC"):
                    # Process the line for GPS data
                    parts = line.split(',')
                    if len(parts) >= 7:
                        speed_knots = parts[7]
                        #print(speed_knots)
                        try:
                            speed_float = float(speed_knots)  # Try to convert to float
                            speed_kmph = speed_float * 1.852
                            rounded_speed = round(speed_kmph,0)
                            print(f"{rounded_speed} kmph")
                            display.lcd_display_string(str(rounded_speed)+" Kmph", 1)
                            if speedLimit and rounded_speed and rounded_speed >= 50.0:
                                buzzer.buzzerContinue()
                                record.write_to_csv(rounded_speed)
                            else:
                                buzzer.buzzerStop()
                            
                            #return speed_kmph
                        
                        except ValueError:
                            print(f"Invalid speed data: {speed_knots}")
                            display.lcd_display_string("Invalid Data", 1)
            return speed_kmph                
        except KeyboardInterrupt:
            display.lcd_clear()
            GPIO.cleanup()
            pass

if __name__ == "__main__":
    get_speed()



