import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, change to other values if necessary

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:
        break

    # Process and display the frame
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press the 'Esc' key to exit
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()