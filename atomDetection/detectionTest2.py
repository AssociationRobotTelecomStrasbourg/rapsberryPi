import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

<<<<<<< Updated upstream
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
=======
# Simple version

file = "../imageRasp/atom/blackFloorHouse/image1.jpg"
image = cv2.imread(file)

saturation = (1-np.min(image,axis=2)/np.mean(image,axis=2))*255
saturation = saturation.astype('uint8')

# plt.figure()
# plt.imshow(saturation, cmap='gray')
# plt.title("Mine")

otsu = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
imVOtsu = otsu[1]
# plt.figure()
# plt.imshow(imVOtsu, cmap='gray')
# plt.title("imVOtsu")


>>>>>>> Stashed changes
params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = True
params.filterByColor = False
params.filterByConvexity = True
params.filterByInertia = True
params.filterByArea = True

<<<<<<< Updated upstream
params.minThreshold = 48
params.maxThreshold = 50
=======
params.minThreshold = 0
params.maxThreshold = 2
>>>>>>> Stashed changes
params.thresholdStep = 1

params.filterByArea = True
params.minArea = 500
params.maxArea = 30000

params.minConvexity = 0.9
params.maxConvexity = 1

<<<<<<< Updated upstream
params.minCircularity = 0.5
params.maxCircularity = 1
=======
params.minInertiaRatio = 0.0
params.maxInertiaRatio = 0.5

params.minCircularity = 0.4
params.maxCircularity = 0.8
>>>>>>> Stashed changes

params.blobColor = 255

params.minDistBetweenBlobs = 0;
# params.minRepeatability = 1;

start = timeit.timeit()

detectorBlob = cv2.SimpleBlobDetector_create(params)

<<<<<<< Updated upstream
keypoints = detectorBlob.detect(threshV)
# keypoints = detectorBlob.detect(imgHSV[:,:,2])

print("Nb keypoints " + str(len(keypoints)))
=======
keypoints = detectorBlob.detect(imVOtsu)
>>>>>>> Stashed changes

for key in keypoints:
    cv2.circle(image, (int(key.pt[0]),int(key.pt[1])) , 5, (255,0,0), -1)

<<<<<<< Updated upstream
print(timeit.timeit()-start)

plt.figure()
plt.imshow(image)
=======
print(start - timeit.timeit())

plt.figure()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Image or")
>>>>>>> Stashed changes
plt.show()

# print(keypoints[0].pt)
# print(keypoints[0].size)

# retval, labels, stats, centroids = cv2.connectedComponentsWithStats(threshV, None, None, None, 4)
