import cv2 as cv
import numpy as np

img = cv.imread("images/Lenna.png",0)
 
def region_grow(img, seed, thres):
    x,y = img.shape

    out_img = np.zeros_like(img)

    for i in range(0,x):
        for j in range(0,y):
            if abs(img[i][j] - seed) <= thres:
                out_img[i][j] = 255
            else:
                out_img[i][j] = 0

    return out_img


cv.imshow('Original', img)
cv.imshow('Region Grow', region_grow(img, 240, 125))


cv.waitKey(0)
cv.destroyAllWindows()
