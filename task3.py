import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 200
t = np.linspace(0, 5, frames)
k1 = 1
A0 = 100
k2 = 2


# Определяем функцию для системы диф. уравнений
def move_func(z, t, k1, k2, A0):
    x, y = z

    dx_dt = k1 * (A0 - x - y)

    dy_dt = k2 * (A0 - x - y)

    return dx_dt, dy_dt


# Определяем начальные значения и параметры
g = 9.8
v = 15
alpha = 30 * np.pi / 180

x0 = 0

y0 = 0

z0 = x0, y0

sol = odeint(move_func, z0, t, args=(k1, k2, A0))

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')


def animate(i):
    ball.set_data([sol[i][0]], [A0 * 0.5])
    ball_line.set_data(sol[:i, 0], [A0 * 0.5] * i)
    ball2.set_data([sol[i][1]], [A0 * 0.25])
    ball_line2.set_data(sol[:i, 1], [A0 * 0.25] * i)


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 100
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.show()
