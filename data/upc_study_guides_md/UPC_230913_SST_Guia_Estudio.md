# 230913 - Señales y Sistemas (SST)
**Grado en Ingeniería Electrónica de Telecomunicación (GREELEC)**  
*Escuela Técnica Superior de Ingeniería de Telecomunicación de Barcelona (ETSETB - UPC)*

## 1. Ficha Técnica y Metadatos Oficiales
- **Código UPC**: `230913`
- **Acrónimo Oficial**: `SST`
- **Semestre**: Q3 (Fase Troncal / Especialización)
- **Créditos ECTS**: 6.0 ECTS (150)
- **Departamento Responsable**: 739 - TSC - Departamento de Teoría de la Señal y Comunicaciones
- **Profesorado / Coordinación**: FRANCISCO VALLVERDU BAYES
- **Guía Docente Oficial en PDF**: [230913_guia_docent.pdf](https://www.upc.edu/grau/guiadocent/pdf/esp/230913/senales-y-sistemas.pdf)

## 2. Descripción General y Requisitos
Señales continuas y discretas, sistemas lineales e invariantes en el tiempo (LTI), convolución temporal, series y transformada de Fourier continua y discreta (CTFT, DTFT, DFT/FFT), teorema de muestreo de Nyquist-Shannon, aliasing, y función de transferencia en transformada Z con análisis de estabilidad BIBO.

## 3. Objetivos de Aprendizaje y Competencias
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
- a
- n
- a
- l
- ó
- g
- i
- c
- a
- s
-  
- y
-  
- d
- i
- g
- i
- t
- a
- l
- e
- s
-  
- e
- n
-  
- t
- i
- e
- m
- p
- o
-  
- y
-  
- f
- r
- e
- c
- u
- e
- n
- c
- i
- a
- 

- T
- r
- a
- t
- a
- m
- i
- e
- n
- t
- o
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
- a
- n
- a
- l
- ó
- g
- i
- c
- a
- s
-  
- c
- o
- n
-  
- s
- i
- s
- t
- e
- m
- a
- s
-  
- d
- i
- s
- c
- r
- e
- t
- o
- s
- 

- I
- m
- p
- l
- e
- m
- e
- n
- t
- a
- c
- i
- ó
- n
-  
- e
- n
-  
- e
- n
- t
- o
- r
- n
- o
- s
-  
- d
- e
-  
- p
- r
- o
- g
- r
- a
- m
- a
- c
- i
- ó
- n
-  
- c
- o
- n
-  
- P
- y
- t
- h
- o
- n
-  
- o
-  
- M
- a
- t
- l
- a
- b

## 4. Temario y Unidades de Contenido
- {'title': 'Contenido General', 'description': 'Señales y sistemas en el dominio temporal Descripción: Caracterización de señales en tiempo continuo y discreto Sistemas lineales e invariantes Convolución Dedicación: 42h Grupo grande/Teoría: 9h Grupo pequeño/Laboratorio: 6h Aprendizaje autónomo: 27h Señales y sistema en el dominio transformado Descripción: Transformada de Fourier y transformada Z Respuesta frecuencial y función de transferència (ceros y pols) Respuesta en régimen permanente Modulación Enventanado Filtrado Dedicación: 42h Grupo grande/Teoría: 9h Grupo pequeño/Laboratorio: 6h Aprendizaje autónomo: 27h Fecha: 06/09/2026 Página: 3 / 3 Señales periódicas y muestreo Descripción: Caracterización en serie de Fourier de señales periódicas Transformada de señales periódicas Potencia media Muestreo Teorema de muestreo Muestreo ideal Muestreo real Conversores AD i DA Dedicación: 42h Grupo grande/Teoría: 9h Grupo pequeño/Laboratorio: 6h Aprendizaje autónomo: 27h Transformada discreta de Fourier, correlación y espectro Descripción: Transformada discreta de Fourier Relación con la transformada de señales analógicas muestreadas Aplicaciones Filtrado Análisis espectral y correlación Dedicación: 42h Grupo grande/Teoría: 9h Grupo pequeño/Laboratorio: 6h Aprendizaje autónomo: 27h'}

## 5. Modelado Matemático y Fórmulas Clave (LaTeX)
### 5.1 Integral de Convolución Continua
$$
y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau
$$

### 5.2 Teorema de Muestreo de Nyquist-Shannon
$$
f_s > 2 f_{\max} = f_{\text{Nyquist}}
$$

### 5.3 Transformada Z Bilateral
$$
X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}
$$

