import numpy as np
import matplotlib.pyplot as plt

def plotTrig(a):
    xRange= np.linspace(-np.pi, np.pi, 3000)
    if a==1:
        plt.plot(xRange,
                 np.cos(xRange))
    if a==2:
        plt.plot(xRange,
                 np.sin(xRange))

xRange= np.linspace(-np.pi, np.pi, 3000)
plt.plot(xRange,
         np.sin(xRange))
plt.plot(xRange,
         np.cos(xRange))

plt.show()

