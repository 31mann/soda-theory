"""
This code is for implementing the differences of  periodic property of Complex exponential & Sinusoidal Signal
of Continuous Time Domain & Discrete Time Domain

In this I have created 4 different Cosine Signal, Out of which 2 are CTS and other are DTS The two CTS have two
different frequency respectively and the DTS are sampled of these two By plot the graph of these 4 Signal I will
understand the difference of the periodic property of Complex exponential & Sinusoidal Signal """


import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0, 36, 2)
t1 = np.arange(0, 62, 1)
n = np.arange(0, 36, 1)
n1 = np.arange(0, 62, 1)
# This CT Signal have a frequency of 2*pi/12
xt = np.cos((2 * np.pi * t) / 12)              # It has Fundamental period of N = 12
# This CT Signal have a frequency of 8*pi/31
xt1 = np.cos((8 * np.pi * t1) / 31)            # It has Fundamental period of N = 31/4
# These 2 are DTS which are sampled from above CTS
xn = np.cos((2 * n / 12) * np.pi)              # It has Fundamental period of N = 12
xn1 = np.cos((8 * n1 / 31) * np.pi)             # It has Fundamental period of N = 31

plt.subplot(2, 2, 1)
plt.plot(t, xt)
plt.subplot(2, 2, 2)
plt.plot(t1, xt1)
plt.subplot(2, 2, 3)
plt.stem(n, xn)
plt.subplot(2, 2, 4)
plt.stem(n1, xn1)
plt.show()
