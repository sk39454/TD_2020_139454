import math
import numpy as np
import matplotlib.pyplot as plt
import array
import math
import numpy as np
import matplotlib.pyplot as plt
import array

def CLK():
    top = [] ; bot = [] ; final = [] ; xcords = []
    for x in np.linspace(1/10,2/10):
        top.append(1)
        bot.append(0)
    zero=top
    for x in range(len(top)):
        zero.append(bot[x])
    x=0
    for j in range(len(mt)):
        xtemp=x
        x=x+0.1
        x=round(x,1)
        xc=np.linspace(xtemp,x,len(zero))
        for i in range(len(zero)):
            final.append(zero[i])
            xcords.append(xc[i])
    return xcords,final

def TTL():
    ycords=[] ; xcords=[] ; x=0
    for i in range (len(mt)):
        xtemp=x
        x=x+0.1
        x=round(x,1)
        if(mt[i]==0):
            for j in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for j in np.linspace(1/10,2/10):
                ycords.append(1)
    xcords=np.linspace(0,len(mt)/10,len(ycords))
    return xcords,ycords

def Manchester(freq):
    top = [] ; bot = [] ; final = [] ; xcords = []
    for x in np.linspace(1/10,2/10):
        top.append(1)
        bot.append(0)
    zero=top
    jeden=bot
    for x in range(len(top)):
        zero.append(bot[x])
        jeden.append(top[x])
    x=0
    for j in range(len(mt)):
        xtemp=x
        x=x+0.1
        x=round(x,1)
        xc=np.linspace(xtemp,x,len(zero))
        if(mt[j]==0):
            for i in range(len(zero)):
                final.append(zero[i])
                xcords.append(xc[i])
        else:
            for i in range(len(jeden)):
                final.append(jeden[i])
                xcords.append(xc[i])

    return xcords,final

def NRZI():
    top = [] ; bot = [] ; final = [] ; xcords = [] ; switch=mt[1]
    for x in np.linspace(1/10,2/10):
        top.append(1)
        bot.append(0)
    for i in range (len(mt)):
        if(mt[i]==1):
            switch=1-switch
        if(switch==0):
            for x in range(len(bot)):
                final.append(bot[x])
        else:
            for x in range(len(top)):
                final.append(top[x])

    xcords=np.linspace(0,len(mt)/10,len(final))
    return xcords,final

def BAMI():
    top = [] ; bot = [] ; final = [] ; zero = [] ; switch=1
    for x in np.linspace(1/10,2/10):
        top.append(1)
        zero.append(0)
        bot.append(-1)
    for i in range (len(mt)):
        if(mt[i]==0):
            for x in range(len(zero)):
                final.append(zero[x])
        else:
            if(switch==1):
                switch=-1
                for x in range(len(bot)):
                    final.append(bot[x])
            else:
                switch=1
                for x in range(len(top)):
                    final.append(top[x])

    xcords=np.linspace(0,len(mt)/10,len(final))
    return xcords,final

plt.figure()
mt=[0,1,0,1,1,0,0,1,0,0,1,0]
tb=0.1 ;N=10;f=N*(tb**(-1));f0=(N+1)/tb;f1=(N+2)/tb;A=1;A1=0;A2=1
LIMIT=10 ; freq=11
[x1,y1]=CLK()
plt.subplot(511)
plt.title("CLK")
plt.plot(x1,y1)
[x2,y2]=TTL()
plt.subplot(512)
plt.title("TTL")
plt.plot(x2,y2)
[x3,y3]=Manchester(freq)
plt.subplot(513)
plt.title("Manchester")
plt.plot(x3,y3)
[x4,y4]=NRZI()
plt.subplot(514)
plt.title("NRZI")
plt.plot(x4,y4)
[x5,y5]=BAMI()
plt.subplot(515)
plt.title("BAMI")
plt.plot(x5,y5)
plt.show()
