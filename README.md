# OpenCV-EC601
  - OpenCV Projects and Exercises

## Exercise 1

  **1. How does a program read the cvMat object, in particular, what is the order of the pixel structure?

The pixel values of a cvMat file can be accessed using _cvMatName.at(x,y)_ where we can access a pixel in the matrix structure where (x,y) is the position and (0,0) position is at the top left corner of the matrix.

## Exercise 2

  **1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.


  **2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?
