# 🍏 Conversor Universal de Documentación Técnica & Suite Metrológica UPC

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Interface: Apple Dark](https://img.shields.io/badge/UI-Apple%20Liquid%20Glass%20Dark-black.svg)]()
[![Target: NotebookLM](https://img.shields.io/badge/Optimized%20for-Google%20NotebookLM-4285F4.svg)]()
[![LaTeX: MathML & OMML Supported](https://img.shields.io/badge/LaTeX-MathML%20%7C%20OMML%20%E2%86%92%20LaTeX-brightgreen.svg)]()
[![UPC GREELEC: 35 Courses & 424 Questions](https://img.shields.io/badge/UPC%20GREELEC-35%20Courses%20%7C%20424%20Exam%20Questions-purple.svg)]()
[![Virtual Lab: 20 Modules 3D](https://img.shields.io/badge/Virtual%20Lab-20%20Modules%20WebGL%203D-orange.svg)]()
[![Engineering Solvers: 37 Tools](https://img.shields.io/badge/Engineering%20Solvers-37%20Computational%20Tools-blueviolet.svg)]()
[![Tests: Pytest Passing](https://img.shields.io/badge/tests-40%2F40%20passing-success.svg)]()

> Suite integral de ingeniería documental, conversores universales de alta fidelidad y estación de trabajo virtual diseñada para transformar contenidos educativos, técnicos e interactivos (HTML, PDF, DOCX, IPYNB, MathML, scripts de examen) en **Markdown técnico estructurado de máxima pureza**, 100% optimizado para **Google NotebookLM**, Gemini, Claude, Obsidian y ChatGPT.
> 
> Incluye el **Plan de Estudios Completo GREELEC (UPC ETSETB)** con las **35 asignaturas obligatorias**, **424 preguntas técnicas de examen con justificación**, 35 calculadoras interactivas de parámetros y bancos de ensayo SPICE/VHDL/C; además del **Laboratorio Virtual de Sensores e Instrumentación 3D (v8.5 Enterprise Workbench)** con 20 módulos circuitales, calculadora metrológica GUM con simulación Monte Carlo, diseñador de filtros activos, banco R-L-C y gestor de flashcards Anki.

---

## 📑 Tabla de Contenidos
- [✨ Características Principales](#-características-principales)
  - [🔄 1. Conversores Universales de Archivos & Extractor de Fórmulas y Problemas](#-1-conversores-universales-de-archivos-de-alta-fidelidad-universal_converterspy)
  - [🎨 2. Interfaz Gráfica de Escritorio (Apple Liquid Glass Dark)](#-2-interfaz-gráfica-de-escritorio-apple-liquid-glass-dark)
  - [🎓 3. Plan de Estudios UPC GREELEC: 35 Asignaturas & 424 Preguntas de Examen](#-3-plan-de-estudios-upc-greelec-35-asignaturas--424-preguntas-de-examen)
  - [🛠️ 4. Suite de 37 Solvers y Herramientas Especializadas de Ingeniería](#-4-suite-de-37-solvers-y-herramientas-especializadas-de-ingeniería-engineering_tools_suitepy)
  - [🔬 5. Laboratorio Virtual de Sensores e Instrumentación 3D](#-5-laboratorio-virtual-de-sensores-e-instrumentación-3d-v85-enterprise)
  - [📐 6. Calculadora Metrológica GUM (ISO/IEC 98-3) & Monte Carlo](#-6-calculadora-metrológica-gum-isoiec-98-3--monte-carlo-supl-1)
  - [🎛️ 7. Diseñador de Filtros Activos & Sensores](#-7-diseñador-de-filtros-activos-sensores--acondicionadores)
  - [🔌 8. Banco R-L-C & Presets Canónicos GREELEC](#-8-banco-r-l-c--presets-canónicos-greelec)
  - [🗂️ 9. Repaso Activo Anki & Gestor de Exámenes](#-9-repaso-activo-anki--gestor-de-exámenes)
- [🚀 Instalación y Requisitos](#-instalación-y-requisitos)
- [🖥️ Uso de la Aplicación (GUI y Terminal CLI)](#-uso-de-la-aplicación-gui-y-terminal-cli)
- [📁 Estructura del Repositorio](#-estructura-del-repositorio)
- [🤖 Integración con Google NotebookLM](#-integración-con-google-notebooklm)
- [📄 Licencia](#-licencia)

---

## ✨ Características Principales

### 🔄 1. Conversores Universales de Archivos de Alta Fidelidad (`universal_converters.py`)
Módulo independiente de conversión universal con algoritmos especializados:
- **Traductor OMML a LaTeX de Precisión Industrial:** Soporte exhaustivo para los 15 elementos matemáticos de Word (`m:f`, `m:sSup`, `m:sSub`, `m:sSubSup`, `m:sPre`, `m:rad`, `m:d`, `m:m`, `m:nary`, `m:limLow`, `m:limUpp`, `m:bar`, `m:acc`, `m:box`, `m:groupChr`, `m:eqArr`). Traduce matrices 2D, integrales múltiples con límites, sumatorios, raíces n-ésimas y acentos vectoriales directamente a $\LaTeX$ puro balanceado.
- **Extractor Universal de Fórmulas Matemáticas Multi-Formato:** Escanea simultáneamente archivos `.md`, `.html`, `.docx`, `.ipynb`, `.pdf`, `.xlsx` y `.csv`, limpia la sintaxis matemática, auto-balancea delimitadores y compila un Formulario Maestro clasificado por temas y asignaturas.
- **Extractor y Compilador Universal de Problemas y Ejercicios:** Identifica automáticamente enunciados, tablas de datos técnicos con unidades, listas de cuestiones formuladas, soluciones paso a paso y resultados clave enmarcados ($\boxed{...}$), generando un Banco Maestro de Problemas Resueltos.
- **PDF a Markdown (PyMuPDF):** Extracción inteligente con detección de encabezados jerárquicos, tablas estructuradas en formato GitHub Flavored Markdown (GFM) e inferencia de bloques matemáticos en $\LaTeX$.
- **Jupyter Notebook (`.ipynb`) a Markdown:** Extracción secuencial de celdas Markdown y código fuente Python, preservando salidas de consola, trazas de ejecución e imágenes gráficas generadas.
- **Extractor Automático de Imágenes Base64:** Decodifica recursos gráficos embebidos y los almacena físicamente en la carpeta `assets/` con control de hash SHA-256 para evitar duplicaciones.
- **Excel (`.xlsx`) y CSV a Tablas Markdown:** Conversor tipado con detección de números, porcentajes y alineación columnar automática.
- **Markdown a HTML Imprimible / PDF Académico:** Motor de maquetación con estilos de alta legibilidad (Apple Pro / San Francisco), integración con MathJax 3 y reglas CSS `@media print` optimizadas para generar PDFs A4 con un solo clic.
- **Extractor de Netlists SPICE:** Detección de esquemas y circuitos en notas técnicas para exportar archivos `.cir` listos para simulación en LTspice, NGSpice o KiCad.
- **Generador de Glosario Técnico A-Z:** Indexación alfabética automática de acrónimos y definiciones con enlace a sus fuentes.
- **Conversión Universal en Lote (`batch_convert_universal`):** Exploración recursiva de directorios para procesar simultáneamente colecciones de archivos heterogéneos (PDF, DOCX, IPYNB, CSV, XLSX, HTML).

---

### 🎨 2. Interfaz Gráfica de Escritorio (Apple Liquid Glass Dark)
La aplicación de escritorio (`conversor_html_notebooklm.py`) cuenta con una interfaz organizada en **9 pestañas temáticas** navegables mediante un selector segmentado tipo macOS:
1. **HTML a MD:** Conversor interactivo con previsualización, extracción de imágenes y perfiles preconfigurados.
2. **Universal:** Panel de control de conversión multi-formato (PDF, DOCX, IPYNB, CSV, Excel) con selección de opciones avanzadas y consola asíncrona en tiempo real.
3. **Visor Markdown:** Lector con resaltado de sintaxis, barra de productividad (zoom tipográfico A-/100%/A+, estadísticas en vivo de palabras, caracteres, fórmulas y tiempo de lectura) y exportador HTML/PDF.
4. **Biblioteca:** Acceso directo a documentos maestros, exámenes resueltos y enlaces de estudio.
5. **Calculadora GUM:** Presupuesto de incertidumbres según la norma ISO/IEC 98-3 con simulación Monte Carlo.
6. **Filtros Activos:** Calculadora y sintetizador de filtros Sallen-Key con diagrama de Bode en tiempo real y acondicionadores analógicos.
7. **Banco R-L-C:** Simulador de topologías canónicas y esquemáticos vectoriales dinámicos.
8. **Flashcards Anki:** Visor de preguntas de autoevaluación, buscador interactivo en vivo, filtrado temático y exportador de mazos Anki (`.apkg` y `.tsv`).
9. **Plan UPC GREELEC:** Estación de trabajo académica completa del grado con explorador de las 35 asignaturas obligatorias, temarios oficiales extraídos de guías docentes PDF, fórmulas $\LaTeX$, 35 calculadoras interactivas de parámetros, bancos SPICE/VHDL/C y 424 preguntas oficiales de autoevaluación con justificación.

#### ⚡ Atajos de Teclado Globales:
| Atajo | Acción |
| :--- | :--- |
| `Ctrl + 1` .. `Ctrl + 9` | Cambio instantáneo a cualquiera de las 9 pestañas |
| `Ctrl + O` | Abrir diálogo de selección de archivo o carpeta de origen |
| `Ctrl + S` | Guardar o exportar resultados de la pestaña activa |
| `F5` / `Ctrl + R` | Recalcular parámetros activos (GUM, Filtros, RLC, UPC) |
| `Drag & Drop` | Arrastrar archivos PDF, DOCX, IPYNB, XLSX o HTML conmuta y precarga la herramienta correspondiente |

---

### 🎓 3. Plan de Estudios UPC GREELEC: 35 Asignaturas & 424 Preguntas de Examen
El motor académico `upc_degree_engine.py` incorpora los datos y competencias oficiales de todas las asignaturas obligatorias del **Grado en Ingeniería Electrónica de Telecomunicación (ETSETB - UPC)**:
- **Catálogo de 35 Asignaturas Obligatorias (210 ECTS Totales):**
  - **Q1:** `230339` IMATEC · `230900` CCE · `230901` APR · `230902` F · `230903` C · `230904` ALN
  - **Q2:** `230905` AC · `230906` PRD · `230907` EMG · `230908` CVEC · `230909` EDT
  - **Q3:** `230910` DE · `230911` DD · `230912` EAFO · `230913` SST · `230914` PPE
  - **Q4:** `230915` CA · `230916` EMB · `230917` ICAF · `230918` TRS · `230919` EP
  - **Q5:** `230920` SM · `230921` SDC · `230922` CIAF · `230923` CEM · `230924` CTR
  - **Q6:** `230925` IOT · `230926` RT · `230927` PEE · `230928` TEL · `230929` TEM
  - **Q7:** `230930` DMIC · `230931` HIPS · `230934` DIFO
  - **Q8:** `230932` INT
- **424 Preguntas Oficiales con Justificación:** 12 a 13 cuestiones técnicas por asignatura con corrección automática y explicación teórica detallada.
- **35 Calculadoras Paramétricas:** Simulación instantánea de divisores, impedancias, márgenes de estabilidad, inductancias Buck/Boost, enlaces LoRa, etc.
- **35 Bancos de Ensayo SPICE / HDL / Firmware C:** Netlists listos para ejecución en simuladores circuitales.
- **Exportación Automática:** Generación de guías de estudio en Markdown para NotebookLM y mazos Anki TSV/APKG individuales y combinados.
- **Cheatsheet Maestro:** Compendio unificado de fórmulas matemáticas y modelos canónicos de todo el plan de estudios.

---

### 🛠️ 4. Suite de 37 Solvers y Herramientas Especializadas de Ingeniería (`engineering_tools_suite.py`)
Módulo integral de **37 herramientas de cálculo numérico, sintetizadores circuitales y generadores de código hardware/firmware** que cubren la totalidad del espectro técnico de las 35 asignaturas del grado GREELEC (UPC ETSETB). Se organizan en 5 ramas canónicas de ingeniería:

#### 📡 Rama 1: RF, Microondas & Telecomunicaciones (10 Herramientas)
- `microstrip_synthesizer`: Síntesis de ancho de pista $W/h$, $\varepsilon_{eff}$ y retardo $t_{pd}$ mediante ecuaciones de Hammerstad-Wheeler.
- `smith_chart_stub_matcher`: Adaptador de impedancias por simple stub en derivación (cortocircuito / circuito abierto) con distancia $d$ y longitud $l$.
- `quarter_wave_transformer`: Transformador de impedancias en cuarto de onda ($\lambda/4$) con cálculo de ancho de banda fraccional para un límite de ROE dado.
- `friis_cascade_analyzer`: Análisis de cascada de receptores RF según fórmula de Friis (ganancia total, figura de ruido NF global y temperatura de ruido en Kelvin).
- `wilkinson_divider_designer`: Dimensionamiento de divisor/combinador Wilkinson de potencia (ramas de $Z_0\sqrt{2}$ y resistencia de aislamiento $2Z_0$).
- `coaxial_cable_solver`: Resolución analítica de cable coaxial ($Z_0$, capacidad por metro, inductancia por metro y frecuencia de corte del modo superior $TE_{11}$).
- `link_budget_calculator`: Balance de enlace radioeléctrico con atenuación en espacio libre (FSPL) y margen de desvanecimiento contra umbral de sensibilidad $P_{rx}$.
- `rectangular_waveguide_modes`: Espectro de frecuencias de corte para guía de ondas rectangular WR-90 / banda X con banda monomodo recomendada.
- `shannon_channel_capacity`: Capacidad teórica de canal AWGN según teorema de Shannon-Hartley y eficiencia espectral en bit/s/Hz.
- `pll_loop_filter_synthesizer`: Síntesis de filtro pasivo de 2º orden para PLL Charge-Pump ($C_1$, $C_2$, $R_2$, frecuencias de polo y cero, factor de división $N$).

#### ⚡ Rama 2: Electrónica Analógica, Filtros & Potencia (8 Herramientas)
- `bjt_amplifier_designer`: Dimensionamiento analítico de etapa de emisor común con polarización de 4 resistencias, transconductancia $g_m$, $r_\pi$, $A_v$, $R_{in}$ y $R_{out}$.
- `mosfet_amplifier_designer`: Polarización y parámetros en pequeña señal de etapa Common-Source MOSFET en saturación ($V_{GS}$, $V_{OV}$, $R_D$, $g_m$, $r_o$ y ganancia).
- `differential_pair_analyzer`: Par diferencial con carga resistiva (ganancia diferencial $A_d$, ganancia de modo común $A_{cm}$ y rechazo CMRR en dB).
- `sallen_key_filter_synthesizer`: Filtros activos paso bajo/paso alto Sallen-Key con aproximaciones Butterworth, Chebyshev o Bessel y desnormalización de componentes.
- `buck_converter_synthesizer`: Convertidor reductor DC-DC con inductancia crítica para modo de conducción continua (CCM), rizado de corriente y condensador de salida.
- `boost_converter_synthesizer`: Convertidor elevador DC-DC en CCM con ciclo de trabajo $D$, inductancia de filtro y condensador para rizado de tensión.
- `rlc_transient_solver`: Resolución del transitorio de circuito RLC serie/paralelo (frecuencia natural $\omega_0$, factor de amortiguamiento $\zeta$, polos $s_1, s_2$ y clasificación del régimen).
- `opamp_error_budget_calculator`: Presupuesto de errores en continua en etapa amplificadora operacional ($V_{os}$, corrientes de polarización $I_b$ y desbalance $I_{os}$, CMRR finito).

#### 💻 Rama 3: Sistemas Digitales, VHDL & Computación Embebida (7 Herramientas)
- `arm_cortex_systick_timer`: Generador de recargas del timer de sistema ARM Cortex-M SysTick para intervalos periódicos de interrupción sin drift.
- `usart_baud_rate_generator`: Divisor de baudios para periféricos USART/UART en microcontroladores (STM32 BRR register) con tasa de error porcentual.
- `adc_sar_timing_calculator`: Temporización de convertidores analógico-digitales SAR (tiempo de muestreo, ciclos de conversión por aproximaciones sucesivas y tasa máxima en kSPS).
- `vhdl_entity_generator`: Generador sintetizable de entidades y arquitecturas VHDL puras (contadores parametrizables, FIFOs síncronas, registros de desplazamiento, decodificadores).
- `sta_timing_slack_analyzer`: Análisis estático de tiempos (Static Timing Analysis - STA) para caminos críticos síncronos con verificación de slack de Setup y Hold.
- `rtos_schedulability_solver`: Test de planificabilidad en tiempo real RTOS bajo algoritmos Rate Monotonic (cota de Liu & Layland) y Earliest Deadline First (EDF).
- `transmission_line_bounce_diagram`: Diagrama de rebotes en línea de transmisión digital de alta velocidad por diferencias de impedancia (reflexiones múltiples).

#### 🎛️ Rama 4: Procesado Digital de Señal & DSP (6 Herramientas)
- `fir_filter_window_designer`: Diseño de filtros digitales FIR por método de ventanas (Hamming, Hann, Blackman, Rectangular) con coeficientes normalizados.
- `bilinear_transform_mapper`: Mapeo continuo-a-discreto por Transformada Bilineal con prewarping de frecuencias analógicas a frecuencias digitales $\omega$.
- `fft_resolution_inspector`: Inspección de parámetros de la Transformada Rápida de Fourier (resolución en frecuencia $\Delta f$, límite de Nyquist y duración de ventana).
- `lora_toa_and_energy_predictor`: Tiempo en el aire (Time-on-Air) y consumo de energía para nodos IoT LoRaWAN según Spreading Factor, ancho de banda y tamaño de payload.
- `adc_quantization_noise_analyzer`: Relación señal a ruido de cuantización teórica (SQNR) según fórmula de Bennett, tensión de LSB y densidad de ruido.
- `z_transform_pole_zero_analyzer`: Inspección de estabilidad en el plano Z para funciones racionales discretas $H(z)$, posición de polos y respuesta a frecuencia canónica.

#### 🌡️ Rama 5: Física, Sensores, Confiabilidad & Control (6 Herramientas)
- `solar_cell_single_diode_solver`: Modelo de célula fotovoltaica de 1 diodo (búsqueda del punto de máxima potencia MPP, tensión $V_{mp}$, corriente $I_{mp}$ y Fill Factor).
- `rtd_pt100_temperature_solver`: Sensor de platino Pt100 según Callendar-Van Dusen (resolución inversa precisa de temperatura para cualquier resistencia $R(T)$).
- `strain_gauge_rosette_solver`: Roseta de galgas extensiométricas a 0°/45°/90° (cálculo de deformaciones principales $\varepsilon_1, \varepsilon_2$, tensiones principales $\sigma_1, \sigma_2$ y ángulo de orientación).
- `pcb_thermal_heatsink_dimensioner`: Dimensionador térmico de encapsulados electrónicos y disipadores (resistencia térmica máxima disipador-ambiente $R_{th,sa}$, análisis de convección pasiva).
- `system_reliability_markov_solver`: Fiabilidad de sistemas redundantes y cadenas de Markov de fallo (MTTF global, probabilidad de supervivencia $R(t)$ en misión).
- `second_order_system_step_response`: Respuesta al escalón de sistemas de 2º orden en lazo cerrado (sobreoscilación $M_p$, tiempo de pico $t_p$, tiempo de subida $t_r$ y establecimiento $t_s$).

---

### 🔬 5. Laboratorio Virtual de Sensores e Instrumentación 3D (v8.5 Enterprise)
Simulador web autónomo (`Laboratorio_Virtual_Sensores.html`) ejecutable localmente sin conexión a internet ni CDNs:
- **Visualización Tridimensional Fluida (60 FPS):** Renderizado volumétrico WebGL acelerado por GPU con cámara orbital 360°, sombreado Phong y carga determinista de geometría (resolución definitiva de pantallas en negro).
- **Esquemático 2D CAD Interactivo:** Representación vectorial de circuitos bajo normativa **IEC 60617 / IEEE Std 315**, con nodos activos, caídas de potencial y cableado dinámico click & drag.
- **Barra de Asignaturas Oficiales UPC con Conteo en Vivo:**
  - `🏛️ Totes (20)`: Catálogo completo de módulos.
  - `📘 SM: Mesura (14)`: Sensores y sistemas de medida.
  - `⚡ CCE: Circuits (3)`: Teoría de circuitos y electrónica analógica.
  - `🔋 PEE: Potència (1)`: Electrónica de potencia y fuentes conmutadas.
  - `📡 CAF: Camps & RF (1)`: Circuitos de alta frecuencia y líneas de transmisión.
  - `🎯 SC: Control (1)`: Sistemas de control feedback y lazos PID.

#### 🗂️ Los 20 Módulos de Simulación:
1. **Puente de Wheatstone & Galgas Extensiométricas:** Viga en voladizo 3D con distribución de tensiones de von Mises.
2. **Sensor Pt100 & Compensación Kelvin:** Conexiones a 2, 3 y 4 hilos en baño termostático 3D.
3. **Amplificador de Instrumentación INA3:** Balanceo de modo común y análisis de CMRR real (AD620 / AD623).
4. **Filtro Activo Sallen-Key Pasobajo:** Aproximaciones Butterworth, Chebyshev y Bessel con diagrama de Bode interactivo.
5. **Muestreo Nyquist, Cuantización ADC & DAC R-2R:** Visualización temporal y espectral con analizador FFT.
6. **Termopares K/J & Bloque Isotérmico:** Compensación electrónica de unión fría (CJC).
7. **Termistor NTC:** Linealización analítica de Taylor en divisor de tensión o puente.
8. **Ruido Térmico Johnson-Nyquist:** Blindaje electromagnético en jaula de Faraday 3D.
9. **Sensor Piezoeléctrico:** Acondicionador de carga frente a amplificador de tensión.
10. **Sensor Capacitivo Diferencial:** Detección síncrona coherente.
11. **Banco R-L-C & Presets Canónicos:** Divisores ADC, desacoplo de rieles, oscilador NE555, driver con diodo volante y resonador LC.
12. **Fuentes Conmutadas DC-DC (PEE):** Convertidores Buck (reductor) y Boost (elevador) en modos CCM y DCM.
13. **Líneas de Transmisión RF & Carta de Smith (CAF):** Coaxial de 50 $\Omega$, cálculo de ROE/VSWR y pérdidas de retorno.
14. **Transistores BJT & MOSFET:** Polarización en continua y amplificación en pequeña señal.
15. **Sistemas de Control Feedback (SC):** Regulador PID continuo con análisis de estabilidad y tiempo de respuesta.
16. **Taller Libre CAD & Simulador MNA:** Resolución matricial nodal con cálculo de equivalentes de Thévenin/Norton y balance de Tellegen.
17. **Amplificador de Aislamiento ISO124:** Barrera dieléctrica capacitiva diferencial de 1500 Vrms, modo común de alta tensión y rechazo IMRR.
18. **Demodulador Coherente Lock-In PSD:** Detección síncrona de señales ultradébiles bajo ruido extremo (SNR < -20 dB).
19. **Transmisor Industrial 4-20 mA:** Bucle de corriente a 2 hilos para Pt100 y diagnóstico de fallos por estándar NAMUR NE43.
20. **Roseta de Galgas a 45° & Círculo de Mohr Dinámico:** Deformaciones principales biaxiales ($\epsilon_1, \epsilon_2$), corte máximo $\gamma_{\max}$ y trazado gráfico del Círculo de Mohr en tiempo real.

#### 🧰 Instrumentación Virtual de Laboratorio:
- **Multímetro Digital Truevolt (6½ Dígitos):** Rangos automáticos y cálculo de incertidumbre Tipo B en tiempo real.
- **Generador de Funciones Arbitrarias (AFG):** Salida de 1 Hz a 10 MHz con 5 formas de onda y modulación.
- **Fuente de Alimentación Triple Regulable:** Canales independientes $\pm 0\dots 30\text{ V}$ con protección CC/CV y riel digital de 3.3V / 5V.
- **Osciloscopio Digital de 4 Canales:** Modos TIME, MATH diferencial, X-Y (figuras de Lissajous) y espectro FFT.
- **Analizador Lógico Digital de 8 Canales:** Decodificador de protocolos serie (I2C, SPI, UART) con tren de datos digital en tiempo real.
- **Inyector de Ruido Térmico Johnson-Nyquist:** Generador de ruido blanco gaussiano calibrado por temperatura ($v_n = \sqrt{4kTR\Delta f}$) con control interactivo de SNR.
- **Generador de Firmware Embebido C/C++:** Generación de código C99 optimizado con DMA para STM32 HAL y ESP32.

---

### 📐 4. Calculadora Metrológica GUM (ISO/IEC 98-3) & Monte Carlo (Supl. 1)
- **Derivadas Numéricas Centrales:** Obtención automática de coeficientes de sensibilidad $c_i = \partial f / \partial x_i$ con perturbación simétrica óptima.
- **Distribuciones de Probabilidad:** Normal ($k=1, 2, 3$), Rectangular ($a/\sqrt{3}$) y Triangular ($a/\sqrt{6}$).
- **Presupuesto de Incertidumbres (Pareto):** Desglose porcentual de varianzas, cálculo de incertidumbre combinada $u_c(y)$ y expandida al 95% ($U_{95\%} = 2 \cdot u_c$).
- **Motor Monte Carlo:** 10.000 iteraciones en menos de 100 ms con histograma de densidad empírico, media $\bar{y}_{MC}$, desviación típica $s(y)_{MC}$ e intervalo de cobertura.
- **6 Plantillas Reales de Examen UPC:** Sensor AD590, Puente de Wheatstone, Termopar K con unión fría, sensor capacitivo, divisor resistivo y disipación en Ley de Ohm.

---

### 🎛️ 5. Diseñador de Filtros Activos, Sensores & Acondicionadores
- **Filtros Sallen-Key de 2º Orden:** Síntesis automática para aproximaciones Butterworth ($Q = 0.7071$), Chebyshev (0.5 dB y 3 dB) y Bessel ($Q = 0.577$).
- **Diagrama de Bode Vectorial:** Trazado de ganancia y fase con retícula logarítmica y marcación visual de $f_c$ a $-3\text{ dB}$.
- **Sensores de Temperatura:**
  - Pt100 (IEC 60751): Ecuación de Callendar-Van Dusen y compensación de cable.
  - Termistor NTC: Linealización óptima de Taylor ($R_{lin} = R_0 \frac{\beta - 2T_0}{\beta + 2T_0}$).
  - Termopares K/J: Curvas termoeléctricas Seebeck y compensación electrónica CJC.
- **Exportación SPICE en 1 Clic:** Sintetiza netlists `.cir` con modelos de amplificadores operacionales para LTspice y KiCad.

---

### 🔌 6. Banco R-L-C & Presets Canónicos GREELEC
- Simulación y trazado de esquemáticos vectoriales dinámicos para topologías electrónicas fundamentales:
  - Divisores resistivos de nivel (Level Shifters 5V a 3.3V).
  - Redes de resistencias normalizadas (E12 / E24 / E96).
  - Redes de desacoplo de rieles de alimentación (100 nF + 10 µF).
  - Circuitos resonantes LC sintonizados.
  - Temporizador astable NE555.
  - Etapas de conmutación de potencia con transistor NPN y diodo volante Schottky.
  - Limitador de corriente para diodos LED con cálculo de potencia.
  - Convertidores DC-DC conmutados (Buck y Boost).
  - Líneas de transmisión RF coaxiales de 50 $\Omega$.

---

### 🗂️ 7. Repaso Activo Anki & Gestor de Exámenes
- **Pestaña Flashcards Nativa:** Explorador de más de 500 afirmaciones y preguntas técnicas oficiales del curso clasificadas por unidad temática.
- **Buscador en Vivo:** Filtrado instantáneo por texto, tema o términos técnicos.
- **Exportación Dual:**
  - Archivo TSV estándar (`_Flashcards_Examen.tsv`) compatible con AnkiWeb y Quizlet.
  - Paquete binario nativo Anki (`_Flashcards_Examen.apkg`) con soporte para MathJax y tema oscuro integrado.

---

## 🚀 Instalación y Requisitos

### Requisitos Previos
- **Python 3.10** o superior en Windows, macOS o Linux.

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Damaga2005/Conversor-HTML-A-MD.git
cd Conversor-HTML-A-MD
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

Dependencias principales:
- `beautifulsoup4`: Análisis y reestructuración del árbol HTML.
- `lxml`: Parser XML de alto rendimiento.
- `pymupdf` (fitz): Extracción de texto, geometría y tablas en documentos PDF.
- `pandas` / `openpyxl`: Procesamiento de tablas tabuladas y hojas de cálculo.
- `genanki`: Generación de paquetes binarios de tarjetas didácticas para Anki.
- `pyinstaller`: Empaquetado en binario ejecutable portable para Windows.

---

## 🖥️ Uso de la Aplicación (GUI y Terminal CLI)

### Iniciar la Interfaz Gráfica
```bash
python conversor_html_notebooklm.py
```

### Uso desde la Línea de Comandos (CLI)
La aplicación incluye soporte completo por terminal:

```bash
# Ayuda y lista de opciones
python conversor_html_notebooklm.py --help

# 1. Conversión de archivo individual HTML a Markdown
python conversor_html_notebooklm.py origen.html destino.md

# 2. Conversión universal de documentos (PDF, DOCX, Notebooks)
python conversor_html_notebooklm.py --pdf documento.pdf salida.md
python conversor_html_notebooklm.py --docx documento.docx salida.md
python conversor_html_notebooklm.py --ipynb practica.ipynb salida.md

# 3. Conversión por lotes de una carpeta completa
python conversor_html_notebooklm.py carpeta_origen/ carpeta_destino/ --preset notebooklm

# 4. Procesamiento secuencial del curso completo (10 Temas + Documentos Maestros)
python conversor_html_notebooklm.py --all-temas carpeta_curso/ dist_course_md/

# 5. Plan de Estudios GREELEC UPC (35 Asignaturas & 424 Preguntas)
python conversor_html_notebooklm.py --degree-plan
python conversor_html_notebooklm.py --degree-stats
python conversor_html_notebooklm.py --degree-export-md mis_guias_upc/
python conversor_html_notebooklm.py --degree-export-anki mis_mazos_anki/

# 6. Motor Independiente de Asignaturas y Calculadoras
python upc_degree_engine.py --list
python upc_degree_engine.py --subject CCE
python upc_degree_engine.py --calc CCE --params '{"vs": 12.0, "r1": 2000, "r2": 4000}'
python upc_degree_engine.py --cheatsheet

# 7. Suite de 37 Solvers Especializados de Ingeniería
# Listar las 37 herramientas agrupadas por rama técnica
python conversor_html_notebooklm.py --tools
python upc_degree_engine.py --tools

# Ejecutar una herramienta con parámetros personalizados (JSON)
python conversor_html_notebooklm.py --tool microstrip_synthesizer --params '{"z0_target": 50.0, "er": 4.4, "h_mm": 1.6}'
python upc_degree_engine.py --tool buck_converter_synthesizer --params '{"vin_v": 24.0, "vout_v": 5.0, "iout_a": 3.0, "fs_khz": 200.0}'
python upc_degree_engine.py --tool lora_toa_and_energy_predictor --params '{"sf": 10, "bw_khz": 125.0, "payload_bytes": 32}'

# 8. Extracción Universal de Fórmulas Matemáticas (Formulario Maestro)
python conversor_html_notebooklm.py --extract-formulas ./mis_apuntes/ ./dist/_Formulario_Maestro.md

# 9. Extracción Universal de Problemas y Ejercicios Resueltos (Banco de Problemas)
python conversor_html_notebooklm.py --extract-problems ./mis_apuntes/ ./dist/_Banco_Problemas.md
```

### Compilar a Ejecutable de Windows (.exe)
```bash
pyinstaller --noconfirm conversor_html_notebooklm.spec
```
El ejecutable compilado estará disponible en `dist/conversor_html_notebooklm/conversor_html_notebooklm.exe`.

### Ejecutar la Suite Completa de Pruebas Automatizadas (40 Tests)
```bash
pytest -v tests/
```

---

## 📁 Estructura del Repositorio

```text
Conversor-HTML-A-MD/
├── conversor_html_notebooklm.py        # Aplicación GUI (9 pestañas) y CLI principal
├── upc_degree_engine.py                # Motor académico del grado GREELEC (35 asignaturas & 424 preguntas)
├── engineering_tools_suite.py          # Suite de 37 solvers numéricos, sintetizadores y generadores de hardware
├── upc_gui_tab.py                      # Pestaña interactiva de escritorio para el Plan UPC GREELEC & Workbench
├── universal_converters.py             # Motor de conversores universales (PDF, DOCX, IPYNB, etc.)
├── Laboratorio_Virtual_Sensores.html   # Simulador web 3D (20 módulos + instrumentos virtuales)
├── conversor_html_notebooklm.spec      # Configuración de compilación PyInstaller
├── requirements.txt                    # Dependencias Python del proyecto
├── data/
│   ├── upc_curriculum_master.json      # Base de datos maestra de las 35 asignaturas con 424 preguntas
│   ├── all_upc_compulsory_guides.json  # Guías docentes oficiales extraídas directamente de PDFs UPC
│   ├── upc_study_guides_md/            # 35 Guías de estudio completas en Markdown para NotebookLM
│   ├── upc_anki_decks/                 # 35 Mazos Anki (.tsv) + Mazo maestro con 424 preguntas
│   └── upc_pdf_raw/                    # 35 PDFs oficiales descargados de la web de la UPC
├── tests/
│   ├── test_engineering_tools.py      # Pruebas automatizadas de los 37 solvers especializados (8 tests)
│   ├── test_upc_curriculum.py          # Pruebas de 35 asignaturas, 424 preguntas y calculadoras (8 tests)
│   ├── test_universal_and_lab.py       # Pruebas de conversores universales y laboratorio (9 tests)
│   ├── test_modern_gui.py              # Verificación de estructura moderna de componentes gráficos (1 test)
│   └── test_modern_theme.py            # Verificación de estilos temáticos ttk y alta resolución DPI (1 test)
├── dist_course_md/                     # Contenidos educativos del curso Sistemes de Mesura
│   ├── Para_Subir_a_NotebookLM/        # Documentos maestros consolidados para NotebookLM
│   ├── Tema 1/ a Tema 10/              # Carpetas individuales de cada unidad temática
│   ├── _Examenes_Finales_Oficiales_UPC.md # Exámenes oficiales (2021, 2024, 2025) resueltos
│   ├── _Problemas_Examen_Resueltos.md    # 10 problemas numéricos de examen paso a paso
│   ├── _Formulario_Oficial_Examen.md     # Formulario consolidado de fórmulas matemáticas
│   ├── _Glosario_Conceptos_Clave.md      # Glosario técnico A-Z
│   ├── _Gran_Indice_Sistemes_de_Mesura.md# Índice general del curso y guía del laboratorio
│   └── Laboratorio_Virtual_Sensores.html # Copia sincronizada del laboratorio virtual
└── README.md                           # Documentación técnica completa
```

---

## 🤖 Integración con Google NotebookLM

1. Abre tu navegador y accede a [Google NotebookLM](https://notebooklm.google.com/).
2. Crea un nuevo cuaderno de estudio (ej: *"Sistemes de Mesura - UPC EEBE"*).
3. Añade como fuentes los archivos ubicados en `dist_course_md/Para_Subir_a_NotebookLM/`:
   - `00_Formulario_Oficial_Examen.md`
   - `00_Glosario_Conceptos_Clave.md`
   - `00_Gran_Indice_Sistemes_de_Mesura.md`
   - `01_Cuaderno_Maestro_Tema_1_Sensores.md` a `10_Cuaderno_Maestro_Tema_10_Calibracion_Incertidumbres.md`
   - `_Examenes_Finales_Oficiales_UPC.md` y `_Problemas_Examen_Resueltos.md`
4. En el panel **Studio**:
   - Genera **Guías de estudio** y **Tarjetas de autoevaluación**.
   - Genera un **Audio Overview** (Podcast didáctico de repaso con dos ponentes virtuales).
5. Utiliza los prompts de `dist_course_md/Para_Subir_a_NotebookLM/_PROMPTS_MAESTROS_NOTEBOOKLM.md` en el chat para obtener respuestas con el máximo rigor académico y matemático.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más información.

---

Desarrollado para estudiantes, investigadores y docentes universitarios de ingeniería electrónica y telecomunicaciones.
