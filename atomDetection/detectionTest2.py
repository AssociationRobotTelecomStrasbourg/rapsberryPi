import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

file = "/home/pi/raspberryPi/imageRasp/atom/terrainAtom/image6.jpg"
image = cv2.imread(file)

imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV);
# plt.figure()
# plt.imshow(imgHSV[:,:,2])

threshV = (imgHSV[:,:,2]>200).astype('uint8')*255
plt.figure()
plt.imshow(threshV)
# plt.figure()
# plt.hist(imgHSV[:,:,2].ravel(),255)
params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = True
params.filterByColor = False
params.filterByConvexity = True
params.filterByInertia = False

params.minThreshold = 48
params.maxThreshold = 50
params.thresholdStep = 1

params.filterByArea = True
params.minArea = 500
params.maxArea = 30000

params.minConvexity = 0.9
params.maxConvexity = 1

params.minCircularity = 0.5
params.maxCircularity = 1

params.blobColor = 255

params.minDistBetweenBlobs = 0;
# params.minRepeatability = 1;

start = timeit.timeit()

detectorBlob = cv2.SimpleBlobDetector_create(params)

keypoints = detectorBlob.detect(threshV)
# keypoints = detectorBlob.detect(imgHSV[:,:,2])

print("Nb keypoints " + str(len(keypoints)))

for key in keypoints:
    cv2.circle(image, (int(key.pt[0]),int(key.pt[1])) , 5, (255,0,0), -1)

print(timeit.timeit()-start)

plt.figure()
plt.imshow(image)
plt.show()

# print(keypoints[0].pt)
# print(keypoints[0].size)

# retval, labels, stats, centroids = cv2.connectedComponentsWithStats(threshV, None, None, None, 4)
