from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,10,10000)

sig1 = np.sin(x)

sig2 = x+3


conv = signal.convolve(sig1,sig2,mode='full',method='auto')*100/(sum(sig2))

fig,(sig1_plot,sig2_plot,sig_conv) = plt.subplots(3,1)
# output can be seen in the picture named convolve.



sig1_plot.plot(sig1)
sig1_plot.set_title("First Signal")

sig2_plot.plot(sig2)
sig2_plot.set_title("Second Signal")


# x = np.linspace(0,10,1999)


sig_conv.plot(conv)
sig_conv.plot(x)
sig_conv.set_title("Convolved Signal")



plt.show()