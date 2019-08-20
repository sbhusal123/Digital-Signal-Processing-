# numerical at : http://www.songho.ca/dsp/convolution/convolution2d_example.html

import numpy as np

from scipy import signal

x1 = np.array([[1,2,3,4],
               [3,4,5,6],
               [7,8,9,10]])

x2 = np.array([[1,1],
               [1,1]])

x3 = signal.convolve(x1,x2,mode='full',method='auto')

#the simple concept is zero padding (over boundary of 2d matrix) and using stride of 1
# and add the dot product of elements os x1 and x2, then

print(x3)




