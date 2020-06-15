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

def bandwidth(A):
    X=np.amax(A)
    Y=np.amin(A)
    return (abs(abs(X)-abs(Y)))

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
    plt.subplot(421)
    plt.title('Sygnal wejjsciowy')
    plt.plot(xcords,ycords)


def ZAT(LIMIT):
    ycords=[]
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )))
    xcords=np.linspace(0,1,len(ycords))
    plt.subplot(423)
    plt.title('ZA(t)')
    plt.plot(xcords,ycords)
    spectrum = np.fft.rfft(ycords)
    xcords = np.linspace(0,1,len(spectrum))
    plt.subplot(424) , plt.xlim(0,0.17), plt.title('Widmo sygnalu')
    plt.plot(xcords,spectrum)
    ycords=np.array(ycords)
    bw=bandwidth(ycords)
    #bw 1.1102230246251565e-16
def ZFT(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )))
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(80*np.pi*(x  - 1/10 )))
    xcords=np.linspace(0,1,len(ycords))
    plt.subplot(425)
    plt.title('ZF(t)')
    plt.plot(xcords,ycords)
    spectrum = np.fft.rfft(ycords)
    xcords = np.linspace(0,1,len(spectrum))
    plt.subplot(426) , plt.xlim(0,0.24) , plt.title('Widmo sygnalu')
    plt.plot(xcords,spectrum)
    ycords=np.array(ycords)
    bw=bandwidth(ycords)
    #bw 1.1102230246251565e-16

def ZPT(LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(20*np.pi*(x  + 0 )))
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(20*np.pi*(x  - np.pi )))
    xcords=np.linspace(0,1,len(ycords))
    plt.subplot(427)
    plt.title('ZP(t)')
    plt.plot(xcords,ycords)
    spectrum = np.fft.rfft(ycords)
    xcords = np.linspace(0,1,len(spectrum))
    plt.subplot(428) , plt.xlim(0,0.1), plt.title('Widmo sygnalu')
    plt.plot(xcords,spectrum)
    ycords=np.array(ycords)
    bw=bandwidth(ycords)
    #bw 0.00037399113886860125

plt.figure()
mt=Binary('Lama MA KOTA',0)
#LIMIT=len(mt)
LIMIT=10
print(mt)
tb=0.1
N=2
f=N*(tb**(-1))
f0=(N+1)/tb
f1=(N+2)/tb
A=1
A1=0
A2=1
MT(LIMIT)
ZAT(LIMIT)
ZFT(LIMIT)
ZPT(LIMIT)
plt.subplot(422).remove()
plt.show()
