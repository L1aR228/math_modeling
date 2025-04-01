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
g = 9.81
m = 0.0095
w = 0.26
r = 0.18
a = 0.065
gama = 0.04003

def move_func(s, t):
    x, vx, y, vy, z, vz,\
        x2, vx2, y2, vy2, z2, vz2 = s
    dx_dt = vx
    dvx_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * x + k * vx + (m * w ** 2 * r) + (m * vx ** 2 / r) - gama * (vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * x
    dy_dt = vy
    dvy_dt = -(vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * y + k * vy + (m * w ** 2 * r) + (m * vy ** 2 / r) - gama * (vx ** 2 + vy ** 2) / (x ** 2 + y ** 2) * y
    dz_dt = vz
    dvz_dt = k * vz + (m * w ** 2 * r) + p * V * g

    dx_dt2 = vx2
    dvx_dt2 = -(vx2 ** 2 + vy2 ** 2) / (x2 ** 2 + y2 ** 2) * x2 + k * vx2 + (m * w ** 2 * r) + (m * vx2 ** 2 / r) - gama * (vx2 ** 2 + vy2 ** 2) / (x2 ** 2 + y2 ** 2) * x2
    dy_dt2 = vy2
    dvy_dt2 = -(vx2 ** 2 + vy2 ** 2) / (x2 ** 2 + y2 ** 2) * y2 + k * vy2 + (m * w ** 2 * r) + (m * vy2 ** 2 / r) - gama * (vx2 ** 2 + vy2 ** 2) / (x2 ** 2 + y2 ** 2) * y2
    dz_dt2 = vz2
    dvz_dt2 = k * vz2 + (m * w ** 2 * r) + p * V * g

    return dx_dt, dvx_dt, dy_dt, dvy_dt, dz_dt, dvz_dt, dx_dt2, dvx_dt2, dy_dt2, dvy_dt2, dz_dt2, dvz_dt2


x0 = 1
vx0 = 0.1
y0 = 0
vy0 = 0.2
z0 = 1
zv0 = 0.4


x02 = 1 + 0.05
vx02 = 0.2
y02 = 0
vy02 = 0.4
z02 = 1
zv02 = 0.6

s0 = x0, vx0, y0, vy0, z0, zv0, x02, vx02, y02, vy02, z02, zv02

sol = odeint(move_func, s0, t)

ball1, = ax.plot([], [], [], 'o', color='b')
line1, = ax.plot([], [], [], '-', color='b')
ball2, = ax.plot([], [], [], 'o', color='r')
line2, = ax.plot([], [], [], '-', color='r')

def animate(i):
    # Первое тело
    ball1.set_data([sol[i][0]], [sol[i][2]])
    ball1.set_3d_properties([sol[i][5]])
    line1.set_data(sol[:i + 1, 0], sol[:i + 1, 2])
    line1.set_3d_properties(sol[:i + 1, 5])

    # Второе тело
    ball2.set_data([sol[i][6]], [sol[i][8]])
    ball2.set_3d_properties([sol[i][5]])
    line2.set_data(sol[:i + 1, 6], sol[:i + 1, 8])
    line2.set_3d_properties(sol[:i + 1, 5])

    return ball1, line1, ball2, line2


edge = 10
ax.set_xlim([-edge, edge])
ax.set_xlabel('X')

ax.set_ylim([-edge, edge])
ax.set_ylabel('Y')

ax.set_zlim([-edge, edge])
ax.set_zlabel('Z')


ani = FuncAnimation(fig, animate, frames=frames, interval=30, blit=True)

ani.save('3.gif')