import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# определяем переменную величину

t = np.arange(-5, 5, 0.01)


# Определяем функцию для системы диф уравнений
def diff_func(z1, t):
    k, y = z1

    dk_dt = np.sin(t) + np.cos(t)
    dy_dt = k

    return dk_dt, dk_dt


k0 = 0
y0 = 3

z0 = k0, y0

sol = odeint(diff_func, z0, t)

plt.plot(t, sol)
plt.show()
