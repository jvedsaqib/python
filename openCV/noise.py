import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random as rd

img = cv.imread("images/Lenna.png",0)
 
x,y = img.shape

z = np.zeros((x,y))
z1 = np.zeros((x,y))
z2 = np.zeros((x,y))

for i in range(0,x):
    for j in range(0,y):
        val = rd.randint(0, 50)
        z[i][j] = val

for i in range(0,x):
    for j in range(0,y):
        val = rd.randint(0, 5)
        z1[i][j] = val

for i in range(0,x):
    for j in range(0,y):
        val = rd.randint(0, 1)
        z2[i][j] = val

cv.imshow('Img1', z)
cv.imshow('Img2', z1)
cv.imshow('Img3', z2)

cv.waitKey(0)
cv.destroyAllWindows()
