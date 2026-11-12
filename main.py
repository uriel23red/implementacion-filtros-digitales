
# ============================================================
# PROYECTO: IMPLEMENTACIÓN Y EVALUACIÓN DE FILTROS DIGITALES
# ETAPA 2: CREACIÓN DE SEÑALES DE PRUEBA
# ============================================================

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ------------------------------------------------------------
# 1. CONFIGURACIÓN DE LA SIMULACIÓN
# ------------------------------------------------------------

frecuencia_muestreo = 1000  # Muestras por segundo (Hz)
duracion = 2                 # Duración de la señal en segundos

# Crear el vector de tiempo
tiempo = np.arange(
    0,
    duracion,
    1 / frecuencia_muestreo
)

# ------------------------------------------------------------
# 2. GENERACIÓN DE SEÑALES DE DIFERENTES FRECUENCIAS
# ------------------------------------------------------------

# Señal de frecuencia baja: 5 Hz
senal_baja = np.sin(2 * np.pi * 5 * tiempo)

# Señal de frecuencia media: 50 Hz
senal_media = 0.7 * np.sin(2 * np.pi * 50 * tiempo)

# Señal de frecuencia alta: 120 Hz
senal_alta = 0.5 * np.sin(2 * np.pi * 120 * tiempo)

# Combinar las tres señales
senal_original = senal_baja + senal_media + senal_alta

# ------------------------------------------------------------
# 3. AGREGAR RUIDO BLANCO
# ------------------------------------------------------------

# Generar ruido aleatorio
np.random.seed(42)
ruido = 0.8 * np.random.normal(0, 1, len(tiempo))

# Agregar ruido a la señal original
senal_ruidosa = senal_original + ruido

# ------------------------------------------------------------
# 4. GRAFICAR LAS SEÑALES
# ------------------------------------------------------------

plt.figure(figsize=(12, 9))

# Gráfica de la señal original
plt.subplot(3, 1, 1)
plt.plot(tiempo, senal_original)
plt.title("Señal original compuesta por tres frecuencias")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()

# Gráfica de la señal con ruido
plt.subplot(3, 1, 2)
plt.plot(tiempo, senal_ruidosa, color="red")
plt.title("Señal contaminada con ruido blanco")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()

