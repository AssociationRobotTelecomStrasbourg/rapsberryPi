import cv2
import numpy as np
import cv2.aruco as aruco

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
charucoBoard = aruco.CharucoBoard_create(6,7,7,6,aruco_dict)

allCorners = []
allIds = []
for i in range(1,7):

    img = cv2.imread("../imageRasp/aruco/charucoBoard/pointOfView" + str(i) + ".jpg")

    markers = aruco.detectMarkers(img,aruco_dict)

    if len(markers[0])>0:
        markers2 = aruco.interpolateCornersCharuco(markers[0],markers[1],img,charucoBoard)
        if markers2[1] is not None and markers2[2] is not None and len(markers2[1])>3:
            allCorners.append(markers2[1])
            allIds.append(markers2[2])

        img = aruco.drawDetectedMarkers(img,markers[0],markers[1])

    # cv2.imshow('frame',img)
    # key = cv2.waitKey(0) & 0xFF
    # while key != ord("q"):
    #     key = cv2.waitKey(0) & 0xFF

[retval, cameraMatrix, distCoeffs, rvecs, tvecs] = aruco.calibrateCameraCharuco(allCorners, allIds, charucoBoard, (700,1000),None,None)

f=cv2.FileStorage("cameraCalibration/raspberryPiSorgan/retvalCameraMatrixDistCoeffs.xml",3)
f.write('retval', retval)
f.write('cameraMatrix', cameraMatrix)
f.write('distCoeffs', distCoeffs)
f.write('rvecs', np.array(rvecs))
f.write('rvecs', np.array(tvecs))


# cv2.destroyAllWindows()
