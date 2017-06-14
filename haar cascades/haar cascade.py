import cv2
import numpy as np

# https://github.com/opencv/opencv/tree/master/data/haarcascades
# HaarCascade Credits ^

# Get the cascade classifer
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	#flip video
	img = cv2.flip(img, 1)
	#converting to gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# detect face
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	# To display faces and eyes
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		# Detect eyes
		eyes = eye_cascade.detectMultiScale(roi_gray)
		# To display Eyes
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
	
	# Display video & Exit procedure
	cv2.imshow('img', img)
	key = cv2.waitKey(1) & 0xFF
	if key == 27:
		break

# Necessary Exit Procedure
cap.release()
cv2.destroyAllWindows()