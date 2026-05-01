import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
plt.style.use('file:///d:/book/dspbook.mplstyle')
plt.close("all")
A1,A2,fa1,fa2,fs,N= 10,6,400,2000,8000,200
n = np.arange(0, N) #Discrete time values
t=1000*n/fs
Q1=2*np.pi*fa1/fs # Normalised frequency
Q2=2*np.pi*fa2/fs
dualTone=A1*np.sin(n*Q1)+A2*np.sin(n*Q2)
freq = np.arange(0,N)*fs/N    
M = 2*np.abs(scipy.fftpack.fft(dualTone))/N
plt.plot(freq,M)
title='Spectrum of Dual Tone'
plt.title(title)
plt.xlabel('Frequency (Hz)')
plt.show()

freq = np.arange(0,N/2)*fs/N    
M = 2*np.abs(scipy.fftpack.fft(dualTone))/N
M = M[0:int(N/2)]
plt.plot(freq,M)
title='Spectrum of Dual Tone (up to fs/2)'
plt.title(title)
plt.xlabel('Frequency (Hz)')
plt.show()

