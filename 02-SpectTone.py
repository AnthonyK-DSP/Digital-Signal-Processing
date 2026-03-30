import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
plt.style.use('file:///d:/book/dspbook.mplstyle')
plt.close("all")
A,fa,fs,N= 10,1000,8000,200
n = np.arange(0, N) #Discrete time values
t=1000*n/fs
Q=2*np.pi*fa/fs # Normalised frequency
tone=A*np.sin(n*Q)
freq = np.arange(0,N)*fs/N    
M = 2*np.abs(scipy.fftpack.fft(tone))/N
plt.plot(freq,M)
title='Spectrum of Tone'
plt.title(title)
plt.xlabel('Frequency (Hz)')
plt.show()
