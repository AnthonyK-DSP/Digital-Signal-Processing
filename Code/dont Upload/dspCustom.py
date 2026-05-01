# dspCustom.py
import numpy as np
import matplotlib.pyplot as plt

# Specify a custom time domain plot
def timePlot(N,fs,signal,title):
    plt.close("all")
    plt.style.use('file:///d:/book/dspbook.mplstyle')
    n = np.arange(0, N) #Discrete time values
    t=1000*n/fs
    plt.plot(t,signal)
    plt.title(title)
    plt.xlabel('Time (msecs)')
    plt.show()
    return


