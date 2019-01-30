import numpy as np



t = np.linspace(0,10,5) # output is [0 2.5  5  7.5  10]

'''
How linspace works?

suppose x = np.linspace(0,10,5)

starting_point = 0

end_point = 10

no_of_points = 5


n-th item = starting_point + (n-1) * (end_point - starting_point) / (no_of_points)

# d = (end_point - starting_point) / (no_of_points)

So, what is does it gives is 5 points evenly spaced  between 0 and 10
'''

print(t)