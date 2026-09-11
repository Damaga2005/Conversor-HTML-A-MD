# 📐 Banco Maestro de Problemas de Cálculo de Examen · Sistemes de Mesura
> 🏛️ **Universitat Politècnica de Catalunya (UPC · EEBE / ETSETB)**  
> 📚 **Guía de Problemas Numéricos de Alta Complejidad con Resolución Paso a Paso en $\LaTeX$**  
> ⚡ **Formato optimizado para preparación de parciales, finales y carga en Google NotebookLM**

---

## 📑 Índice de Problemas

1. [Problema 1: Cadena Piezorresistiva con Galgas Extensométricas en Flexión](#problema-1-cadena-piezorresistiva-con-galgas-extensom%C3%A9tricas-en-flexi%C3%B3n)
2. [Problema 2: Termorresistencia Pt100 y Compensación de Resistencia de Línea (2, 3 y 4 Hilos)](#problema-2-termorresistencia-pt100-y-compensaci%C3%B3n-de-resistencia-de-l%C3%ADnea-2-3-y-4-hilos)
3. [Problema 3: Amplificador de Instrumentación (INA) y Rechazo en Modo Común (CMRR)](#problema-3-amplificador-de-instrumentaci%C3%B3n-ina-y-rechazo-en-modo-com%C3%BAn-cmrr)
4. [Problema 4: Ruido Térmico Johnson-Nyquist y Ancho de Banda Equivalente de Ruido (ENBW)](#problema-4-ruido-t%C3%A9rmico-johnson-nyquist-y-ancho-de-banda-equivalente-de-ruido-enbw)
5. [Problema 5: Filtro Activo Sallen-Key Butterworth de 2º Orden y Atenuación de Red](#problema-5-filtro-activo-sallen-key-butterworth-de-2%C2%BA-orden-y-atenuaci%C3%B3n-de-red)
6. [Problema 6: Conversor Analógico-Digital (ADC), Cuantificación y Rango Dinámico (ENOB)](#problema-6-conversor-anal%C3%B3gico-digital-adc-cuantificaci%C3%B3n-y-rango-din%C3%A1mico-enob)
7. [Problema 7: Circuito de Muestreo y Retención (Sample & Hold) y Criterio de Apertura](#problema-7-circuito-de-muestreo-y-retenci%C3%B3n-sample--hold-y-criterio-de-apertura)
8. [Problema 8: Evaluación de Incertidumbre Combinada y Expandida (Guía GUM)](#problema-8-evaluaci%C3%B3n-de-incertidumbre-combinada-y-expandida-gu%C3%ADa-gum)
9. [Problema 9: Termopar Tipo K con Compensación Electrónica de Unión Fría](#problema-9-termopar-tipo-k-con-compensaci%C3%B3n-electr%C3%B3nica-de-uni%C3%B3n-fr%C3%ADa)
10. [Problema 10: Linealización de Termistor NTC mediante Resistencia Shunt en Paralelo](#problema-10-linealizaci%C3%B3n-de-termistor-ntc-mediante-resistencia-shunt-en-paralelo)

---

## Problema 1: Cadena Piezorresistiva con Galgas Extensométricas en Flexión

### Enunciado
Se instrumenta una viga en voladizo sometida a una carga puntual en su extremo libre para medir deformaciones mecánicas en el rango $\varepsilon \in [-1500, +1500]\,\mu\varepsilon$. Se utilizan galgas metálicas idénticas de constante nominal $R_0 = 120.0\,\Omega$ y factor de galga $K = 2.05$. El puente de medida se alimenta con una fuente de tensión estabilizada $V_s = 10.0\,\text{V}$.

Se consideran dos montajes experimentales:
1. **Montaje A (Cuarto de puente):** Una única galga activa en la cara superior ($R_1 = R_0 + \Delta R$) y tres resistencias fijas de precisión $R_2 = R_3 = R_4 = 120.0\,\Omega$.
2. **Montaje B (Medio puente push-pull):** Dos galgas activas, una en la cara superior sometida a tracción ($R_1 = R_0 + \Delta R$) y otra en la cara inferior simétrica sometida a compresión ($R_2 = R_0 - \Delta R$), con dos resistencias fijas $R_3 = R_4 = 120.0\,\Omega$.

**Se pide:**
1. Calcular la variación de resistencia máxima $\Delta R_{\max}$ correspondiente a $\varepsilon = +1500\,\mu\varepsilon$.
2. Deducir la expresión exacta de la tensión de salida $V_o(\varepsilon)$ para ambos montajes.
3. Para $\varepsilon = +1500\,\mu\varepsilon$, calcular numéricamente la tensión de salida exacta y la tensión calculada mediante la aproximación lineal.
4. Determinar el error de no-linealidad relativo al fondo de escala ($\% \text{FSR}$) en el Montaje A y justificar el comportamiento del Montaje B.
5. Calcular la potencia disipada por cada galga y verificar si es inferior al límite de auto-calentamiento recomendado ($25\,\text{mW}$).

---

### Solución Paso a Paso

#### 1. Cálculo de la variación máxima de resistencia ($\Delta R_{\max}$)
La definición del factor de galga $K$ relaciona la deformación unitaria $\varepsilon$ con la variación fraccional de resistencia:
$$\begin{equation}
\frac{\Delta R}{R_0} = K \cdot \varepsilon
\end{equation}$$

Sustituyendo los valores para $\varepsilon = +1500\,\mu\varepsilon = 1500 \times 10^{-6}$:
$$\begin{equation}
\frac{\Delta R}{R_0} = 2.05 \times (1500 \times 10^{-6}) = 3.075 \times 10^{-3} = 0.3075\%
\end{equation}$$
$$\begin{equation}
\Delta R_{\max} = R_0 \cdot (K \cdot \varepsilon) = 120.0\,\Omega \times 3.075 \times 10^{-3} = 0.369\,\Omega
\end{equation}$$

#### 2. Deducción de la tensión de salida $V_o(\varepsilon)$

**Montaje A (Cuarto de Puente):**
La tensión entre las ramas del puente de Wheatstone viene dada por:
$$\begin{equation}
V_o = V_s \left( \frac{R_1}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)
\end{equation}$$
Como $R_2 = R_3 = R_4 = R_0$ y $R_1 = R_0 + \Delta R$:
$$\begin{equation}
V_o = V_s \left( \frac{R_0 + \Delta R}{2 R_0 + \Delta R} - \frac{1}{2} \right) = \frac{V_s}{4} \frac{\frac{\Delta R}{R_0}}{1 + \frac{1}{2}\frac{\Delta R}{R_0}}
\end{equation}$$

Aproximación lineal para $\Delta R \ll R_0$:
$$\begin{equation}
V_{o,\text{aprox}} = \frac{V_s}{4} \frac{\Delta R}{R_0} = \frac{V_s}{4} K \varepsilon
\end{equation}$$

**Montaje B (Medio Puente Push-Pull):**
Con $R_1 = R_0 + \Delta R$, $R_2 = R_0 - \Delta R$ y $R_3 = R_4 = R_0$:
$$\begin{equation}
V_o = V_s \left( \frac{R_0 + \Delta R}{(R_0 + \Delta R) + (R_0 - \Delta R)} - \frac{1}{2} \right) = \frac{V_s}{2} \frac{\Delta R}{R_0} = \frac{V_s}{2} K \varepsilon
\end{equation}$$
*(Relación exactamente lineal, sin términos de orden superior en el denominador)*.

#### 3. Cálculo numérico para $\varepsilon = +1500\,\mu\varepsilon$ ($x = \Delta R / R_0 = 0.003075$)

- **Montaje A:**
  $$\begin{equation}
  V_{o,\text{exacta}} = \frac{10.0}{4} \times \frac{0.003075}{1 + 0.5 \times 0.003075} = 2.5 \times \frac{0.003075}{1.0015375} \approx 7.6757\,\text{mV}
  \end{equation}$$
  $$\begin{equation}
  V_{o,\text{aprox}} = \frac{10.0}{4} \times 0.003075 = 7.6875\,\text{mV}
  \end{equation}$$

- **Montaje B:**
  $$\begin{equation}
  V_o = \frac{10.0}{2} \times 0.003075 = 15.3750\,\text{mV}
  \end{equation}$$
  *(Proporciona exactamente el doble de sensibilidad: $15.375\,\text{mV}$ frente a $7.676\,\text{mV}$)*.

#### 4. Error de no linealidad ($\% \text{FSR}$)
El error absoluto de linealidad en el Montaje A es:
$$\begin{equation}
e_{NL} = V_{o,\text{exacta}} - V_{o,\text{aprox}} = 7.6757\,\text{mV} - 7.6875\,\text{mV} = -0.0118\,\text{mV} = -11.8\,\mu\text{V}
\end{equation}$$

Como el fondo de escala diferencial total va de $-7.676\,\text{mV}$ a $+7.676\,\text{mV}$ ($\text{FSR} = 15.351\,\text{mV}$):
$$\begin{equation}
\varepsilon_{NL} = \frac{|-0.0118\,\text{mV}|}{15.351\,\text{mV}} \times 100\% \approx 0.0768\% \approx 0.08\%
\end{equation}$$

En el **Montaje B**, el término $\Delta R$ del denominador se cancela algebraicamente:
$$\begin{equation}
\varepsilon_{NL,\text{Montaje B}} = 0.000\% \quad \text{(Linealidad teórica perfecta)}
\end{equation}$$

#### 5. Potencia disipada y autocalentamiento
En reposo, la tensión en cada galga es $V_{\text{galga}} = V_s / 2 = 5.0\,\text{V}$.
$$\begin{equation}
P = \frac{V_{\text{galga}}^2}{R_0} = \frac{(5.0\,\text{V})^2}{120\,\Omega} = \frac{25}{120}\,\text{W} \approx 0.2083\,\text{W} = 208.3\,\text{mW}
\end{equation}$$

> [!WARNING]
> $208.3\,\text{mW}$ excede el límite recomendado de $25\,\text{mW}$ para galgas sobre soportes metálicos o polímeros, provocando derivas térmicas por autocalentamiento.
> En diseño real se debe reducir $V_s$ a $2.0\,\text{V}$ ($P \approx 8.33\,\text{mW}$) o usar galgas de $350\,\Omega$.

---

## Problema 2: Termorresistencia Pt100 y Compensación de Resistencia de Línea (2, 3 y 4 Hilos)

### Enunciado
Se utiliza una sonda de temperatura industrial Pt100 ($R_0 = 100.0\,\Omega$ a $0.0^\circ\text{C}$, $\alpha = 3.85 \times 10^{-3}\,{}^\circ\text{C}^{-1}$) ubicada a 40 metros de la sala de control. El cable de conexión de cobre introduce una resistencia parásita por hilo $R_L = 2.50\,\Omega$.

La sonda opera en el rango de $T \in [0^\circ\text{C}, 150^\circ\text{C}]$, donde $R(T) = R_0 (1 + \alpha T)$.

Se evalúan 3 configuraciones de conexionado:
1. **Conexión a 2 hilos:** La sonda está en serie directa con ambos hilos de ida y vuelta ($2 R_L$) hacia un puente de Wheatstone equilibrado a $0^\circ\text{C}$ ($R_2 = R_3 = R_4 = 100.0\,\Omega$).
2. **Conexión a 3 hilos (Siemens):** Un hilo de alimentación en el nodo común y dos hilos de medida balanceados en ramas opuestas del puente.
3. **Conexión a 4 hilos (Kelvin):** Alimentación con fuente de corriente constante $I_{\text{bias}} = 1.00\,\text{mA}$ por dos hilos y medida de tensión con amplificador de alta impedancia ($R_{\text{in}} > 10\,\text{G}\Omega$) por los otros dos hilos.

**Se pide:**
1. Para $T = 50.0^\circ\text{C}$, calcular la resistencia real $R(50^\circ\text{C})$ de la Pt100.
2. En la conexión a 2 hilos, calcular la resistencia aparente medida $R_{\text{aparente}}$ y el error de temperatura inducido en grados Celsius ($\Delta T_{\text{error}}$).
3. En la conexión a 3 hilos, deducir la tensión de desequilibrio del puente con $V_s = 5.0\,\text{V}$ y demostrar que el efecto de primer orden de $R_L$ se anula a $0^\circ\text{C}$.
4. En la conexión a 4 hilos, calcular la tensión leída a $0^\circ\text{C}$ y a $150^\circ\text{C}$, y justificar por qué el error por resistencia de cable es estrictamente nulo.

---

### Solución Paso a Paso

#### 1. Resistencia real a $50.0^\circ\text{C}$
$$\begin{equation}
R(50^\circ\text{C}) = 100.0 \times [1 + 3.85 \times 10^{-3} \times 50.0] = 119.25\,\Omega
\end{equation}$$
Sensibilidad: $S_{RTD} = R_0 \alpha = 0.385\,\Omega/{}^\circ\text{C}$.

#### 2. Conexión a 2 hilos: Error inducido
$$\begin{equation}
R_{\text{aparente}} = R(T) + 2 R_L = 119.25\,\Omega + 2 \times 2.50\,\Omega = 124.25\,\Omega
\end{equation}$$
$$\begin{equation}
T_{\text{aparente}} = \frac{124.25 - 100.0}{0.385} \approx 62.99^\circ\text{C}
\end{equation}$$
$$\begin{equation}
\Delta T_{\text{error}} = T_{\text{aparente}} - T_{\text{real}} = \frac{2 R_L}{R_0 \alpha} = \frac{5.00\,\Omega}{0.385\,\Omega/{}^\circ\text{C}} \approx +12.99^\circ\text{C}
\end{equation}$$

#### 3. Conexión a 3 hilos (Montaje Siemens)
Al conectar un hilo en serie con la Pt100 en la rama superior y otro hilo en serie con la resistencia fija en la rama inferior:
$$\begin{equation}
V_o = V_s \left( \frac{R(T) + R_L}{R(T) + R_0 + 2 R_L} - \frac{1}{2} \right)
\end{equation}$$
A $T = 0^\circ\text{C}$, $R(0^\circ\text{C}) = R_0$:
$$\begin{equation}
V_o(0^\circ\text{C}) = V_s \left( \frac{R_0 + R_L}{2 R_0 + 2 R_L} - \frac{1}{2} \right) = 0.000\,\text{V}
\end{equation}$$
A $T = 50^\circ\text{C}$ con $V_s = 5.0\,\text{V}$:
$$\begin{equation}
V_o = 5.0 \times \left( \frac{119.25 + 2.50}{119.25 + 100.0 + 5.0} - 0.5 \right) = 5.0 \times \left( \frac{121.75}{224.25} - 0.5 \right) \approx +214.6\,\text{mV}
\end{equation}$$

#### 4. Conexión a 4 hilos (Método Kelvin)
Corriente inyectada constante: $I_{\text{bias}} = 1.00\,\text{mA}$.
Como el voltímetro digital tiene $R_{\text{in}} > 10^{10}\,\Omega$, la corriente por los hilos de medida es prácticamente nula ($I_{\text{sense}} \approx 10\,\text{pA}$):
$$\begin{equation}
V_{\text{error}} = 2 I_{\text{sense}} R_L \approx 50\,\text{pV} \approx 0.00\,\mu\text{V}
\end{equation}$$
- A $0.0^\circ\text{C}$: $V(0^\circ\text{C}) = 1.00\,\text{mA} \times 100.0\,\Omega = 100.00\,\text{mV}$.
- A $150.0^\circ\text{C}$: $V(150^\circ\text{C}) = 1.00\,\text{mA} \times 157.75\,\Omega = 157.75\,\text{mV}$.
**Error por cable:** $\Delta T = 0.000^\circ\text{C}$.

---

## Problema 3: Amplificador de Instrumentación (INA) y Rechazo en Modo Común (CMRR)

### Enunciado
Se diseña una etapa de acondicionamiento basada en la topología clásica de 3 amplificadores operacionales (INA3). La señal diferencial proviene de un puente de galgas con rango $V_d \in [0, 20.0\,\text{mV}]$. Se desea amplificar dicha señal para adaptarla a un microcontrolador con rango $V_o \in [0, 5.00\,\text{V}]$.

El circuito tiene resistencias internas en la primera etapa $R_1 = 25.0\,\text{k}\Omega$ y una resistencia de ganancia externa $R_g$. En la segunda etapa se emplean cuatro resistencias nominales $R_2 = R_3 = 10.0\,\text{k}\Omega$.

Existe una tensión de modo común parásita de $50\,\text{Hz}$ acoplada a los cables, de amplitud $V_{cm} = 2.50\,\text{V}_{\text{pico}}$.

**Se pide:**
1. Calcular el valor necesario de $R_g$ para obtener la ganancia diferencial nominal $G_d = 250$.
2. Si las resistencias de la segunda etapa ($R_2, R_3$) tienen una tolerancia de fabricación del $\pm 1\%$ ($\delta = 0.01$), calcular el $\text{CMRR}$ mínimo de la etapa diferencial y el $\text{CMRR}_{\text{total}}$ en decibelios.
3. Calcular la amplitud del error de modo común inducido en la salida $V_{o,cm}$ debido al desbalance de resistencias del $1\%$.
4. Si se sustituyen las resistencias por componentes de precisión del $\pm 0.1\%$ ($\delta = 0.001$), calcular la nueva tensión de error $V_{o,cm}$ y el nuevo $\text{CMRR}_{\text{dB}}$.

---

### Solución Paso a Paso

#### 1. Cálculo de la resistencia de ganancia $R_g$
$$\begin{equation}
G_d = \frac{5.00\,\text{V}}{0.020\,\text{V}} = 250 = 1 + \frac{2 R_1}{R_g} \implies 249 = \frac{50\,000\,\Omega}{R_g} \implies R_g = \frac{50\,000}{249} \approx 200.80\,\Omega
\end{equation}$$

#### 2. Cálculo del CMRR con tolerancia $\delta = 1\%$
$$\begin{equation}
A_{cm2,\text{peor caso}} \approx 4 \delta = 4 \times 0.01 = 0.04
\end{equation}$$
$$\begin{equation}
\text{CMRR} = \frac{G_1}{4 \delta} = \frac{250}{4 \times 0.01} = 6250
\end{equation}$$
$$\begin{equation}
\text{CMRR}_{\text{dB}} = 20 \log_{10}(6250) \approx 75.92\,\text{dB}
\end{equation}$$

#### 3. Tensión de error en la salida $V_{o,cm}$ para $\delta = 1\%$
$$\begin{equation}
V_{o,cm} = \frac{G_d}{\text{CMRR}} \cdot V_{cm} = 0.04 \times 2.50\,\text{V} = 0.100\,\text{V} = 100\,\text{mV} \quad (2.0\% \text{ del fondo de escala})
\end{equation}$$

#### 4. Con resistencias de precisión al $0.1\%$ ($\delta = 0.001$)
$$\begin{equation}
\text{CMRR} = \frac{250}{4 \times 0.001} = 62\,500 \implies \text{CMRR}_{\text{dB}} = 20 \log_{10}(62\,500) \approx 95.92\,\text{dB}
\end{equation}$$
$$\begin{equation}
V_{o,cm} = \frac{250}{62\,500} \times 2.50\,\text{V} = 10.0\,\text{mV} \quad (0.2\% \text{ del fondo de escala})
\end{equation}$$

---

## Problema 4: Ruido Térmico Johnson-Nyquist y Ancho de Banda Equivalente de Ruido (ENBW)

### Enunciado
Un sensor piezoeléctrico presenta una resistencia equivalente de salida $R_{\text{eq}} = 50.0\,\text{k}\Omega$ a una temperatura de $T = 27^\circ\text{C}$ ($300.15\,\text{K}$). La señal analógica útil es $V_{\text{señal}} = 5.0\,\text{mV}_{\text{rms}}$.

Para eliminar el ruido, se conecta un filtro paso bajo activo Butterworth de 1º orden con $f_c = 1.00\,\text{kHz}$. Constante de Boltzmann: $k_B = 1.3806 \times 10^{-23}\,\text{J/K}$.

**Se pide:**
1. Calcular la densidad espectral de ruido térmico $e_n$ en $\text{nV}/\sqrt{\text{Hz}}$.
2. Calcular el ancho de banda equivalente de ruido ($\text{ENBW}$) del filtro de 1º orden.
3. Calcular la tensión eficaz de ruido $v_{n,\text{rms}}$ a la salida del filtro.
4. Calcular la relación señal-ruido ($\text{SNR}$) en decibelios.
5. Comparar con un filtro Butterworth de 2º orden con la misma $f_c = 1.00\,\text{kHz}$.

---

### Solución Paso a Paso

#### 1. Densidad espectral de ruido térmico
$$\begin{equation}
e_n = \sqrt{4 k_B T R_{\text{eq}}} = \sqrt{4 \times (1.3806 \times 10^{-23}) \times 300.15 \times 50\,000} \approx 28.79\,\text{nV}/\sqrt{\text{Hz}}
\end{equation}$$

#### 2. Ancho de banda equivalente de ruido (1º orden)
$$\begin{equation}
\text{ENBW}_1 = \frac{\pi}{2} f_c \approx 1.5708 \times 1000\,\text{Hz} \approx 1570.8\,\text{Hz}
\end{equation}$$

#### 3. Tensión eficaz de ruido
$$\begin{equation}
v_{n,\text{rms}} = e_n \sqrt{\text{ENBW}_1} = (28.786 \times 10^{-9}) \times \sqrt{1570.8} \approx 1.141\,\mu\text{V}_{\text{rms}}
\end{equation}$$

#### 4. Relación Señal-Ruido (SNR)
$$\begin{equation}
\text{SNR}_{1,\text{dB}} = 20 \log_{10}\left( \frac{5.0 \times 10^{-3}}{1.1409 \times 10^{-6}} \right) \approx 72.83\,\text{dB}
\end{equation}$$

#### 5. Filtro Butterworth de 2º orden
$$\begin{equation}
\text{ENBW}_2 = \frac{\pi}{2\sqrt{2}} f_c \approx 1.1107 \times 1000\,\text{Hz} = 1110.7\,\text{Hz}
\end{equation}$$
$$\begin{equation}
v_{n2,\text{rms}} = (28.786 \times 10^{-9}) \times \sqrt{1110.7} \approx 0.9593\,\mu\text{V}_{\text{rms}}
\end{equation}$$
$$\begin{equation}
\text{SNR}_{2,\text{dB}} = 20 \log_{10}\left( \frac{5.0 \times 10^{-3}}{0.9593 \times 10^{-6}} \right) \approx 74.34\,\text{dB} \quad (\Delta \text{SNR} = +1.51\,\text{dB})
\end{equation}$$

---

## Problema 5: Filtro Activo Sallen-Key Butterworth de 2º Orden y Atenuación de Red

### Enunciado
Se diseña un filtro anti-aliasing Sallen-Key paso bajo con respuesta Butterworth ($Q = 1/\sqrt{2}$) y frecuencia de corte $f_c = 15.0\,\text{Hz}$ para atenuar la interferencia de red de $50.0\,\text{Hz}$. Se eligen $C_1 = 1.0\,\mu\text{F}$, $C_2 = 0.50\,\mu\text{F}$ y resistencias iguales $R_1 = R_2 = R$.

**Se pide:**
1. Demostrar la condición de diseño Butterworth ($C_1 = 2 C_2$).
2. Calcular el valor necesario de $R$.
3. Calcular la atenuación en decibelios a $50.0\,\text{Hz}$.
4. Calcular el desfase $\phi$ introducido a $50.0\,\text{Hz}$.

---

### Solución Paso a Paso

#### 1. Condición Butterworth
Para $R_1 = R_2 = R$, $Q = \frac{1}{2} \sqrt{\frac{C_1}{C_2}}$.
Para respuesta Butterworth: $Q = \frac{1}{\sqrt{2}} \implies \sqrt{\frac{C_1}{C_2}} = \sqrt{2} \implies C_1 = 2 C_2$ (se cumple con $1.0\,\mu\text{F}$ y $0.5\,\mu\text{F}$).

#### 2. Cálculo de $R$
$$\begin{equation}
\omega_0 = 2\pi \times 15.0 \approx 94.248\,\text{rad/s}, \quad \sqrt{C_1 C_2} = \sqrt{0.5 \times 10^{-12}} \approx 7.0711 \times 10^{-7}\,\text{F}
\end{equation}$$
$$\begin{equation}
R = \frac{1}{\omega_0 \sqrt{C_1 C_2}} = \frac{1}{94.248 \times 7.0711 \times 10^{-7}} \approx 15.0\,\text{k}\Omega
\end{equation}$$

#### 3. Atenuación a $50\,\text{Hz}$
$$\begin{equation}
|H(f)| = \frac{1}{\sqrt{1 + (f/f_c)^4}} = \frac{1}{\sqrt{1 + (50/15)^4}} = \frac{1}{\sqrt{1 + (3.333)^4}} \approx \frac{1}{\sqrt{124.46}} \approx 0.08964
\end{equation}$$
$$\begin{equation}
|H(50\,\text{Hz})|_{\text{dB}} = 20 \log_{10}(0.08964) \approx -20.95\,\text{dB}
\end{equation}$$

#### 4. Desfase a $50\,\text{Hz}$
$$\begin{equation}
\phi(50\,\text{Hz}) = -\left(180^\circ - \arctan\left( \frac{\sqrt{2} \times 3.333}{(3.333)^2 - 1} \right)\right) \approx -(180^\circ - 25.0^\circ) = -155.0^\circ
\end{equation}$$

---

## Problema 6: Conversor Analógico-Digital (ADC), Cuantificación y Rango Dinámico (ENOB)

### Enunciado
Un ADC de $N=16$ bits opera con rango unipolar $V_{\text{in}} \in [0, 4.096\,\text{V}]$. Especificaciones: $\text{SINAD} = 86.4\,\text{dB}$, $\text{INL} = \pm 1.5\,\text{LSB}$.

**Se pide:**
1. Calcular el escalón de cuantificación $q$ ($\text{LSB}$) en $\mu\text{V}$.
2. Calcular la tensión eficaz del ruido de cuantificación ideal $v_{q,\text{rms}}$.
3. Calcular la $\text{SNR}_{\text{ideal}}$ teórica.
4. Calcular el Número Efectivo de Bits ($\text{ENOB}$).
5. Calcular el error de tensión absoluto asociado al $\text{INL}$.

---

### Solución Paso a Paso

#### 1. Escalón de cuantificación
$$\begin{equation}
q = \text{LSB} = \frac{4.096\,\text{V}}{2^{16}} = \frac{4.096}{65\,536} = 62.5\,\mu\text{V}
\end{equation}$$

#### 2. Tensión eficaz del ruido de cuantificación
$$\begin{equation}
v_{q,\text{rms}} = \frac{q}{\sqrt{12}} = \frac{62.5\,\mu\text{V}}{\sqrt{12}} \approx 18.04\,\mu\text{V}_{\text{rms}}
\end{equation}$$

#### 3. $\text{SNR}_{\text{ideal}}$
$$\begin{equation}
\text{SNR}_{\text{ideal}} = 6.02 \times N + 1.76 = 6.02 \times 16 + 1.76 = 98.08\,\text{dB}
\end{equation}$$

#### 4. $\text{ENOB}$
$$\begin{equation}
\text{ENOB} = \frac{\text{SINAD} - 1.76}{6.02} = \frac{86.4 - 1.76}{6.02} \approx 14.1\,\text{bits}
\end{equation}$$

#### 5. Error por $\text{INL}$
$$\begin{equation}
e_{\text{INL}} = \pm 1.5 \times 62.5\,\mu\text{V} = \pm 93.75\,\mu\text{V}
\end{equation}$$

---

## Problema 7: Circuito de Muestreo y Retención (Sample & Hold) y Criterio de Apertura

### Enunciado
S&H para ADC de 14 bits ($N=14$, $\text{FSR} = 5.00\,\text{V}$) con condensador $C_H = 1.0\,\text{nF}$, $R_{\text{on}} = 50\,\Omega$, $R_s = 50\,\Omega$, corriente de fuga $I_{\text{fuga}} = 200\,\text{pA}$, jitter de apertura $t_a = 60\,\text{ps}$.

**Se pide:**
1. Tiempo mínimo de adquisición $t_{\text{acq}}$ para error $< \frac{1}{2}\text{LSB}$.
2. Tasa de caída (*droop rate*) en $\text{mV/s}$.
3. Caída de tensión durante $t_{\text{hold}} = 10.0\,\mu\text{s}$.
4. Frecuencia analógica máxima $f_{\max}$ para error de jitter $< 1\,\text{LSB}$.

---

### Solución Paso a Paso

#### 1. Tiempo de adquisición
$$\begin{equation}
\tau = (R_s + R_{\text{on}}) C_H = 100\,\Omega \times 1.0\,\text{nF} = 100\,\text{ns}
\end{equation}$$
$$\begin{equation}
t_{\text{acq}} \ge \tau \ln(2^{15}) = 15 \tau \ln(2) \approx 10.397 \times 100\,\text{ns} \approx 1.04\,\mu\text{s}
\end{equation}$$

#### 2. Tasa de caída
$$\begin{equation}
\frac{dV}{dt} = \frac{I_{\text{fuga}}}{C_H} = \frac{200 \times 10^{-12}}{1.0 \times 10^{-9}} = 0.200\,\text{V/s} = 200\,\text{mV/s}
\end{equation}$$

#### 3. Caída de tensión en $10.0\,\mu\text{s}$
$$\begin{equation}
\Delta V_{\text{droop}} = 0.200\,\text{V/s} \times 10.0\,\mu\text{s} = 2.0\,\mu\text{V} \ll \frac{1}{2}\text{LSB} \approx 152.6\,\mu\text{V}
\end{equation}$$

#### 4. Frecuencia máxima por jitter
$$\begin{equation}
f_{\max} \le \frac{1}{2^N \pi t_a} = \frac{1}{16\,384 \times \pi \times 60 \times 10^{-12}} \approx 323.8\,\text{kHz}
\end{equation}$$

---

## Problema 8: Evaluación de Incertidumbre Combinada y Expandida (Guía GUM)

### Enunciado
Calibración de presión a $p_0 = 100.00\,\text{kPa}$. 6 lecturas: $\{ 100.12, 100.08, 100.15, 100.10, 100.14, 100.09 \}\,\text{kPa}$. Resolución display: $0.01\,\text{kPa}$ (rectangular). Patrón: $U = 0.040\,\text{kPa}$ ($k=2$, normal). Temperatura: $\pm 2^\circ\text{C}$ con $0.008\,\text{kPa/}^\circ\text{C}$ (triangular).

**Se pide:**
1. Media muestral $\bar{p}$ e incertidumbre Tipo A $u_A$.
2. Componentes Tipo B ($u_{B,\text{res}}$, $u_{B,\text{patr}}$, $u_{B,\text{temp}}$).
3. Incertidumbre combinada $u_c$.
4. Grados efectivos $\nu_{\text{eff}}$ (Welch-Satterthwaite).
5. Incertidumbre expandida $U$ ($95.45\%$, $k=2$) y resultado final.

---

### Solución Paso a Paso

#### 1. Tipo A
$$\begin{equation}
\bar{p} = 100.1133\,\text{kPa}, \quad s = 0.02805\,\text{kPa}, \quad u_A = \frac{s}{\sqrt{6}} \approx 0.01145\,\text{kPa} \quad (\nu_A = 5)
\end{equation}$$

#### 2. Tipo B
$$\begin{equation}
u_{B,\text{res}} = \frac{0.005}{\sqrt{3}} \approx 0.00289\,\text{kPa}, \quad u_{B,\text{patr}} = \frac{0.040}{2} = 0.02000\,\text{kPa}, \quad u_{B,\text{temp}} = \frac{0.016}{\sqrt{6}} \approx 0.00653\,\text{kPa}
\end{equation}$$

#### 3. Incertidumbre combinada
$$\begin{equation}
u_c = \sqrt{0.01145^2 + 0.00289^2 + 0.02000^2 + 0.00653^2} \approx \sqrt{5.821 \times 10^{-4}} \approx 0.02413\,\text{kPa}
\end{equation}$$

#### 4. Grados de libertad efectivos
$$\begin{equation}
\nu_{\text{eff}} = \frac{u_c^4}{(u_A^4 / 5)} = \frac{(0.02413)^4}{(0.01145^4 / 5)} \approx 98.5 \gg 30 \implies \text{Normal estándar válida}
\end{equation}$$

#### 5. Resultado final
$$\begin{equation}
U = 2.00 \times 0.02413\,\text{kPa} \approx 0.048\,\text{kPa}
\end{equation}$$
$$\begin{equation}
p = (100.11 \pm 0.05)\,\text{kPa} \quad (k=2, \; 95.45\% \text{ confianza})
\end{equation}$$

---

## Problema 9: Termopar Tipo K con Compensación Electrónica de Unión Fría

### Enunciado
Termopar tipo K ($S_{AB} = 41.2\,\mu\text{V/}^\circ\text{C}$) mide $T = 450^\circ\text{C}$. Unión fría en bornes a $T_{\text{amb}} = 25.0^\circ\text{C}$. Sensor auxiliar con $S_{\text{comp}} = 10.0\,\text{mV/}^\circ\text{C}$.

**Se pide:**
1. Tensión bruta del termopar $V_{\text{termopar}}$.
2. Error de lectura si no se compensa.
3. Factor atenuador del divisor resistivo $\beta$.
4. Demostración de invariancia si $T_{\text{amb}}$ sube a $35^\circ\text{C}$.

---

### Solución Paso a Paso

#### 1. Tensión bruta
$$\begin{equation}
V_{\text{termopar}} = (41.2\,\mu\text{V} \times 450) - (41.2\,\mu\text{V} \times 25) = 18.540\,\text{mV} - 1.030\,\text{mV} = 17.510\,\text{mV}
\end{equation}$$

#### 2. Error sin compensación
$$\begin{equation}
T_{\text{leída}} = \frac{17.510}{0.0412} = 425.0^\circ\text{C} \implies \Delta T = -25.0^\circ\text{C}
\end{equation}$$

#### 3. Factor atenuador
$$\begin{equation}
\beta = \frac{S_{AB}}{S_{\text{comp}}} = \frac{41.2\,\mu\text{V}}{10\,000\,\mu\text{V}} = 4.12 \times 10^{-3} \implies \frac{R_2}{R_1 + R_2} = 0.00412 \implies R_1 \approx 241.7 R_2
\end{equation}$$

#### 4. Invarianza a $35^\circ\text{C}$
- $V_{\text{termopar}}(450, 35) = 18.540 - 1.442 = 17.098\,\text{mV}$.
- $V_{\text{comp}}^* = 41.2\,\mu\text{V} \times 35 = 1.442\,\text{mV}$.
- $V_{\text{total}} = 17.098 + 1.442 = 18.540\,\text{mV} \implies T = 450.0^\circ\text{C}$ (Exacto).

---

## Problema 10: Linealización de Termistor NTC mediante Resistencia Shunt en Paralelo

### Enunciado
Termistor NTC con $R_0 = 10.0\,\text{k}\Omega$ a $T_0 = 25^\circ\text{C}$ ($298.15\,\text{K}$), $\beta = 3950\,\text{K}$. Rango: $[20^\circ\text{C}, 60^\circ\text{C}]$, centro $T_c = 40^\circ\text{C}$ ($313.15\,\text{K}$). Se coloca $R_p$ en paralelo: $R_{\text{eq}} = \frac{R(T) R_p}{R(T) + R_p}$.

**Se pide:**
1. Resistencia del termistor a $20^\circ\text{C}$, $40^\circ\text{C}$, $60^\circ\text{C}$.
2. Fórmula del punto de inflexión $\left. \frac{d^2 R_{\text{eq}}}{dT^2} \right|_{T_c} = 0$.
3. Valor óptimo de $R_p$.
4. Comparación de linealidad con y sin $R_p$.

---

### Solución Paso a Paso

#### 1. Valores de resistencia del NTC
- $R(20^\circ\text{C}) \approx 12\,535\,\Omega = 12.54\,\text{k}\Omega$
- $R(40^\circ\text{C}) \approx 5302\,\Omega = 5.302\,\text{k}\Omega$
- $R(60^\circ\text{C}) \approx 2487\,\Omega = 2.487\,\text{k}\Omega$

#### 2. Condición analítica del punto de inflexión
$$\begin{equation}
R_p = R(T_c) \cdot \frac{\beta - 2 T_c}{\beta + 2 T_c} \quad (T_c \text{ en Kelvin})
\end{equation}$$

#### 3. Cálculo de $R_p$
$$\begin{equation}
\frac{3950 - 2(313.15)}{3950 + 2(313.15)} = \frac{3323.7}{4576.3} \approx 0.7263
\end{equation}$$
$$\begin{equation}
R_p = 5302\,\Omega \times 0.7263 \approx 3851\,\Omega = 3.85\,\text{k}\Omega
\end{equation}$$

#### 4. Comparativa de linealidad
Con $R_p = 3851\,\Omega$:
- $R_{\text{eq}}(20^\circ\text{C}) \approx 2946\,\Omega$
- $R_{\text{eq}}(40^\circ\text{C}) \approx 2231\,\Omega$
- $R_{\text{eq}}(60^\circ\text{C}) \approx 1511\,\Omega$

- Sin $R_p$: $\Delta R_{20\to 40} = 7233\,\Omega$ vs $\Delta R_{40\to 60} = 2815\,\Omega$ (Asimetría $2.57 \implies > 35\%$ de no-linealidad).
- Con $R_p$: $\Delta R_{\text{eq}, 20\to 40} = 715\,\Omega$ vs $\Delta R_{\text{eq}, 40\to 60} = 720\,\Omega$ (Diferencia de solo $5\,\Omega$ sobre $720\,\Omega \implies < 0.7\%$ de no-linealidad).

---
*Documento maestro de problemas oficiales de examen · Sistemes de Mesura (UPC)*
