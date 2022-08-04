import cv2
import glob
import numpy as np
import math


# imports the path that you want to read:
path = glob.glob('photos/*.jpg')

imageScalePercent = 70
basicCounter = 0
counterBetween75 = 0
counterBetween105 = 0
counterBetween120 = 0

# print(path)
if len(path) > 0:
   for file in path:
      originalImage = cv2.imread(file)
      grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
      def getImgPixels():
         microns = 0
         (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 1, 255, cv2.THRESH_BINARY) 
         orgW = grayImage.shape[0]
         orgH = grayImage.shape[1]
         if orgH > 1280:
            microns = orgH / 1294.57
         if float(microns):
            microns = math.ceil(microns)
         if microns < 1:
            microns = 1
         # print(orgW, orgH, microns)

      (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 135, 255, cv2.THRESH_BINARY) 
      kernel=np.ones((2,2),np.uint8)
      dilated=cv2.dilate(blackAndWhiteImage, kernel, iterations=1)

      # original image rescaling
      width = int(originalImage.shape[1] * imageScalePercent / 100)
      height = int(originalImage.shape[0] * imageScalePercent / 100)
      dim = (width, height)
      originalImage = cv2.resize(originalImage, dim, interpolation = cv2.INTER_AREA)

      #to calculate micron we have to get the image width and height
      # after that we divide 
      (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 135, 255, cv2.THRESH_BINARY) 
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
      # cv2.drawContours(originalImage, contours, -1, (0,0,0), 1)
      contours=[cv2.boundingRect(cnt) for cnt in contours]


      for cnt in contours:
         x,y,w,h = cnt
         x2 = w + x
         x1 = x 
         y1 = y
         y2 = h + y
         XYDistance = math.dist([x2,y2], [x1,y1])
         XYDistance = round(XYDistance, 4)
         # if XYDistance > 3

         if XYDistance > 75 and XYDistance < 90:
            counterBetween75 += 1
            cv2.rectangle(originalImage, (x,y-4),(x+w,y+h), (255,155,0),1)
            cv2.putText(originalImage, str(XYDistance), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
            print("The file that exceded 75 microns: ", file)

         if XYDistance > 90 and XYDistance < 110:
            counterBetween105 += 1
            cv2.rectangle(originalImage, (x,y-4),(x+w,y+h), (255,0,0),1)
            cv2.putText(originalImage, str(XYDistance), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (19, 0, 0), 1)
            print("The file that exceded 105 microns: ", file)

         if XYDistance > 110:
            counterBetween120 += 1
            cv2.rectangle(originalImage, (x,y-4),(x+w,y+h), (255,155,0),1)
            cv2.putText(originalImage, str(XYDistance), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
            print("The file that exceded 120 microns: ", file)

         ########## to see all of the boxes we change the 45 to 2 so basic filtration works
         if XYDistance > 3 and XYDistance < 75: 
            basicCounter += 1     
            # cv2.rectangle(originalImage, (x,y-4),(x+w,y+h), (255,155,0),1)
            # cv2.putText(originalImage, str(XYDistance), (x, y-9), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)


      getImgPixels()
      cv2.imshow("Image", originalImage)
      cv2.waitKey(0)
      cv2.destroyAllWindows()


print("Below 75 micron", basicCounter)
print("Between 75 micron",counterBetween75)
print("Between 105 micron", counterBetween105)
print("Between 120 micron",counterBetween120)