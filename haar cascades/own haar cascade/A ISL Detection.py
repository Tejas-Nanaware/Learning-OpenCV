import cv2
import numpy as np

# Get the cascade classifer
# Cascade Credits Tejas Nanaware
# Note the gesture is detected on white background as I used that while generating
A_cascade = cv2.CascadeClassifier('A-ISL-11 Stages.xml')

cap = cv2.VideoCapture(0)

# To record the video
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('A gesture detected.avi', fourcc, 10.0, (640,480))
while True:
	ret, img = cap.read()
	#flip video
	img = cv2.flip(img, 1)
	#converting to gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# detect face
	A = A_cascade.detectMultiScale(gray)

	# To display faces and eyes
	for (x,y,w,h) in A:
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

	# To record the video
	# out.write(img)		
	# Display video & Exit procedure
	cv2.imshow('img', img)
	key = cv2.waitKey(1) & 0xFF
	if key == 27:
		break

# Necessary Exit Procedure
# out.release() # To record the video
cap.release()
cv2.destroyAllWindows()