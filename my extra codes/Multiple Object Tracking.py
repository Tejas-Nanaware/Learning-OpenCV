# This code will help you in detecting a yellow ball and a pink ball
# Object tracking will help in tracking the yellow and the pink ball
import cv2
import numpy as np
# Capture Video from webcam
cap = cv2.VideoCapture(0)

while True:
	# Read webcam data
	res, frame = cap.read()
	# Flip the video
	frame = cv2.flip(frame, 1)

	# Convert BGR To HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Setting up the minimum and the maximum HSV values for object tracking
	lower_pink = np.array([165, 160, 140])
	upper_pink = np.array([179, 255, 255])

	lower_green = np.array([29, 86, 6])
	upper_green = np.array([64, 255, 255])

	# For multicolor filtering, make two masks and add them
	pink_mask = cv2.inRange(hsv, lower_pink, upper_pink)
	green_mask = cv2.inRange(hsv, lower_green, upper_green)
	mask = pink_mask + green_mask

	res = cv2.bitwise_and(frame, frame, mask = mask)

	# Morphological filtering
	kernel = np.ones((15,15), np.float32) / 225
	dilate = cv2.dilate(res, kernel, iterations = 1)
	blur = cv2.GaussianBlur(dilate, (15,15), 0)

	# Converting to gray
	gray = cv2.cvtColor(blur, cv2.COLOR_HSV2BGR)
	gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

	# Detect circles using HoughCircles
	circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,120,param1=120,param2=50,minRadius=10,maxRadius=0)
	print circles
	if circles is not None:
		for i in circles[0,:]:
			cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,255,0),5)
			cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,255,0),10)




	# Displaying various video feeds
	cv2.imshow('frame', hsv)
	cv2.imshow('fram', blur)
	cv2.imshow('framee', frame)
	# Exit the program if Esc is pressed
	exit_key = cv2.waitKey(5)
	if exit_key == 27:
		break

# Necessary exit procedure
cap.release()
cv2.destroyAllWindows()