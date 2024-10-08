import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math


x = np.linspace(0,2)
y1= np.exp(x)
y2 = x**3 + x**2 + x

plt.plot(x, y1, label="e^x", color="blue")
plt.plot(x, y2, label="x^3 + x^2 + x", color="green")

plt.title("Grafy funkcí")
plt.xlabel("x")
plt.ylabel("y")

plt.legend() #legenda pro rozlišení křivek
plt.show() # Zobrazení grafu


#tridiagonální matice 10x10
n = 10
A = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:  # hlavní diagonála
            A[i, j] = 2
        elif i == j + 1 or i == j - 1:  # nad a pod diagonálou
            A[i, j] = -1


plt.imshow(A, cmap="Blues", interpolation="none")
plt.colorbar() #legenda barev
plt.title("Tridiagonální matice")
plt.show()


B = np.zeros((n, n))

# Vyplnění horní trojúhelníkové matice s hodnotami 1-10 na diagonále a libovolnými hodnotami nahoře
for i in range(n):
    for j in range(n):
        if i == j:  # hlavní diagonála
            B[i, j] = i + 1
        elif i < j:  # horní trojúhelník
            B[i, j] = np.random.randint(1, 10)

# Zobrazení horní trojúhelníkové matice
plt.imshow(B, cmap="twilight", interpolation="bilinear") #asi né uplně nejlepší využít bilinear, ale je to hezký :)
plt.colorbar()
plt.title("Horní trojúhelníková matice s čísly 1-10")
plt.show()

# Druhá verze horní trojúhelníkové matice s konstantní hodnotou 5 v horním trojúhelníku
C = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:  # hlavní diagonála
            C[i, j] = i + 1
        elif i < j:  # horní trojúhelník
            C[i, j] = 5

# Zobrazení alternativní horní trojúhelníkové matice
plt.imshow(C, cmap="viridis", interpolation="none")
plt.colorbar()
plt.title("Horní trojúhelníková matice s fixními hodnotami nad diagonálou")
plt.show()
