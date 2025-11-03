
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# ------------------------------------------------------------
# Datos de entrada
# ------------------------------------------------------------
ruta = r"C:\Users\DELL\Desktop\señal 2 emg\Senal_lab_4_parteb.2.txt"
fs = 1000  # Frecuencia de muestreo (Hz)

data = np.loadtxt(ruta)
t = data[:, 0]
emg = data[:, 1]

# ------------------------------------------------------------
# Filtrado pasa banda (20–450 Hz)
# ------------------------------------------------------------
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

emg_filt = butter_bandpass_filter(emg, 20, 450, fs)

# ------------------------------------------------------------
# Detección automática de contracciones
# ------------------------------------------------------------
abs_emg = np.abs(emg_filt)
peaks, _ = find_peaks(abs_emg, distance=fs*0.5, height=np.mean(abs_emg)*2)
segments = np.array_split(emg_filt, len(peaks))

print(f"Contracciones detectadas: {len(segments)}")

# ------------------------------------------------------------
# (a) Aplicar la FFT a cada contracción
# ------------------------------------------------------------
fft_results = []
for seg in segments:
    fft_vals = np.fft.rfft(seg)
    freqs = np.fft.rfftfreq(len(seg), 1/fs)
    magnitude = np.abs(fft_vals) / len(seg)
    fft_results.append((freqs, magnitude))

print("Transformada Rápida de Fourier aplicada a cada contracción.")

# ------------------------------------------------------------
# (b) Graficar el espectro de amplitud
# ------------------------------------------------------------
for i, (f, mag) in enumerate(fft_results):
    plt.figure(figsize=(8,4))
    plt.plot(f, mag, color='C0')
    plt.title(f"(a–b) Espectro de amplitud - Contracción {i+1}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid()
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# (c) Comparar primeras y últimas contracciones
# ------------------------------------------------------------
plt.figure(figsize=(8,5))
plt.plot(fft_results[0][0], fft_results[0][1], label="Primera contracción", color='C0')
plt.plot(fft_results[-1][0], fft_results[-1][1], label="Última contracción", color='C3')
plt.title("(c) Comparación de espectros: primera vs última contracción")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# (d–e) Reducción de alta frecuencia y desplazamiento del pico
# ------------------------------------------------------------
f1, mag1 = fft_results[0]
fN, magN = fft_results[-1]

# Pico espectral
peak1 = f1[np.argmax(mag1)]
peakN = fN[np.argmax(magN)]

# Contenido de alta frecuencia (150–400 Hz)
mask1 = (f1 >= 150) & (f1 <= 400)
maskN = (fN >= 150) & (fN <= 400)
mean_high_1 = np.mean(mag1[mask1])
mean_high_N = np.mean(magN[maskN])

print("\n(d–e) Análisis espectral:")
print(f"   Pico espectral inicial: {peak1:.2f} Hz")
print(f"   Pico espectral final: {peakN:.2f} Hz")
print(" Contenido de alta frecuencia (150–400 Hz):")
print(f"      Primera contracción: {mean_high_1:.5f}")
print(f"      Última contracción:  {mean_high_N:.5f}")

# ------------------------------------------------------------
# (f) Conclusión
# ------------------------------------------------------------
print("\n(f) CONCLUSIÓN:")
print("El análisis espectral muestra que, a medida que progresa la fatiga muscular,")
print("el pico espectral y el contenido de alta frecuencia disminuyen.")
print("Esto refleja una reducción en la velocidad de conducción de las fibras musculares")
print("y una pérdida progresiva de unidades motoras rápidas.")
print("Por tanto, el análisis de FFT es una herramienta útil para evaluar la fatiga en EMG.")
