import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 200
t = np.linspace(0, 5, frames)

u = (0.1 / (1 * 0.5)) ** 2
# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    x, vx, y, vy = z

    dx_dt = vx
    dvx_dt = -u * vx
    dy_dt = vy
    dvy_dt = - g

    return dx_dt, dvx_dt, dy_dt, dvy_dt


# Определяем начальные значения и параметры
g = 9.8
v = 20
alpha = 60 * np.pi / 180

x0 = 0
vx0 = v * np.cos(alpha)
y0 = 0
vy0 = v * np.sin(alpha)

z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')


def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 30
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.show()