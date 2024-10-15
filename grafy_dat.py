import numpy as np
import matplotlib.pyplot as plt

# Načtení dat ze souborů
data1 = np.loadtxt('data1.txt')
data2 = np.loadtxt('data2.txt')

# Extrakce sloupců
x1 = data1[:, 0]
x2 = data2 [:, 0]
y1 = data1[:, 1]
y2 = data2[:, 1]

# Graf z dat 1

plt.plot(x1, y1, label='Data 1')
plt.yscale('log')  # Logaritmická osa Y
plt.ylabel('Y (Logarytmická osa Y)')
plt.xlabel('X')
plt.title('Graf dat 1')
plt.legend()
plt.show()

# Graf z dat 2

plt.plot(x2, y2, label='Data 2',color='red')
plt.yscale('log')
plt.ylabel('Y (Logarytmická osa Y)')
plt.xlabel('X')
plt.title('Graf dat 2')
plt.legend()
plt.show()

# Sdružený graf

plt.plot(x1, y1, label='Data 1')
plt.plot(x2, y2, label='Data 2')
plt.yscale('log')  
plt.xlabel('X')
plt.ylabel('Y (logarytmická osa Y)')
plt.title('Sdružený graf')
plt.legend()
plt.grid(True)
plt.show()

# Výpočet průměru pomocí numpy

prumer_numpy = (y1 + y2) / 2

# Výpočet průměru manuálně pomocí for cyklu, zápis výsledků - nevěděl jsem, ChatGPT poradil :)

prumer_manual = []
for i in range(len(y1)):
    avg = (y1[i] + y2[i]) / 2  # Výpočet průměru i-tých prvků
    prumer_manual.append(avg)  # Přidání průměru do seznamu

print("Průměry (manuální výpočet):", prumer_manual)

# Zápis výsledků

with open('prumery.md', 'w') as f:
       
    f.write('| {:^5} | {:^15} | {:^18} |\n'.format('Index', 'Prumer (numpy)', 'Prumer (manualni)')) # Zápis záhlaví tabulky s pevnou šířkou
    f.write('|{:-^7}|{:-^18}|{:-^20}|\n'.format('', '', ''))


    for i in range(len(prumer_numpy)):
        f.write('| {:^5} | {:^16.4f} | {:^18.4f} |\n'.format(i+1, prumer_numpy[i], prumer_manual[i]))  # Formátování čísel na 4 desetinná místa a pevná šířka sloupců

print("Průměry byly zapsány do souboru 'prumery.md'.")

#####################

# Vytvoření matice

matice = np.random.rand(100, 100)

prumer = np.mean(matice, axis=1)  # Průměry řádků
odchylka = np.std(matice, axis=1)     # Standardní odchylky řádků

# Vykreslení grafu

for row in matice:
    plt.plot(row, color='lightgray', linewidth=0.5, alpha=0.3) # Vykreslení hodnot řádků

plt.plot(prumer, color='blue', label='Průměr', linewidth=2) # Vykreslení průměrů řádků

plt.fill_between(range(100), prumer - odchylka, prumer + odchylka, color='red', label='Průměr ± Std') # Vykreslení průměru standardní odchylky

plt.title('Průměry a standardní odchylky řádků náhodné matice')
plt.xlabel('Index sloupce')
plt.ylabel('Hodnoty')
plt.legend()
plt.show()
