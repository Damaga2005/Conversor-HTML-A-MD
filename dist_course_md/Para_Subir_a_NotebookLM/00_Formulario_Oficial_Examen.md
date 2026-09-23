# 📐 Formulario Oficial de Examen · Sistemes de Mesura
> 🏛️ **Universitat Politècnica de Catalunya (UPC · EEBE)**  
> 📚 **Guía Rápida de Ecuaciones, Leyes Físicas y Criterios de Diseño (Temas 1 al 10)**  
> ⚡ **Formato optimizado para NotebookLM, consulta en pantalla y preparación de examen**

---

## 📑 Índice de Bloques Temáticos
1. [Tema 1: Características Estáticas y Dinámicas de Sensores](#tema-1-características-estáticas-y-dinámicas-de-sensores)
2. [Tema 2: Puentes de Medida (Wheatstone y Variantes)](#tema-2-puentes-de-medida-wheatstone-y-variantes)
3. [Tema 3: Amplificación y Acondicionamiento de Señal (INA)](#tema-3-amplificación-y-acondicionamiento-de-señal-ina)
4. [Tema 4: Ruido e Interferencias en Instrumentación](#tema-4-ruido-e-interferencias-en-instrumentación)
5. [Tema 5 y 6: Filtros Analógicos Activos y Respuesta Temporal](#tema-5-y-6-filtros-analógicos-activos-y-respuesta-temporal)
6. [Tema 7: Convertidores Digital-Analógico (DAC)](#tema-7-convertidores-digital-analógico-dac)
7. [Tema 8: Convertidores Analógico-Digital (ADC)](#tema-8-convertidores-analógico-digital-adc)
8. [Tema 9: Muestreo y Retención (Sample & Hold)](#tema-9-muestreo-y-retención-sample--hold)
9. [Tema 10: Calibración, Linealización e Incertidumbre (GUM)](#tema-10-calibración-linealización-e-incertidumbre-gum)

---

## Tema 1: Características Estáticas y Dinámicas de Sensores

### 1.1 Sensibilidad Estática
$$\begin{equation}
S = \frac{dy}{dx} \quad \text{o} \quad S_0 = \left. \frac{dy}{dx} \right|_{x_0}
\end{equation}$$
- Para respuesta lineal: $y = S \cdot x + y_0$.
- Unidades: $[\text{Unidades de Salida}] / [\text{Unidades de Entrada}]$.

### 1.2 Errores Estáticos
- **Error Absoluto:**
  $$\begin{equation}
  e_a = y_{\text{mesurat}} - y_{\text{patró}}
  \end{equation}$$
- **Error Relativo:**
  $$\begin{equation}
  e_r = \frac{y_{\text{mesurat}} - y_{\text{patró}}}{y_{\text{patró}}} \times 100\%
  \end{equation}$$
- **No-Linealidad respecto al Fondo de Escala (FSR):**
  $$\begin{equation}
  \varepsilon_{NL} = \frac{\max |y_i - y_{\text{lin},i}|}{\text{FSR}} \times 100\%
  \end{equation}$$
- **Histéresis Máxima:**
  $$\begin{equation}
  H_{\max} = \frac{\max |y_{\text{pujada}} - y_{\text{baixada}}|}{\text{FSR}} \times 100\%
  \end{equation}$$

### 1.3 Sensores Resistivos de Temperatura
- **RTD (Pt100, aproximación lineal en rango industrial):**
  $$\begin{equation}
  R(T) = R_0 \left( 1 + \alpha \Delta T \right) \quad \text{con } \alpha \approx 3.85 \times 10^{-3} \text{ }^\circ\text{C}^{-1}
  \end{equation}$$
- **Termistor NTC (Ecuación Exponencial simplificada):**
  $$\begin{equation}
  R(T) = R_0 \exp\left[ \beta \left( \frac{1}{T} - \frac{1}{T_0} \right) \right], \quad \alpha = \frac{1}{R} \frac{dR}{dT} = -\frac{\beta}{T^2}
  \end{equation}$$
  *(Temperaturas siempre en Kelvin en la formulación de $\beta$)*.

### 1.4 Galgas Extensométricas (Strain Gauges)
- **Factor de Galga ($K$ o $GF$):**
  $$\begin{equation}
  K = \frac{\Delta R / R}{\varepsilon} = 1 + 2\nu + \frac{\Delta \rho / \rho}{\varepsilon}
  \end{equation}$$
  - Metálicas: $K \approx 2.0$ a $2.1$ (predomina cambio geométrico con coeficiente de Poisson $\nu$).
  - Semiconductoras (Piezorresistivas): $K \approx 100$ a $150$ (predomina efecto piezorresistivo $\Delta \rho / \rho$).

---

## Tema 2: Puentes de Medida (Wheatstone y Variantes)

### 2.1 Ecuación General del Puente de Wheatstone
$$\begin{equation}
V_o = V_s \left( \frac{R_1}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)
\end{equation}$$
- **Condición de Equilibrio ($V_o = 0$):**
  $$\begin{equation}
  R_1 R_3 = R_2 R_4
  \end{equation}$$

### 2.2 Configuraciones con Sensores Piezorresistivos / Galgas
| Configuración | Galgas Activas | Tensión de Salida $V_o$ | Linealidad | Compensación Térmica |
| :--- | :---: | :---: | :---: | :---: |
| **Cuarto de Puente (1/4)** | 1 ($R_1 = R + \Delta R$) | $$V_o \approx \frac{V_s}{4} \frac{\Delta R}{R}$$ | No lineal (error $\approx \frac{1}{2} \frac{\Delta R}{R}$) | Requiere galga ficticia dummy |
| **Medio Puente Push-Pull (1/2)** | 2 ($R_1=R+\Delta R, R_2=R-\Delta R$) | $$V_o = \frac{V_s}{2} \frac{\Delta R}{R}$$ | **Exactamente lineal** | Excelente ($\Delta T$ idéntica) |
| **Puente Completo (4/4)** | 4 (flexión o tracción/comp.) | $$V_o = V_s \frac{\Delta R}{R}$$ | **Exactamente lineal** ($4\times$ sensibilidad) | Total intrínseca |

---

## Tema 3: Amplificación y Acondicionamiento de Señal (INA)

### 3.1 Amplificador de Instrumentación Clásico (3 Operacionales)
$$\begin{equation}
V_o = \left( 1 + \frac{2 R_1}{R_g} \right) \frac{R_3}{R_2} (V_2 - V_1)
\end{equation}$$
- **Ganancia Diferencial ($G_d$)** fijada por una única resistencia $R_g$:
  $$\begin{equation}
  G_d = 1 + \frac{2 R_1}{R_g} \quad (\text{cuando } R_3 = R_2)
  \end{equation}$$
- Impedancia de entrada diferencial y en modo común: extremadamente elevada ($> 10^9 \,\Omega$).

### 3.2 Relación de Rechazo en Modo Común (CMRR)
$$\begin{equation}
\text{CMRR} = \left| \frac{A_d}{A_{cm}} \right|, \quad \text{CMRR}_{\text{dB}} = 20 \log_{10} \left| \frac{A_d}{A_{cm}} \right|
\end{equation}$$
- **Efecto de la Tolerancia de las Resistencias ($\delta = \Delta R / R$):**
  $$\begin{equation}
  \text{CMRR}_{\text{peor caso}} \approx \frac{1 + G_1}{4 \delta}
  \end{equation}$$
  *(Con resistencias al 1% ($\delta=0.01$), el CMRR de la etapa diferencial cae a $\approx 54\text{ dB}$ si $G_1=1$)*.

---

## Tema 4: Ruido e Interferencias en Instrumentación

### 4.1 Fuentes de Ruido Físico Intrínseco
- **Ruido Térmico Johnson-Nyquist (en cualquier resistencia $R$):**
  $$\begin{equation}
  v_n = \sqrt{4 k_B T R \Delta f} \quad (\text{V}_{\text{rms}}), \quad e_n = \sqrt{4 k_B T R} \quad (\text{V}/\sqrt{\text{Hz}})
  \end{equation}$$
  - Constante de Boltzmann: $k_B \approx 1.38 \times 10^{-23} \text{ J/K}$.
  - A $T = 300\text{ K}$ ($27^\circ\text{C}$): $e_n \approx 4 \sqrt{R\,(\text{k}\Omega)} \text{ nV}/\sqrt{\text{Hz}}$.
- **Ruido de Disparo (Shot Noise en uniones PN con corriente continua $I_{DC}$):**
  $$\begin{equation}
  i_{sh} = \sqrt{2 q I_{DC} \Delta f} \quad (\text{A}_{\text{rms}}), \quad q \approx 1.602 \times 10^{-19} \text{ C}
  \end{equation}$$
- **Suma Cuadrática de Fuentes de Ruido Incorreladas:**
  $$\begin{equation}
  v_{n,\text{total}} = \sqrt{v_{n1}^2 + v_{n2}^2 + \dots + v_{nk}^2}
  \end{equation}$$

### 4.2 Factor y Figura de Ruido
$$\begin{equation}
F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}}, \quad \text{NF} = 10 \log_{10} F \quad (\text{dB})
\end{equation}$$

---

## Tema 5 y 6: Filtros Analógicos Activos y Respuesta Temporal

### 5.1 Función de Transferencia y Atenuación
- **Filtro Butterworth (Respuesta Máximamente Plana en banda de paso):**
  $$\begin{equation}
  |H(j\omega)| = \frac{1}{\sqrt{1 + \left( \frac{\omega}{\omega_c} \right)^{2n}}}
  \end{equation}$$
  - Pendiente en banda atenuada (Roll-off): $-20n \text{ dB/década}$ o $-6n \text{ dB/octava}$.
- **Filtro Chebyshev:** Mayor pendiente de transición a costa de rizado (ripple) $\varepsilon$ en banda pasante.
- **Filtro Bessel:** Retardo de grupo $\tau_g(\omega) = -\frac{d\phi}{d\omega} \approx \text{cte}$, respuesta transitoria sin sobreoscilación.

### 5.2 Celda Sallen-Key Pasa-Bajos de 2º Orden
$$\begin{equation}
f_0 = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}, \quad Q = \frac{\sqrt{R_1 R_2 C_1 C_2}}{C_2(R_1 + R_2)}
\end{equation}$$

---

## Tema 7: Convertidores Digital-Analógico (DAC)

### 7.1 Relación de Entrada/Salida
$$\begin{equation}
V_o = V_{\text{ref}} \sum_{i=1}^{N} b_i 2^{-i} = \frac{V_{\text{ref}}}{2^N} \times D
\end{equation}$$
- **Peso del Bit Menos Significativo (LSB):**
  $$\begin{equation}
  1 \text{ LSB} = \frac{V_{\text{ref}}}{2^N}
  \end{equation}$$
- **Tensión de Fondo de Escala Real (Full Scale Range):**
  $$\begin{equation}
  V_{FS} = V_{\text{ref}} \left( 1 - 2^{-N} \right) = V_{\text{ref}} - 1 \text{ LSB}
  \end{equation}$$

### 7.2 Métricas de Linealidad
- **DNL (No Linealidad Diferencial):** Condición de monotonicidad estricta: $|\text{DNL}| < 1 \text{ LSB}$.
- **INL (No Linealidad Integral):** Desviación máxima respecto a la recta ideal o recta de ajuste.

---

## Tema 8: Convertidores Analógico-Digital (ADC)

### 8.1 Criterio de Nyquist-Shannon y Aliasing
$$\begin{equation}
f_s \ge 2 f_{\max}
\end{equation}$$
- El filtro antialiasing analógico previo debe garantizar una atenuación de al menos $6.02N\text{ dB}$ en $f = f_s - f_{\max}$.

### 8.2 Ruido de Cuantificación y Relación Señal/Ruido Teórica (SNR)
- **Paso de Cuantificación (Quantum $q$):**
  $$\begin{equation}
  q = \frac{V_{\text{FSR}}}{2^N}
  \end{equation}$$
- **Varianza del Error de Cuantificación (suponiendo distribución uniforme en $[-q/2, +q/2]$):**
  $$\begin{equation}
  \sigma_q^2 = \frac{q^2}{12} \quad \implies \quad v_{q,\text{rms}} = \frac{q}{\sqrt{12}}
  \end{equation}$$
- **Relación Señal/Ruido Máxima (Señal senoidal a fondo de escala):**
  $$\begin{equation}
  \text{SNR}_{\max} = 6.02 N + 1.76 \quad (\text{dB})
  \end{equation}$$
- **Número Efectivo de Bits (ENOB):**
  $$\begin{equation}
  \text{ENOB} = \frac{\text{SINAD}_{\text{dB}} - 1.76}{6.02}
  \end{equation}$$

---

## Tema 9: Muestreo y Retención (Sample & Hold)

### 9.1 Aperture Jitter (Incertidumbre de Tiempo de Muestreo)
$$\begin{equation}
\Delta V = \left. \frac{dv(t)}{dt} \right|_{\max} \Delta t_a = 2\pi f_{\max} V_{\text{peak}} \Delta t_a
\end{equation}$$
- **Condición para que el error de apertura no supere $1/2\text{ LSB}$:**
  $$\begin{equation}
  \Delta t_a < \frac{1}{2\pi f_{\max} 2^N}
  \end{equation}$$

### 9.2 Caída de Retención (Droop Rate)
$$\begin{equation}
\frac{dV_H}{dt} = \frac{I_{\text{fuga}}}{C_H}
\end{equation}$$

---

## Tema 10: Calibración, Linealización e Incertidumbre (GUM)

### 10.1 Ley de Propagación de Incertidumbres Combinadas (Variables Incorreladas)
$$\begin{equation}
u_c^2(y) = \sum_{i=1}^{n} c_i^2 u^2(x_i) = \sum_{i=1}^{n} \left( \frac{\partial f}{\partial x_i} \right)^2 u^2(x_i)
\end{equation}$$
- Coeficientes de sensibilidad: $c_i = \frac{\partial f}{\partial x_i}$.

### 10.2 Evaluación de Incertidumbres Estándar
- **Tipo A (Estadística de $n$ mediciones repetidas):**
  $$\begin{equation}
  u(x) = \frac{s(x)}{\sqrt{n}} = \sqrt{\frac{\sum_{j=1}^n (x_j - \bar{x})^2}{n(n - 1)}}
  \end{equation}$$
- **Tipo B (Distribución Rectangular / Uniforme de semi-anchura $a$):**
  $$\begin{equation}
  u(x) = \frac{a}{\sqrt{3}}
  \end{equation}$$
- **Tipo B (Distribución Triangular):**
  $$\begin{equation}
  u(x) = \frac{a}{\sqrt{6}}
  \end{equation}$$
- **Incertidumbre Expandida ($U$):**
  $$\begin{equation}
  U = k \cdot u_c(y) \quad (k=2 \text{ para } 95.45\% \text{ de nivel de confianza})
  \end{equation}$$

---

## Tema 11: Instrumentación Industrial y Técnicas Avanzadas de Medida

### 11.1 Amplificador de Aislamiento Galvánico (ISO124)
- **Rechazo de Modo Común de Aislamiento (IMRR):**
  $$\begin{equation}
  \text{IMRR}_{\text{dB}} = 20 \log_{10} \left( \frac{V_{\text{ISO}}}{V_{\text{error\_out}}} \right)
  \end{equation}$$
- **Tensión de barrera dieléctrica:** $V_{\text{ISO}} \le 1500\text{ V}_{\text{rms}}$ continua (acoplo capacitivo diferencial modulado).
- **Relación de transferencia unitaria:** $V_o = 1.000 \cdot V_{in} + V_{os,\text{iso}}$.

### 11.2 Demodulador Coherente Síncrono (Lock-In PSD)
- **Multiplicación Analógica de Señal y Referencia:**
  $$\begin{equation}
  v_m(t) = \left[ V_s \cos(\omega_0 t + \theta) + n(t) \right] \cdot \left[ V_r \cos(\omega_0 t + \phi) \right]
  \end{equation}$$
- **Salida Continua DC tras Filtro Paso Bajo Integrador ($f_c \ll \omega_0$):**
  $$\begin{equation}
  V_{\text{PSD}} = \frac{1}{2} V_s V_r \cos(\theta - \phi) = \frac{1}{2} V_s V_r \cos(\Delta \phi)
  \end{equation}$$
- **Mejora de Relación Señal/Ruido (SNR):**
  $$\begin{equation}
  \Delta \text{SNR}_{\text{dB}} \approx 10 \log_{10}\left(\frac{\Delta f_{\text{in}}}{B_{\text{LPF}}}\right)
  \end{equation}$$

### 11.3 Bucle de Corriente Industrial 4-20 mA (Transmisor a 2 Hilos)
- **Ecuación de Conversión Lineal (Cero Vivo / Live Zero):**
  $$\begin{equation}
  I_{\text{loop}} = 4\text{ mA} + 16\text{ mA} \cdot \left( \frac{T - T_{\min}}{T_{\max} - T_{\min}} \right)
  \end{equation}$$
- **Resistencia Máxima de Carga admisible (Loop Compliance):**
  $$\begin{equation}
  R_{L,\max} = \frac{V_{\text{fuente}} - V_{\text{tx},\min}}{I_{\max}} = \frac{V_{\text{fuente}} - 12\text{ V}}{20\text{ mA}}
  \end{equation}$$
- **Diagnóstico de Fallos según Estándar NAMUR NE43:**
  - $I_{\text{loop}} < 3.6\text{ mA}$ $\rightarrow$ Rotura de cable o fallo en sensor (circuito abierto).
  - $I_{\text{loop}} > 21.0\text{ mA}$ $\rightarrow$ Cortocircuito o saturación destructiva.

### 11.4 Roseta de Galgas Extensiométricas a 45° & Círculo de Mohr
- **Lectura de Galgas:** $\epsilon_a$ (a $0^\circ$), $\epsilon_b$ (a $45^\circ$), $\epsilon_c$ (a $90^\circ$).
- **Deformación Media (Centro de Mohr):**
  $$\begin{equation}
  \epsilon_{\text{avg}} = \frac{\epsilon_a + \epsilon_c}{2}
  \end{equation}$$
- **Radio de Mohr y Deformación de Cizalladura Máxima ($\gamma_{\max}$):**
  $$\begin{equation}
  R_{\text{Mohr}} = \frac{1}{\sqrt{2}} \sqrt{(\epsilon_a - \epsilon_b)^2 + (\epsilon_b - \epsilon_c)^2}, \quad \gamma_{\max} = 2 R_{\text{Mohr}}
  \end{equation}$$
- **Deformaciones Principales Biaxiales:**
  $$\begin{equation}
  \epsilon_1 = \epsilon_{\text{avg}} + R_{\text{Mohr}}, \quad \epsilon_2 = \epsilon_{\text{avg}} - R_{\text{Mohr}}
  \end{equation}$$
- **Orientación de los Planos Principales:**
  $$\begin{equation}
  \theta_p = \frac{1}{2} \arctan \left( \frac{2\epsilon_b - \epsilon_a - \epsilon_c}{\epsilon_a - \epsilon_c} \right)
  \end{equation}$$

---
> 💡 **Consejo para NotebookLM:** Sube este documento como fuente prioritaria bajo el nombre `_Formulario_Oficial_Examen.md`. Cuando le pidas al modelo resolver problemas numéricos del examen, dile: *"Usa las fórmulas y constantes del Formulario Oficial para deducir y comprobar los resultados numéricos"*.

