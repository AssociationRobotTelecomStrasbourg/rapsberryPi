import cv2
import numpy as np
import cv2.aruco as aruco
import sys

# Dictionary with two 5x5pixels markers
aruco_dict = aruco.Dictionary_create(2,5)

if (len(sys.argv) < 2):
    print("ERROR: Need one argument, path of an image")
    exit()

# Load one marker
arucoIm = cv2.imread(sys.argv[1])
arucoImG = cv2.cvtColor(arucoIm,cv2.COLOR_RGB2GRAY)
sizeAruco=arucoIm.shape

# Detect marker
corners, ids, rejectedImgPoints = aruco.detectMarkers(arucoImG, aruco_dict)

# Draw square and ID
result = aruco.drawDetectedMarkers(arucoIm, corners, ids, (0, 0, 255))

cv2.imshow('result',result)
key = cv2.waitKey(0) & 0xFF
while key != ord("q"):
    key = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
