import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

'''
actually magnitude plot is the plot of the harmonic  vs the amplitude of the corresponding harmonic 
'''

n = np.linspace(0,10,1000)

x = 5*np.sin(2*5*np.pi*n) + 50*np.sin(2*4*np.pi*n) + 40 * np.sin(2*np.pi*8*n)


xf = scipy.fftpack.fft(x)


power = abs(xf)*2 #multiplied by 2 because the amplitude is distributed to the the complex conjugate part too

plt.plot(10*n[0:100],power[0:100]/1000) #must scale otherwise plot wont be accurate
plt.title("Magnitude plot")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")

plt.show()





