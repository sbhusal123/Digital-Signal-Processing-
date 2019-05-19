import numpy as np
import matplotlib.pyplot as plt




def exponential_wave(lower_lim,upper_lim,interval,amplitude,increasing = 1):
    '''

    :param lower_lim: lower_limit of the sampling data in x
    :param upper_lim: upper limit of the sampling data in x
    :param interval: interval at which to sample
    :param increasing: if decreasing exponential, set this to 0, by default 1(increasing)
    :param amplitude: amplitude of the exponential wave
    :return: returns the list of x and y popints
    '''

    x = np.linspace(lower_lim,upper_lim,interval)

    if(increasing):
        y = amplitude*np.exp(x)
    else:
        y = amplitude * np.exp(-x)

    plt.plot(x,y)

    plt.show()


exponential_wave(0,10,100,10,0)













