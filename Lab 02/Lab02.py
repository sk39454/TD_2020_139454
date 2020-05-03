import math
import numpy as np
import matplotlib.pyplot as plt
import array

a=4;b=5;c=4;
xcords = [] ; ycords = [] ; bob = [] ; aoa = []
xcords1 = []
x=0
while x <= a:
  xcords.append(x)
  funkcja = 1 * math.sin(2 * math.pi * b * x + c*math.pi)
  aa=math.floor((funkcja*(math.pow(2,15)-1)+math.pow(2,15)-1))

  ycords.append(funkcja)
  aoa.append(aa)

  x=x+0.006
  x=round(x,4)

x=0
while x <= a:
  xcords1.append(x)
  funkcja = 1 * math.sin(2 * math.pi * b * x + c*math.pi)
  bb=math.floor((funkcja*(math.pow(2,7)-1)+math.pow(2,7)-1))
  bob.append(bb)

  x=x+0.012
  x=round(x,4)

fig, axs=plt.subplots(3)
fig.suptitle('Vertically stacked subplots')

axs[0].plot(xcords,ycords,'bo')
axs[1].plot(xcords,aoa,'bo')
axs[2].plot(xcords1,bob,'bo')
plt.show()
