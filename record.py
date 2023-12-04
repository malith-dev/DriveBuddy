
import csv
import os
import datetime

# Function to write records to a CSV file
def write_to_csv(speed):
    csv_file = 'speed_records.csv'

    # Check if the CSV file exists or create a new one
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ['Timestamp', 'Speed']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is newly created
        if not file_exists:
            writer.writeheader()

        # Generate current timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Write speed record with timestamp to CSV
        writer.writerow({'Timestamp': timestamp, 'Speed': speed})
