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
	# Or Gimp or photoshop H/2, %S*255, %V*255 for OpenCV Values
	lower_pink = np.array([165, 160, 76])
	upper_pink = np.array([179, 255, 255])

	# for specific color
	# dark_red = np.uint8([[[12, 22, 121]]])
	# dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_pink, upper_pink)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	# For erosion and dilation
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilate = cv2.dilate(mask, kernel, iterations = 1)

	# Opening and closing removes false positives that are in the background
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


	cv2.imshow('frame', frame)
	cv2.imshow('res', res)
	cv2.imshow('erode', erosion)
	cv2.imshow('dilate', dilate)
	cv2.imshow('open', opening)
	cv2.imshow('close', closing)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()