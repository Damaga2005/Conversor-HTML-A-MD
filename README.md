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
- **Visor Markdown Integrado:** Lee los documentos generados directamente en la app con resaltado de sintaxis, conteo de palabras y buscador con resaltado en tiempo real.
- **Acceso Directo a la Nube:** Botón para abrir directamente [Google NotebookLM](https://notebooklm.google.com/) en tu navegador predeterminado.

---

### 🔍 3. Buscador Ultrarrápido estilo macOS Spotlight
- Pulsa el botón **Spotlight** o el atajo de búsqueda para indexar en milisegundos todos los archivos Markdown de tu curso.
- Búsqueda por palabras clave, fórmulas, conceptos o nombres de preguntas, con previsualización del fragmento y salto directo al visor.

---

### 🃏 4. Generador de Flashcards y Paquetes Anki (.apkg)
- Extrae automáticamente los bancos de preguntas interactivas presentes en los scripts HTML (`BANC`, `DATA.items`, `ITEMS`).
- Genera el mazo oficial empaquetado **`_Flashcards_Examen.apkg`** listo para importar en [Anki](https://apps.ankiweb.net/) con tarjetas de dos caras estilizadas (anverso con enunciado y tema, reverso con respuesta oficial, color condicional y justificación técnica).
- Exporta en paralelo el fichero `_Flashcards_Examen.tsv` compatible con Quizlet y herramientas de repaso.

---

### 🎯 5. Simulador Oficial de Examen UPC
- Simulador de examen integrado con la reglamentación y baremo oficial de la UPC:
  $$\text{Nota Final} = \frac{\text{Aciertos} \times 1.00 - \text{Fallos} \times 0.33}{\text{Total de Preguntas}} \times 10.0$$
- Modo test rápido (10 preguntas), simulacro parcial (20 preguntas), tema completo (50 preguntas) o examen final con el banco de 500 preguntas del curso.
- Retroalimentación pedagógica instantánea con solución oficial (`VERTADER` / `FALS`) y explicación teórica.

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

### 🔬 7. Laboratorio Virtual Interactivo de Sensores (`Laboratorio_Virtual_Sensores.html`) — v4.0 Ultimate Edition
- **Simulador Web Autónomo de Categoría PhET / Apple Studio Display:** Sin dependencias externas, sin CDNs ni compilación. Ejecutable en local en cualquier navegador web moderno con estética visual Apple Dark Mode (`#000000`, `#1c1c1e`, `#0a84ff`, `#30d158`) y renderizado Retina High-DPI.
- **🔊 Síntesis Acústica en Tiempo Real con Web Audio API:** Permite *escuchar* la física de los sensores directamente en el navegador:
  - **Aliasing Acústico en ADC:** Escucha el colapso tonal de Nyquist al reducir la frecuencia de muestreo $f_s$ por debajo de $2 f_{in}$.
  - **Zumbido de Red 50 Hz en INA/Filtros:** Escucha el zumbido de modo común desaparecer al elevar el CMRR o al pasar por el filtro pasobajos Sallen-Key.
  - **Ruido Blanco Térmico Johnson:** Escucha el silbido de ruido blanco variar en amplitud según la temperatura y el valor óhmico.
- **📈 Osciloscopio Activo a 60 FPS (`requestAnimationFrame`):** Formas de onda continuas en barrido temporal interactivo con botón Play/Pausa, controles de escala (Volts/Div y Time/Div) y retícula phosphor-green.
- **10 Módulos de Simulación Física y Circuital en Tiempo Real (HTML5 Canvas):**
  1. **Puente de Wheatstone & Galgas:** Selector 1/4, 1/2 y puente completo, deformación $\varepsilon$, viga en voladizo animada con zonas de tracción y compresión, esquema en rombo y cálculo de sensibilidad ($\mu\text{V}/\mu\varepsilon$).
  2. **Sensor Pt100 (2, 3 y 4 hilos):** Sonda industrial, error sistemático por resistencia de cables ($R_{cable}$) y demostración gráfica de compensación con termómetro comparativo.
  3. **Amplificador de Instrumentación INA3 & CMRR Real:** Arquitectura de 3 amplificadores operacionales ($A_1, A_2$ con $R_g$, y $A_3$ sustractor con tolerancia $\delta$), con osciloscopio dual mostrando el rechazo de armónicos parásitos de $50\text{ Hz}$.
  4. **Filtro Activo Sallen-Key (Butterworth & Chebyshev):** Diagrama de Bode en vivo con respuesta en frecuencia, ganancia en dB y fase, junto a visualización temporal de filtrado.
  5. **Muestreo Nyquist & ADC:** Reconstrucción de onda analógica frente a la frecuencia de muestreo $f_s$ y resolución en bits (3 a 16 bits), con analizador de espectro FFT animado que muestra el deslizamiento del *alias*.
  6. **Termopares & Compensación de Unión Fría (CJC):** Tipos K, J y T con unión caliente $T_h$ y de referencia $T_0$, simulando la corrección electrónica con sensor LM35/Pt100.
  7. **Linealización de Termistores NTC (Circuito de Taylor):** Curva exponencial $R(T)$ y cálculo de la resistencia en paralelo $R_p = R_0 \frac{\beta - 2T_0}{\beta + 2T_0}$ que anula la segunda derivada en el punto de inflexión.
  8. **Ruido Térmico Johnson-Nyquist & SNR:** Ruido de tensión $v_n = \sqrt{4 k_B T R \Delta f}$, densidad espectral en $\text{nV}/\sqrt{\text{Hz}}$, relación señal/ruido (SNR) y osciloscopio virtual.
  9. **Sensor Piezoeléctrico & Amplificador de Carga vs Tensión:** Cristal dinámico piezoeléctrico de cuarzo/PZT ($d_{33}$), modelado de respuesta en frecuencia $f_L = \frac{1}{2\pi R_f C_f}$, demostración gráfica de la inmunidad al cable largo ($C_c$) del amplificador de carga frente a la atenuación severa del amplificador de tensión.
  10. **Sensor Capacitivo Diferencial & Detección Síncrona (Lock-in/PSD):** Transductor capacitivo diferencial de 3 placas (placa central móvil), excitación senoidal en antifase, y desmodulación síncrona sensible a la fase (PSD) con filtro pasobajo para eliminar la portadora y recuperar el signo exacto del desplazamiento.
- **🎯 10 Retos de Examen Interactivos:** Cada módulo incluye un problema numérico oficial de examen UPC con verificación en tiempo real de tolerancia y resolución detallada paso a paso.
- **🖥️ Modo Presentación Pantalla Completa:** Vista inmersiva optimizada para docencia, proyectores de aula y monitores Ultra-Wide con tecla rápida o botón Fullscreen.
- **📄 Exportador de Informes de Prácticas:** Genera y descarga en 1 clic un informe experimental completo en formato Markdown con todos los parámetros actuales y deducciones de los 10 temas.

---

### 📚 8. Documentos Maestros Generados
Al procesar el curso completo, la herramienta sintetiza automáticamente:
1. **`_Examenes_Finales_Oficiales_UPC.md`:** 3 exámenes finales oficiales completos (2021, 2024, 2025) resueltos con 100% rigor analítico en LaTeX.
2. **`_Problemas_Examen_Resueltos.md`:** 10 problemas numéricos de nivel de examen completamente resueltos y explicados.
3. **`Laboratorio_Virtual_Sensores.html`:** Simulador interactivo en tiempo real de instrumentación (v4.0 Ultimate Edition).
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
