import numpy as np
import matplotlib.pyplot as plt

#zadání úlohy 1
# f(x) = x + e**x 
#x = np.linspace(2,5,10)


def f(x):
    return x + np.exp(x)

def integral(a, b):
    return (b**2 / 2 + np.exp(b)) - (a**2 / 2 + np.exp(a))

# Numerická integrace pomocí trapezoidálního pravidla
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    return dx * (np.sum(y) - (y[0] + y[-1]) / 2)

a = 2
b = 5
reseni = integral(a, b)  # analytické řešení


n_values = np.logspace(1, 4, 20, dtype=int)
chyba = []

for n in n_values:
    numericke_reseni = trapezoidal_rule(f, a, b, n)
    error = abs(numericke_reseni - reseni)
    chyba.append(error)


print("analytické řešení = ",reseni)
plt.figure(figsize=(10, 6))
plt.loglog(n_values, chyba, '-o', label="Chyba numerické integrace")
plt.xlabel("Počet dílků (n)")
plt.ylabel("Absolutní chyba")
plt.title("konvergence pro integraci f(x) = x + e^x")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()



# Zadání úlohy 4
#f(x)= 3 / ((x - 1)**2 + 1)
#f(x) = np.sqrt(x + 0.5) 
#f(x) = e**(-x)

# Průsečíky:
#f12 = lambda x: f1(x) - f2(x)
#f13 = lambda x: f1(x) - f3(x)
#f23 = lambda x: f2(x) - f3(x)

from scipy.optimize import fsolve

f1 = lambda x: 3 / ((x - 1)**2 + 1)
f2 = lambda x: np.sqrt(x + 0.5)
f3 = lambda x: np.exp(-x)

x = np.linspace(-1, 8, 500) # X-ové souřadnice do 8 pro lepší viditelnost 
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$f_1(x) = \frac{3}{(x - 1)^2 + 1}$', color='blue')
plt.plot(x, y2, label=r'$f_2(x) = \sqrt{x} + 0.5$', color='green')
plt.plot(x, y3, label=r'$f_3(x) = e^{-x}$', color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafy funkcí $f_1(x)$, $f_2(x)$, $f_3(x)$')
plt.legend()
plt.grid(True)
plt.show()

# Druhá část 
# a)

def f12(x):
    return (3 / ((x - 1)**2 + 1)) - (np.sqrt(x + 0.5))

x12 = fsolve(f12, x0=2)  # x0 je počáteční odhad
print(f"x12 = {x12[0]:.4f}")

def f13(x):
    return (3 / ((x - 1)**2 + 1)) - (np.exp(-x))

x13 = fsolve(f13, x0=-0.5)
print(f"x13 = {x13[0]:.4f}")

def f23(x):
    return (np.sqrt(x + 0.5) ) - (np.exp(-x))

x23 = fsolve(f23, x0=0.5)  
print(f"x23 = {x23[0]:.4f}")

# b)


def metoda_puleni(func, a, b, tolerance):
    # Zkontrolujeme, zda na okrajích intervalu existuje změna znaménka
    if func(a) * func(b) >= 0:
        print("Funkce nemá v intervalu [a, b] průsečík nebo má více průsečíků.")
        return None
    
    # Hledání průsečíku s danou přesností
    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:  # Přesný průsečík nalezen
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    
    
    return (a + b) / 2


a, b = -1, 3
tolerance = 0.0001

# Výpočet průsečíků metodou půlení intervalu
x12_bisection = metoda_puleni(f12, a, b, tolerance)
x13_bisection = metoda_puleni(f13, a, b, tolerance)

a, b = 0, 1 # Pro x23 byl interval -1, 3 příliš velký

x23_bisection = metoda_puleni(f23, a, b, tolerance)

print(f"x12 (půlení intervalu) = {x12_bisection:.4f}")
print(f"x13 (půlení intervalu) = {x13_bisection:.4f}")
print(f"x23 (půlení intervalu) = {x23_bisection:.4f}")


#
#
# Asi jsem trochu odbočil, tady je pokračování dle zadání z githubu
#
#


def f(x):
    return 3 / ((x - 1)**2 + 1)

def f_referencni(a, b):
    return (3*np.arctan(b - 1)) - (3*np.arctan(a - 1))


# Numerická integrace pomocí trapezoidálního pravidla
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    return dx * (np.sum(y) - (y[0] + y[-1]) / 2)


a = -1
b = 3
reseni = f_referencni(a, b)

n_values = np.logspace(1, 4, 20, dtype=int)
chyba = []

for n in n_values:
    numericke_reseni = trapezoidal_rule(f, a, b, n)
    error = abs(numericke_reseni - reseni)
    chyba.append(error)

plt.figure(figsize=(10, 6))
plt.loglog(n_values, chyba, '-o', label="Chyba numerické integrace")
plt.xlabel("Počet dílků (n)")
plt.ylabel("Absolutní chyba")
plt.title("Konvergence numerické integrace pro f(x) = 3 / ((x - 1)^2 + 1)")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
print("Referenční numerické řešení =", reseni)




def f(x):
    return np.sqrt(x + 0.5)

def f_referencni(a, b):
    return ((2*(b+0.5)*np.sqrt(b+0.5))/3) - ((2*(a+0.5)*np.sqrt(a+0.5))/3)


def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    return dx * (np.sum(y) - (y[0] + y[-1]) / 2)


a = 0
b = 3
reseni = f_referencni(a, b)

n_values = np.logspace(1, 4, 20, dtype=int)
chyba = []

for n in n_values:
    numericke_reseni = trapezoidal_rule(f, a, b, n)
    error = abs(numericke_reseni - reseni)
    chyba.append(error)

plt.figure(figsize=(10, 6))
plt.loglog(n_values, chyba, '-o', label="Chyba numerické integrace")
plt.xlabel("Počet dílků (n)")
plt.ylabel("Absolutní chyba")
plt.title("Konvergence numerické integrace pro f(x) = √x+0.5")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
print("Referenční numerické řešení =", reseni)


def f(x):
    return np.exp(-x)

def f_referencni(a, b):
    return (-1/(np.exp(b))) - (-1/(np.exp(a)))


def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    return dx * (np.sum(y) - (y[0] + y[-1]) / 2)


a = -1
b = 3
reseni = f_referencni(a, b)

n_values = np.logspace(1, 4, 20, dtype=int)
chyba = []

for n in n_values:
    numericke_reseni = trapezoidal_rule(f, a, b, n)
    error = abs(numericke_reseni - reseni)
    chyba.append(error)

plt.figure(figsize=(10, 6))
plt.loglog(n_values, chyba, '-o', label="Chyba numerické integrace")
plt.xlabel("Počet dílků (n)")
plt.ylabel("Absolutní chyba")
plt.title("Konvergence numerické integrace pro f(x) = e^(-x)")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
print("Referenční numerické řešení =", reseni)