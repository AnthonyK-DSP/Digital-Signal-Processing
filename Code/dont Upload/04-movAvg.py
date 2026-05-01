import numpy as np
import dspCustom as dsp

ip=np.load("d:\python\ipx.npy")
N=ip.size
fs=40000.0 #Sampling Freq
xd1=np.append(0,ip)
xd1=np.delete(xd1,N)
xd2=np.append(0,xd1)
xd2=np.delete(xd2,N)
movAv3=ip+xd1+xd2
title=r'$3\ Term\ Moving\ Average\ Filter\ Output$'
dsp.timePlot(N,fs, movAv3,title)


