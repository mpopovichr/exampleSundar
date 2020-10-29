import numpy as np
import matplotlib.pyplot as plt


xRange= np.linspace(-np.pi, np.pi, 3000)
plt.plot(xRange,
         np.cos(xRange))
plt.show()

