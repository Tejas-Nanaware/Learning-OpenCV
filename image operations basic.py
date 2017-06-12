import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55,55] #locate a pixel
print px
img[55,55] = [255,255,255] #modify pixel
print px

roi = img[100:150, 100:150]
# print roi
# img[100:150, 100:150] = [255,255,255] #put white patch on roi

watch_face = img[57:130, 97:170]
#130-57=73 170-97=73
img[0:73, 0:73] = watch_face #copy paste watch_face to new location

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()