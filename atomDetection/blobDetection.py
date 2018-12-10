import time
import cv2
import numpy as np
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera

 # Start the camera and define settings
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 100
rawCapture = PiRGBArray(camera, size=(640,480))

# Give camera time to warm up
time.sleep(2)

nbPic=0
# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10;
    # params.maxThreshold = 200;

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 1000

    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.1

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.1

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image_gray)

    im_with_keypoints = cv2.drawKeypoints(image_gray, keypoints, np.array([]), (0,0,255),    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


    cv2.imshow("Display", im_with_keypoints)

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
