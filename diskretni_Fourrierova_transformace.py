import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

nahravka = wavfile.read('C:/Users\Peťas\Documents\GitHub\ZAPG/a-dur.wav')
fs, data = nahravka


print(f"Vzorkovací frekvence: {fs} Hz")
print(f"Počet vzorků: {len(data)}")
print(f"Tvar dat: {data.shape}")
plt.figure(figsize=(10, 4))
plt.plot(np.linspace(0, len(data) / fs, num=len(data)), data, color='blue')
plt.title("Časový průběh signálu")
plt.xlabel("Čas [s]")
plt.ylabel("Amplituda")
plt.show()

# Fourierova transformace
N = len(data)
yf = fft(data)
xf = fftfreq(N, 1 / fs)[:N // 2]
amplituda = np.abs(yf[:N // 2])


plt.figure(figsize=(10, 4))
plt.plot(xf, amplituda, color='red')
plt.title("Frekvenční spektrum signálu")
plt.xlabel("Frekvence [Hz]")
plt.ylabel("Amplituda")
plt.grid()
plt.show()

# Výrazné frekvence z grafu: 334 Hz,448 Hz, 668-678 Hz, 167, 225, 501, 850 Hz
#nota C# s frekencí 554.365 Hz
#nota A s frekvencí 440 Hz
#nota E s frekvencí 329.628 Hz

# Největší je křivka pro 334 Hz a 448 Hz, tudíž A a E jsou mírně vychýlené, ale nikdo by to nepoznal :)
# Při 554 Hz máme náznak křivky, ale ve velmi nízkém zastoupení
# Frekvence 668 Hz je nejblíže E5, což je 659,25 Hz? Bohužel nejsem hudebník, takže nevím co z toho vyvodit..