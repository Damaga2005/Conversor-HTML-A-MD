# 🍏 Conversor HTML a Markdown para Google NotebookLM & LLMs

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Interface: Apple Dark](https://img.shields.io/badge/UI-Apple%20Dark%20Mode-black.svg)]()
[![Target: NotebookLM](https://img.shields.io/badge/Optimized%20for-Google%20NotebookLM-4285F4.svg)]()
[![LaTeX: MathML Supported](https://img.shields.io/badge/LaTeX-MathML%20%E2%86%92%20LaTeX-brightgreen.svg)]()

> Suite integral de ingeniería documental y aplicación de escritorio diseñada para convertir contenidos educativos web e interactivos (HTML, MathML, scripts de autoevaluación) en **Markdown técnico de alta fidelidad**, 100% optimizado para la base de conocimiento de **Google NotebookLM**, Gemini, Claude y ChatGPT.
> 
> Incluye adaptación completa para la asignatura **Sistemes de Mesura (EEBE · Universitat Politècnica de Catalunya)** con 500 preguntas oficiales de examen, formulario consolidado de ecuaciones y simulador interactivo.

---

## ✨ Características Principales

### 🧠 1. Motor de Conversión de Alta Fidelidad (HTML → Markdown)
- **Matemáticas en LaTeX puro:** Convierte MathML nativo (`<math>`, `<mrow>`, `<mfrac>`, `<msub>`, etc.) y etiquetas de notación técnica en $\LaTeX$ estándar (`$...$` inline y `$$...$$` display) perfectamente interpretables por NotebookLM y KaTeX.
- **Extracción Inteligente de Imágenes:** Decodifica imágenes embebidas en Base64 y recursos enlazados, guardándolos ordenadamente en la subcarpeta `assets/` con nombres normalizados y hashing SHA-256 para prevenir duplicados.
- **Callouts Semánticos Modernos:** Transforma bloques destacados y notas docentes en callouts de GitHub Flavored Markdown (`> [!NOTE]`, `> [!WARNING]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!CAUTION]`).
- **Tablas Complejas y Código:** Limpia y preserva la alineación de tablas HTML, bloques de código preformateado y estructuras de listas anidadas.
- **Reescritura de Enlaces Locales:** Convierte automáticamente referencias internas `.html` en sus correspondientes ficheros `.md`, garantizando una navegación cruzada fluida.

---

### 🎨 2. Interfaz Gráfica de Escritorio (Apple Dark Aesthetic)
- **Diseño Apple macOS:** Paleta cromática oscura de alto contraste (`#000000`, `#1c1c1e`, `#2c2c2e`, acentos `#0a84ff` y `#30d158`), tipografía San Francisco / Segoe UI y tarjetas de profundidad visual.
- **Drag & Drop Nativo en Windows:** Arrastra archivos HTML individuales o carpetas de cursos completas directamente a la ventana de la aplicación.
- **Visor Markdown Integrado & Exportador HTML/PDF:** Lee los documentos generados directamente en la app con resaltado de sintaxis, conteo de palabras y buscador con resaltado en tiempo real. Incluye botón **"🌐 Exportar HTML / PDF"** para generar documentos web imprimibles con MathJax 3 y estilos de impresión para guardar en PDF con 1 clic.
- **Barra de Productividad:** Controles de zoom tipográfico dinámico (**A-**, **100%**, **A+**) y badge de estadísticas en vivo con conteo de palabras, caracteres, fórmulas $\LaTeX$, tablas e imágenes, junto al tiempo estimado de lectura.
- **Acceso Directo a la Nube & Exámenes:** Botón para abrir directamente [Google NotebookLM](https://notebooklm.google.com/) en tu navegador, y atajo **"🎓 Finales UPC"** para cargar de inmediato los exámenes oficiales resueltos.

---

### 📐 3. Calculadora Metrológica GUM (ISO/IEC 98-3) & Motor Monte Carlo (Supl. 1)
- **Pestaña Nativa en la Aplicación:** Sistema completo para resolución de problemas metrológicos según la Guía Internacional GUM.
- **6 Plantillas de Modelos de Medida Reales de la UPC:**
  - *Sensor AD590 & Acondicionador diferencial (Examen Final 2025)*
  - *Puente de Wheatstone Completo con Galgas Extensométricas*
  - *Termopar Tipo K con Compensación de Unión Fría (Pt100 / CJC)*
  - *Acondicionador Inversor para Sensor Capacitivo*
  - *Divisor de Tensión Resistivo*
  - *Ley de Ohm (Disipación de Potencia)*
- **Derivadas Numéricas Centrales Automáticas:** Obtención instantánea de los coeficientes de sensibilidad $c_i = \partial f / \partial x_i$ con perturbación simétrica óptima sin errores analíticos manuales.
- **Distribuciones de Probabilidad Normalizadas:** Soporte para distribuciones Normales ($k=1, 2, 3$), Rectangulares ($\Delta x / \sqrt{3}$) y Triangulares ($\Delta x / \sqrt{6}$).
- **Desglose de Contribución a la Varianza (Pareto):** Muestra el peso porcentual de cada magnitud de entrada en la incertidumbre combinada final $u_c(y)$ y calcula la incertidumbre expandida al 95% ($U_{95\%} = 2 \cdot u_c$).
- **🎲 Motor de Simulación Monte Carlo (GUM Suplemento 1):** Propagación de distribuciones mediante $10,000$ iteraciones en menos de 100 ms, con media empírica $\bar{y}_{MC}$, desviación típica $s(y)_{MC}$, intervalo de cobertura empírico del 95%, histograma ASCII de densidad de probabilidad y verificación del teorema central del límite frente a la ley analítica lineal.
- **Exportación en 1 Clic:** Botón para copiar la tabla completa del presupuesto de incertidumbres directamente en sintaxis Markdown lista para informes o exámenes.

---

### 🎛️ 4. Diseñador de Filtros Activos, Sensores & Acondicionadores de Señal
- **5ª Pestaña Nativa en la Suite:** Herramienta interactiva para el cálculo, análisis circuital y exportación de etapas analógicas clásicas de la UPC:
  - **Filtros Activos Sallen-Key (2º Orden Pasobajo / Pasoalto):** Síntesis de componentes para aproximaciones polinomiales Butterworth ($Q = 0.7071$), Chebyshev 0.5dB ($Q = 0.8637$), Chebyshev 3dB ($Q = 1.3049$) y Bessel ($Q = 0.577$).
  - **Diagrama de Bode en Tiempo Real:** Curva de ganancia en dB renderizada nativamente con gráficos vectoriales acelerados en Tkinter `Canvas`, con retícula logarítmica y marcación visual de $f_c$ y el punto de $-3\text{ dB}$.
  - **Sensores de Temperatura (Pt100, NTC Taylor, Termopar CJC):**
    * *Termorresistencia Pt100 (IEC 60751):* Ecuación de Callendar-Van Dusen, inversión analítica exacta $R \to T$ y cálculo del error por resistencia de cable ($+2R_L / \alpha$) en 2, 3 y 4 hilos Kelvin.
    * *Termistor NTC:* Resistencia óptima de linealización de Taylor ($R_{lin} = R_0 \frac{\beta - 2T_0}{\beta + 2T_0}$) en divisor o puente.
    * *Termopares K/J:* Cálculo de fuerza electromotriz Seebeck y compensación electrónica de unión fría (CJC).
    * *Curva de Calibración en Vivo:* Trazado continuo en Canvas y generación de netlist SPICE a 4 hilos.
  - **Generador de Netlists SPICE / LTspice:** Código de circuito `.cir` completo con subcircuitos de amplificador operacional y directivas de simulación en corriente alterna (`.ac dec 100 ...`), copiable en 1 clic para validar en LTspice, Multisim o KiCad.
  - **Puente de Wheatstone & INA (AD620 / AD623):** Cálculo de tensión diferencial, ajuste de resistencia de ganancia $R_g$, error inducido por tensión de modo común según CMRR en dB y disipación térmica en las galgas para evitar autocalentamiento.
---

### 🔌 4b. Banco de Componentes R-L-C, Presets Canónicos & Asignaturas GREELEC
- **Modelado de Circuitos Fundamentales y Topologías GREELEC (UPC ETSETB):**
  * *Divisores resistivos de nivel (5V a 3.3V ADC / Level Shifter).*
  * *Redes serie y paralelo de resistencias (series normalizadas E12 / E24).*
  * *Redes de condensadores & desacoplo de rieles de alimentación (100nF cerámico + 10µF reserva).*
  * *Circuitos resonantes LC sintonizados.*
  * *Temporizador NE555 astable (oscilador de reloj con ciclo de trabajo ajustable).*
  * *Driver NPN (2N2222) con diodo volante Schottky/Flyback (1N4007) para cargas inductivas.*
  * *Limitador de corriente para diodos LED (cálculo de disipación y resistencia de polarización).*
  * *Decodificador de código de colores de resistencias (4 y 5 bandas).*
  * *Convertidor DC-DC Buck Reductor (PWM, CCM/DCM, cálculo de Lcrit y rizado de corriente).*
  * *Convertidor DC-DC Boost Elevador (Step-Up con conmutación MOSFET y diodo de potencia).*
  * *Línea de Transmisión RF Coaxial 50 Ω (ROE / VSWR, pérdidas de retorno y potencia reflejada).*
  * *Amplificador BJT Emisor Común (polarización por divisor, recta de carga DC y ganancia $A_v$).*
  * *Lazo de Control Feedback PID continuo (análisis de estabilidad, sobreoscilación $M_p$ y tiempo de establecimiento $t_s$).*
- **Esquemáticos Vectoriales Dinámicos en Tkinter:** Dibujo paramétrico del esquema eléctrico en tiempo real en el lienzo de la aplicación de escritorio para todas las topologías.
- **Generador Automático de Netlists SPICE (.cir):** Sintetiza archivos de simulación listos para ejecutar en LTspice, NGSpice, Micro-Cap y Multisim con un solo clic (incluyendo modelos de componentes, análisis transitorio `.tran`, puntos de operación `.op` y barridos en frecuencia `.ac`).

### 🔍 5. Buscador Ultrarrápido estilo macOS Spotlight
- Pulsa el botón **Spotlight** o el atajo de búsqueda para indexar en milisegundos todos los archivos Markdown de tu curso.
- Búsqueda por palabras clave, fórmulas, conceptos o nombres de preguntas, con previsualización del fragmento y salto directo al visor.

---

### 🃏 6. Generador de Flashcards y Paquetes Anki (.apkg)
- Extrae automáticamente los bancos de preguntas interactivas presentes en los scripts HTML (`BANC`, `DATA.items`, `ITEMS`).
- Genera el mazo oficial empaquetado **`_Flashcards_Examen.apkg`** listo para importar en [Anki](https://apps.ankiweb.net/) con tarjetas de dos caras estilizadas (anverso con enunciado y tema, reverso con respuesta oficial, color condicional y justificación técnica).
- Exporta en paralelo el fichero `_Flashcards_Examen.tsv` compatible con Quizlet y herramientas de repaso.

---

### 🎯 7. Simulador Oficial de Examen UPC & Generador de Cuadernillos Impresos (PDF)
- **Simulador de examen en pantalla:** Baremo oficial UPC ($\text{Nota} = [(\text{Aciertos} \times 1.00 - \text{Fallos} \times 0.33)/\text{Total}] \times 10.0$).
- **📄 Generador de Cuadernillos de Examen Impresos:** Botón para crear al instante un examen en formato A4 formal imprimible con encabezado de la Universitat Politècnica de Catalunya (EEBE), cajetín de identificación del estudiante, casillas de respuesta `[ ] V   [ ] F` y **plantilla de corrección razonada** con fundamento matemático para el profesor o autoevaluación.

---

### 📝 6. Banco Maestro de Problemas de Examen Resueltos (10 Problemas UPC Paso a Paso)
- **Desarrollos analíticos exhaustivos en $\LaTeX$:** Resolución completa de 10 problemas numéricos de nivel de examen que cubren la totalidad del temario de la UPC (puente de Wheatstone, linealización de termistores NTC, acondicionamiento de Pt100 a 3 hilos, amplificador de instrumentación INA con CMRR real, filtro activo Sallen-Key, acondicionador para sensor piezoeléctrico de aceleración, balanceo de puentes AC para sensores capacitivos, y cuantización/muestreo ADC con aliasing).
- **Generador Paramétrico de Problemas (`problem_generator.py`):** Motor de generación de problemas aleatorizados con comprobación matemática de tolerancia numérica para autoevaluación continua del estudiante.

---

### 🎓 6b. Colección Oficial de Exámenes Finales Reales UPC (`_Examenes_Finales_Oficiales_UPC.md`)
- **3 Convocatorias Oficiales Íntegras con Soluciones Oficiales en $\LaTeX$:**
  1. **Convocatoria 8 de enero de 2021 (Prof. Miguel Ángel García González):**
     - *Problema 1:* Tiempo de subida con osciloscopio ($R_{osc} = 1\text{ M}\Omega \parallel 13\text{ pF}$, cable coaxial $1.5\text{ m}$) y diseño de compensación de sonda pasiva $10\times$ ($C_p = 15.33\text{ pF}$) para elevar el ancho de banda a $230.7\text{ MHz}$ y reducir $t_{r,\min}$ de $30.04\text{ ns}$ a $3.3\text{ ns}$.
     - *Problema 2:* Termopar tipo K con compensación electrónica de unión fría (Pt100 con $I = 100\,\mu\text{A}$) y amplificador AD623 con balanceo de ganancia para sensibilidad de $10\text{ mV/}^\circ\text{C}$ e insensibilidad total a $T_a$.
     - *Problema 3:* Oscilador de relajación para sensor capacitivo $C(x) = \frac{330\text{ pF}}{1+x}$ con operacional rail-to-rail, e incertidumbre GUM con multímetro Keysight 34465A.
  2. **Convocatoria 16 de enero de 2024 (Profs. M. Á. García González y J. Ramos Castro):**
     - *Problema 1:* Tratamiento estadístico con 25 lecturas de multímetro: Criterio de Chauvenet ($D_{\max} = 3$) para descarte de outliers, función de autocorrelación ($r_1$) para independencia al $99.9\%$, e incertidumbres Tipo A ($97.6\,\mu\text{V}$), Tipo B ($94.6\,\mu\text{V}$) y combinada ($136\,\mu\text{V}$).
     - *Problema 2:* Acondicionador lineal capacitivo con OPA134 ($30\text{ kHz}$), verificación de Slew-Rate, inmunidad por CMRR y análisis riguroso de interferencias por PSRR ($41\text{ mV}$) y acoplo capacitivo parásito de red de $230\text{ V}$ a $50\text{ Hz}$ ($0.84\text{ V}$).
     - *Problema 3:* Termopar tipo K con NTC linealizada por Taylor ($R_{lin} = 10.06\text{ k}\Omega$), inyección de compensación en pin REF del AD620, e integración de ruido blanco + flicker $1/f$ ($0.01\text{ Hz} - 10\text{ Hz}$) resultando en $u(T_h) = 0.0014^\circ\text{C}$.
  3. **Convocatoria 14 de enero de 2025 (Profs. M. Á. García González y J. Ramos Castro):**
     - *Ejercicios Cortos (30%):* Impedancia y capacidad de aislamiento de multímetro a partir de CMRR ($1\text{ G}\Omega, 100.7\text{ pF}$), saturación por offset en TIA con red T ($V_{os} < 980.2\,\mu\text{V}$), CMRR mínimo para célula de carga ($89.9\text{ dB}$), y transmisión por lazo de corriente 4-20 mA.
     - *Problema 1 (35%):* Sensor AD590 ($1\,\mu\text{A/K}$) con presupuesto de incertidumbres GUM completo: matriz de 5 coeficientes de sensibilidad analíticos $\partial V_o / \partial x_i$ e incertidumbre expandida $U(T)_{95\%} = 0.46^\circ\text{C}$.
     - *Problema 2 (35%):* Termómetro termopar tipo J con Pt100 ($10\text{ mA}$), ajuste de ganancias y cálculo de ruido $1/f$ + banda ancha.

---

### 🔬 8. Laboratorio Virtual Interactivo de Sensores & Grado GREELEC (`Laboratorio_Virtual_Sensores.html`) — v7.5 Enterprise 3D Edition
- **Simulador Industrial Web de Categoría Multisim / Keysight BenchVue / SPICE:** 100% autónomo, ejecutable en local sin internet ni CDNs, optimizado para los planes de estudio de la UPC (ETSETB / EEBE) y las asignaturas del Grado en Ingeniería Electrónica de Telecomunicación (GREELEC).
- **🌐 Motor WebGL 3D Nativo con Reconstrucción Dinámica por Topología (GPU 60 FPS):**
  - **Rotación Orbital y Zoom Interactivos:** Control táctil y con ratón (arrastrar para orbitar, rueda para zoom, doble clic para centrar la cámara).
  - **Iluminación Realista Phong:** Materiales metálicos (oro, cobre esmaltado, aluminio mecanizado, acero pulido) y dieléctricos con reflejos dinámicos y sombras.
  - **Reconstrucción Geométrica 3D Dinámica por Topología Física:**
    * *Módulo 11 (Banco RLC):* La protoboard 3D se reconstruye físicamente según la topología activa:
      - **Divisor de Tensión:** 2 resistencias axiales con anillos de colores reales calculados dinámicamente según su valor nominal, jumpers de alimentación VCC/GND y clip de prueba de osciloscopio amarillo en el nodo central.
      - **Red Serie/Paralelo:** 3 resistencias en red mixta con puentes de inserción y bananas de prueba.
      - **Filtro de Desacoplo:** Condensador electrolítico radial de 10 µF azul con banda de polaridad (-) y tapa con cruz de seguridad + condensador cerámico de lenteja de 100 nF directamente sobre los rieles de alimentación.
      - **Filtro RC Pasa-Bajos:** Resistencia axial + condensador de película tipo Mylar rectangular amarillo + sonda de osciloscopio BNC con pinza de masa.
      - **Temporizador 555 Astable:** Encapsulado DIP-8 sobre el canal central con muesca y punto pin 1, resistencias $R_A/R_B$, condensador $C_T$ y **LED rojo de 5 mm pulsando en tiempo real**.
      - **Driver de Relé Inductivo:** Relé azul cúbico electromagnético (Songle), transistor NPN TO-92 (2N2222), diodo flyback 1N4007 de vidrio y bornera de tornillo.
      - **Limitador de Corriente con LED:** Resistencia limitadora + LED de 5 mm con bisel y ánodo/cátodo, brillando en función de la corriente directa.
      - **Resonador LC Tanque:** Bobina toroidal con espiras de cobre esmaltado visibles sobre núcleo de ferrita + condensador WIMA de poliéster.
    * *Módulo 12 (Fuentes Conmutadas Buck vs Boost):*
      - **Buck (Reductor):** MOSFET High-Side con disipador, diodo Schottky shunt a masa, inductor toroidal de potencia de salida y condensador Low-ESR.
      - **Boost (Elevador):** Inductor de choque a la entrada, MOSFET Low-Side con aletas disipadoras, diodo Schottky en serie y condensador electrolítico de alta tensión.
    * *Módulo 13 (Líneas de Transmisión RF):* Cable coaxial RG-58 pelado por capas (PVC, malla de blindaje, dieléctrico PTFE, vivo de cobre) con conector SMA dorado y terminaciones intercambiables: carga adaptada de 50 $\Omega$ con aletas de refrigeración, tapón de cortocircuito de latón dorado, circuito abierto o antena helicoidal de cobre.
    * *Módulo 14 (Semiconductores BJT vs MOSFET):* Encapsulado plástico TO-92 de 3 pines (2N2222) vs encapsulado TO-220 de potencia (IRF540) atornillado a disipador de aluminio extruido con tornillo y mica aislante.
    * *Módulo 15 (Control PID):* Servomotor DC con disco encoder ranurado y horquilla optoacopladora vs horno térmico de aluminio con cartucho calefactor y vaina RTD vs depósito hidráulico acrílico transparente con nivel de agua dinámico y flotador.
    * *Módulo 16 (Taller Libre CAD):* Gran protoboard de desarrollo libre donde se renderizan físicamente en 3D todos los componentes activos del netlist SPICE (resistencias, condensadores, inductores, diodos, integrados DIP-8 y cables jumpers flexibles de interconexión).

- **🛠️ Módulo 16: Taller Libre CAD & Editor de Circuitos Manual (MNA Solver & SPICE):**
  - **Entorno de Diseño Circuital Abierto:** Permite diseñar, analizar y testear cualquier circuito analógico personalizado o seleccionar topologías predefinidas (Filtro RLC Butterworth de 2º orden con factor $Q=0.707$, Rectificador de media onda con filtro capacitivo y cálculo de rizado $V_r$, Amplificador Operacional no inversor LM358 con límite de ganancia-ancho de banda GBW y saturación a $\pm 14	ext{ V}$, Atenuador en Pi coaxial RF 50 $\Omega$ adaptado a $-6	ext{ dB}$, y Filtro Notch doble T para rechazo de zumbido de red de $50	ext{ Hz}$).
  - **Editor Interactivo de Netlist SPICE (.cir):**
    * Caja de texto interactiva con resaltado para código SPICE estándar (`VIN 1 0 AC ...`, `R1 1 2 1k`, `C1 2 0 100n`, etc.).
    * Botones de inserción rápida de componentes: `+ R`, `+ C`, `+ L`, `+ D`, `+ OpAmp`.
    * Botón de simulación matricial instantánea (**`⚡ Simular Netlist`**) mediante análisis nodal modificado (MNA).
    * Botones para descargar el archivo de circuito listo para simular (**`💾 .cir`**) o copiarlo al portapapeles (**`📋 Copiar`**).
  - **Esquemático CAD Vectorial de Alta Precisión:** Dibujo en tiempo real sobre lienzo Canvas con normas IEC/IEEE, nodos de circuito claramente numerados (Node 1 IN, Node 2 OUT, GND 0), valores de componentes en unidades ingenieriles normalizadas (k$\Omega$, nF, mH), etiquetas de tensión en vivo y flechas de flujo de corriente.

- **🎛️ Rack de Instrumentación Triple de Laboratorio (Keysight + Rigol + Tektronix):**
  - **1. Multímetro Digital Keysight 34465A Truevolt (6½ Dígitos):** Pantalla VFD de alta resolución, barra analógica bar-graph con rangos automáticos, conmutación DC/AC RMS y cálculo de incertidumbre metrológica $u_B$ en tiempo real según la guía GUM.
  - **2. Generador de Funciones Arbitrarias Rigol DG1022Z (AFG):**
    * Réplica del panel de instrumentos con pantalla LCD y controles de ajuste rápido para Frecuencia (1 Hz a 10 MHz), Amplitud (0.1 a 20.0 Vpp), Offset (-10 a +10 V), Ciclo de Trabajo (Duty Cycle) y Barrido de Frecuencia (Sweep).
    * 5 Formas de onda sintetizadas: Senoidal, Cuadrada, Triangular/Rampa, Pulso y DC pura.
    * Botón conmutable de salida con LED de activación (`Output ON/OFF`).
  - **3. Osciloscopio Digital Tektronix TDS2024C de Doble Traza (Phosphor 60 FPS):**
    * **Canal 1 (CH1 - Amarillo fosforescente `#facc15`):** Visualiza en tiempo real la señal inyectada por el Generador AFG Rigol DG1022Z.
    * **Canal 2 (CH2 - Cian fosforescente `#38bdf8`):** Visualiza simultáneamente la respuesta de salida del circuito bajo prueba (filtrada, atenuada, recortada o con desfase $\Delta\phi$).
    * **On-Screen Display (OSD) Calibrado:** Muestra en pantalla la tasa de muestreo `2.0 GS/s Trig'd`, badges con parámetros de canal (`CH1: SINE 1.0 kHz 5.0 Vpp`, `CH2: Vout Circuito Activo`), base de tiempos `M: 250 µs` y nivel de disparo `CH1 / 0.00 V`.
    * **Modo FFT (Fast Fourier Transform):** Espectro de frecuencias de 0 a 500 Hz con detección de picos armónicos y suelo de ruido en dBV.
    * **Cursores de Medición de Precisión:** Medición de $\Delta t$, $\Delta V$ y cálculo directo de frecuencia experimental $f = 1/\Delta t$.
    * **Exportación de Telemetría a CSV:** Descarga inmediata de las trazas de tensión digitalizadas para su procesamiento en MATLAB, Python o Excel.

- **🎨 Decodificador Interactivo de Código de Colores de Resistencias:**
  - Visualizador vectorial SVG interactivo de resistencias axiales con selector de bandas (4 y 5 anillos).
  - Cálculo instantáneo de valor nominal, tolerancia y rango admisible $[R_{\min}, R_{\max}]$, con botón para inyectar el valor directamente en el banco de simulación.

- **16 Módulos de Simulación Física y Circuital (Temario Sistemes de Mesura + Plan de Estudios GREELEC UPC):**
  1. *Puente de Wheatstone & Galgas (1/4, 1/2 y completo con viga 3D deformable y mapa de von Mises)*
  2. *Pt100 y compensación a 4 hilos Kelvin con sonda DIN B 3D sumergida en baño termostático*
  3. *INA3 & CMRR real con amplificadores AD623/AD620 y balanceo de modo común*
  4. *Filtro activo Sallen-Key pasobajo de 2º orden con respuesta Butterworth/Chebyshev*
  5. *Muestreo Nyquist & ADC con analizador FFT y DAC R-2R*
  6. *Termopares K/J & compensación de unión fría (CJC) con bloque isotérmico*
  7. *Termistor NTC & linealización analítica de Taylor*
  8. *Ruido térmico Johnson-Nyquist & relación SNR con jaula de Faraday*
  9. *Sensor piezoeléctrico & amplificador de carga vs tensión*
  10. *Sensor capacitivo diferencial & detección síncrona lock-in (PSD)*
  11. *🔌 Banco R-L-C & Presets Canónicos de Laboratorio (Divisores ADC, desacoplo digital 100nF+10µF, 555 astable con LED pulsante, driver relé con diodo flyback 1N4007, limitador LED, resonador LC)*
  12. *⚡ Fuentes Conmutadas DC-DC: Buck (Reductor) & Boost (Elevador) — GREELEC PEE (Procesado de Energía Eléctrica)*
  13. *📡 Líneas de Transmisión RF & Carta de Smith Vectorial — GREELEC CAF (Circuitos de Alta Frecuencia / Ondas)*
  14. *🎛️ Transistores BJT & MOSFET: Polarización y Pequeña Señal — GREELEC DE/CA (Dispositivos & Circuitos Analógicos)*
  15. *🎯 Sistemas de Control Feedback & Regulador PID Continuo — GREELEC SC (Sistemas de Control)*
  16. *🛠️ Taller Libre CAD & Editor de Circuitos Manual con Motor Matricial MNA y Editor SPICE en vivo*

- **🎯 16 Retos de Examen Oficiales UPC:** Problemas numéricos reales integrados en cada módulo con comprobación automática de tolerancia y desglose algebraico de la solución.
- **📄 Exportador de Informes Experimentales:** Generador de informe estructurado en Markdown con todas las mediciones, métricas y ecuaciones, descargable o copiable al portapapeles en 1 clic.

---

### 📚 8. Documentos Maestros Generados
Al procesar el curso completo, la herramienta sintetiza automáticamente:
1. **`_Examenes_Finales_Oficiales_UPC.md`:** 3 exámenes finales oficiales completos (2021, 2024, 2025) resueltos con 100% rigor analítico en LaTeX.
2. **`_Problemas_Examen_Resueltos.md`:** 10 problemas numéricos de nivel de examen completamente resueltos y explicados.
3. **`Laboratorio_Virtual_Sensores.html`:** Simulador industrial de física e instrumentación 3D (v7.5 Enterprise 3D Edition).
4. **`_Cuaderno_Maestro_Tema_XX.md`:** 10 cuadernos maestros temáticos de alta densidad.
5. **`_Formulario_Oficial_Examen.md`:** Formulario consolidado con todas las ecuaciones matemáticas del curso.
6. **`_Glosario_Conceptos_Clave.md`:** Vocabulario técnico y definiciones operativas.
7. **`_Gran_Indice_Sistemes_de_Mesura.md`:** Índice general jerárquico con enlaces directos.
8. **`_Flashcards_Examen.apkg` y `.tsv`:** Mazo de 550 tarjetas didácticas para Anki (autoevaluación + preguntas de finales oficiales).
9. **`_Instrucciones_Sistema_NotebookLM.md`:** Instrucciones de sistema recomendadas para tutor interactivo en NotebookLM.

---

## 🚀 Instalación y Requisitos

### Requisitos Previos
- **Python 3.10** o superior instalado en el sistema.

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Damaga2005/Conversor-HTML-A-MD.git
cd Conversor-HTML-A-MD
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

Las dependencias principales son:
- `beautifulsoup4`: Análisis y manipulación del árbol DOM HTML.
- `lxml`: Parser XML/HTML de alto rendimiento.
- `mathml2latex`: Conversión de ecuaciones MathML a formato LaTeX.
- `pyinstaller`: (Opcional) Compilación del script en binario independiente para Windows.

---

## 🖥️ Uso de la Aplicación

### Iniciar la Interfaz Gráfica
```bash
python conversor_html_notebooklm.py
```

### Modos de Operación:
1. **Archivo Único (`Single File`):** Convierte un archivo `.html` específico a `.md`.
2. **Carpeta de Archivos (`Batch Folder`):** Procesa recursivamente todos los `.html` de un directorio.
3. **Curso Completo (`All Course`):** Procesa los 10 temas, genera los cuadernos maestros, extrae las 500 preguntas para Anki, compila el formulario de ecuaciones y genera el índice general.

### Compilar a Ejecutable de Windows (.exe)
Si deseas crear el binario ejecutable portable para Windows:
```bash
pyinstaller --noconfirm conversor_html_notebooklm.spec
```
El ejecutable se generará en la carpeta `dist/conversor_html_notebooklm/`.

---

## 📁 Estructura del Proyecto

```text
Conversor-HTML-A-MD/
├── conversor_html_notebooklm.py     # Aplicación principal (GUI Apple Dark + Motor de conversión)
├── conversor_html_notebooklm.spec   # Configuración de empaquetado PyInstaller
├── requirements.txt                 # Dependencias del entorno Python
├── LICENSE                          # Licencia de código abierto MIT
├── README.md                        # Documentación completa del proyecto
└── dist_course_md/                  # Material convertido del curso Sistemes de Mesura
    ├── Para_Subir_a_NotebookLM/     # Archivos consolidados listos para subir a NotebookLM
    ├── Tema_01/ a Tema_10/          # Carpetas de cada tema con sus MD individuales y assets
    ├── _Problemas_Examen_Resueltos.md # 10 problemas numéricos completos con desarrollo en LaTeX
    ├── Laboratorio_Virtual_Sensores.html # Simulador web interactivo en tiempo real (Apple Dark)
    ├── _Cuaderno_Maestro_Tema_*.md  # 10 cuadernos maestros temáticos
    ├── _Formulario_Oficial_Examen.md# Formulario oficial de fórmulas del curso
    ├── _Glosario_Conceptos_Clave.md # Glosario de términos técnicos
    ├── _Gran_Indice_*.md            # Índice navegable de todo el temario
    ├── _Flashcards_Examen.apkg      # Mazo empaquetado para Anki (500 preguntas oficiales)
    ├── _Flashcards_Examen.tsv       # Mazo en texto tabulado
    └── _Instrucciones_Sistema_NotebookLM.md # Guía de prompts para NotebookLM
```

---

## 🤖 Integración con Google NotebookLM

1. Accede a [Google NotebookLM](https://notebooklm.google.com/).
2. Crea un nuevo cuaderno (por ejemplo, *"Sistemes de Mesura - UPC EEBE"*).
3. Sube los archivos ubicados en `dist_course_md/Para_Subir_a_NotebookLM/` o los cuadernos maestros `_Cuaderno_Maestro_Tema_XX.md`.
4. En el panel lateral derecho (**Studio**):
   - Genera resúmenes ejecutivos.
   - Crea automáticamente **Tarjetas didácticas** (flashcards).
   - Crea un **Audio Overview** (Podcast de estudio interactivo con dos presentadores AI).
5. En el chat, pega las instrucciones de `_Instrucciones_Sistema_NotebookLM.md` para que Gemini responda con el máximo rigor académico y matemático.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más información.

---

Desarrollado con ❤️ para estudiantes y docentes universitarios.
