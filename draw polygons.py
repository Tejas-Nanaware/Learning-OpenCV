import numpy as np
import cv2
img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,1), (60,70), (255,0,0), 6) #source, (plot points), (BGR Color), thickness

cv2.rectangle(img, (12,12), (60,70), (255,255,0), 5) #source, (top points), (bottom points), (BGR Color), thickness

cv2.circle(img, (100, 120), 25, (0,0,255), -1) #souce, (center), radius, (BGR Color), -1 for fill

pts = np.array([[1,43], [42,44], [25,12], [54,54], [76,35]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], False, (0,255,0), 3) #src, points, join first and last, color, thickness

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'SUP', (130,130), font, 1, (0,0,0), 2, cv2.LINE_AA) #src, text, start pos, font, size, color, thickness, anti aliasing

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)