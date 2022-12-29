import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Google Colab
# from google.colab.patches import cv2_imshow
# import cv2

img = cv.imread('images/Lenna.png', 0)
#cv.imshow("image", img)

h, w = img.shape

h = len(img)
w = len(img)


mask = np.ones([3,3], dtype=int)
mask = mask / 9
img_new = np.zeros([h,w])
img_new2 = np.zeros([h,w])

'''
        0       1       2

    0   i-1     i-1     i-1
        j-1     j       j+1

    1   i       i       i
        j-1     j       j+1

    2   i+1     i+1     i+1
        j-1     j       j+1

'''

for i in range(1, h-1):
    for j in range(1, w-1):
        temp = img[i-1, j-1] * mask[0, 0] + img[i-1, j] * mask[0, 1] + img[i-1, j+1] * mask[0,2] + img[i, j-1] * mask[1,0] + img[i,j] * mask[1,1] + img[i, j+1] * mask[1,2] + img[i+1, j-1] * mask[2,0] + img[i+1, j] * mask[2,1] + img[i+1, j+1] * mask[2,2]
        img_new[i,j] = temp // 9


plt.figure().set_figwidth(10)

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Mean")
plt.imshow(img_new, cmap='gray')


plt.show()
cv.waitKey(0)
