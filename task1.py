import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры
N0 = 1       # Начальное количество бактерий
k = 0.1      # Коэффициент роста
t = np.linspace(0, 50, 500)  # Время от 0 до 50

# Функция для модели роста
def model(N, t, k):
    dNdt = k * N
    return dNdt

# Решение ОДУ
N = odeint(model, N0, t, args=(k,))

# Визуализация
plt.figure(figsize=(10, 5))
plt.plot(t, N, label='Количество бактерий (N)', color='blue')
plt.axhline(y=10*N0, color='red', linestyle='--', label='10 * N0')
plt.title('Рост популяции бактерий')
plt.xlabel('Время (t)')
plt.ylabel('Количество бактерий (N)')
plt.legend()
plt.grid()
plt.show()

# Время, чтобы количество увеличилось в 10 раз
time_to_tenfold = np.log(10) / k
print(f"Время, спустя которое количество бактерий станет в 10 раз больше: {time_to_tenfold:.2f} единиц времени.")
