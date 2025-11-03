|  # Laboratorio-4
# Señales electromiográficas EMG
# TABLA DE CONTENIDOS
1. Objetivos y metodología del experimento.
2. Marco Conceptual.
3. Diagramas de flujo.
4. Adquisición de la señal.
5. Análisis de resultados.
6. Conclusiones.
7. Aplicaciones biomédicas.

# 1.  Objetivos y metodología del experimento.
La presente práctica tiene como objetivo aplicar el filtrado de señales continuas para procesar una señal electromiográfica (EMG). Además, se busca detectar la aparición de fatiga muscular meidante el análisis espectral de contracciones musculares individuales y con ello, compara el comportamiento con una señal emulada (capturada por un generador de señales biológicas) en terminos de frecuencia media y mediana. Todo eso, empleando herramientas computacionales para el procesamiento, segmentación y análisis de señales biomédicas.

# 2. Marco conceptual.

**Electromiografía.**

<img width="350" height="180" alt="image" src="https://github.com/user-attachments/assets/b1c75e85-1172-4f78-b4b0-8dfd5522944b" />

La electromiografía (EMG) es un procedimiento donde se evalua la salud muscular y se estudian los nervios que controlan los músculos, mediante el registro de su actividad eléctrica, es decir la suma de todos los potenciales de acción de las unidades motoras detectadas. A través de la señal electromiográfica, se pueden diagnosticar trastornos musculares y nerviosos, como disfunción muscular.

Además de esto, se puede visualizar en la señal EMG cuando un músculo entra en fátiga, donde disminuye la capacidad del musculo para generar una fuerza. Esto se puede visualizar en la señal en el aumento de la amplitud, ya que el sistema nervioso "recluta" más unidades motoras para mantener la fuerza ejercida. Del mismo modo, evaluar la fatiga muscular resulta efectivo para prevenir lesiones u optimizar el rendimiento deportivo, con el fin de garantizar la salud a largo plazo al permitir ajustar la carga de entrenamiento.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/50d9e1e1-6145-43a0-9aa0-ca443567369c" />

Del mismo modo, la señal electromiográfica posee mucha información para analizar, por lo que se necesita visualizar la señal en terminos de frecuencia y esto se hace aplicando la transformada de fourier, ya que transforma la señal del dominio del tiempo al dominio de la frecuencia, revelando así información oculta que puede ser relevante para un diagnostico clínico.

# 3. Diagramas de flujo.
**3.1. Diagrama de flujo - Parte A:Captura de la señal emulada**
Se adquirio una señal EMG emulada, en primera instancia se confiduró el generador de señales para así adquirir la señal y  simular cinco contracciones musculares. 
Se implemento un algoritmo para calcular la frecuencia media y mediana, de los cuales estos resultados arrrojados se presentaron en una tabla y gráficamente para observar la variación de las frecuencias durantes dichas contracciones.


<img width="1280" height="960" alt="2" src="https://github.com/user-attachments/assets/8de8cd81-8bfb-44e6-b354-f799c4d0bc10" />



**3.2. Diagrama de flujo - Parte B:Captura de la señal de paciente**

En la parte B se implemeto un algoritmo para analizar y registrar una señal EMG obtenidas por una persona. Se añadieron electrodos en el músculo del antebrazo y se registró la señal durante contracciones repetidas hasta la fatiga. El código aplica un filtro pasa banda para poder eliminar el ruido,divide la señal en las contracciones realizadas y poder calcular la frecuencia media y mediana y finalmente analiza la relación con la fatiga muscular.

<img width="1664" height="1248" alt="1" src="https://github.com/user-attachments/assets/29c04892-33d3-42c1-be99-b6263f10033d" />


**3.3. Diagrama de flujo - Parte C:Análisis espectral mediante FFT**

<img width="1024" height="768" alt="Grafica Diagrama de Flujo Proceso Organico Colorido" src="https://github.com/user-attachments/assets/86740838-a247-45f7-b1a6-564e857cf1e9" />

