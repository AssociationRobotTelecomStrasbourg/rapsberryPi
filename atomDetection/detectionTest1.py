import cv2
import numpy as np
from matplotlib import pyplot as plt

file = "../imageRasp/atom/distTestBlackFloor/image4.jpg"
image = cv2.imread(file)

imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV);
cv2.imshow("imgHSV",imgHSV[:,:,2])

threshV=np.array((imgHSV[:,:,2]>40)*255,dtype='uint8')

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

detectorBlob = cv2.SimpleBlobDetector_create(params)
keypoints = detectorBlob.detect(imgHSV[:,:,2])
# keypoints = detectorBlob.detect(threshV)

centerBlobs = [ [int(k.pt[0]),int(k.pt[1])] for k in keypoints]

imageKeypoints = cv2.drawKeypoints(threshV, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow("imageKeypoints",imageKeypoints)

retval, labels, stats, centroids = cv2.connectedComponentsWithStats(threshV, None, None, None, 4)
cv2.imshow("threshVc", threshV)

possiblePucks=[]
possiblePucksStats=[]
possibleCenters=[]
for ce in centerBlobs:
    if( (ce[0] < image.shape[0]) and (ce[1] < image.shape[1]) ):
        if ( (threshV[ce[1],ce[0]]==[255,255,255]).all() ):
                possiblePucks.append(labels[ce[1],ce[0]])
                possiblePucksStats.append(stats[labels[ce[1],ce[0]]])
                possibleCenters.append((ce[1],ce[0]))

for i in range(len(possiblePucks)):
    area = np.uint8((labels==possiblePucks[i])*255)
    stats = possiblePucksStats[i]
    cv2.imshow("area",area)

    #if(stats[cv2.CC_STAT_AREA])
    im2, contours, hierarchy = cv2.findContours(area, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if ( contours[0].shape[0] > 5 ) :
        eli=cv2.fitEllipse(contours[0])
        cv2.ellipse(image,eli,(0,255,0),2)

cv2.imshow("image",image)


key = cv2.waitKey(0) & 0xFF
while key != ord("q"):
    key = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
