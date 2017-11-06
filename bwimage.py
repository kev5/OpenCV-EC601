# Converts an RGB image into grayscale and saves it in the same directory

import cv2
import numpy as np

img = cv2.imread('bu.png',0)

cv2.imwrite('saved_bu.png',img)

cv2.namedWindow('B/W image',cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

cv2.imshow('B/W image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
