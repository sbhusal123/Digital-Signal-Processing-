# Digital-Signal-Processing
This repository is for the learning of digital signal processing and simulation in python.

# 1. Fourier Transform 
Basically the fourier transform is signal processing techniques used in finding the frequency component 
present in the given signal. Basic intution of the fourier transform can be better described by the figure
below:

![Fourier Transform](https://github.com/sbhusal123/Digital-Signal-Processing-/blob/master/Figures/fourier_transform1.png)

Basically i've created the two sine signal of frequency o.2, 0.8 with amplitude 5 and 12 respectively
as shown in the first and second subplot, while in the third plot green line shows the signal being 
superposed. 

So to find out the frequencies present in the superposed signal, fourier transform is used.
In the third figure, major spikes at 0.2 and 0.8 shows the presence of such ferquency components.

# 2. Convolution

Convolution is a term used in signal processing which simply means **coiling or twisting of two signals**

### Techniques of convolution:

1. By direct sum method.
2. Or by using the property of fourier transform 
   <img align="center" src="https://tex.s2cms.ru/svg/f(t)*g(t)%20%3D%20ft%5E%7B-1%7D(F(f)*G(f))%20" alt="f(t)*g(t) = ft^{-1}(F(f)*G(f)) " />
   
#### Example:

![](https://github.com/sbhusal123/Digital-Signal-Processing-/blob/master/Figures/convolution_log_sine.png?raw=true)

Basically to convolve, two of the continous signal is taken in consideration logarithmic signal(plot1), sinusoidal signal(plot2). While the third plot shows the convolution obtained. 

 > In the third plot, amplitude of the sine wave is gradually increasing on the logarithmic fashion.
 > Mode of convolution is taken full. i.e the length of convolution is 1999. (N1+ N2-1)
 
 [Code ](https://github.com/sbhusal123/Digital-Signal-Processing-/blob/master/Convolution/example2.py)









 
