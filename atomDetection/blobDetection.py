import time
import cv2
import numpy as np
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera

 # Start the camera and define settings
camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(1024, 768))

# Give camera time to warm up
time.sleep(2)

# Create aruco dictionary
aruco_dict = aruco.Dictionary_create(2, 5)


# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = cv2.SimpleBlobDetector_create()
    keypoints = detector.detect(image_gray)

    im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255),    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


    cv2.imshow("Display", image)

    # Clear the stream capture
    rawCapture.truncate(0)

    # set "q" as the key to exit the program when pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    # "c" to capture photo
    if key == ord("c") :
        nbPic = nbPic + 1;
        camera.capture('/home/pi/raspberry/imageRasp/image%s.jpg' % nbPic)
        print("Pictuuuure !")
