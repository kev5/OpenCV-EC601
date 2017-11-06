# Copyright 2017 Keval Khara kevalk@bu.edu

img=cv2.imread('Test_images/baboon.jpg')
cv2.imshow('Original',img)

noise_img=img.copy()
mean=0
sigma=50
Add_gaussian_Noise(noise_img,mean,sigma)
cv2.imshow('Gaussian Noise',noise_img)

noise_dst=noise_img.copy()
cv2.blur(noise_dst,(3,3))
cv2.imshow('Box filter',noise_dst)

noise_dst1=noise_img.copy()
cv2.GaussianBlur(noise_dst1,(3,3),1.5)
cv2.imshow('GaussianBlur filter',noise_dst1)

noise_dst2=noise_img.copy()
cv2.medianBlur(noise_dst2,3)
cv2.imshow('Median filter',noise_dst2)
