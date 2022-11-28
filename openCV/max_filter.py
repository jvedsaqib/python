import cv2 as cv
import numpy as np
import matplotlib.pyplot as plp

# Google Colab
# from google.colab.patches import cv2_imshow
# import cv2

img = cv.imread('images/Lenna.png', 0)
# cv.imshow("image", img)


h, w = img.shape

img_new = np.zeros([h,w])

'''
        0       1       2

    0   i-1     i-1     i-1
        j-1     j       j+1

    1   i       i       i
        j-1     j       j+1

    2   i+1     i+1     i+1
        j-1     j       j+1

'''

print(h)
print(w)

for i in range(1, h-1):
    for j in range(1, w-1):
        temp = max(img[i-1, j-1], img[i-1, j], img[i-1, j+1],
                    img[i, j-1], img[i, j], img[i, j+1],
                    img[i+1, j-1], img[i+1, j], img[i+1, j+1])
        img_new[i,j] = temp

# cv.imshow("image", img)
# cv.imshow("New", img_new)


cv.waitKey(0)
