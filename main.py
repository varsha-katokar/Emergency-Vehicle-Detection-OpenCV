import cv2
import numpy as np
from tkinter import Tk, Button, filedialog, Label

def detect_vehicle(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red detection (using both lower and upper red ranges)
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])
        mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask_red = cv2.bitwise_or(mask_red1, mask_red2)

        # Blue detection
        lower_blue = np.array([94, 80, 2])
        upper_blue = np.array([126, 255, 255])
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

        red_pixels = cv2.countNonZero(mask_red)
        blue_pixels = cv2.countNonZero(mask_blue)

        vehicle = "Unknown"
        if red_pixels > 3000 and blue_pixels > 3000:
            vehicle = "Police Vehicle"
        elif red_pixels > 3000:
            vehicle = "Ambulance"
        elif blue_pixels > 3000:
            vehicle = "Fire Truck"

        cv2.putText(frame, f"Detected: {vehicle}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)
        cv2.imshow("Emergency Vehicle Detection", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def browse_video():
    path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if path:
        detect_vehicle(path)

# GUI Setup
window = Tk()
window.title("Emergency Vehicle Detector")
window.geometry("400x200")

label = Label(window, text="Click below to select a siren video", font=("Arial", 12))
label.pack(pady=20)

btn = Button(window, text="Select Video File", command=browse_video, font=("Arial", 12), bg="lightblue")
btn.pack(pady=10)

window.mainloop()