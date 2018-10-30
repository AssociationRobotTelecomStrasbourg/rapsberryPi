import cv2
import numpy as np
import cv2.aruco as aruco

# Dictionary with two 5x5pixels markers
aruco_dict = aruco.Dictionary_create(2,5)

# Load one marker
arucoIm = cv2.imread('../imageRasp/aruco/testMarker_Dict2-5_Id0_Size700.jpg',cv2.IMREAD_GRAYSCALE)
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
cv2.waitKey(0)
cv2.destroyAllWindows()
