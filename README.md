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

