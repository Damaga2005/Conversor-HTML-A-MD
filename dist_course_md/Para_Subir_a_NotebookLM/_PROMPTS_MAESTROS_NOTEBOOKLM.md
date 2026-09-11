# 🤖 Prompts Maestros para Google NotebookLM
> 🏛️ **Curso:** Sistemes de Mesura · ETSETB / EEBE (UPC)  
> 📚 **Instrucciones:** Abre tu cuaderno en [NotebookLM](https://notebooklm.google.com/), sube los 13 archivos de esta carpeta y copia y pega cualquiera de los siguientes prompts en el chat para obtener respuestas de nivel de examen universitario.

---

### 🎯 Prompt 1: Tribunal Examinador UPC (Simulacro de Examen con Corrección Oficial)
`	ext
Actúa como el tribunal examinador de la asignatura 'Sistemes de Mesura' de la UPC.
Quiero que me hagas un examen de 5 preguntas tipo test, una a una.
Reglas:
1. Formula una pregunta técnica desafiante con 4 opciones (A, B, C, D) o afirmación Verdadero/Falso basada exclusivamente en las fuentes cargadas.
2. Espera a que yo te responda.
3. Tras mi respuesta, dime si he acertado o fallado, aplica el baremo UPC (+1 acierto, -0.33 fallo, 0 en blanco) y explícame la deducción física y la fórmula matemática exacta que justifica la respuesta correcta.
4. Luego pasa a la siguiente pregunta.
Comienza con la Pregunta 1.
`

---

### 📐 Prompt 2: Resolución y Deducción Rigurosa de Fórmulas
`	ext
Basándote en el archivo '_Formulario_Oficial_Examen.md' y los Cuadernos Maestros, resuelve el siguiente problema explicando cada paso:
1. Enuncia la ley física y las fórmulas involucradas.
2. Especifica las unidades en el Sistema Internacional de cada variable.
3. Muestra el desarrollo matemático paso a paso sin omitir pasos algebraicos.
4. Proporciona el resultado numérico final con su correspondiente margen de tolerancia e incertidumbre.

Problema a resolver: [Escribe aquí tu enunciado o pregunta numérica]
`

---

### 🔍 Prompt 3: Tabla Comparativa y Diferencias Críticas
`	ext
Genera una tabla comparativa exhaustiva entre los siguientes conceptos del temario: [Ejemplo: Filtro Butterworth vs Chebyshev vs Bessel / Puente de Wheatstone 1/4 vs Medio Puente vs Puente Completo / ADC Flash vs SAR vs Sigma-Delta].
Incluye:
- Principio físico de operación.
- Ventajas y desventajas principales.
- Sensibilidad, linealidad y respuesta temporal/frecuencial.
- Ecuación matemática definitoria.
- Ejemplo típico de aplicación en instrumentación médica o industrial.
`

---

### 🧠 Prompt 4: Tutor Socrático de Conceptos Difíciles
`	ext
Actúa como mi profesor particular de instrumentación electrónica.
Explícame el concepto de [Ejemplo: Relación de Rechazo al Modo Común (CMRR) / Ruido Johnson-Nyquist / Aperture Jitter / Guía GUM de Incertidumbres] como si tuviera que explicárselo a un ingeniero novato.
Usa analogías intuitivas, muestra por qué surge físicamente en el circuito y concluye con una pregunta para comprobar si lo he entendido bien.
`
