import cv2
import numpy as np
from skimage import measure


originalImage = cv2.imread('photos/2108901x10.13.jpg', cv2.IMREAD_UNCHANGED)
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)



# creates black and white image
# grayImage, imports the photo
# sensitivity of the white : 
# 0 - Ultra sensitive    255 - not sensitive
# best value 127... for low res photos 135 works best
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 135, 255, cv2.THRESH_BINARY) 



# original image rescaling
scale_percent = 40
width = int(originalImage.shape[1] * scale_percent / 100)
height = int(originalImage.shape[0] * scale_percent / 100)
dim = (width, height)
originalImage = cv2.resize(originalImage, dim, interpolation = cv2.INTER_AREA)

#gray image rescale
scale_percent = 40
width = int(grayImage.shape[1] * scale_percent / 100)
height = int(grayImage.shape[0] * scale_percent / 100)
dim = (width, height)
grayImage = cv2.resize(grayImage, dim, interpolation = cv2.INTER_AREA)

# black and white rescale
scale_percent = 40
width = int(blackAndWhiteImage.shape[1] * scale_percent / 100)
height = int(blackAndWhiteImage.shape[0] * scale_percent / 100)
dim = (width, height)
blackAndWhiteImage = cv2.resize(blackAndWhiteImage, dim, interpolation = cv2.INTER_AREA)



contours, heirarchy = cv2.findContours(blackAndWhiteImage, 
                                       cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(originalImage, contours, -1, (0,255,0), 1)


cv2.imshow('Gray image', grayImage)
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)



cv2.waitKey(0)
cv2.destroyAllWindows()



#https://youtu.be/efWITgemKvs?t=1845
