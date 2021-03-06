import numpy as np
import cv2 as cv

#example 1
from matplotlib import pyplot as plt

img = cv.imread('shap.jpeg')

# Initiate STAR detector
orb = cv.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img,kp,None,color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()

#example 2
img = cv.imread('shapes.png')

cv.namedWindow('ORB', cv.WINDOW_NORMAL)

def f(x):
    return

# Initiate ORB detector
cv.createTrackbar('Edge Threshold', 'ORB', 15, 50, f)
cv.createTrackbar('Patch Size', 'ORB', 31, 30, f)
cv.createTrackbar('N Levels', 'ORB', 8, 30, f)
cv.createTrackbar('Fast Threshold', 'ORB', 20, 50, f)
cv.createTrackbar('Scale Factor', 'ORB', 12, 25, f)
cv.createTrackbar('WTA K', 'ORB', 2, 4, f)
cv.createTrackbar('First Level', 'ORB', 0, 20, f)
cv.createTrackbar('N Features', 'ORB', 500, 1000, f)

while True:
    edge_threshold = cv.getTrackbarPos('Edge Threshold', 'ORB')
    patch_size = cv.getTrackbarPos('Patch Size', 'ORB')
    n_levels = cv.getTrackbarPos('N Levels', 'ORB')
    fast_threshold = cv.getTrackbarPos('Fast Threshold', 'ORB')
    scale_factor = cv.getTrackbarPos('Scale Factor', 'ORB') / 10
    wta_k = cv.getTrackbarPos('WTA K', 'ORB')
    first_level = cv.getTrackbarPos('First Level', 'ORB')
    n_features = cv.getTrackbarPos('N Features', 'ORB')

    if wta_k < 2:
        wta_k = 2

    if patch_size < 2:
        patch_size = 2

    if n_levels < 1:
        n_levels = 1

    if scale_factor < 1:
        scale_factor = 1

    orb = cv.ORB_create(edgeThreshold=edge_threshold, patchSize=patch_size, nlevels=n_levels, fastThreshold=fast_threshold, scaleFactor=scale_factor, WTA_K=wta_k,scoreType=cv.ORB_HARRIS_SCORE, firstLevel=first_level, nfeatures=n_features)

    # find the keypoints with ORB
    kp = orb.detect(img,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)

    # draw only keypoints location,not size and orientation
    img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv.imshow('ORB', img2)

    if cv.waitKey(10) & 0xFF == 27:
        break

cv.destroyAllWindows()