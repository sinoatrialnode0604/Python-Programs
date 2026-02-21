import matplotlib.pyplot as plt
import numpy as np

x = np.array([12,16,20,24])
y = x * 2

plt.plot(x,y)

x1 = np.array([4,8,12,16])
y1 = x1 * 4

plt.plot(x1,y1,'+')
plt.show()