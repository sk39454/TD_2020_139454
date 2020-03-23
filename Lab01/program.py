import math
import numpy as np
import matplotlib.pyplot as plt
import array

a=4;b=5;c=4;

delta=(b*b)+((-4)*a*c)
if delta == 0:
  x1 = (-b) / (2 * a)
  print('x1 = ',x1,'\n\n')

if delta > 0:
  x1 = ((-b)-(math.sqrt(delta)))/(2*a)
  x2 = ((-b)+(math.sqrt(delta)))/(2*a)
  print('x1 = ',x1,'\n','x2 = ',x2,'\n\n')

if delta < 0:
  print('Brak miejsc zerowych')

xcords1 = [] ; acords = [] ; xcords = [] ; ycords = [] ; zcords = [] ; ucords = [] ; vcords1 = [] ;vcords2 = [] ;vcords3 = [] ; pcords = []

x=-10
while x < 10:
  xcords1.append(x)
  fx = (a * (x * x)) + (b * x) +  c
  acords.append(fx)
  x=x+0.01
  x=round(x,2)

x=0
while x < 1:
  xcords.append(x)
  fx = (a * (x * x)) + (b * x) +  c
  funkcja = (2 * (fx * fx)) + (12*math.cos(x))
  ycords.append(funkcja)

  funkcja2 = (math.sin(2*math.pi*7*x)*fx)-0.2*math.log((abs(funkcja)+math.pi),10)
  zcords.append(funkcja2)

  funkcja3 = math.sqrt(abs(funkcja*funkcja*funkcja2))-1.8*math.sin(0.4*x*funkcja2*funkcja)
  ucords.append(funkcja3)

  if 0.22 > x >= 0:
    funkcja41 = (1-(7*x))*math.sin((2*math.pi*x*10)/(x+0.04))
    vcords1.append(funkcja41)
  if 0.22 <= x < 0.7:
    funkcja42 = 0.63 * x * math.sin(125*x)
    vcords2.append(funkcja42)
  if 1 >= x >= 0.7:
    funkcja43 = math.pow(x,-0.662)+0.77*math.sin(8*x)
    vcords3.append(funkcja43)

  n=1
  N=45
  wynik=0
  while n < N :
      funkcja5=(math.cos(12*x*(n*n))+math.cos(16*x*n))/(n*n)
      wynik=wynik+funkcja5
      n+=1
  pcords.append(wynik)

  x=x+(1/22050)
  x=round(x,6)

fig, axs=plt.subplots(6)
fig.suptitle('Vertically stacked subplots')

axs[0].plot(xcords1,acords)
axs[1].plot(xcords,ycords)
axs[2].plot(xcords,zcords)
axs[3].plot(xcords,ucords)
#Wykres 4
len1=len(vcords1)
len2=len(vcords1)+len(vcords2)
len3=len2+len(vcords3)
axs[4].plot(xcords[:len1],vcords1)
axs[4].plot(xcords[len1:len2],vcords2)
axs[4].plot(xcords[len2:len3],vcords3)

axs[5].plot(xcords,pcords)

plt.show()
