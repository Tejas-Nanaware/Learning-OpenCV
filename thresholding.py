import numpy as np
import cv2
# basic thresholding is 0 or 1 or black or white

img = cv2.imread('thresholding.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

# Gausian Adaptive Threshold
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


retval, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('threshed', threshold)
cv2.imshow('bw threshed', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()