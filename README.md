# Implementación y evaluación de filtros digitales

## Descripción
Este proyecto implementa y evalúa filtros digitales utilizando Python.
Se genera una señal compuesta por diferentes frecuencias y se agrega
ruido blanco para comprobar el funcionamiento de los filtros.

## Objetivo
Diseñar, implementar y comparar filtros digitales pasa bajos,
pasa altos y pasa bandas, utilizando filtros IIR y FIR.

## Tecnologías utilizadas
- Python 3.14
- NumPy
- SciPy
- Matplotlib

## Señales utilizadas
Se combinaron tres señales sinusoidales:

- 5 Hz: amplitud 1.0
- 50 Hz: amplitud 0.7
- 120 Hz: amplitud 0.5

Se agregó ruido blanco para simular una señal contaminada.

## Filtros implementados

### Filtros IIR Butterworth
- Pasa bajos: frecuencia de corte de 20 Hz.
- Pasa altos: frecuencia de corte de 80 Hz.
- Pasa bandas: frecuencias de 40 a 60 Hz.

### Filtro FIR
- Pasa bajos: frecuencia de corte de 20 Hz.
- Diseño mediante ventana FIR de 101 coeficientes.

## Resultados
Los filtros consiguieron conservar las frecuencias deseadas
y reducir las frecuencias no deseadas.

El filtro pasa bajos conservó la señal de 5 Hz.
El pasa altos conservó principalmente la señal de 120 Hz.
El pasa bandas conservó principalmente la señal de 50 Hz.

También se realizó una comparación entre los filtros FIR e IIR.

## Archivos generados
- senal_original.png
- filtros_resultados.png
- respuesta_frecuencia.png
- comparacion_fir_iir.png

## Ejecución
Instalar las dependencias:

pip install numpy scipy matplotlib

Ejecutar el programa:

python main.py