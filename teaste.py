import cv2
import glob
import numpy as np
import math


# imports the path that you want to read:
path = glob.glob('photos/*.jpg')



#global variable
filterPhoto = 0
remClutter= 0

stopOnPhoto = 0
basicCounter = 0
counterBetween75 = 0
counterBetween105 = 0
counterBetween120 = 0

#trackbar callback fucntion to update HSV value
def callback(x):
	global filterPhoto, remClutter
	#assign trackbar position value to H,S,V High and low variable
	filterPhoto = cv2.getTrackbarPos('Filter','Clutter controller')
	remClutter = cv2.getTrackbarPos('Clutter','Clutter controller')


#create a seperate window named 'Clutter controller' for trackbar
cv2.namedWindow('Clutter controller',2)
cv2.resizeWindow("Clutter controller", 670,10);

#create trackbars
cv2.createTrackbar('Filter','Clutter controller',16,50,callback)
cv2.createTrackbar('Clutter','Clutter controller',175,255,callback)

# print(path)
if len(path) > 0:
	for file in path:
		while(1):
			#read source image
			img = cv2.imread(file)
			#convert sourece image to HSC color mode
			hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


			hsremClutter = np.array([filterPhoto, 0, remClutter], np.uint8)
			hsv_high = np.array([180, 255, 255], np.uint8)



			######################################################
			#making mask for hsv range
			mask = cv2.inRange(hsv, hsremClutter, hsv_high)
			#masking HSV value selected color becomes black
			res = cv2.bitwise_and(img, img, mask=mask)


			contours, heirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
			cv2.drawContours(img, contours, -1, (0,0,0), 1)
			for c in contours:
				rect = cv2.boundingRect(c)
				x,y,w,h = rect
				distancePoints = math.dist([w + x, h + y] , [x, y])
				distancePoints = round(distancePoints, 3)
    
				if distancePoints > 75 and distancePoints < 90:
					counterBetween75 += 1
					cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
					cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
					print("The file has exceded 75 microns: ", file)

				if distancePoints > 90 and distancePoints < 110:
					counterBetween105 += 1
					cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
					cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
					print("The file has exceded 105 microns: ", file)

     
				if distancePoints > 110:
					counterBetween120 += 1
					cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
					cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
					print("The file has exceded 120 microns: ", file)

				if distancePoints > 0 and distancePoints < 75:
					basicCounter += 1
					# cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
					# cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

			#show image
			# cv2.imshow('mask',mask)
			cv2.imshow('original',img)
			# cv2.imshow('res',res)
		

		
			#waitfor the user to press escape and break the while loop 
			k = cv2.waitKey(1) & 0xFF
			if k == 27:
				break
				
#destroys all window
cv2.destroyAllWindows()
numOfObj= len(contours)
print("Below 75 micron", numOfObj)
print("Between 75 micron",counterBetween75)
print("Between 105 micron", counterBetween105)
print("Between 120 micron",counterBetween120)
