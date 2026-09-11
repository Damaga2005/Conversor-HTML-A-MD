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

### 🔬 7. Laboratorio Virtual Interactivo de Sensores (`Laboratorio_Virtual_Sensores.html`)
- **Simulador Web Autónomo:** Sin dependencias externas ni compilación, ejecutable en cualquier navegador web moderno con estética visual Apple Dark Mode (`#000000`, `#1c1c1e`, `#0a84ff`).
- **5 Módulos de Simulación Gráfica en Tiempo Real (HTML5 Canvas):**
  1. **Puente de Wheatstone:** Ajuste dinámico de galga extensométrica ($\Delta R$), resistencia $R_0$, tensión $V_{in}$ y cálculo de sensibilidad con voltímetro virtual.
  2. **Sensor Pt100 (2, 3 y 4 hilos):** Simulación del error sistemático introducido por la resistencia de los cables de conexión ($R_{cable}$) y demostración interactiva de la compensación a 3 y 4 hilos.
  3. **Amplificador de Instrumentación (INA) & Ruido en Modo Común:** Impacto del CMRR finito ($40 \text{ dB}$ a $120 \text{ dB}$) sobre el rechazo de armónicos parásitos de $50 \text{ Hz}$ de la red eléctrica.
  4. **Filtro Activo Sallen-Key (Pasa-Bajo Butterworth 2º Orden):** Diagrama de Bode en vivo con respuesta en frecuencia, ganancia y fase según los valores de $R$ y $C$.
  5. **Muestreo Nyquist & ADC:** Reconstrucción de onda analógica frente a la frecuencia de muestreo $f_s$ y resolución en bits (1 a 12 bits), visualizando en tiempo real la distorsión por *aliasing* y el error de cuantización.

---

### 📚 8. Documentos Maestros Generados
Al procesar el curso completo, la herramienta sintetiza automáticamente:
1. **`_Problemas_Examen_Resueltos.md`:** 10 problemas de examen numéricos completamente resueltos y explicados.
2. **`Laboratorio_Virtual_Sensores.html`:** Simulador interactivo en tiempo real de instrumentación.
3. **`_Cuaderno_Maestro_Tema_XX.md`:** Documento unificado de alta densidad por cada unidad didáctica.
4. **`_Formulario_Oficial_Examen.md`:** Formulario consolidado con todas las ecuaciones matemáticas del curso (puentes de Wheatstone, amplificadores, incertidumbres GUM, termopares, galgas, etc.).
5. **`_Glosario_Conceptos_Clave.md`:** Vocabulario técnico y definiciones operativas.
6. **`_Gran_Indice_Sistemes_de_Mesura.md`:** Índice general jerárquico con enlaces directos.
7. **`_Instrucciones_Sistema_NotebookLM.md`:** Instrucciones de sistema recomendadas para configurar a Gemini como tutor interactivo en NotebookLM.

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
