import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

# file = "../imageRasp/atom/terrainAtom/image1.jpg"
file = "../imageRasp/atom/blackFloorHouse/image1.jpg"
image = cv2.imread(file)

sat = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
sat = sat[:,:,1]>30
print(sat.dtype)

saturation = (1-np.min(image,axis=2)/np.mean(image,axis=2))*255
saturation = saturation.astype('uint8')

otsu = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU);
imVOtsu = otsu[1]

# plt.figure()
# plt.imshow(saturation, cmap='gray')
# plt.title("Mine")

# plt.figure()
# plt.imshow(sat, cmap='gray')
# plt.title("sat")

ss = np.zeros(saturation.shape)

ss[sat] = saturation[sat].ravel()

plt.figure()
plt.imshow(ss, cmap='gray')
plt.title("Sat OPenCV")

# plt.figure()
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title("Image or")
plt.show()
