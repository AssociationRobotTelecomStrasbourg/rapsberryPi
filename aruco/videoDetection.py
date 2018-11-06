import time
import cv2
import numpy as np
import cv2.aruco as aruco
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera

 # Start the camera and define settings
camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 32
rawCapture = PiRGBArray(camera)

# Load calibration parameters
f=cv2.FileStorage()
file="cameraCalibration/raspberryPiSorgan/retvalCameraMatrixDistCoeffs.xml"
j=cv2.FileStorage.open(f,file,0)

if(f.getNode("retval").isNone()):
    print("Error reading retval in " + file)
    exit()
else:
    retval=f.getNode("retval").real()

if(f.getNode("cameraMatrix").isNone()):
    print("Error reading cameraMatrix in " + file)
    exit()
else:
    cameraMatrix = f.getNode("cameraMatrix").mat()

if(f.getNode("distCoeffs").isNone()):
    print("Error reading distCoeffs in " + file)
    exit()
else:
    distCoeffs = f.getNode("distCoeffs").mat()

if(f.getNode("rvecs").isNone()):
    print("Error reading rvecs in " + file)
    exit()
else:
    rvecs = f.getNode("rvecs").mat()


if(f.getNode("tvecs").isNone()):
    print("Error reading tvecs in " + file)
    exit()
else:
    tvecs = f.getNode("tvecs").mat()

# Give camera time to warm up
time.sleep(0.1)


# if (len(sys.argv) < 4):
#     print("ERROR: Need 3 arguments: <nbMark>, <nbPix> ")
#     exit()

# Create aruco dictionary
# aruco_dict = aruco.Dictionary_create(nbMark, nbPix)
aruco_dict = aruco.Dictionary_create(2, 5)
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)


# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict)

    if len(ids) > 0:
        arucoImMarkers = aruco.drawDetectedMarkers(image, corners, ids, (0, 0, 255))

        [rvecs, tvecs, _objPoints] = aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs, rvecs, tvecs);

        for i in range(len(ids)):
            aruco.drawAxis(image, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.05);

        cv2.imshow("Display", image)

    # Clear the stream capture
    rawCapture.truncate(0)

    #set "q" as the key to exit the program when pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
