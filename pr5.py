import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
frames = 500
t = np.linspace(0, 400, frames)

k = 0.02
p = 0.01
V = 0.01
m = 0.0095
w = 0.26
r = 0.18
gama = 0.04
g = 9.81


def move_func(s, t):
    sp = []

    for i in range(10):
        idx = i * 6
        x, vx, y, vy, z, vz = s[idx:idx + 6]

        dx_dt = vx
        dvx_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * x + k * vx + (m * w ** 2 * r) + (m * vx ** 2 / r) - gama * (
                vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * x
        dy_dt = vy
        dvy_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * y + k * vy + (m * w ** 2 * r) + (m * vy ** 2 / r) - gama * (
                vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * y
        dz_dt = vz
        dvz_dt = k * vz + (m * w ** 2 * r) + p * V * g

        sp.extend([dx_dt, dvx_dt, dy_dt, dvy_dt, dz_dt, dvz_dt])

    return sp


s0 = []
vx0 = 0.1
vy0 = 0.2
vz0 = 0.4
x0 = 1
y0 = 0
z0 = 1
count_x = 0.1
count_y = 0.2
count_z = 0.4
for i in range(10):
    x0 = 1 + i * 0.001
    y0 = 0 + i * 0.001
    z0 = 1 + i * 0.001
    while vx0 < 0.1 or vy0 < 0.1 or vz0 < 0.1:
        vx0 = count_x + i * 0.01
        vy0 = count_y + i * 0.01
        vz0 = count_z + i * 0.01
    else:
        vx0 = 0.1 + i * 0.01
        vy0 = 0.2 + i * 0.01
        vz0 = 0.4 + i * 0.01
    print(x0)
    print(y0)
    print(z0)
    s0.extend([x0, vx0, y0, vy0, z0, vz0])

sol = odeint(move_func, s0, t)

balls = [ax.plot([], [], [], 'o', color='b')[0] for _ in range(10)]
lines = [ax.plot([], [], [], '-', color='b')[0] for _ in range(10)]


def animate(i):
    for j in range(10):
        balls[j].set_data([sol[i][j * 6]], [sol[i][j * 6 + 2]])
        balls[j].set_3d_properties([sol[i][j * 6 + 5]])
        lines[j].set_data(sol[:i + 1, j * 6], sol[:i + 1, j * 6 + 2])
        lines[j].set_3d_properties(sol[:i + 1, j * 6 + 5])

    return balls + lines


edge = 30
ax.set_xlim([-edge, edge])
ax.set_xlabel('X')
ax.set_ylim([-edge, edge])
ax.set_ylabel('Y')
ax.set_zlim([-edge, edge])
ax.set_zlabel('Z')

ani = FuncAnimation(fig, animate, frames=frames, interval=30, blit=True)
plt.show()
