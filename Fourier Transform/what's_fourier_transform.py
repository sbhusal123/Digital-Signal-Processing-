import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

fig , (p1,p2,p3,p4) = plt.subplots(4,1)

fig.tight_layout()

x = np.linspace(0,10,1000)


a1 = 5
f1 = 0.2
y1 = a1*np.sin(2*np.pi*f1*x)


a2 = 12
f2 = 0.8
y2 = a2*np.sin(2*np.pi*f2*x)


p1.set_title("Sine signal with frequncy = "+str(f1)+" amplitude = "+str(a1))
p1.plot(x,y1)


p2.set_title("Sine signal with frequncy = "+str(f2)+" amplitude = "+str(a2))
p2.plot(x,y2)


y = y1+y2

p3.set_title("Superposition of two above signals.")
p3.plot(x,y1,'b--')
p3.plot(x,y2,'y--')
p3.plot(x,y,c='g')


y_fourier = scipy.fftpack.fft(y)


p4.set_title("Fourier transform of above two superposed signals. Major spikes at any x shows the presence of such harmonics")
p4.plot(10*x[0:50],y_fourier[0:50]/10)


plt.show()












