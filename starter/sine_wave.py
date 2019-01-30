import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,20,50000)

amplitude = 1

#one complete wave completes at given time period i.e determines the periodicity of the signal
timePeriod =  10

# no of wave per unit time
frequency = 1/timePeriod

# y = a*sin(omega*time) = a*sin(2*pie*f*t)
x = amplitude*np.sin(2*np.pi*frequency*t)

plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(t,x)

plt.show()