En la Parte C, se muestra el diagrama de flujo que implementa el algoritmo para el análisis espectral de la señal EMG. El proceso inicia con la importación de librerías, la carga de datos y la aplicación de un filtro pasa banda  para aislar la señal. Luego el código detecta las contracciones individuales y calcula la Transformada Rápida de Fourier  para cada una obteniendo su espectro de magnitud y frecuencia. Finalmente se hace el análisis de fatiga comparando gráficamente el espectro de la primera y la última contracción y analizando métricas clave como los picos espectrales y el contenido de alta frecuencia para cuantificar el efecto del cansancio muscular. 


# 4. Adquisición de la señal.
Para la captura de la señal, se colocaron electrodos en el músculo del antebrazo. La señal analógica fue acondicionada utilizando un módulo AD8232. Posteriormente, la señal fue digitalizada y adquirida por un sistema de adquisición de datos (DAQ) de National Instruments (controlado a través de la librería nidaqmx de Python), y exportada al archivo de texto para su análisis.
Las características de la señal cargada en el script de análisis son:
Archivo:.txt
Frecuencia de Muestreo (fs): 1000 Hz (Detectada desde los datos del archivo)
Músculo Medido: Antebrazo

**Materiales utilizados**

DAQ

AD8232

Cables

Electrodos

