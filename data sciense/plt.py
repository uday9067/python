import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-100,100,100)
y=0.5 *x + x**2
plt.plot(x,y)
plt.show()
