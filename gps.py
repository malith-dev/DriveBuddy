import serial

# Define the serial port and baud rate
serial_port = 'COM5'  # Replace with the correct COM port on your PC
baud_rate = 9600

# Open the serial port
# with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
#     try:
#         while True:
#             # Read a line of data from the GPS module
#             line = ser.readline().decode('utf-8').strip()
            
#             # Check if the line starts with "$GPRMC" (recommended minimum GPS data)
#             if line.startswith("$GPRMC"):
#                 # Process the line for GPS data
#                 parts = line.split(',')
#                 if len(parts) >= 7:
#                     speed_knots = float(parts[7])  # Speed in knots
#                     speed_mph = speed_knots * 1.15078  # Convert knots to mph
#                     speed_kph = speed_knots * 1.852  # Convert knots to km/h
                    
#                     #print(f"Speed (knots): {speed_knots}")
#                     print(f"Speed (mph): {speed_mph}")
#                     print(f"Speed (km/h): {speed_kph}")

#     except KeyboardInterrupt:
#         pass

def get_speed():
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        try:
            while True:
                # Read a line of data from the GPS module
                line = ser.readline().decode('utf-8').strip()
                
                # Check if the line starts with "$GPRMC" (recommended minimum GPS data)
                if line.startswith("$GPRMC"):
                    # Process the line for GPS data
                    parts = line.split(',')
                    if len(parts) >= 7:
                        speed_knots = float(parts[7])  # Speed in knots
                        speed_mph = speed_knots * 1.15078  # Convert knots to mph
                        speed_kph = speed_knots * 1.852  # Convert knots to km/h
                        
                        #print(f"Speed (knots): {speed_knots}")
                        # print(f"Speed (mph): {speed_mph}")
                        # print(f"Speed (km/h): {speed_kph}")
                        return speed_kph

        except KeyboardInterrupt:
            pass

while True:
    print(get_speed())

    