# Comparación de ambas señales
plt.subplot(3, 1, 3)
plt.plot(tiempo, senal_original, label="Original")
plt.plot(tiempo, senal_ruidosa, alpha=0.5, label="Con ruido")
plt.title("Comparación de señales")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("senal_original.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# 5. INFORMACIÓN DE LA SIMULACIÓN
# ------------------------------------------------------------

print("SIMULACIÓN DE SEÑALES COMPLETADA")
print("--------------------------------")
print("Frecuencia de muestreo:", frecuencia_muestreo, "Hz")
print("Duración:", duracion, "segundos")
print("Número de muestras:", len(tiempo))
print("Frecuencias utilizadas: 5 Hz, 50 Hz y 120 Hz")
print("Ruido blanco agregado correctamente")

# ============================================================
# ETAPA 3: DISEÑO E IMPLEMENTACIÓN DE FILTROS DIGITALES
# ============================================================

# ------------------------------------------------------------
# 1. DISEÑAR LOS FILTROS BUTTERWORTH
# ------------------------------------------------------------

orden = 4

# Filtro pasa bajos: conserva frecuencias menores a 20 Hz
filtro_bajos = signal.butter(
    orden, 20,
    btype="lowpass",
    fs=frecuencia_muestreo,
    output="sos"
)

# Filtro pasa altos: conserva frecuencias mayores a 80 Hz
filtro_altos = signal.butter(
    orden, 80,
    btype="highpass",
    fs=frecuencia_muestreo,
    output="sos"
)

# Filtro pasa bandas: conserva frecuencias entre 40 y 60 Hz
filtro_bandas = signal.butter(
    orden, [40, 60],
    btype="bandpass",
    fs=frecuencia_muestreo,
    output="sos"
)

# ------------------------------------------------------------
# DISEÑO DEL FILTRO CHEBYSHEV TIPO I
# ------------------------------------------------------------

filtro_chebyshev = signal.cheby1(
    4,                  # Orden del filtro
    1,                  # Rizado máximo en banda de paso (dB)
    20,                 # Frecuencia de corte (Hz)
    btype="lowpass",
    fs=frecuencia_muestreo,
    output="sos"
)

# ------------------------------------------------------------
# 2. APLICAR LOS FILTROS A LA SEÑAL RUIDOSA
# ------------------------------------------------------------

resultado_bajos = signal.sosfiltfilt(
    filtro_bajos, senal_ruidosa
)

# Aplicar el filtro Chebyshev
resultado_chebyshev = signal.sosfiltfilt(
    filtro_chebyshev,
    senal_ruidosa
)


resultado_altos = signal.sosfiltfilt(
    filtro_altos, senal_ruidosa
)

resultado_bandas = signal.sosfiltfilt(
    filtro_bandas, senal_ruidosa
)


# ------------------------------------------------------------
# 3. DISEÑAR Y APLICAR UN FILTRO FIR
# ------------------------------------------------------------

# Diseñar un filtro FIR pasa bajos de 101 coeficientes
coeficientes_fir = signal.firwin(
    numtaps=101,
    cutoff=20,
    fs=frecuencia_muestreo,
    pass_zero="lowpass"
)

# Aplicar el filtro FIR a la señal con ruido
resultado_fir = signal.filtfilt(
    coeficientes_fir,
    1.0,
    senal_ruidosa
)

# Graficar la comparación entre IIR y FIR
plt.figure(figsize=(12, 6))

plt.plot(
    tiempo,
    resultado_bajos,
    label="IIR Butterworth"
)

plt.plot(
    tiempo,
    resultado_fir,
    label="FIR"
)

plt.title("Comparación de filtros IIR y FIR")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("comparacion_fir_iir.png", dpi=300)
plt.show()

print("Filtro FIR aplicado correctamente.")

# ------------------------------------------------------------
# 3. GRAFICAR LAS SEÑALES FILTRADAS
# ------------------------------------------------------------

plt.figure(figsize=(12, 10))

plt.figure(figsize=(12, 12))

plt.subplot(4, 1, 1)
plt.plot(tiempo, resultado_bajos, color="blue")
plt.title("Filtro pasa bajos Butterworth (20 Hz)")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(tiempo, resultado_altos, color="green")
plt.title("Filtro pasa altos Butterworth (80 Hz)")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(tiempo, resultado_bandas, color="purple")
plt.title("Filtro pasa bandas Butterworth (40-60 Hz)")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(tiempo, resultado_chebyshev, color="orange")
plt.title("Filtro pasa bajos Chebyshev (20 Hz)")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.savefig("filtros_resultados.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# 4. ANALIZAR LA RESPUESTA EN FRECUENCIA
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

# Obtener la respuesta en frecuencia de cada filtro
for filtro, nombre in [
    (filtro_bajos, "Pasa bajos Butterworth"),
    (filtro_altos, "Pasa altos Butterworth"),
    (filtro_bandas, "Pasa bandas Butterworth"),
    (filtro_chebyshev, "Pasa bajos Chebyshev")
]:

    frecuencias, respuesta = signal.sosfreqz(
        filtro,
        worN=2048,
        fs=frecuencia_muestreo
    )

    # Convertir la magnitud a decibelios
    magnitud_db = 20 * np.log10(
        np.maximum(np.abs(respuesta), 1e-10)
    )

    plt.plot(frecuencias, magnitud_db, label=nombre)

# Obtener la respuesta en frecuencia del filtro FIR
frecuencias_fir, respuesta_fir = signal.freqz(
    coeficientes_fir,
    worN=2048,
    fs=frecuencia_muestreo
)

# Convertir la magnitud del FIR a decibelios
magnitud_fir_db = 20 * np.log10(
    np.maximum(np.abs(respuesta_fir), 1e-10)
)

# Agregar el FIR a la gráfica
plt.plot(
    frecuencias_fir,
    magnitud_fir_db,
    label="Pasa bajos FIR",
    linestyle="--"
)


plt.title("Respuesta en frecuencia de los filtros Butterworth")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.xlim(0, 200)
plt.ylim(-100, 5)
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("respuesta_frecuencia.png", dpi=300)
plt.show()
# ------------------------------------------------------------
# 5. ANALIZAR EL ESPECTRO DE LAS SEÑALES
# ------------------------------------------------------------

# Calcular la Transformada Rápida de Fourier
def obtener_espectro(senal):

    espectro = np.fft.rfft(senal)

    frecuencias = np.fft.rfftfreq(
        len(senal),
        d=1 / frecuencia_muestreo
    )

    amplitud = 2 * np.abs(espectro) / len(senal)

    return frecuencias, amplitud


# Obtener el espectro de la señal original y filtradas
plt.figure(figsize=(12, 7))

for nombre, senal in [
    ("Señal con ruido", senal_ruidosa),
    ("Butterworth pasa bajos", resultado_bajos),
    ("Butterworth pasa altos", resultado_altos),
    ("Butterworth pasa bandas", resultado_bandas),
    ("Chebyshev pasa bajos", resultado_chebyshev),
    ("FIR pasa bajos", resultado_fir)
]:

    frecuencias, amplitud = obtener_espectro(senal)

    plt.plot(
        frecuencias,
        amplitud,
        label=nombre
    )

plt.title("Espectro de frecuencias antes y después del filtrado")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.xlim(0, 200)
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("espectro_frecuencias.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# 5. CONFIRMAR LOS RESULTADOS
# ------------------------------------------------------------

print("\nDISEÑO DE FILTROS COMPLETADO")
print("--------------------------------")
print("Filtro pasa bajos: 20 Hz")
print("Filtro pasa altos: 80 Hz")
print("Filtro pasa bandas: 40 a 60 Hz")
print("Orden de los filtros:", orden)
print("Los tres filtros se aplicaron correctamente.")

print("\nARCHIVOS GENERADOS:")
print("1. senal_original.png")
print("2. filtros_resultados.png")
print("3. respuesta_frecuencia.png")
print("4. comparacion_fir_iir.png")

print("Pasa bajos:", np.std(resultado_bajos))
print("Pasa altos:", np.std(resultado_altos))
print("Pasa bandas:", np.std(resultado_bandas))


# ============================================================
# ETAPA 4: EVALUACIÓN DE LOS FILTROS
# ============================================================

# Función para medir la amplitud de una frecuencia
def medir_frecuencia(senal, frecuencia_objetivo):

    # Calcular la Transformada Rápida de Fourier
    espectro = np.fft.rfft(senal)

    # Obtener las frecuencias correspondientes
    frecuencias = np.fft.rfftfreq(
        len(senal),
        d=1 / frecuencia_muestreo
    )

    # Encontrar la frecuencia más cercana
    indice = np.argmin(
        np.abs(frecuencias - frecuencia_objetivo)
    )

    # Calcular la amplitud
    amplitud = 2 * np.abs(espectro[indice]) / len(senal)

    return amplitud


# Señales que vamos a evaluar

senales = {
    "Original": senal_original,
    "Con ruido": senal_ruidosa,
    "Pasa bajos Butterworth": resultado_bajos,
    "Pasa altos Butterworth": resultado_altos,
    "Pasa bandas Butterworth": resultado_bandas,
    "Pasa bajos Chebyshev": resultado_chebyshev,
    "Pasa bajos FIR": resultado_fir
}

# Frecuencias que queremos analizar
frecuencias_objetivo = [5, 50, 120]

print("\nEVALUACIÓN DE FRECUENCIAS")
print("--------------------------------")

# Mostrar los resultados
for nombre, senal in senales.items():

    print("\n", nombre)

    for frecuencia in frecuencias_objetivo:

        amplitud = medir_frecuencia(
            senal,
            frecuencia
        )

        print(
            f"Frecuencia {frecuencia} Hz: "
            f"{amplitud:.4f}"
        )

print("\nEVALUACIÓN COMPLETADA")

