There is an easier and faster way for template matching which can be achieved by using the OpenCV function matchTemplate which has 
6 methods namely - 

**1. method=CV_TM_SQDIFF**
R(x,y)= \sum _{x',y'} (T(x',y')-I(x+x',y+y'))^2

**2. method=CV_TM_SQDIFF_NORMED**
R(x,y)= \frac{\sum_{x',y'} (T(x',y')-I(x+x',y+y'))^2}{\sqrt{\sum_{x',y'}T(x',y')^2 \cdot \sum_{x',y'} I(x+x',y+y')^2}}

**3. method=CV_TM_CCORR**
R(x,y)= \sum _{x',y'} (T(x',y')  \cdot I(x+x',y+y'))

**4. method=CV_TM_CCORR_NORMED**
R(x,y)= \frac{\sum_{x',y'} (T(x',y') \cdot I(x+x',y+y'))}{\sqrt{\sum_{x',y'}T(x',y')^2 \cdot \sum_{x',y'} I(x+x',y+y')^2}}

**5. method=CV_TM_CCOEFF**
R(x,y)= \sum _{x',y'} (T'(x',y')  \cdot I(x+x',y+y'))

where

\begin{array}{l} T'(x',y')=T(x',y') - 1/(w  \cdot h)  \cdot \sum _{x'',y''} T(x'',y'') \\ I'(x+x',y+y')=I(x+x',y+y') - 
1/(w  \cdot h)  \cdot \sum _{x'',y''} I(x+x'',y+y'') \end{array}

**6. method=CV_TM_CCOEFF_NORMED**
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
