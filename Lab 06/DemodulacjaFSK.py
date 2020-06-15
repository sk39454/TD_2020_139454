
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
    demodulatoFSK0=[] ; demodulatoFSK1=[]
    for i,j in zip(FSK,t):
        demodulatoFSK0.append(i* A1 * np.sin(2 * np.pi *f1*j + fi))

    for i,j in zip(FSK,t):
        demodulatoFSK1.append(i* A1 * np.sin(2 * np.pi *f2*j + fi))

    integralFSK0 = []
    for i in range(z1):
        x0 = 0
        for j in range(50):
            x0 = x0 + demodulatoFSK0[(i * 50) + j]
        integralFSK0.append(x0)

    integralFSK1 = []
    for i in range(z1):
        x1 = 0
        for j in range(50):
            x1 = x1 + demodulatoFSK1[(i * 50) + j]
        integralFSK1.append(x1)

    integral_FULL_FSK = []
    for i in range(z1):
        integral_FULL_FSK.append(integralFSK0[i] - integralFSK1[i])

    interpolatingFSK=interp1d(x, integral_FULL_FSK, kind='previous')
    FSK_pt=interpolatingFSK(t)

    return demodulatoFSK0,demodulatoFSK1,FSK_pt

def wartoscProgowa (pt_key,h):
    tab_wart_prog = []
    for p in pt_key:
        if p < h:
            tab_wart_prog.append(1)
        else:
            tab_wart_prog.append(0)
    return tab_wart_prog

mt=Binary('Kamil')
plt.figure()
fi0=0 ; fi1=np.pi;fi = np.pi;A1=1;A2=0.3;Tb=1 ;N=1/Tb;f = N * (Tb ** -1)
f1 = (N + 1)/Tb;f2 = (N + 2)/Tb;x=50;z1=len(mt);prb=x*(z1/Tb);prb1=int(prb)
t = np.linspace(0,z1,prb1);x = np.linspace(0,z1,z1);h=10

interpolacja = interp1d(x, mt, kind='previous')
TBs = interpolacja(t)
plt.subplot(611)
plt.plot(t,TBs)

FSK=FSK()
plt.subplot(612)
plt.plot(t,FSK)

[demodulatoFSK0,demodulatoFSK1,FSK_pt]=demo()
FSKwp=wartoscProgowa(FSK_pt,h)

plt.subplot(613)
plt.plot(t,demodulatoFSK0)

plt.subplot(614)
plt.plot(t,demodulatoFSK1)

plt.subplot(615)
plt.plot(t,FSK_pt)

#plt.subplot(616)
#plt.plot(FSKwp)

plt.show()
