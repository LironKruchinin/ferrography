import tkinter as tk
from tkinter.filedialog import askopenfilenames, askdirectory
import spalingIdentify as spalling
import graphData as graph
import spectroUI as spectro
import getFilePath as filePath
import glob
import numpy as np
import os
import sys
import shutil

global spectroWindow
global pathTemp
global hourAnswer
spectroWindow = 0
pathTemp = ''
hourAnswer = ''

window = tk.Tk()
window.geometry('350x450')
window.title("Ferrography")

isRunOnPhoto = tk.BooleanVar()

def teset():
   if spectro.spectroWindow.state():
      filePath.ferroSN = textFieldTestSN.get('1.0', 'end-1c')
      spectroSN = spectro.testSNText.get('1.0', 'end-1c')
      
   if spectro.spectroWindow.state() and filePath.ferroSN != spectroSN:
      tk.messagebox.showerror('Serial number Error', f'The serial numbers dont match \n Ferro SN: {filePath.ferroSN} \n Spectro SN: {spectroSN}')
   else:
      spalling.stopOnPhoto = isRunOnPhoto.get()
      if len(spalling.path) > 0:
         if isRunOnPhoto.get():
            spalling.photo()

         else:
            spalling.photo()

   # print(len(spalling.path))
   # print(spalling.counterBetween75)

def runOnPhoto():
   if not os.path.exists(f'{pathTemp}/Output photo'):
      os.mkdir(f'{pathTemp}/Output photo')
   # else:
   #    try:
         # shutil.rmtree(f'{pathTemp}/Output photo')
   #    except:
   #       print('test')
      
   spalling.overFilter = int(textBoxFilter.get('1.0', 'end-1c'))
   spalling.overClutter = int(textBoxClutter.get('1.0', 'end-1c'))
   try: 
      if spectro.spectroWindow.state():
         filePath.ferroSN = textFieldTestSN.get('1.0', 'end-1c')
         
         spectroSN = filePath.spectroSN

         if filePath.ferroSN != spectroSN:
            tk.messagebox.showerror('Serial number Error', f'The serial numbers dont match \n Ferro SN: {filePath.ferroSN} \n Spectro SN: {spectroSN}')
         
         else:
            spalling.stopOnPhoto = isRunOnPhoto.get()
            if len(spalling.path) > 0:
               if isRunOnPhoto.get():
                  spalling.photo()

               else:
                  spalling.photo()

            else:
               tk.messagebox.showerror('No Data loaded', 'No data was loaded')

   except:
      spalling.stopOnPhoto = isRunOnPhoto.get()
      if len(spalling.path) > 0:
         if isRunOnPhoto.get():
            spalling.photo()
         else:
            spalling.photo()

      else:
         tk.messagebox.showerror('No Data loaded', 'No data was loaded')

   if spalling.counterBetween120 >= 3:
         filePath.hourAnswer = '1'
         print(filePath.hourAnswer)

   elif spalling.counterBetween120 >= 1:
         filePath.hourAnswer = 5
         print(int(filePath.hourAnswer))

   elif spalling.counterBetween105 >= 3:
         filePath.hourAnswer = 10
         print(int(filePath.hourAnswer))

   elif spalling.counterBetween105 >= 1:
         filePath.hourAnswer = 15
         print(int(filePath.hourAnswer))

   elif spalling.counterBetween75 >= 10:
         filePath.hourAnswer = 15
         print(int(filePath.hourAnswer))

   elif spalling.counterBetween75 >= 1:
         filePath.hourAnswer = 27.5
         print(float(filePath.hourAnswer))

   else:
         filePath.hourAnswer = 27.5
         print(float(filePath.hourAnswer))




############################################################################################################
def selFilePath():
   
   global pathTemp
   spalling.path = askopenfilenames(parent=window, title='Select files')
   pathTemp = spalling.path[0]
   pathTemp = ''.join(pathTemp)
   pathTemp = pathTemp.split('/')
   pathTemp.pop()
   pathTemp = '/'.join(pathTemp)
   filePath.saveFilePath = pathTemp
   
   if not os.path.exists(f'{pathTemp}/Output photo'):
      os.mkdir(f'{pathTemp}/Output photo')
   else:
      try:
         shutil.rmtree(f'{pathTemp}/Output photo')
      except:
         print("Error")

   # print(pathTemp)



def resetSpallingCount():
   spalling.countUnder75 = 0
   spalling.basicCounter = 0
   spalling.counterBetween75 = 0
   spalling.counterBetween105 = 0
   spalling.counterBetween120 = 0
   spalling.calcPercentageOfPic = 0



   
                     # UI

# label for Test SN:
labelFieldTestSN = tk.Label(window, text='Test SN:')
labelFieldTestSN.pack()
labelFieldTestSN.place(x = 55, y = 18)

# text field for Test SN:
textFieldTestSN = tk.Text(window, width=20, height=1, font=("Helvetica", 11))
textFieldTestSN.pack()
textFieldTestSN.place(x = 105, y = 20)

# button that imports images
filePathBtn = tk.Button(window, text='Import file', command=selFilePath, 
                        height=1, width=15, bg="#e3e3e3")
filePathBtn.pack()
filePathBtn.place(x = 125, y = 55)

# checkmark for Pause for each photo?
chk1 = tk.Checkbutton(window, text='Pause on each photo?', 
                     variable=isRunOnPhoto, onvalue=True, offvalue=False)
chk1.pack()
chk1.place(x = 110, y = 95)



# label for overwrite default values
labelOverWriteValues = tk.Label(window, text='Overwrite default values:')
labelOverWriteValues.pack()
labelOverWriteValues.place(x = 116, y = 140)

# label for filter
filterLabel = tk.Label(window, text='Filter:')
filterLabel.pack()
filterLabel.place(x = 75, y = 175)

# text box for filter
textBoxFilter = tk.Text(window, width=5, height=1, font=("Helvetica", 11))
textBoxFilter.insert(tk.END, 15)
textBoxFilter.pack()
textBoxFilter.place(x = 110, y = 175)

# label for clutter
ClutterLabel = tk.Label(window, text='Clutter:')
ClutterLabel.pack()
ClutterLabel.place(x = 170, y = 175)

# text box for clutter
textBoxClutter = tk.Text(window, width=5, height=1, font=("Helvetica", 11))
textBoxClutter.insert(tk.END, 196)
textBoxClutter.pack()
textBoxClutter.place(x = 225, y = 175)

# run button
runBtn = tk.Button(window, text="Run", command=lambda:[runOnPhoto()], 
                     height=1, width=10, bg="#e3e3e3", state=tk.NORMAL)
runBtn.pack()
runBtn.place(x = 90, y = 245)

# show graph button
graphBtn = tk.Button(window, text='Show graph', command=graph.showSpallingGraph, 
                     height=1, width=10, bg="#e3e3e3")
graphBtn.pack()
graphBtn.place(x = 190, y = 245)

# reset spalling count
resetCount = tk.Button(window, text='Reset spalling count', command=resetSpallingCount, 
                        height=1, width=18, bg="#e3e3e3")
resetCount.pack()
resetCount.place(x = 112, y = 295)

# spectro button
spectroBtn = tk.Button(window, text='Spectro', command=lambda:[spectro.spectroUI()], 
                        height=3, width=18, bg="#e3e3e3")
spectroBtn.pack()  
spectroBtn.place(x = 112, y = 345)



window.mainloop()