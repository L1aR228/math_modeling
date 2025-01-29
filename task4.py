import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# определяем переменную величину

t = np.arange(-5, 5, 0.01)


# Определяем функцию для системы диф уравнений
def diff_func(z1, t):
    k, y = z1

    dk_dt = (-4*k) - (5 * y)
    dy_dt = k

    return dk_dt, dk_dt


k0 = 4
y0 = -1

z0 = y0, k0

sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 0])
plt.show()
