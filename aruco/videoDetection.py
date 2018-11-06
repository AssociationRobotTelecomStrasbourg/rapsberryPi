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


# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict)

    if (ids is not None):
        arucoImMarkers = aruco.drawDetectedMarkers(image, corners, ids, (0, 0, 255))

        [rvecs, tvecs, _objPoints] = aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs, None, None);

        for i in range(len(ids)):
            aruco.drawAxis(image, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.05);
            points = cv2.projectPoints(np.array([[0, 0, 0]], dtype=np.float),rvecs[i], tvecs[i], cameraMatrix, distCoeffs)
            cv2.putText(image,str(round(np.sqrt(points[0][0][0][0]**2+points[0][0][0][1]**2)/10)),(int(points[0][0][0][0])+10,int(points[0][0][0][1]+10)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))

    cv2.imshow("Display", image)

    # Clear the stream capture
    rawCapture.truncate(0)

    # set "q" as the key to exit the program when pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    # "c" to capture photo
    if key == ord("c") :
        nbPic = nbPic + 1;
        camera.capture('/home/pi/raspberry/imageRasp/image%s.jpg' % nbPic)
        print("Pictuuuure !")
