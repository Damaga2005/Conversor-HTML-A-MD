# 230900 - Componentes y Circuitos Electrónicos (CCE)
**Grado en Ingeniería Electrónica de Telecomunicación (GREELEC)**  
*Escuela Técnica Superior de Ingeniería de Telecomunicación de Barcelona (ETSETB - UPC)*

## 1. Ficha Técnica y Metadatos Oficiales
- **Código UPC**: `230900`
- **Acrónimo Oficial**: `CCE`
- **Semestre**: Q1 (Fase Inicial)
- **Créditos ECTS**: 6.0 ECTS (150)
- **Departamento Responsable**: 710 - EEL - Departamento de Ingeniería Electrónica
- **Profesorado / Coordinación**: ALBERTO ORPELLA GARCIA
- **Guía Docente Oficial en PDF**: [230900_guia_docent.pdf](https://www.upc.edu/grau/guiadocent/pdf/esp/230900/componentes-y-circuitos-electronicos.pdf)

## 2. Descripción General y Requisitos
Variables eléctricas, KCL, KVL, teoremas de Thévenin/Norton, máxima transferencia de potencia, diodos semiconductores, transistores BJT y amplificadores operacionales en régimen lineal.

## 3. Objetivos de Aprendizaje y Competencias
- A
- p
- r
- e
- n
- d
- e
- r
-  
- a
-  
- a
- n
- a
- l
- i
- z
- a
- r
-  
- c
- i
- r
- c
- u
- i
- t
- o
- s
-  
- l
- i
- n
- e
- a
- l
- e
- s
-  
- b
- à
- s
- i
- c
- o
- s
-  
- u
- t
- i
- l
- i
- z
- a
- n
- d
- o
-  
- l
- o
- s
-  
- d
- i
- f
- e
- r
- e
- n
- t
- e
- s
-  
- m
- é
- t
- o
- d
- o
- s
-  
- p
- o
- s
- i
- b
- l
- e
- s
- .
-  
- E
- n
- t
- e
- n
- d
- e
- r
-  
- e
- l
-  
- f
- u
- n
- c
- i
- o
- n
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
- l
- o
- s
-  
- e
- l
- e
- m
- e
- n
- t
- o
- s
- 

- n
- o
-  
- l
- i
- n
- e
- a
- l
- e
- s
- :
-  
- d
- i
- o
- d
- o
- ,
-  
- t
- r
- a
- n
- s
- i
- s
- t
- o
- r
-  
- b
- i
- p
- o
- l
- a
- r
-  
- y
-  
- a
- m
- p
- l
- i
- f
- i
- c
- a
- d
- o
- r
-  
- o
- p
- e
- r
- a
- c
- i
- o
- n
- a
- l
- .
-  
- E
- s
- t
- u
- d
- i
- a
- r
-  
- s
- u
- s
-  
- c
- i
- r
- c
- u
- i
- t
- o
- s
-  
- e
- q
- u
- i
- v
- a
- l
- e
- n
- t
- e
- s
- ,
-  
- y
-  
- a
- p
- r
- e
- n
- d
- e
- r
-  
- a
-  
- a
- n
- a
- l
- i
- z
- a
- r
-  
- l
- o
- s
-  
- c
- i
- r
- c
- u
- i
- t
- o
- s
- 

- b
- á
- s
- i
- c
- o
- s
-  
- u
- t
- i
- l
- i
- z
- a
- n
- d
- o
-  
- e
- s
- t
- o
- s
-  
- m
- o
- d
- e
- l
- o
- s
- .

## 4. Temario y Unidades de Contenido
- {'title': 'Tema 1. Introducción a los circuitos electrónicos', 'description': 'Variables eléctricas: Diferencia de potencial, intensidad de la corriente, potencia. Concepto de circuito. Leyes de Kirchhoff de las corrientes (KCL) y de las tensiones (KVL). Elementos circuitales básicos. Características tensión-corriente.'}
- {'title': 'Tema 2. Circuitos resistivos. Técnicas de simplificación', 'description': 'Concepto de circuito equivalente. Elementos en serie y paralelo. Resistencias y fuentes en serie y en paralelo. Divisor de tensión y corriente. Elementos superfluos. Efectos de carga. Reducción de circuits.'}
- {'title': 'Tema 3. Métodos sistemáticos de análisis circuital', 'description': 'Análisis por tensiones de nodo. Análisis por corrientes de malla. Ejemplos'}
- {'title': 'Tema 4. Teoremas de circuitos lineales', 'description': 'Concepto de linealidad. Teorema de superposición. Circuitos equivalentes de Thevenin y de Norton. Transferencia de señal. Máxima transferencia de potencia.'}
- {'title': 'Tema 5. Introducción al modelado de componentes electrónicos. Aplicaciones', 'description': 'Diodo: Diodo ideal. Modelo exponencial y lineal a tramos. Análisis de circuitos con diodos. Transistor bipolar NPN: Características de entrada y de salida. Zonas de funcionamiento y circuitos equivalentes. Análisis de circuitos con transistor bipolar. Amplificador operacional: Amplificador operacional ideal. Característica de salida y zonas de funcionamiento. Circuitos equivalentes. Análisis básico de circuitos con amplificadores operacionales ideales.'}

## 5. Modelado Matemático y Fórmulas Clave (LaTeX)
### 5.1 Leyes de Kirchhoff
$$
\sum I_{k} = 0 \text{ (KCL)}, \quad \sum V_{k} = 0 \text{ (KVL)}
$$

### 5.2 Divisor de Tensión Resistivo
$$
V_o = V_s \cdot \frac{R_2}{R_1 + R_2}
$$

### 5.3 Resistencia de Thévenin
$$
R_{th} = \frac{V_{oc}}{I_{sc}}
$$

### 5.4 Máxima Transferencia de Potencia
$$
R_L = R_{th} \implies P_{max} = \frac{V_{th}^2}{4 R_{th}}
$$

### 5.5 Ecuación de Shockley del Diodo
$$
I_D = I_s \left( e^{V_D / (n V_T)} - 1 \right)
$$

## 6. Banco de Ensayos / Laboratorio Virtual
```spice
* CCE - Divisor Thevenin y Diodo de Union
Vs in 0 DC 10V
R1 in out 1k
R2 out 0 2k
D1 out load 1N4148
RL load 0 1k
.model 1N4148 D(Is=2.52n Rs=0.568 N=1.752)
.dc Vs 0 15 0.1
.print dc V(out) V(load) I(RL)
.end
```

## 7. Preguntas de Autoevaluación y Examen con Justificación Técnica
#### Pregunta 1
**¿El teorema de máxima transferencia de potencia establece que la carga debe ser igual a Rth para maximizar la potencia disipada?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Al derivar P_L respecto a R_L e igualar a cero se obtiene R_L = R_th.

#### Pregunta 2
**¿El principio de superposición es aplicable al cálculo directo de potencias?**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. La potencia es cuadrática (P = I^2*R); solo se pueden superponer tensiones y corrientes.

#### Pregunta 3
**En un divisor de tensión con R1=1k y R2=3k alimentado a 12V, la tensión en bornes de R2 es 9V.**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Vo = 12 * (3 / (1 + 3)) = 9.0 V.

#### Pregunta 4
**¿La caída de tensión típica en directa de un diodo de silicio es de aproximadamente 0.7 V?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Debido al potencial de contacto y la banda prohibida del silicio a 300 K.

#### Pregunta 5
**Si un circuito lineal tiene Voc = 10V y Isc = 2A, su resistencia de Thévenin es de 20 ohms.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Rth = Voc / Isc = 10V / 2A = 5 ohms.

#### Pregunta 6
**¿La ley de corrientes de Kirchhoff (KCL) se fundamenta en la conservación de la carga eléctrica?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. En régimen cuasiestacionario la carga neta en cualquier nodo cerrado permanece constante.

#### Pregunta 7
**¿La ley de tensiones de Kirchhoff (KVL) se fundamenta en el carácter conservativo del campo electrostático?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. La integral de línea del campo eléctrico sobre un lazo cerrado es nula.

#### Pregunta 8
**En un transistor BJT en zona activa directa, la corriente de colector Ic depende fuertemente de Vce.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Ic = beta * Ib y es casi independiente de Vce (salvo por el efecto Early secundario).

#### Pregunta 9
**¿La resistencia dinámica de pequeña señal de un diodo polarizado con ID0 es rd = VT / ID0?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Derivando la ecuación de Shockley dVD/dID = VT / ID0.

#### Pregunta 10
**¿Un amplificador operacional ideal con realimentación negativa mantiene un cortocircuito virtual entre sus entradas?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Como Aol -> infinito, (V+ - V-) = Vo / Aol = 0.

#### Pregunta 11
**La resistencia equivalente de dos resistencias idénticas R en paralelo es 2R.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. R_eq = (R * R) / (R + R) = R / 2.

#### Pregunta 12
**¿El nudo de referencia o masa se define arbitrariamente con potencial de 0 voltios?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Sirve de origen de potenciales para todo el circuito.

## 8. Sistema de Evaluación y Bibliografía Recomendada
**Evaluación**: Cualquier acto de fraude académico, plagio o uso o mera tenencia al alcance de medios no autorizados en cualquier actividad de
evaluación comportará la calificación de cero (0) en la prueba o entrega afectada. Además, de acuerdo con la normativa de la
Universidad, la posible derivación de los hechos para la apertura de un expediente disciplinario implicará que la asignatura quede en
el estado provisional de "pendiente de evaluación" hasta la resolución del expediente. La gestión de estas incidencias se lleva a cabo
de acuerdo con el Marco de actuación para la integridad académica en la evaluación de la UPC.
Nota de laboratorio (LAB): 10%
Problemas y actividades a casa (PRO): 10%
Examen parcial de teoría durante el curso (EXPAR): 30%
Examen final de teoría (EXFIN): 50%
La nota final (NF) es la mayor de las dos cantidades:
NF = 0,1*LAB + 0,1*PROB + 0,3*EXPAR + 0,5*EXFIN , o bien
NF = 0,1*LAB + 0,1*PROB + 0,8*EXFIN , si el resultado de esta expresión es mayor que la anterior.
Solamente es reevaluable la parte de teoría de la asignatura con un peso del 90%. La nota de laboratorio se conservará de la
evaluación anterior con un peso del 10%.

**Bibliografía de Referencia**:
- - Thomas, R.E.; Rosa, A.J.; Toussaint, G.J. The analysis and design of linear circuits. 7th ed. Hoboken, NJ: John Wiley & Sons, 2012.
- ISBN 9781118065587.
- - Prat, L.; Bragós, R. Circuits i dispositius electrònics: fonaments d'electrònica. 2a ed. Barcelona: Edicions UPC, 2002. ISBN
- 8483015749.