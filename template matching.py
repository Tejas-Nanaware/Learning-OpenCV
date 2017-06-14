import numpy as np
import cv2
# read images for template matching
img_bgr = cv2.imread('template matching.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template matching template.jpg', 0)

w, h = template.shape[::-1]
# thresholding image for template matching
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.79 # instead of decreasing the threshold, have multiple images for the templates and then match them

loc = np.where(res >= threshold)
# Marking the templates on the main image
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

cv2.imshow('detected', img_bgr)
cv2.waitKey(0)