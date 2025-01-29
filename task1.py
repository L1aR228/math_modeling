import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# определяем переменную величину

x = np.arange(-5, 5, 0.01)


# Определяем функцию для системы диф уравнений
def diff_func(z1, x):
    y, z = z1

    dtheta_dt = y ** 2 * z

    domega_dt = z / x - y * z**2

    return dtheta_dt, domega_dt


theta0 = 1
omega0 = -3

z0 = theta0, omega0


sol = odeint(diff_func, z0, x)


plt.plot(x, sol[:], 'b')
plt.show()