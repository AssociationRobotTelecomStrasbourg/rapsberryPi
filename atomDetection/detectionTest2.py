import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

#
# Detect puck in image with my own saturation and with blobDetection
#

# Simple version

# file = "../imageRasp/atom/terrainAtom/image1.jpg"
file = "../imageRasp/atom/blackFloorHouse/image1.jpg"
image = cv2.imread(file)

saturation = (1-np.min(image,axis=2)/np.mean(image,axis=2))*255
saturation = saturation.astype('uint8')

otsu = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
imVOtsu = otsu[1]

plt.figure()
plt.imshow(saturation, cmap='gray')
plt.title("Mine")

plt.figure()
plt.imshow(imVOtsu, cmap='gray')
plt.title("imVOtsu")


params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = False
params.filterByColor = False
params.filterByConvexity = True
params.filterByInertia = False
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

params.minCircularity = 0.4
params.maxCircularity = 0.9

params.blobColor = 255

params.minDistBetweenBlobs = 0;
# params.minRepeatability = 1;

start = timeit.timeit()

detectorBlob = cv2.SimpleBlobDetector_create(params)

keypoints = detectorBlob.detect(imVOtsu)

for key in keypoints:
    cv2.circle(image, (int(key.pt[0]),int(key.pt[1])) , 5, (255,0,0), -1)

print(start - timeit.timeit())

plt.figure()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Image or")
plt.show()

# print(keypoints[0].pt)
# print(keypoints[0].size)

# retval, labels, stats, centroids = cv2.connectedComponentsWithStats(threshV, None, None, None, 4)
