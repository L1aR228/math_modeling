import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A0 = 100
k1 = 0.1
k2 = 0.05
k3 = 0.02
t = np.linspace(0, 100, 1000)


def model(y, t, k1, k2, k3):
    A, B, C = y
    dA_dt = -k1 * A
    dB_dt = k1 * A - k2 * B
    dC_dt = k2 * B - k3 * C
    return dA_dt, dB_dt, dC_dt


y0 = A0, 0, 0

solution = odeint(model, y0, t, args=(k1, k2, k3))

fig, ax = plt.subplots()
line_A, = ax.plot([], [], label='Вещество A', color='blue')
line_B, = ax.plot([], [], label='Вещество B', color='orange')
line_C, = ax.plot([], [], label='Вещество C', color='green')
edge = 100
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
ax.set_xlabel('Время')
ax.set_ylabel('Количество веществ')
ax.grid()


def init():
    line_A.set_data([], [])
    line_B.set_data([], [])
    line_C.set_data([], [])
    return line_A, line_B, line_C


def update(frame):
    line_A.set_data(t[:frame], solution[:, 0][:frame])
    line_B.set_data(t[:frame], solution[:, 1][:frame])
    line_C.set_data(t[:frame], solution[:, 2][:frame])
    return line_A, line_B, line_C


ani = FuncAnimation(fig, update, frames=1000, init_func=init, blit=True, interval=50)

plt.show()
