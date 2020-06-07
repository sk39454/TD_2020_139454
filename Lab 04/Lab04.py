import math
import numpy as np
import matplotlib.pyplot as plt
import array

def Zadanie(Ka,Kp):
    fm=5;fn=100;a=1
    xcords = [] ; ycords = [] ; ycords1 = [] ; ycords2 = []
    x=0
    while x <= a:
      xcords.append(x)
      MT = 1 * math.sin(2 * math.pi * fm * x)
      ycords.append(MT)
      ZA = (Ka*MT+1)*np.cos(2 * math.pi * fn * x)
      ycords1.append(ZA)
      ZT = np.cos(2 * math.pi * fn * x + Kp*MT)
      ycords2.append(ZT)
      x=x+0.001
      x=round(x,4)
    ZAW = np.fft.rfft(ycords1)
    ZTW = np.fft.rfft(ycords2)

    plt.figure()
    plt.subplot(511), plt.title('Pure tone'),plt.xlabel('Time'), plt.ylabel('Signal Strength'), plt.plot(xcords,ycords)
    plt.subplot(512), plt.title('Amplitude modulation'),plt.xlabel('Time'), plt.ylabel('Signal Strength'), plt.plot(xcords,ycords1)
    plt.subplot(513), plt.title('Amplitude modulation'),plt.xlabel('Time'), plt.ylabel('Signal Strength'), plt.plot(xcords,ycords2)
    plt.subplot(514)
    if 1>Ka>0:
        plt.xlim(90,110)
        plt.ylim(-50)
        plt.title('Amplitude of spectrum')
        plt.xlabel('Frequency')
        plt.ylabel('Decibels')
        plt.stem(ZAW,use_line_collection=True)
        plt.subplot(515)
        plt.xlim(90,100)
        plt.ylim(-250)
        plt.title('Amplitude of spectrum')
        plt.xlabel('Frequency')
        plt.ylabel('Decibels')
        plt.stem(ZTW,use_line_collection=True)
        plt.show()
    if  12>Ka>2:
        plt.xlim(90,110)
        plt.ylim(-70)
        plt.title('Amplitude of spectrum')
        plt.xlabel('Frequency')
        plt.ylabel('Decibels')
        plt.stem(ZAW,use_line_collection=True)
        plt.subplot(515)
        plt.xlim(89,96)
        plt.ylim(-50)
        plt.title('Amplitude of spectrum')
        plt.xlabel('Frequency')
        plt.ylabel('Decibels')
        plt.stem(ZTW,use_line_collection=True)
        plt.show()
    if  Ka>12:
        plt.xlim(90,115)
        plt.ylim(-300)
        plt.title('Amplitude of spectrum')
        plt.xlabel('Frequency')
        plt.ylabel('Decibels')
        plt.stem(ZAW,use_line_collection=True)
        plt.subplot(515)
        plt.xlim(0,200)
        plt.ylim(-150)
        plt.title('Amplitude of spectrum')
        plt.xlabel('Frequency')
        plt.ylabel('Decibels')
        plt.stem(ZTW,use_line_collection=True)
        plt.show()

    pasmo1=[] ; pasmo2=[]
    for i in range(len(ZTW)):
        if(ZTW[i]>=-3):
            pasmo1.append(ycords1[i])
    for i in range(len(ZAW)):
        if(ZAW[i]>=-3):
            pasmo2.append(ycords2[i])
    fmin1=np.min(pasmo1) ; fmin2=np.min(pasmo2)
    fmax1=np.max(pasmo1) ; fmax2=np.max(pasmo2)
    w1 = fmax1-fmin1 ; w2 = fmax2-fmin1
    #wyniki dla podpunktu pierwszego
    #w1 = 2.993 w 2.493
    #wyniki dla podpunktu drugiego
    #w1 = 23.864 w 12.864
    #wyniki dla podpunktu trzeciego
    #w1 = 69.581 w 35.581

Zadanie(0.5,1.5)
Zadanie(11,1.4)
Zadanie(34,43)
