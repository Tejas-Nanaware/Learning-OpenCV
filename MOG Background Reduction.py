import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Create Background reductor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)
	fgmask = fgbg.apply(frame)

	cv2.imshow('original', frame)
	cv2.imshow('fg', fgmask)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()