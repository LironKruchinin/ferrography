import tkinter as tk
import getFilePath as tempData

global getAnswer
getAnswer = ''

def spectroUI():
   OPTIONS = [
      'Same',
      'Different'
   ]

   HOUR = [
      'Repair',
      5,
      10,
      15,
      27.5
   ]

   # if spectro 27.5 ferro 15, check if same, 
   # if different go to lowest hour, else go to user written hour
   def showAnswer():
      tempData.spectroSN = testSNText.get('1.0', 'end-1c')
      spectroSN = testSNText.get('1.0', 'end-1c')
      if tempData.ferroSN != testSNText.get('1.0', 'end-1c'):
         tk.messagebox.showerror('Serial number Error', f'The serial numbers dont match \n Ferro SN: {tempData.ferroSN} \n Spectro SN: {spectroSN}')
      global getAnswer
      userChoice = hourChoice.get()
      rate = dropDownChoice.get()
      computerAnswer = tempData.hourAnswer
      if userChoice == 'Repair':
         userChoice = 1
      
# if different, spectro 27.5 and fero 15 set 15
# if same, spectro 27.5 and fero 15 set 27.5

      if rate == 'Different':
         
         if computerAnswer == 15 and userChoice == 27.5:
            getAnswer = 15
            tk.messagebox.showinfo('Final answer', '15 Flight hours')

         if float(userChoice) > float(computerAnswer):
            getAnswer = float(computerAnswer)
            if getAnswer == 1.0:
               tk.messagebox.showinfo('Final answer', 'Send the enigine to repairs')
            
            else:
               tk.messagebox.showinfo('Final answer', f'{getAnswer} Flight hours')


         else:
            getAnswer = float(userChoice)
            if getAnswer == 1.0:
               tk.messagebox.showinfo('Final answer', 'Send the enigine to repairs')
           
            else:
               tk.messagebox.showinfo('Final answer', f'{getAnswer} Flight hours')

      else:

         if computerAnswer == 15 and userChoice == 27.5:
            getAnswer = 27.5
            tk.messagebox.showinfo('Final answer', '27.5 Flight hours')

         if float(userChoice) < float(computerAnswer):
            getAnswer = float(userChoice)
            if getAnswer == 1.0:
               tk.messagebox.showinfo('Final answer', 'Send the enigine to repairs')
            else:
               tk.messagebox.showinfo('Final answer', f'{getAnswer} Flight hours')

         else:
            getAnswer = float(computerAnswer)
            if getAnswer == 1.0:
               tk.messagebox.showinfo('Final answer', 'Send the enigine to repairs')
            else:
               tk.messagebox.showinfo('Final answer', f'{getAnswer} Flight hours')

      # print(userChoice)
      # print(rate)
      # print(computerAnswer)
      # get the smallest amount of h
      # if rate == 'Different':


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

   hLimLabel = tk.Label(spectroWindow, text='H Lim:')
   hLimLabel.pack()
   hLimLabel.place(x = 92, y = 55)

   global hLimText
   hourChoice = tk.StringVar()
   hourChoice.set(HOUR[0])
   
   hourDownMenu = tk.OptionMenu(spectroWindow, hourChoice, *HOUR)
   hourDownMenu.config(width=12, height=1, bg="#e3e3e3")
   hourDownMenu.pack()
   hourDownMenu.place(x = 135, y = 51)


   dropDownChoice = tk.StringVar()
   dropDownChoice.set(OPTIONS[0])
   
   metalRateLabel = tk.Label(spectroWindow, text='Rate:')
   metalRateLabel.pack()
   metalRateLabel.place(x = 101, y = 98)

   dropDownMenu = tk.OptionMenu(spectroWindow, dropDownChoice, *OPTIONS)
   dropDownMenu.config(width=12, height=1, bg="#e3e3e3")
   dropDownMenu.pack()
   dropDownMenu.place(x = 135, y = 95)

   runBtn = tk.Button(spectroWindow, text="Run", 
                        height=2, width=15, bg="#e3e3e3", command=showAnswer)
   runBtn.pack()
   runBtn.place(x = 120, y = 155)

   

# check if rate is different,
# rate = different
# check if tempData is lower than hourChoice
# tempData < hourChoice
# return temp data

# tempData > hourChoice
# return hourChoice
