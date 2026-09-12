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

### 🔬 8. Laboratorio Virtual Interactivo de Sensores & Grado GREELEC (`Laboratorio_Virtual_Sensores.html`) — v6.0 Enterprise 3D Edition
- **Simulador Industrial Web de Categoría Multisim / Keysight BenchVue / SPICE:** 100% autónomo, ejecutable en local sin internet ni CDNs, optimizado para los planes de estudio de la UPC (ETSETB / EEBE).
- **🌐 Motor WebGL 3D Nativo Acelerado por GPU (60 FPS):**
  - **Rotación Orbital y Zoom Interactivos:** Control total con ratón (arrastrar para orbitar, rueda para zoom, doble clic para centrar).
  - **Iluminación Realista Phong:** Materiales metálicos (oro, acero pulido, cobre) y dieléctricos con reflejos especulares dinámicos.
  - **Modelos Físicos 3D Paramétricos:**
    * *Viga en voladizo 3D deformable* con curvatura elástica de Euler-Bernoulli y mapa de calor de tensiones mecánicas de von Mises.
    * *Sonda industrial Pt100 3D* con termopozo de acero inoxidable y cabezal DIN B sumergida en baño termostático agitado.
    * *Acelerómetro piezoeléctrico 3D* con cristal de cuarzo $d_{33}$ deformable bajo masa sísmica.
    * *Sensor capacitivo diferencial MEMS 3D* de 3 placas móviles con visualización de desplazamiento micrométrico.
    * *Protoboard 3D de Electrónica* con matriz de inserción, resistencias axiales con anillos de color, condensadores radiales y encapsulado DIP-8.
    * *Convertidor DC-DC Buck/Boost 3D* con inductor toroidal de cobre, MOSFET TO-263 con disipador, diodo Schottky y condensador electrolítico Low-ESR.
    * *Cable Coaxial de Alta Frecuencia 3D* seccionado por capas (cubierta PVC, malla de blindaje, dieléctrico PTFE, vivo) y conector SMA dorado.
    * *Etapa Transistor BJT/MOSFET 3D* con encapsulado TO-92, resistencias de película metálica y condensadores cerámicos de paso.
    * *Actuador y Lazo de Control PID 3D* con servomotor DC, disco encoder óptico ranurado, horquilla optoacopladora y módulo PID industrial con display digital.
- **📐 Esquemáticos Circuitales de Precisión (100% Cobertura Vectorial):**
  - **Cobertura Absoluta de los 15 Módulos:** Eliminados por completo los bloques genéricos o esquemas en negro. Cada módulo cuenta con representación de grado libro de texto (normas IEC 60617 / IEEE Std 315) con valores dinámicos calculados en tiempo real.
  - **Carta de Smith Vectorial Interactiva (Módulo 13):** Proyección polar en vivo del coeficiente de reflexión complejo $\Gamma = |\Gamma| e^{j\theta}$, círculos de resistencia normalizada ($r = 0.5, 1.0, 2.0$), arcos de reactancia ($x = \pm 0.5, \pm 1.0$) y círculo de ROE constante.
- **🎛️ Banco de Instrumentación con Réplicas Fidedignas:**
  - **Keysight 34465A Truevolt 6½ Digit DMM:** Pantalla digital VFD de alta resolución, barra analógica bar-graph con rangos automáticos y cálculo de incertidumbre metrológica $u_B$ en vivo.
  - **Osciloscopio Tektronix TBS2000B (Phosphor 60 FPS):**
    * *Modo Doble `[TIME DOMAIN]` / `[FFT SPECTRUM]`:* Permite conmutar con 1 clic al análisis espectral de Fourier con span de $500\text{ Hz}$, detección de picos armónicos y suelo de ruido en dBV.
    * *Formas de Onda Específicas por Física Circuital:*
      - *Buck/Boost:* Onda PWM de nodo switch $V_{SW}$ con ringing de conmutación y rizado triangular de corriente en inductor $i_L(t)$.
      - *Líneas RF:* Onda incidente $V^+(t)$, onda reflejada $V^-(t)$ y envolvente de onda estacionaria con nodos y vientres de tensión según VSWR.
      - *BJT/MOSFET:* Señal sinusoidal de entrada y señal amplificada invertida $180^\circ$ con saturación y corte visibles ante excursión excesiva.
      - *Control PID:* Respuesta temporal al escalón unitario con tiempo de subida $t_r$, sobreoscilación $M_p$ y tiempo de establecimiento $t_s (2\%)$.
    * *Cursores Duales de Medición:* Líneas móviles de precisión para $\Delta t$, $\Delta V$ y cálculo instantáneo de frecuencia $f = 1/\Delta t$.
    * *Exportación de Telemetría a CSV:* Descarga inmediata de las señales adquiridas para su procesamiento en Python, MATLAB o Excel.
