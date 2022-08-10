import cv2
import glob
import numpy as np
import math
import os

# imports the path that you want to read:
path = glob.glob('photos/*.jpg')
pathOutPut = glob.glob('Output photo/*.jpg')


#global variable
filterPhoto = 0
remClutter= 0

stopOnPhoto = False
basicCounter = 0
counterBetween75 = 0
counterBetween105 = 0
counterBetween120 = 0

#trackbar callback fucntion to update HSV value
def callback(x):
	pass


#create a seperate window named 'Clutter controller' for trackbar
cv2.namedWindow('Clutter controller',2)
cv2.resizeWindow("Clutter controller", 670,10)

#create trackbars
cv2.createTrackbar('Filter','Clutter controller',15,50,callback)
cv2.createTrackbar('Clutter','Clutter controller',196,255,callback)
# print(path)
if stopOnPhoto:

	if len(path) > 0:

		for file in path:

			while(1):

			#read source image
					img = cv2.imread(file)
					#convert sourece image to HSC color mode
					hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
				

					def getImgPixels():
						microns = 0
						orgW = hsv.shape[0]
						orgH = hsv.shape[1]
						if orgH > 1280 or orgH < 1280:
							microns = float(orgH) / 1294.57
						if float(microns) == 0:
							microns = 1
						# print(orgW, orgH, microns)

					filterPhoto = cv2.getTrackbarPos('Filter','Clutter controller')
					remClutter = cv2.getTrackbarPos('Clutter','Clutter controller')
					hsremClutter = np.array([filterPhoto, 0, remClutter], np.uint8)
					hsv_high = np.array([180, 255, 255], np.uint8)



					######################################################
					#making mask for hsv range
					mask = cv2.inRange(hsv, hsremClutter, hsv_high)
					#masking HSV value selected color becomes black
					res = cv2.bitwise_and(img, img, mask=mask)


					contours, heirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
					cv2.drawContours(img, contours, -1, (0,0,0), 1)
					contours=[cv2.boundingRect(cnt) for cnt in contours]

					for cnt in contours:
						global x,y,w,h
						x,y,w,h = cnt
						distancePoints = math.dist([w + x, h + y] , [x, y])
						distancePoints = round(distancePoints, 3)

						if distancePoints > 50 and distancePoints < 75:
							# counterBetween75 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (12,13,205),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (170, 255, 198), 1)
							# cv2.imwrite("Output photo/"+imgName, img)
							# print("The file has exceded 75 microns: ", imgName)
						
						if distancePoints > 70 and distancePoints < 100:
							# counterBetween75 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
							# print("The file has exceded 75 microns: ", file)

						if distancePoints > 100 and distancePoints < 120:
							# counterBetween105 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
							# print("The file has exceded 105 microns: ", file)

			
						if distancePoints > 120:
							# counterBetween120 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
							# print("The file has exceded 120 microns: ", file)

						# if distancePoints > 0 and distancePoints < 75:
							# basicCounter += 1
							# cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
							# cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

					getImgPixels()
					#show image
					cv2.imshow('mask',mask)
					cv2.imshow('original',img)
					img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)
					# cv2.imshow('res',res)
		

		
					#waitfor the user to press escape and break the while loop 
					k = cv2.waitKey(1) & 0xFF
					if k == 27:
						break





else:

		if len(path) > 0:
			if not os.path.exists('Output photo'):
				os.mkdir('Output photo')

			for file in path:
				imgPath = file
				# print(imgPath.split('\\'))
				imgPath = imgPath.split('\\')
				imgName = imgPath[len(imgPath) - 1]
				# print(imgName)
				#read source image
				img = cv2.imread(file)
				#convert sourece image to HSC color mode
				hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			

				def getImgPixels():
					microns = 0
					orgW = hsv.shape[0]
					orgH = hsv.shape[1]
					if orgH > 1280 or orgH < 1280:
						microns = float(orgH) / 1294.57
					if float(microns) == 0:
						microns = 1
					# print(orgW, orgH, microns)

				filterPhoto = cv2.getTrackbarPos('Filter','Clutter controller')
				remClutter = cv2.getTrackbarPos('Clutter','Clutter controller')
				hsremClutter = np.array([filterPhoto, 0, remClutter], np.uint8)
				hsv_high = np.array([180, 255, 255], np.uint8)



				######################################################
				#making mask for hsv range
				mask = cv2.inRange(hsv, hsremClutter, hsv_high)
				#masking HSV value selected color becomes black
				res = cv2.bitwise_and(img, img, mask=mask)


				contours, heirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
				cv2.drawContours(img, contours, -1, (0,0,0), 1)
				contours=[cv2.boundingRect(cnt) for cnt in contours]

				for cnt in contours:
					x,y,w,h = cnt
					distancePoints = math.dist([w + x, h + y] , [x, y])
					distancePoints = round(distancePoints, 3)
					
					if distancePoints > 50 and distancePoints < 75:
						cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
						cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
					
					if distancePoints > 70 and distancePoints < 105:
						counterBetween75 += 1
						cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
						cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
						cv2.imwrite("Output photo/"+imgName, img)
						print("The file has exceded 75 microns: ", imgName)

					if distancePoints > 105 and distancePoints < 120:
						counterBetween105 += 1
						cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
						cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
						cv2.imwrite("Output photo/"+imgName, img)
						print("The file has exceded 105 microns: ", imgName)

		
					if distancePoints > 120:
						counterBetween120 += 1
						cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
						cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
						cv2.imwrite("Output photo/"+imgName, img)
						print("The file has exceded 120 microns: ", imgName)

					if distancePoints > 0 and distancePoints < 75:
						basicCounter += 1
						# cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
						# cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

				getImgPixels()
				#show image
				# cv2.imshow('mask',mask)
				cv2.imshow('original',img)
				# cv2.imshow('res',res)
				# img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)
	

	
				#waitfor the user to press escape and break the while loop 
				k = cv2.waitKey(1) & 0xFF
				if k == 27:
					break

		print()
		print("--------")
		print("Below 75 micron", basicCounter)
		print("Between 75 micron",counterBetween75)
		print("Between 105 micron", counterBetween105)
		print("Between 120 micron",counterBetween120)
		print(len(pathOutPut), "photos have exceded the limits")
		print("--------")

# destroys all window
cv2.destroyAllWindows()

