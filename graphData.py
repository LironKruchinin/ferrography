import spalingIdentify as spalling
import matplotlib.pyplot as plt

def showSpallingGraph():
      def addlabels(x,y):
            for i in range(len(x)):
                  plt.text(i, y[i], y[i], ha = 'center')
                  
#    data = {'Under 75 micron': spalling.countUnder75, '75 micron':spalling.counterBetween75, '105 micron':spalling.counterBetween105, '120 micron':spalling.counterBetween120 }
      x = ['Under 75 micron', '75 micron', '105 micron', '120 micron']
      y = [spalling.countUnder75, spalling.counterBetween75, spalling.counterBetween105, spalling.counterBetween120]

      plt.figure(figsize = (10, 5))
      plt.bar(x, y)
      addlabels(x, y)
      plt.title("College Admission")
      plt.xlabel("Courses")
      plt.ylabel("Number of Admissions")
      plt.show()
      


# print(spalling.counterBetween75)
# print(spalling.counterBetween75)
