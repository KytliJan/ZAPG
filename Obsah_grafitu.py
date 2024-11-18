import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

#kontrola správné cesty, plt.imread mi nefungovala?
print(os.path.exists('C:/Users/Peťas/Documents/GitHub/ZAPG//obsah_grafitu.png'))

#puvodni_obrazek= plt.imread('C:/Users/Peťas/Documents/GitHub/ZAPG//obsah_grafitu.png')
puvodni_obrazek = np.array(Image.open('C:/Users/Peťas/Documents/GitHub/ZAPG//obsah_grafitu.png'))


print(f"Výška, šířka, počet barevných kanálů původního obrázku:{puvodni_obrazek.shape}")

plt.title("Původní obrázek")
plt.imshow(puvodni_obrazek)
plt.axis('off')
plt.show()

if len(puvodni_obrazek.shape) == 3: 
    puvodni_obrazek = np.mean(puvodni_obrazek, axis=2)

plt.title("Původní obrázek černobíle")
plt.imshow(puvodni_obrazek, cmap='gray')
plt.axis('off')
plt.show()
# Histogram intenzit pixelů- čím nižší hodnota, tím tmavší

plt.figure(figsize=(8, 6))
plt.title("Histogram intenzit pixelů")
plt.hist(puvodni_obrazek.ravel(), bins=256, color='gray')
plt.xlabel("Intenzita")
plt.ylabel("Počet pixelů")
plt.show()

# Definice prahové hodnoty pro oddělení grafitu- zvolíme buď experimentálně nebo podle histogramu (dokud se nezačnou zobrazovat hranice zrn)
threshold = 150

# Prahování obrázku
binarni_obrazek_pozadovany = puvodni_obrazek > threshold  

# Výpočet procentuálního podílu grafitu v závislosti na def. hodnotě
pixely_celkem = binarni_obrazek_pozadovany.size
pixely_zeleza = np.sum(binarni_obrazek_pozadovany)
procento_zeleza = (pixely_zeleza / pixely_celkem) * 100
procento_uhliku = (100 - procento_zeleza)

print(f"pixely celkem: {pixely_celkem:.2f}" )
print(f"pixely železa: {pixely_zeleza:.2f}" )
print(f"Procentuální podíl uhlíku: {procento_uhliku:.2f}%")

plt.title("Binární obrázek (černé oblasti = grafit)")
plt.imshow(binarni_obrazek_pozadovany, cmap='gray')
plt.axis('off')
plt.show()

#binarni_obrazek_invertovany = 255 - binarni_obrazek_pozadovany
#plt.title("Binární obrázek invertovaný")
#plt.imshow(binarni_obrazek_invertovany, cmap='gray')
#plt.axis('off')
#plt.show()


