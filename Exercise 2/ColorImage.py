# Copyright 2017 Keval Khara kevalk@bu.edu

import cv2

img = cv2.imread('Test_images/baboon.jpg')	# read the image

[b,g,r] = cv2.split(img) #split into color channels

cv2.imshow('Blue',b)
cv2.imwrite('Blue.png',b)
cv2.imshow('Red',r) 
cv2.imwrite('Red.png',r)
cv2.imshow('Green',g)
cv2.imwrite('Green.png',g)

ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)	#convert to YCrCb

[y,Cb,Cr] = cv2.split(ycrcb_img) #split YCrCb channels

cv2.imshow('Y',y)
cv2.imwrite('Y.png',y)
cv2.imshow('Cb',Cb)
cv2.imwrite('Cb.png',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('Cr.png',Cr)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)	# convert to HSV

[h,s,v] = cv2.split(hsv_img)	# split into HSV channells

cv2.imshow('Hue',h)
cv2.imwrite('Hue.png',h)
cv2.imshow('Saturation',s)
cv2.imwrite('Saturation.png',s)
cv2.imshow('Value',v)
cv2.imwrite('Value.png',v)

cv2.waitKey(0)