- **🎨 Decodificador Interactivo de Código de Colores de Resistencias:**
  - Modal integrado con visualizador vectorial SVG interactivo de resistencias axiales (normas E12 / E24 / E96).
  - Cálculo instantáneo de valor nominal, tolerancia y rango admisible $[R_{\min}, R_{\max}]$, con botón para inyectar el valor directamente en el banco de simulación.
- **15 Módulos de Simulación Física y Circuital (Temario Sistemes de Mesura + Plan de Estudios GREELEC UPC):**
  1. *Puente de Wheatstone & Galgas (1/4, 1/2 y completo con viga 3D)*
  2. *Pt100 y compensación a 4 hilos Kelvin con sonda DIN B 3D*
  3. *INA3 & CMRR real con amplificadores AD623/AD620*
  4. *Filtro activo Sallen-Key pasobajo de 2º orden con respuesta Butterworth/Chebyshev*
  5. *Muestreo Nyquist & ADC con analizador FFT y DAC R-2R*
  6. *Termopares K/J & compensación de unión fría (CJC) con bloque isotérmico*
  7. *Termistor NTC & linealización analítica de Taylor*
  8. *Ruido térmico Johnson-Nyquist & relación SNR con jaula de Faraday*
  9. *Sensor piezoeléctrico & amplificador de carga vs tensión*
  10. *Sensor capacitivo diferencial & detección síncrona lock-in (PSD)*
  11. *🔌 Banco R-L-C & Presets Canónicos de Laboratorio (13 proyectos típicos: divisores ADC, desacoplo digital 100nF+10µF, 555 astable/monoestable, driver relé con diodo volante 1N4007, limitadores LED, resonador LC)*
  12. *⚡ Fuentes Conmutadas DC-DC: Buck (Reductor) & Boost (Elevador) — GREELEC PEE (Procesado de Energía Eléctrica)*
  13. *📡 Líneas de Transmisión RF & Carta de Smith Vectorial — GREELEC CAF (Circuitos de Alta Frecuencia / Ondas)*
  14. *🎛️ Transistores BJT & MOSFET: Polarización y Pequeña Señal — GREELEC DE/CA (Dispositivos & Circuitos Analógicos)*
  15. *🎯 Sistemas de Control Feedback & Regulador PID Continuo — GREELEC SC (Sistemas de Control)*
- **🎯 15 Retos de Examen Oficiales UPC:** Problemas numéricos reales integrados en cada módulo con comprobación automática de tolerancia y desglose algebraico de la solución.
- **📄 Exportador de Informes Experimentales:** Generador de informe estructurado en Markdown con todas las mediciones, métricas y ecuaciones, descargable o copiable al portapapeles en 1 clic.

---

### 📚 8. Documentos Maestros Generados
Al procesar el curso completo, la herramienta sintetiza automáticamente:
1. **`_Examenes_Finales_Oficiales_UPC.md`:** 3 exámenes finales oficiales completos (2021, 2024, 2025) resueltos con 100% rigor analítico en LaTeX.
2. **`_Problemas_Examen_Resueltos.md`:** 10 problemas numéricos de nivel de examen completamente resueltos y explicados.
3. **`Laboratorio_Virtual_Sensores.html`:** Simulador industrial de física e instrumentación 3D (v5.0 Enterprise 3D Edition).
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
