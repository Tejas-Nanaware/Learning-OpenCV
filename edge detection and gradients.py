import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:

	# Capture Video
	_, frame = cap.read()
	# flip video
	frame = cv2.flip(frame, 1) 
	
	# gradients
	#laplacian gradient
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	#sobel gradient
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

	#edge detectors
	edges = cv2.Canny(frame, 100, 200)

	cv2.imshow('original', frame)
	# cv2.imshow('laplacial', laplacian)
	# cv2.imshow('sobelx', sobelx)
	# cv2.imshow('sobely', sobely)
	cv2.imshow('edges', edges)

	# Exit process
	key = cv2.waitKey(23) & 0xFF
	if key == 27:
		break

# Post exit cleanup
cv2.release()
cv2.destroyAllWindows()