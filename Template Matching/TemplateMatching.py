# Copyright 2017 Keval Khara kevalk@bu.edu

import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0;
    var_t = 0;
    location = [0, 0];

    # Calculating the mean and variance of template pixel values 
    mean_t = np.mean(temp)
    var_t = np.var(temp)
    print("Mean of temp: ", np.mean(temp))
    print("Variance of temp: ", np.var(temp))

    max_corr = 0;
    # Sliding window in source image to find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0;
            var_s = 0;
            corr = 0;

            # Calculating the mean and variance of source image pixel values inside window
            mean_s = np.mean(src)
            var_s = np.var(src)
            print("Mean of source: ", np.mean(src))
            print("Variance of source: ", np.var(src))

            # Calculating normalized correlation coefficient (NCC) between source and template
            for k in range(0, temp.shape[0]):
                for l in range(0, temp.shape[1]):
                    corr += (src[k+i,l+j] - mean_s) * (temp[k,l] - mean_t)
            corr = corr / (temp.shape[0] * temp.shape[1] * var_t * var_s)
            print("NCC = " + str(corr))

            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
    return location

# load source and template images
source_img = cv2.imread('Capture1.png',0)   # read image in grayscale
temp = cv2.imread('Capture2.png',0)     # read image in grayscale
location = TemplateMatching(source_img, temp, 20);
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Drawing a red rectangle
match_img = cv2.rectangle(match_img, (location[1], location[0]), (location[1] + temp.shape[1], location[0] + temp.shape[0]), (0,0,255),3)

# Saving the template matching result image 
cv2.imwrite('template matching.png', match_img)

# Displaying the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
