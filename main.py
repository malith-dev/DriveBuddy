#!/usr/bin/python

import subprocess
import threading
import time
import detection 
import speed
import led
import buzzer
import drivers

stop_gps_thread = False
display = drivers.Lcd()

def run_detection_and_speed():
    led.green()
    buzzer.alert()
    display.lcd_display_string("WELCOME",1)
    #display.lcd_display_string("Starting",2)
    #display.lcd_display_string("        ",2)
    global stop_gps_thread
    while not stop_gps_thread:
        # Call your detection function
        current_class_name = detection.detect(**vars())
        # Process the detected class, check for speed limit signs, and speed from GPS
        if current_class_name and current_class_name == "50kmph":
            
            current_speed = speed.get_speed()
            #print("current speed is: ".current_speed)
            # Compare current_speed with the speed limit and trigger an alert if exceeded
            
libcamera_process = subprocess.Popen(
    'libcamera-vid -n -t 0 --width 640 --height 480 --framerate 5 --inline --listen -o tcp://127.0.0.1:8888',
    shell=True,
    start_new_session=True
)


# Start the GPS speed reading thread
gps_thread = threading.Thread(target=speed.get_speed)
gps_thread.start()

# Start the detection and speed tracking
run_detection_and_speed()

try:
    while True:
        pass
except KeyboardInterrupt:
    stop_gps_thread = True
    gps_thread.join()  # Wait for the GPS speed reading thread to finish
    libcamera_process.terminate()  # Terminate the libcamera-vid process when the program stops
    display.lcd_clear()
    

