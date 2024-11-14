"""
Velmi pekne, dekuji.
Ten subplot je velmi pekny.

Co se poznamek a tipu tyce, vetsinu jsem shrnul v uloze s numerickou integraci, odkazuji Vas proto tam.
Ohledne kvadraticke odchylky - lze to vylepsit tak, ze rozdil mezi daty a predikci polynomu pred umoznenim podelite napriklad maximalni hodnotou nebo prumerem z dostupnych dat. Timto normovanim zajistite, ze kvadraticka odchylka 
bude mit rozumne hodnoty.

Zaroven doplnuji k subplotu, ze existuje moznost mit sdilene osy. Tzn. mate-li vedle sebe nekolik obrazku, ma-li kazdy stejne hodnoty na ose x a ose y, lze hodnoty a popisky os zobrazit pouze u krajnich obrazkuch - za se tim usetrit trochu mista.

"""

import numpy as np
import matplotlib.pyplot as plt

# Linearni krivka
#x = [-1, -0.5, 0, 0.5, 1]
#y = [-1.6781, 0.3151, 1.1051, 1.9512, 2.5884]

# Kvadraticka krivka
#x = [-1, -0.5, 0, 0.5, 1]
#y = [3, 4, 7, 18, 30]

# Obecna data
#rok = [1960:1:2021]
#Ethiopia = [22151284,22671193,23221385,23798418,24397010,25013634,25641040,26280135,26944386,27652715,28415080,29248650,30140799,31036670,31861353,32566855,33128151,33577240,33993301,34487806,35141703,35984531,36995246,38142679,39374346,40652146,41965696,43329238,44757205,46272308,47887864,49609976,51423591,53295556,55180993,57047906,58883531,60697443,62507724,64343008,66224809,68159422,70142090,72170581,74239508,76346310,78489205,80674343,82916236,85233923,87639962,90139928,92726982,95385793,98094264,100835453,103603461,106399926,109224410,112078727,114963583,117876226]



#Vytvořte funkci, která provede aproximaci zadaných dat polynomem N-tého stupně. 

# Ověřte na lineárnim polynomu

# Ověřte na kvadratickém polynomu

# Ověřte na obecných datech a obecném polynomu

# Porovnejte aproximaci pomocí polynomů 4, 5, 6 řádu (či exp. funkce)

# Zobrazte kvadratickou odchylku a prozkoumejte její velikost


## Lineární polynom

x = [-1, -0.5, 0, 0.5, 1]
y = [-1.6781, 0.3151, 1.1051, 1.9512, 2.5884]
stupne = [1]


# Funkce pro aproximaci pomocí polynomu stupně N
def poly_approximation(x, y, stupen):
    # Vypočítá koeficienty polynomu
    koeficient = np.polyfit(x, y, stupen)
    # Vytvoří polynomickou funkci na základě koeficientů
    poly_funkce = np.poly1d(koeficient)
    return poly_funkce

# Funkce pro výpočet kvadratické odchylky
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


# Vykreslení aproximací
plt.figure(figsize=(8, 6))
for i, stupen in enumerate(stupne, 1):
    # Aproximace
    poly_func = poly_approximation(x, y, stupen)
    y_approx = poly_func(x)
    
    # Výpočet kvadratické odchylky
    kvadraticka_odchylka = mean_squared_error(y, y_approx)
    print(f"{stupen}.Stupeň  - Kvadratická odchylka: {kvadraticka_odchylka}")
    
    # Vykreslení původních dat a aproximace
    plt.plot(x, y, 'o', label='Původní data', markersize=3)
    plt.plot(x, y_approx, label=f'Aproximace polyn. {stupen}. stupně')
    plt.title(f'Polynom {stupen}. stupně\nKvadratická odchylka = {kvadraticka_odchylka:.2f}')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
plt.show()

## Kvadratický polynom

x = [-1, -0.5, 0, 0.5, 1]
y = [3, 4, 7, 18, 30]
stupne = [1, 2]


def poly_approximation(x, y, stupne):
    koeficient = np.polyfit(x, y, stupne)
    poly_func = np.poly1d(koeficient)
    return poly_func

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


plt.figure(figsize=(12, 6))
for i, stupne in enumerate(stupne, 1):
   
    poly_func = poly_approximation(x, y, stupne)
    y_approx = poly_func(x)
    
    
    kvadraticka_odchylka = mean_squared_error(y, y_approx)
    print(f"{stupne}.Stupeň  - Kvadratická odchylka: {kvadraticka_odchylka}")
    
   
    plt.subplot(1, 2, i)
    plt.plot(x, y, 'o', label='Původní data', markersize=3)
    plt.plot(x, y_approx, label=f'Aproximace polyn. {stupne}. stupně')
    plt.title(f'Polynom {stupne}. stupně\nKvadratická odchylka = {kvadraticka_odchylka:.2f}')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
plt.tight_layout()
plt.show()

## Obecná data, vyšší řád polynomu

rok = np.arange(1960,2022,1)  #[1960:1:2021]
Ethiopia = [22151284,22671193,23221385,23798418,24397010,25013634,25641040,26280135,26944386,27652715,28415080,29248650,30140799,31036670,31861353,32566855,33128151,33577240,33993301,34487806,35141703,35984531,36995246,38142679,39374346,40652146,41965696,43329238,44757205,46272308,47887864,49609976,51423591,53295556,55180993,57047906,58883531,60697443,62507724,64343008,66224809,68159422,70142090,72170581,74239508,76346310,78489205,80674343,82916236,85233923,87639962,90139928,92726982,95385793,98094264,100835453,103603461,106399926,109224410,112078727,114963583,117876226]
stupne = [1, 2, 4, 5, 6, 12]


def poly_approximation(rok, Ethiopia, stupen):
    koeficient = np.polyfit(rok, Ethiopia, stupen)
    poly_func = np.poly1d(koeficient)
    return poly_func

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


plt.figure(figsize=(12, 8))
for i, stupen in enumerate(stupne, 1):
   
    poly_func = poly_approximation(rok, Ethiopia, stupen)
    y_approx = poly_func(rok)
    
  
    kvadraticka_odchylka = mean_squared_error(Ethiopia, y_approx)
    print(f"{stupen}.Stupeň  - Kvadratická odchylka: {kvadraticka_odchylka}")
    

    plt.subplot(2, 3, i)
    plt.plot(rok, Ethiopia, 'o', label='Původní data', markersize=3)
    plt.plot(rok, y_approx, label=f'Aproximace polyn. {stupen}. stupně')
    plt.title(f'Polynom {stupen}. stupně\nKvadratická odchylka = {kvadraticka_odchylka:.2f}')
    plt.xlabel("Rok")
    plt.ylabel("Počet obyvatel Ethiopie")
    plt.legend()
plt.tight_layout()
plt.show()

# Do polynomu 5. stupně se odchylka snižuje zhruba o polovinu, poté zůstává v podstatě stejná..
# Nemám tušení proč mi vyšla kvadratická odchylka pro Ethiopii takhle vysoká..
