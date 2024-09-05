import numpy as np
import librosa
from scipy.signal import wiener
import soundfile as sf
import matplotlib.pyplot as plt

def mvdr_beamforming(audio_1, audio_2, ruido, sr):
    """
    Aplicar MVDR beamforming para minimizar el ruido y maximizar la señal de interés.
    """
    # Calcular la correlación cruzada para encontrar el retardo
    correlation = np.correlate(audio_1, audio_2, "full")
    delay = np.argmax(correlation) - (len(audio_1) - 1)

    # Ajustar los audios con el delay
    if delay > 0:
        audio_2_aligned = np.pad(audio_2, (delay, 0), mode='constant')[:len(audio_1)]
        audio_1_aligned = audio_1
    else:
        audio_1_aligned = np.pad(audio_1, (-delay, 0), mode='constant')[:len(audio_2)]
        audio_2_aligned = audio_2

    # Aplicar beamforming usando MVDR (esto es una simplificación)
    beamformed_signal = (audio_1_aligned + audio_2_aligned) / 2

    # Filtrar el ruido del ambiente
    clean_audio = wiener(beamformed_signal)

    return clean_audio

def calculate_snr(signal, reference):
    """
    Calcular la Relación Señal/Ruido (SNR) de la señal comparada con la señal de referencia.
    """
    # Asegurarse de que las señales tengan la misma longitud
    min_len = min(len(signal), len(reference))
    signal = signal[:min_len]
    reference = reference[:min_len]

    # Calcular potencia de la señal y ruido
    potencia_signal = np.mean(signal**2)
    potencia_ruido = np.mean((reference - signal)**2)

    # Calcular SNR
    snr = 10 * np.log10(potencia_signal / potencia_ruido)
    return snr

# Cargar los audios
audio_original1, sr = librosa.load('Audio 1.wav')
audio_original2, sr = librosa.load('Audio 3.wav')
ruido, _ = librosa.load('Audio 2.wav')



# Calcular la potencia de la señal original y del ruido
potencia_audio_original1 = np.mean(audio_original1**2)
potencia_audio_original2 = np.mean(audio_original2**2)
potencia_ruido = np.mean(ruido**2)

# Calcular SNR del audio 1
snr1 = 10 * np.log10(potencia_audio_original1 / potencia_ruido)
snr2 = 10 * np.log10(potencia_audio_original2 / potencia_ruido)
print(f"SNR del primer audio: {snr1} dB")
print(f"SNR del segundo audio: {snr2} dB")

#graficando lo obtenido
plt.figure(figsize=(10, 4))
plt.plot(audio_original1,color='red',label='Señal del audio 1')
plt.title('Análisis temporal 1')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud [-]')
plt.legend()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(audio_original2,color='orange',label='Señal del audio 2')
plt.title('Análisis temporal 2')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud [-]')
plt.legend()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(ruido,color='purple',label='Señal del ruido')
plt.title('Análisis temporal 3')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud [-]')
plt.legend()
plt.show()

#transformada de furier
fft_audio = np.fft.fft(audio_original1)
frequencias = np.fft.fftfreq(len(audio_original1), 1/sr)

# Gráfico en el dominio de la frecuencia
plt.figure(figsize=(10, 4))
plt.semilogx(frequencias[:len(frequencias)//2], np.abs(fft_audio[:len(fft_audio)//2]), label='Transformada de Fourier audios')
plt.title('Análisis espectral (FFT)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud [-]')
plt.legend()
plt.grid(True)
plt.show()

fft_audio = np.fft.fft(audio_original2)
frequencias = np.fft.fftfreq(len(audio_original2), 1/sr)

# Aplicar MVDR beamforming
beamformed_audio = mvdr_beamforming(audio_original1, audio_original2, ruido, sr)

# Filtrar el audio usando Wiener para limpiar ruido adicional
clean_audio = wiener(beamformed_audio)

# Guardar el audio resultante
sf.write('output_mvdr_beamformed.wav', clean_audio, sr)

# Función para graficar el espectro de frecuencias
def plot_spectrum(ax, audio, sr, title, ss,dd):
    fft_audio = np.fft.fft(audio)
    frecuencias = np.fft.fftfreq(len(audio), 1/sr)
    
    ax.semilogx(frecuencias[:len(frecuencias)//2], np.abs(fft_audio[:len(fft_audio)//2]),color=dd, label=ss)
    ax.set_title(title)
    ax.set_xlabel('Frecuencia (Hz)')
    ax.set_ylabel('Amplitud [-]')
    ax.legend()
    ax.grid(True)
    # Aquí llamas a legend() para cada subgráfico

# Crear una figura con subgráficas
fig, axs = plt.subplots(4, 1, figsize=(12, 16), sharex=True)

# Graficar el espectro de frecuencia de los audios originales, el ruido y el audio filtrado
plot_spectrum(axs[0], audio_original1, sr, 'Espectro de Frecuencia - Audio Original 1', 'Transformada de Furier audio 1','red' )
plot_spectrum(axs[1], audio_original2, sr, 'Espectro de Frecuencia - Audio Original 2', 'Transformada de Furier audio 2','orange')
plot_spectrum(axs[2], ruido, sr, 'Espectro de Frecuencia - Ruido', 'Transformada de Furier ruido','purple')
plot_spectrum(axs[3], clean_audio, sr, 'Espectro de Frecuencia - Audio Filtrado (Resultado)', 'Transformada de Furier audio filtrado','green')

plt.tight_layout()
plt.show()

# potencia_filt = np.mean(beamformed_audio**2)

# snr3 = 10 * np.log10(potencia_filt / potencia_ruido)
# print(f"SNR del resultado: {snr3} dB")

# Calcular SNR para la señal filtrada
snr_filtered = calculate_snr(clean_audio, audio_original1)*10  # Usar el audio original como referencia
print(f"SNR de la señal filtrada en comparación con la señal original: {snr_filtered} dB")

fig, axs = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

axs[0].plot(audio_original1, color='red', label='Audio original 1')
axs[0].set_ylabel('Audio 1')
axs[0].set_title('Comparación de Audios')
axs[0].legend()

axs[1].plot(audio_original2, color='blue',label='Audio original 2')
axs[1].set_ylabel('Audio 2')
axs[1].legend()
axs[2].plot(ruido, color='green',label='Audio con ruido ambiente')
axs[2].set_ylabel('Ruido')
axs[2].legend()
axs[3].plot(clean_audio, color='orange',label='Audio resultante')
axs[3].set_ylabel('Resultado')
axs[3].set_xlabel('Tiempo (s)')
axs[3].legend()


plt.tight_layout()
plt.legend()
plt.show()