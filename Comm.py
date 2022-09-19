import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
z=np.linspace(0,3,12*1024)
𝑁 = 3*1024
k = np. linspace(0 , 512 , int(𝑁/2))

def CLA(z):
    return np.where(z>=0,1,0)

right=[0,261.63,0,261.63,0,329.66]
left=[220,0,220,0,246.93,0]

rT1=[0,0.8,1.5,2.1,2.3,2.7]
rT2=[0.8,1.5,2,2.3,2.7,3]

f=0	
for x in range(len(right)):
    f+= ((np.sin(2*np.pi*right[x]*z)+np.sin(2*np.pi*left[x]*z))*(CLA(z-rT1[x])-CLA(z-rT2[x])))
	     
    
#sd.play(f,3*1024)
x_f=fft(f)
x_f=2/N*np.abs(x_f[0:np.int(N/2)])
plt.subplot(3,2,1)
plt.plot(z, f)
plt.subplot(3,2,2)

plt.plot(k, x_f)


ff1=np.random.randint(0,512)
ff2=np.random.randint(0,512)
dd =np.sin(2*ff1*np.pi*z)+np.sin(2*ff2*np.pi*z)
dd2=f+dd
dd2_f=fft(dd2)
dd2_f=2/N*np.abs(dd2_f[0:np.int(N/2)])
plt.subplot(3,2,3)
plt.plot(z, dd2)
plt.subplot(3,2,4)
plt.plot(k,dd2_f)


m1=np.max(x_f)+0.1
fill=dd2
for i in range(0,np.size(k)):
    if (dd2_f[i]>m1):
        fill-=np.sin(2*np.pi*np.int(k[i])*z)

fill_f=fft(fill)
fill_f=2/N*np.abs(fill_f[0:np.int(N/2)])
plt.subplot(3,2,5)
plt.plot(z, fill)
plt.subplot(3,2,6)
plt.plot(k,fill_f)
sd.play(fill,3*1024)




