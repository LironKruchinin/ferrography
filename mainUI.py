import tkinter as tk
from tkinter.filedialog import askopenfilenames
import spalingIdentify as spalling


window = tk.Tk()
window.geometry('600x450')


isRunOnPhoto = tk.BooleanVar()

def runOnPhoto():
   spalling.stopOnPhoto = isRunOnPhoto.get()
   if len(spalling.path) > 0:
      if isRunOnPhoto.get():
         spalling.photo()

      else:
         spalling.photo()

   # print(len(spalling.path))
   getTextInput()


def selFilePath():
   spalling.path = askopenfilenames(parent=window, title='Select files')

def getTextInput():
   inputTestSN = textFieldTestSN.get('1.0', 'end-1c')
   print(inputTestSN)


textFieldTestSN = tk.Text(window, width=15, height=1)

labelFieldTestSN = tk.Label(window, text='Test SN:')

filePathBtn = tk.Button(window, text='File path...', command=selFilePath)

chk1 = tk.Checkbutton(window, text='Do you want to stop on photo?', variable=isRunOnPhoto, onvalue=True, offvalue=False)

submitBtn = tk.Button(window, text="Run", command=runOnPhoto)

graphBtn = tk.Button(window, text='Show graph')

spectroBtn = tk.Button(window, text='Spectro')


labelFieldTestSN.pack()
textFieldTestSN.pack()
filePathBtn.pack()
chk1.pack()
submitBtn.pack()
graphBtn.pack()
spectroBtn.pack()


window.mainloop()