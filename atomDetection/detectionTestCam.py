import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit
import time
from picamera.array import PiRGBArray
from picamera import PiCamera


#
# Detect puck in image with my opencv saturation and remove black color and with blobDetection
#

params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = True
params.filterByColor = False
params.filterByConvexity = True
params.filterByInertia = True
params.filterByArea = True

params.minThreshold = 0
params.maxThreshold = 2
params.thresholdStep = 1

params.minArea = 300
params.maxArea = 30000

params.minConvexity = 0.8
params.maxConvexity = 1

params.minInertiaRatio = 0.1
params.maxInertiaRatio = 0.9

params.minCircularity = 0.5
params.maxCircularity = 0.9

params.blobColor = 255

params.minDistBetweenBlobs = 0;
# params.minRepeatability = 1;

#
# Start the camera and define settings
# Init parameters
#
camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 32
rawCapture = PiRGBArray(camera)

# Give camera time to warm up
time.sleep(0.1)

nbPic=0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Init
    start = timeit.timeit()
    image = frame.array

    # Take images: saturation, luminosity
    imhHLS = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
    saturation = imhHLS[:,:,2]
    lum = imhHLS[:,:,1]>30

    # Combine Saturation and Luminosity
    SatLum = np.zeros(lum.shape, dtype="uint8")
    SatLum[lum] = saturation[lum].ravel()

    # Classify black and white pixels
    otsu = cv2.threshold(SatLum, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
    imVOtsu = otsu[1]

    # Find blob
    detectorBlob = cv2.SimpleBlobDetector_create(params)

    keypoints = detectorBlob.detect(imVOtsu)

    print("Nb of keypoints")
    print(len(keypoints))

    # Draw center
    for key in keypoints:
        cv2.circle(image, (int(key.pt[0]),int(key.pt[1])) , 5, (255,255,255), -1)

    print(start - timeit.timeit())

    # Display
    cv2.imshow("Display", image)

    rawCapture.truncate(0)

    # User input
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("c") :
        nbPic = nbPic + 1;
        camera.capture('/home/pi/raspberryPi/imageRasp/image%s.jpg' % nbPic)
        print("Pictuuuure !")

cv2.destroyAllWindows()
