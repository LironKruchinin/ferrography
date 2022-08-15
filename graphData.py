import spalingIdentify as spalling
import matplotlib.pyplot as plt

def showSpallingGraph():
   data = {'Under 75 micron': spalling.countUnder75, '75 micron':spalling.counterBetween75, '105 micron':spalling.counterBetween105, '120 micron':spalling.counterBetween120 }

   courses = list(data.keys())
   values = list(data.values())

   fig, ax = plt.subplots(figsize =(10, 6))
   ax.yaxis.set_tick_params(pad = 2)
   # creating the bar plot
   plt.bar(courses, values, color ='blue',
         width = 0.4)
   
   

   plt.xlabel("size of spalling")
   plt.ylabel("No. of spalling ")
   plt.title("Count of spalling fragments in the loaded photo set")
   plt.show()

# print(spalling.counterBetween75)
# print(spalling.counterBetween75)