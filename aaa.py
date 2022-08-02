import cv2 as cv#read the image
img = cv.imread("pat.jpeg")
#convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blur image to reduce the noise in the image while thresholding. #This smoothens the sharp edges in the image.

blur = cv.blur(gray, (10,10))

#Apply thresholding to the image

ret, thresh = cv.threshold(blur, 1, 255, cv.THRESH_OTSU)
#find the contours in the image
contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#draw the obtained contour lines(or the set of coordinates forming a line) on the original image
cv.drawContours(img, contours, -1, (0,255,0), 5)
#show the image
cv.namedWindow('Contours',cv.WINDOW_NORMAL)
cv.namedWindow('Thresh',cv.WINDOW_NORMAL)
cv.imshow('Contours', img)
cv.imshow('Thresh', thresh)
cv.waitKey(0)
cv.destroyAllWindows()