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

'''
There is an easier and faster way for template matching which can be achieved by using the OpenCV function matchTemplate which has 
6 methods namely - 

1. method=CV_TM_SQDIFF

R(x,y)= \sum _{x',y'} (T(x',y')-I(x+x',y+y'))^2

2. method=CV_TM_SQDIFF_NORMED

R(x,y)= \frac{\sum_{x',y'} (T(x',y')-I(x+x',y+y'))^2}{\sqrt{\sum_{x',y'}T(x',y')^2 \cdot \sum_{x',y'} I(x+x',y+y')^2}}

3. method=CV_TM_CCORR

R(x,y)= \sum _{x',y'} (T(x',y')  \cdot I(x+x',y+y'))

4. method=CV_TM_CCORR_NORMED

R(x,y)= \frac{\sum_{x',y'} (T(x',y') \cdot I(x+x',y+y'))}{\sqrt{\sum_{x',y'}T(x',y')^2 \cdot \sum_{x',y'} I(x+x',y+y')^2}}

5. method=CV_TM_CCOEFF

R(x,y)= \sum _{x',y'} (T'(x',y')  \cdot I(x+x',y+y'))

where

\begin{array}{l} T'(x',y')=T(x',y') - 1/(w  \cdot h)  \cdot \sum _{x'',y''} T(x'',y'') \\ I'(x+x',y+y')=I(x+x',y+y') - 
1/(w  \cdot h)  \cdot \sum _{x'',y''} I(x+x'',y+y'') \end{array}

6. method=CV_TM_CCOEFF_NORMED

R(x,y)= \frac{ \sum_{x',y'} (T'(x',y') \cdot I'(x+x',y+y')) }{ \sqrt{\sum_{x',y'}T'(x',y')^2 \cdot \sum_{x',y'} I'(x+x',y+y')^2} }

The reason that the OpenCV methods are so fast is because -

1. Instead of going having 4 for loops like in our program above, they use Fast Fourier Transform (FFT) techinique to find the cross 
correlation between the original image and the template image.

2. In simple language, the OpenCV method suppresses all features within the image that do not have the same features as the template. 
The image is then converted back using a Inverse Fast Fourier Transform (IFFT) to produce images where high values mean a match and 
low values mean the opposite. This image is often normalised so 1's represent a match and 0's or near 0's mean the object is not
present in the original image.

3. Hence, the amount of operations required is far less. Moreover, OpenCV is highly optimised C++ code and runs faster than the Python
code.
'''
