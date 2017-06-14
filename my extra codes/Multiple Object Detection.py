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
	lower_pink = np.array([165, 160, 140])
	upper_pink = np.array([179, 255, 255])

	lower_green = np.array([29, 86, 6])
	upper_green = np.array([64, 255, 255])

	# for specific color
	# dark_red = np.uint8([[[12, 22, 121]]])
	# dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

	# For multicolor filtering, make two masks and add them
	pink_mask = cv2.inRange(hsv, lower_pink, upper_pink)
	green_mask = cv2.inRange(hsv, lower_green, upper_green)
	mask = pink_mask + green_mask

	res = cv2.bitwise_and(frame, frame, mask = mask)

	# Adding blurs to reduce noise
	#creating a smoothed kernel
	kernel = np.ones((15,15), np.float32) / 225
	smoothed = cv2.filter2D(res, -1, kernel)
	# Gaussian Blur
	blur = cv2.GaussianBlur(res, (15,15), 0)
	# Median Blur
	median_blur = cv2.medianBlur(res, 15) #this is really nice
	# Bilateral Blur
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)

	# For erosion and dilation
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilate = cv2.dilate(mask, kernel, iterations = 1)

	# Opening and closing removes false positives that are in the background
	opening = cv2.morphologyEx(median_blur, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(median_blur, cv2.MORPH_CLOSE, kernel)

	cv2.imshow('frame', frame)
	cv2.imshow('res', res)
	cv2.imshow('blur', median_blur)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()