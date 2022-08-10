import cv2
import glob
import numpy as np
import math

path = glob.glob('photos/*.jpg')

imageScalePercent = 70
basicCounter = 0
counterBetween75 = 0
counterBetween105 = 0
counterBetween120 = 0

if len(path) > 0:
    for file in path:
        originalImage = cv2.imread(file)
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
        def getImgPixels():
            microns = 0
            orgW = grayImage.shape[0]
            orgH = grayImage.shape[1]
            if orgH > 1280:
                microns = orgH / 1294.57
            if float(microns):
                microns = math.ceil(microns)
            if microns < 1:
                microns = 1
            # print(orgW, orgH, microns)

        def callback(x):
            global H_low,H_high,S_low,S_high,V_low,V_high
            #assign trackbar position value to H,S,V High and low variable
            H_low = cv2.getTrackbarPos('low H','controls')
            H_high = cv2.getTrackbarPos('high H','controls')
            S_low = cv2.getTrackbarPos('low S','controls')
            S_high = cv2.getTrackbarPos('high S','controls')
            V_low = cv2.getTrackbarPos('low V','controls')
            V_high = cv2.getTrackbarPos('high V','controls')
            #trackbar callback fucntion to update HSV value

        #create a seperate window named 'controls' for trackbar
        cv2.namedWindow('controls',2)
        cv2.resizeWindow("controls", 550,10)

        #global variable
        H_low = 0
        H_high = 179
        S_low= 0
        S_high = 255
        V_low= 0
        V_high = 255

        #create trackbars for high,low H,S,V 
        cv2.createTrackbar('low H','controls',0,180,callback)
        cv2.createTrackbar('high H','controls',180,180,callback)

        cv2.createTrackbar('low S','controls',0,255,callback)
        cv2.createTrackbar('high S','controls',255,255,callback)

        cv2.createTrackbar('low V','controls',0,255,callback)
        cv2.createTrackbar('high V','controls',255,255,callback)





# while(1):
# 	#read source image
# 	img=cv2.imread("photos/2008924x10.3.jpg")
# 	#convert sourece image to HSC color mode
# 	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 	#
# 	hsv_low = np.array([H_low, S_low, V_low], np.uint8)
# 	hsv_high = np.array([H_high, S_high, V_high], np.uint8)

# 	#making mask for hsv range
# 	mask = cv2.inRange(hsv, hsv_low, hsv_high)
# 	# print (mask)
# 	#masking HSV value selected color becomes black
# 	res = cv2.bitwise_and(img, img, mask=mask)



# 	#show image
# 	cv2.imshow('mask',mask)
# 	cv2.imshow('original',img)
# 	cv2.imshow('res',res)
	
# 	#waitfor the user to press escape and break the while loop 
# 	k = cv2.waitKey(1) & 0xFF
# 	if k == 27:
# 		break
		
# #destroys all window
# cv2.destroyAllWindows()