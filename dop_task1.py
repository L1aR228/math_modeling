import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# определяем переменную величину

t = np.arange(-5, 5, 0.01)


# Определяем функцию для системы диф уравнений
def diff_func(z1, t):
    x, y, z = z1

    dx_dt = 3 * x - y + z
    dy_dt = x + y + z
    dz_dt = 4 * x - y + 4 * z

    return dx_dt, dy_dt, dz_dt


x0 = -71
y0 = 1
z0 = -3

zet = x0, y0, z0

sol = odeint(diff_func, zet, t)

plt.plot(t, sol[:])
plt.show()
