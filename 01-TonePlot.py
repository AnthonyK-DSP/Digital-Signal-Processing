import numpy as np
import matplotlib.pyplot as plt
plt.style.use('file:///d:/book/dspbook.mplstyle')
plt.close("all")
A=10
fa=1000 #Analogue Freq
fs=8000.0 #Sampling Freq
N=20 #No. of display samples
n = np.arange(0, N) #Discrete time values
t=1000*n/fs
Q=2*np.pi*fa/fs # Normalised frequency
tone=A*np.sin(n*Q)
plt.stem(t,tone)
plt.title('1 kHz Tone of amplitude 10 V')
plt.xlabel('Time (msecs)')
plt.show()

