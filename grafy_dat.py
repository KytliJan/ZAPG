"""
Opet velmi pekne. Diky. Velke plus mate opet za to, ze kod je prehledne strukturovay a citelny a zapis konzistentni.
Opek doplnuji par poznamek (nektere jsou tentokrat vsak na vrub mne, nebot jsem zadani neformuloval uplne jasne).
"""
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

"""
Grafy jsou pekne. Pripominam plt.rcParams, ktere jsem znimoval posledne.
(Pripravte se na to, ze celou vasi stuijni praxi Vas bude nekdo peskovat, ze mate male popisky u obrazku. Pripadne pokud neco
publikujete, jedna se o oblibenou stiznost editora. :-) )
"""

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

"""
Pokud pracujeme s velkym mnozstvim cisel, append neni uplne vhodny. Lepsi je inicializovat si pole o potrebne velikosti
(treba pres np.ones, np.zeros ) a nebo zkratka python list pomoci [ 1/0/None,...  ] * size ci pomoci range(size) a potom
upravoat jednotlive pozice.

Append totiz pri kazdem zavolani zvetsuje pole o jedna - coz vyzaduje realokaci, ktera obvykle vypada tak ze cely blok pameti
se musi naalokovat nekde jinde (pocitac si totiz pole ulozi zrovna tam, kde ma nejaky kus volne pamtice a neni garantovano, ze mam-li
pole o N prvnich, N+1 blok pameti je stale jeste volny), data presunout - a to se deje v kazdem kroku. Pokud nemame prvku
prilis mnoho tak to obvykle neni takovy problem, ale pro dlouha pole uz jde o signifikantni zdrzeni.

Zkuste si vygenerovat vektory y1 a y2 o ruznych velikostech (100000/1000000/10000000) prvku (treba jako nahodne vektory)
a zkuste zmerit, jak dlouho kod pobezi, pouzijete-li append a jak dlouho pouzijete-li predalokovane pole.

Priste mi, prosim, kdyztak pripomente, abych k tomu dal kratky komentar.
"""

# Výpočet průměru manuálně pomocí for cyklu, zápis výsledků - nevěděl jsem, ChatGPT poradil :)

prumer_manual = []
for i in range(len(y1)):
    avg = (y1[i] + y2[i]) / 2  # Výpočet průměru i-tých prvků
    prumer_manual.append(avg)  # Přidání průměru do seznamu

print("Průměry (manuální výpočet):", prumer_manual)

# Zápis výsledků
"""
Na temto miste se omlouvam, ze jsem Vas ponekud zmatl. Myslenkou bylo vytvorit prumer z prvniho sloupce (jedno cislo) a prumer
druheho sloupce (druhe cislo) - jsem si vedom, ze to v zadani bylo napsano vice nez neobratne.

V takovem pripade (dve cisla) ma smysl zabyvat se zapisem do nejakeho lepsiho formatu - tabulka/markdown, ktery vyuzijeme
nekde jinde/dal. Na zapis "nesmyslneho" mnozstvi dat neni ani jeden z formatu delany a data lze ulozit do obycejneho textoveho
souboru (klidne bez koncovky).

K vypoctu prumeru:
int sum_data = 0
for i in range( 0, len( data ) ): # alternativne: for d in data:
    sum_data += data[ i ]         # alternativne:    sum_data += d

avg = sum_data / len( data )

Chvalim, ze mate pekne udelany formatovnay vystup.
Jeste pohodlnejsi variantou jsou tzv. formatovane stirngy (viz poznamky k cv1)
print( f'V teto kazce jsme vypsali cislo promenna s hodnotou {promenna:.f2} na dve desetinna mista.' )
"""

with open('prumery.md', 'w') as f:
       
    f.write('| {:^5} | {:^15} | {:^18} |\n'.format('Index', 'Prumer (numpy)', 'Prumer (manualni)')) # Zápis záhlaví tabulky s pevnou šířkou
    f.write('|{:-^7}|{:-^18}|{:-^20}|\n'.format('', '', ''))


    for i in range(len(prumer_numpy)):
        f.write('| {:^5} | {:^16.4f} | {:^18.4f} |\n'.format(i+1, prumer_numpy[i], prumer_manual[i]))  # Formátování čísel na 4 desetinná místa a pevná šířka sloupců

print("Průměry byly zapsány do souboru 'prumery.md'.")

#####################

# Vytvoření matice

matice = np.random.rand(100, 100)

"""
Pekne. A chvalim za axis.
"""
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
