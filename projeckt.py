import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 200
t = np.linspace(0, 10, frames)


k = 0.02
# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    x, vx, y, vy = s
    dx_dt = vx
    dvx_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * x + k * vx
    dy_dt = vy
    dvy_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * y + k * vx

    return dx_dt, dvx_dt, dy_dt, dvy_dt


# Определяем начальные значения и параметры

x0 = 1
vx0 = 0
y0 = 0
vy0 = 0.5

z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)

fig, ax = plt.subplots()
plt.axis('equal')
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')


def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 2
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
