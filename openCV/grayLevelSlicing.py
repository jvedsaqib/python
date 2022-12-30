import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

a = int(input("Enter Range 1: "))
b = int(input("Enter Range 2: "))

img = cv.imread("images/Lenna.png",0)
 
x,y = img.shape

z = np.zeros((x,y))
z1 = np.zeros((x,y))

# gray level without background
for i in range(0,x):
    for j in range(0,y):
        if(img[i][j] > a and img[i][j] < b):
            z[i][j] = 255
        else:
            z[i][j] = 0

# gray level with background
for i in range(0,x):
    for j in range(0,y):
        if(img[i][j] > a and img[i][j] < b):
            z1[i][j] = 255
        else:
            z1[i][j] = img[i][j]

# imgs = np.hstack((img, z))
# cv.imshow("", imgs)

# cv.imshow('Original', img)
# cv.imshow('Bright', z)

plt.figure().set_figwidth(10)

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Without Background")
plt.imshow(z, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("With Background")
plt.imshow(z1, cmap='gray')
plt.axis('off')

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
