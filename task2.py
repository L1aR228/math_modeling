import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N0 = 1000  #Мои деньги
k = 0.08  # Коэффициент роста(по условию)
t = np.arange(0, 10, 0.1)


def model(N, t, k):
    dNdt = -k * N * t
    return dNdt


N = odeint(model, N0, t, args=(k,))

plt.figure(figsize=(10, 5))
plt.plot(t, N, label='Деньги', color='blue')
plt.show()
