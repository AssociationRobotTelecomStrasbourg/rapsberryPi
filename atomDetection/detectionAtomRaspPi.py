import time
import cv2
import numpy as np
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera

 # Start the camera and define settings
camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(1024, 768))

# Load calibration parameters
f=cv2.FileStorage()
file="/home/pi/raspberryPi/aruco/cameraCalibration/coeffCalibrationCamSorgan.xml"
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
time.sleep(2)

params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = False
params.filterByColor = False
params.filterByConvexity = False
params.filterByInertia = False

# params.minCircularity = 0.1
# params.maxCircularity = 1000
#
# params.minConvexity = 0.8
# params.maxConvexity = 1
#
# params.minInertiaRatio = 0.01
# params.maxInertiaRatio = 1000

params.minThreshold = 0
params.maxThreshold = 50
params.thresholdStep = 1

params.filterByArea = True
params.minArea = 500
params.maxArea = 30000

params.minDistBetweenBlobs = 0;
# params.minRepeatability = 1;


# Start video frame capture
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    print('New frame')
    image = (frame.array).copy()

    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV);
    # cv2.imshow("imgHSV",imgHSV[:,:,2])

    threshV=np.array((imgHSV[:,:,2]>125)*255,dtype='uint8')
    # cv2.imshow("threshV", threshV)

    print('Detect blob Begin')
    detectorBlob = cv2.SimpleBlobDetector_create(params)
    keypoints = detectorBlob.detect(imgHSV[:,:,2])
    # keypoints = detectorBlob.detect(threshV)
    print('Detect blob End')
    centerBlobs = [ [int(k.pt[0]),int(k.pt[1])] for k in keypoints]

    print('Draw blob')
    imageKeypoints = cv2.drawKeypoints(threshV, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("imageKeypoints",imageKeypoints)

    print('Components Connection')
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(threshV, None, None, None, 4)

    possiblePucks=[]
    possiblePucksStats=[]
    possibleCenters=[]
    for ce in centerBlobs:
        if( (ce[0] < image.shape[0]) and (ce[1] < image.shape[1]) ):
            if ( (threshV[ce[1],ce[0]]==[255,255,255]).all() ):
                    possiblePucks.append(labels[ce[1],ce[0]])
                    possiblePucksStats.append(stats[labels[ce[1],ce[0]]])
                    possibleCenters.append((ce[1],ce[0]))

    print('Fit ellipse Begin')
    for i in range(len(possiblePucks)):
        image[possibleCenters[i]]=[0,255,0]
        area = np.uint8((labels==possiblePucks[i])*255)
        stats = possiblePucksStats[i]

        cv2.imshow("area", area)
        contours= cv2.findContours(area, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        eli=cv2.fitEllipse(contours[1][0])
        cv2.ellipse(image, eli, (0,255,0),2)
    print('Fit ellipse End')
    # cv2.imshow("image",image)

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
