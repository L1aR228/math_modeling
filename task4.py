import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 200
t = np.linspace(0, 5, frames)
k = 500
m = 0.8
u = 0.1 / (1 * 0.5)
# Определяем функцию для системы диф. уравнений
def move_func(z, t,g, k, m):
    x, vx = z

    dx_dt = vx
    dxvx_dt = - g - (k/m)*x

    return dx_dt, dxvx_dt


# Определяем начальные значения и параметры
g = 9.8
v = 20
alpha = 60 * np.pi / 180

x0 = 0
vx0 = v * np.cos(alpha)
y0 = 0
vy0 = v * np.sin(alpha)

z0 = x0, vx0

sol = odeint(move_func, z0, t, args=(g, k, m))

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')


def animate(i):
    ball.set_data([0], [sol[i][0]])



ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 1
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()