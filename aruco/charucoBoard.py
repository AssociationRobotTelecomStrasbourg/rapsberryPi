import sys
import cv2
import cv2.aruco as aruco

if (len(sys.argv) < 7):
    print("ERROR: Need 6 arguments:  <squaresX> <squaresY> <squareLength> <markerLength> <sizeXImg> <sizeYImg> ")
    exit()

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

squaresX = int(sys.argv[1])
squaresY = int(sys.argv[2])
squareLength = int(sys.argv[3])
markerLength = int(sys.argv[4])
sizeXImg = int(sys.argv[5])
sizeYImg = int(sys.argv[6])

charucoBoard = aruco.CharucoBoard_create(squaresX,6,7,6,aruco_dict)
charucoBoard = aruco.CharucoBoard_create(squaresX, squaresY, squareLength, markerLength, aruco_dict)

imBoard = aruco.drawPlanarBoard(charucoBoard,(sizeXImg,sizeYImg))

cv2.imwrite("../imageRasp/aruco/charucoBoard" + str(squaresX) + "-" + str(squaresY) + "Len" + str(squareLength) + "-" + str(markerLength) + "Size" + str(sizeXImg) + "-" + str(sizeYImg) + "_6X6_250.jpg", imBoard)

cv2.imshow('chaBoard',imBoard)
key = cv2.waitKey(0) & 0xFF
while key != ord("q"):
    key = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
