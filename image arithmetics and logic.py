import numpy as np
import cv2

img1 = cv2.imread('image arith1.png')
img2 = cv2.imread('image arith2.png')
img3 = cv2.imread('image arith3.png')

# add = img1 + img2
# add = cv2.add(img1, img2) #adds pixel values

# weighted = cv2.addWeighted(img1, 0.2, img2, 0.6, 5) #img1, %opaque, img2, %opaque, gamma

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV) #thresholding image, anything above 220 is converted to 255 and below 220 is converted to black
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask = mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('final', img1)
cv2.imshow('maskinv', mask_inv)
cv2.imshow('img1bg', img1_bg)
cv2.imshow('img3fg', img3_fg)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
