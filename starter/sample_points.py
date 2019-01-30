import numpy as np
import matplotlib.pyplot as plt



# Number of samplepoints
N = 600

# sample spacing
T = 1.0 / 800.0

x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x)

plt.plot(x[0:30],y[0:30])

print(x[0:10])

plt.show()
