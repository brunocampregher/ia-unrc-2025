import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 8])

X = np.column_stack((np.ones(len(x)), x))

XtX = X.T @ X

XtXinv = np.linalg.inv(XtX)

XtXinvXt = XtXinv @ X.T

theta = XtXinvXt @ y

b, w = theta

plt.scatter(x, y, color="blue", label="Datos")

plt.plot(x, w*x + b, color="red", label=f"Recta: y={w:.2f}x+{b:.2f}")

plt.show()
