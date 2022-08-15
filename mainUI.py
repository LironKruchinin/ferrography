import tkinter as tk
from tkinter.filedialog import askopenfilenames
import spalingIdentify as spalling
import graphData as graph

window = tk.Tk()
window.geometry('350x250')


isRunOnPhoto = tk.BooleanVar()

def runOnPhoto():
   spalling.stopOnPhoto = isRunOnPhoto.get()
   if len(spalling.path) > 0:
      if isRunOnPhoto.get():
         spalling.photo()

      else:
         spalling.photo()

   # print(len(spalling.path))
   # print(spalling.counterBetween75)

   getTextInput()


def selFilePath():
   spalling.path = askopenfilenames(parent=window, title='Select files')

def getTextInput():
   inputTestSN = textFieldTestSN.get('1.0', 'end-1c')
   # print(inputTestSN)

def resetSpallingCount():
   spalling.basicCounter = 0
   spalling.counterBetween75 = 0
   spalling.counterBetween105 = 0
   spalling.counterBetween120 = 0


textFieldTestSN = tk.Text(window, width=15, height=1)

labelFieldTestSN = tk.Label(window, text='Test SN:')

filePathBtn = tk.Button(window, text='Import file', command=selFilePath)

chk1 = tk.Checkbutton(window, text='Pause on each photo?', variable=isRunOnPhoto, onvalue=True, offvalue=False)

submitBtn = tk.Button(window, text="Run", command=runOnPhoto)

graphBtn = tk.Button(window, text='Show graph', command=graph.showSpallingGraph)
resetCount = tk.Button(window, text='Reset spalling count', command=resetSpallingCount)
spectroBtn = tk.Button(window, text='Spectro')


labelFieldTestSN.pack()
textFieldTestSN.pack()
filePathBtn.pack()
chk1.pack()
submitBtn.pack()
graphBtn.pack()
resetCount.pack()
spectroBtn.pack()


window.mainloop()