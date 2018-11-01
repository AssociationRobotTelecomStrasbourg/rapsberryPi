import cv2
import cv2.aruco as aruco
import numpy as np
import sys

if (len(sys.argv) < 5):
    print("ERROR: Need 4 arguments: <Number of markers in dictionary> <Number of pixel (4,5,6, etc...)> <Size of image (px)> <Id of marker> ")
    exit()

nbMark = sys.argv[1]
nbPix = sys.argv[2]
sizeMark = sys.argv[3]
idMark =sys.argv[4]

# Create dictionnary
aruco_dict = aruco.Dictionary_create(nbMark, nbPix)

# Create marker and save
img = aruco.drawMarker(aruco_dict, idMark, sizeMark)
cv2.imwrite("../imageRasp/aruco/marker_Dict" + nbMark + "-" + nbPix + "_Id" + idMark + "_Size" + sizeMark + ".jpg", img)
