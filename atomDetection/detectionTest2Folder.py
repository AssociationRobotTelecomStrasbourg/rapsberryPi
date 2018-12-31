import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit
import glob

#
# Detect puck in a set of image with my own saturation and with blobDetection
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

params.minArea = 100
params.maxArea = 30000

params.minConvexity = 0.9
params.maxConvexity = 1

params.minInertiaRatio = 0.1
params.maxInertiaRatio = 0.8

params.minCircularity = 0.55
params.maxCircularity = 0.9

params.blobColor = 255

params.minDistBetweenBlobs = 0;
# params.minRepeatability = 1

# Folder to find information

folder = "../imageRasp/atom/terrainAtom/"

# Read JPG images
files = glob.glob(folder+"*.jpg")
for f in range(len(files)):
    file = files[f]
    image = cv2.imread(file)

    # Find color
    saturation = (1-np.min(image,axis=2)/np.mean(image,axis=2))*255
    saturation = saturation.astype('uint8')

    otsu = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
    imVOtsu = otsu[1]

    # Find blob

    start = timeit.timeit()

    detectorBlob = cv2.SimpleBlobDetector_create(params)

    keypoints = detectorBlob.detect(imVOtsu)

    # Draw center
    for key in keypoints:
        cv2.circle(image, (int(key.pt[0]),int(key.pt[1])) , 5, (255,0,0), -1)

    print(start - timeit.timeit())
    plt.subplot(len(files)//3,3,f+1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(file)


plt.show()
