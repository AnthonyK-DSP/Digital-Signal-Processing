import numpy as np
import matplotlib.pyplot as plt
#import scipy.fftpack
plt.style.use('file:///d:/book/dspbook.mplstyle')
plt.close("all")
A1,A2,fa1,fa2,fs,N= 10,6,500,5000,50000,250
n = np.arange(0, N) #Discrete time values
t=1000*n/fs
Q1=2*np.pi*fa1/fs # Normalised frequency
Q2=2*np.pi*fa2/fs
dualTone=A1*np.sin(n*Q1)+A2*np.sin(n*Q2)
plt.plot(t,dualTone)
plt.title('DualTone Signal')
plt.xlabel('Time (msecs)')
plt.show()
x=dualTone
np.save("d:\python\ipx.npy",dualTone)


import numpy as np
import matplotlib.pyplot as plt
x=np.load("d:\python\ipx.npy")
xd1=np.append(0,x)
xd1=np.delete(xd1,N)
diff=x-xd1
title='Difference Filter o/p'
plt.plot(t,diff)
plt.title('Difference Signal')
plt.xlabel('Time (msecs)')
plt.show()
