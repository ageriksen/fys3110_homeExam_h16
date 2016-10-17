"""
This is a quick program to plot the probability curve of 
a state with known initial state. 
"""
# imports
import numpy as np
import matplotlib.pyplot as plt

#constants
#J = 1 # units of energy unknown, immaterial for now. 
#h_ = 1.054e-34 #J*s, reduced planck constant (low accuracy)


#settign function 
def P(t):
    return (5./9) + (4./9)*np.cos( 3*t/2)

# defining time array
t = np.linspace(0, 10, 1e4) # could be nanoseconds
p = P(t)

# plotting:

plt.plot(t, p, label=('sketch of probability'))
plt.legend()
plt.title('visualization of probability of state over time')
plt.show()
