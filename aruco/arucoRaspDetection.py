import time
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2.aruco as aruco

# Start the camera and define settings
camera = PiCamera()
camera.resolution = (600, 400) # A smaller resolution means faster processing
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(600, 400))

# Give camera time to warm up
time.sleep(0.1)

nbPic=0
# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Take the frame as an array, convert it to black and white
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Dictionary with two 5x5pixels markers
    aruco_dict = aruco.Dictionary_create(2,5)

    # Detect marker
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict)

    # Draw square and ID
    result = aruco.drawDetectedMarkers(image, corners, ids, (0, 0, 255))

    cv2.imshow('result',result)

    # Clear the stream capture
    rawCapture.truncate(0)

    #set "q" as the key to exit the program when pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("c") :
        nbPic = nbPic + 1;
        camera.capture('/home/pi/raspberry/image%s.jpg' % nbPic)
        print("Pictuuure ! Cheeeese !")


