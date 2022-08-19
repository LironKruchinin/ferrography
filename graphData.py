import spalingIdentify as spalling
import matplotlib.pyplot as plt
import spalingIdentify as spalling


def showSpallingGraph():
      def addlabels(x,y):
            for i in range(len(x)):
                  plt.text(i, y[i], y[i], ha = 'center')
                  
#    data = {'Under 75 micron': spalling.countUnder75, '75 micron':spalling.counterBetween75, '105 micron':spalling.counterBetween105, '120 micron':spalling.counterBetween120 }
      x = ['Small spalling %', 'Under 75 micron', '75 micron', '105 micron', '120 micron']
      y = [round(spalling.calcPercentageOfPic, 3), spalling.countUnder75, spalling.counterBetween75, spalling.counterBetween105, spalling.counterBetween120]

      plt.figure(figsize = (10, 5))
      plt.bar(x, y)
      addlabels(x, y)
      plt.title("Spalling count")
      plt.xlabel("Spalling size")
      plt.ylabel("Spalling amount")
      plt.show()


      


# print(spalling.counterBetween75)
# print(spalling.counterBetween75)
