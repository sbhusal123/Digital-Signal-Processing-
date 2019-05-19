import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

#still problem with understanding what the plot is giving??


x = np.linspace(0,10,1000)

y = 2*x+3

xf = scipy.fftpack.fft(y)

power = abs(xf)*2

fig , (p1,p2) = plt.subplots(2,1)

fig.subplots_adjust(hspace=1)

p2.plot(10*x[0:100],power[0:100]/1000) #must scale otherwise plot wont be accurate
p2.set_title("Magnitude plot")
p2.set_xlabel("Frequency")
p2.set_ylabel("Amplitude")



p1.plot(x,y) #must scale otherwise plot wont be accurate
p1.set_title("St Line Plot")
p1.set_xlabel("X")
p1.set_ylabel("Y")


plt.show()

