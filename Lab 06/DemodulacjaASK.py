import math
import numpy as np
import matplotlib.pyplot as plt
import array
import math
import numpy as np
import matplotlib.pyplot as plt
import array

def Binary(string,switch):
    if (switch == 0):
        bin = ''.join(format(i, 'b') for i in bytearray(string, encoding ='utf-8'))
        bin = list(map(int, bin))
        #print('variant=littleEndian\n','conversion of ', string,' to binary is equal to [ ', bin,' ]')
        return bin
    else:
        rev=string[::-1]
        bin2 = ''.join(format(i, 'b') for i in bytearray(rev, encoding ='utf-8'))
        bin2 = list(map(int, bin2))
        #print('variant=BigEndian\n','conversion of ', string,' to binary is equal to [ ',''.join(bin2),' ]')
        return bin2

def MT(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(1)
    xcords=np.linspace(0,1,len(ycords))
    plt.subplot(231)
    plt.plot(xcords,ycords)

def ASK(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )*1))
    xcords=np.linspace(0,1,len(ycords))
    plt.subplot(232)
    plt.plot(xcords,ycords)
    return ycords

def demodulator1(Modulacja,h):
    Demo=[] ; Final=[] ;  Demov2 = []
    sum=0 ; sumabs = 0

    for i in range (len(Modulacja)):
        if (Modulacja[i] == 0.0000000):
            sum = 0
        sum=sum+Modulacja[i]
        Demo.append(sum)

    xcords = np.linspace(0,1,len(Demo))
    plt.subplot(235)
    plt.plot(xcords,Demo)

    for i in range (len(Modulacja)):
        if (Modulacja[i] == 0.0000000):
            sumabs = 0
        if (Modulacja[i]>h):
            sumabs=sumabs+(Modulacja[i])
        Demov2.append(sumabs)

    xcords = np.linspace(0,1,len(Demov2))
    plt.subplot(236)
    plt.plot(xcords,Demov2)

    for i in range (len(Demov2)):
        roundmt=round(Demov2[i],0)
        if(roundmt==0):
            for x in np.linspace(1/10,2/10):
                Final.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                Final.append(1)

    xcords=np.linspace(0,1,len(Final))
    plt.subplot(234)
    plt.plot(xcords,Final)

plt.figure()
mt=Binary('Kamil',0)
tb=0.1 ;N=10;f=N*(tb**(-1));f0=(N+1)/tb;f1=(N+2)/tb;A=1;A1=0;A2=1
LIMIT=10
MT(LIMIT)
ycords=ASK(LIMIT)
demodulator1(ycords,0.2)
plt.show()
