import os, numpy as np, matplotlib.pyplot as plt
location=os.path.expanduser('~')
path=os.path.join(location,'python','c.mplstyle')
plt.style.use(path)
title=r'$20log_{10}(|H(\theta)|^2)$'
b,fs=0.6, 16000
theta=np.arange(0,np.pi,np.pi/32)
f=theta*fs/(2*np.pi);
magH_sqr=(1+2*b*np.cos(theta)+b*b)
Hnorm_sqr=magH_sqr/(1+b)**2
HdB=10*np.log10(Hnorm_sqr)
plt.plot(f,HdB)
plt.xlabel ('Frequency (Hz)')
plt.title (title)
plt.show()

