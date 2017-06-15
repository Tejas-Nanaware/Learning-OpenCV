import numpy as np
import cv2

# Capture Video from webcam
cap = cv2.VideoCapture(0)

while True:
	# Read webcam data
	res, frame = cap.read()
	# Flip the video
	frame = cv2.flip(frame, 1)

	# Convert BGR To GRAY
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect circles in the image
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
 
	# ensure at least some circles were found
	if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

	# show the output image
	cv2.imshow("output", frame)
	exit_key = cv2.waitKey(5)
	if exit_key == 27:
		break

# Necessary exit procedure
cap.release()
cv2.destroyAllWindows()