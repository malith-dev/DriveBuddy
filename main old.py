import multiprocessing
import time

# Import your traffic sign detection and speed tracking scripts
import detection
import speed 

# Create queues for inter-process communication
detection_queue = multiprocessing.Queue()
speed_queue = multiprocessing.Queue()

# Define a function to monitor results and provide an alert
def monitor_traffic_and_speed():
    while True:
        # Check the traffic sign detection results
        if not detection_queue.empty():
            detection_class = detection_queue.get()

            # Check the speed tracking results
            if not speed_queue.empty():
                current_speed = speed_queue.get()

                # Check if the speed limit is detected
                if detection_class == 'speed_limit':
                    # Check if the speed exceeds the limit
                    speed_limit = 60  # Replace with the appropriate speed limit
                    if current_speed > speed_limit:
                        print(f"Speed limit exceeded: {current_speed} km/h")
                        # Provide an alert here (e.g., sound an alarm)

# Create processes for traffic sign detection and speed tracking
traffic_sign_process = multiprocessing.Process(target=detection.detect, args=(detection_queue,))
speed_tracking_process = multiprocessing.Process(target=speed.get_speed, args=(speed_queue,))

if __name__ == '__main__':
    # Start the processes
    traffic_sign_process.start()
    speed_tracking_process.start()

    # Start the monitor function
    monitor_traffic_and_speed()
