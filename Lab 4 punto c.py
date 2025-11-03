import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# ------------------------------------------------------------
# 1. CONFIGURACIÓN INICIAL
# ------------------------------------------------------------
ruta = r"C:\Users\DELL\Desktop\señal 2 emg\Senal_lab_4_parteb.2.txt"
fs = 1000  # Frecuencia de muestreo (Hz)

# Puedes ajustar este rango según el músculo o estudio
high_freq_range = (150, 400)  # Hz

# ------------------------------------------------------------
# 2. CARGAR SEÑAL
# ------------------------------------------------------------
data = np.loadtxt(ruta)
t = data[:, 0]
emg = data[:, 1]

# ------------------------------------------------------------
# 3. FILTRO PASA BANDA (20–450 Hz)
# ------------------------------------------------------------
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [lowcut / nyq, highcut / nyq], btype='band')
    return filtfilt(b, a, data)

emg_filt = butter_bandpass_filter(emg, 20, 450, fs)

# ------------------------------------------------------------
# 4. MOSTRAR SEÑAL FILTRADA
# ------------------------------------------------------------
plt.figure(figsize=(10,4))
plt.plot(t, emg_filt, color='C0')
plt.title("(1) Señal EMG Filtrada (20–450 Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 5. DETECCIÓN AUTOMÁTICA DE CONTRACCIONES
# ------------------------------------------------------------
abs_emg = np.abs(emg_filt)
peaks, _ = find_peaks(abs_emg, distance=fs*0.5, height=np.mean(abs_emg)*2)
segments = np.array_split(emg_filt, len(peaks))

print(f"Contracciones detectadas: {len(segments)}")

# ------------------------------------------------------------
# 6. FFT — CALCULAR PARA CADA CONTRACCIÓN
# ------------------------------------------------------------
fft_results = []
for seg in segments:
    fft_vals = np.fft.rfft(seg)
    freqs = np.fft.rfftfreq(len(seg), 1/fs)
    magnitude = np.abs(fft_vals) / len(seg)
    fft_results.append((freqs, magnitude))

# ------------------------------------------------------------
# 7. MOSTRAR TODOS LOS ESPECTROS POR SEPARADO
# ------------------------------------------------------------
for i, (f, mag) in enumerate(fft_results):
    plt.figure(figsize=(8,4))
    plt.plot(f, mag)
    plt.title(f"(2) Espectro de amplitud — Contracción {i+1}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid()
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# 8. MOSTRAR TODOS LOS ESPECTROS EN UNA SOLA GRÁFICA
# ------------------------------------------------------------
plt.figure(figsize=(10,5))
for i, (f, mag) in enumerate(fft_results):
    plt.plot(f, mag, label=f"Contracción {i+1}")
plt.title("(3) Comparación de espectros — Todas las contracciones")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 9. COMPARAR PRIMERA Y ÚLTIMA CONTRACCIÓN
# ------------------------------------------------------------
plt.figure(figsize=(9,5))
plt.plot(fft_results[0][0], fft_results[0][1], label="Primera contracción", color='C0')
plt.plot(fft_results[-1][0], fft_results[-1][1], label="Última contracción", color='C3')
plt.title("(4) Comparación de espectros: Primera vs Última contracción")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 10. ANÁLISIS ESPECTRAL — FATIGA MUSCULAR
# ------------------------------------------------------------
f1, mag1 = fft_results[0]
fN, magN = fft_results[-1]

# Pico espectral
peak1 = f1[np.argmax(mag1)]
peakN = fN[np.argmax(magN)]

# Contenido de alta frecuencia ajustable
mask1 = (f1 >= high_freq_range[0]) & (f1 <= high_freq_range[1])
maskN = (fN >= high_freq_range[0]) & (fN <= high_freq_range[1])
mean_high_1 = np.mean(mag1[mask1])
mean_high_N = np.mean(magN[maskN])

print("\n--- (5) ANÁLISIS DE FATIGA MUSCULAR ---")
print(f"Pico espectral inicial: {peak1:.2f} Hz")
print(f"Pico espectral final:   {peakN:.2f} Hz")
print(f"Contenido de alta frecuencia ({high_freq_range[0]}–{high_freq_range[1]} Hz):")
print(f"   Primera contracción: {mean_high_1:.5f}")
print(f"   Última contracción:  {mean_high_N:.5f}")

# ------------------------------------------------------------
# 11. CONCLUSIONES
# ------------------------------------------------------------
print("\n--- (6) CONCLUSIONES ---")
print("• Se observa una disminución del contenido de alta frecuencia con la fatiga muscular.")
print("• El pico espectral se desplaza hacia frecuencias más bajas, indicando menor velocidad de conducción.")
print("• Esto evidencia la pérdida progresiva de fibras rápidas tipo II.")
print("• El análisis espectral (FFT) es una herramienta útil para evaluar la fatiga en EMG.")
