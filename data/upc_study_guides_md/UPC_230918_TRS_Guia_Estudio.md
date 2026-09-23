# 230918 - Tratamiento de la Señal (TRS)
**Grado en Ingeniería Electrónica de Telecomunicación (GREELEC)**  
*Escuela Técnica Superior de Ingeniería de Telecomunicación de Barcelona (ETSETB - UPC)*

## 1. Ficha Técnica y Metadatos Oficiales
- **Código UPC**: `230918`
- **Acrónimo Oficial**: `TRS`
- **Semestre**: Q4 (Fase Troncal / Especialización)
- **Créditos ECTS**: 6.0 ECTS (150)
- **Departamento Responsable**: 739 - TSC - Departamento de Teoría de la Señal y Comunicaciones
- **Profesorado / Coordinación**: Otros:
- **Guía Docente Oficial en PDF**: [230918_guia_docent.pdf](https://www.upc.edu/grau/guiadocent/pdf/esp/230918/tratamiento-de-la-senal.pdf)

## 2. Descripción General y Requisitos
Filtrado digital (filtros FIR de fase lineal por enventanado y Remez-Parks-McClellan, filtros IIR por transformación bilineal Butterworth, Chebyshev y elípticos), procesamiento multirate (diezmado, interpolación, filtros polifase), cuantización y ruido de redondeo, estimación espectral paramétrica y no paramétrica (periodograma de Welch), y algoritmos adaptativos (LMS y RLS).

## 3. Objetivos de Aprendizaje y Competencias
- -
-  
- C
- a
- r
- a
- c
- t
- e
- r
- i
- z
- a
- c
- i
- ó
- n
-  
- d
- e
-  
- s
- e
- ñ
- a
- l
- e
- s
-  
- c
- o
- m
- o
-  
- p
- r
- o
- c
- e
- s
- o
- s
-  
- e
- s
- t
- o
- c
- á
- s
- t
- i
- c
- o
- s
- .
- 

- -
-  
- T
- e
- o
- r
- í
- a
-  
- d
- e
-  
- l
- a
-  
- d
- e
- t
- e
- c
- c
- i
- ó
- n
- .
- 

- -
-  
- T
- e
- o
- r
- í
- a
-  
- d
- e
-  
- e
- s
- t
- i
- m
- a
- c
- i
- ó
- n
- .
- 

- -
-  
- F
- i
- l
- t
- r
- a
- d
- o
-  
- ó
- p
- t
- i
- m
- o
- .
- 

- -
-  
- F
- i
- l
- t
- r
- a
- d
- o
-  
- a
- d
- a
- p
- t
- a
- t
- i
- v
- o
- .
- 

- 

- F
- e
- c
- h
- a
- :
-  
- 0
- 6
- /
- 0
- 9
- /
- 2
- 0
- 2
- 6
- 

- P
- á
- g
- i
- n
- a
- :
-  
- 2
-  
- /
-  
- 4

## 4. Temario y Unidades de Contenido
- {'title': 'Tema 1. Caracterización de procesos en tiempo discreto.', 'description': '- Notación vectorial y variable aleatoria. - Caracterización de procesos estocásticos (estacionarios y ergódicos), matriz de correlación y propiedades, densidad espectral de potencia, procesos discretos y sistemas lineales.'}
- {'title': 'Tema 2. Teoria de la detección', 'description': '- El problema de la toma de decisiones: verificación de hipótesis, terminología y ejemplos - Criterios MAP y Neyman-Pearson - Detección de señales deterministas y ROC'}
- {'title': 'Tema 3. Teoría de la estimación.', 'description': '- El problema de la estimación. - Estimación de parámetros y estimador MVUE. - Límite de Cramer-Rao y estimador eficiente. - Estimación de máxima verosimilitud, estimación MAP y MMSE.'}
- {'title': 'Tema 4. Filtrado óptimo.', 'description': '- Estimación lineal cuadrático-media. - Tipos de filtrado: identificación de sistema, ecualización, cancelación, predicción e interpolación. - Regresión lineal y mínimos cuadrados.'}
- {'title': 'Tema 5. Filtro adaptativo', 'description': '- Método de gradiente para regresión lineal. - Métodos de gradiente estocástico (LMS). - Convergencia y desajuste. LMS normalizado.'}

## 5. Modelado Matemático y Fórmulas Clave (LaTeX)
### 5.1 Transformación Bilineal (Analógico a Digital)
$$
s = \frac{2}{T_s} \frac{1 - z^{-1}}{1 + z^{-1}}, \quad \Omega = \frac{2}{T_s} \tan\left( \frac{\omega}{2} \right)
$$

### 5.2 Relación de Fase Lineal en Filtro FIR Simétrico
$$
\theta(\omega) = -\alpha \omega, \quad \tau_g = -\frac{d\theta}{d\omega} = \frac{N-1}{2}
$$

### 5.3 Potencia de Ruido de Cuantización Uniforme
$$
\sigma_q^2 = \frac{\Delta^2}{12}, \quad \Delta = \frac{V_{\text{FS}}}{2^B}
$$

### 5.4 Relación Señal a Ruido de Cuantización (SQNR)
$$
\text{SQNR} \approx 6.02 B + 1.76\,\text{dB}
$$

### 5.5 Algoritmo LMS Adaptativo
$$
\vec{w}[n+1] = \vec{w}[n] + 2 \mu e[n] \vec{x}[n], \quad e[n] = d[n] - \vec{w}^T[n] \vec{x}[n]
$$

## 6. Banco de Ensayos / Laboratorio Virtual
```c
// TRS - Implementación en C de Filtro FIR Direct Form de Fase Lineal
#define N_TAPS 5
float fir_filter(float input, const float *coeffs, float *buffer) {
    float acc = 0.0f;
    for (int i = N_TAPS - 1; i > 0; i--) buffer[i] = buffer[i - 1];
    buffer[0] = input;
    for (int i = 0; i < N_TAPS; i++) acc += coeffs[i] * buffer[i];
    return acc;
}
```

## 7. Preguntas de Autoevaluación y Examen con Justificación Técnica
#### Pregunta 1
**¿Los filtros FIR son intrínsecamente estables porque todas sus funciones de transferencia presentan únicamente polos en el origen z = 0?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Tienen un número finito de coeficientes en su respuesta impulsional.

#### Pregunta 2
**¿Los filtros FIR con simetría par o impar garantizan una fase rigurosamente lineal y retardo de grupo constante?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Preservan la forma de onda de las señales complejas sin dispersión de fase.

#### Pregunta 3
**La transformación bilineal introduce una deformación o compresión de la escala de frecuencias (frequency warping) que exige un predistorsionado previo.**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Omega = (2/Ts)*tan(omega/2); mapea todo el eje jOmega en la circunferencia unidad |z|=1.

#### Pregunta 4
**¿Cada bit adicional de resolución en un convertidor ADC cuantizado uniformemente incrementa la relación SQNR en aproximadamente 6.02 dB?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. SQNR approx 6.02*B + 1.76 dB.

#### Pregunta 5
**Un filtro IIR requiere siempre mayor número de coeficientes y operaciones que un filtro FIR para satisfacer las mismas especificaciones de atenuación.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Los filtros IIR aprovechan polos y ceros, requiriendo un orden mucho menor que los FIR equivalentes.

#### Pregunta 6
**¿El diezmado por un factor M consiste en un filtrado antialiasing pasobajo previo seguido de la eliminación de M-1 de cada M muestras?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. El prefiltrado evita el solapamiento espectral.

#### Pregunta 7
**¿La interpolación por un factor L inserta L-1 ceros entre muestras consecutivas seguida de un filtro pasobajo de anti-imagen?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Elimina las réplicas espectrales intermedias restaurando la señal en la nueva frecuencia de muestreo L*fs.

#### Pregunta 8
**El algoritmo LMS adaptativo minimiza el error cuadrático medio actualizando los pesos en la dirección del gradiente instantáneo.**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. w[n+1] = w[n] + 2*mu*e[n]*x[n].

#### Pregunta 9
**¿El método del periodograma de Welch divide la señal en segmentos solapados enventanados y promedia sus periodogramas para reducir la varianza de la estimación espectral?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Reduce el ruido y la varianza espectral a costa de una pequeña merma en resolución frecuencial.

#### Pregunta 10
**Los filtros Butterworth se caracterizan por presentar un rizado equiripple en la banda de paso y de corte.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Los Butterworth son de máxima planicidad (maximally flat) sin ningún rizado. El rizado equiripple es característico de Chebyshev y Cauer/Elípticos.

#### Pregunta 11
**¿La estructura de filtrado polifase permite trasladar los filtros digitales a la frecuencia de muestreo más baja optimizando el número de operaciones por segundo?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Fundamento de los bancos de filtros eficientes en telecomunicaciones.

#### Pregunta 12
**¿El desbordamiento en aritmética de punto fijo en complementario a dos sin saturación puede originar ciclos límite de gran amplitud?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Las oscilaciones por wrap-around provocan inestabilidad si no se incluye lógica de saturación.

## 8. Sistema de Evaluación y Bibliografía Recomendada
**Evaluación**: Cualquier acto de fraude académico, plagio o uso o mera tenencia al alcance de medios no autorizados en cualquier actividad de
evaluación comportará la calificación de cero (0) en la prueba o entrega afectada. Además, de acuerdo con la normativa de la
Universidad, la posible derivación de los hechos para la apertura de un expediente disciplinario implicará que la asignatura quede en
el estado provisional de "pendiente de evaluación" hasta la resolución del expediente. La gestión de estas incidencias se lleva a cabo
de acuerdo con el Marco de actuación para la integridad académica en la evaluación de la UPC.
La realización de todas las prácticas de laboratorio y presentación de los correspondientes informes durante el cuatrimestre en el que
se cursa la asignatura son obligatorias y, por lo tanto, una condición necesaria para superar la asignatura. En caso de no hacerlo, el
alumno obtendrá un No Presentado (NP) de la asignatura sin aplicársele los porcentajes que se detallan más abajo. Las prácticas no
son reevaluables.
Una prueba de control consistente en la realización de ejercicios. (20%)
Seguimiento del trabajo realizado en el laboratorio (25%)
Examen final (55%)

**Bibliografía de Referencia**:
- - Manolakis, D.G.; Ingle, V.K.; Kogon, S.M. Statistical and adaptive signal processing: spectral estimation, signal modeling, adaptive
- filtering, and array processing. Boston: Artech House, 2005. ISBN 1580536107.
- - Kay, S.M. Fundamentals of statistical signal processing. Englewood Cliffs: Prentice-Hall, 1993-2013. ISBN 0130422681.
- Complementaria:
- - Theodoridis, S. Machine learning : a bayesian and optimization perspective [en línea]. 2nd ed. London: Elsevier Academic Press,