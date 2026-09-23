# 230916 - Sistemas Embebidos (EMB)
**Grado en Ingeniería Electrónica de Telecomunicación (GREELEC)**  
*Escuela Técnica Superior de Ingeniería de Telecomunicación de Barcelona (ETSETB - UPC)*

## 1. Ficha Técnica y Metadatos Oficiales
- **Código UPC**: `230916`
- **Acrónimo Oficial**: `EMB`
- **Semestre**: Q4 (Fase Troncal / Especialización)
- **Créditos ECTS**: 6.0 ECTS (150)
- **Departamento Responsable**: 710 - EEL - Departamento de Ingeniería Electrónica
- **Profesorado / Coordinación**: Otros:
- **Guía Docente Oficial en PDF**: [230916_guia_docent.pdf](https://www.upc.edu/grau/guiadocent/pdf/esp/230916/sistemas-embebidos.pdf)

## 2. Descripción General y Requisitos
Arquitecturas de microcontroladores modernos (ARM Cortex-M), registros, periféricos hardware integrados (GPIO, Timers, PWM, ADC/DAC), sistemas de interrupciones vectorizadas y anidadas (NVIC), buses serie de comunicación síncronos y asíncronos (UART, SPI, I2C, CAN), control de acceso directo a memoria (DMA), gestión de bajo consumo y desarrollo de firmware bare-metal en C embebido.

## 3. Objetivos de Aprendizaje y Competencias
- P
- r
- o
- g
- r
- a
- m
- a
- c
- i
- ó
- n
- ,
-  
- a
- n
- á
- l
- i
- s
- i
- s
-  
- y
-  
- d
- i
- s
- e
- ñ
- o
-  
- d
- e
-  
- s
- i
- s
- t
- e
- m
- a
- s
-  
- b
- a
- s
- a
- d
- o
- s
-  
- e
- n
-  
- m
- i
- c
- r
- o
- p
- r
- o
- c
- e
- s
- a
- d
- o
- r
-  
- /
-  
- m
- i
- c
- r
- o
- c
- o
- n
- t
- r
- o
- l
- a
- d
- o
- r
- .
- 

- 

- F
- e
- c
- h
- a
- :
-  
- 0
- 6
- /
- 0
- 9
- /
- 2
- 0
- 2
- 6
- 

- P
- á
- g
- i
- n
- a
- :
-  
- 2
-  
- /
-  
- 4

## 4. Temario y Unidades de Contenido
- {'title': 'Contenido General', 'description': '1.- Introducción Descripción: Descripción de la asignatura. Contexto de la electrónica digital. Opciones de implementación digital. Estructura básica de un sistema basado en CPU. Ejecución de software. Dedicación: 5h Grupo grande/Teoría: 2h Aprendizaje autónomo: 3h 2.- Compatinilidad eléctrica Descripción: Características estáticas y dinámicas. Requisitos y respuestas. Compatibilidad en conexiones. Buses. Uso de colector/drenador abierto en buses no arbitrados. Dedicación: 14h Grupo grande/Teoría: 6h Aprendizaje autónomo: 8h 3.- La CPU Descripción: Unidad de control y datapah. Estructura Von Neumann y Harvard. Ciclo de instrucción. Métricas de velocidad y consumo. Optimización de CPUs. Buses externos. Endianness. Jerarquía de memoria. Memoria cache. Protección y memoria virtual. Dedicación: 18h Grupo grande/Teoría: 8h Aprendizaje autónomo: 10h 4.- Subsistema de memoria Descripción: Tipos de memorias. Señales típicas en memorias SRAM y ROM. Decodificación de memoria en CPUs y MCUs. Memorias DRAM y otras. Dedicación: 23h Grupo grande/Teoría: 10h Aprendizaje autónomo: 13h Fecha: 06/09/2026 Página: 3 / 4 5.- Temporización Descripción: Respuestas temporales. Requisitos de Setup y Hold. Evaluación de temporización en lectura y escritura. Temporización en DRAMs. Dedicación: 14h Grupo grande/Teoría: 6h Aprendizaje autónomo: 8h 6.- Entrada/Salida Descripción: Conexión de periféricos. Mapa de I/O. Registros. Sincronización por polling e interrupción. RSIs. Contexto de ejecución. Enmascaramiento. Latencias. Excepciones. Ejemplos de periféricos: Temporizadores, Convertidores, Comunicaciones. Dedicación: 16h Grupo grande/Teoría: 7h Aprendizaje autónomo: 9h Prácticas Descripción: Desarrollo con un sistema ARM Cortex M4. Entorno de desarrollo. Depuración. Acceso a periféricos. Interrupciones. Medidas de temporización. Uso de hilos de ejecución. Dedicación: 60h Grupo pequeño/Laboratorio: 26h Aprendizaje autónomo: 34h'}

## 5. Modelado Matemático y Fórmulas Clave (LaTeX)
### 5.1 Periodo de Interrupción de Temporizador (Timer)
$$
T_{\text{int}} = \frac{(\text{PSC} + 1) \cdot (\text{ARR} + 1)}{f_{\text{clk}}}
$$

### 5.2 Baud Rate en Transmisión UART
$$
\text{Baud} = \frac{f_{\text{clk}}}{16 \cdot \text{USARTDIV}}
$$

### 5.3 Resolución de Convertidor ADC de N Bits
$$
\Delta V = \frac{V_{\text{ref}}}{2^N}, \quad V_{\text{medido}} = \text{ADC\_VAL} \cdot \frac{V_{\text{ref}}}{2^N - 1}
$$

### 5.4 Frecuencia de Bus SPI Síncrono
$$
f_{\text{SCK}} = \frac{f_{\text{bus}}}{2^{\text{BR}[2:0] + 1}}
$$

### 5.5 Ciclo de Trabajo (Duty Cycle) PWM
$$
D = \frac{\text{CCR}}{\text{ARR}} \times 100\%
$$

## 6. Banco de Ensayos / Laboratorio Virtual
```c
// EMB - Firmware de Interrupcion por Timer y Generacion PWM en C Embebido (ARM Cortex-M)
#include <stdint.h>
#define TIM2_ARR  (*(volatile uint32_t*)0x4000002C)
#define TIM2_CCR1 (*(volatile uint32_t*)0x40000034)
void TIM2_IRQHandler(void) {
    // Rutina de Servicio de Interrupcion (ISR)
    TIM2_CCR1 = (TIM2_CCR1 + 10) % TIM2_ARR;
}
```

## 7. Preguntas de Autoevaluación y Examen con Justificación Técnica
#### Pregunta 1
**¿El controlador de interrupciones NVIC en arquitecturas ARM Cortex-M soporta anidamiento de interrupciones por niveles de prioridad?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Una interrupción de mayor prioridad desaloja a una de menor prioridad en ejecución.

#### Pregunta 2
**¿El protocolo de comunicación I2C requiere resistencias de pull-up externas en las líneas SDA y SCL porque sus salidas son de colector/drenador abierto?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Permite la conexión cableada en 'wired-AND' y evita colisiones por contención.

#### Pregunta 3
**El protocolo SPI requiere direccionamiento explícito por software de 7 bits para seleccionar cada esclavo.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. SPI utiliza líneas físicas dedicadas de selección de chip (Chip Select / SS). El direccionamiento por 7 bits es de I2C.

#### Pregunta 4
**¿El controlador DMA permite transferir bloques de datos entre periféricos y la memoria RAM sin intervención de la CPU?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Libera a la CPU de bucles continuos de copia reduciendo consumo y latencia.

#### Pregunta 5
**¿Una variable compartida entre la rutina de interrupción (ISR) y el bucle principal de control debe declararse con el cualificador 'volatile'?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Evita que el compilador optimice o cachee su lectura en un registro interno de la CPU.

#### Pregunta 6
**La comunicación UART es un protocolo serie síncrono que transmite una línea de reloj compartida entre transmisor y receptor.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. Es asíncrono (Universal Asynchronous Receiver-Transmitter); se sincroniza mediante bits de start y stop y un baud rate acordado.

#### Pregunta 7
**¿Un temporizador configurado con prescaler PSC divide la frecuencia del reloj maestro por el factor PSC + 1?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. El contador de prescaler cuenta de 0 a PSC.

#### Pregunta 8
**¿El convertidor analógico-digital (ADC) de aproximaciones sucesivas (SAR) requiere N ciclos de reloj para una conversión de N bits?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Resuelve un bit por ciclo mediante un comparador y un DAC interno.

#### Pregunta 9
**En el protocolo I2C, la condición de parada (STOP) se genera con una transición de nivel alto a bajo en SDA mientras SCL está en alto.**
- **Respuesta**: `[F]` (Falso)
- **Justificación Teórica**: Falso. La condición STOP es una transición de bajo a alto en SDA con SCL en alto (la de alto a bajo es la condición de START).

#### Pregunta 10
**¿El temporizador Watchdog (WDT) restablece el microcontrolador si el software queda bloqueado y no refresca el contador periódicamente?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Mecanismo de seguridad crítico contra bloqueos de software.

#### Pregunta 11
**¿En los modos de suspensión de muy bajo consumo (Deep Sleep/Standby), se desactivan osciladores y reguladores no esenciales?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Permite operar dispositivos IoT a batería durante años.

#### Pregunta 12
**¿El bit de paridad en una trama UART permite detectar errores de bit único en la recepción de un carácter?**
- **Respuesta**: `[V]` (Verdadero)
- **Justificación Teórica**: Verdadero. Verifica si el número total de unos coincide con la paridad par o impar configurada.

## 8. Sistema de Evaluación y Bibliografía Recomendada
**Evaluación**: Cualquier acto de fraude académico, plagio o uso o mera tenencia al alcance de medios no autorizados en cualquier actividad de
evaluación comportará la calificación de cero (0) en la prueba o entrega afectada. Además, de acuerdo con la normativa de la
Universidad, la posible derivación de los hechos para la apertura de un expediente disciplinario implicará que la asignatura quede en
el estado provisional de "pendiente de evaluación" hasta la resolución del expediente. La gestión de estas incidencias se lleva a cabo
de acuerdo con el Marco de actuación para la integridad académica en la evaluación de la UPC.
50 % Examen Final
30 % Prácticas
20 % Evaluación continua
En el examen de reevaluación sólo se reevaluan los contenidos de teoria, por lo que la nota resultante de la reevaluación será:
70% Examen de Reevaluación
30% Prácticas previas

Fecha: 06/09/2026
Página: 4 / 4

**Bibliografía de Referencia**:
- - Clements, A. Microprocessor systems design: 68000 hardware, software, and interfacing. 3rd ed. Boston: PWS, 1997. ISBN
- 0534948227.
- - Cabestany Moncusí, J. Disseny de sistemes digitals amb microprocessadors [en línea]. 2a ed. Barcelona: Edicions UPC, 2000
- [Consulta: 10/07/2019]. Disponible a: http://hdl.handle.net/2099.3/36234. ISBN 8483013657.
- Complementaria: