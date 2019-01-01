import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

# Simple version

file = "../imageRasp/atom/blackFloorHouse/image1.jpg"
image = cv2.imread(file)

imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB);
imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV);
plt.figure()
plt.imshow(imgRGB)
plt.title("RGB")

plt.figure()
for i in range(3):
    plt.subplot(2,2,i+1)
    plt.imshow(imgRGB[:,:,i], cmap='gray')
    plt.title("Img " + str(i))

plt.figure()
for i in range(3):
    plt.subplot(2,2,i+1)
    plt.imshow(imgHSV[:,:,i], cmap='gray')
    plt.title("Img " + str(i))


otsu = cv2.threshold(imgHSV[:,:,1], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
imVOtsu = otsu[1]
plt.figure()
plt.imshow(imVOtsu, cmap='gray')
plt.title("imVOtsu")

plt.figure()
plt.hist(imgHSV[:,:,1].ravel(),256)
plt.title("hist")

plt.show()
