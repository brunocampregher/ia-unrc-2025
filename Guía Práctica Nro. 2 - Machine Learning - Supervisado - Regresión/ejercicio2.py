import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1) Generar datos sintéticos
# -----------------------------
N = 10 # Cantidad de datos generados
x = np.linspace(1, N, N)
e = np.random.normal(0, 1, N)  # ruido ~ N(0,1)
y = 3 * x + 2 + e              # datos reales

# -----------------------------
# 2) Ecuación normal
# -----------------------------
def minimos_cuadrados(x, y):
    X = np.column_stack((np.ones(len(x)), x))
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return theta  # [b, w]

# -----------------------------
# 3) Gradiente descendente
# -----------------------------
def gradiente_descendente(x, y, eta=0.01, n_iter=1000):
    y = y.reshape(-1,1)
    X = np.column_stack((np.ones(len(x)), x))
    theta = np.zeros((2,1))
    errores = []

    for iteration in range(n_iter):
        y_hat = X @ theta # Valor estimado
        mse = (1/len(x)) * np.sum((y_hat - y)**2) # Error
        errores.append(mse)

        gradients = (1/len(x)) * X.T @ (y_hat - y)
        theta = theta - eta * gradients # Actualización de theta

    return theta, errores

# -----------------------------
# 4) Calcular parámetros
# -----------------------------
theta_normal = minimos_cuadrados(x, y)
theta_gd, errores = gradiente_descendente(x, y)

print("Ecuación normal: θ0={:.4f}, θ1={:.4f}".format(theta_normal[0], theta_normal[1]))
print("Gradiente descendente: θ0={:.4f}, θ1={:.4f}".format(theta_gd[0,0], theta_gd[1,0]))

# -----------------------------
# 5) Graficar puntos y rectas
# -----------------------------
plt.scatter(x, y, color="blue", label="Datos")

# Línea ecuación normal
b1, w1 = theta_normal
plt.plot(x, w1*x + b1, color="red", label=f"Ecuación Normal: y={w1:.2f}x+{b1:.2f}")

# Línea gradiente descendente
b2, w2 = theta_gd.flatten()
plt.plot(x, w2*x + b2, color="green", linestyle="--", label=f"Gradiente Desc.: y={w2:.2f}x+{b2:.2f}")

plt.legend()
plt.title("Regresión lineal: comparación de métodos")
plt.show()

# -----------------------------
# 6) Graficar convergencia del error
# -----------------------------
plt.plot(errores, color="purple")
plt.xlabel("Iteraciones")
plt.ylabel("Error (MSE)")
plt.title("Convergencia del error - Gradiente Descendente")
plt.show()
