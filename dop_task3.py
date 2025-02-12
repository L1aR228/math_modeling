import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 200
t = np.linspace(0, 10, frames)
k = 125
m = 250000
u = 3000
k = 1000
# Определяем функцию для системы диф. уравнений
def move_func(z, t, g, k, m):
    x, vx = z
    dx_dt = vx
    dxvx_dt = (u * 1000 - m * g)/m
    return dx_dt, dxvx_dt


# Определяем начальные значения и параметры
g = 9.8
v = 10


x0 = 0
vx0 = 0

z0 = x0, vx0

sol = odeint(move_func, z0, t, args=(g, k, m))

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')


def animate(i):
    ball.set_data([0], [sol[i][0]])



ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 100
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()