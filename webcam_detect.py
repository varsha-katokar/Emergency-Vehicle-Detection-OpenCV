import cv2
import numpy as np

# Start the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for faster processing (optional)
    frame = cv2.resize(frame, (640, 480))

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define RED range
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    # Define BLUE range
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Count number of pixels for each color
    red_pixels = cv2.countNonZero(red_mask)
    blue_pixels = cv2.countNonZero(blue_mask)

    # Thresholds to decide detection
    threshold = 1000  # you can tune this

    text = "No Emergency Light Detected"
    if red_pixels > threshold and blue_pixels > threshold:
        text = "Detected: Police Vehicle"
    elif red_pixels > threshold:
        text = "Detected: Ambulance"
    elif blue_pixels > threshold:
        text = "Detected: Fire Truck"

    # Display text on video
    cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    cv2.imshow("Emergency Vehicle Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