![imagenad8232](https://github.com/user-attachments/assets/31599700-db7e-4bff-827b-13d273a132aa)


# 5. Análisis de resultados.

-**Parte A**
En primera instancia, se capturó una señal EMG ideal a través de un generador de señales biológicas, en el que se simularon aproximadamente 5 contracciones, obteniendo la siguiente señal:

<img width="440" height="207" alt="image" src="https://github.com/user-attachments/assets/5841c205-355c-45bd-ba20-ff4b1cea06eb" />

Dicha señal, al tratarse de una señl ideal, no posee ningun tipo de ruido o comportamiento anormal. Sin embargo, para señales reales se requiere de la aplicación de filtros para poder visualizar una señal mucho más limpia.

Seguido de esto, se hizo la segmentación de la señal para cada contracción y se calculó su frecuencia media y frecuencia mediana, en el que se obtuvo lo siguiente:

- Contracción 1:

<img width="442" height="218" alt="image" src="https://github.com/user-attachments/assets/df08df78-b3e6-47ad-a43f-5cf5d7e83a5a" />

- Contracción 2:

<img width="450" height="210" alt="image" src="https://github.com/user-attachments/assets/cbfb9351-7183-4eb2-85f1-c34c2268be54" />

- Contracción 3:

<img width="450" height="210" alt="image" src="https://github.com/user-attachments/assets/b01c49e3-0ad7-42e4-9e5b-de39808cecdc" />

- Contracción 4:

<img width="450" height="210" alt="image" src="https://github.com/user-attachments/assets/39ad6473-4f76-44d4-acef-b1803d29214b" />

- Contracción 5:

<img width="450" height="210" alt="image" src="https://github.com/user-attachments/assets/3fb5dbaa-3f9a-4300-8932-e6028fa10c0f" />



|                 |Frecuencia media (Hz) | Frecuencia mediana (Hz) |
|-----------------|---------------------- | ----------------------  |
|  Contracción 1  |        96.79          |        47.62            |
|  Contracción 2  |        120.74         |           60            |
|  Contracción 3  |        114.48         |           60            |
|  Contracción 4  |        112.38         |           60            |
|  Contracción 5  |        113.89         |           60            |



Con base a los datos calculados, se representó graficamente la evolución de las frecuencias, obteniendo:


<img width="450" height="210" alt="image" src="https://github.com/user-attachments/assets/8aa6677c-f54b-4579-87fb-8e9ff89f8cf9" />


Teniendo en cuenta los resultados obtenidos, se puede percibir que todas las contracciones oscilan entre un rango de frecuencias de 50 y 150 Hz, siendo valores típicos para una señal de electromiografía. Del mismo modo, se observa que la frecuencia mediana es igual luego de la segunda contracción y es por la razón de que la señal es ideal (capturada de un generador de señales biológicas). Lo mismo ocurre con la frecuencia media, con la diferencia que estos valores presentan variaciones mínimas, pero dentro de la energía útil de la señal, tal y como se había mencionado anteriormente.

-**Parte B** En esta sección, se capturó una señal EMG por medio de electrodos puestos sobre el músculo del antebrazo, en el que se registraron unas contracciones repetidas hasta llegar a la fatiga (o la falla), obteniendo la siguiente señal original y filtrada eliminando asi el ruido y artefactos:

<img width="1438" height="674" alt="image" src="https://github.com/user-attachments/assets/f21cb0c2-63e4-47d2-ba66-9f94189d5eea" />


Seguido de esto, se dividio la señal en el número de contracciones realizadas que fueron 51, obteniendo así las siguientes señales(se mostraran algunas de las señales adquiridas):

<img width="966" height="538" alt="image" src="https://github.com/user-attachments/assets/83b0d90b-297c-42d0-8cb6-420054f6553e" />


Luego calculamos por cada contraccioón la frecuencia media y mediana, graficando así los resultados obtenidos  y analizanqdo la tendencia de esta frecuencias a medida que progesa la fatiga muscular:

-**Cálculos por cada contracción:**

<img width="715" height="343" alt="image" src="https://github.com/user-attachments/assets/02e09f10-60f7-4766-8087-7d846ea7b546" />

Al observar los valores de frecuencia media y mediana de las contracciones, se observar que ambas tienden a disminuir ligeramente a medida que avanza el esfuerzo. Esto indica la alta frecuencia en la señal EMG se reduce con el tiempo, lo cual nos permite ver con claridad la fatiga muscular.

-**Gráfica de tendencia de las freuencias media y mediana**

<img width="988" height="674" alt="image" src="https://github.com/user-attachments/assets/9634e3ea-4ca1-40bf-9eb7-7f55db31120b" />



-**Parte c**


En esa última sección se hizo el análisis espectral mediante FFT,aplicando en primera instancia la transformada de fourier en la señal:


<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/d95916eb-7f31-4edd-9228-24d2da8e3a17" />

Luego se aplico la transformada de fourier a cada una de las contracciones junto con una gráfica del espectro de amplitud (frecuencia vs magnitud) observando así cómo cambia el contenido de frecuncia, algunas de las gráficas tomadas son:

<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/fc3f3683-2142-4d29-a98c-82aeaa631451" />


Comparación de todos los espectros obtenidos:

En las primeras contracciones, se nota una mayor amplitud en frecuencias medias y altas (entre aproximadamente 50 y 150 Hz), lo que indica una mayor actividad eléctrica muscular y la participación de contracciones más rápidas.

A medida que van pasando las contracciones, las gráficas muestran una reducción progresiva de la amplitud y  frecuencias más bajas.Este desplazamiento hacia frecuencias menores hace referencia a la fatiga muscular.

<img width="1243" height="1614" alt="image" src="https://github.com/user-attachments/assets/4d21fe4d-1c19-49bb-9a1d-3a6af9b5e248" />



Comparación de espectros obtenidos en la primera contracción y la última:

La primera contracción (línea azul) presenta un pico espectral pronunciado (alrededor de los 60–70 Hz), lo que indica una buena sincronización y activación de fibras musculares de alta frecuencia.

La última contracción (línea roja) muestra un pico de menor amplitud y desplazado hacia frecuencias más bajas (alrededor de 40–50 Hz), estas frecuncias representan la fatiga muscular.

<img width="1281" height="705" alt="image" src="https://github.com/user-attachments/assets/c4e2c7dc-6d4a-425d-94b9-a5bf61c61dc0" />

 Se identifico la reducción del contenido de alta frecuencia asociada con la fatiga muscular, lo cual demuestra una pérdida significativa de energía en las altas frecuencias  con la fatiga muscular, en el cual disminuyó de 0.00019 en la primera contracción a 0.00001 en la última, lo que representa una reducción aproximada del 94.7%.
 
-**Análisis  espectral como herramienta diagnóstica en EMG:**
*El análisis espectral es una herramienta fundamental en electromiografía (EMG) ya que permite evaluar el comportamiento fisiológico  y las frecuencias de los músculos durante las  contracción y  de la fatiga muscular.

# 6. Conclusiones.
La aplicación de un filtro pasa banda Butterworth (20-450 Hz) fue una etapa de preprocesamiento muy importante. Como se observa en las gráficas de la Parte B el filtro eliminó eficazmente el ruido de baja frecuencia  y los artefactos de alta frecuencia de la señal real permitiendo un análisis espectral más preciso.

Se demostró  que la fatiga muscular puede ser detectada y cuantificada mediante el análisis espectral de la señal EMG. A medida quese realizo las contracciones repetidas hasta la fatiga (51 contracciones), se observó una clara tendencia a la baja tanto en la frecuencia media como en la frecuencia mediana. Este hallazgo es consistente con la teoría fisiológica de la fatiga muscular.

El análisis mediante la Transformada Rápida de Fourier confirmó visual y cuantitativamente el fenómeno de la fatiga. Se observo una compresión del espectro de potencia hacia frecuencias más bajas a medida que avanzaba el experimento. Las primeras contracciones mostraron picos de energía en frecuencias más altas aproximadamente 60-70 Hz mientras que las contracciones finales como la 51 mostraron un claro desplazamiento de este pico de energía hacia frecuencias menores aproximadamente 40-50 Hz además de una reducción significativa en la amplitud espectral.

Tambien se encuentra que en la  frecuencia media y la frecuencia mediana son indicadores robustos y fiables para monitorear la fatiga muscular. La disminución progresiva de estos dos parámetros está directamente correlacionada con el agotamiento de las fibras musculares de contracción rápida y el reclutamiento de unidades motoras que operan a frecuencias más bajas.

La comparación entre la Parte A señal ideal y la Parte B señal real fue fundamental. La señal ideal del generador mantuvo parámetros de frecuencia estables notablemente la frecuencia mediana constante en 60 Hz tras la segunda contracción, lo cual era esperado de una simulación. En contraste, la señal biológica real mostró la variabilidad y la tendencia descendente característica de un proceso fisiológico dinámico, validando el montaje experimental para capturar fenómenos reales.
# 7. Aplicaciones biomédicas.
<img width="243" height="207" alt="image" src="https://github.com/user-attachments/assets/770ed8ef-ebbe-4e03-a7a8-3fad7ad4741a" />

Las señales EMG (electromiográficas) tiene una gran importancia en el campo de la ingeniria biomédica, ya que nos permiten registrar la actividad eléctrica generada por los músculos durante cada contracción.  En la biomédica, la emg se utiliza para poder evaluar el correcto funcionamiento del sistema  muscular y así poder  diagnosticar diversas patologías cómo las lesiones nerviosas o enfermedades de la uion neuromuscular, todo esto ayuda a diferenciar si el origen del problema es muscular o nervioso. Además, es fundamental para el control de prótesis y exesqueletos, ya que estas señales captadas en los músculos pueden utilizarse para generar movimientos en dispositivos robótico.También se emplea en el análisis de movimiento donde esto puede permitir examinar la coordinación y la fatiga muscular durante actividades físicas o deportivas. Por ende, estas señales EMG representan una herramienta muy esencial para el diagnóstico rehabilitación y el desarrollo tecnológico aplicando el al movimiento humano.

