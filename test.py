import cv2
import numpy as np
import math

originalImage = cv2.imread('2101903x10.2.jpg', cv2.IMREAD_UNCHANGED)
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
imageScalePercent = 40


# creates black and white image
# grayImage, imports the photo
# sensitivity of the white : 
# 0 - Ultra sensitive    255 - not sensitive
# best value 127... for low res photos 135 works best
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 140, 255, cv2.THRESH_BINARY) 

kernel=np.ones((2,2),np.uint8)
dilated=cv2.dilate(blackAndWhiteImage, kernel, iterations=1)



# original image rescaling
width = int(originalImage.shape[1] * imageScalePercent / 100)
height = int(originalImage.shape[0] * imageScalePercent / 100)
dim = (width, height)
originalImage = cv2.resize(originalImage, dim, interpolation = cv2.INTER_AREA)

#gray image rescale
width = int(grayImage.shape[1] * imageScalePercent / 100)
height = int(grayImage.shape[0] * imageScalePercent / 100)
dim = (width, height)
grayImage = cv2.resize(grayImage, dim, interpolation = cv2.INTER_AREA)

# black and white rescale
width = int(dilated.shape[1] * imageScalePercent / 100)
height = int(dilated.shape[0] * imageScalePercent / 100)
dim = (width, height)
dilated = cv2.resize(dilated, dim, interpolation = cv2.INTER_AREA)



contours, heirarchy = cv2.findContours(dilated, 
                                       cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(originalImage, contours, -1, (0,0,255), 1)
contours=[cv2.boundingRect(cnt) for cnt in contours]

for cnt in contours:
   x,y,w,h = cnt
   x2 = w + x
   x1 = x 
   y1 = y
   y2 = h + y
   XYDistance = math.dist([x2,y2], [x1,y1])
   cv2.rectangle(originalImage, (x,y),(x+w,y+h), (255,155,0),1)
   cv2.putText(originalImage, str(XYDistance), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
   print(x, y)
   print(w, h)
   print(x+w, y+h)
   print(XYDistance)
   print("____________")

cv2.imshow('Gray image', grayImage)
cv2.imshow('Black white image', dilated)
cv2.imshow('Original image',originalImage)



cv2.waitKey(0)
cv2.destroyAllWindows()



#https://youtu.be/efWITgemKvs?t=1845