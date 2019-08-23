import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


log  = [sc.log(i) for i in np.linspace(0,100,1000)]
sine = [sc.sin(2*np.pi*0.2*i) for i in np.linspace(0,100,1000)]


convolved = np.convolve(sine,log,mode="full")
fig, (plt1,plt2,plt3) = plt.subplots(3,1)
fig.tight_layout() #for spacing between subplots


plt1.plot(np.linspace(0,100,1000),log)
plt1.set_title("Logarithmic signal")
plt1.set_xlabel("X")
plt1.set_ylabel("Y = log(X)")

plt2.set_title("Sinusoidal signal")
plt2.set_xlabel("X")
plt2.set_ylabel("Y = sin(2*pie*0.2*X)")
plt2.plot(np.linspace(0,100,1000),sine)

plt3.set_title("Convolution of two of above signal")
plt3.plot(-convolved)

plt.show()













