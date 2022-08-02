import cv2
  
originalImage = cv2.imread('photos/2101903x10.4.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# grayImage, imports the photo
# sensitivity of the white : 
# 0 - Ultra sensitive    255 - not sensitive
# best value 127... for low res photos 135 works best
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 136, 255, cv2.THRESH_BINARY) 




# blackAndWhiteImage = cv2.erode(blackAndWhiteImage, None, iterations=1)
# blackAndWhiteImage = cv2.dilate(blackAndWhiteImage, None, iterations=0)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)
cv2.imshow('Black white image', blackAndWhiteImage)
  
cv2.waitKey(0)
cv2.destroyAllWindows()