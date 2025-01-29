import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# определяем переменную величину

t = np.arange(-5, 5, 0.01)

e = 2.71


# Определяем функцию для системы диф уравнений
def diff_func(z1, t):
    x, y = z1

    dtheta_dt = 3 * x - 2 * y + (e ** (3 * t) / ((e ** t) + 1))

    domega_dt = x - (e ** 3 * t / (e ** t + 1))

    return dtheta_dt, domega_dt


theta0 = 5
omega0 = -7

z0 = theta0, omega0

sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:], 'b')
plt.show()
