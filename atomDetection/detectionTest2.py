import cv2
import numpy as np
from matplotlib import pyplot as plt

file = "../imageRasp/atom/distTestBlackFloor/image4.jpg"
image = cv2.imread(file)

imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV);

threshV = (imgHSV[:,:,2]>40).astype('uint8')*255

params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = False
params.filterByColor = True
params.filterByConvexity = True
params.filterByInertia = False

params.minThreshold = 0
params.maxThreshold = 50
params.thresholdStep = 1
params.filterByArea = True

params.minArea = 500
params.maxArea = 30000

params.minConvexity = 0.9
params.maxConvexity = 1

params.blobColor = 255

params.minDistBetweenBlobs = 0;
# params.minRepeatability = 1;

detectorBlob = cv2.SimpleBlobDetector_create(params)
print(detectorBlob)
keypoints = detectorBlob.detect(imgHSV[:,:,2])

for key in keypoints:
    cv2.circle(image, (int(key.pt[0]),int(key.pt[1])) , 5, (255,0,0), -1)

plt.imshow(image)
plt.show()

# print(keypoints[0].pt)
# print(keypoints[0].size)

# retval, labels, stats, centroids = cv2.connectedComponentsWithStats(threshV, None, None, None, 4)
