import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd

# --- 1. Cargar la señal ---
signal = np.loadtxt(r'C:\Users\danil\Downloads\EMG1.txt')


# --- 2. Graficar la señal ---
fs = 1000  # frecuencia de muestreo en Hz
dt = 1 / fs  # intervalo entre muestras en segundos
t = np.arange(len(signal)) * dt


plt.figure(figsize=(10,4))
plt.plot(t, signal, color='blue')
plt.title("Señal EMG ideal")
plt.xlabel("Tiempo [S]")
plt.grid(True)
plt.show()

# --- 3. Segmentar señal en torno a cada contracción ---
# Duración de cada ventana
fs = int(len(t) / (t[-1] - t[0]))
pre = int(0.05 * fs)
post = int(0.15 * fs)

segments = []
time_segments = []

peaks, properties = find_peaks(signal, height=0.5, distance=100)

# === SEGMENTACIÓN ===
duracion_contraccion = 0.1
fs = 1 / (t[1] - t[0])
ventana_muestras = int(duracion_contraccion * fs / 2)  # mitad antes y mitad después

frecuencias_medias = []
frecuencias_medianas = []

# === GRAFICADO DE CADA CONTRACCIÓN ===
for i, p in enumerate(peaks[:5]):  # solo las primeras 5 contracciones
    inicio = max(0, p - ventana_muestras)
    fin = min(len(signal), p + ventana_muestras)
    t_segmento = t[inicio:fin]
    emg_segmento = signal[inicio:fin]
    
    # --- Eliminar componente DC ---
    emg_segmento = emg_segmento - np.mean(emg_segmento)
    
    # FFT
    N = len(emg_segmento)
    freqs = np.fft.rfftfreq(N, d=1/fs)
    fft_vals = np.fft.rfft(emg_segmento)
    potencia = np.abs(fft_vals)**2

    # Frecuencia media
    f_mean = np.sum(freqs * potencia) / np.sum(potencia)
    
    # Frecuencia mediana
    cumsum = np.cumsum(potencia)
    f_median = freqs[np.where(cumsum >= cumsum[-1] / 2)[0][0]]
    
    frecuencias_medias.append(f_mean)
    frecuencias_medianas.append(f_median)
    
    plt.figure(figsize=(6, 3))
    plt.plot(t_segmento, emg_segmento, color='blue')
    plt.title(f'Contracción {i+1}')
    plt.xlabel('Tiempo [s]')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# === RESULTADOS ===
for i in range(5):
    print(f"Contracción {i+1}: f_media = {frecuencias_medias[i]:.2f} Hz, f_mediana = {frecuencias_medianas[i]:.2f} Hz")

# === TABLA DE RESULTADOS ===
resultados = pd.DataFrame({
    'Contracción': np.arange(1, 6),
    'Frecuencia Media [Hz]': frecuencias_medias,
    'Frecuencia Mediana [Hz]': frecuencias_medianas
})


print("\n=== Resultados de las contracciones ===")
print(resultados.to_string(index=False))

# === GRÁFICA DE EVOLUCIÓN ===
plt.figure(figsize=(7, 4))
plt.plot(resultados['Contracción'], resultados['Frecuencia Media [Hz]'], 
         marker='o', linestyle='-', label='Frecuencia Media', color='tab:blue')
plt.plot(resultados['Contracción'], resultados['Frecuencia Mediana [Hz]'], 
         marker='s', linestyle='--', label='Frecuencia Mediana', color='tab:orange')

plt.title('Evolución de las Frecuencias por Contracción')
plt.xlabel('# de contracción')
plt.ylabel('Frecuencia [Hz]')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
