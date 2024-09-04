# Laboratorio 2 Procesamiento  Digital de Señales: Problema del coctel 
Autores: Fabián Alberto López Lemus y Tania Angélica Sandoval Ramírez
## Introducción
El propósito del presente laboratorio es aplicar el análisis en frecuencia de señales de voz en un problema de captura de señales mezcladas. Esto con el fin de resolver el problema del cóctel, este hace referencia a la separación de una fuente de sonido específica en un entorno donde múltiples fuentes están presentes. Este fenómeno es típico en situaciones como una fiesta o un cóctel, donde varias personas hablan simultáneamente y se desea enfocar la atención en una sola conversación.<br>
<br>
La solución al problema implicó el uso de técnicas como beamforming, y separación de fuentes. Estos métodos permiten mejorar la calidad de la señal de interés (la voz objetivo) mientras se atenúan las demás fuentes de ruido;para la obtención de las señales; se hizo uso de una interfaz de audio, la cual permitió tomar 2 señales al tiempo(micrófonos), garantizando la frecuencia de muestreo de los 2 y se hizo el mismo procedimiento con el ruido ambiente .<br>
<br>
Para cumplir con todos los objetivos se utilizó el lenguaje de programación Python, en el cual se realizó la importación, muestra y tratamiento de los datos mencionados anteriormente(**para terceros se recomienda usar el software "Anaconda Navigator con su herramienta "Spider"**), al final de este repositorio se encontrarán las instrucciones para poder usar el código de manera adecuada.

## Procedimiento 
### Primera parte
En este laboratorio, se utilizó una interfaz, como se muestra en la imagen, con dos micrófonos situados en diferentes partes de un salón. Estos micrófonos capturaron las señales de audio mientras Fabian y Tania hablaban simultáneamente, simulando el problema conocido como efecto cóctel. Las señales de audio fueron grabadas utilizando la aplicación Audacity, y posteriormente se descargaron tres archivos de audio (ruido, audio del primer micrófono y audio del segundo micrófono) en formato WAV.<br>

<img src="https://github.com/user-attachments/assets/2f53232e-810a-4017-bbd7-aece4d0d962c" alt="Descripción de la imagen" width="600"/>

### Segunda parte

Se van cargan los tres archivos de audio, en donde ("Audio 1.wav" y "Audio 3.wav") son los audios de las dos personas hablando y el ("Audio 3.wav") es el audio del ruido. Aquí estamos abriendo tres archivos de audio usando la librería librosa para el análisis y procesamiento de audio:

```python
audio_original1, sr = librosa.load('Audio 1.wav')
audio_original2, sr = librosa.load('Audio 3.wav')
ruido, _ = librosa.load('Audio 2.wav')
```

También se va a ajusta el volumen de cada archivo de audio para que todos estén en un rango similar para que sus valores estén entre -1 y 1:

```python
audio_original1 = audio_original1 / np.max(np.abs(audio_original1))
audio_original2 = audio_original2 / np.max(np.abs(audio_original2))
ruido = ruido / np.max(np.abs(ruido))
```
Se realizó el cálculo del SNR (Relación Señal-Ruido) para evaluar la calidad de la señal después de aplicar el procesamiento de audio, comparándola con la señal de ruido. Un SNR más alto indica una señal más clara en relación con el ruido. En nuestro caso, el SNR del primer audio es de **17.16 dB**, lo que sugiere una buena relación señal-ruido. El SNR del segundo audio es de **22.50 dB**, que indica una relación aún mejor, sugiriendo que el segundo audio es más claro. La señal filtrada tiene un SNR de **11.54 dB** en comparación con la señal original, lo que indica que el procesamiento mejoró la relación señal-ruido en comparación con el estado inicial. Estos valores muestran que el procesamiento ha sido efectivo, mejorando la claridad del audio, aunque aún hay margen para mejorar el SNR.<br>
Para ver cómo cambia la amplitud de la señal de audio a medida que pasa el tiempo, se realizó la gráfica del análisis. Esto ayuda a visualizar el contenido del audio, como los picos que podrían representar palabras o sonidos importantes.

# Instrucciones para el usuario 
Para evitar problemas se le recomienda al usuario usar la versión 3.10 de Python y no modificar nada de lo que no se menciona en los siguientes pasos, ya que el código generará las demás cosas de manera automática. Además, se recomienda usar solo 2 microfonos con una sola interfaz, ya que así se duplicarían los factores de la experimentación y se evitan errores.
1. Realizar la grabación de la fiesta o del entorno con varias voces, asegurándose que el archivo de audio sea del formato .wav y que se haya grabado el ruido ambiente con la misma duración de los audios(puede ser después de los audios), todo con los mismos instrumentos, las mismas configuraciones y en la misma posición.
2. Importar las siguientes librerías luego de instalarlas previamente, para instalar usar en la consola el siguiente comando: “pip install ‘nombre de la libreria’”
   
```python
import numpy as np
import librosa
from scipy.signal import wiener
import soundfile as sf
import matplotlib.pyplot as plt

```
3. Cargar los datos tomados anteriormente de la siguiente forma (línea 49, 50 y 15 del código)
```python
audio_original1, sr = librosa.load('nombre del archivo de audio 1(micrófono 1).wav')
audio_original2, sr = librosa.load('nombre del archivo de audio 1(micrófono 2).wav')
ruido, _ = librosa.load('nombre del archivo de audio del ruido.wav’)
```
4. Una vez realizado este procedimiento, el programa generará el SNR de ambos audios con respecto al ruido, para esto, si el SNR da menor de 10 probablemente se tenga que regrabar los audios(se recomienda hacer una prueba previa y de ser posible grabar el ruido ambiente al terminar ya que tiene que ser del mismo tiempo que las otras muestras).
5. El programa generará automáticamente las gráficas de los audios obtenidos y posteriormente hará la transformada de fourier y también mostrará la gráfica de este.
6. Si todo funcionó correctamente, podrá observar un SNR mayor a 10 en el audio filtrado y obtendrá las 4 gráficas en función de la frecuencia de: el audio 1, audio 2, ruido y audio filtrado.
### Uso 
Por favor, cite este artículo:
<br>
Lopez L., Sandoval R. (2024). Github 'Laboratorio 1 Procesamiento de señales'[Online].
### Informacion de contacto
est.fabiana.lopez@unimilitar.edu.co
<br>
est.tania.sandoval@unimilitar.edu.co







