import numpy as np

def tile(value, count):
    return [value for __ in range(int(count))]

def linspace(low, high, stepCount):
    step = (high - low) / (stepCount - 1)
    values = [low + step * i for i in range(stepCount)]
    return values

def Binary(string):
    bin = ''.join(format(i, 'b') for i in bytearray(string, encoding ='utf-8'))
    bin = list(map(int, bin))
    #print('variant=littleEndian\n','conversion of ', string,' to binary is equal to [ ', bin,' ]')
    return bin

def Hamming_SECDED(word):
    print('Slowo zapisane binarnie - ', word)
    word1 = np.array(word[0:4])
    word2 = np.array(word[4:8])

    G_SECDED = np.array([[1,1,1,0,0,0,0,1], [1,0,0,1,1,0,0,1], [0,1,0,1,0,1,0,1], [1,1,0,1,0,0,1,0]])

    h_word1_e = (np.dot(G_SECDED.T, word1)).transpose() % 2
    h_word2_e = (np.dot(G_SECDED.T, word2)).transpose() % 2
    Wynik = np.concatenate((h_word1_e,h_word2_e))
    print('Hamming74: ',Wynik)
    return h_word1_e,Wynik

def Hamming_Dekoder_SECDED(word,h_word1_e):
    hamm_SECDED = np.array([[1,0,1,0,1,0,1,0], [0,1,1,0,0,1,1,0], [0,0,0,1,1,1,1,0,], [1,1,1,1,1,1,1,1]])
    hamm_SECDED = np.dot(hamm_SECDED,h_word1_e.T) % 2
    n0 = hamm_SECDED[0] ; n2 = hamm_SECDED[2] ; n1 = hamm_SECDED[1]

    if n0 != 0 & n1 != 0 & n2 != 0:
        print('Korekty w indeksie nie są równe 0!')
    else:
        p1_e = (word[0] + word[1] + word[3] + word[4] + word[6]) % 2
        p2_e = (word[0] + word[2] + word[3] + word[5] + word[6]) % 2
        p3_e = (word[1] + word[2] + word[3] + word[7]) % 2
        p4_e = (word[4] + word[5] + word[6] + word[7]) % 2
        c = (p1_e + p2_e + word[0] + p3_e + word[1] + word[2] + word[3] + p4_e + word[4] + word[5] + word[6] + word[7]) % 2
        neg_c = np.logical_not(c).astype(int)

    print('wektor danych - ', p1_e, p2_e, p3_e, p4_e, neg_c)
    print('Hamming - ', p1_e, p2_e, word[0], p3_e, word[1], word[2], word[3], p4_e, word[4], word[5],word[6], word[7], neg_c)

def info_Signal(secondsPerBit, bits, s_p_Bit):
    time = linspace(0, secondsPerBit * len(bits), s_p_Bit * len(bits))

    s_samples = s_p_Bit * len(bits) * [None] #próbki sygnału
    for i, bit in enumerate(bits):
        s_samples[i * s_p_Bit:(i + 1) * s_p_Bit] = tile(bit, s_p_Bit)
    return time, s_samples

def CLK(samplesPerBit, clockCount):
    halfSamples = int(samplesPerBit / 2)

    clockSamples = samplesPerBit * clockCount * [None]
    for i in range(clockCount * 2):
        clockSamples[i * halfSamples:(i + 1) * halfSamples] = tile((i % 2) == 0, halfSamples)
    return clockSamples

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

def Manchester(clk, ttl):
    M_C = [0]
    currentValue = 0
    #wzgórze malejące
    for i in range(len(clk) - 1):
        if (clk[i] == 1 and clk[i + 1] == 0):
            if (ttl[i] == 0):
                currentValue = 1
            else:
                currentValue = -1
        #wzgórze narastające
        elif (clk[i] == 0 and clk[i + 1] == 1):
            if (ttl[i] == ttl[i + 1]):
                currentValue *= -1
        M_C.append(currentValue)
    return M_C

def DekoderManchester(clock, manchester, samplesPerbit):
    quarterSamplesPerBit = int(samplesPerbit / 4)
    clock = tile(1, quarterSamplesPerBit) + clock
    clock = clock[:int(len(clock) - quarterSamplesPerBit)]

    bits = []
    for i in range(len(clock) - 1):
        #wzgórze malejące
        if (clock[i] == 1 and clock[i + 1] == 0):
            bits.append(manchester[i])
    return bits

def MT(mt,LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(1)
    xcords=np.linspace(0,1,len(ycords))
    return xcords, ycords

def ASK(mt,LIMIT):
    ycords=[] ; xcords = []
    for i in range (LIMIT):
        if(mt[i]==0):
            for x in np.linspace(1/10,2/10):
                ycords.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                ycords.append(np.sin(40*np.pi*(x  - 1/10 )*1))
    xcords=np.linspace(0,1,len(ycords))
    return xcords, ycords

def demodulator1(Modulacja,h):
    Demo=[] ; Final=[] ;  Demov2 = []
    sum=0 ; sumabs = 0

    for i in range (len(Modulacja)):
        if (Modulacja[i] == 0.0000000):
            sum = 0
        sum=sum+Modulacja[i]
        Demo.append(sum)

    for i in range (len(Modulacja)):
        if (Modulacja[i] == 0.0000000):
            sumabs = 0
        if (Modulacja[i]>h):
            sumabs=sumabs+(Modulacja[i])
        Demov2.append(sumabs)

    for i in range (len(Demov2)):
        roundmt=round(Demov2[i],0)
        if(roundmt==0):
            for x in np.linspace(1/10,2/10):
                Final.append(0)
        else:
            for x in np.linspace(1/10,2/10):
                Final.append(1)

    return Demo,Demov2,Final

def spectrum(ycords):
    spectrum = np.fft.rfft(ycords)
    xcords = np.linspace(0,1,len(spectrum))
    return xcords,spectrum
