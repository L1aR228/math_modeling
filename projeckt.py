import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 300
t = np.linspace(0, 10, frames)


def vortex_func(s, t, k=1.0, vz=0.1):
    x, y, z = s
    # Уравнения движения для вихря с центростремительной силой
    dxdt = -k * y  # Скорость x пропорциональна -y
    dydt = k * x  # Скорость y пропорциональна x
    dzdt = vz  # Постоянное восходящее движение по оси Z
    return [dxdt, dydt, dzdt]


# Инициализация частиц вихря
num_particles = 10
initial_conditions = np.zeros((num_particles, 3))
theta = np.linspace(0, 2 * np.pi, num_particles)
initial_conditions[:, 0] = np.cos(theta)  # x
initial_conditions[:, 1] = np.sin(theta)  # y
initial_conditions[:, 2] = np.linspace(0, 1, num_particles)  # z для разной высоты

# Решение системы уравнений для каждой частицы
sol = np.zeros((frames, num_particles, 3))

for i in range(num_particles):
    sol[:, i, :] = odeint(vortex_func, initial_conditions[i], t)

# Создание анимации
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
lines = [ax.plot([], [], [], 'r-')[0] for el in range(num_particles)]
points = [ax.plot([], [], [], 'bo')[0] for el in range(num_particles)]

# Границы графика
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Анимация вихря')


def init():
    for line, point in zip(lines, points):
        line.set_data([], [])
        line.set_3d_properties([])
        point.set_data([], [])
        point.set_3d_properties([])
    return lines + points


def animate(i):
    for j in range(num_particles):
        lines[j].set_data(sol[:i, j, 0], sol[:i, j, 1])  # История траектории
        lines[j].set_3d_properties(sol[:i, j, 2])  # Z-координаты для линии
        points[j].set_data([sol[i, j, 0]], [sol[i, j, 1]])  # Текущая позиция
        points[j].set_3d_properties(sol[i, j, 2])  # Текущая позиция по оси Z
    return lines + points


ani = FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=30)

plt.show()