### 5.4 Condición de Estabilidad BIBO en Tiempo Discreto
$$
\sum_{n=-\infty}^{\infty} |h[n]| < \infty \iff \text{Polos de } H(z) \text{ dentro de } |z| < 1
$$

### 5.5 Transformada Discreta de Fourier (DFT de N Puntos)
$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n}
$$

## 6. Banco de Ensayos / Laboratorio Virtual
```spice
* SST - Respuesta al Impulso y Filtrado Pasobajo RC
Vin in 0 PULSE(0 1000 0 1n 1n 1u 10m)
R1 in out 1k
C1 out 0 100nF
.tran 1u 2m
.print tran V(out)
.end
```

## 7. Preguntas de Autoevaluación y Examen con Justificación Técnica
#### Pregunta 1
**¿Un sistema LTI continuo es causal y estable BIBO si y solo si todos los polos de su función de transferencia H(s) se ubican estrictamente en el semiplano izquierdo Re(s) < 0?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Garantiza que la respuesta impulsional decaiga exponencialmente a cero.

#### Pregunta 2
**¿El teorema de Nyquist exige muestrear a una frecuencia estrictamente mayor que el doble del ancho de banda máximo para evitar aliasing?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. fs > 2*fmax.

#### Pregunta 3
**La convolución en el dominio temporal equivale a la convolución en el dominio frecuencial de Fourier.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Equivale a la multiplicación punto a punto Y(w) = X(w) * H(w).

#### Pregunta 4
**¿En un sistema LTI discreto causal, los polos de H(z) deben situarse dentro del círculo unidad (|z| < 1) para garantizar estabilidad?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. La región de convergencia (ROC) debe abarcar la circunferencia unidad |z| = 1.

#### Pregunta 5
**¿La transformada discreta de Fourier de N puntos (DFT) computada mediante el algoritmo FFT tiene una complejidad O(N log2 N)?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Gran mejora frente al cálculo directo O(N^2).

#### Pregunta 6
**La respuesta impulsional h(t) de un sistema estático sin memoria es proporcional a la función escalón unitario u(t).**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Es proporcional a un impulso delta de Dirac K*delta(t).

#### Pregunta 7
**¿Un sistema es invariante en el tiempo si un retardo en la entrada x(t - T) produce idéntico retardo en la salida y(t - T)?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Propiedad fundamental de invariancia temporal.

#### Pregunta 8
**¿La respuesta al escalón de un sistema LTI es la integral en el tiempo de su respuesta impulsional h(t)?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Dado que el escalón es la integral del impulso de Dirac.

#### Pregunta 9
**El aliasing espectral se puede corregir digitalmente después del convertidor ADC sin pérdida de información.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. El aliasing solapa espectros irreversiblemente; debe eliminarse antes del muestreo con un filtro antialiasing analógico.

#### Pregunta 10
**¿La autocorrelación de una señal continua en el origen R_xx(0) equivale a la energía total de la señal?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. R_xx(0) = integral(|x(t)|^2 dt) = E_total.

#### Pregunta 11
**¿Un filtro de fase lineal pura introduce un retardo de grupo constante en todas las frecuencias de la banda de paso evitando la distorsión de fase?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Mantiene intacta la forma de onda de la señal compuesta.

#### Pregunta 12
**El producto de dos funciones periódicas siempre da como resultado una función periódica para cualquier relación de periodos.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Solo es periódica si el cociente de sus periodos o frecuencias es un número racional.

## 8. Sistema de Evaluación y Bibliografía Recomendada
**Evaluación**: Cualquier acto de fraude académico, plagio o uso o mera tenencia al alcance de medios no autorizados en cualquier actividad de
evaluación comportará la calificación de cero (0) en la prueba o entrega afectada. Además, de acuerdo con la normativa de la
Universidad, la posible derivación de los hechos para la apertura de un expediente disciplinario implicará que la asignatura quede en
el estado provisional de "pendiente de evaluación" hasta la resolución del expediente. La gestión de estas incidencias se lleva a cabo
de acuerdo con el Marco de actuación para la integridad académica en la evaluación de la UPC.
Control a mitad del curso 30%
Laboratori 10%
Examen final 60%
NORMAS PARA LA REALIZACIÓN DE LAS PRUEBAS.
Solamente pueden ser reevaluados los contenidos teóricos

**Bibliografía de Referencia**:
- - Proakis, John G; Manolakis, Dimitris G. Digital signal processing. 4th ed. New Jersey: Prentice-Hall International, Inc, cop. 2007.
- ISBN 0131873741.