import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создание пространства для анимации
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
frames = 200
t = np.linspace(0, 100, frames)

k = 0.02
p = 0.01
V = 0.01
g = 9.81
m = 0.01
w = 0.3
r = 0.1
a = 1.3


# Вертикальная турбулентность
# Центростремительная сила

def move_func(s, t):
    x, vx, y, vy, z, vz = s
    dx_dt = vx
    dvx_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * x + k * vx + (m * w ** 2 * r) + (m * vx ** 2 / r)
    dy_dt = vy
    dvy_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * y + k * vy + (m * w ** 2 * r) + (m * vy ** 2 / r)
    dz_dt = vz
    dvz_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * z + k * vz + (m * w ** 2 * r) + (m * vz ** 2 / r)

    return dx_dt, dvx_dt, dy_dt, dvy_dt, dz_dt, dvz_dt


x0 = 1
vx0 = 0.2
y0 = 0
vy0 = 0.4
z0 = 1
zv0 = 0.8
s0 = x0, vx0, y0, vy0, z0, zv0

sol = odeint(move_func, s0, t)

ball, = ax.plot([], [], [], 'o', color='b')
line, = ax.plot([], [], [], '-', color='b')


def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball.set_3d_properties([sol[i][3]])

    line.set_data(sol[:i + 1, 0], sol[:i + 1, 2])
    line.set_3d_properties(sol[:i + 1, 3])
    return ball, line


edge = 3
ax.set_xlim([-edge, edge])
ax.set_xlabel('X')

ax.set_ylim([-edge, edge])
ax.set_ylabel('Y')

ax.set_zlim([-edge, edge])
ax.set_zlabel('Z')

# Анимирование
ani = FuncAnimation(fig, animate, frames=frames, interval=30, blit=True)

plt.show()
