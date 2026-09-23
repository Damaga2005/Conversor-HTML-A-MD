# 🍏 Conversor Universal de Documentación Técnica & Suite Metrológica UPC

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Interface: Apple Dark](https://img.shields.io/badge/UI-Apple%20Liquid%20Glass%20Dark-black.svg)]()
[![Target: NotebookLM](https://img.shields.io/badge/Optimized%20for-Google%20NotebookLM-4285F4.svg)]()
[![LaTeX: MathML & OMML Supported](https://img.shields.io/badge/LaTeX-MathML%20%7C%20OMML%20%E2%86%92%20LaTeX-brightgreen.svg)]()
[![Virtual Lab: 20 Modules 3D](https://img.shields.io/badge/Virtual%20Lab-20%20Modules%20WebGL%203D-orange.svg)]()
[![Tests: Pytest Passing](https://img.shields.io/badge/tests-9%2F9%20passing-success.svg)]()

> Suite integral de ingeniería documental, conversores universales de alta fidelidad y estación de trabajo virtual diseñada para transformar contenidos educativos, técnicos e interactivos (HTML, PDF, DOCX, IPYNB, MathML, scripts de examen) en **Markdown técnico estructurado de máxima pureza**, 100% optimizado para **Google NotebookLM**, Gemini, Claude, Obsidian y ChatGPT.
> 
> Incluye el **Laboratorio Virtual de Sensores e Instrumentación 3D (v8.5 Enterprise Workbench)** con 20 módulos circuitales organizados por asignaturas oficiales de la **Universitat Politècnica de Catalunya (UPC)**, calculadora metrológica GUM con simulación Monte Carlo, diseñador de filtros activos, banco de componentes R-L-C y gestor de flashcards con 500 preguntas de examen.

---

## 📑 Tabla de Contenidos
- [✨ Características Principales](#-características-principales)
  - [🔄 1. Conversores Universales de Archivos de Alta Fidelidad](#-1-conversores-universales-de-archivos-de-alta-fidelidad-universal_converterspy)
  - [🎨 2. Interfaz Gráfica de Escritorio (Apple Liquid Glass Dark)](#-2-interfaz-gráfica-de-escritorio-apple-liquid-glass-dark)
  - [🔬 3. Laboratorio Virtual de Sensores e Instrumentación 3D](#-3-laboratorio-virtual-de-sensores-e-instrumentación-3d-v85-enterprise)
  - [📐 4. Calculadora Metrológica GUM (ISO/IEC 98-3) & Monte Carlo](#-4-calculadora-metrológica-gum-isoiec-98-3--monte-carlo-supl-1)
  - [🎛️ 5. Diseñador de Filtros Activos & Sensores](#-5-diseñador-de-filtros-activos-sensores--acondicionadores)
  - [🔌 6. Banco R-L-C & Presets Canónicos GREELEC](#-6-banco-r-l-c--presets-canónicos-greelec)
  - [🗂️ 7. Repaso Activo Anki & Gestor de Exámenes](#-7-repaso-activo-anki--gestor-de-exámenes)
- [🚀 Instalación y Requisitos](#-instalación-y-requisitos)
- [🖥️ Uso de la Aplicación (GUI y Terminal CLI)](#-uso-de-la-aplicación-gui-y-terminal-cli)
- [📁 Estructura del Repositorio](#-estructura-del-repositorio)
- [🤖 Integración con Google NotebookLM](#-integración-con-google-notebooklm)
- [📄 Licencia](#-licencia)

---

## ✨ Características Principales

### 🔄 1. Conversores Universales de Archivos de Alta Fidelidad (`universal_converters.py`)
Módulo independiente de conversión universal con algoritmos especializados:
- **PDF a Markdown (PyMuPDF):** Extracción inteligente con detección de encabezados jerárquicos, tablas estructuradas en formato GitHub Flavored Markdown (GFM) e inferencia de bloques matemáticos en $\LaTeX$.
- **Word DOCX a Markdown (OMML a LaTeX):** Parseador de Office Math Markup Language (OMML) que traduce fórmulas matemáticas complejas nativas de Microsoft Word (`<m:oMath>`, `<m:f>`, `<m:sSup>`, `<m:rad>`) directamente a $\LaTeX$ puro sin pérdidas.
- **Jupyter Notebook (`.ipynb`) a Markdown:** Extracción secuencial de celdas Markdown y código fuente Python, preservando salidas de consola, trazas de ejecución e imágenes gráficas generadas.
- **Extractor Automático de Imágenes Base64:** Decodifica recursos gráficos embebidos y los almacena físicamente en la carpeta `assets/` con control de hash SHA-256 para evitar duplicaciones.
- **Excel (`.xlsx`) y CSV a Tablas Markdown:** Conversor tipado con detección de números, porcentajes y alineación columnar automática.
- **Markdown a HTML Imprimible / PDF Académico:** Motor de maquetación con estilos de alta legibilidad (Apple Pro / San Francisco), integración con MathJax 3 y reglas CSS `@media print` optimizadas para generar PDFs A4 con un solo clic.
- **Extractor de Formulario Maestro:** Escaneo automatizado de repositorios documentales para recopilar todas las ecuaciones matemáticas en una hoja de referencia unificada.
- **Extractor de Netlists SPICE:** Detección de esquemas y circuitos en notas técnicas para exportar archivos `.cir` listos para simulación en LTspice, NGSpice o KiCad.
- **Generador de Glosario Técnico A-Z:** Indexación alfabética automática de acrónimos y definiciones con enlace a sus fuentes.
- **Conversión Universal en Lote (`batch_convert_universal`):** Exploración recursiva de directorios para procesar simultáneamente colecciones de archivos heterogéneos (PDF, DOCX, IPYNB, CSV, XLSX, HTML).

---

### 🎨 2. Interfaz Gráfica de Escritorio (Apple Liquid Glass Dark)
La aplicación de escritorio (`conversor_html_notebooklm.py`) cuenta con una interfaz organizada en **8 pestañas temáticas** navegables mediante un selector segmentado tipo macOS:
1. **HTML a MD:** Conversor interactivo con previsualización, extracción de imágenes y perfiles preconfigurados.
2. **Universal:** Panel de control de conversión multi-formato (PDF, DOCX, IPYNB, CSV, Excel) con selección de opciones avanzadas y consola asíncrona en tiempo real.
3. **Visor Markdown:** Lector con resaltado de sintaxis, barra de productividad (zoom tipográfico A-/100%/A+, estadísticas en vivo de palabras, caracteres, fórmulas y tiempo de lectura) y exportador HTML/PDF.
4. **Biblioteca:** Acceso directo a documentos maestros, exámenes resueltos y enlaces de estudio.
5. **Calculadora GUM:** Presupuesto de incertidumbres según la norma ISO/IEC 98-3 con simulación Monte Carlo.
6. **Filtros Activos:** Calculadora y sintetizador de filtros Sallen-Key con diagrama de Bode en tiempo real y acondicionadores analógicos.
7. **Banco R-L-C:** Simulador de topologías canónicas y esquemáticos vectoriales dinámicos.
8. **Flashcards Anki:** Visor de preguntas de autoevaluación, buscador interactivo en vivo, filtrado temático y exportador de mazos Anki (`.apkg` y `.tsv`).

#### ⚡ Atajos de Teclado Globales:
| Atajo | Acción |
| :--- | :--- |
| `Ctrl + 1` .. `Ctrl + 8` | Cambio instantáneo a cualquiera de las 8 pestañas |
| `Ctrl + O` | Abrir diálogo de selección de archivo o carpeta de origen |
| `Ctrl + S` | Guardar o exportar resultados de la pestaña activa |
| `F5` / `Ctrl + R` | Recalcular parámetros activos (GUM, Filtros, RLC) |
| `Drag & Drop` | Arrastrar archivos PDF, DOCX, IPYNB, XLSX o HTML conmuta y precarga la herramienta correspondiente |

---

### 🔬 3. Laboratorio Virtual de Sensores e Instrumentación 3D (v8.5 Enterprise)
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

# 5. Generación de mazos Anki directamente por consola
python conversor_html_notebooklm.py --anki dist_course_md/
```

### Compilar a Ejecutable de Windows (.exe)
```bash
pyinstaller --noconfirm conversor_html_notebooklm.spec
```
El ejecutable compilado estará disponible en `dist/conversor_html_notebooklm/conversor_html_notebooklm.exe`.

### Ejecutar la Suite de Pruebas Automatizadas
```bash
pytest -v tests/test_universal_and_lab.py
```

---

## 📁 Estructura del Repositorio

```text
Conversor-HTML-A-MD/
├── conversor_html_notebooklm.py        # Aplicación GUI (8 pestañas) y CLI principal
├── universal_converters.py             # Motor de conversores universales (PDF, DOCX, IPYNB, etc.)
├── Laboratorio_Virtual_Sensores.html   # Simulador web 3D (20 módulos + instrumentos virtuales)
├── conversor_html_notebooklm.spec      # Configuración de compilación PyInstaller
├── requirements.txt                    # Dependencias Python del proyecto
├── tests/
│   └── test_universal_and_lab.py       # Pruebas automatizadas con Pytest (100% passing)
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
