import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
import pylab
from scipy.interpolate import interp1d

from Utilities import Binary, Hamming_SECDED, Hamming_Dekoder_SECDED
from Utilities import MT,ASK,demodulator1,spectrum

def Slim(word,p3):
    final = []
    step = len(p3)/(len(word))
    poz = 0
    for x in range (len(word)):
        final.append(p3[int(poz)])
        poz = poz + step
    return final

word = [0,1,0,0,0,0,0,1]
tb=0.1 ;N=10;f=N*(tb**(-1));f0=(N+1)/tb;f1=(N+2)/tb;A=1;A1=0;A2=1
LIMIT=8
word = Binary('a')
word = [0,1,0,0,0,0,0,1]

[x,wynik]=Hamming_SECDED(word)
[x1,y1]=MT(x,LIMIT)
[x2,y2]=ASK(x,LIMIT)
[x2s,y2s]=spectrum(y1)
noise = np.random.normal(0,1,len(y2s))
spec_with_noise=y2s+noise
[x2n,y2n]=spectrum(spec_with_noise)
[p1,p2,p3]=demodulator1(y2,0.2)

plt.figure()
plt.subplot(511)
plt.title('Sygnal wejsciowy')
plt.plot(x1,y1)

plt.subplot(512)
plt.title('ZA(t)')
plt.plot(x2,y2)

plt.subplot(513)
plt.plot(x2s,y2s)
plt.title('widmo sygnalu')
plt.subplot(514)
plt.plot(x2n,y2n)
plt.title('widmo sygnalu z szumem')
plt.subplot(515)
plt.title('Demodulacja sygnalu')
xlen=np.linspace(0,1,len(p3))
plt.plot(xlen,p3)
decode=Slim(word,p3)
decode=np.array(decode)
Hamming_Dekoder_SECDED(word,decode)
plt.show()
