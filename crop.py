# Crops an image

import cv2
import numpy as np

img = cv2.imread('bu.png',1)

cropped_img = img[170:300, 85:200]

cv2.namedWindow('Original image', cv2.WINDOW_NORMAL)

cv2.namedWindow('Cropped image', cv2.WINDOW_NORMAL)

cv2.imshow('Original image', img)

cv2.imshow('Cropped image', cropped_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
