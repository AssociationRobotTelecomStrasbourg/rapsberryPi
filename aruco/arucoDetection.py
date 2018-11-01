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
arucoIm = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
sizeAruco=arucoIm.shape

# Add white border
border = 100
img = np.ones((sizeAruco[0]+border*2,sizeAruco[1]+border*2),'uint8')*255 # White matrix
img[border:border+sizeAruco[0],border:border+sizeAruco[1]] = arucoIm;

# Detect marker
corners, ids, rejectedImgPoints = aruco.detectMarkers(img, aruco_dict)

# Draw square and ID
imc = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
result = aruco.drawDetectedMarkers(imc, corners, ids, (0, 0, 255))


cv2.imshow('result',imc)
key = cv2.waitKey(0) & 0xFF
while key != ord("q"):
    key = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
