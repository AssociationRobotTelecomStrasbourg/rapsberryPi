import cv2
import cv2.aruco as aruco
import numpy as np

# 2 Markers with 5x5 pixels
aruco_dict = aruco.Dictionary_create(2,5)

# Create marker
img = aruco.drawMarker(aruco_dict, 1, 700)
cv2.imwrite("../imageRasp/aruco/testMarker_Dict2-5_Id1_Size700.jpg", img)

img = aruco.drawMarker(aruco_dict, 0, 700)
cv2.imwrite("../imageRasp/aruco/testMarker_Dict2-5_Id0_Size700.jpg", img)
