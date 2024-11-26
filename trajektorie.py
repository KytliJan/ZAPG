import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline


trajektorie= open('C:/Users/Peťas/Documents/GitHub/ZAPG/trajektorie.csv')


data = np.loadtxt(trajektorie, delimiter=',')
x_points, y_points, z_points = data[:, 0], data[:, 1], data[:, 2]


lagrange_x = lagrange(range(len(x_points)), x_points)
lagrange_y = lagrange(range(len(y_points)), y_points)
lagrange_z = lagrange(range(len(z_points)), z_points)


t = np.linspace(0, len(x_points) - 1, 1000)
x_hladka = lagrange_x(t)
y_hladka = lagrange_y(t)
z_hladka = lagrange_z(t)


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_points, y_points, z_points, color='red', label='Původní body')
ax.plot(x_hladka, y_hladka, z_hladka, color='blue', label='Interpolovaná trajektorie')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Hladká trajektorie Lagrangeovy interpolace')
ax.legend()
plt.show()

#Lagrangeova interpolace neprotíná poslední body, použijeme kubickou interpolaci, která lépe zvládá větší množství bodů


t_points = np.arange(len(x_points))
krivka_a = CubicSpline(t_points, x_points)
krivka_b = CubicSpline(t_points, y_points)
krivka_c = CubicSpline(t_points, z_points)


t_hladka = np.linspace(0, len(x_points) - 1, 1000)  
a_hladka = krivka_a(t_hladka)
b_hladka = krivka_b(t_hladka)
c_hladka = krivka_c(t_hladka)


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_points, y_points, z_points, color='red', label='Původní body')
ax.plot(a_hladka, b_hladka, c_hladka, color='blue', label='Interpolovaná trajektorie')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Hladká trajektorie kubické interpolace')
ax.legend()
plt.show()
# V kódu jsem si osy přejmenoval, v zadání jsou ale stejné, takže nechávám stejné i popisky os

