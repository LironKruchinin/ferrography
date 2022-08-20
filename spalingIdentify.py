# This file gets ferrography photos, and calculates each spalling fragment in the photo
# and we have live calculation of each spalling.
# First we convert the img to HSV and we get a slider that we can change the values of H and V.
# After the that we convert the mask to Black and white to get the spalling chips,
# and we draw on each spall a contour that we get the values of x, y, w, h.
# The drawing of the box and text works on the values of the x, y, w, h.
# The calculation function works on getting the top left point of the contour, 
# and then drawing an imaginary line to the bottom right point of the contour. 
# After that we get the rough distance between each point. In the end we display live the alternications each millisecond.
# The complexity of stop on each img is O(n log n), not running on each img is O(n^2)

import cv2
import glob
import numpy as np
import math
import os
import tkinter as tk
import getFilePath as filePath
# imports the path that you want to read:


#global variable
global path
global stopOnPhoto
global filterPhoto 
global remClutter
global basicCounter 
global countUnder75 
global counterBetween75 
global counterBetween105 
global counterBetween120 
global overFilter
global overClutter 
global calcPercentageOfPic
global photoArea

photoArea = 1
path = ''
stopOnPhoto = True
filterPhoto = 0
remClutter= 0
basicCounter = 0
countUnder75 = 0
counterBetween75 = 0
counterBetween105 = 0
counterBetween120 = 0
calcPercentageOfPic = 0

overFilter = 15
overClutter = 196

path = glob.glob(f'{filePath.saveFilePath}/*.jpg')

pathOutPut = glob.glob('/Output photo*.jpg')

# askopenfilenames(parent=window, title='Select files')
# print(pa)
#trackbar callback fucntion to update HSV value
def callback(x):
	pass


#create a seperate window named 'Clutter controller' for trackbar
def photo():
	cv2.namedWindow('Clutter controller',2)
	cv2.resizeWindow("Clutter controller", 670,10)

	#create trackbars
	cv2.createTrackbar('Filter','Clutter controller',overFilter,50,callback)
	cv2.createTrackbar('Clutter','Clutter controller',overClutter,255,callback)

	# stopOnPhoto = True
	global filterPhoto
	global remClutte
	global countUnder75
	global basicCounter
	global counterBetween75
	global counterBetween105
	global counterBetween120
	global calcPercentageOfPic


	# If true, we stop on photos, If false we run and calculate all photos
	if stopOnPhoto:

		# Checks if path is empty, if not we run on script (to negate error on empty path) 
		if len(path) > 0:

			for file in path:

				while(1):

						# read source image
						img = cv2.imread(file)

						# convert sourece image to HSC color mode
						hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
					
						# this function gets img pixels
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
						# making mask for hsv range
						mask = cv2.inRange(hsv, hsremClutter, hsv_high)
						# masking HSV value selected color becomes black
						res = cv2.bitwise_and(img, img, mask=mask)


						contours, heirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
						cv2.drawContours(img, contours, -1, (0,0,0), 1)
						contours=[cv2.boundingRect(cnt) for cnt in contours]

						for cnt in contours:
							global x,y,w,h
							x,y,w,h = cnt
							distancePoints = math.dist([w + x, h + y] , [x, y])
							distancePoints = round(distancePoints, 3)

							if distancePoints > 45 and distancePoints < 70:
								# counterBetween75 += 1
								cv2.rectangle(img, (x,y-5),(x+w,y+h), (12,13,205),1)
								cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
								# cv2.imwrite("Output photo/"+imgName, img)
								# print("The file has exceded 75 microns: ", imgName)
							
							if distancePoints > 70 and distancePoints < 105:
								# counterBetween75 += 1
								cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
								cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
								# print("The file has exceded 75 microns: ", file)

							if distancePoints > 105 and distancePoints < 120:
								# counterBetween105 += 1
								cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
								cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
								# print("The file has exceded 105 microns: ", file)

				
							if distancePoints > 120:
								# counterBetween120 += 1
								cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
								cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
								# print("The file has exceded 120 microns: ", file)

							# if distancePoints > 0 and distancePoints < 75:
								# basicCounter += 1
								# cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
								# cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

						getImgPixels()
						#show image
						cv2.imshow('mask',mask)
						cv2.imshow('original',img)
						# img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)
						# cv2.imshow('res',res)
			

			
						#waitfor the user to press escape and break the while loop 
						k = cv2.waitKey(1) & 0xFF
						if k == 27:
							break

		lastFilterPhotoPos = cv2.getTrackbarPos('Filter','Clutter controller')
		lastremClutterPos = cv2.getTrackbarPos('Clutter','Clutter controller')



	else:

			if len(path) > 0:


				for file in path:
					imgPath = file
					# print(imgPath.split('\\'))
					imgPath = imgPath.split('/')
					imgName = imgPath[len(imgPath) - 1]
					# print(imgName)
					#read source image
					img = cv2.imread(file)
					#convert sourece image to HSC color mode
					hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
				

					def getImgPixels():
						global orgW, orgH, photoArea
						microns = 0
						orgW = hsv.shape[0]
						orgH = hsv.shape[1]
						if orgH > 1280 or orgH < 1280:
							microns = float(orgH) / 1294.57
						if float(microns) == 0:
							microns = 1

						photoArea = orgW * orgH
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
						
						if distancePoints > 0 and distancePoints < 70:
							countUnder75 += 1
							# cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
							# cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
						
						if distancePoints > 45 and distancePoints < 70:
							# counterBetween75 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (10,240,240),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
							cv2.imwrite(f'{filePath.saveFilePath}/Suspects/'+imgName, img)
							# print("The file has exceded 75 microns: ", imgName)
      
						if distancePoints > 70 and distancePoints < 105:
							counterBetween75 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
							cv2.imwrite(f'{filePath.saveFilePath}/75 Micron/'+imgName, img)
							# print("The file has exceded 75 microns: ", imgName)

						if distancePoints > 105 and distancePoints < 120:
							counterBetween105 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
							cv2.imwrite(f'{filePath.saveFilePath}/105 Micron/'+imgName, img)
							# print("The file has exceded 105 microns: ", imgName)

			
						if distancePoints > 120:
							counterBetween120 += 1
							cv2.rectangle(img, (x,y-5),(x+w,y+h), (236,240,24),1)
							cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
							cv2.imwrite(f'{filePath.saveFilePath}/120 Micron/'+imgName, img)
							# print("The file has exceded 120 microns: ", imgName)

						if distancePoints > 0 and distancePoints < 70:
							basicCounter += 1
							calcPercentageOfPic += distancePoints
							# cv2.rectangle(img, (x,y-4),(x+w,y+h), (255,155,0),1)
							# cv2.putText(img, str(distancePoints), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

					getImgPixels()
					#show image
					# cv2.imshow('mask',mask)
					# img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)
					cv2.imshow('original',img)
					# cv2.imshow('res',res)
		

		
					#waitfor the user to press escape and break the while loop 
					k = cv2.waitKey(1) & 0xFF
					if k == 27:
						break


			calcPercentageOfPic = ((calcPercentageOfPic * 100) / photoArea)
			# print(photoArea)
			# print("--------")
			# print("Below 75 micron", basicCounter)
			# print("Between 75 micron",counterBetween75)
			# print("Between 105 micron", counterBetween105)
			# print("Between 120 micron",counterBetween120)
			# print("Total surface of spalling is ", calcPercentageOfPic)
			# print(len(pathOutPut), "photos have exceded the limits")
			# print("--------")


				
	# destroys all window
	cv2.destroyAllWindows()




