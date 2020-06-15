
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def Binary(string):
    bin = ''.join(format(i, 'b') for i in bytearray(string, encoding ='utf-8'))
    bin = list(map(int, bin))
    #print('variant=littleEndian\n','conversion of ', string,' to binary is equal to [ ', bin,' ]')
    return bin

def FSK():
    FSK=[]
    for i,j in zip(TBs,t):
        if i == 1:
            FSK.append(A1 * np.sin(2 * np.pi *f*j + fi))
        if i==0:
             FSK.append(A1 * np.sin(2 * np.pi *f1*j + fi))
    return FSK

def demo():
    DemoX1=[] ; DemoX2=[]
    for i,j in zip(FSK,t):
        DemoX1.append(i* A1 * np.sin(2 * np.pi *f1*j + fi))

    for i,j in zip(FSK,t):
        DemoX2.append(i* A1 * np.sin(2 * np.pi *f2*j + fi))

    pt1 = []
    for i in range(z1):
        x0 = 0
        for j in range(50):
            x0 = x0 + DemoX1[(i * 50) + j]
        pt1.append(x0)

    pt2 = []
    for i in range(z1):
        x1 = 0
        for j in range(50):
            x1 = x1 + DemoX2[(i * 50) + j]
        pt2.append(x1)

    pt = []
    for i in range(z1):
        pt.append(pt1[i] - pt2[i])

    interpolatingFSK=interp1d(x, pt, kind='previous')
    FSK_pt=interpolatingFSK(t)

    return DemoX1,DemoX2,FSK_pt

def wartoscProgowa (pt,h):
    wp = []
    for p in pt:
        if p < h:
            wp.append(1)
        else:
            wp.append(0)
    return wp

mt=Binary('Kamil')
plt.figure()
fi0=0 ; fi1=np.pi;fi = np.pi;A1=1;A2=0.3;Tb=1 ;N=1/Tb;f = N * (Tb ** -1)
f1 = (N + 1)/Tb;f2 = (N + 2)/Tb;x=50;z1=len(mt);prb=x*(z1/Tb);prb1=int(prb)
t = np.linspace(0,z1,prb1);x = np.linspace(0,z1,z1);h=10

interpolacja = interp1d(x, mt, kind='previous')
TBs = interpolacja(t)
plt.subplot(511)
plt.title('sygnal wejsciowy')
plt.plot(t,TBs)

FSK=FSK()
plt.subplot(512)
plt.title('FSK')
plt.plot(t,FSK)

[DemoX1,DemoX2,FSK_pt]=demo()
FSKwp=wartoscProgowa(FSK_pt,h)

plt.subplot(513)
plt.title('Demodulacja FSK x1(t)')
plt.plot(t,DemoX1)

plt.subplot(514)
plt.title('Demodulacja FSK x2(t)')
plt.plot(t,DemoX2)

plt.subplot(515)
plt.title('Demodulacja FSK p(t)')
plt.plot(FSKwp)

plt.show()
