import tkinter as tk

def spectroUI():
   OPTIONS = [
      'Same',
      'Different'
   ]

   global spectroWindow
   spectroWindow = tk.Toplevel()
   spectroWindow.title("Spectro")
   spectroWindow.geometry('350x300')
   
   testSNLabel = tk.Label(spectroWindow, text='Test SN:')
   testSNLabel.pack()
   testSNLabel.place(x = 85, y = 18)

   global testSNText
   testSNText = tk.Text(spectroWindow, width=15, height=1, font=("Helvetica", 11))
   testSNText.pack()
   testSNText.place(x = 135, y = 18)

   global hLimText
   hLimLabel = tk.Label(spectroWindow, text='H Lim:')
   hLimLabel.pack()
   hLimLabel.place(x = 92, y = 55)

   hLimText = tk.Text(spectroWindow, width=15, height=1)
   hLimText.pack()
   hLimText.place(x = 135, y = 55)

   dropDownChoice = tk.StringVar()
   dropDownChoice.set(OPTIONS[0])
   
   dropDownMenu = tk.OptionMenu(spectroWindow, dropDownChoice, *OPTIONS)
   dropDownMenu.config(width=15, height=1, bg="#e3e3e3")
   dropDownMenu.pack()
   dropDownMenu.place(x = 110, y = 95)

   runBtn = tk.Button(spectroWindow, text="Run", 
                        height=2, width=15, bg="#e3e3e3")
   runBtn.pack()
   runBtn.place(x = 120, y = 155)



