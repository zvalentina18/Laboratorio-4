# Laboratorio-4
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
# 3. Diagramas de flujo.
**3.1. Diagrama de flujo - Parte A:Captura de la señal emulada**
Se adquirio una señal EMG emulada, en primera instancia se confiduró el generador de señales para así adquirir la señal y  simular cinco contracciones musculares. 
Se implemento un algoritmo para calcular la frecuencia media y mediana, de los cuales estos resultados arrrojados se presentaron en una tabla y gráficamente para observar la variación de las frecuencias durantes dichas contracciones.

<img width="1280" height="960" alt="2" src="https://github.com/user-attachments/assets/8de8cd81-8bfb-44e6-b354-f799c4d0bc10" />


**3.2. Diagrama de flujo - Parte B:Captura de la señal de paciente**
En la parte B se implemeto un algoritmo para analizar y registrar una señal EMG obtenidas por una persona. Se añadieron electrodos en el músculo del antebrazo y se registró la señal durante contracciones repetidas hasta la fatiga. El código aplica un filtro pasa banda para poder eliminar el ruido,divide la señal en las contracciones realizadas y poder calcular la frecuencia media y mediana y finalmente analiza la relación con la fatiga muscular.
<img width="1664" height="1248" alt="1" src="https://github.com/user-attachments/assets/29c04892-33d3-42c1-be99-b6263f10033d" />


**3.3. Diagrama de flujo - Parte C:Análisis espectral mediante FFT**
En la parte C se implemeto un algoritmo para analizar 


# 4. Adquisición de la señal.
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


-**Gráfica de tendencia de las freuencias media y mediana**

<img width="988" height="674" alt="image" src="https://github.com/user-attachments/assets/9634e3ea-4ca1-40bf-9eb7-7f55db31120b" />



# 6. Conclusiones.
# 7. Aplicaciones biomédicas.
<img width="243" height="207" alt="image" src="https://github.com/user-attachments/assets/770ed8ef-ebbe-4e03-a7a8-3fad7ad4741a" />

Las señales EMG (electromiográficas) tiene una gran importancia en el campo de la ingeniria biomédica, ya que nos permiten registrar la actividad eléctrica generada por los músculos durante cada contracción.  En la biomédica, la emg se utiliza para poder evaluar el correcto funcionamiento del sistema  muscular y así poder  diagnosticar diversas patologías cómo las lesiones nerviosas o enfermedades de la uion neuromuscular, todo esto ayuda a diferenciar si el origen del problema es muscular o nervioso. Además, es fundamental para el control de prótesis y exesqueletos, ya que estas señales captadas en los músculos pueden utilizarse para generar movimientos en dispositivos robótico.También se emplea en el análisis de movimiento donde esto puede permitir examinar la coordinación y la fatiga muscular durante actividades físicas o deportivas. Por ende, estas señales EMG representan una herramienta muy esencial para el diagnóstico rehabilitación y el desarrollo tecnológico aplicando el al movimiento humano.

