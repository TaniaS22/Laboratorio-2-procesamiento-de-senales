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
En este laboratorio, se utilizó una interfaz, como se muestra en la imagen, con dos micrófonos situados en diferentes partes de un salón (distanciados entre sí a 3,5m, el primer micrófono estaba a una distancia 1,5m del suelo y el segundo estaba a 80cm). Estos micrófonos capturaron las señales de audio en 20 segundos mientras Fabián y Tania hablaban simultáneamente (el primer micrófono estaba a una distancia de 1,5m de Fabián y Tania, mientras que el segundo micrófono estaba a una distancia de 4m y los dos estaban ubicados en orientación donde Tania y Fabián hablaban), simulando el problema conocido como efecto cóctel. Las señales de audio fueron grabadas utilizando la aplicación Audacity, y posteriormente se descargaron tres archivos de audio (ruido, audio del primer micrófono y audio del segundo micrófono) en formato WAV. El audio fue grabado a una frecuencia de muestreo (sample rate, sr) definida al cargar los archivos de audio. En este caso, se utiliza una frecuencia de muestreo típica, alrededor de 44.1 kHz, que significa que se capturan 44,100 muestras por segundo y como se grabaron 20 segundos, se capturaron alrededor de 882000 muestras por cada señal. <br>

<img src="https://github.com/user-attachments/assets/2f53232e-810a-4017-bbd7-aece4d0d962c" alt="Descripción de la imagen" width="600"/>

### Segunda parte

Se van cargan los tres archivos de audio, en donde ("Audio 1.wav" y "Audio 3.wav") son los audios de las dos personas hablando y el ("Audio 3.wav") es el audio del ruido, con ayuda de una librería llamada librosa. Para evaluar las señales, primero se realiza un análisis en el dominio del tiempo, donde se observa cómo varía la amplitud de las señales a lo largo del tiempo. Este análisis se realiza visualizando las gráficas como se muestra a continuación:

```python
plt.plot(nombre del audio, label='La señal del audio')
```

![image](https://github.com/user-attachments/assets/c1901d37-7eae-4dcb-aef3-0aa3f527bea0)

Los dos primeros gráficos muestran las formas de onda de las señales capturadas por los dos micrófonos en el dominio del tiempo. El eje horizontal representa el tiempo, mientras que el eje vertical representa la amplitud de la señal. La amplitud representa las variaciones del sonido que capturaron los micrófonos. Se puede ver que las formas de onda son bastante ruidosas, lo cual refleja la presencia de ruido de fondo y las señales de voz de Tania y Fabián.La diferencia en las formas de onda entre los dos audios se debe a la ubicación diferente de los micrófonos. El tercer gráfico muestra la señal de ruido capturada por un micrófono. En comparación con los dos primeros audios, la amplitud del ruido es mucho menor pero constante. Y en el cuarto gráfico se muestra la señal después de aplicar las técnicas de beamforming MVDR y filtrado Wiener que veremos más adelante. Esta señal muestra mayormente la voz de Fabián, habiendo reducido la voz de Tania. Comparando este gráfico con los originales, se puede ver que la señal resultante tiene una forma más definida, lo que indica que el ruido ha sido filtrado.

### Tercera parte
Se utiliza la Transformada Rápida de Fourier (FFT) para transformar la señal del dominio temporal al dominio de la frecuencia, lo cual permite identificar qué componentes de frecuencia están presentes en la señal. Las gráficas espectrales muestran la amplitud de cada frecuencia, mostrando patrones importantes como las frecuencias dominantes.

```python
fft_audio = np.fft.fft(audio)
frequencias = np.fft.fftfreq(len(audio), 1/sr)
plt.semilogx(frecuencias[:len(frecuencias)//2], np.abs(fft_audio[:len(fft_audio)//2]))
```
Mostrando la siguiente gráfica:

![image](https://github.com/user-attachments/assets/214ba98f-ca36-4179-962d-39f2c44a7e4c)

Este gráfico muestra cómo la señal del Audio Original 1 se distribuye en el dominio de la frecuencia. En el eje horizontal tenemos la frecuencia en Hz, y en el eje vertical la amplitud de cada componente frecuencial. La mayor parte está concentrada entre los 100 Hz y 1000 Hz, con algunos picos más pronunciados alrededor de los 200-300 Hz y 600-700 Hz. Estos picos representan las frecuencias dominantes en la señal (la voz de Tania Y Fabián). Similar al gráfico anterior, el Audio Original 2 también muestra concentraciones entre 100 Hz y 1000 Hz, con picos en frecuencias similares. Sin embargo, la distribución de las amplitudes varía ligeramente en comparación con el Audio 1, lo cual se debe a las diferencias de posición de los micrófonos. El espectro de ruido muestra una concentración mucho más baja en términos de amplitud. La mayor parte de la energía se encuentra entre 100 Hz y 1000 Hz, similar a los audios originales, pero con amplitudes mucho menores. Tras aplicar los métodos de beamforming MVDR y filtrado Wiener, el espectro resultante muestra una señal más clara. La distribución parece más concentrada en el rango entre 100 Hz y 700 Hz, lo que indica que la voz de Fabián ha sido aislada. La caída en frecuencias altas muestra que los componentes no deseados (ruido y la voz de Tania). Se uso una frecuencia logarítmica porque se permite ver tanto las frecuencias bajas como las frecuencias altas, mientras que una escala lineal dificultaría la visualización, ya que las frecuencias bajas estarían muy comprimidas y las altas muy expandidas.

### Cuarta parte

El beamforming MVDR (Minimum Variance Distortionless Response) es una técnica utilizada en el procesamiento de señales para mejorar la señal de interés (voz de Fabián) y suprimir el ruido. El algoritmo ajusta las señales capturadas por los dos micrófonos, realizando una media ponderada para eliminar el ruido ambiental y maximizar la dirección de la fuente deseada.

```python
beamformed_signal = (audio_1_aligned + audio_2_aligned) / 2
```
Este proceso mejora la claridad de la voz de Fabián. 

Después del beamforming, se utiliza el filtro Wiener para eliminar el ruido del salón, generando una señal de audio más limpia.

```python
clean_audio = wiener(beamformed_signal)
```
### Quinta parte
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
Lopez L., Sandoval R. (2024). Github 'Laboratorio 2 Procesamiento de señales: problema del coctel'[Online].
### Informacion de contacto
est.fabiana.lopez@unimilitar.edu.co
<br>
est.tania.sandoval@unimilitar.edu.co







