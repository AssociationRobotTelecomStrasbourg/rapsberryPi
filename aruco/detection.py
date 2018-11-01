import cv2
import numpy as np
import cv2.aruco as aruco
import sys

if (len(sys.argv) < 4):
    print("ERROR: Need 3 arguments: <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Path of marker image>")
    exit()

nbMark = sys.argv[1]
nbPix = sys.argv[2]
pathMarker = sys.argv[3]

# Dictionary
aruco_dict = aruco.Dictionary_create(nbMark,nbPix)

# Load one marker
arucoIm = cv2.imread(pathMarker)
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
