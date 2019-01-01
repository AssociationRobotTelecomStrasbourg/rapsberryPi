import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

#
# Detect puck in image with my opencv saturation and remove black color and with blobDetection
#

# file = "../imageRasp/atom/terrainAtom/image1.jpg"
file = "../imageRasp/atom/testCamFailed/image2.jpg"
image = cv2.imread(file)

imhHLS = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
saturation = imhHLS[:,:,2]
lum = imhHLS[:,:,1]>10

# saturationMine = (1-np.min(image,axis=2)/np.mean(image,axis=2))*255
# saturationMine = saturationMine.astype('uint8')

SatLum = np.zeros(lum.shape, dtype="uint8")
SatLum[lum] = saturation[lum].ravel()

otsu = cv2.threshold(SatLum, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
imVOtsu = otsu[1]

plt.figure()
plt.imshow(imhHLS[:,:,1], cmap='gray')
plt.title("Lum")

plt.figure()
plt.imshow(saturation, cmap='gray')
plt.title("saturation")

# plt.figure()
# plt.imshow(saturationMine, cmap='gray')
# plt.title("saturationMine")

plt.figure()
plt.imshow(SatLum, cmap='gray')
plt.title("Mine")

plt.figure()
plt.imshow(imVOtsu, cmap='gray')
plt.title("imVOtsu")


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

start = timeit.timeit()

detectorBlob = cv2.SimpleBlobDetector_create(params)

keypoints = detectorBlob.detect(imVOtsu)

for key in keypoints:
    cv2.circle(image, (int(key.pt[0]),int(key.pt[1])) , 5, (255,255,255), -1)

print(start - timeit.timeit())

plt.figure()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Image or")
plt.show()
