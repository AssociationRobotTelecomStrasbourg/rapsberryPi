import time
import cv2
import numpy as np
import cv2.aruco as aruco
import sys

# Load calibration parameters
f=cv2.FileStorage()
file="cameraCalibration/coeffCalibrationCamSorgan.xml"
j=cv2.FileStorage.open(f,file,0)
if(not f.isOpened()):
    print("Error reading " + file)
    exit()

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

# Give camera time to warm up
time.sleep(0.1)


# if (len(sys.argv) < 4):
#     print("ERROR: Need 3 arguments: <nbMark>, <nbPix> ")
#     exit()

# Create aruco dictionary
# aruco_dict = aruco.Dictionary_create(nbMark, nbPix)
aruco_dict = aruco.Dictionary_create(2, 5)
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)


# Read image
file = "../imageRasp/aruco/MarkerOnScreen.jpg"
image = cv2.imread(file)
if image is None:
    print("Error loading " + file)
    exit()
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict)

if (ids is not None):
    arucoImMarkers = aruco.drawDetectedMarkers(image, corners, ids, (0, 0, 255))

    [rvecs, tvecs, _objPoints] = aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs, None, None);

    for i in range(len(ids)):
        aruco.drawAxis(image, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.05);

cv2.imshow("Display", image)

key = cv2.waitKey(0) & 0xFF
while key != ord("q"):
    key = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
