# 🎓 Exámenes Finales Oficiales Resueltos · Sistemes de Mesura (UPC)
> 🏛️ **Universitat Politècnica de Catalunya (UPC · EEBE / ETSETB)**  
> 👨‍🏫 **Profesores:** Miguel Ángel García González y Juan José Ramos Castro  
> 📚 **Asignatura:** SISTEMES DE MESURA (230920)  
> ⚡ **Documento Maestro con Enunciados Íntegros y Resoluciones Oficiales Paso a Paso en $\LaTeX$**  
> 🎯 **Convocatorias Incluidas:** Enero 2021, Enero 2024 y Enero 2025

---

## 📑 Tabla de Contenidos

1. [Convocatoria 1: Examen Final del 8 de enero de 2021](#convocatoria-1-examen-final-del-8-de-enero-de-2021)
   - [Problema 1: Tiempo de Subida en Osciloscopio y Compensación de Sonda Pasiva 10x](#problema-1-tiempo-de-subida-en-osciloscopio-y-compensación-de-sonda-pasiva-10x)
   - [Problema 2: Termopar Tipo K con Compensación de Unión Fría (Pt100) y AD623](#problema-2-termopar-tipo-k-con-compensación-de-unión-fría-pt100-y-ad623)
   - [Problema 3: Oscilador para Sensor Capacitivo y Presupuesto de Incertidumbre GUM](#problema-3-oscilador-para-sensor-capacitivo-y-presupuesto-de-incertidumbre-gum)
2. [Convocatoria 2: Examen Final del 16 de enero de 2024](#convocatoria-2-examen-final-del-16-de-enero-de-2024)
   - [Problema 1: Análisis Estadístico de Mediciones (Criterio de Chauvenet, Autocorrelación e Incertidumbre GUM)](#problema-1-análisis-estadístico-de-mediciones-criterio-de-chauvenet-autocorrelación-e-incertidumbre-gum)
   - [Problema 2: Acondicionador Lineal para Sensor Capacitivo con OPA134 e Interferencias (PSRR, Red 230V)](#problema-2-acondicionador-lineal-para-sensor-capacitivo-con-opa134-e-interferencias-psrr-red-230v)
   - [Problema 3: Termopar Tipo K con Linealización de NTC (Taylor), AD620 y Ruido 1/f](#problema-3-termopar-tipo-k-con-linealización-de-ntc-taylor-ad620-y-ruido-1f)
3. [Convocatoria 3: Examen Final del 14 de enero de 2025](#convocatoria-3-examen-final-del-14-de-enero-de-2025)
   - [Ejercicios Cortos (30%): Aislamiento, TIA en Red T, Célula de Carga y Lazo 4-20 mA](#ejercicios-cortos-30-aislamiento-tia-en-red-t-célula-de-carga-y-lazo-4-20-ma)
   - [Problema 1 (35%): Sensor de Temperatura de Corriente AD590 y Presupuesto GUM Completo](#problema-1-35-sensor-de-temperatura-de-corriente-ad590-y-presupuesto-gum-completo)
   - [Problema 2 (35%): Termómetro Termopar Tipo J con Pt100 y Análisis de Ruido Flicker/Blanco](#problema-2-35-termómetro-termopar-tipo-j-con-pt100-y-análisis-de-ruido-flickerblanco)

---

# Convocatoria 1: Examen Final del 8 de enero de 2021
> **Profesor:** Miguel Ángel García González  
> **Asignatura:** Sistemas de Medida (230920) · UPC

---

## Problema 1: Tiempo de Subida en Osciloscopio y Compensación de Sonda Pasiva 10x

### Enunciado

Se conecta un generador de funciones con resistencia de salida $R_s = 50\,\Omega$ a un osciloscopio con impedancia de entrada $R_{osc} = 1\text{ M}\Omega \parallel C_{osc} = 13\text{ pF}$ empleando un cable coaxial de $1.5\text{ m}$ de longitud y capacidad entre vivo y malla de $75\text{ pF/m}$. El propósito de la medida es medir el tiempo de subida de la señal del generador entre el $10\%$ y el $90\%$. Debido a que la impedancia de entrada del osciloscopio no es infinita y que la resistencia de salida del generador no es nula, el tiempo de subida medido será superior al de circuito abierto.

```
       Rs = 50 Ω
Vin ───/\/\/\─────────┬───────────────┬─────────────── Vout
                      │               │
                     === Cc          === Cosc
                      │  112.5 pF     │  13 pF
                      │               │
                     GND             GND
                                      │
                                    [ Rosc = 1 MΩ ]
                                      │
                                     GND
```

**Se pide:**
1. Estime el tiempo mínimo de subida de la señal del generador para que el sesgo en la medida de dicho tiempo a la entrada del osciloscopio sea, como máximo, del $10\%$.
2. Como se pretende medir tiempos más rápidos, se emplea una sonda pasiva atenuadora por 10. En esta sonda, la punta tiene una resistencia $R_p = 9\text{ M}\Omega$ en paralelo con un condensador ajustable de valor $C_p$ y, tras la punta, la capacidad entre vivo y masa del cable de la sonda es $C_c = 125\text{ pF}$. El osciloscopio sigue teniendo $1\text{ M}\Omega \parallel 13\text{ pF}$. Indique el valor al que debe ajustarse $C_p$ para que la respuesta frecuencial sea un sistema paso bajo de primer orden.
3. Suponiendo ajustada la sonda a dicho valor de $C_p$, estime el tiempo mínimo de subida de la señal del generador para que el sesgo sea, como máximo, del $10\%$.

---

### Solución Oficial Paso a Paso

#### Apartado a: Medida Directa con Cable Coaxial
La capacidad total del cable es:
$$C_c = 1.5\text{ m} \times 75\text{ pF/m} = 112.5\text{ pF}$$

La función de transferencia del circuito formado por el generador ($R_s$), el cable ($C_c$) y el osciloscopio ($R_{osc} \parallel C_{osc}$) es:
$$H(s) = \frac{R_{osc} \parallel \frac{1}{(C_c + C_{osc})s}}{R_s + R_{osc} \parallel \frac{1}{(C_c + C_{osc})s}} = \frac{\frac{R_{osc}}{1 + R_{osc}(C_c + C_{osc})s}}{R_s + \frac{R_{osc}}{1 + R_{osc}(C_c + C_{osc})s}}$$

$$H(s) = \frac{R_{osc}}{R_{osc} + R_s + R_s R_{osc}(C_c + C_{osc})s} = \frac{R_{osc}}{R_{osc} + R_s} \cdot \frac{1}{1 + s (R_s \parallel R_{osc})(C_c + C_{osc})}$$

Como $R_s = 50\,\Omega \ll R_{osc} = 1\text{ M}\Omega$, se tiene $R_s \parallel R_{osc} \cong R_s = 50\,\Omega$.
La frecuencia de corte a $-3\text{ dB}$ es:
$$f_{-3\text{dB}} = \frac{1}{2\pi (R_s \parallel R_{osc})(C_c + C_{osc})} = \frac{1}{2\pi \cdot 50\,\Omega \cdot (112.5\text{ pF} + 13\text{ pF})} = \frac{1}{2\pi \cdot 50 \cdot 125.5 \times 10^{-12}} = 25.36\text{ MHz} \cong 25.4\text{ MHz}$$

El tiempo de subida $t_r$ medido por el osciloscopio se relaciona con el tiempo de subida real $t_r(V_{in})$ y el tiempo de respuesta propio del sistema mediante la suma cuadrática:
$$t_r(V_{out}) = \sqrt{t_r(V_{in})^2 + t_r(\text{sistema})^2} = \sqrt{t_r(V_{in})^2 + \left(\frac{\ln 9}{2\pi f_{-3\text{dB}}}\right)^2}$$

> **Nota:** $\ln 9 \cong 2.1972$. Por tanto, $\frac{\ln 9}{2\pi f_{-3\text{dB}}} \cong \frac{0.35}{f_{-3\text{dB}}}$.

Se exige que el sesgo no supere el $10\%$, es decir:
$$t_r(V_{out}) \le 1.1 \cdot t_{r,\min}(V_{in})$$
$$1.1 \cdot t_{r,\min}(V_{in}) = \sqrt{t_{r,\min}(V_{in})^2 + \left(\frac{\ln 9}{2\pi f_{-3\text{dB}}}\right)^2}$$

Elevando ambos miembros al cuadrado:
$$(1.1)^2 \cdot t_{r,\min}(V_{in})^2 = t_{r,\min}(V_{in})^2 + \left(\frac{\ln 9}{2\pi f_{-3\text{dB}}}\right)^2$$
$$(1.21 - 1) \cdot t_{r,\min}(V_{in})^2 = 0.21 \cdot t_{r,\min}(V_{in})^2 = \left(\frac{\ln 9}{2\pi f_{-3\text{dB}}}\right)^2$$
$$t_{r,\min}(V_{in}) = \frac{\ln 9}{2\pi f_{-3\text{dB}} \cdot \sqrt{0.21}} = \frac{2.1972}{2\pi \cdot 25.36 \times 10^6 \cdot 0.45826} = 30.04\text{ ns}$$

$$\mathbf{t_{r,\min}(V_{in}) = 30.04\text{ ns}}$$

---

#### Apartado b: Condición de Compensación de la Sonda Pasiva 10x
Para que el divisor de tensión frecuencial formado por la punta ($R_p \parallel C_p$) y la carga ($R_{osc} \parallel (C_{cable} + C_{osc})$) mantenga una atenuación constante e independiente de la frecuencia (cero que cancela el polo de la sonda), se debe cumplir la condición clásica de puente equilibrado:
$$R_p \cdot C_p = R_{osc} \cdot (C_c + C_{osc})$$
$$C_p = (C_c + C_{osc}) \cdot \frac{R_{osc}}{R_p} = (125\text{ pF} + 13\text{ pF}) \cdot \frac{1\text{ M}\Omega}{9\text{ M}\Omega} = 138\text{ pF} \cdot \frac{1}{9} = 15.33\text{ pF}$$

$$\mathbf{C_p = 15.33\text{ pF}}$$

---

#### Apartado c: Nuevo Tiempo de Subida con Sonda Compensada
Con la sonda compensada, el polo dominante del sistema ya no viene fijado por el cable largo de entrada, sino por la combinación de la impedancia equivalente vista desde la fuente $R_1 = 50\,\Omega$ y la capacidad equivalente $C_{eq} = C_c + C_{osc} = 138\text{ pF}$:
$$k = \frac{R_p}{C_{eq}}\left(\frac{1}{R_1 R_p} + \frac{1}{R_p R_{osc}} + \frac{1}{R_{osc} R_1}\right)$$
$$f_{-3\text{dB}} = \frac{k}{2\pi} = \frac{R_p}{2\pi C_{eq}}\left(\frac{1}{R_1 R_p} + \frac{1}{R_p R_{osc}} + \frac{1}{R_{osc} R_1}\right) = 230.7\text{ MHz}$$

El nuevo tiempo mínimo de subida medible con un sesgo del $10\%$ es:
$$t_{r,\min}(V_{in}) = \frac{\ln 9}{2\pi f_{-3\text{dB}} \cdot \sqrt{0.21}} = \frac{2.1972}{2\pi \cdot 230.7 \times 10^6 \cdot \sqrt{0.21}} = 3.30\text{ ns}$$

$$\mathbf{t_{r,\min}(V_{in}) = 3.3\text{ ns}}$$

> [!TIP]
> **Conclusión Docente:** El empleo de la sonda atenuadora $10\times$ reduce el tiempo de subida medible de $30.04\text{ ns}$ a tan solo $3.3\text{ ns}$, mejorando la velocidad de medida casi en un factor de 10 a costa de atenuar la amplitud por 10.

---

## Problema 2: Termopar Tipo K con Compensación de Unión Fría (Pt100) y AD623

### Enunciado

Se desea acondicionar un termopar normalizado de tipo K. Se añade circuitería para la corrección de temperatura de unión de referencia ($T_a$) empleando una Pt100 ($R_0 = 100\,\Omega, \alpha = 0.00385\,^\circ\text{C}^{-1}$) excitada con una corriente de $I = 100\,\mu\text{A}$.
La curva del termopar referida a $T_a = 0^\circ\text{C}$ viene dada por:
$$V(\text{mV}) \cong 0.039 \cdot T_1 + 2 \times 10^{-6} \cdot T_1^2$$
donde $T_1 \in [0^\circ\text{C}, 300^\circ\text{C}]$ y $T_a \in [10^\circ\text{C}, 30^\circ\text{C}]$.

```
             ┌─────────┐
Nickel-Cr ───┤+  AI1   │
             │  (AD623)├─────┐
             │ Rg1     │     │
Nickel-Al ───┤-        │     │  R1      R2
 (T1)        └─────────┘     ├─/\/\/\─┬─/\/\/\─┐
                                      │        │
                                    ┌─┴─┐      │
                                    │ - │      │
                             0 ─────┤ + │──────┴─ Vout (TLC2272)
                                    └───┘
  100 µA      ┌─────────┐
    │     Ro  │+  AI2   │
    ├───/\/\──┤  (AD623)├─────┘ (a través de R1/R2)
    │         │ Rg2     │
    ├───[Pt]──┤-        │
  100 µA      └─────────┘
```

**Se pide:**
1. Hallar $V$ para los extremos $0^\circ\text{C}$ y $300^\circ\text{C}$ ($T_a=0^\circ\text{C}$) y calcular la sensibilidad media $s_{T1}$.
2. Si $T_1 = 0^\circ\text{C}$, hallar $V$ para $10^\circ\text{C}$ y $30^\circ\text{C}$ de $T_a$ y estimar la sensibilidad $s_{Ta}$.
3. Hallar $R_0$ para que la tensión diferencial de entrada a AI2 sea nula cuando $T_a = 0^\circ\text{C}$.
4. Deducir $V_{out}$ en función de $T_1, T_a, R_{g1}, R_{g2}, R_1$ y $R_2$.
5. Diseñar $R_{g1}$ y $R_{g2}$ con $R_1 = R_2$ para sensibilidad de $10\text{ mV/}^\circ\text{C}$ respecto a $T_1$ e insensibilidad total a $T_a$.

---

### Solución Oficial Paso a Paso

#### 1 y 2. Sensibilidades del Termopar
- Para $T_a = 0^\circ\text{C}$:
  $$V(0^\circ\text{C}) = 0\text{ mV}$$
  $$V(300^\circ\text{C}) = 0.039 \cdot 300 + 2 \times 10^{-6} \cdot (300)^2 = 11.70 + 0.18 = 11.88\text{ mV}$$
  $$s_{T1} = \frac{11.88\text{ mV}}{300^\circ\text{C}} = \mathbf{39.6\,\mu\text{V/}^\circ\text{C}}$$

- Para $T_1 = 0^\circ\text{C}$ y variando $T_a$:
  $$V(T_a = 10^\circ\text{C}) = -[0.039 \cdot 10 + 2 \times 10^{-6} \cdot 10^2] = -0.390\text{ mV}$$
  $$V(T_a = 30^\circ\text{C}) = -[0.039 \cdot 30 + 2 \times 10^{-6} \cdot 30^2] = -1.172\text{ mV}$$
  $$s_{Ta} = \frac{-1.172 - (-0.390)}{30 - 10} = \frac{-0.782\text{ mV}}{20^\circ\text{C}} = \mathbf{-39.1\,\mu\text{V/}^\circ\text{C}}$$
  $$V \cong 39.6\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_1 - 39.1\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_a$$

---

#### 3. Equilibrio del Puente de la Pt100
$$V_d = I \cdot (R_0 - R_{Pt100}(T_a)) = I \cdot [R_0 - 100\,\Omega(1 + 0.00385 \cdot T_a)]$$
Para que $V_d = 0$ cuando $T_a = 0^\circ\text{C}$:
$$R_0 = 100\,\Omega$$
Sustituyendo $I = 100\,\mu\text{A}$:
$$V_d(T_a) = -100\,\mu\text{A} \cdot 100\,\Omega \cdot 0.00385 \cdot T_a = -38.5\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_a$$

---

#### 4 y 5. Expresión de Salida y Diseño de Ganancias
La ganancia diferencial del AD623 es $G_{AI} = 1 + \frac{100\text{ k}\Omega}{R_g}$.
La etapa sumadora con TLC2272 suma las tensiones provenientes de AI1 y AI2:
$$V_{out} = \left(1 + \frac{100\text{ k}\Omega}{R_{g1}}\right)\left(1 + \frac{R_1}{R_2}\right) \cdot 39.6\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_1 - \left(1 + \frac{100\text{ k}\Omega}{R_{g1}}\right)\left(1 + \frac{R_1}{R_2}\right) \cdot 39.1\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_a + \left(1 + \frac{100\text{ k}\Omega}{R_{g2}}\right)\left(\frac{R_1}{R_2}\right) \cdot 38.5\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_a$$

Para anular la dependencia de $T_a$:
$$\left(1 + \frac{100\text{ k}\Omega}{R_{g1}}\right)\left(1 + \frac{R_1}{R_2}\right) \cdot 39.1\,\frac{\mu\text{V}}{^\circ\text{C}} = \left(1 + \frac{100\text{ k}\Omega}{R_{g2}}\right)\left(\frac{R_1}{R_2}\right) \cdot 38.5\,\frac{\mu\text{V}}{^\circ\text{C}}$$

Para que la sensibilidad respecto a $T_1$ sea $10\text{ mV/}^\circ\text{C}$:
$$\left(1 + \frac{100\text{ k}\Omega}{R_{g1}}\right)\left(1 + \frac{R_1}{R_2}\right) \cdot 39.6\,\mu\text{V/}^\circ\text{C} = 10\text{ mV/}^\circ\text{C}$$
$$\left(1 + \frac{100\text{ k}\Omega}{R_{g1}}\right)\left(1 + \frac{R_1}{R_2}\right) = \frac{10\text{ mV}}{0.0396\text{ mV}} = 252.53$$

Con $R_1 = R_2$:
$$\left(1 + \frac{100\text{ k}\Omega}{R_{g1}}\right) \cdot 2 = 252.53 \implies 1 + \frac{100\text{ k}\Omega}{R_{g1}} = 126.26 \implies \mathbf{R_{g1} = 798.3\,\Omega}$$

Sustituyendo en la ecuación de cancelación:
$$252.53 \cdot 39.1 = \left(1 + \frac{100\text{ k}\Omega}{R_{g2}}\right) \cdot 1 \cdot 38.5$$
$$1 + \frac{100\text{ k}\Omega}{R_{g2}} = \frac{252.53 \cdot 39.1}{38.5} = 256.46 \implies \mathbf{R_{g2} = 391.4\,\Omega}$$

---

## Problema 3: Oscilador para Sensor Capacitivo y Presupuesto de Incertidumbre GUM

### Enunciado

El siguiente circuito es un oscilador para acondicionar un sensor capacitivo $C$:
```
          ┌─────────────/\/\/\─────────────┐
          │               R                │
          │                                │
         === C                             │
          │                                │
         GND      ┌───┐                    │
          ├───────┤ - │                    │
                  │   ├─── OUT ────────────┴─── Vout
  2.5 V ──/\/\/\──┤ + │
            R2    └───┘
                    │
                    └─/\/\/\── Vout
                        R1
```
El operacional se alimenta a $V^+ = 5\text{ V}$ y $V^- = 0\text{ V}$ (rail-to-rail).

**Se pide:**
1. Expresión analítica de la frecuencia de oscilación en función de $R, C, R_1$ y $R_2$.
2. Si $R_2 = R_1, R = 100\text{ k}\Omega$ y $C = \frac{330\text{ pF}}{1+x}$, hallar $f(x)$, $f_{\min}$ y $f_{\max}$ para $x \in [0, 0.1]$.
3. Medida con multímetro Keysight 34465A (tiempo de apertura $1\text{ s}$, calibrado hace 1 año, exactitud $0.006\%$ de lectura con $k=2$). Estimar la incertidumbre típica Tipo B para $x=0$.
4. Estimar la incertidumbre típica en capacidad $u(C)$ y el incremento en $x$ equivalente a dicha incertidumbre. Juzgar si es relevante.

---

### Solución Oficial Paso a Paso

#### 1. Frecuencia de Oscilación
Por superposición, la tensión en el terminal no inversor $V_+$ es:
$$V_+ = V_{out} \frac{R_2}{R_1 + R_2} + 2.5\text{ V} \frac{R_1}{R_1 + R_2}$$
- Cuando $V_{out} = 5\text{ V}$: $V_{+,H} = 5\text{ V} \frac{R_2}{R_1 + R_2} + 2.5\text{ V} \frac{R_1}{R_1 + R_2}$.
- Cuando $V_{out} = 0\text{ V}$: $V_{+,L} = 2.5\text{ V} \frac{R_1}{R_1 + R_2}$.

Integrando la carga y descarga del condensador:
$$T_1 = T_2 = R \cdot C \cdot \ln\left(1 + \frac{2 R_2}{R_1}\right)$$
$$T = T_1 + T_2 = 2 R C \ln\left(1 + \frac{2 R_2}{R_1}\right)$$
$$\mathbf{f = \frac{1}{2 R C \ln\left(1 + \frac{2 R_2}{R_1}\right)}}$$

---

#### 2. Rango de Frecuencias
Con $R_2 = R_1 \implies 1 + \frac{2 R_2}{R_1} = 3$:
$$f = \frac{1}{2 R C \ln 3} = \frac{1+x}{2 \cdot 100\text{ k}\Omega \cdot 330\text{ pF} \cdot \ln 3} = \mathbf{13.793\text{ kHz} \cdot (1+x)}$$
- Para $x = 0$: $\mathbf{f_{\min} = 13.793\text{ kHz}}$
- Para $x = 0.1$: $\mathbf{f_{\max} = 15.171\text{ kHz}}$

---

#### 3 y 4. Incertidumbre Metrológica (GUM)
- Para $x = 0$ ($f = 13.793\text{ kHz}$):
  $$u(f) = \frac{0.006\%}{2} \cdot 13.793\text{ kHz} = \mathbf{0.41\text{ Hz}}$$

- Relación de capacidad con la frecuencia:
  $$C = \frac{1}{2 R f \ln 3} \implies \frac{\partial C}{\partial f} = -\frac{1}{2 R f^2 \ln 3} = -2.39 \times 10^{-14}\text{ F/Hz}$$
  $$u(C) = \left|\frac{\partial C}{\partial f}\right| \cdot u(f) = 2.39 \times 10^{-14} \cdot 0.41 = 9.8 \times 10^{-15}\text{ F} = \mathbf{0.0098\text{ pF}}$$

- Variación en $x$ provocada por esta incertidumbre:
  $$u(x) \cong \frac{u(C)}{C_0} = \frac{0.0098\text{ pF}}{330\text{ pF}} = \mathbf{2.97 \times 10^{-5}}$$
  $$\frac{x_{\max}}{u(x)} = \frac{0.1}{2.97 \times 10^{-5}} = \mathbf{3667}$$

> [!NOTE]
> La incertidumbre de medida es **3667 veces menor** que el fondo de escala de $x$, por lo que el multímetro de laboratorio no introduce una limitación apreciable en la medida.

---

# Convocatoria 2: Examen Final del 16 de enero de 2024
> **Profesores:** Miguel Ángel García González y Juan José Ramos Castro  
> **Asignatura:** Sistemas de Medida (230920) · UPC

---

## Problema 1: Análisis Estadístico de Mediciones (Criterio de Chauvenet, Autocorrelación e Incertidumbre GUM)

### Enunciado

Se mide una tensión continua con el multímetro de laboratorio Keysight 34465A (calibrado hace menos de 2 años) con 10 PLC, adquiriendo 25 lecturas consecutivas:

| # | $V_{DC}\text{ (V)}$ | # | $V_{DC}\text{ (V)}$ | # | $V_{DC}\text{ (V)}$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 3.31313 | 10 | 3.31383 | 19 | 3.31356 |
| 2 | 3.31290 | 11 | 3.31331 | 20 | 3.31354 |
| 3 | 3.31386 | 12 | **3.32179** | 21 | 3.31466 |
| 4 | 3.31337 | 13 | 3.31430 | 22 | 3.31380 |
| 5 | 3.31308 | 14 | 3.31331 | 23 | 3.31297 |
| 6 | 3.31371 | 15 | 3.31353 | 24 | 3.31281 |
| 7 | 3.31315 | 16 | 3.31354 | 25 | 3.31262 |
| 8 | 3.31360 | 17 | 3.31382 | | |
| 9 | 3.31410 | 18 | 3.31349 | | |

**Se pide:**
1. Eliminar las lecturas aberrantes aplicando el criterio de Chauvenet con $D_{\max} = 3$.
2. Demostrar la independencia de las lecturas mediante la función de autocorrelación con retardo 1 ($r_1$) para un nivel de confianza del $99.9\%$.
3. Evaluar la incertidumbre típica de Tipo A ($u_A$).
4. Estimar la incertidumbre típica de Tipo B ($u_B$) según las especificaciones del multímetro ($0.0045\%\text{ lectura} + 0.0004\%\text{ escala}$, escala $10\text{ V}$, $k=2$).
5. Expresar el resultado final de la medida $\bar{V} \pm u_c$ con las cifras significativas correctas.

---

### Solución Oficial Paso a Paso

#### 1. Criterio de Chauvenet ($D_{\max} = 3$)
Para la serie completa de 25 datos:
- Media inicial: $\bar{V}_{25} \cong 3.3138\text{ V}$
- Desviación estándar muestral: $s_{25} = 0.0017\text{ V}$
- Para la lectura #12 ($V = 3.32179\text{ V}$):
  $$D_{12} = \frac{|3.32179 - 3.3138|}{0.0017} = 4.62 > D_{\max} = 3$$
  **Se elimina la lectura #12 por considerarse una observación aberrante (outlier).**

Recalculando con las $N = 24$ lecturas restantes:
- Media: $\bar{V} = 3.31350\text{ V}$
- Desviación estándar: $s = 0.00048\text{ V}$
- La lectura más alejada es ahora la #21 ($3.31466\text{ V}$):
  $$D_{21} = \frac{|3.31466 - 3.31350|}{0.00048} = 2.43 < 3$$
  Ningún otro dato supera el umbral, por lo que las 24 lecturas restantes son válidas.

---

#### 2. Test de Independencia por Autocorrelación ($r_1$)
Calculando el coeficiente de autocorrelación con retardo 1 para $N = 24$:
$$r_1 = 0.191$$
Para un nivel de confianza del $99.9\%$, el factor crítico bilateral de la distribución normal es $k = 3.2905$.
La desviación estándar asintótica de $r_1$ bajo la hipótesis nula de ruido blanco independiente es $\sigma_r = \frac{1}{\sqrt{N}} = \frac{1}{\sqrt{24}} \cong 0.204$.
Los límites críticos de aceptación son:
$$\text{Límites} = \pm \frac{k}{\sqrt{N}} = \pm \frac{3.2905}{\sqrt{24}} \cong \pm 0.200$$

Como $|r_1| = 0.191 \le 0.200$, **se acepta la hipótesis de independencia estadística** de las observaciones al $99.9\%$ de confianza.

---

#### 3. Incertidumbre Tipo A ($u_A$)
$$u_A(\bar{V}) = \frac{s}{\sqrt{N}} = \frac{0.00048\text{ V}}{\sqrt{24}} = 9.76 \times 10^{-5}\text{ V} = \mathbf{97.6\,\mu\text{V}}$$

---

#### 4. Incertidumbre Tipo B ($u_B$)
Especificación del Keysight 34465A a 2 años en escala de $10\text{ V}$:
$$\text{Exactitud} = 0.0045\% \cdot \text{Lectura} + 0.0004\% \cdot \text{Rango}$$
$$\Delta V = \frac{0.0045}{100} \cdot 3.31350\text{ V} + \frac{0.0004}{100} \cdot 10\text{ V} = 1.491 \times 10^{-4}\text{ V} + 4.0 \times 10^{-5}\text{ V} = 189.1\,\mu\text{V}$$
Como el fabricante especifica $k = 2$:
$$u_B(\bar{V}) = \frac{\Delta V}{k} = \frac{189.1\,\mu\text{V}}{2} = \mathbf{94.6\,\mu\text{V}}$$

---

#### 5. Incertidumbre Combinada y Resultado Final
$$u_c(\bar{V}) = \sqrt{u_A^2 + u_B^2} = \sqrt{(97.6\,\mu\text{V})^2 + (94.6\,\mu\text{V})^2} = 135.9\,\mu\text{V} \cong 136\,\mu\text{V} = 0.00014\text{ V}$$

$$\mathbf{\bar{V}_{DC} = 3.31350\text{ V} \pm 0.00014\text{ V} \quad (k=1)}$$

---

## Problema 2: Acondicionador Lineal para Sensor Capacitivo con OPA134 e Interferencias (PSRR, Red 230V)

### Enunciado

Acondicionador lineal para convertir cambios de capacidad $C_1 = C_0(1+x)$ a tensión mediante un amplificador operacional inversor OPA134, donde $C_0 = 100\text{ pF}$, $x \in [-0.9, +0.9]$ y la señal de excitación es $V_s(t) = 1\text{ V}_{\text{pico}}$ a $f_0 = 30\text{ kHz}$. En la realimentación se dispone $C_2 = C_0 = 100\text{ pF}$ en paralelo con una resistencia $R_1$.

```
           ┌──────────/\/\/\──────────┐
           │            R1            │
           │                          │
           ├───────────||─────────────┤
           │         C2 = Co          │
           │                          │
           │        ┌───┐             │
Vs ───||───┴────────┤ - │             │
   C1=Co(1+x)       │   ├─────────────┴── V6
              GND ──┤ + │ (OPA134)
                    └───┘
```

**Se pide:**
1. Valor mínimo de $R_1$ para ser al menos 100 veces superior al módulo de la impedancia de $C_2$ a $30\text{ kHz}$.
2. Con $R_1 = 8.2\text{ M}\Omega$, hallar las amplitudes de pico máxima y mínima de salida $V_6$.
3. Indicar el desfase entre $V_6$ y $V_s$.
4. Verificar si existe distorsión por Slew-Rate ($SR_{\min} = 15\text{ V}/\mu\text{s}$).
5. Error debido al CMRR finito a $30\text{ kHz}$.
6. Interferencia conducida de alimentación: si la rama de $+5\text{ V}$ tiene un rizado senoidal de $100\text{ mV}_{\text{rms}}$ a $600\text{ kHz}$, estimar el pico inducido sabiendo que $\text{PSRR}^+ = 20\text{ dB}$.
7. Interferencia de red: acoplo capacitivo parásito de $1\text{ pF}$ conectado a la línea de red ($230\text{ V}_{\text{rms}}$ a $50\text{ Hz}$) directo al pin 2 (inversor). Estimar el pico resultante a la salida.

---

### Solución Oficial Paso a Paso

#### 1. Dimensionamiento de $R_1$
$$|Z_{C2}(30\text{ kHz})| = \frac{1}{2\pi f C_2} = \frac{1}{2\pi \cdot 30 \times 10^3 \cdot 100 \times 10^{-12}} = 53.05\text{ k}\Omega$$
$$R_1 \ge 100 \cdot |Z_{C2}| = 100 \cdot 53.05\text{ k}\Omega = \mathbf{5.31\text{ M}\Omega}$$
*(Se selecciona el valor comercial $R_1 = 8.2\text{ M}\Omega$)*.

---

#### 2 y 3. Función de Transferencia y Desfase
Despreciando la corriente por $R_1$ a la frecuencia de trabajo:
$$\frac{V_6}{V_s}(s) \cong -\frac{Z_{C2}}{Z_{C1}} = -\frac{1 / (C_0 s)}{1 / (C_0(1+x) s)} = -(1+x)$$

Como $V_{s,\text{pico}} = 1\text{ V}$:
- Para $x = -0.9$: $V_{6,\text{pico},\min} = 1 - 0.9 = \mathbf{0.1\text{ V}}$
- Para $x = +0.9$: $V_{6,\text{pico},\max} = 1 + 0.9 = \mathbf{1.9\text{ V}}$

El signo negativo introduce un **desfase de $180^\circ$ ($\pi\text{ rad}$)**.

---

#### 4. Verificación de Slew-Rate
La máxima pendiente temporal ocurre a la máxima amplitud:
$$\left.\frac{\partial V_6}{\partial t}\right|_{\max} = V_{p,\max} \cdot 2\pi f = 1.9\text{ V} \cdot 2\pi \cdot 30\text{ kHz} = 0.358\text{ V}/\mu\text{s} \cong \mathbf{0.36\text{ V}/\mu\text{s}}$$
Como $SR_{\min} = 15\text{ V}/\mu\text{s} \gg 0.36\text{ V}/\mu\text{s}$, **no existe riesgo alguno de distorsión**.

---

#### 5. Error por CMRR
El terminal no inversor está conectado directamente a masa ($V_+ = 0$). Como el operacional mantiene cortocircuito virtual ($V_- \cong 0$), la tensión en modo común es nula ($V_{cm} = 0$), por lo que **el CMRR finito no introduce error apreciable**.

---

#### 6. Interferencia Conducida de Alimentación (PSRR)
A $600\text{ kHz}$, la gráfica del fabricante indica $\text{PSRR}^+ = 20\text{ dB} \implies 10^{20/20} = 10$.
La interferencia referida a la entrada no inversora es $V_{in,\text{interf}} = \frac{100\text{ mV} \cdot \sqrt{2}}{10} = 14.14\text{ mV}$.
La ganancia de ruido no inversora es:
$$G_{no-inv} = 1 + \frac{C_1}{C_2} = 1 + (1+x) = 2 + x$$
En el caso más desfavorable ($x = +0.9 \implies G = 2.9$):
$$V_{6,\text{pico},\max}(\text{PSRR}) = 14.14\text{ mV} \cdot 2.9 = \mathbf{41\text{ mV}}$$

---

#### 7. Interferencia Capacitiva de Red (230 V a 50 Hz)
A $50\text{ Hz}$, la reactancia de $C_2$ es:
$$|Z_{C2}(50\text{ Hz})| = \frac{1}{2\pi \cdot 50 \cdot 100 \times 10^{-12}} = 31.83\text{ M}\Omega$$
En paralelo con $R_1 = 8.2\text{ M}\Omega$, la impedancia equivalente es:
$$|Z_{eq}| \cong 7.9\text{ M}\Omega \quad (\text{o aproximando por } R_1 = 8.2\text{ M}\Omega)$$
La corriente inyectada por la capacidad parásita $C_p = 1\text{ pF}$ desde la red de $230\text{ V}_{\text{rms}}$ ($V_{pico} = 230\sqrt{2}\text{ V}$) es:
$$I_p = 230\sqrt{2} \cdot 2\pi \cdot 50 \cdot 1 \times 10^{-12} = 1.022 \times 10^{-7}\text{ A}$$
La tensión de pico inducida a la salida es:
$$V_{6,\text{pico}}(50\text{ Hz}) = I_p \cdot R_1 = 1.022 \times 10^{-7}\text{ A} \cdot 8.2\text{ M}\Omega = \mathbf{0.84\text{ V}}$$
*(Si se toma la impedancia paralela exacta de $7.9\text{ M}\Omega$, resulta $0.81\text{ V}$)*.

> [!WARNING]
> ¡Una capacidad parásita de tan solo $1\text{ pF}$ acoplada a la red genera una interferencia de **$0.84\text{ V}$**, comparable con la señal útil completa ($0.1\text{ V} - 1.9\text{ V}$)! Esto demuestra la imperiosa necesidad de apantallamiento en transductores capacitivos de alta impedancia.

---

## Problema 3: Termopar Tipo K con Linealización de NTC (Taylor), AD620 y Ruido 1/f

### Enunciado

Medida de un horno ($100^\circ\text{C}$ a $350^\circ\text{C}$) con termopar tipo K:
$$V_K[\mu\text{V}] \cong 41.078\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_h - 39.606\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot T_c$$
La unión fría está a $T_c \in [5^\circ\text{C}, 40^\circ\text{C}]$. Se utiliza un termistor NTC para monitorizar $T_c$. Se desea que la salida del amplificador AD620 cumpla:
$$V_a[\text{V}] = 0.01\,\frac{\text{V}}{^\circ\text{C}} \cdot T_h = 10\,\frac{\text{mV}}{^\circ\text{C}} \cdot T_h$$

```
   Termopar K                   AD620
     (+) ─────────────────────── pin 3 (+)
     (-) ────────┬────────────── pin 2 (-)
                 │  [ Rg ]
                 └───────────────
                                pin 5 (Vref) ◄── Vref(Tc)
                                pin 6 (OUT)  ───► Va = G·Vd + Vref
```

**Se pide:**
1. Parámetros NTC: $R(0^\circ\text{C}) = 34\text{ k}\Omega$ y $R(50^\circ\text{C}) = 6.7\text{ k}\Omega$. Hallar $\beta$ y $R_0(25^\circ\text{C})$.
2. Diseñar $R_{lin}$ para que $V_{ntc}$ tenga un punto de inflexión en $T_{xc} = 22.5^\circ\text{C}$.
3. Linealización de $V_{ntc}$ en torno a $22.5^\circ\text{C}$.
4. Diseñar la ganancia $G$ y $R_g$ del AD620.
5. Hallar la relación $V_{ref}(T_c) = A \cdot V_{ntc}(T_c) + B$ para compensar exactamente la unión fría.
6. Estimar el valor eficaz de ruido referido a la entrada entre $0.01\text{ Hz}$ y $10\text{ Hz}$.
7. Incertidumbre típica en $V_a$ y en temperatura $u(T_h)$ debida al ruido.

---

### Solución Oficial Paso a Paso

#### 1. Parámetros del Termistor NTC
$$R_{th}(T) = R_0 \cdot \exp\left[\beta\left(\frac{1}{T} - \frac{1}{T_0}\right)\right]$$
$$\frac{R(0^\circ\text{C})}{R(50^\circ\text{C})} = \frac{34\text{ k}\Omega}{6.7\text{ k}\Omega} = 5.0746 = \exp\left[\beta\left(\frac{1}{273.15} - \frac{1}{323.15}\right)\right]$$
$$\ln(5.0746) = 1.6242 = \beta \cdot 5.6644 \times 10^{-4} \implies \mathbf{\beta = 2867.4\text{ K}}$$
$$R_0(298.15\text{ K}) = \frac{34\text{ k}\Omega}{\exp\left[2867.4 \cdot \left(\frac{1}{273.15} - \frac{1}{298.15}\right)\right]} = \mathbf{14.1\text{ k}\Omega}$$

---

#### 2. Resistencia de Taylor $R_{lin}$ en $T_{xc} = 22.5^\circ\text{C}$ ($295.65\text{ K}$)
$$R_{th}(295.65\text{ K}) = 14.1\text{ k}\Omega \cdot \exp\left[2867.4 \cdot \left(\frac{1}{295.65} - \frac{1}{298.15}\right)\right] = 15.3\text{ k}\Omega$$
$$R_{lin} = R_{th}(T_{xc}) \cdot \frac{\beta - 2 T_{xc}}{\beta + 2 T_{xc}} = 15.3\text{ k}\Omega \cdot \frac{2867.4 - 2(295.65)}{2867.4 + 2(295.65)} = 15.3\text{ k}\Omega \cdot \frac{2276.1}{3458.7} = \mathbf{10.06\text{ k}\Omega}$$

---

#### 3. Linealización de $V_{ntc}$
Alimentado a $5\text{ V}$:
$$V_{ntc}(T_{xc}) = 5\text{ V} \cdot \frac{10.06}{10.06 + 15.3} = 1.984\text{ V}$$
$$\left.\frac{\partial V_{ntc}}{\partial T}\right|_{T_{xc}} = 5\text{ V} \cdot \frac{R_{lin}}{(R_{lin} + R_{th})^2} \cdot \frac{\beta}{T^2} \cdot R_{th} = 39.3\text{ mV/}^\circ\text{C}$$
$$V_{ntc}(T_c) \cong 1.984\text{ V} + 0.0393\text{ V/}^\circ\text{C} \cdot (T_c - 22.5^\circ\text{C}) = \mathbf{1.101\text{ V} + 0.0393 \cdot T_c}$$

---

#### 4 y 5. Ganancia del AD620 y Compensación de Unión Fría
$$41.078\,\frac{\mu\text{V}}{^\circ\text{C}} \cdot G = 10\,\frac{\text{mV}}{^\circ\text{C}} = 10000\,\frac{\mu\text{V}}{^\circ\text{C}} \implies \mathbf{G = 243.4}$$
$$G = 1 + \frac{49.4\text{ k}\Omega}{R_g} \implies \mathbf{R_g = 203.76\,\Omega}$$

Para compensar el término $-39.606\,\mu\text{V/}^\circ\text{C} \cdot T_c$:
$$V_{ref}(T_c) = 39.606\,\mu\text{V/}^\circ\text{C} \cdot G \cdot T_c = 0.0096\text{ V/}^\circ\text{C} \cdot T_c$$
Despejando $T_c$ de la expresión de la NTC:
$$T_c = \frac{V_{ntc} - 1.101\text{ V}}{0.0393\text{ V/}^\circ\text{C}}$$
$$V_{ref}(T_c) = \frac{0.0096}{0.0393}(V_{ntc} - 1.101\text{ V}) = 0.246 \cdot V_{ntc} - 0.270\text{ V}$$
$$\mathbf{A = 0.246, \quad B = -0.270\text{ V}}$$

---

#### 6 y 7. Análisis de Ruido del AD620 ($0.01\text{ Hz}$ a $10\text{ Hz}$)
Del datasheet del AD620:
- Densidad de ruido blanco: $e_{nw} = 9\text{ nV}/\sqrt{\text{Hz}}$
- A $1\text{ Hz}$, densidad total: $e_{total}(1\text{ Hz}) = 21\text{ nV}/\sqrt{\text{Hz}}$
  $$e_{n,1/f}(1\text{ Hz}) = \sqrt{(21)^2 - (9)^2} = \sqrt{441 - 81} = \sqrt{360} \cong 19\text{ nV}/\sqrt{\text{Hz}}$$

Integrando en la banda $[0.01\text{ Hz}, 10\text{ Hz}]$:
$$\sigma_{white} = 9\text{ nV}/\sqrt{\text{Hz}} \cdot \sqrt{10 - 0.01} = 28.4\text{ nV}$$
$$\sigma_{1/f} = 19\text{ nV}/\sqrt{\text{Hz}} \cdot \sqrt{\ln\left(\frac{10}{0.01}\right)} = 19 \cdot \sqrt{6.908} = 49.9\text{ nV}$$
$$\sigma_{total} = \sqrt{(28.4)^2 + (49.9)^2} = \mathbf{57.4\text{ nV}}$$

A la salida del AD620:
$$u(V_a)_{\text{ruido}} = G \cdot \sigma_{total} = 243.4 \cdot 57.4\text{ nV} = \mathbf{13.98\,\mu\text{V}}$$

Incertidumbre referida a la temperatura medida $T_h$:
$$u(T_h)_{\text{ruido}} = \frac{u(V_a)}{\text{Sensibilidad}} = \frac{13.98\,\mu\text{V}}{10\text{ mV/}^\circ\text{C}} = \mathbf{0.0014^\circ\text{C}}$$

---

# Convocatoria 3: Examen Final del 14 de enero de 2025
> **Profesores:** Miguel Ángel García González y Juan José Ramos Castro  
> **Asignatura:** Sistemas de Medida (230920) · UPC

---

## Ejercicios Cortos (30%)

### Ejercicio 1: Aislamiento del Multímetro
Un multímetro tiene un CMRR de $120\text{ dB}$ en continua y de $90\text{ dB}$ a $50\text{ Hz}$ para una resistencia de desequilibrio $R_{des} = 1\text{ k}\Omega$. Estime la capacidad y la resistencia de aislamiento del instrumento.

**Solución Oficial:**
$$R_{iso} = R_{des} \cdot 10^{\frac{\text{CMRR}_{DC}}{20}} = 1\text{ k}\Omega \cdot 10^{6} = \mathbf{1\text{ G}\Omega}$$
A $50\text{ Hz}$:
$$|Z_{iso}| = R_{des} \cdot 10^{\frac{\text{CMRR}(50\text{ Hz})}{20}} = 1\text{ k}\Omega \cdot 10^{4.5} = 31.6\text{ M}\Omega$$
Como $|Z_{iso}| \ll R_{iso}$, la reactancia capacitiva domina:
$$C_{iso} = \frac{1}{2\pi \cdot 50\text{ Hz} \cdot 31.6\text{ M}\Omega} = \mathbf{100.7\text{ pF}}$$

---

### Ejercicio 2: Amplificador de Transimpedancia (Red T) y Tensión de Offset
Un TIA con red T cumple $R_1 = R_3 = 5100 R_2$. Si está alimentado a $\pm 5\text{ V}$ ($V_{sat} = \pm 5\text{ V}$), halle la máxima tensión de offset $V_{os}$ para que no haya peligro de saturación. Suponga $Z_s \to \infty$.

**Solución Oficial:**
Por el cortocircuito virtual, $V_+$ tiene $V_{os}$. Como por $R_1$ no circula corriente ($I_s = 0, Z_s \to \infty$), el nodo intermedio de la red T está a $V_{os}$.
La corriente por $R_2$ es $\frac{V_{os}}{R_2}$, la cual fluye íntegra por $R_3$:
$$V_o|_{V_{os}} = V_{os} + \frac{V_{os}}{R_2} \cdot R_3 = \left(1 + \frac{R_3}{R_2}\right) V_{os} = (1 + 5100) V_{os} = 5101 \cdot V_{os}$$
Para evitar saturación:
$$5101 \cdot V_{os} < 5\text{ V} \implies \mathbf{V_{os} < 980.2\,\mu\text{V}}$$

---

### Ejercicio 3: Célula de Carga y CMRR Mínimo
Célula de carga alimentada con $V_s = 5\text{ V}$. Dos etapas amplificadoras donde la ganancia nominal es $R_7/R_6 = 35.36$. Halle el CMRR mínimo en dB para que el error de cero en $V_{out}$ sea menor a $0.1\text{ V}$.

**Solución Oficial:**
Para $x = 0$, la tensión en modo común a la entrada es:
$$V_c = \frac{V_s}{2} = 2.5\text{ V}$$
A la salida de la cascada:
$$V_o|_{V_c} = \frac{V_c}{\text{CMRR}} \cdot \left(\frac{R_7}{R_6}\right)^2 < 0.1\text{ V}$$
$$\text{CMRR} > \frac{2.5\text{ V}}{0.1\text{ V}} \cdot (35.36)^2 = 25 \cdot 1250.3 = 31258$$
$$\mathbf{\text{CMRR}_{\min} = 20 \log_{10}(31258) = 89.9\text{ dB}}$$

---

### Ejercicio 4: Lazo de Corriente Industrial 4-20 mA
Sistema de medida de presión industrial ($0$ a $30\text{ kPa}$) con estándar 4-20 mA. Halle la presión si circula una corriente de $15\text{ mA}$.

**Solución Oficial:**
Relación lineal estándar:
$$P = \frac{I - 4\text{ mA}}{16\text{ mA}} \cdot (30\text{ kPa} - 0\text{ kPa}) = \frac{15 - 4}{16} \cdot 30 = \frac{11}{16} \cdot 30 = \mathbf{20.625\text{ kPa}}$$

---

## Problema 1 (35%): Sensor de Temperatura de Corriente AD590 y Presupuesto GUM Completo

### Enunciado

Medida de temperatura mediante el sensor de corriente AD590:
$$I_{AD590} = 1\,\frac{\mu\text{A}}{\text{K}} \cdot T[\text{K}] \pm 0.5\,\mu\text{A} \quad (k=3)$$

```
                     R3 = 10 kΩ
                 ┌─────/\/\/\─────┐
     R2=3.65 kΩ  │                │
Vref ──/\/\/\────┤                │
 (5V)            │   ┌───┐        │
          Vx ────┼───┤ - │        │
                 │   │   ├────────┴─── Vo
                 │ ┌─┤ + │
                 │ │ └───┘
                 │ │
     R4=7.87 kΩ  │ │
GND ───/\/\/\────┘ │
                   │
GND ───────────────┘
```
$V_x$ se obtiene haciendo circular la corriente del AD590 a través de una resistencia $R_1$: $V_x = I_{AD590} \cdot R_1$.

**Se pide:**
1. Hallar $R_1$ para que $V_x$ tenga una sensibilidad de $10\text{ mV/}^\circ\text{C}$.
2. Con $R_3 = 10\text{ k}\Omega, R_2 = 3.65\text{ k}\Omega$ y $R_4 = 7.87\text{ k}\Omega$, hallar la sensibilidad de $V_o$ y la temperatura en $^\circ\text{C}$ para la cual $V_o = 0\text{ V}$.
3. Para una temperatura ambiente de unos $20^\circ\text{C}$, sabiendo que $R_1, R_2, R_3, R_4$ tienen una tolerancia del $0.1\%$ ($k=2$), estimar el valor nominal de $V_o$ y su presupuesto de incertidumbres detallado $u(V_o)$ (GUM).
4. Estimar la incertidumbre expandida en temperatura $U(T)$ para un nivel de confianza del $95\%$ ($k=2$).

---

### Solución Oficial Paso a Paso

#### 1. Sensibilidad de $V_x$ y Valor de $R_1$
$$\frac{\partial V_x}{\partial T} = 1\,\frac{\mu\text{A}}{\text{K}} \cdot R_1 = 10\,\frac{\text{mV}}{^\circ\text{C}} \implies R_1 = \frac{10\text{ mV}}{1\,\mu\text{A}} = \mathbf{10\text{ k}\Omega}$$

---

#### 2. Sensibilidad de $V_o$ y Cero de Tensión
Por superposición:
$$V_o = V_x \left(1 + \frac{R_3}{R_4} + \frac{R_3}{R_2}\right) - V_{ref} \frac{R_3}{R_2}$$
$$\frac{\partial V_o}{\partial T} = \frac{\partial V_x}{\partial T} \cdot \left(1 + \frac{10\text{ k}\Omega}{7.87\text{ k}\Omega} + \frac{10\text{ k}\Omega}{3.65\text{ k}\Omega}\right) = 10\,\frac{\text{mV}}{^\circ\text{C}} \cdot (1 + 1.2706 + 2.7397) = 10 \cdot 5.0103 = \mathbf{50.1\text{ mV/}^\circ\text{C}}$$

Para $V_o = 0\text{ V}$:
$$50.1\,\frac{\text{mV}}{\text{K}} \cdot T[\text{K}] = 5\text{ V} \cdot \frac{10}{3.65} = 13.6986\text{ V}$$
$$T = \frac{13.6986\text{ V}}{0.0501\text{ V/K}} = 273.43\text{ K} \implies \mathbf{T(V_o = 0) = 0.28^\circ\text{C}}$$

---

#### 3. Presupuesto de Incertidumbres (GUM)
A $T = 20^\circ\text{C} = 293.15\text{ K}$:
$$I_{AD590} = 293.15\,\mu\text{A}$$
$$V_o = 293.15\,\mu\text{A} \cdot 10\text{ k}\Omega \cdot 5.0103 - 5\text{ V} \cdot \frac{10}{3.65} = 14.6877\text{ V} - 13.6986\text{ V} = \mathbf{0.989\text{ V}}$$

Incertidumbres típicas de las fuentes:
- Resistencias (tolerancia $0.1\%$, $k=2$):
  $$u(R_1) = u(R_3) = \frac{0.1\% \cdot 10\text{ k}\Omega}{2} = \mathbf{5\,\Omega}$$
  $$u(R_2) = \frac{0.1\% \cdot 3.65\text{ k}\Omega}{2} = \mathbf{1.825\,\Omega}$$
  $$u(R_4) = \frac{0.1\% \cdot 7.87\text{ k}\Omega}{2} = \mathbf{3.935\,\Omega}$$
- Sensor AD590 ($k=3$):
  $$u(I_{AD590}) = \frac{0.5\,\mu\text{A}}{3} = \mathbf{0.167\,\mu\text{A}}$$

Derivadas parciales y coeficientes de sensibilidad:
1. $c_{R1} = \frac{\partial V_o}{\partial R_1} = I_{AD590} \left(1 + \frac{R_3}{R_4} + \frac{R_3}{R_2}\right) = 293.15\,\mu\text{A} \cdot 5.01 = 1.47\text{ mV/}\Omega$
2. $c_{R2} = \frac{\partial V_o}{\partial R_2} = -I_{AD590} R_1 \frac{R_3}{R_2^2} + V_{ref} \frac{R_3}{R_2^2} = 1.55\text{ mV/}\Omega$
3. $c_{R3} = \frac{\partial V_o}{\partial R_3} = I_{AD590} R_1 \left(\frac{1}{R_4} + \frac{1}{R_2}\right) - \frac{V_{ref}}{R_2} = -0.194\text{ mV/}\Omega$
4. $c_{R4} = \frac{\partial V_o}{\partial R_4} = -I_{AD590} R_1 \frac{R_3}{R_4^2} = -0.473\text{ mV/}\Omega$
5. $c_I = \frac{\partial V_o}{\partial I_{AD590}} = R_1 \left(1 + \frac{R_3}{R_4} + \frac{R_3}{R_2}\right) = 50.1\text{ mV/}\mu\text{A}$

Tabla de contribuciones a la incertidumbre:

| Magnitud $x_i$ | Valor Nominal | Incertidumbre $u(x_i)$ | Coef. Sensibilidad $c_i$ | Contribución $u_i = |c_i| u(x_i)$ |
| :--- | :--- | :--- | :--- | :--- |
| $R_1$ | $10\text{ k}\Omega$ | $5\,\Omega$ | $1.47\text{ mV/}\Omega$ | $7.35\text{ mV}$ |
| $R_2$ | $3.65\text{ k}\Omega$ | $1.825\,\Omega$ | $1.55\text{ mV/}\Omega$ | $2.83\text{ mV}$ |
| $R_3$ | $10\text{ k}\Omega$ | $5\,\Omega$ | $-0.194\text{ mV/}\Omega$ | $0.97\text{ mV}$ |
| $R_4$ | $7.87\text{ k}\Omega$ | $3.935\,\Omega$ | $-0.473\text{ mV/}\Omega$ | $1.86\text{ mV}$ |
| $I_{AD590}$ | $293.15\,\mu\text{A}$ | $0.167\,\mu\text{A}$ | $50.1\text{ mV/}\mu\text{A}$ | $8.52\text{ mV}$ |

Incertidumbre típica combinada:
$$u(V_o) = \sqrt{(7.35)^2 + (2.83)^2 + (0.97)^2 + (1.86)^2 + (8.52)^2} = \mathbf{11.8\text{ mV}}$$
$$\mathbf{V_o = 0.9893\text{ V} \pm 0.0118\text{ V} \quad (k=1)}$$

---

#### 4. Incertidumbre en Temperatura
$$u(T) = \frac{u(V_o)}{\partial V_o / \partial T} = \frac{11.8\text{ mV}}{50.1\text{ mV/}^\circ\text{C}} = \mathbf{0.236^\circ\text{C}}$$
Con factor de cobertura $k = 2$ (confianza del $95\%$):
$$U(T) = 2 \cdot u(T) = 2 \cdot 0.236^\circ\text{C} = \mathbf{0.46^\circ\text{C}}$$

---

## Problema 2 (35%): Termómetro Termopar Tipo J con Pt100 y Análisis de Ruido Flicker/Blanco

### Enunciado

Termómetro con termopar tipo J ($0^\circ\text{C}$ a $500^\circ\text{C}$), sensibilidad deseada $5\text{ mV/}^\circ\text{C}$ y $V_o = 0\text{ V}$ para $T = 0^\circ\text{C}$. Unión fría en $T_a \in [5^\circ\text{C}, 40^\circ\text{C}]$, compensada con una Pt100 ($R_0 = 100\,\Omega, \alpha = 0.00385\,^\circ\text{C}^{-1}$) excitada con corriente $I = 10\text{ mA}$ y tensión auxiliar $V_{comp}$.
Curva del termopar:
$$V_i(T) = 0.052\,\frac{\text{mV}}{^\circ\text{C}} \cdot T + 4.5 \times 10^{-6}\,\frac{\text{mV}}{(^\circ\text{C})^2} \cdot T^2$$

**Se pide:**
1. Estimar la sensibilidad media $s_T$ ($0^\circ\text{C}$ a $500^\circ\text{C}$) y $s_{Ta}$ ($5^\circ\text{C}$ a $40^\circ\text{C}$).
2. Calcular $V_{comp}$ para que $V_c = 0\text{ V}$ a $T_a = 0^\circ\text{C}$, y hallar la sensibilidad de $V_c$ frente a $T_a$.
3. Expresión de $V_o$ en función de $V_i, V_c, G, R_1$ y $R_2$.
4. Calcular $G$ y la relación $R_1/R_2$ para cumplir la sensibilidad deseada e inmunidad a $T_a$.
5. Ruido del amplificador en la banda $0.01\text{ Hz}$ a $100\text{ Hz}$: densidad de ruido blanco $8\text{ nV}/\sqrt{\text{Hz}}$, densidad a $0.1\text{ Hz} = 20\text{ nV}/\sqrt{\text{Hz}}$. Estimar la incertidumbre típica en temperatura $u(T)_{\text{ruido}}$ asociada.

---

### Solución Oficial Paso a Paso

#### 1. Sensibilidades del Termopar
$$\frac{\partial V_i}{\partial T} = 0.052 + 9 \times 10^{-6} T$$
- En $0^\circ\text{C}$: $0.052\text{ mV/}^\circ\text{C}$
- En $500^\circ\text{C}$: $0.052 + 9 \times 10^{-6}(500) = 0.0565\text{ mV/}^\circ\text{C}$
$$s_T = \frac{0.052 + 0.056}{2} = \mathbf{0.054\text{ mV/}^\circ\text{C}}$$
$$s_{Ta} = \mathbf{-0.052\text{ mV/}^\circ\text{C}}$$

---

#### 2. Circuito de Compensación Pt100
$$V_c = V_{comp} + I \cdot R_{Pt100} = V_{comp} + 10\text{ mA} \cdot 100\,\Omega(1 + \alpha T_a)$$
Para $V_c = 0$ a $T_a = 0^\circ\text{C}$:
$$V_{comp} = -10\text{ mA} \cdot 100\,\Omega = \mathbf{-1\text{ V}}$$
$$V_c(T_a) = 1\text{ V} \cdot \alpha \cdot T_a = 3.85\,\frac{\text{mV}}{^\circ\text{C}} \cdot T_a \implies \mathbf{\frac{\partial V_c}{\partial T_a} = 3.85\text{ mV/}^\circ\text{C}}$$

---

#### 3 y 4. Relación de Salida y Diseño
Por superposición (polaridad invertida en entrada del A.I.):
$$V_o = V_i \cdot G \cdot \frac{R_2}{R_1} + V_c \cdot \left(1 + \frac{R_2}{R_1}\right)$$
Sustituyendo $V_i = |s_T| T - |s_{Ta}| T_a$ y $V_c = 3.85 \cdot T_a$:
$$\frac{\partial V_o}{\partial T} = |s_T| \cdot G \cdot \frac{R_2}{R_1} = 5\text{ mV/}^\circ\text{C}$$
$$G \cdot \frac{R_2}{R_1} = \frac{5\text{ mV/}^\circ\text{C}}{0.054\text{ mV/}^\circ\text{C}} = 92.59 \cong 92.6$$

Cancelación del efecto de la temperatura ambiente $T_a$:
$$|s_{Ta}| \cdot G \cdot \frac{R_2}{R_1} = 3.85 \cdot \left(1 + \frac{R_2}{R_1}\right)$$
$$0.052 \cdot 92.6 = 3.85 \cdot \left(1 + \frac{R_2}{R_1}\right) \implies 4.815 = 3.85 \cdot \left(1 + \frac{R_2}{R_1}\right)$$
$$1 + \frac{R_2}{R_1} = 1.2506 \implies \frac{R_2}{R_1} = 0.274 \implies \mathbf{\frac{R_1}{R_2} = 3.65}$$
$$\mathbf{G = \frac{92.6}{0.274} = 337.2}$$

---

#### 5. Separación Espectral de Ruido e Incertidumbre
- Banda equivalente: $B = 0.01\text{ Hz}$ a $100\text{ Hz}$.
- Densidad de ruido blanco: $e_{nw} = 8\text{ nV}/\sqrt{\text{Hz}}$.
- Densidad a $0.1\text{ Hz}$: $e_n(0.1\text{ Hz}) = 20\text{ nV}/\sqrt{\text{Hz}}$.
  $$e_{n,1/f}(0.1\text{ Hz}) = \sqrt{20^2 - 8^2} = 18.33\text{ nV}/\sqrt{\text{Hz}}$$
  $$e_{n,1/f}(1\text{ Hz}) = \frac{18.33}{\sqrt{10}} \cong 5.8\text{ nV}/\sqrt{\text{Hz}} \approx 6\text{ nV}/\sqrt{\text{Hz}}$$

Integrando cada componente:
$$\sigma_{blanco} = 8\text{ nV}/\sqrt{\text{Hz}} \cdot \sqrt{100 - 0.01} = 80\text{ nV}$$
$$\sigma_{1/f} = 6\text{ nV}/\sqrt{\text{Hz}} \cdot \sqrt{\ln\left(\frac{100}{0.01}\right)} = 6 \cdot \sqrt{9.21} = 18.2\text{ nV}$$
$$\sigma_{ruido} = \sqrt{(80)^2 + (18.2)^2} = \mathbf{82\text{ nV}}$$

Refiriendo a incertidumbre típica en temperatura:
$$u(T)_{\text{ruido}} = \frac{\sigma_{ruido}}{s_T} = \frac{82 \times 10^{-9}\text{ V}}{0.054 \times 10^{-3}\text{ V/}^\circ\text{C}} = \mathbf{1.52 \times 10^{-3}{}^\circ\text{C}}$$

---
*Documento compilado y verificado con máxima fidelidad técnica para la asignatura Sistemes de Mesura (UPC EEBE / ETSETB).*
