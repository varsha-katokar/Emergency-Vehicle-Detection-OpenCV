# Emergency Vehicle Detection Using Siren Light Pattern

## Project Overview

This project detects emergency vehicles such as Ambulance, Fire Truck, and Police vehicles using siren light color detection from video input. The system processes video frames using OpenCV and HSV color space to identify flashing red and blue lights and classify vehicle types accordingly.

## Features

- Detects Ambulance (Red siren light)
- Detects Fire Truck (Blue siren light)
- Detects Police Vehicle (Red + Blue siren light)
- GUI-based video upload using Tkinter
- Supports MP4 video input

## Technologies Used

Python  
OpenCV  
NumPy  
Tkinter  

## Working Principle

1. Upload video through GUI
2. Convert video frames from BGR to HSV color space
3. Detect red and blue pixels
4. Apply pixel threshold logic
5. Classify emergency vehicle type
6. Display detection result on video frame

## How to Run

Install dependencies:

pip install -r requirements.txt

Run program:

python emergency_vehicle_detector.py

Upload a video file using the GUI and detection will start.

## Output

Sample detection results are included in screenshots inside this repository.
