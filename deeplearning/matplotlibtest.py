import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, np.pi * 2, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos", linestyle="--")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()