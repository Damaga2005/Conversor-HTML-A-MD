# 230914 - Probabilidad y Procesos Estocásticos (PPE)
**Grado en Ingeniería Electrónica de Telecomunicación (GREELEC)**  
*Escuela Técnica Superior de Ingeniería de Telecomunicación de Barcelona (ETSETB - UPC)*

## 1. Ficha Técnica y Metadatos Oficiales
- **Código UPC**: `230914`
- **Acrónimo Oficial**: `PPE`
- **Semestre**: Q3 (Fase Troncal / Especialización)
- **Créditos ECTS**: 6.0 ECTS (150)
- **Departamento Responsable**: 749 - MAT / 739 - TSC
- **Profesorado / Coordinación**: ORIOL SERRA ALBO
- **Guía Docente Oficial en PDF**: [230914_guia_docent.pdf](https://www.upc.edu/grau/guiadocent/pdf/esp/230914/probabilidad-y-procesos-estocasticos.pdf)

## 2. Descripción General y Requisitos
Espacios de probabilidad, probabilidad total y regla de Bayes, variables aleatorias discretas y continuas (Gaussianas, uniformes, Poisson, exponenciales), vectores aleatorios, momentos, covarianza y correlación, Teorema Central del Límite, procesos estocásticos estacionarios en sentido amplio (WSS), autocorrelación y densidad espectral de potencia (Wiener-Khinchin), y filtrado LTI de procesos aleatorios.

## 3. Objetivos de Aprendizaje y Competencias
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
- P
- r
- o
- b
- a
- b
- i
- l
- i
- d
- a
- d
- .
-  
- V
- a
- r
- i
- a
- b
- l
- e
- s
-  
- a
- l
- e
- a
- t
- o
- r
- i
- a
- s
- .
-  
- C
- o
- n
- c
- e
- p
- t
- o
- s
-  
- d
- e
-  
- E
- s
- t
- a
- d
- í
- s
- t
- i
- c
- a
-  
- y
-  
- d
- e
-  
- P
- r
- o
- c
- e
- s
- o
- s
-  
- E
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
- {'title': 'Contenido General', 'description': '1. Teoría básica de la probabilidad Descripción: Combinatoria: Permutaciones, variaciones y combinaciones. Experimento aleatorio, espacio mostral, sucesos aleatorios. Espacio de probabilidad. Espacios discretos, fórmula de Laplace. Espacios continuos, sigma-álgebra de Borel. Independencia y probabilidad condicionada. Teorema de Bayes y fórmula de la probabilidad total. Significado de la probabilidad. Actividades vinculadas: Ciestionario Probabilidad Básica Dedicación: 15h Grupo grande/Teoría: 15h 2. Variables aleatorias unidimensionales Descripción: Variable aleatoria. Función de distribución. Variables aleatorias discretas, función de probabilidad. Ejemplos de variables discretas (Bernoulli, geométrica, binomial, Poisson). Variables aleatorias continuas, función de densidad. Ejemplos de variables continuas (uniforme, exponencial, gaussiana). Teorema de DeMoivre-Laplace. Densidad condicionada. Funciones de una variable aleatoria (caso discreto, caso continuo, casos especiales). Parámetros estadísticos: Esperança, varianza, desviación estándar. Momentos y momentos centrados. Desigualdad de Chebyshov. Ley de los grandes números. Actividades vinculadas: Cuestionario Variables Aleatorias Dedicación: 13h Grupo grande/Teoría: 13h 3. Variables aleatorias multidimensionals Descripción: Variables aleatorias multidimensionales. Función de distribución conjunta. Caso discreto, función de probabilidad conjunta. Caso continuo, función de densidad conjunta. Ejemplos de variables multidimensionals (multinomiales, uniformes, gaussianas). Distribuciones marginales. Independencia de variables aleatorias. Distribuciones condicionadas. Funciones de varias variables. Suma de variables aleatorias: teorema de convolución. Cambios de variable. Teorema de la esperanza. Covarianza y coeficiente de correlación. Ortogonalidad, incorrelación e independencia. Estimación de variables aleatorias. Estimación lineal. Principio de ortogonalitat. Actividades vinculadas: Cuestionario Variables multidimensionales Examen Parcial (3h) Dedicación: 14h Grupo grande/Teoría: 14h Fecha: 06/09/2026 Página: 3 / 4 4. Estadística Descripción: Variables aleatorias relevantes en estadística: gaussianas multidimensionals, Khi cuadrado, t de Student, F de Fisher. Teorema Central del Límite. Poblaciones y muestras. Estadística descriptiva (histogramas, boxplots, scatterplots). Estadísticos muestrales: distribución y parámetros. Estimación de parámetros: método de los momentos y método de la máxima verosimilitud. Intervalos de confianza (para la esperanza, la varianza, proporciones, comparación de pobleciones). Actividades vinculadas: Cuestionario Estadística Dedicación: 13h Grupo grande/Teoría: 13h 5. Procesos Estocásticos Descripción: Introducción a los procesos estocásticos. Funciones de distribución y de densidad de un proceso estocástico. Valor medio, autocorrelación y autocovarianza. Procesos estocásticos estacionarios en sentido estricto y en sentido amplio. Procesos estocásticos gaussianos. el proceso de Poisson. Oscilaciones aleatorias. Actividades vinculadas: Cuestionario Procesos Estocásticos Dedicación: 10h Grupo grande/Teoría: 10h'}

## 5. Modelado Matemático y Fórmulas Clave (LaTeX)
### 5.1 Teorema de Bayes
$$
P(A|B) = \frac{P(B|A) P(A)}{P(B)} = \frac{P(B|A) P(A)}{\sum_k P(B|A_k) P(A_k)}
$$

### 5.2 Distribución Gaussiana Normal
$$
f_X(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

### 5.3 Teorema de Wiener-Khinchin
$$
S_{xx}(f) = \mathcal{F}\{R_{xx}(\tau)\} = \int_{-\infty}^{\infty} R_{xx}(\tau) e^{-j 2\pi f \tau} d\tau
$$

### 5.4 Filtrado LTI de Procesos WSS
$$
S_{yy}(f) = |H(f)|^2 S_{xx}(f)
$$

### 5.5 Coeficiente de Correlación de Pearson
$$
\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \in [-1, 1]
$$

## 6. Banco de Ensayos / Laboratorio Virtual
```spice
* PPE - Simulacion de Ruido Blanco Termico de Resistencia
R1 in out 10k
C1 out 0 10nF
.noise V(out) R1 dec 20 100 100k
.print noise onoise inoise
.end
```

## 7. Preguntas de Autoevaluación y Examen con Justificación Técnica
#### Pregunta 1
**¿El Teorema de Wiener-Khinchin establece que la densidad espectral de potencia (PSD) de un proceso WSS es la transformada de Fourier de su autocorrelación?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Sxx(f) = F{Rxx(tau)}.

#### Pregunta 2
**¿Si dos variables aleatorias son independientes, su covarianza y su correlación son estrictamente cero?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. La independencia implica incorrelación.

#### Pregunta 3
**La función de autocorrelación R_xx(tau) de un proceso WSS alcanza su máximo valor en el infinito.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Su valor máximo absoluto se encuentra siempre en el origen: |R_xx(tau)| <= R_xx(0).

#### Pregunta 4
**¿El Teorema Central del Límite establece que la suma de un gran número de variables independientes e idénticamente distribuidas tiende asintóticamente a una distribución Gaussiana?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Pilar fundamental de la teoría de la probabilidad y del análisis de ruido.

#### Pregunta 5
**La varianza de una variable aleatoria puede tomar valores negativos si la media es negativa.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Por definición Var(X) = E[(X - mu)^2] >= 0; es siempre no negativa.

#### Pregunta 6
**¿Cuando un proceso WSS con densidad Sxx(f) pasa por un filtro LTI con respuesta H(f), la densidad espectral de salida es Syy(f) = |H(f)|^2 * Sxx(f)?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Relación espectral fundamental para sistemas lineales.

#### Pregunta 7
**¿La densidad espectral de un ruido blanco ideal es constante e idéntica en todas las frecuencias (S_w(f) = N0 / 2)?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. De ahí el nombre 'blanco', por analogía con la luz blanca que contiene todas las frecuencias con igual energía.

#### Pregunta 8
**La función de distribución acumulada F_X(x) = P(X <= x) es siempre una función monótona no decreciente que varía entre 0 y 1.**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Propiedad axiomática de toda variable aleatoria.

#### Pregunta 9
**¿Para dos eventos independientes A y B, la probabilidad de su intersección es P(A y B) = P(A) * P(B)?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Definición formal de independencia probabilística.

#### Pregunta 10
**Un proceso estocástico ergódico en la media tiene un promedio temporal diferente a su esperanza estadística de conjunto.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. En un proceso ergódico, el promedio temporal sobre una realización coincide con el promedio estadístico de conjunto.

#### Pregunta 11
**¿La integral de menos infinito a más infinito de una función de densidad de probabilidad (PDF) es siempre exactamente 1?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Condición de normalización del espacio de probabilidad.

#### Pregunta 12
**¿El coeficiente de correlación de Pearson rho_XY está rigurosamente acotado en el intervalo [-1, +1]?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Desigualdad de Cauchy-Schwarz.

## 8. Sistema de Evaluación y Bibliografía Recomendada
**Evaluación**: Cualquier acto de fraude académico, plagio o uso o mera tenencia al alcance de medios no autorizados en cualquier actividad de
evaluación comportará la calificación de cero (0) en la prueba o entrega afectada. Además, de acuerdo con la normativa de la
Universidad, la posible derivación de los hechos para la apertura de un expediente disciplinario implicará que la asignatura quede en
el estado provisional de "pendiente de evaluación" hasta la resolución del expediente. La gestión de estas incidencias se lleva a cabo
de acuerdo con el Marco de actuación para la integridad académica en la evaluación de la UPC.
Qüestionaris quinzenals 10%
Exámenes parciales: 40%
Examen final: 50%

**Bibliografía de Referencia**:
- - Leon-Garcia, A. Probability, statistics and random processes for electrical engineering. 3rd ed. Upper Saddle River, NJ: Pearson
- Education, 2009. ISBN 9780137155606.
- - Ross, S.M. Introduction to probability and statistics for engineers and scientists. 5th ed. Oxford: Academic Press, 2014. ISBN
- 9780123948113.
- Complementaria: