from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

'''
 -> documentation at : https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html#scipy.signal.convolve
 
'''

sig1 = np.array([1,2,3])

sig2 = np.array([1,2,3])


conv = signal.convolve(sig1,sig2,mode='full',method='auto')
'''
This method is explained intutively in the figure named "convoln".
'''


'''

mode : str {‘full’, ‘valid’, ‘same’}, optional

    A string indicating the size of the output:

    full

        The output is the full discrete linear convolution of the inputs. (Default)
    valid

        The output consists only of those elements that do not rely on the zero-padding. In ‘valid’ mode, either in1 or in2 must be at least as large as the other in every dimension.
    same

        The output is the same size as in1, centered with respect to the ‘full’ output.
        
method : str {‘auto’, ‘direct’, ‘fft’}, optional

    A string indicating which method to use to calculate the convolution.

    direct

        The convolution is determined directly from sums, the definition of convolution.
    fft

        The Fourier Transform is used to perform the convolution by calling fftconvolve.
    auto

        Automatically chooses direct or Fourier method based on an estimate of which is faster (default). See Notes for more detail.

'''

print(conv)

fig,(sig1_plot,sig2_plot,sig_conv) = plt.subplots(3,1)
# output can be seen in the picture named convolve.



sig1_plot.plot(sig1)
sig2_plot.plot(sig2)
sig2_plot.set_title("Second Signal")



sig_conv.plot(conv)
sig_conv.set_title("Convolved Signal")


plt.show()
