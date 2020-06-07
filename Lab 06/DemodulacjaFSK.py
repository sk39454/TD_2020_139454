import math
import numpy as np
import matplotlib.pyplot as plt
import array
import math
import numpy as np
import matplotlib.pyplot as plt
import array

def Uno(string,switch):
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
    plt.plot(xcords,ycords)

def ASK(mt,LIMIT,Amp):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )*Amp))
    xcords=np.linspace(0,1,len(ycords))
    plt.plot(xcords,ycords)
    return ycords

def Duo(mt):
    mt2=[]
    for i in range(len(mt)):
        if (mt[i]==0):
            mt2.append(1)
        else:
            mt2.append(0)
    return mt2

def Join(A,B):
    for i in range (len(A)):
        if(A[i]==0):
            A[i]=B[i]
    return A

def demodulator(A,B,h):
    sum=0 ; sum2=0 ; Demo1=[]; Demo2=[]; fcplus=[]; fcminus=[]; Final=[]
    sumabs= 0; Demov2=[]
    for i in range(len(A)):
        sum=sum+A[i]
        Demo1.append(sum)
        sum2=sum2+B[i]
        Demo2.append(sum2)

    for i in range(len(A)):
        fcplus.append(Demo2[i]-Demo1[i])
        fcminus.append(Demo1[i]-Demo2[i])

    plt.subplot(242)
    xcords=np.linspace(0,1,len(fcplus))
    plt.plot(xcords,fcplus)

    plt.subplot(243)
    xcords=np.linspace(0,1,len(fcminus))
    plt.plot(xcords,fcminus)

    plt.subplot(248)
    C=Join(A,B)
    plt.plot(C)

    for j in range(len(mt)):
        if(mt[j]==0):
            for i in range (len(A)):
                if(A[i]<0):
                    sumabs=sumabs+A[i]
                    Demov2.append(sumabs)
        else:
            for i in range (len(A)):
                if(A[i]>0):
                    sumabs=sumabs+A[i]
                    Demov2.append(sumabs)
        sumabs=0

    for i in range (len(Demov2)):
        roundmt=round(Demov2[i],0)
        if(roundmt<=0):
            for x in np.linspace(1/10,2/10):
                Final.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                Final.append(1)

    xcords=np.linspace(0,1,len(Final))
    plt.subplot(245)
    plt.plot(xcords,Final)

plt.figure()
mt=Uno('Kamil',0)
mt=[0,1,1,0,1,0]
mt2=Duo(mt)
LIMIT=6 ; tb=0.1 ; N=10 ; f=N*(tb**(-1)) ; f0=(N+1)/tb ; f1=(N+2)/tb ; A=1 ; A1=0 ; A2=1

plt.subplot(241)
MT(LIMIT)

plt.subplot(246)
ycords1=ASK(mt,LIMIT,1)
A1=ycords1
plt.subplot(247)
ycords2=ASK(mt2,LIMIT,0.5)
A2=ycords2
demodulator(A1,A2,0.2)

plt.show()
