import numpy as np
import cv2

# Haar Cascade for A credits:
# https://raw.githubusercontent.com/Aravindlivewire/Opencv/master/haarcascade/aGest.xml



# Import cascade classifier
a_cascade = cv2.CascadeClassifier('aGest.xml')

cap = cv2.VideoCapture(0)

# To record the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('A gesture detected.avi', fourcc, 10.0, (640,480))
while True:
	ret, img = cap.read()
	# Flip video
	img = cv2.flip(img, 1)
	# Convert to gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Detect A gesture
	sign_a = a_cascade.detectMultiScale(gray, 1.3, 5)	
	if sign_a is not ():
		print "a"
	for (x,y,w,h) in sign_a:
		cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2)
	
	# To record the video
	out.write(img)
	# Display video & Exit procedure
	cv2.imshow('img', img)
	key = cv2.waitKey(1) & 0xFF
	if key == 27:
		break

# Necessary Exit Procedure
out.release() # To record the video
cap.release()
cv2.destroyAllWindows()