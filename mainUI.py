import tkinter as tk
from tkinter.filedialog import askopenfilenames
import spalingIdentify as spalling
import graphData as graph
import spectroUI as spectro
import glob
import numpy as np



global spectroWindow
spectroWindow = 0
global path
path = ''

window = tk.Tk()
window.geometry('350x300')
window.title("Ferrography")

isRunOnPhoto = tk.BooleanVar()

def teset():
   if spectro.spectroWindow.state():
      ferroSN = textFieldTestSN.get('1.0', 'end-1c')
      spectroSN = spectro.testSNText.get('1.0', 'end-1c')
      
   if spectro.spectroWindow.state() and ferroSN != spectroSN:
      tk.messagebox.showerror('Serial number Error', f'The serial numbers dont match \n Ferro SN: {ferroSN} \n Spectro SN: {spectroSN}')
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
   try: 
      if spectro.spectroWindow.state():
         ferroSN = textFieldTestSN.get('1.0', 'end-1c')
         spectroSN = spectro.testSNText.get('1.0', 'end-1c')

         if ferroSN != spectroSN:
            tk.messagebox.showerror('Serial number Error', f'The serial numbers dont match \n Ferro SN: {ferroSN} \n Spectro SN: {spectroSN}')
         
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



############################################################################################################
def selFilePath():
   global path
   spalling.path = askopenfilenames(parent=window, title='Select files')
   # arr = np.asarray(spalling.path)
   # spalling.path = arr[0].split('/')
   # spalling.path.pop()
   # # spalling.path.join()
   # for i in spalling.path:
   #    path += str(i)+"/"

   print(path)



def resetSpallingCount():
   spalling.countUnder75 = 0
   spalling.basicCounter = 0
   spalling.counterBetween75 = 0
   spalling.counterBetween105 = 0
   spalling.counterBetween120 = 0




   

labelFieldTestSN = tk.Label(window, text='Test SN:')
labelFieldTestSN.pack()
labelFieldTestSN.place(x = 55, y = 18)

textFieldTestSN = tk.Text(window, width=20, height=1, font=("Helvetica", 11))
textFieldTestSN.pack()
textFieldTestSN.place(x = 105, y = 20)

filePathBtn = tk.Button(window, text='Import file', command=selFilePath, 
                        height=1, width=15, bg="#e3e3e3")
filePathBtn.pack()
filePathBtn.place(x = 125, y = 55)

chk1 = tk.Checkbutton(window, text='Pause on each photo?', 
                     variable=isRunOnPhoto, onvalue=True, offvalue=False)
chk1.pack()
chk1.place(x = 110, y = 95)

runBtn = tk.Button(window, text="Run", command=lambda:[runOnPhoto()], 
                     height=1, width=10, bg="#e3e3e3", state=tk.NORMAL)
runBtn.pack()
runBtn.place(x = 90, y = 135)

graphBtn = tk.Button(window, text='Show graph', command=graph.showSpallingGraph, 
                     height=1, width=10, bg="#e3e3e3")
graphBtn.pack()
graphBtn.place(x = 190, y = 135)

resetCount = tk.Button(window, text='Reset spalling count', command=resetSpallingCount, 
                        height=1, width=18, bg="#e3e3e3")
resetCount.pack()
resetCount.place(x = 112, y = 175)

spectroBtn = tk.Button(window, text='Spectro', command=lambda:[spectro.spectroUI()], 
                        height=3, width=18, bg="#e3e3e3")
spectroBtn.pack()  
spectroBtn.place(x = 112, y = 225)



window.mainloop()