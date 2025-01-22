import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

V = 100
a0 = 10
Y = -0.5
m = 70  # Коэффициент роста(по условию)
t = np.arange(0, 10, 0.1)


def model(a0, t, Y):
    dNdt = a0 - Y / m * V ** 2
    return dNdt


N = odeint(model, m, t, args=(a0,))

plt.figure(figsize=(10, 5))
plt.plot(t, N, label='Деньги', color='blue')
plt.show()
