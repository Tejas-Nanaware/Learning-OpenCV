# First look at the color filtering
# It is based on that code for pink ball detection color filtering.py
# That code was for Green Ball, this is for pink ball
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	#flip video
	frame=cv2.flip(frame, 1)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# Hue Saturation Value
	# http://colorizer.org/ for knowing color hsv values
	lower_pink = np.array([165, 160, 140])
	upper_pink = np.array([179, 255, 255])

	# for specific color
	# dark_red = np.uint8([[[12, 22, 121]]])
	# dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_pink, upper_pink)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	#creating a smoothed kernel
	kernel = np.ones((15,15), np.float32) / 225
	smoothed = cv2.filter2D(res, -1, kernel)
	# Gaussian Blur
	blur = cv2.GaussianBlur(res, (15,15), 0)
	# Median Blur
	median_blur = cv2.medianBlur(res, 15) #this is really nice
	# Bilateral Blur
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)


	cv2.imshow('frame', frame)
	# cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	# cv2.imshow('smoothed', smoothed)
	# cv2.imshow('blur', blur)
	# cv2.imshow('M blur', median_blur)
	cv2.imshow('Bilateral', bilateral)


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()