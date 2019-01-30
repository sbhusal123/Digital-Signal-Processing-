import numpy as np

import matplotlib.pyplot as plt

fig, (p1,p2,p3) = plt.subplots(3,1)

fig.tight_layout()

t = np.linspace(0,10,1000)

a1 = 5
f1 = 1
x1 = a1*np.sin(2*np.pi*f1*t)

a2 = 5
f2 = 0.2
x2 = a2*np.sin(2*np.pi*f2*t)


x = x1+x2


p1.set_title("Sine wave with time period 1")
p1.set_xlabel("T")
p1.set_ylabel("Amplitude")
p1.plot(t,x1)


p2.set_title("Sine wave with time period 5")
p2.set_xlabel("T")
p2.set_ylabel("Amplitude")
p2.plot(t,x2)


p3.set_title("Addition of two above sine waves")
p3.set_xlabel("T")
p3.set_ylabel("Amplitude")


p3.plot(t,x)

plt.show()




