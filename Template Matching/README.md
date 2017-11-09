There is an easier and faster way for template matching which can be achieved by using the OpenCV function matchTemplate which has 
6 methods namely - 

**1. method=CV_TM_SQDIFF -** 

                ![](https://docs.opencv.org/2.4/_images/math/f096a706cb9499736423f10d901c7fe13a1e6926.png)

**2. method=CV_TM_SQDIFF_NORMED**

                ![](https://docs.opencv.org/2.4/_images/math/6d6a720237b3a4c1365c8e86a9cfcf0895d5e265.png)

**3. method=CV_TM_CCORR**

                ![](https://docs.opencv.org/2.4/_images/math/93f1747a86a3c5095a0e6a187442c6e2a0ae0968.png)

**4. method=CV_TM_CCORR_NORMED**

                ![](https://docs.opencv.org/2.4/_images/math/6a72ad9ae17c4dad88e33ed16308fc1cfba549b8.png)

**5. method=CV_TM_CCOEFF**

                ![](https://docs.opencv.org/2.4/_images/math/6d8865ea008412bdc246ace6f5a3fe0991502881.png)
        where,
                ![](https://docs.opencv.org/2.4/_images/math/ffb6954b6020b02e13b73c79bd852c1627cfb79c.png)

**6. method=CV_TM_CCOEFF_NORMED**

                ![](https://docs.opencv.org/2.4/_images/math/235e42ec68d2d773899efcf0a4a9d35a7afedb64.png)

The reason that the OpenCV methods are so fast is because -

1. Instead of going having 4 for loops like in our program above, they use Fast Fourier Transform (FFT) techinique to find the cross 
correlation between the original image and the template image.

2. In simple language, the OpenCV method suppresses all features within the image that do not have the same features as the template. 
The image is then converted back using a Inverse Fast Fourier Transform (IFFT) to produce images where high values mean a match and 
low values mean the opposite. This image is often normalised so 1's represent a match and 0's or near 0's mean the object is not
present in the original image.

3. Hence, the amount of operations required is far less. Moreover, OpenCV is highly optimised C++ code and runs faster than the Python
code.
