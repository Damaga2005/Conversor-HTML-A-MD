# 📚 Cuaderno Maestro: Tema 8

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 8` | 📄 **Capítulos incluidos:** 8  
> 📅 **Generado:** 2026-09-11 19:10

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 8 — Condicionament de sensors en alterna · Lectura prèvia](#unitat-8-condicionament-de-sensors-en-alterna-lectura-prèvia)
2. [Sensors reactius, freqüència de treball i cadena de condicionament](#sensors-reactius-freqüència-de-treball-i-cadena-de-condicionament)
   - [1 El sensor reactiu com a impedància complexa](#1-el-sensor-reactiu-com-a-impedància-complexa)
   - [2 La freqüència de treball](#2-la-freqüència-de-treball)
   - [3 Les dues aproximacions al condicionament](#3-les-dues-aproximacions-al-condicionament)
   - [4 La cadena de condicionament lineal](#4-la-cadena-de-condicionament-lineal)
   - [5 Models canònics del sensor](#5-models-canònics-del-sensor)
   - [6 Dos condicionadors integrats](#6-dos-condicionadors-integrats)
3. [Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts](#conversió-impedànciatensió-divisors-inversor-ponts-i-pseudoponts)
   - [1 Divisors de tensió](#1-divisors-de-tensió)
   - [2 La impedància de sortida del divisor passiu](#2-la-impedància-de-sortida-del-divisor-passiu)
   - [3 Amplificador inversor capacitiu](#3-amplificador-inversor-capacitiu)
   - [4 Ponts d'alterna](#4-ponts-dalterna)
   - [5 Pseudoponts d'alterna](#5-pseudoponts-dalterna)
4. [Amplificadors d'alterna i limitacions dels operacionals](#amplificadors-dalterna-i-limitacions-dels-operacionals)
   - [1 La banda que ocupa el senyal](#1-la-banda-que-ocupa-el-senyal)
   - [2 Centrat i amplada de banda](#2-centrat-i-amplada-de-banda)
   - [3 Amplificador d'alterna no inversor](#3-amplificador-dalterna-no-inversor)
   - [4 Amplificador d'instrumentació d'alterna](#4-amplificador-dinstrumentació-dalterna)
   - [5 Limitacions de l'amplificador operacional](#5-limitacions-de-lamplificador-operacional)
5. [Estimació de l'amplitud: mètodes no coherents](#estimació-de-lamplitud-mètodes-no-coherents)
   - [1 Modulació AM i modulació DSB](#1-modulació-am-i-modulació-dsb)
   - [2 Convertidors de valor eficaç](#2-convertidors-de-valor-eficaç)
   - [3 Multiplicadors analògics](#3-multiplicadors-analògics)
   - [4 Detectors de pic o d'envolupant](#4-detectors-de-pic-o-denvolupant)
6. [Detecció coherent: homodina, rectificació síncrona i mostreig síncron](#detecció-coherent-homodina-rectificació-síncrona-i-mostreig-síncron)
   - [1 Principi i avantatges](#1-principi-i-avantatges)
   - [2 Detecció homodina](#2-detecció-homodina)
   - [3 Rectificació síncrona](#3-rectificació-síncrona)
   - [4 Mostreig síncron i sub-mostreig](#4-mostreig-síncron-i-sub-mostreig)
7. [Mètodes basats en oscil·ladors i mesura de freqüència](#mètodes-basats-en-oscilladors-i-mesura-de-freqüència)
   - [1 Codificar el mesurand en la freqüència](#1-codificar-el-mesurand-en-la-freqüència)
   - [2 Oscil·ladors de relaxació](#2-oscilladors-de-relaxació)
   - [3 Conversió freqüència–tensió](#3-conversió-freqüènciatensió)
   - [4 Comptatge digital de flancs](#4-comptatge-digital-de-flancs)
8. [Entrenament V/F · Unitat 8: Unitat 8](#entrenament-vf-unitat-8-unitat-8)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_Unitat8_Index -->

# Unitat 8 — Condicionament de sensors en alterna · Lectura prèvia

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 8 — Condicionament de sensors en alterna

Materials de lectura prèvia · dedicació total estimada: 61 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents contenen tot el que cal per preparar la unitat.

Llegeix els sis documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor.

### [1. Sensors reactius, freqüència de treball i cadena de condicionament](#sensors-reactius-freqüència-de-treball-i-cadena-de-condicionament)

El model d'impedància complexa Z(f,x)=R+jX i la condició que fa que un sensor es pugui tractar com a reactiu. Com es tria la freqüència de treball: el que hi imposa el sensor —nucli ferromagnètic, corrents de Foucault, capacitiu— i el que hi imposa el sistema, allunyar-se de la xarxa i del soroll 1/f. Les dues aproximacions al condicionament, la lineal i la basada en oscil·ladors. Els quatre blocs de la cadena lineal i la funció de cadascun. Els quatre models canònics de sensor. Dos condicionadors integrats comercials com a il·lustració de les dues aproximacions.

*⏱️ Dedicació estimada: 10 min*

### [2. Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts](#conversió-impedànciatensió-divisors-inversor-ponts-i-pseudoponts)

El divisor d'impedàncies i quan la freqüència s'hi cancel·la. La no linealitat del divisor amb un sol sensor i la linealitat exacta del divisor diferencial, amb el seu rebuig de mode comú. El problema de la impedància de sortida del divisor passiu i les seves mitigacions, de l'apantallament a l'amplificador operacional. L'amplificador inversor capacitiu, la resistència de polarització i les seves dues condicions contraposades, i on col·locar el sensor. El pont d'alterna: homogeneïtat de branques, condició d'equilibri, sortida amb sensor diferencial i impedància de sortida. El pseudopont i els seus dos avantatges.

*⏱️ Dedicació estimada: 9 min*

### [3. Amplificadors d'alterna i limitacions dels operacionals](#amplificadors-dalterna-i-limitacions-dels-operacionals)

Per què l'amplificació ha de ser passa-banda: supressió dels errors de contínua, reducció del soroll 1/f i rebuig de la xarxa. La banda que ocupa el senyal modulat i la condició de guany pla als seus extrems. Centrat per mitjana geomètrica i el compromís d'amplada de banda entre error de guany i rebuig de soroll. Les dues topologies —no inversora i d'instrumentació— amb l'anàlisi en tres règims i les freqüències de tall. Les quatre limitacions de l'operacional a la freqüència de treball: GBW, slew rate, capacitat d'entrada i de les pistes, i degradació de CMRR i PSRR, amb el desacoblament de l'alimentació.

*⏱️ Dedicació estimada: 12 min*

### [4. Estimació de l'amplitud: mètodes no coherents](#estimació-de-lamplitud-mètodes-no-coherents)

Modulació AM clàssica davant de modulació DSB i què determina quines tècniques són admissibles. Els convertidors de valor eficaç: tèrmics, de càlcul explícit i implícit, i per rectificació amb el seu factor de forma, comparats en exactitud, amplada de banda, velocitat i cost. Per què tot mètode no coherent introdueix un biaix positiu davant del soroll i les interferències. Els multiplicadors analògics i els seus quadrants, les implementacions amb amplificadors logarítmics i antilogarítmics i la cèl·lula de Gilbert. Els detectors de pic: arrissat, criteri de la constant de temps i sensibilitat al soroll impulsiu.

*⏱️ Dedicació estimada: 12 min*

### [5. Detecció coherent: homodina, rectificació síncrona i mostreig síncron](#detecció-coherent-homodina-rectificació-síncrona-i-mostreig-síncron)

Què aporta la referència de fase: recuperació del signe en DSB, rebuig de la quadratura i reducció del soroll. La detecció homodina, el terme a 2f0 que el filtre elimina i la interpretació de la sortida en funció del desfasament. La tria de la freqüència de tall, l'atenuació d'una interferència i la reducció de soroll respecte de l'amplada de banda de l'amplificador. La rectificació síncrona amb referència quadrada i commutador, i el preu dels seus harmònics imparells. El mostreig síncron: què elimina cada combinació de mostres, per què la taxa la fixa el mesurand i no la portadora, i la validesa del sub-mostreig.

*⏱️ Dedicació estimada: 10 min*

### [6. Mètodes basats en oscil·ladors i mesura de freqüència](#mètodes-basats-en-oscilladors-i-mesura-de-freqüència)

Codificar el mesurand en la freqüència: senzillesa, sortida digital directa i immunitat a les pertorbacions d'amplitud, davant de la no linealitat, la deriva dels components i el temps d'integració. Els tres oscil·ladors de relaxació —555 astable, amplificador operacional amb histèresi i inversors CMOS de Schmitt— amb les seves expressions i el seu cicle de treball. La conversió freqüència–tensió amb monoestable i la condició sobre la durada del pols. El comptatge digital de flancs, la resolució 1/Tgate i el compromís amb la velocitat de resposta.

*⏱️ Dedicació estimada: 8 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

<!-- FIN CAPÍTULO: 00_Unitat8_Index -->

---

<!-- INICIO CAPÍTULO: 01_Unitat8_Sensors_reactius_i_cadena_de_condicionament -->

# Sensors reactius, freqüència de treball i cadena de condicionament

Sistemes de Mesura · **Unitat 8 — Condicionament de sensors en alterna** · Document 1 de 6

# Sensors reactius, freqüència de treball i cadena de condicionament

Dedicació estimada: 10 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Escriure el model d'impedància complexa d'un sensor reactiu i la condició que el fa tractable com a tal.
> - Justificar l'elecció de la freqüència de treball  $f_0$  a partir del sensor, de les interferències i del soroll  $\frac{1}{f}$.
> - Distingir les dues aproximacions al condicionament en alterna: la lineal i la basada en oscil·ladors.
> - Enumerar els blocs de la cadena de condicionament lineal i la funció de cadascun.
> - Associar cada model canònic de sensor reactiu a la forma en què la seva impedància varia amb el mesurand.

A la unitat 6 s'ha tractat el condicionament de sensors resistius, que treballa en contínua. Els sensors reactius de la unitat 7 —capacitius i inductius— codifiquen el mesurand en la **part imaginària** d'una impedància, i això obliga a excitar-los amb un senyal sinusoïdal i a processar-ne la resposta en alterna. Aquesta unitat tracta l'electrònica que ho fa.

## 1 El sensor reactiu com a impedància complexa

Qualsevol sensor que requereixi condicionament en alterna es modela, en primera aproximació, com una impedància complexa que depèn de la freqüència  $f$  i del mesurand  $x$:

$$
Z(f,x) = R(f,x) + j\,X(f,x) \qquad (8.1)
$$

Un sensor capacitiu ideal tindria  $R=0$  i  $X = -1/(2\pi f C(x))$; un sensor inductiu ideal,  $R=0$  i  $X = 2\pi f L(x)$. Cap sensor real no és purament reactiu: la resistència del fil de coure en els inductius i les pèrdues del dielèctric en els capacitius aporten sempre una part real.

La condició per considerar-lo **reactiu** en sentit estricte és que, a la freqüència de treball, els canvis relatius que el mesurand indueix sobre la part imaginària dominin sobre els que indueix sobre la part real:

$$
\frac{|\Delta X_f(x)|}{|X_0|} \gg \frac{|\Delta R_f(x)|}{|R_0|} \qquad (8.2)
$$

A la pràctica s'accepta el model si  $|R_0| \ll |X_0|$  a la freqüència escollida. Quan es compleix, la part real produeix errors petits que alguns mètodes de condicionament poden corregir o rebutjar.

La freqüència ajuda a complir-ho, però de manera diferent segons el tipus de sensor. En un sensor inductiu,  $X = 2\pi f L(x)$  creix linealment amb la freqüència mentre la resistència del bobinatge es manté, de manera que pujar en freqüència afavoreix la condició. En un sensor capacitiu amb pèrdues, modelat com la capacitat  $C$  en paral·lel amb la resistència del dielèctric  $R_d$:

$$
Z_\mathrm{cap}(f,x) = \frac{R_d}{1 + j\,2\pi f R_d C(x)} \qquad (8.3)
$$

En pujar la freqüència, la part real d'aquesta impedància decreix com l'invers del *quadrat* de la freqüència i la part imaginària com l'invers de la freqüència. Existeix, doncs, per a cada sensor capacitiu, un interval de freqüències on la condició de sensor reactiu es compleix acceptablement.

## 2 La freqüència de treball

La tria de  $f_0$  respon a criteris del sensor i a criteris del sistema, que actuen simultàniament.

| Tipus de sensor | Rang i motiu |
|:--- |:--- |
| **Inductiu amb nucli ferromagnètic** | Com a molt uns pocs kHz. Per damunt d'una certa freqüència, la permeabilitat del nucli disminueix per les pèrdues per histèresi i per corrents de Foucault; aquestes pèrdues modifiquen la part real i converteixen el sensor en majoritàriament resistiu. |
| **Inductiu per corrents de Foucault** | De centenars de kHz a diversos MHz, i fins a desenes o centenars de MHz en sensors de proximitat d'alta resolució. El principi de mesura són els corrents induïts al metall proper, i la seva profunditat de penetració només és prou petita a freqüència elevada. |
| **Capacitiu** | De 10 kHz a 100 MHz per a capacitats d'alguns pF a uns pocs nF. Es busca un mòdul d'impedància entre unes centenes d'ohms i alguns kΩ, que dona alhora prou sensibilitat i prou immunitat a les interferències capacitives. |

| Criteri | Conseqüència sobre  $f_0$ |
|:--- |:--- |
| **Interferències electromagnètiques** | Les fonts dominants —xarxa elèctrica a 50 Hz o 60 Hz, els seus harmònics i els rellotges dels sistemes digitals propers— ocupen bandes ben definides. Triant  $f_0$  allunyada d'aquestes bandes i emprant detecció selectiva en freqüència, la interferència queda molt atenuada. |
| **Soroll  $\frac{1}{f}$  de l'electrònica** | Per sota d'una freqüència característica del dispositiu actiu, el soroll rosa domina sobre el blanc i limita la relació senyal-soroll. Treballant per damunt d'aquesta freqüència, el soroll de l'amplificador és essencialment blanc i, per tant, menor. |

La freqüència de treball ha de ser, doncs, superior al límit inferior que imposa el comportament reactiu del sensor i, alhora, prou elevada per allunyar-se del soroll  $\frac{1}{f}$  i de les interferències de baixa freqüència, sense superar el límit superior del sensor.

## 3 Les dues aproximacions al condicionament

Hi ha dues maneres de convertir la variació d'impedància en una mesura, i el capítol s'estructura al voltant de totes dues.

- **Condicionament lineal.** Un oscil·lador sinusoïdal excita el sensor; un circuit converteix la variació d'impedància en una variació d'amplitud; el senyal s'amplifica selectivament i, finalment, se'n extreu l'amplitud com a tensió contínua. La informació viatja en l'**amplitud**.
- **Mètodes no lineals basats en oscil·ladors.** El sensor s'incorpora dins d'un oscil·lador com a element que en fixa la freqüència. Quan el mesurand canvia, canvia la freqüència d'oscil·lació. La informació viatja en la **freqüència** d'un senyal generalment quadrat, i no cal cap oscil·lador de referència extern.

## 4 La cadena de condicionament lineal

![Cadena de condicionament lineal: un oscil·lador excita el sensor Z(f,x) dins d'un convertidor impedància–tensió; la sortida passa per un amplificador d'alterna i per un convertidor alterna–contínua.](assets/01_Unitat8_Sensors_reactius_i_cadena_de_condicionament_img_1.png)

*Figura: Figura 8.1 Cadena de processament del condicionament lineal de sensors en alterna.*

| Bloc | Funció |
|:--- |:--- |
| **Oscil·lador** | Genera la tensió sinusoïdal d'excitació d'amplitud  $V$  i freqüència  $f_0$, i en els sistemes coherents proporciona també la referència de fase. Fa el paper que en contínua fa l'alimentació d'un pont o d'un divisor: qualsevol deriva de la seva amplitud es transmet directament com un error de mesura, i qualsevol deriva de  $f_0$  altera el valor de la impedància del sensor. Per això convé que porti control automàtic d'amplitud o que sigui de molt alta estabilitat. |
| **Convertidor impedància–tensió** | Circuit —divisor de tensió, pont d'alterna o pseudopont— que combina el sensor amb impedàncies fixes de referència i lliura una tensió sinusoïdal a la mateixa freqüència  $f_0$, l'amplitud de la qual és una funció coneguda i monotònica de  $x$. |
| **Amplificador d'alterna** | Amplificador de característica passa-banda centrada a  $f_0$. S'insereix quan el canvi d'amplitud associat al rang de  $x$  és massa petit per a les etapes posteriors, i amplifica el senyal sense amplificar les interferències ni el soroll de fora de la banda. |
| **Convertidor alterna–contínua** | Extreu l'amplitud del senyal sinusoïdal i la lliura com a tensió contínua. Es divideix en **mètodes no coherents** —convertidors de valor eficaç i detectors de pic, que mesuren l'envolupant sense cap referència de fase— i **mètodes coherents** —detecció homodina, rectificació síncrona i mostreig síncron, que multipliquen el senyal per una referència en fase amb l'oscil·lador i poden així discriminar el signe de  $x$, rebutjar components en quadratura i reduir el soroll. |

Per a l'anàlisi dels circuits de conversió impedància–tensió se suposa que l'oscil·lador és ideal: amplitud  $V$  i freqüència  $f_0$  exactament constants, i impedància de sortida nul·la.

## 5 Models canònics del sensor

Per analitzar els circuits de manera sistemàtica se suposa que el sensor és ideal —impedància purament imaginària— i que la seva reactància depèn del mesurand en una de dues formes canòniques: proporcional o inversament proporcional. El paràmetre  $x$  és normalitzat, de manera que  $x=0$  és la situació de referència i sovint  $|x| \ll 1$.

| Model | Element | Impedància | Origen físic |
|:--- |:--- |:--- |:--- |
| **a** | $C_s = C_0(1+x)$ | $Z_s = \frac{1}{j\omega C_0(1+x)}$ | Variació de la constant dielèctrica del material entre plaques o de l'àrea efectiva. El mòdul de la impedància varia com  $\frac{1}{1+x}$. |
| **b** | $C_s = C_0/(1+x)$ | $Z_s = \frac{1+x}{j\omega C_0}$ | Sensors capacitius de distància per variació de la separació entre plaques. El mòdul de la impedància varia linealment amb  $x$. |
| **c** | $L_s = L_0(1+x)$ | $Z_s = j\omega L_0(1+x)$ | El mesurand modifica la permeabilitat del circuit magnètic, el nombre d'enrotllaments efectius o la geometria de la bobina. El mòdul varia linealment amb  $x$. |
| **d** | $L_s = L_0/(1+x)$ | $Z_s = \frac{j\omega L_0}{1+x}$ | Proximitat per corrents de Foucault: l'apropament d'un conductor redueix l'autoinductància de la bobina. El mòdul varia com  $\frac{1}{1+x}$. |

El model determina l'estructura del circuit de conversió. Si la impedància del sensor varia de manera inversament proporcional a  $x$, se solen emprar ponts o pseudoponts per obtenir una sortida lineal; si varia de manera proporcional, un divisor de tensió o un amplificador inversor pot ser suficient.

## 6 Dos condicionadors integrats

És habitual trobar sensors reactius comercialitzats amb l'electrònica de condicionament ja integrada al mateix encapsulat, amb sortida analògica estandarditzada o digital. Aquests **sensors integrats** amaguen la complexitat del condicionament darrere d'una interfície senzilla, però conèixer-ne els principis interns continua essent necessari per triar el sensor adequat, seleccionar-ne els components externs, interpretar-ne les especificacions i diagnosticar problemes. Dos circuits de Texas Instruments il·lustren les dues aproximacions.

![Diagrama de blocs del front end analògic d'un canal del LDC5071-Q1: correcció de mode comú, protecció ESD, filtre passa-banda, bloc de desmodulació, filtre passa-baixes amb guany, control automàtic de guany i driver de sortida.](assets/01_Unitat8_Sensors_reactius_i_cadena_de_condicionament_img_2.png)

*Figura: Figura 8.2 Front end analògic de cada canal del LDC5071-Q1.*

El **LDC5071-Q1** condiciona sensors de rotació per inducció magnètica —un transformador amb el primari en un rotor i dos secundaris a 90°— i implementa el **condicionament lineal**. Un oscil·lador LC intern excita el primari i serveix alhora de referència, de manera que la fase de referència és sempre coherent amb l'excitació: el circuit és un detector homodí de dos canals. Cada canal filtra el senyal amb un passa-banda centrat a la freqüència de treball, el desmodula multiplicant-lo per la referència, en filtra el resultat amb un passa-baixes amb guany —la freqüència de tall del qual fixa l'amplada de banda i el soroll de la mesura— i el normalitza amb un control automàtic de guany, perquè el càlcul de l'angle sigui robust davant de variacions de la distància entre el rotor i el sensor. El microcontrolador posterior obté l'angle absolut aplicant un arctangent al quocient dels dos canals.

![Connexió del FDC2114 amb quatre sensors capacitius, cadascun en sèrie amb una bobina formant un circuit ressonant LC, rellotge de referència extern i bus I²C cap al microcontrolador.](assets/01_Unitat8_Sensors_reactius_i_cadena_de_condicionament_img_3.png)

*Figura: Figura 8.3 Connexió del FDC2114 amb quatre sensors capacitius.*

El **FDC2114** és un convertidor de capacitat a dades digitals de quatre canals i empra el **mètode basat en freqüència**. Cada sensor capacitiu es munta en sèrie amb una bobina i forma un circuit ressonant de freqüència

$$
f_\mathrm{res} = \frac{1}{2\pi\sqrt{L\,C_s(x)}} \qquad (8.4)
$$

que el circuit mesura comparant-la amb un rellotge de referència extern o amb un oscil·lador intern, i lliura el resultat pel bus I²C. Perquè la mesura sigui correcta la bobina ha de ser de valor conegut i estable i el factor  $Q$  del ressonant prou elevat perquè la freqüència de ressonància quedi ben definida; amb  $Q$  baix la ressonància s'esmorteeix i la mesura perd precisió.

> [!TIP] **Síntesi**
>
> Un sensor reactiu es modela com  $Z(f,x) = R + jX$  i es tracta com a tal quan els canvis relatius de la part imaginària dominen sobre els de la part real a la freqüència de treball. La tria de  $f_0$  combina el que permet el sensor —pocs kHz amb nucli ferromagnètic, centenars de kHz a MHz per corrents de Foucault, de 10 kHz a 100 MHz en capacitius— amb el que exigeix el sistema: allunyar-se de la xarxa i dels seus harmònics i situar-se per damunt del soroll  $\frac{1}{f}$. Hi ha dues aproximacions: la lineal, que codifica el mesurand en l'amplitud i encadena oscil·lador, convertidor impedància–tensió, amplificador d'alterna i convertidor alterna–contínua; i la basada en oscil·ladors, que el codifica en la freqüència. Els quatre models canònics de sensor —capacitiu i inductiu, proporcional i inversament proporcional a  $1+x$ — determinen quin circuit de conversió dona una sortida lineal.

[2. Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts →](#conversió-impedànciatensió-divisors-inversor-ponts-i-pseudoponts)

---

<!-- FIN CAPÍTULO: 01_Unitat8_Sensors_reactius_i_cadena_de_condicionament -->

---

<!-- INICIO CAPÍTULO: 02_Unitat8_Conversio_impedancia_tensio -->

# Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts

Sistemes de Mesura · **Unitat 8 — Condicionament de sensors en alterna** · Document 2 de 6

# Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts

Dedicació estimada: 9 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Calcular la sortida d'un divisor d'impedàncies i reconèixer quan la freqüència s'hi cancel·la.
> - Explicar per què el divisor capacitiu passiu té una impedància de sortida problemàtica i com es resol.
> - Dimensionar la resistència de polarització d'un amplificador inversor capacitiu a partir de les seves dues condicions.
> - Escriure la condició d'equilibri d'un pont d'alterna i obtenir-ne la tensió diferencial.
> - Justificar els dos avantatges del pseudopont respecte al pont passiu.

El convertidor impedància–tensió és el primer bloc de la cadena lineal: ha de generar un senyal sinusoïdal a  $f_0$  l'amplitud del qual sigui una funció coneguda i monotònica del mesurand. Les quatre topologies d'aquest document són el divisor, l'amplificador inversor, el pont i els pseudoponts, amb les resistències substituïdes per impedàncies avaluades a la freqüència de treball.

## 1 Divisors de tensió

Un oscil·lador d'amplitud  $V$  i freqüència  $f_0$  alimenta la sèrie de dues impedàncies. La tensió als borns de  $Z_2$, connectada entre la sortida i massa, és

$$
V_o = V\,\frac{Z_2}{Z_1+Z_2} \qquad (8.5)
$$

Quan les dues impedàncies són del **mateix tipus** —les dues capacitives, les dues inductives o les dues resistives— el factor  $j\omega$  es cancel·la en el quocient. Amb  $Z_1 = \frac{1}{j\omega C_1}$  i  $Z_2 = \frac{1}{j\omega C_2}$  la relació d'amplituds és simplement  $C_1/(C_1+C_2)$, independent de  $f_0$: el divisor és un sistema d'ordre zero.

![Divisor de tensió format per un sensor capacitiu de model Cs = C0/(1+x) en sèrie amb un condensador fix de valor C0, excitat per un oscil·lador sinusoïdal.](assets/02_Unitat8_Conversio_impedancia_tensio_img_1.png)

*Figura: Figura 8.4 Divisor de tensió amb un sensor capacitiu de model $C_s = C_0/(1+x)$ i un condensador fix.*

Amb el sensor  $C_s = C_0/(1+x)$  en sèrie amb un condensador de referència  $C = C_0$, la tensió als borns del sensor és

$$
V_o = V\,\frac{1+x}{2+x} \qquad (8.6)
$$

La relació no és lineal, perquè el denominador és  $2+x$  i no una constant. Per a variacions petites la resposta s'aproxima a lineal, però per a sensors amb rang ampli l'error de no linealitat pot ser significatiu. Amb  $C = C_0$, la sensibilitat a l'origen val  $dV_o/dx|_{x=0} = V/4$.

![Divisor de tensió format per les dues capacitats d'un sensor capacitiu diferencial, que varien de manera complementària amb el mesurand.](assets/02_Unitat8_Conversio_impedancia_tensio_img_2.png)

*Figura: Figura 8.5 Divisor de tensió amb un sensor capacitiu diferencial.*

Un **sensor capacitiu diferencial** —dues plaques fixes i una placa mòbil entre elles— es modela amb  $C_{s1} = C_0/(1+x)$  i  $C_{s2} = C_0/(1-x)$. Cancel·lant factors:

$$
V_o = V\,\frac{1+x}{2} \qquad (8.7)
$$

La sortida és estrictament lineal amb  $x$, sigui quina sigui la magnitud del canvi, amb constant de proporcionalitat  $V/2$. A més, qualsevol pertorbació que afecti igualment les dues capacitats —per exemple una variació de temperatura que canviï  $C_0$  però deixi  $x$  constant— es cancel·la en el quocient. Aquesta supressió del mode comú és anàloga a la dels ponts de Wheatstone resistius.

## 2 La impedància de sortida del divisor passiu

L'equivalent de Thévenin al node de sortida té com a impedància el paral·lel de les dues capacitats. Per a  $x=0$, totes dues valen  $C_0$:

$$
|Z_\mathrm{out}| = \frac{1}{\omega \cdot 2C_0} \qquad (8.8)
$$

Amb  $C_0 = 100$  pF i a la freqüència de la xarxa, el mòdul és d'uns 16 MΩ. Un node amb aquesta impedància és extremament vulnerable a l'acoblament capacitiu de qualsevol senyal elèctric de l'entorn —cablejat de la xarxa, cables de dades, motors—, i la interferència pot arribar a tenir una amplitud comparable o superior a la del senyal útil.

Les mitigacions passives són el **cable coaxial apantallat** entre el divisor i l'etapa següent, amb la pantalla connectada a massa o a una tensió de guarda, la **proximitat** entre sensor i electrònica, i el **pla de massa** envoltant les pistes que transporten el senyal. Redueixen el problema però no l'eliminen. La solució de fons és intercalar un **amplificador operacional**: gràcies a la realimentació negativa, la seva impedància de sortida és de pocs mil·liohms, cosa que fa el node pràcticament insensible a les interferències capacitives i elimina els efectes de càrrega de les etapes posteriors.

## 3 Amplificador inversor capacitiu

![Amplificador operacional en configuració inversora amb un condensador C1 com a impedància d'entrada i un condensador C2 en realimentació; un dels dos és el sensor.](assets/02_Unitat8_Conversio_impedancia_tensio_img_3.png)

*Figura: Figura 8.6 Amplificador inversor per al condicionament de sensors capacitius.*

És l'amplificador inversor clàssic amb dos condensadors en lloc de dues resistències:  $C_1$  fa d'impedància d'entrada i  $C_2$  d'impedància de realimentació, i un dels dos és el sensor.

Els condensadors bloquegen la contínua, de manera que els corrents de polarització del terminal inversor no tenen camí per circular i acabarien carregant els condensadors fins a saturar l'amplificador. S'hi afegeix per això una **resistència de polarització**  $R_p$  en paral·lel amb  $C_2$, que els proporciona el camí de contínua. La funció de transferència resultant és

$$
H(j\omega) = -\,\frac{j\omega R_p C_1}{1 + j\omega R_p C_2} \qquad (8.9)
$$

A la freqüència de treball, si la impedància de  $R_p$  és molt més gran que la de  $C_2$, el denominador queda dominat pel terme imaginari i la resposta s'aproxima al quocient de capacitats,  $H(j\omega_0) \approx -C_1/C_2$, de manera que  $|V_o| = V\,C_1/C_2$. La condició de disseny és

$$
R_p \gg \frac{1}{2\pi f_0 C_2} \qquad (8.10)
$$

i a la pràctica es recomana  $R_p \geq 10/(2\pi f_0 C_2)$  —impedància deu vegades la de  $C_2$  a  $f_0$ — per mantenir l'error relatiu de l'amplitud de sortida per sota del 0,5 %.

Alhora, els corrents de polarització i d'offset circulen per  $R_p$  i generen a la sortida una tensió contínua de valor  $R_p(I_B + I_{\text{OS}}/2)$, que ocupa part del rang lineal de l'amplificador. Cal, doncs, que

$$
V_\mathrm{sat} - V_{o,\max} > R_p\left(\frac{I_B + I_{\text{OS}}}{2}\right) \qquad (8.11)
$$

on  $V_{o,\max}$  és la màxima amplitud de pic del senyal altern de sortida. Les dues condicions es contraposen: la primera demana  $R_p$  gran i la segona  $R_p$  petita. Amb amplificadors d'entrada FET, de corrents de polarització molt baixos, la restricció es relaxa i es pot triar  $R_p$  molt gran, cosa especialment convenient a freqüències de treball baixes, on  $\frac{1}{2\pi f_0 C_2}$  ja és elevat.

La posició del sensor la fixa la forma funcional de la seva capacitat. Si  $C_s = C_0(1+x)$  se situa a  $C_1$  i llavors  $|V_o| = V C_0(1+x)/C_2$. Si  $C_s = C_0/(1+x)$  se situa a  $C_2$  i llavors  $|V_o| = V C_1(1+x)/C_0$. En tots dos casos l'amplitud de sortida és lineal amb  $x$  i la impedància de sortida és molt baixa.

## 4 Ponts d'alterna

Quan la variació del sensor és petita,  $x \ll 1$, la variació de tensió d'un divisor o d'un inversor és minúscula comparada amb el valor que ja hi ha per a  $x=0$. La solució clàssica és el pont, equivalent en alterna del pont de Wheatstone.

![Estructura general d'un pont d'alterna: quatre impedàncies en quadrilàter, excitació sinusoïdal per dos nodes oposats i sortida diferencial entre els altres dos.](assets/02_Unitat8_Conversio_impedancia_tensio_img_4.png)

*Figura: Figura 8.7 Estructura general d'un pont d'alterna.*

L'oscil·lador alimenta dos nodes oposats i la sortida es pren entre els dos restants:

$$
V_\mathrm{diff} = V\left(\frac{Z_2}{Z_1+Z_2} - \frac{Z_4}{Z_3+Z_4}\right) \qquad (8.12)
$$

Perquè la freqüència es cancel·li en cada quocient,  $Z_1$  i  $Z_2$  han de ser del mateix tipus d'impedància, i el mateix  $Z_3$  i  $Z_4$. Les dues branques poden ser de tipus diferent entre elles —una resistiva i l'altra inductiva, per exemple—; el que importa és la homogeneïtat dins de cada branca. Per conveni, el pont es dissenya perquè la sortida sigui nul·la a la situació de referència:

$$
\left.\frac{Z_2}{Z_1}\right|_{x=0} = \left.\frac{Z_4}{Z_3}\right|_{x=0} \qquad (8.13)
$$

![Pont d'alterna per al condicionament d'una LVDT: les dues inductàncies del sensor formen una branca i dues resistències iguals la branca de referència.](assets/02_Unitat8_Conversio_impedancia_tensio_img_5.png)

*Figura: Figura 8.8 Pont d'alterna per al condicionament d'una LVDT.*

Amb un sensor inductiu diferencial — $L_1 = L_0(1-x)$  i  $L_2 = L_0(1+x)$, el cas de la LVDT de la unitat 7— i dues resistències de referència iguals:

$$
V_\mathrm{diff} = V\left(\frac{1+x}{2} - \frac{1}{2}\right) = V\,\frac{x}{2} \qquad (8.14)
$$

La sortida és estrictament lineal amb  $x$, independent de la freqüència i nul·la per a  $x=0$, amb sensibilitat  $|dV_\mathrm{diff}/dx| = V/2$.

El pont passiu arrossega el mateix problema que el divisor. La impedància de sortida diferencial per a  $x=0$  és la sèrie dels dos paral·lels de cada branca:

$$
Z_\mathrm{out} = \frac{j\omega L_0}{2} + \frac{R}{2} \qquad (8.15)
$$

A les freqüències de treball habituals la part inductiva pot ser prou gran per causar errors de càrrega quan s'hi connecta l'amplificador d'instrumentació posterior, i la impedància elevada torna a fer el circuit vulnerable a interferències si els cables no estan apantallats.

## 5 Pseudoponts d'alterna

El pseudopont incorpora amplificadors operacionals al pont i en resol els dos problemes: la sortida es pren als terminals de sortida dels operacionals, de manera que la impedància de sortida és de l'ordre de mΩ en la banda de pas. Té a més un segon avantatge: en basar-se molts en la configuració inversora, la **tensió de mode comú** a l'entrada de l'operacional és nul·la o molt petita, cosa que redueix els errors deguts al CMRR finit a alta freqüència.

![Pseudopont d'alterna amb un amplificador operacional en configuració inversora: Z1 i Z2 en el camí inversor, Z3 i Z4 formant un divisor cap al terminal no inversor.](assets/02_Unitat8_Conversio_impedancia_tensio_img_6.png)

*Figura: Figura 8.9 Pseudopont d'alterna amb sortida unipolar.*

La tensió al terminal no inversor surt del divisor  $Z_3$ – $Z_4$, i, pel curtcircuit virtual, el corrent que circula per  $Z_1$  és el mateix que circula per  $Z_2$. Combinant totes dues coses:

$$
V_o = \frac{V}{Z_1}\cdot\frac{Z_3 Z_1 - Z_4 Z_2}{Z_3+Z_4} \qquad (8.16)
$$

La condició de sortida nul·la a  $x=0$  és, doncs,

$$
Z_3 Z_1 = Z_4 Z_2 \Leftrightarrow \left.\frac{Z_4}{Z_3}\right|_{x=0} = \left.\frac{Z_1}{Z_2}\right|_{x=0} \qquad (8.17)
$$

Amb  $Z_2$  el sensor de model  $C_s = C_0/(1-x)$,  $Z_1$  un condensador fix de valor  $C_0$  i  $Z_3 = Z_4 = R$, la tensió al terminal no inversor val  $V/2$  i la sortida resulta  $V_o = (V/2)\,x$: lineal amb  $x$, nul·la a l'origen i de baixa impedància.

![Pseudopont d'alterna amb sortida diferencial: dos amplificadors operacionals generen Vo+ i Vo− a partir de les quatre impedàncies.](assets/02_Unitat8_Conversio_impedancia_tensio_img_7.png)

*Figura: Figura 8.10 Pseudopont d'alterna amb sortida diferencial.*

Quan la sortida ha de ser diferencial —per connectar-la a un amplificador d'instrumentació d'alterna— s'empren dos operacionals que generen  $V_{o+}$  i  $V_{o-}$, i es pren  $V_\mathrm{diff} = V_{o+} - V_{o-}$. Amb  $Z_2 = (1-x)/(j\omega C_2)$,  $Z_1 = \frac{1}{j\omega C_1}$,  $Z_3 = R_3$  i  $Z_4 = R_4$, amb la condició d'equilibri  $R_3/R_4 = C_1/C_2$, la sortida diferencial és  $V_\mathrm{diff} = V\,x$: lineal, nul·la a l'origen i de baixa impedància en tots dos pins.

> [!TIP] **Síntesi**
>
> El divisor d'impedàncies té la mateixa estructura formal que el resistiu i esdevé d'ordre zero quan les dues impedàncies són del mateix tipus, perquè la freqüència s'hi cancel·la. Amb un sol sensor la resposta és no lineal — $V(1+x)/(2+x)$ — i amb un sensor diferencial és estrictament lineal,  $V(1+x)/2$, amb rebuig de les pertorbacions comunes. El seu punt feble és la impedància de sortida, de l'ordre de megaohms amb capacitats petites, que es resol amb un amplificador operacional. L'amplificador inversor capacitiu dona  $-C_1/C_2$  a  $f_0$  sempre que la resistència de polarització presenti una impedància molt superior a la de  $C_2$, i el seu valor queda acotat per dalt per la tensió contínua que hi generen els corrents de polarització. El pont d'alterna exigeix impedàncies del mateix tipus dins de cada branca, s'equilibra perquè la sortida sigui nul·la a  $x=0$  i dona  $V x/2$  amb un sensor diferencial, però conserva una impedància de sortida elevada. El pseudopont hi afegeix operacionals: impedància de sortida de mil·liohms i tensió de mode comú petita a l'entrada.

[← 1. Sensors reactius, freqüència de treball i cadena de condicionament](#sensors-reactius-freqüència-de-treball-i-cadena-de-condicionament)[3. Amplificadors d'alterna i limitacions dels operacionals →](#amplificadors-dalterna-i-limitacions-dels-operacionals)

---

<!-- FIN CAPÍTULO: 02_Unitat8_Conversio_impedancia_tensio -->

---

<!-- INICIO CAPÍTULO: 03_Unitat8_Amplificadors_d_alterna -->

# Amplificadors d'alterna i limitacions dels operacionals

Sistemes de Mesura · **Unitat 8 — Condicionament de sensors en alterna** · Document 3 de 6

# Amplificadors d'alterna i limitacions dels operacionals

Dedicació estimada: 12 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Justificar per què l'amplificació del senyal de mesura ha de ser passa-banda i no de banda ampla.
> - Determinar la banda que ocupa el senyal modulat a partir de la dinàmica del mesurand.
> - Aplicar la condició de centrat per mitjana geomètrica i el compromís d'amplada de banda.
> - Relacionar cada condensador de les dues topologies amb la freqüència de tall que fixa.
> - Comprovar si un amplificador operacional concret és adequat quant a GBW, slew rate, capacitat d'entrada i CMRR/PSRR a  $f_0$.

El canvi d'amplitud que el rang complet del mesurand produeix a la sortida del convertidor impedància–tensió pot ser en alguns casos de mil·livolts o fins i tot de microvolts, mentre que la conversió alterna–contínua i la digitalització posteriors demanen senyals de l'ordre de volts. Cal amplificar, però no de qualsevol manera: un amplificador de contínua o de banda ampla amplificaria per igual el senyal, el soroll  $\frac{1}{f}$  i la interferència de xarxa. La solució és un amplificador de característica **passa-banda** centrada a  $f_0$.

![Mòdul de la resposta freqüencial en dB, normalitzat pel guany màxim, d'un amplificador d'alterna: passa-banda amb guany màxim al voltant de f0 i caiguda cap a totes dues bandes.](assets/03_Unitat8_Amplificadors_d_alterna_img_1.png)

*Figura: Figura 8.11 Mòdul de la resposta freqüencial d'un amplificador d'alterna, normalitzat pel guany màxim.*

| Avantatge | Origen |
|:--- |:--- |
| **Supressió dels errors de contínua** | L'offset de tensió i els corrents de polarització de l'operacional generen una tensió contínua a la sortida que pot ser comparable o superior al senyal útil. En la configuració passa-banda la contínua queda fortament atenuada i aquests errors no s'amplifiquen. |
| **Reducció del soroll  $\frac{1}{f}$** | La densitat espectral del soroll rosa creix en baixar la freqüència. Com més elevada és  $f_0$, menor és el soroll  $\frac{1}{f}$  dins de la banda amplificada. |
| **Rebuig de la xarxa** | Com més gran és la distància entre 50 Hz i  $f_0$, més atenuació rep la interferència de la xarxa. |

## 1 La banda que ocupa el senyal

![Tres traces temporals: el mesurand a recuperar, el senyal de l'oscil·lador i la sortida del convertidor impedància–tensió, que és una portadora d'amplitud modulada pel mesurand.](assets/03_Unitat8_Amplificadors_d_alterna_img_2.png)

*Figura: Figura 8.12 Mesurand, senyal de l'oscil·lador i sortida del convertidor impedància–tensió, que és l'entrada de l'amplificador d'alterna.*

![Espectre d'un senyal modulat en amplitud: una ratlla a la freqüència de la portadora i dues bandes laterals simètriques separades per la freqüència del modulador.](assets/03_Unitat8_Amplificadors_d_alterna_img_3.png)

*Figura: Figura 8.13 Espectre d'un senyal modulat en amplitud amb portadora a $C$ i modulador a $M$.*

La sortida del convertidor impedància–tensió és un senyal modulat en amplitud. Si el mesurand no és constant, l'espectre ja no és una ratlla a  $f_0$: s'expandeix al seu voltant. Amb un mesurand sinusoïdal de freqüència  $f_m$  apareixen tres components —la portadora a  $f_0$  i les dues bandes laterals a  $f_0 \pm f_m$ —; en el cas general, amb un mesurand d'espectre estès fins a  $f_{m,\max}$, el senyal modulat ocupa

$$
f_{\min} = f_0 - f_{m,\max}, \qquad f_{\max} = f_0 + f_{m,\max} \qquad (8.18)
$$

Perquè el mesurand es pugui recuperar sense distorsió, el guany ha de ser essencialment constant en tota aquesta banda. Si  $\delta$  és la màxima variació relativa admissible respecte al guany màxim  $G$:

$$
|H(f_{\min})| \geq G(1-\delta), \qquad |H(f_{\max})| \geq G(1-\delta) \qquad (8.19)
$$

Els extrems de l'espectre **no coincideixen** amb les freqüències de tall a −3 dB:  $f_{-3\mathrm{dB},\min}$  i  $f_{-3\mathrm{dB},\max}$  s'han de situar molt per sota i molt per sobre de  $f_{\min}$  i  $f_{\max}$. Com més petit sigui  $\delta$  i menor l'ordre dels filtres, més gran ha de ser aquesta separació.

## 2 Centrat i amplada de banda

El criteri estàndard per centrar la característica a la freqüència de treball és fer coincidir  $f_0$  amb la **mitjana geomètrica** de les dues freqüències de tall:

$$
f_0 = \sqrt{f_{-3\mathrm{dB},\min}\cdot f_{-3\mathrm{dB},\max}} \qquad (8.20)
$$

La condició és en escala logarítmica:  $f_0$  equidista de totes dues en logaritmes, no en escala lineal. Amb talls a 10 Hz i 30 kHz, la freqüència de treball òptima és de 548 Hz; la mitjana aritmètica hauria donat 15 kHz, molt lluny del màxim real de la característica.

L'amplada de banda fixa alhora dos paràmetres en conflicte. Una banda més **ampla** allunya els extrems de l'espectre de les freqüències de tall i, per tant, redueix l'error de guany; però eixampla la banda equivalent de soroll i atenua menys les interferències. Una banda més **estreta** fa el contrari: millora el rebuig de soroll i introdueix un error de guany als extrems que es percep com un error sistemàtic dependent de la freqüència del mesurand. El compromís és triar l'amplada mínima que garanteixi l'error de guany admissible:

$$
BW = f_{-3\mathrm{dB},\max} - f_{-3\mathrm{dB},\min} \geq 2\,k\,f_{m,\max} \qquad (8.21)
$$

amb  $k>1$, tant més gran com menor es vulgui l'error de guany.

## 3 Amplificador d'alterna no inversor

![Amplificador no inversor amb un condensador C1 en sèrie amb R1 cap a massa i un condensador C2 en paral·lel amb la resistència de realimentació R2.](assets/03_Unitat8_Amplificadors_d_alterna_img_4.png)

*Figura: Figura 8.14 Amplificador d'alterna no inversor.*

És la topologia habitual quan la sortida del convertidor impedància–tensió és unipolar referida a massa, com en el divisor o el pseudopont de sortida única. Es construeix sobre l'amplificador no inversor clàssic afegint-hi dos condensadors:  $C_1$  en sèrie amb  $R_1$  i  $C_2$  en paral·lel amb  $R_2$.

| Règim | Comportament dels condensadors | Guany |
|:--- |:--- |:--- |
| **Freqüència molt baixa** | $C_1$  i  $C_2$  són circuits oberts. Amb  $C_1$  obert no circula corrent per  $R_1$  ni per  $R_2$. | Seguidor de tensió, guany 1. Tota tensió contínua a l'entrada es transmet a la sortida amb guany unitari. |
| **Banda de pas ( $f_0$ )** | $C_1$  és curtcircuit davant de  $R_1$;  $C_2$  és circuit obert davant de  $R_2$. | No inversor clàssic,  $G = 1 + R_2/R_1$. |
| **Freqüència molt alta** | $C_2$  curtcircuita  $R_2$  i la realimentació negativa es maximitza. | Seguidor de tensió, guany 1. |

Les freqüències de tall a −3 dB, amb l'operacional suposat ideal, s'obtenen igualant la impedància de cada condensador a la de la resistència que l'acompanya:

$$
f_{-3\mathrm{dB},\min} = \frac{1}{2\pi R_1 C_1}, \qquad f_{-3\mathrm{dB},\max} = \frac{1}{2\pi R_2 C_2} \qquad (8.22)
$$

de manera que la condició de centrat esdevé  $f_0 = \frac{1}{2\pi\sqrt{R_1 C_1 R_2 C_2}}$.

![Resposta freqüencial mesurada de l'amplificador d'alterna no inversor, amb guany unitari a totes dues bandes i guany màxim a la banda de pas.](assets/03_Unitat8_Amplificadors_d_alterna_img_5.png)

*Figura: Figura 8.15 Resposta freqüencial de l'amplificador d'alterna no inversor.*

El procés de disseny parteix de  $G$  i  $f_0$  com a especificacions: es tria  $R_1$, se'n calcula  $R_2 = R_1(G-1)$, s'escullen les dues freqüències de tall que compleixin el centrat amb un error de guany acceptable, i se n'obtenen  $C_1$  i  $C_2$. Finalment se selecciona l'operacional.

## 4 Amplificador d'instrumentació d'alterna

![Amplificador d'instrumentació de tres operacionals amb un condensador C1 en sèrie amb la resistència de guany R1 i dos condensadors C2 en paral·lel amb les dues resistències R2 de la primera etapa.](assets/03_Unitat8_Amplificadors_d_alterna_img_6.png)

*Figura: Figura 8.16 Amplificador d'instrumentació d'alterna.*

Quan la sortida del convertidor impedància–tensió és diferencial —pont d'alterna o pseudopont diferencial— cal aquesta topologia. És un amplificador d'instrumentació de tres operacionals amb tres condensadors a la primera etapa:  $C_1$  en sèrie amb la resistència de guany  $R_1$, i dos condensadors  $C_2$, cadascun en paral·lel amb una de les dues resistències  $R_2$. La segona etapa és un amplificador diferencial de guany fix  $G$, sense modificacions freqüencials.

L'anàlisi en els tres règims és anàloga. A freqüència molt baixa la primera etapa té guany diferencial unitari i el guany total és  $G$. A la banda de pas, amb  $C_1$  en curtcircuit i  $C_2$  obert:

$$
G_\mathrm{total} = \left(1 + \frac{2R_2}{R_1}\right)\cdot G \qquad (8.23)
$$

i a freqüència molt alta  $C_2$  curtcircuita  $R_2$  i el guany torna a ser  $G$. Les freqüències de tall coincideixen formalment amb les del cas no inversor, perquè el tall inferior el fixa  $R_1 C_1$  i el superior  $R_2 C_2$; la condició de centrat és, doncs, idèntica.

![Resposta freqüencial de l'amplificador d'instrumentació d'alterna, de forma passa-banda anàloga a la del no inversor.](assets/03_Unitat8_Amplificadors_d_alterna_img_7.png)

*Figura: Figura 8.17 Resposta freqüencial de l'amplificador d'instrumentació d'alterna.*

L'avantatge principal és l'elevat **rebuig del mode comú**: en ser l'entrada diferencial, qualsevol senyal comú als dos terminals queda atenuat pel CMRR de l'amplificador. La limitació pràctica és que **no es pot implementar amb un amplificador d'instrumentació comercial**: en els integrats de tres terminals, la resistència  $R_1$  és accessible pels pins de guany, però les  $R_2$  són internes i no tenen pins on connectar-hi els  $C_2$. Cal muntar-lo amb operacionals discrets, amb el cost i la superfície de placa que això implica, a canvi de control total sobre els components.

Les dues etapes no tenen els mateixos requisits de producte guany × amplada de banda. La primera ha de complir  $GBW \gg (1+2R_2/R_1)\,f_{-3\mathrm{dB},\max}$  i la segona  $GBW \gg G\,f_{-3\mathrm{dB},\max}$; com que el guany de la segona sol ser el menor, la seva condició és menys restrictiva.

## 5 Limitacions de l'amplificador operacional

A les freqüències de treball del condicionament de sensors reactius —de centenars de Hz a desenes de MHz— quatre limitacions de l'operacional passen a ser determinants.

### Producte guany × amplada de banda

En un operacional de realimentació de tensió, el producte del guany en llaç tancat per la freqüència de tall és pràcticament constant. La condició de disseny és

$$
GBW \gg G\cdot f_{-3\mathrm{dB},\max} \qquad (8.24)
$$

Amb  $G=100$  i  $f_{-3\mathrm{dB},\max} = 20$  kHz cal  $GBW \gg 2$  MHz, de manera que un operacional d'ús general de 3 MHz queda al límit i en calen de 10–20 MHz. Si la condició no es compleix, el tall superior real ja no el fixen  $R_2$  i  $C_2$  sinó el propi operacional, el  $GBW$  del qual varia fins a un factor 2–3 entre mostres del mateix model i amb la temperatura: el tall esdevé poc controlable i el guany en banda de pas queda per sota del dissenyat. Una alternativa són els amplificadors de realimentació de corrent, en què guany i amplada de banda no estan lligats de la mateixa manera, a canvi d'un soroll intrínsec superior.

### Slew rate

El slew rate és el màxim pendent que la sortida pot lliurar. El pendent màxim d'una sinusoide de sortida d'amplitud  $G\,V_{in,\mathrm{pic}}$  es dona al pas per zero, de manera que

$$
SR \geq 2\pi f_0\, G\, V_{in,\mathrm{pic}} \qquad (8.25)
$$

La condició és tant més exigent com majors són el guany, la freqüència de treball i l'amplitud d'entrada: a 1 MHz amb  $G=10$  i 100 mV de pic ja calen 6,3 V/µs, fora de l'abast dels operacionals d'ús general d'1 V/µs. Si el slew rate limita, la sortida s'aproxima a una ona triangular i apareixen harmònics que interfereixen amb la conversió alterna–contínua posterior.

### Impedància d'entrada i capacitats paràsites

La impedància d'entrada no es pot considerar infinita. La seva component capacitiva —d'1 a 10 pF diferencial i d'1 a 20 pF de mode comú en els operacionals típics— domina en pujar la freqüència:

$$
|Z_{\text{in}}(f)| \approx \frac{1}{2\pi f\, C_{\text{in}}} \qquad (8.26)
$$

Aquesta impedància finita forma un divisor amb la impedància de sortida del bloc anterior i introdueix una atenuació dependent de la freqüència i difícil de predir. A més, les pistes del circuit imprès aporten de 0,5 a 5 pF per centímetre: en una pista que transporti un senyal d'alta impedància, 2 pF paràsits ja poden degradar la resposta. Les mitigacions són minimitzar la longitud de les pistes d'alta impedància, envoltar-les de pla de massa o de guarda, i triar encapsulats de baixa capacitat entre pins.

### CMRR i PSRR a la freqüència de treball

![Corba del CMRR d'un amplificador operacional en funció de la freqüència: valor elevat a baixa freqüència i caiguda progressiva a partir d'una freqüència de cantonada baixa.](assets/03_Unitat8_Amplificadors_d_alterna_img_8.png)

*Figura: Figura 8.18 Variació del CMRR amb la freqüència en un amplificador operacional real.*

![Corba del PSRR per a l'alimentació positiva d'un amplificador operacional en funció de la freqüència, amb caiguda progressiva.](assets/03_Unitat8_Amplificadors_d_alterna_img_9.png)

*Figura: Figura 8.19 Variació del PSRR de l'alimentació positiva amb la freqüència.*

El CMRR i el PSRR valen 80–120 dB a baixa freqüència, però es degraden a raó de 20 dB/dècada a partir d'una freqüència de cantonada que sol ser de desenes o centenars de Hz. A  $f_0 \gg f_{c,CMRR}$  el rebuig pot haver caigut a 40–60 dB. En un exemple amb 100 mV de mode comú a 10 kHz, CMRR de 80 dB i guany 100, la component d'error a la sortida val 1 mV; i per damunt de la cantonada aquesta component apareix **desfasada 90°** respecte al senyal útil, cosa que la fa rebutjable per la detecció coherent però no pels mètodes no coherents.

El PSRR es degrada igual: tota variació de l'alimentació modifica la tensió d'offset per un factor  $\Delta V_{\text{CC}}/PSRR$  i es reflecteix a la sortida, també desfasada 90° a alta freqüència. El PSRR de l'alimentació negativa sol ser pitjor que el de la positiva. Amb 10 mV superposats a l'alimentació i guany 100, la sortida en pateix 0,32 mV a 10 kHz i 32 mV a 1 MHz, on el PSRR ja ha caigut a uns 30 dB: les fonts commutades són especialment problemàtiques.

Aquestes degradacions pesen sobre els circuits amb tensió de mode comú significativa a l'entrada, com el propi amplificador d'alterna no inversor, on  $V_{\text{CM}} = V_i$; en canvi són irrellevants en els circuits inversors, com el pseudopont, on la tensió de mode comú és nul·la.

![Connexió de condensadors de desacoblament, un electrolític i un ceràmic en paral·lel, entre cada pin d'alimentació de l'amplificador operacional i massa.](assets/03_Unitat8_Amplificadors_d_alterna_img_10.png)

*Figura: Figura 8.20 Condensadors de desacoblament als pins d'alimentació.*

La mitigació estàndard davant del PSRR finit és el **desacoblament**: dos condensadors en paral·lel per a cada tensió d'alimentació. L'**electrolític** de 10–100 µF dona baixa impedància a baixa freqüència, però la seva inductància sèrie el fa comportar-se com una bobina per damunt de la seva ressonància pròpia, de desenes de kHz a pocs MHz. El **ceràmic** de 100 nF a 1 µF té la ressonància pròpia a desenes de MHz i cobreix les freqüències que l'electrolític ja no filtra. El muntatge exigeix col·locar el ceràmic el més a prop possible dels pins d'alimentació —menys de 5 mm per damunt de 100 kHz—, pistes curtes i amples per minimitzar-ne la inductància, i un pla de massa continu que redueixi la impedància de retorn dels corrents d'alimentació.

> [!TIP] **Síntesi**
>
> L'amplificador d'alterna és passa-banda perquè així suprimeix els errors de contínua de l'operacional, redueix el soroll  $\frac{1}{f}$  i atenua la xarxa. Ha de deixar passar amb guany pla no només  $f_0$  sinó tota la banda  $f_0 \pm f_{m,\max}$  que ocupa el senyal modulat, amb les freqüències de tall a −3 dB clarament fora d'aquest interval, i es centra fent  $f_0$  igual a la mitjana geomètrica dels dos talls. L'amplada de banda enfronta error de guany contra rebuig de soroll. En les dues topologies, el condensador en sèrie amb  $R_1$  fixa el tall inferior i el condensador en paral·lel amb  $R_2$  el superior; la versió d'instrumentació aporta rebuig de mode comú però no es pot muntar amb un integrat comercial de tres terminals. La tria de l'operacional queda condicionada pel  $GBW$, pel slew rate, per la capacitat d'entrada i de les pistes, i per la degradació de CMRR i PSRR a 20 dB/dècada, que a més genera errors desfasats 90° respecte al senyal útil.

[← 2. Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts](#conversió-impedànciatensió-divisors-inversor-ponts-i-pseudoponts)[4. Estimació de l'amplitud: mètodes no coherents →](#estimació-de-lamplitud-mètodes-no-coherents)

---

<!-- FIN CAPÍTULO: 03_Unitat8_Amplificadors_d_alterna -->

---

<!-- INICIO CAPÍTULO: 04_Unitat8_04_Metodes_no_coherents -->

# Estimació de l'amplitud: mètodes no coherents

Sistemes de Mesura · **Unitat 8 — Condicionament de sensors en alterna** · Document 4 de 6

# Estimació de l'amplitud: mètodes no coherents

Dedicació estimada: 12 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir la modulació AM de la DSB i decidir quan un mètode no coherent és suficient.
> - Comparar les tres famílies de convertidors de valor eficaç quant a exactitud, amplada de banda, velocitat i cost.
> - Explicar per què tot mètode no coherent introdueix un biaix positiu davant del soroll i les interferències.
> - Relacionar el nombre de quadrants d'un multiplicador analògic amb la seva aplicació.
> - Dimensionar la constant de temps d'un detector de pic entre les seves dues condicions.

Un cop el convertidor impedància–tensió ha generat el senyal sinusoïdal i l'amplificador d'alterna l'ha portat al nivell adequat, cal extreure'n l'amplitud com a tensió contínua. Quines tècniques són admissibles depèn de com respon el convertidor davant del mesurand, i per això cal distingir abans dos tipus de modulació.

## 1 Modulació AM i modulació DSB

![Senyal amb modulació d'amplitud clàssica: portadora amb envolupant sempre positiva i separada de zero, amb el seu espectre.](assets/04_Unitat8_04_Metodes_no_coherents_img_1.png)

*Figura: Figura 8.21 Modulació d'amplitud clàssica: l'envolupant, en discontinu, no arriba mai a zero.*

En la **modulació d'amplitud clàssica** l'amplitud a la sortida del convertidor és diferent de zero per a qualsevol valor físicament possible del mesurand, i la fase respecte a l'oscil·lador es manté constant —0° o 180°, però no canvia amb  $x$:

$$
v(t) = A(x)\cos(2\pi f_0 t + \varphi_0), \qquad A(x) > 0\ \ \forall x \qquad (8.27)
$$

És el cas de l'amplificador inversor capacitiu amb un sensor  $C_s = C_0(1+x)$: la sortida és proporcional a  $1+x$, estrictament positiva mentre  $x > -1$, i el desfasament de 180° que introdueix l'inversor és constant. Aquí n'hi ha prou amb mesurar l'envolupant, i tots els mètodes no coherents hi són adequats.

![Senyal amb modulació de doble banda lateral: l'amplitud s'anul·la quan el mesurand passa per zero i la fase salta 180 graus en canviar-ne el signe.](assets/04_Unitat8_04_Metodes_no_coherents_img_2.png)

*Figura: Figura 8.22 Modulació de doble banda lateral: l'amplitud s'anul·la a $x=0$ i el signe queda codificat en la fase.*

En la **modulació de doble banda lateral** (DSB) l'amplitud és proporcional a  $x$  i s'anul·la a l'origen,  $v(t) = A\,x(t)\cos(2\pi f_0 t)$. És el cas paradigmàtic del pont o pseudopont diferencial, dissenyat precisament perquè la sortida sigui nul·la a la situació de referència. Quan  $x>0$  la fase respecte a l'oscil·lador és 0°, i quan  $x<0$  passa a 180°. L'envolupant val  $|A\,x(t)|$, sempre positiva: un detector d'envolupant retorna  $|x|$  i **perd el signe**. En una LVDT centrada la sortida és nul·la, i en desplaçar-se el nucli el senyal creix en amplitud però el sentit del desplaçament queda codificat en la fase. Recuperar-lo exigeix detecció coherent.

## 2 Convertidors de valor eficaç

El valor eficaç d'un senyal periòdic de període  $T$  és

$$
V_\mathrm{rms} = \sqrt{\frac{1}{T}\int_0^T v^2(t)\,dt} \qquad (8.28)
$$

i té una interpretació física directa: és la tensió contínua que dissiparia la mateixa potència en una resistència. Un convertidor RMS lliura una tensió contínua i positiva per conveni, igual al valor eficaç de l'entrada.

> [!WARNING] **El límit de tots els mètodes no coherents**
>
> Un convertidor RMS mesura el valor eficaç de tot el que li arriba, sense discriminar la freqüència de treball. Amb senyal útil  $V_s$, interferència  $V_{\text{int}}$  i soroll  $V_n$  a l'entrada, la sortida val
>
>

$$
V_\mathrm{out} = \sqrt{V_s^2 + V_{\text{int}}^2 + V_n^2} \qquad (8.29)
$$

>
> de manera que la interferència i el soroll hi entren de forma quadràtica i generen un biaix **sempre positiu**. El soroll  $V_n$  depèn de l'amplada de banda equivalent de soroll del sistema, fixada generalment per l'amplificador d'alterna.

![Convertidor RMS tèrmic: el senyal escalfa una resistència, la sortida contínua n'escalfa una altra i un llaç de retroalimentació iguala les dues temperatures.](assets/04_Unitat8_04_Metodes_no_coherents_img_3.png)

*Figura: Figura 8.23 Convertidor RMS tèrmic.*

El **convertidor tèrmic** materialitza la definició física. El senyal altern escalfa una resistència  $R_1$, la tensió contínua de sortida n'escalfa una altra  $R_2$  de les mateixes característiques, i un amplificador de retroalimentació compara les temperatures mesurades pels dos sensors i ajusta la sortida fins a igualar-les. En estat estacionari les potències dissipades s'igualen i, si  $R_1 = R_2$, la sortida és el valor eficaç de l'entrada.

El **càlcul matemàtic** implementa la fórmula amb circuits analògics, en dues variants.

![Diagrama de blocs del convertidor RMS de càlcul explícit: elevació al quadrat, filtre passa-baixes i arrel quadrada.](assets/04_Unitat8_04_Metodes_no_coherents_img_4.png)

*Figura: Figura 8.24 Convertidor RMS de càlcul explícit.*

En la implementació **explícita** el senyal s'eleva al quadrat amb un multiplicador analògic, es filtra passa-baixes per estimar-ne el valor mitjà i se'n calcula l'arrel quadrada amb un amplificador logarítmic, un divisor per dos i un antilogarítmic. El seu inconvenient és el marge dinàmic: amb entrades grans, el quadrat pot saturar les etapes intermèdies.

![Diagrama de blocs del convertidor RMS de càlcul implícit: el quadrat es normalitza per la pròpia sortida i el resultat es filtra passa-baixes.](assets/04_Unitat8_04_Metodes_no_coherents_img_5.png)

*Figura: Figura 8.25 Convertidor RMS de càlcul implícit.*

En la implementació **implícita** el quadrat es divideix per la pròpia sortida abans de filtrar-lo, i la retroalimentació fa que la sortida s'autoajusti:

$$
V_\mathrm{out} = \overline{\left(\frac{v^2(t)}{V_\mathrm{out}}\right)} \Rightarrow V_\mathrm{out}^2 = \overline{v^2(t)} \Rightarrow V_\mathrm{out} = \sqrt{\overline{v^2(t)}} \qquad (8.30)
$$

La divisió evita la saturació i dona un marge dinàmic més gran, a canvi d'una amplada de banda menor —fins a alguns MHz— i de pitjor exactitud, per les imprecisions del divisor analògic. En totes dues variants, la freqüència de tall del filtre passa-baixes fixa el compromís entre velocitat de resposta i arrissat residual a la sortida: tall baix dona bona estimació del valor mitjà però resposta lenta; tall alt segueix canvis ràpids però deixa arrissat.

![Convertidor RMS basat en rectificació: rectificador de doble ona, filtre passa-baixes i amplificador de guany 1,11.](assets/04_Unitat8_04_Metodes_no_coherents_img_6.png)

*Figura: Figura 8.26 Convertidor RMS basat en rectificació.*

El tercer mètode rectifica el senyal,troba el valor mitjà i el multiplica per 1,1. Aquest factor es basa en la relació que existeix, per a una forma d'ona donada, entre el valor eficaç i el valor mitjà rectificat: el **factor de forma**. Per a una sinusoide de pic  $V_p$, el valor eficaç és  $V_p/\sqrt{2}$  i el valor mitjà rectificat de doble ona és  $2V_p/\pi$, de manera que

$$
V_\mathrm{rms} = \frac{\pi}{2\sqrt{2}}\,\overline{|v(t)|} \approx 1{,}11\cdot\overline{|v(t)|} \qquad (8.31)
$$

L'arquitectura és, doncs, un rectificador de doble ona —de precisió amb operacionals, si es vol eliminar la caiguda dels díodes—, un filtre passa-baixes i un amplificador de guany 1,11.

| Família | Exactitud i abast | Velocitat i cost |
|:--- |:--- |:--- |
| **Tèrmic** | Valor eficaç veritable de qualsevol forma d'ona, independentment del contingut harmònic. Amplada de banda fins a centenars de MHz, perquè la mesura es basa en efectes tèrmics que no depenen de la freqüència. | Resposta lenta, de dècimes de segon o més, perquè la transmissió de calor ho és. El més car del mercat. |
| **Càlcul matemàtic** | Valor eficaç veritable. L'explícita té més amplada de banda i menys marge dinàmic; la implícita, a l'inrevés. | Molt més ràpid i molt menys costós que el tèrmic. |
| **Rectificació** | El factor de forma 1,11 **només val per a senyals sinusoïdals**: amb distorsió harmònica el factor ja no és aquest i la mesura és errònia. L'amplada de banda la limita la velocitat de commutació dels díodes, que per damunt d'alguns centenars de kHz distorsionen la forma d'ona rectificada. | El més senzill i barat, amb components molt comuns. Resposta ràpida segons el filtre. |

En el condicionament de sensors reactius la portadora a  $f_0$  és sempre sinusoïdal, de manera que la limitació del mètode per rectificació no acostuma a ser un problema pràctic mentre els harmònics siguin negligibles.

## 3 Multiplicadors analògics

![Símbol d'un multiplicador analògic amb dues entrades Vx i Vy i una sortida Vout.](assets/04_Unitat8_04_Metodes_no_coherents_img_7.png)

*Figura: Figura 8.27 Multiplicador analògic.*

Els multiplicadors analògics són el bloc central dels convertidors RMS per càlcul matemàtic i, com es veurà, també dels detectors coherents homodins. Implementen el producte instantani de dues entrades:

$$
V_\mathrm{out}(t) = \frac{V_x(t)\cdot V_y(t)}{K} \qquad (8.32)
$$

on  $K$  és un factor d'escala amb unitats de volt que depèn de l'integrat.

| Quadrants | Signes admesos | Aplicació típica |
|:--- |:--- |:--- |
| **Un quadrant** | Les dues entrades sempre positives; sortida sempre positiva. | No pot multiplicar senyals alterns, que canvien de signe. |
| **Dos quadrants** | Una entrada bipolar i l'altra unipolar. La sortida canvia de signe amb l'entrada bipolar. | Modulació d'amplitud, control de guany variable, detecció coherent amb referència unipolar. |
| **Quatre quadrants** | Totes dues entrades bipolars, amb signes independents. | Detecció homodina, on tant el senyal com la referència sinusoïdal canvien de signe. És la norma en condicionament de sensors, perquè els senyals a  $f_0$  canvien de signe cada semiperíode. |

![Esquemes de multiplicació, divisió i elevació a potència construïts amb amplificadors logarítmics i antilogarítmics.](assets/04_Unitat8_04_Metodes_no_coherents_img_8.png)

*Figura: Figura 8.28 Operacions no lineals amb amplificadors logarítmics i antilogarítmics.*

La manera més senzilla d'implementar un multiplicador d'**un quadrant** aprofita la propietat dels logaritmes,  $V_x V_y = \exp(\ln V_x + \ln V_y)$: es calcula el logaritme de cada entrada, se sumen i se'n pren l'exponencial. Cada bloc es construeix amb un operacional i una unió p-n que aporta la relació exponencial corrent–tensió.

![Amplificador logarítmic: operacional amb una resistència d'entrada i un díode en conducció directa a la realimentació.](assets/04_Unitat8_04_Metodes_no_coherents_img_9.png)

*Figura: Figura 8.29 Amplificador logarítmic amb un díode.*

Amb l'operacional ideal, tot el corrent d'entrada  $V_{\text{in}}/R$  circula pel díode. De la característica  $I_F = I_S(e^{V_F/\eta V_T} - 1)$, amb  $V_T = kT/q$  i  $\eta$  entre 1 i 2 segons el procés de fabricació, i tenint en compte que en conducció directa  $I_F \gg I_S$:

$$
V_\mathrm{out} = -V_F \approx -\eta\,V_T \ln\!\left(\frac{V_{\text{in}}}{I_S R}\right) \qquad (8.33)
$$

El mateix circuit amb un transistor bipolar amb la base a massa —i per tant el col·lector també, pel curtcircuit virtual— dona la mateixa relació, perquè el transistor hi actua com un díode.

![Característica entrada-sortida d'un amplificador logarítmic, amb la regió logarítmica útil acotada per una tensió d'entrada mínima i una de màxima.](assets/04_Unitat8_04_Metodes_no_coherents_img_10.png)

*Figura: Figura 8.30 Característica entrada–sortida d'un amplificador logarítmic.*

Aquests amplificadors també serveixen per convertir magnituds a decibels: posant-hi al darrere un inversor de guany  $-G$, la sortida és proporcional a  $\log_{10}(V_{\text{in}}/V_X)$  amb  $V_X = I_S R$, de manera que s'anul·la per a  $V_{\text{in}} = V_X$. El pendent de la característica val  $G\,\eta\,k\,T/(q\log_{10}e)$  i, per tant, **depèn de la temperatura** de la unió. A més, la saturació de l'operacional i la conducció del transistor acoten per baix i per dalt el rang d'entrada útil.

![Amplificador antilogarítmic: la resistència i el transistor intercanvien posicions respecte a l'amplificador logarítmic.](assets/04_Unitat8_04_Metodes_no_coherents_img_11.png)

*Figura: Figura 8.31 Amplificador antilogarítmic.*

L'amplificador antilogarítmic fa la funció inversa intercanviant les posicions de la resistència i el transistor, de manera que la sortida és el corrent de col·lector per la resistència de realimentació:

$$
V_\mathrm{out} = I_C R_1 \approx R_1 I_{\text{ES}}\, e^{-V_i/V_T} \qquad (8.34)
$$

i torna a dependre fortament de la temperatura de la unió; hi ha circuits més sofisticats que ho compensen.

![Cèl·lula de Gilbert: dos transistors NPN i dos díodes en una topologia que dona el producte de dues entrades.](assets/04_Unitat8_04_Metodes_no_coherents_img_12.png)

*Figura: Figura 8.32 Cèl·lula de Gilbert.*

El multiplicador logarítmic és d'un sol quadrant, precisament perquè el logaritme només admet una polaritat. Per a dos o quatre quadrants cal la **cèl·lula de Gilbert**, la topologia multiplicadora més emprada en circuits integrats. Combina dos transistors NPN amb dos díodes —o dos transistors en configuració de díode— i aconsegueix alhora el producte analògic, la compensació intrínseca de la dependència amb la temperatura i l'admissió d'una entrada bipolar.

Imposant l'equació de malla a les quatre unions i suposant els transistors i els díodes aparellats i a la mateixa temperatura, els termes  $V_T$  i els corrents de saturació es cancel·len i queda  $I_{c1}/I_{c2} = I_{D1}/I_{D2}$. Escrivint els corrents com un valor mitjà més una desviació,  $I_{c1{,}2} = I_c \pm \Delta I_c$  i  $I_{D1{,}2} = I_x \pm \Delta I_x$, la sortida en corrent diferencial resulta

$$
\Delta I_c = I_Y\cdot\frac{\Delta I_x}{I_x} \qquad (8.35)
$$

on  $I_Y$  és el corrent de polarització de la cèl·lula. Com que  $I_Y$  és sempre positiu, la cèl·lula sola és un multiplicador de **dos quadrants**, amb  $\Delta I_x$  com a entrada bipolar. Les implementacions comercials hi afegeixen xarxes d'atenuació a l'entrada i amplificació a la sortida perquè la cèl·lula treballi sempre en règim lineal.

![Multiplicador de quatre quadrants: dues cèl·lules de Gilbert amb convertidors tensió-corrent a les dues entrades i un convertidor corrent-tensió a la sortida.](assets/04_Unitat8_04_Metodes_no_coherents_img_13.png)

*Figura: Figura 8.33 Multiplicador de quatre quadrants.*

El multiplicador de **quatre quadrants** combina dues cèl·lules de Gilbert amb conversió tensió–corrent a les dues entrades i conversió corrent–tensió a la sortida. Cada entrada s'aplica a un parell diferencial amb resistència entre emissors, que en genera un corrent diferencial proporcional:  $\Delta I_X = V_X/(2R_{\text{EX}})$  i  $\Delta I_{\text{REF}} = V_Y/(2R_{\text{EY}})$. La diferència de corrents de col·lector de les dues cèl·lules és proporcional al producte  $\Delta I_X \cdot \Delta I_{\text{REF}}$  i l'amplificador de sortida la converteix en  $E_o = K\,V_X V_Y$.

## 4 Detectors de pic o d'envolupant

![Detector de pic bàsic format per un díode, un condensador i una resistència de descàrrega.](assets/04_Unitat8_04_Metodes_no_coherents_img_14.png)

*Figura: Figura 8.34 Detector de pic bàsic.*

Els detectors de pic no calculen el valor eficaç: lliuren una estimació de l'envolupant superior. Quan la tensió d'entrada supera la de sortida més la caiguda del díode, aquest condueix i el condensador es carrega ràpidament cap al pic; quan cau per sota, el díode es talla i el condensador es descarrega lentament per la resistència amb constant de temps  $\tau = RC$.

![Senyal d'entrada, envolupant teòrica i sortida d'un detector d'envolupant, amb la sortida d'un disseny poc afortunat com a comparació.](assets/04_Unitat8_04_Metodes_no_coherents_img_15.png)

*Figura: Figura 8.35 Entrada, envolupant teòrica i sortida d'un detector d'envolupant.*

La sortida puja de pressa fins al pic i baixa lentament seguint l'exponencial de descàrrega, i mai no supera  $V_p - V_D$: amb  $V_D \approx 0{,}6$  V, el detector passiu no funciona amb senyals d'amplitud inferior. El **detector de pic de precisió** amb operacionals supera aquesta limitació i permet detectar senyals petits.

![Detector de pic de precisió construït amb amplificadors operacionals per eliminar l'efecte de la caiguda del díode.](assets/04_Unitat8_04_Metodes_no_coherents_img_16.png)

*Figura: Figura 8.36 Detector de pic de precisió.*

La constant de temps és el paràmetre de disseny crític i té dues exigències contraposades. Quan l'amplitud és constant, la sortida ha de ser tan plana com sigui possible: l'**arrissat** entre dues crestes successives val aproximadament

$$
\Delta V \approx \frac{V_p T_0}{\tau} = \frac{V_p}{f_0\,\tau} \qquad (8.36)
$$

de manera que  $\tau \gg \frac{1}{f_0}$, i típicament es recomana  $\tau \geq 10/f_0$. Quan l'amplitud varia, en canvi, el condensador s'ha de poder descarregar prou de pressa per seguir-la, cosa que exigeix  $\tau \leq \frac{1}{2\pi f_{m,\max}}$. El criteri conjunt és

$$
\frac{1}{2\pi f_{m,\max}} \geq \tau \gg \frac{1}{f_0} \qquad (8.37)
$$

L'inconvenient principal dels detectors de pic és la sensibilitat al **soroll impulsiu**. Un pols breu de tensió alta carrega ràpidament el condensador fins a un pic fals molt superior a l'envolupant real i, com que la descàrrega és lenta, l'error persisteix durant molts períodes de la portadora. Per això els detectors de precisió solen incorporar un díode addicional de protecció o una limitació del corrent de càrrega; en entorns molt sorollosos —motors, commutadors de potència, contactes mecànics— la solució preferida és la detecció coherent.

> [!TIP] **Síntesi**
>
> Amb modulació AM clàssica l'amplitud no s'anul·la mai i la fase és constant, de manera que n'hi ha prou amb mesurar l'envolupant; amb modulació DSB l'amplitud s'anul·la a  $x=0$  i el signe queda a la fase, que cap mètode no coherent no pot recuperar. Tots els mètodes no coherents mesuren el que els arriba sense discriminar la freqüència, i per això el soroll i les interferències hi entren quadràticament com a biaix positiu. Els convertidors RMS tèrmics donen el valor eficaç veritable amb gran amplada de banda però són lents i cars; els de càlcul matemàtic són ràpids i econòmics, amb l'explícit limitat pel marge dinàmic i l'implícit per l'amplada de banda; els de rectificació són els més senzills, amb el factor 1,11 vàlid només per a sinusoides. El multiplicador analògic és el bloc comú: d'un quadrant amb logaritmes, i de dos o quatre amb cèl·lules de Gilbert. Els detectors de pic exigeixen una constant de temps prou gran davant del període de la portadora i prou petita davant de la dinàmica del mesurand, i són vulnerables al soroll impulsiu.

[← 3. Amplificadors d'alterna i limitacions dels operacionals](#amplificadors-dalterna-i-limitacions-dels-operacionals)[5. Detecció coherent: homodina, rectificació síncrona i mostreig síncron →](#detecció-coherent-homodina-rectificació-síncrona-i-mostreig-síncron)

---

<!-- FIN CAPÍTULO: 04_Unitat8_04_Metodes_no_coherents -->

---

<!-- INICIO CAPÍTULO: 05_Unitat8_Deteccio_coherent -->

# Detecció coherent: homodina, rectificació síncrona i mostreig síncron

Sistemes de Mesura · **Unitat 8 — Condicionament de sensors en alterna** · Document 5 de 6

# Detecció coherent: homodina, rectificació síncrona i mostreig síncron

Dedicació estimada: 10 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Enunciar els tres avantatges de la detecció coherent i la condició que ha de complir la referència.
> - Obtenir la sortida d'un detector homodí i interpretar-la en funció del desfasament.
> - Quantificar l'atenuació d'una interferència i la reducció de soroll que aporta el filtre passa-baixes.
> - Justificar per què la rectificació síncrona no necessita multiplicador i quin preu paga per això.
> - Explicar què elimina cada combinació de mostres en el mostreig síncron i quan és vàlid sub-mostrejar.

Els mètodes no coherents mesuren l'envolupant sense cap referència temporal: ignoren la fase i per això la seva sortida és sempre positiva. En termes d'informació, en llencen la meitat —saben quant val l'amplitud, però no en quin sentit apunta el mesurand. La detecció coherent aprofita que l'oscil·lador que excita el convertidor impedància–tensió és, en tot moment, una referència de fase perfectament coneguda.

## 1 Principi i avantatges

Un senyal sinusoïdal té dos paràmetres lliures, l'amplitud i la fase. La tensió d'entrada al detector és

$$
v_i(t) = V_i \cos(2\pi f_0 t + \varphi) \qquad (8.38)
$$

on  $V_i$  depèn del mesurand i  $\varphi$  és el desfasament respecte a la referència. Un convertidor no coherent retorna només  $V_i$; un detector coherent pot retornar  $V_i\cos\varphi$  i  $V_i\sin\varphi$  —les components en fase i en quadratura— i, a partir d'elles, reconstruir tant l'amplitud,  $V_i = \sqrt{V_I^2 + V_Q^2}$, com la fase,  $\varphi = \arctan(V_Q/V_I)$. La configuració més habitual, però, és una sortida única proporcional a  $V_i\cos\varphi$, quan el desfasament de la cadena és conegut i compensat.

L'element diferenciador és el **senyal de referència**. Ha de ser síncron amb l'oscil·lador que excita el convertidor —sovint és literalment el mateix senyal— i la condició imprescindible és que tots dos tinguin exactament la mateixa freqüència  $f_0$. Pot tenir un desfasament conegut respecte a l'oscil·lador, però ha de ser estable i controlat: un desfasament desconegut o variable és una font d'error sistemàtic. La forma d'ona de la referència —sinusoïdal, quadrada o tren d'impulsos— determina el tipus de detector.

| Avantatge | Origen |
|:--- |:--- |
| **Recuperació del signe en DSB** | Amb el pont o pseudopont diferencial, la fase salta de 0° a 180° quan  $x$  canvia de signe. El detector coherent retorna valor positiu per a  $x>0$  i negatiu per a  $x<0$, cosa que el fa imprescindible en sensors de desplaçament bidireccional com la LVDT. |
| **Rebuig de soroll i interferències** | El filtre passa-baixes que segueix la multiplicació estreny l'amplada de banda efectiva de soroll. Amb amplada de banda de l'amplificador d'alterna  $BW_{\text{AC}}$  i tall del filtre  $f_c$, el soroll es comprimeix en un factor  $\sqrt{\frac{f_c}{BW_{\text{AC}}}}$. |
| **Rebuig de la quadratura** | Els errors deguts al CMRR i al PSRR finits apareixen desfasats 90° respecte al senyal útil. Un detector configurat per mesurar la component en fase els rebutja completament, cosa que els mètodes no coherents no poden fer. |

## 2 Detecció homodina

![Detector homodí: multiplicador que rep el senyal i la referència sinusoïdal, seguit d'un filtre passa-baixes.](assets/05_Unitat8_Deteccio_coherent_img_1.png)

*Figura: Figura 8.37 Detector homodí.*

És el mètode coherent canònic: multiplicar el senyal per una referència de la mateixa freqüència i filtrar el resultat amb un passa-baixes. La multiplicació trasllada part de l'espectre des de  $f_0$  fins a la contínua, on s'extreu el valor del mesurand. Amb una referència  $v_{\text{ref}}(t) = V_r\cos(2\pi f_0 t)$  i la identitat  $\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha-\beta) + \cos(\alpha+\beta)]$:

$$
v_i\cdot v_{\text{ref}} = \frac{V_i V_r}{2}\left[\cos\varphi + \cos(4\pi f_0 t + \varphi)\right] \qquad (8.39)
$$

El producte conté un terme constant i un terme al doble de la freqüència de treball. Si el tall del filtre compleix  $f_c \ll 2f_0$, el segon terme s'elimina i la sortida és

$$
V_\mathrm{out} = \frac{V_i V_r}{2}\cos\varphi \qquad (8.40)
$$

![Senyal d'entrada, referència i sortida del multiplicador amb el seu valor mitjà per als casos en fase, en quadratura i en contrafase.](assets/05_Unitat8_Deteccio_coherent_img_2.png)

*Figura: Figura 8.38 Senyals d'un detector homodí en fase, en quadratura i en contrafase.*

La interpretació és directa. Per a  $\varphi = 0°$  la sortida és màxima i positiva; per a  $\varphi = 180°$, màxima en valor absolut i negativa, que és el cas de  $x<0$  en modulació DSB; i per a  $\varphi = 90°$  o  $270°$  la sortida és nul·la, és a dir, la quadratura queda completament rebutjada.

A la pràctica  $\varphi$  no és exactament zero, pels retards de fase de l'amplificador d'alterna i de les altres etapes. Per a desfasaments petits l'error relatiu és  $(1-\cos\varphi) \approx \varphi^2/2$, de segon ordre i per tant molt petit; si el desfasament és gran però constant, és fàcilment corregible, i si no ho és, cal recórrer a la detecció I/Q.

### Tria de la freqüència de tall

És el paràmetre de disseny clau, i comporta un compromís anàleg al de la constant de temps del detector de pic. Una  $f_c$  baixa dona millor rebuig de soroll —el soroll de sortida és proporcional a  $\sqrt{f_c}$ — però impedeix seguir canvis ràpids del mesurand: si  $x$  varia a una freqüència superior a  $f_c$, la sortida s'atenua i apareix retard de fase.

Una interferència sinusoïdal a  $f_{\text{int}}$  superposada al senyal es trasllada, en multiplicar, a  $|f_{\text{int}}-f_0|$  i a  $f_{\text{int}}+f_0$. L'atenuació que rep la component baixa amb un filtre de primer ordre és

$$
|H(f_{\text{int}}-f_0)| \approx \frac{f_c}{|f_{\text{int}}-f_0|} \qquad \mathrm{per a } |f_{\text{int}}-f_0| \gg f_c \qquad (8.41)
$$

Amb  $f_0 = 100$  kHz, la xarxa a 50 Hz i  $f_c = 10$  Hz, la interferència queda traslladada a prop de 100 kHz i l'atenuació val  $10^{-4}$: la seva amplitud a la sortida és deu mil vegades inferior a la que tindria en un convertidor RMS equivalent. Aquest és l'avantatge de la detecció coherent quan la freqüència de treball s'ha escollit prou allunyada de les interferències.

Pel que fa al soroll, amb  $BW_{\text{AC}} = 1$  kHz i  $f_c = 1$  Hz la reducció és d'un factor  $\sqrt{\frac{1}{1000}} \approx 1/31{,}6$. Valors habituals de 10–100 Hz per a  $f_c$  i d'1–10 kHz per a  $BW_{\text{AC}}$  donen reduccions de 20–40 dB respecte als mètodes no coherents, entre un i dos ordres de magnitud de millora en la resolució.

## 3 Rectificació síncrona

![Diagrama de blocs del rectificador síncron amb referència quadrada i filtre passa-baixes, i senyals resultants.](assets/05_Unitat8_Deteccio_coherent_img_3.png)

*Figura: Figura 8.39 Rectificador síncron: diagrama de blocs i senyals.*

Comparteix el principi de la detecció homodina —multiplicació seguida de filtratge— però substitueix la referència sinusoïdal per una **ona quadrada** sincronitzada amb l'oscil·lador, que val +1 durant el semiperíode positiu i −1 durant el negatiu. Multiplicar per  $\pm 1$  no és res més que canviar de signe el senyal cada semiperíode, i això **no necessita cap multiplicador analògic**: n'hi ha prou amb un commutador.

![Implementació circuital del rectificador síncron: operacional que actua com a seguidor o com a inversor de guany −1 segons el nivell de la referència quadrada.](assets/05_Unitat8_Deteccio_coherent_img_4.png)

*Figura: Figura 8.40 Implementació circuital del rectificador síncron.*

La implementació típica connecta el terminal no inversor d'un operacional alternativament al senyal d'entrada o a massa, segons el nivell de la referència: en el primer cas el circuit actua com a seguidor, i en el segon com a inversor de guany −1. Darrere s'hi situa el mateix filtre passa-baixes del detector homodí.

| Desfasament | Resultat |
|:--- |:--- |
| **0° (en fase)** | El semiperíode positiu del senyal coincideix amb el de la referència. No hi ha inversió on el senyal és positiu i sí on és negatiu: s'obté una rectificació de doble ona sempre positiva, de valor mitjà màxim i proporcional a l'amplitud. |
| **180° (contrafase)** | El resultat és sempre negatiu i la sortida del filtre és màxima en valor absolut i negativa, exactament com en la detecció homodina. |
| **90° (quadratura)** | La simetria del sinus desplaçat 90° respecte als semiperíodes de la referència fa que la integral neta sobre cada semiperíode sigui zero i el valor mitjà sigui nul: la quadratura queda completament rebutjada, igual que en la detecció homodina. |

El preu és un rebuig de soroll lleugerament inferior. La referència quadrada conté, a més de la fonamental a  $f_0$, **harmònics imparells** a  $3f_0, 5f_0, 7f_0,\dots$  amb amplituds  $4/(k\pi)$, de manera que el rectificador és sensible també a components de soroll i d'interferència properes a aquests harmònics, que es traslladen a la contínua i travessen el filtre. L'efecte sol ser negligible si les interferències estan prou allunyades de tots els harmònics de  $f_0$, però és un problema real en entorns amb interferències harmònicament relacionades amb la freqüència de treball.

A canvi, la rectificació síncrona és molt més senzilla d'implementar, és menys sensible a les imperfeccions del circuit de referència —una ona quadrada es genera amb precisió amb circuits digitals— i consumeix menys. Per a la majoria d'aplicacions de condicionament de sensors reactius la degradació del rebuig és irrellevant, i és la solució preferida.

## 4 Mostreig síncron i sub-mostreig

La tercera modalitat pren com a referència un **tren d'impulsos** situats en instants precisos i sincronitzats amb l'oscil·lador, de manera que el mostreig equival a multiplicar el senyal per  $\sum_n \delta(t-t_n)$. Amb  $t_n = n/f_0 + \tau_0$, on  $\tau_0$  és el desplaçament del tren respecte al zero de l'oscil·lador:

$$
v_i(t_n) = V_i\cos(2\pi n + 2\pi f_0\tau_0 + \varphi) = V_i\cos(2\pi f_0\tau_0 + \varphi) \qquad (8.42)
$$

El valor mostrejat és constant —independent de  $n$ — i proporcional a  $V_i\cos(\varphi + \psi)$  amb  $\psi = 2\pi f_0\tau_0$. Variant  $\tau_0$  es pot obtenir la mostra en qualsevol fase del cicle, i mostres preses en instants diferents donen projeccions del senyal en direccions de fase diferents.

![Estratègia de detecció amb quatre mostres per cicle, uniformement espaiades un quart de període.](assets/05_Unitat8_Deteccio_coherent_img_5.png)

*Figura: Figura 8.41 Detecció amb quatre mostres per cicle.*

L'estratègia habitual pren quatre mostres per cicle, espaiades  $T_0/4$. Amb  $B$  l'amplitud d'una component en quadratura —un error de CMRR, per exemple— i  $C$  una tensió d'offset contínua, les quatre mostres valen  $V_i\cos\varphi + B\sin\varphi + C$,  $-V_i\sin\varphi + B\cos\varphi + C$,  $-V_i\cos\varphi - B\sin\varphi + C$  i  $V_i\sin\varphi - B\cos\varphi + C$. Combinant-les:

$$
v_s(0) - v_s(T_0/2) = 2V_i\cos\varphi + 2B\sin\varphi \qquad (8.43)
$$

$$
v_s(T_0/4) - v_s(3T_0/4) = -2V_i\sin\varphi + 2B\cos\varphi \qquad (8.44)
$$

Amb mostreig perfectament en fase, la primera combinació val  $2V_i$  i la segona  $2B$, de manera que senyal útil i quadratura queden separats. En general, per a  $\varphi$  arbitrari, les quatre mostres permeten resoldre el sistema i extreure  $V_i$,  $B$,  $C$  i  $\varphi$  per separat. Amb **dues** mostres per cicle, als instants 0 i  $T_0/2$, s'elimina l'offset però no la quadratura; amb **quatre** s'eliminen totes dues i, a més, es recupera el signe de  $x$.

> [!WARNING] **Què fixa la taxa de mostreig**
>
> El mostreig síncron no pretén reconstruir la sinusoide a  $f_0$, sinó l'envolupant  $V_i(t)\cos\varphi$, que varia molt més lentament: fa implícitament una desmodulació coherent i mostreja després el senyal desmodulat. Per això la condició de Nyquist s'aplica al mesurand,
>
>

$$
f_s \geq 2\,f_{m,\max} \qquad (8.45)
$$

>
> i no a la portadora. La taxa de mostreig pot ser molt inferior a  $f_0$: amb  $f_0 = 10$  kHz i  $f_{m,\max} = 1$  Hz n'hi hauria prou amb una mostra cada 5.000 cicles, tot i que a la pràctica es prefereix  $f_s$  entre 10 i 100 vegades  $f_{m,\max}$  per tenir marge i poder emprar filtres digitals senzills. El **sub-mostreig estricte**,  $f_s < f_0$, és per tant perfectament vàlid.

El sub-mostreig té un avantatge addicional: es poden **promitjar** múltiples mostres preses en el mateix instant de fase del cicle, cosa que redueix el soroll de la mesura.

> [!TIP] **Síntesi**
>
> La detecció coherent multiplica el senyal per una referència síncrona amb l'oscil·lador i de la mateixa freqüència, i n'obté  $V_i\cos\varphi$: recupera el signe del mesurand en modulació DSB, rebutja les components en quadratura i redueix el soroll en un factor  $\sqrt{\frac{f_c}{BW_{\text{AC}}}}$. En la detecció homodina la referència és sinusoïdal i el producte dona un terme en contínua i un altre a  $2f_0$  que el filtre elimina; la freqüència de tall enfronta rebuig de soroll contra velocitat de seguiment, i atenua una interferència en la raó  $f_c/|f_{\text{int}}-f_0|$. La rectificació síncrona substitueix la referència per una ona quadrada i el multiplicador per un commutador, amb el mateix comportament davant la fase, a canvi de sensibilitat als harmònics imparells de  $f_0$. El mostreig síncron pren mostres en instants de fase coneguda: dues per cicle eliminen l'offset, quatre eliminen també la quadratura, i la taxa de mostreig la fixa la dinàmica del mesurand i no la portadora, de manera que el sub-mostreig és vàlid i permet promitjar mostres de la mateixa fase.

[← 4. Estimació de l'amplitud: mètodes no coherents](#estimació-de-lamplitud-mètodes-no-coherents)[6. Mètodes basats en oscil·ladors i mesura de freqüència →](#mètodes-basats-en-oscilladors-i-mesura-de-freqüència)

---

<!-- FIN CAPÍTULO: 05_Unitat8_Deteccio_coherent -->

---

<!-- INICIO CAPÍTULO: 06_Unitat8_Oscil_ladors_de_frequencia_variable -->

# Mètodes basats en oscil·ladors i mesura de freqüència

Sistemes de Mesura · **Unitat 8 — Condicionament de sensors en alterna** · Document 6 de 6

# Mètodes basats en oscil·ladors i mesura de freqüència

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Enunciar els avantatges i els inconvenients de codificar el mesurand en la freqüència.
> - Relacionar el període i la freqüència d'oscil·lació amb la capacitat del sensor en els tres oscil·ladors de relaxació.
> - Aplicar la condició de funcionament del monoestable en la conversió freqüència–tensió.
> - Quantificar el compromís entre resolució i velocitat de resposta en el comptatge digital de flancs.

Tots els mètodes anteriors comparteixen una arquitectura: un oscil·lador sinusoïdal excita un circuit lineal que converteix la impedància en una tensió alterna, i un convertidor alterna–contínua n'extreu l'amplitud. L'alternativa d'aquest document prescindeix del senyal sinusoïdal i de tota la cadena en alterna: **el sensor s'incorpora dins d'un oscil·lador** com a element que en fixa la freqüència, i estimar el mesurand es redueix a mesurar una freqüència.

## 1 Codificar el mesurand en la freqüència

Quan el mesurand canvia, la capacitat  $C(x)$  o la inductància  $L(x)$  del sensor varia i, amb ella, la freqüència d'oscil·lació  $f(x)$. La informació ja no viatja en l'amplitud sinó en la freqüència, una magnitud robusta i mesurable amb gran exactitud.

| Avantatge | Motiu |
|:--- |:--- |
| **Senzillesa del circuit** | L'arquitectura es redueix a un oscil·lador de relaxació i un circuit de mesura de freqüència. No calen amplificadors d'alterna, convertidors RMS, multiplicadors analògics ni filtres precisos: menys components, menys cost, menys superfície de placa i menys fonts d'error. |
| **Sortida digital directa** | La freqüència es mesura amb un comptador digital, sense cap convertidor analògic–digital, cosa que facilita la integració amb microcontroladors i FPGA. |
| **Immunitat a pertorbacions d'amplitud** | Com que la informació rau exclusivament en la freqüència, el soroll, les interferències i les variacions d'alimentació que afectin l'amplitud no tenen cap efecte sobre la mesura. És la característica més valorada en entorns industrials. |

Com a contrapartida, la relació entre freqüència i mesurand és en general **no lineal** —inversament proporcional a  $C(x)$  o a  $\sqrt{L(x)C}$ —, cosa que cal recollir en la calibració; el sistema és sensible a les toleràncies i a la deriva tèrmica dels components passius de temporització; i la mesura de freqüència requereix un temps d'integració que limita la velocitat de resposta.

## 2 Oscil·ladors de relaxació

Per raons de senzillesa no s'empren oscil·ladors sinusoïdals, que exigeixen realimentació més complexa i control d'amplitud, sinó **oscil·ladors de relaxació**: circuits no lineals que generen un senyal quadrat o de pols la freqüència del qual depèn del temps de càrrega i descàrrega d'un element reactiu a través d'una resistència. Quan la tensió al condensador arriba a un llindar superior el circuit commuta i inicia la descàrrega; en arribar al llindar inferior torna a commutar. La freqüència depèn de la constant de temps i, com que  $C$  és el sensor, depèn del mesurand.

![Oscil·lador astable basat en un temporitzador 555, amb el sensor capacitiu, la resistència de càrrega R1 i la de descàrrega R2.](assets/06_Unitat8_Oscil_ladors_de_frequencia_variable_img_1.png)

*Figura: Figura 8.42 Oscil·lador astable basat en el temporitzador 555.*

En la configuració **astable amb el 555**, el condensador es carrega des de  $V_{\text{CC}}/3$  fins a  $2V_{\text{CC}}/3$  a través de  $R_1+R_2$  amb la sortida a nivell alt, i es descarrega de  $2V_{\text{CC}}/3$  fins a  $V_{\text{CC}}/3$  a través de  $R_2$, mitjançant el transistor intern de descàrrega, amb la sortida a nivell baix. Els temps valen  $t_H = \ln 2\,(R_1+R_2)C$  i  $t_L = \ln 2\,R_2 C$, de manera que

$$
T = \ln 2\,(R_1 + 2R_2)\,C, \qquad f = \frac{1}{T} \approx \frac{1{,}44}{(R_1+2R_2)\,C} \qquad (8.46)
$$

El període és **directament proporcional** a la capacitat del sensor —amb  $C = C_0(1+x)$, proporcional a  $1+x$ — i la freqüència inversament proporcional. L'oscil·lació no té un cicle de treball del 50%

![Oscil·lador de relaxació amb amplificador operacional: realimentació positiva per fixar els llindars i condensador amb resistència de càrrega a l'entrada inversora.](assets/06_Unitat8_Oscil_ladors_de_frequencia_variable_img_2.png)

*Figura: Figura 8.43 Oscil·lador de relaxació amb amplificador operacional.*

Un operacional amb **realimentació positiva** actua com a comparador amb histèresi. Amb la sortida a  $+V_{\text{sat}}$, el condensador es carrega a través de  $R$  mentre les dues resistències de realimentació fixen el llindar superior  $V_{th+} = V_{\text{sat}}\,R_1/(R_1+R_2)$. En assolir-lo, la sortida commuta a  $-V_{\text{sat}}$, el llindar passa a  $-V_{th+}$  i el condensador es descarrega. Amb saturacions simètriques i totes les resistències iguals:

$$
f = \frac{1}{2\ln(3)\,R\,C} \qquad (8.47)
$$

Les tensions de saturació depenen de l'alimentació i del model d'operacional, però la simetria dels llindars dona de manera natural un cicle de treball del 50 %, cosa que simplifica el circuit de mesura posterior.

![Oscil·lador de relaxació construït amb portes inversores CMOS amb histèresi, una resistència i el condensador del sensor.](assets/06_Unitat8_Oscil_ladors_de_frequencia_variable_img_3.png)

*Figura: Figura 8.44 Oscil·lador basat en inversors CMOS.*

Amb **portes inversores CMOS amb histèresi** —inversors de Schmitt, com els del 74HC14— el funcionament és conceptualment idèntic i la freqüència ideal és la mateixa expressió. És la solució de menor cost i consum: un encapsulat de sis inversors val cèntims i consumeix corrents de l'ordre de µA en repòs, i tota la lògica del comptador pot anar al mateix microcontrolador, de manera que el condicionament extern queda reduït a la porta, la resistència i el sensor. Per contra, els llindars de la histèresi varien amb la tensió d'alimentació i amb la temperatura, cosa que introdueix errors sistemàtics que cal compensar per calibració si es vol alta exactitud.

## 3 Conversió freqüència–tensió

![Conversió freqüència a tensió amb un monoestable que genera polsos de durada fixa per cada flanc, seguit d'un filtre passa-baixes.](assets/06_Unitat8_Oscil_ladors_de_frequencia_variable_img_4.png)

*Figura: Figura 8.45 Conversió freqüència–tensió amb un monoestable.*

L'arquitectura analògica clàssica es basa en un **monoestable**: un biestable amb un únic estat estable que, en rebre un flanc d'activació, commuta a l'estat inestable i hi roman un temps precís  $\tau$  fixat per un condensador intern i una resistència externa, abans de tornar sol a l'estat estable. El resultat és un tren de polsos de durada i amplitud constants, separats pel període de l'oscil·lador. La condició de funcionament correcte és que el pols acabi abans que arribi el flanc següent, en tot el marge de mesura:

$$
\tau < T_{\min} = \frac{1}{f_{\max}} \qquad (8.48)
$$

Si es viola, el monoestable es bloqueja, perd flancs i produeix errors greus. Filtrant el tren de polsos amb un passa-baixes se n'obté el valor mitjà:

$$
V = V_{\text{DD}}\cdot\frac{\tau}{T} = V_{\text{DD}}\cdot\tau\cdot f \qquad (8.49)
$$

directament proporcional a la freqüència i, per tant, al mesurand. Amb  $V_{\text{DD}} = 5$  V i  $\tau = 100$  µs, una freqüència d'1 kHz dona un cicle de treball del 10 % i 0,5 V de sortida, i 5 kHz en donen el 50 % i 2,5 V. A mesura que la freqüència s'aproxima a  $1/\tau = 10$  kHz el cicle de treball tendeix al 100 % i la sortida a  $V_{\text{DD}}$; per damunt de  $f_{\max} = 1/\tau$  el circuit deixa de funcionar.

## 4 Comptatge digital de flancs

L'alternativa digital compta els flancs del senyal de l'oscil·lador durant un interval fixat  $T_{\text{gate}}$:

$$
N = f\cdot T_{\text{gate}} \qquad (8.50)
$$

La resolució és d'un flanc, cosa que correspon a una resolució en freqüència  $\Delta f = 1/T_{\text{gate}}$: amb un temps de porta d'1 s la resolució és d'1 Hz, i amb 10 s de 0,1 Hz. El compromís és immediat, perquè a major temps de porta menor velocitat de resposta —el mesurand no es pot actualitzar més d'una vegada cada  $T_{\text{gate}}$  segons.

El comptador pot ser un perifèric del propi microcontrolador de l'aplicació, en mode captura, i molts microcontroladors industrials incorporen mòduls que mesuren directament el període del senyal entrant amb la resolució temporal del seu rellotge. El comptatge digital és, doncs, la solució preferida sempre que hi hagi un microcontrolador al sistema, condició gairebé universal en instruments moderns; la conversió freqüència–tensió analògica queda per als casos en què cal una sortida analògica contínua sense microcontrolador, com en control analògic o en instruments on la sortida ha de ser una tensió estàndard de 0–10 V o un llaç de 4–20 mA.

> [!TIP] **Síntesi**
>
> Incorporant el sensor dins d'un oscil·lador de relaxació, el mesurand queda codificat en la freqüència: circuit senzill, sortida digital directa i immunitat total a les pertorbacions d'amplitud, a canvi d'una relació no lineal, de sensibilitat a les toleràncies i derives dels components de temporització i d'un temps d'integració que limita la velocitat. En el 555 astable el període val  $\ln 2\,(R_1+2R_2)C$  i el cicle de treball s'allunya del 50 %; amb operacional o amb inversors CMOS amb histèresi la freqüència val  $\frac{1}{2\ln 3\,RC}$  i el cicle de treball és simètric per construcció. Per llegir la freqüència, el monoestable seguit d'un filtre dona  $V = V_{\text{DD}}\tau f$  sempre que la durada del pols sigui menor que el període mínim, i el comptatge de flancs durant  $T_{\text{gate}}$  dona  $N = f\,T_{\text{gate}}$  amb resolució  $1/T_{\text{gate}}$, enfrontant resolució i velocitat de resposta.

[← 5. Detecció coherent: homodina, rectificació síncrona i mostreig síncron](#detecció-coherent-homodina-rectificació-síncrona-i-mostreig-síncron)

---

<!-- FIN CAPÍTULO: 06_Unitat8_Oscil_ladors_de_frequencia_variable -->

---

<!-- INICIO CAPÍTULO: 07_Unitat8_Entrenament -->

# Entrenament V/F · Unitat 8: Unitat 8

Sistemes de Mesura (230920) · ETSETB-UPC · **Unitat 8 — Unitat 8**

# Entrenament V/F

50 afirmacions repartides entre els sis documents de la unitat. Tot el càlcul es fa al vostre navegador: les respostes no s'envien enlloc.

**Simulacre cronometrat**
Les 50 afirmacions en ordre aleatori, amb cronòmetre i correcció al final. El temps es calcula a 30 s per afirmació, el ritme del qüestionari real.

**Entrenament lliure**
Les 50 afirmacions en l'ordre dels documents, sense rellotge i amb resposta immediata després de cada tria.

Les dues modalitats tenen tres respostes possibles: **Vertader**, **Fals** i **No ho sé**. Feu servir «No ho sé» quan realment no ho sabeu: al qüestionari real, endevinar penalitza.

Respostes: **0** / 50
Encerts: **0**
Corregir
Sortir

Corregir

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

---

## 🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)

> [!TIP] **Com utilitzar aquest material d'entrenament**
> Aquest banc conté **50 afirmacions clau** dissenyades per consolidar els conceptes de la unitat i preparar els qüestionaris d'avaluació continuada.
> Intenta respondre mentalment **Vertader (V)** o **Fals (F)** abans de desplegar la solució i la justificació tècnica.

### Qüestió 01
> 📌 **Afirmació:** *L'amplificador d'alterna pot atenuar l'offset de contínua i reduir-ne l'impacte sobre la mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En la característica passa-banda la contínua queda fortament atenuada i l'offset no s'amplifica.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 02
> 📌 **Afirmació:** *Els oscil·ladors de relaxació generen un senyal periòdic a partir de processos de càrrega i descàrrega.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un oscil·lador de relaxació commuta entre dos llindars carregant i descarregant l'element reactiu.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 03
> 📌 **Afirmació:** *En un sensor inductiu ideal, la reactància és positiva i proporcional a la freqüència i a la inductància.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Sensor inductiu ideal: X = 2πfL(x), positiva i proporcional a totes dues magnituds.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *Un convertidor RMS ideal proporciona una tensió positiva igual al valor eficaç de l'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La sortida del convertidor RMS és contínua i positiva per conveni, igual al valor eficaç.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *Reduir la freqüència de tall del filtre passa-baixes en detecció coherent redueix l'amplada de banda equivalent de soroll.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El soroll de sortida és proporcional a √fc: estrènyer el filtre estreny la banda de soroll.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 14
> 📌 **Afirmació:** *Perquè l'inversor capacitiu es comporti com un quocient de capacitats, la resistència de polarització ha de curtcircuitar el condensador a f0.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La condició és Rp ≫ 1/(2πf0C2): impedància molt major que la de C2, no un curtcircuit.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 18
> 📌 **Afirmació:** *Un sensor diferencial amb dues impedàncies que varien de manera complementària pot millorar la linealitat de la conversió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb dues capacitats complementàries la sortida és V(1+x)/2, estrictament lineal.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 20
> 📌 **Afirmació:** *La condició de sensor reactiu exigeix que els canvis relatius de la part imaginària dominin sobre els de la part real.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició: |ΔX|/|X0| ≫ |ΔR|/|R0| a la freqüència de treball.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *La resolució d'una mesura de freqüència per comptatge empitjora sempre quan s'allarga la finestra de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És a l'inrevés: la resolució val Δf = 1/Tgate i millora en allargar la finestra.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 31
> 📌 **Afirmació:** *La relació entre freqüència i mesurand en oscil·ladors de relaxació és sempre lineal sense calibració.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La relació és en general no lineal, inversament proporcional a C(x) o a √(L(x)C).*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 35
> 📌 **Afirmació:** *Els multiplicadors basats en logaritmes i antilogaritmes aprofiten que ln(x+y)=ln(x)+ln(y).*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La identitat que s'aprofita és ln(xy) = ln x + ln y, sobre el producte.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 43
> 📌 **Afirmació:** *Un detector coherent pot recuperar el signe del mesurand en una modulació DSB.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Retorna valor positiu per a x > 0 i negatiu per a x < 0, perquè la fase salta 180°.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 52
> 📌 **Afirmació:** *Treballar en alterna permet desplaçar la mesura fora de la zona on el soroll 1/f pot ser dominant.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Situant f0 per damunt de la freqüència característica, el soroll de l'amplificador és essencialment blanc.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 60
> 📌 **Afirmació:** *El centrat passa-banda es pot definir imposant que f0 sigui la mitjana geomètrica de les dues freqüències de tall a -3 dB.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *f0 = √(f−3dB,min · f−3dB,max): la condició de centrat és en escala logarítmica.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 62
> 📌 **Afirmació:** *En un amplificador inversor capacitiu, cal proporcionar un camí de contínua per als corrents de polarització.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Rp en paral·lel amb C2 proporciona el camí de contínua per als corrents de polarització.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 66
> 📌 **Afirmació:** *Multiplicar per una referència quadrada de valors +1 i -1 equival a calcular el valor RMS del senyal.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Multiplicar per ±1 canvia el signe cada semiperíode; el valor eficaç és una altra magnitud.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 73
> 📌 **Afirmació:** *En un sensor capacitiu ideal, la reactància és negativa i depèn inversament de la freqüència i de la capacitat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Sensor capacitiu ideal: X = −1/(2πfC(x)).*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 74
> 📌 **Afirmació:** *En una modulació DSB, l'envolupant conserva directament el signe del mesurand.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'envolupant val |A·x(t)|, sempre positiva: el signe queda a la fase.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 78
> 📌 **Afirmació:** *Un convertidor freqüència-tensió amb monoestable genera una sinusoide d'amplitud fixa per cada flanc d'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El monoestable genera polsos d'amplitud i durada fixos, no sinusoides.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 80
> 📌 **Afirmació:** *Un convertidor RMS suma de manera quadràtica les contribucions de senyal útil, soroll i interferències presents a l'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Vout = √(Vs² + Vint² + Vn²): les contribucions s'hi acumulen quadràticament.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 84
> 📌 **Afirmació:** *La capacitat d'entrada de l'operacional es pot ignorar sempre en sensors capacitius de baixa capacitat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cin domina en pujar la freqüència i forma un divisor amb la impedància de sortida anterior.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 91
> 📌 **Afirmació:** *En el 555 astable, si les resistències de càrrega i descàrrega són diferents, el cicle de treball pot diferir del 50%.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *tH = ln2(R1+R2)C i tL = ln2·R2C: si difereixen, el cicle de treball no és del 50 %.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 95
> 📌 **Afirmació:** *La referència quadrada de la rectificació síncrona conté únicament la component fonamental i cap harmònic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Conté harmònics imparells a 3f0, 5f0, 7f0… amb amplituds 4/(kπ).*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 96
> 📌 **Afirmació:** *Un convertidor RMS basat en rectificació dona el valor eficaç exacte de qualsevol forma d'ona sense calibració del factor de forma.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El factor de forma 1,11 només val per a sinusoides; amb distorsió harmònica la mesura és errònia.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 100
> 📌 **Afirmació:** *Els condensadors de desacoblament s'han de col·locar lluny del circuit integrat per augmentar la inductància de connexió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal col·locar-los el més a prop possible dels pins, a menys de 5 mm per damunt de 100 kHz.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 104
> 📌 **Afirmació:** *Els detectors no coherents necessiten dues referències en quadratura per funcionar.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Els mètodes no coherents no fan servir cap referència de fase.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 105
> 📌 **Afirmació:** *El filtre passa-baixes del detector homodí s'escull només per eliminar la component de contínua de sortida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Fixa alhora el rebuig de soroll, l'atenuació d'interferències i la velocitat de seguiment.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 106
> 📌 **Afirmació:** *En un divisor de tensió d'alterna, les impedàncies s'avaluen a la freqüència de treball.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Les resistències es substitueixen per impedàncies avaluades a la freqüència de treball.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 107
> 📌 **Afirmació:** *Per un amplificador d'alterna, convé que el GBW de l'operacional sigui molt superior a G multiplicat per la freqüència de tall superior.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La condició de disseny és GBW ≫ G·f−3dB,max.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 112
> 📌 **Afirmació:** *Els sensors inductius amb nucli ferromagnètic milloren indefinidament quan es porta la freqüència de treball a centenars de MHz.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Les pèrdues del nucli limiten la freqüència útil a uns pocs kHz.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 113
> 📌 **Afirmació:** *En un amplificador d'instrumentació d'alterna, la primera etapa pot proporcionar el guany diferencial principal en la banda de pas.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *A la banda de pas el guany total és (1 + 2R2/R1)·G, amb la primera etapa aportant-hi el gruix.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 117
> 📌 **Afirmació:** *En detecció coherent, una component en quadratura apareix amb la mateixa sortida que una component en fase.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La component en quadratura dona sortida nul·la; la component en fase, màxima.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 122
> 📌 **Afirmació:** *En sensors capacitius, una impedància de sortida molt alta fa el node de mesura immune a qualsevol acoblament extern.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És a l'inrevés: un node de 16 MΩ és extremament vulnerable a l'acoblament capacitiu.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 125
> 📌 **Afirmació:** *Els detectors de pic són sensibles als impulsos positius de soroll perquè poden carregar el condensador a un valor erroni.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un impuls positiu carrega el condensador fins a un pic fals que la descàrrega lenta manté.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 130
> 📌 **Afirmació:** *Fer l'amplada de banda més gran redueix simultàniament l'error de guany i el soroll total de sortida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Redueix l'error de guany però eixampla la banda equivalent de soroll: són objectius en conflicte.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 140
> 📌 **Afirmació:** *En un convertidor RMS de càlcul explícit, el senyal es diferencia dues vegades i després s'integra.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El càlcul explícit eleva al quadrat, filtra passa-baixes i pren l'arrel quadrada.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 141
> 📌 **Afirmació:** *En mostreig síncron, la taxa de mostreig necessària ve determinada per la dinàmica del mesurand, no per la reconstrucció de la portadora.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La condició de Nyquist s'aplica a l'envolupant, que varia molt més lentament que la portadora.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 150
> 📌 **Afirmació:** *La condició d'equilibri d'un pont d'alterna exigeix que les quatre impedàncies tinguin el mateix valor absolut.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'equilibri és una igualtat de quocients, Z2/Z1 = Z4/Z3, no d'impedàncies individuals.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 156
> 📌 **Afirmació:** *Una pista llarga d'alta impedància sempre redueix la capacitat paràsita del sistema.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Les pistes aporten de 0,5 a 5 pF per centímetre: com més llargues, més capacitat paràsita.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 161
> 📌 **Afirmació:** *Un detector de pic proporciona una tensió que segueix l'envolupant superior del senyal d'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició del detector d'envolupant.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 162
> 📌 **Afirmació:** *En un convertidor impedància-tensió lineal, la freqüència de sortida és proporcional al mesurand mentre l'amplitud roman fixa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En el condicionament lineal la freqüència és fixa a f0 i el mesurand va en l'amplitud.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 167
> 📌 **Afirmació:** *En un sensor capacitiu amb C_s=C0(1+x), el mòdul de la impedància augmenta quan x augmenta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Amb Cs = C0(1+x) la capacitat creix amb x i el mòdul de la impedància decreix.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 168
> 📌 **Afirmació:** *La mesura de freqüència pot fer-se comptant flancs durant una finestra temporal coneguda.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *N = f·Tgate: es compten flancs durant un interval fixat.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 171
> 📌 **Afirmació:** *En un pont passiu, la impedància de sortida pot provocar errors de càrrega en connectar l'etapa posterior.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Zout = jωL0/2 + R/2 pot ser prou gran per carregar l'etapa posterior.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 180
> 📌 **Afirmació:** *Un sensor reactiu ideal es modela com una resistència variable alimentada en contínua.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Es modela com una impedància complexa i cal excitar-lo en alterna.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 187
> 📌 **Afirmació:** *Amb dues mostres separades mig període es pot cancel·lar una component d'offset constant.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *vs(0) − vs(T0/2) elimina la component contínua comuna.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 190
> 📌 **Afirmació:** *Els amplificadors logarítmics amb díodes o transistors presenten dependència amb la temperatura de la unió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Tant el logarítmic com l'antilogarítmic depenen fortament de la temperatura de la unió.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 191
> 📌 **Afirmació:** *Si el mesurand varia amb el temps, el senyal modulat conserva una única ratlla espectral exactament a f0.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'espectre s'expandeix en bandes laterals a f0 ± fm.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 195
> 📌 **Afirmació:** *El condicionament lineal de sensors reactius elimina la necessitat d'un oscil·lador de referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El condicionament lineal necessita precisament un oscil·lador que exciti el sensor i doni la referència.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 197
> 📌 **Afirmació:** *En l'amplificador d'alterna no inversor, el guany de banda de pas ideal és 1+R2/R1.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *A la banda de pas el circuit és un no inversor clàssic, G = 1 + R2/R1.*

> **📚 Document de referència:** `Document 03`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | En la característica passa-banda la contínua queda fortament atenuada i l'offset no s'amplifica. | Document 03 |
| **02** | **V** | Un oscil·lador de relaxació commuta entre dos llindars carregant i descarregant l'element reactiu. | Document 06 |
| **03** | **V** | Sensor inductiu ideal: X = 2πfL(x), positiva i proporcional a totes dues magnituds. | Document 01 |
| **06** | **V** | La sortida del convertidor RMS és contínua i positiva per conveni, igual al valor eficaç. | Document 04 |
| **08** | **V** | El soroll de sortida és proporcional a √fc: estrènyer el filtre estreny la banda de soroll. | Document 05 |
| **14** | **F** | La condició és Rp ≫ 1/(2πf0C2): impedància molt major que la de C2, no un curtcircuit. | Document 02 |
| **18** | **V** | Amb dues capacitats complementàries la sortida és V(1+x)/2, estrictament lineal. | Document 02 |
| **20** | **V** | És la definició: \|ΔX\|/\|X0\| ≫ \|ΔR\|/\|R0\| a la freqüència de treball. | Document 01 |
| **27** | **F** | És a l'inrevés: la resolució val Δf = 1/Tgate i millora en allargar la finestra. | Document 06 |
| **31** | **F** | La relació és en general no lineal, inversament proporcional a C(x) o a √(L(x)C). | Document 06 |
| **35** | **F** | La identitat que s'aprofita és ln(xy) = ln x + ln y, sobre el producte. | Document 04 |
| **43** | **V** | Retorna valor positiu per a x > 0 i negatiu per a x < 0, perquè la fase salta 180°. | Document 05 |
| **52** | **V** | Situant f0 per damunt de la freqüència característica, el soroll de l'amplificador és essencialment blanc. | Document 01 |
| **60** | **V** | f0 = √(f−3dB,min · f−3dB,max): la condició de centrat és en escala logarítmica. | Document 03 |
| **62** | **V** | Rp en paral·lel amb C2 proporciona el camí de contínua per als corrents de polarització. | Document 02 |
| **66** | **F** | Multiplicar per ±1 canvia el signe cada semiperíode; el valor eficaç és una altra magnitud. | Document 05 |
| **73** | **V** | Sensor capacitiu ideal: X = −1/(2πfC(x)). | Document 01 |
| **74** | **F** | L'envolupant val \|A·x(t)\|, sempre positiva: el signe queda a la fase. | Document 04 |
| **78** | **F** | El monoestable genera polsos d'amplitud i durada fixos, no sinusoides. | Document 06 |
| **80** | **V** | Vout = √(Vs² + Vint² + Vn²): les contribucions s'hi acumulen quadràticament. | Document 04 |
| **84** | **F** | Cin domina en pujar la freqüència i forma un divisor amb la impedància de sortida anterior. | Document 03 |
| **91** | **V** | tH = ln2(R1+R2)C i tL = ln2·R2C: si difereixen, el cicle de treball no és del 50 %. | Document 06 |
| **95** | **F** | Conté harmònics imparells a 3f0, 5f0, 7f0… amb amplituds 4/(kπ). | Document 05 |
| **96** | **F** | El factor de forma 1,11 només val per a sinusoides; amb distorsió harmònica la mesura és errònia. | Document 04 |
| **100** | **F** | Cal col·locar-los el més a prop possible dels pins, a menys de 5 mm per damunt de 100 kHz. | Document 03 |
| **104** | **F** | Els mètodes no coherents no fan servir cap referència de fase. | Document 04 |
| **105** | **F** | Fixa alhora el rebuig de soroll, l'atenuació d'interferències i la velocitat de seguiment. | Document 05 |
| **106** | **V** | Les resistències es substitueixen per impedàncies avaluades a la freqüència de treball. | Document 02 |
| **107** | **V** | La condició de disseny és GBW ≫ G·f−3dB,max. | Document 03 |
| **112** | **F** | Les pèrdues del nucli limiten la freqüència útil a uns pocs kHz. | Document 01 |
| **113** | **V** | A la banda de pas el guany total és (1 + 2R2/R1)·G, amb la primera etapa aportant-hi el gruix. | Document 03 |
| **117** | **F** | La component en quadratura dona sortida nul·la; la component en fase, màxima. | Document 05 |
| **122** | **F** | És a l'inrevés: un node de 16 MΩ és extremament vulnerable a l'acoblament capacitiu. | Document 02 |
| **125** | **V** | Un impuls positiu carrega el condensador fins a un pic fals que la descàrrega lenta manté. | Document 04 |
| **130** | **F** | Redueix l'error de guany però eixampla la banda equivalent de soroll: són objectius en conflicte. | Document 03 |
| **140** | **F** | El càlcul explícit eleva al quadrat, filtra passa-baixes i pren l'arrel quadrada. | Document 04 |
| **141** | **V** | La condició de Nyquist s'aplica a l'envolupant, que varia molt més lentament que la portadora. | Document 05 |
| **150** | **F** | L'equilibri és una igualtat de quocients, Z2/Z1 = Z4/Z3, no d'impedàncies individuals. | Document 02 |
| **156** | **F** | Les pistes aporten de 0,5 a 5 pF per centímetre: com més llargues, més capacitat paràsita. | Document 03 |
| **161** | **V** | És la definició del detector d'envolupant. | Document 04 |
| **162** | **F** | En el condicionament lineal la freqüència és fixa a f0 i el mesurand va en l'amplitud. | Document 01 |
| **167** | **F** | Amb Cs = C0(1+x) la capacitat creix amb x i el mòdul de la impedància decreix. | Document 01 |
| **168** | **V** | N = f·Tgate: es compten flancs durant un interval fixat. | Document 06 |
| **171** | **V** | Zout = jωL0/2 + R/2 pot ser prou gran per carregar l'etapa posterior. | Document 02 |
| **180** | **F** | Es modela com una impedància complexa i cal excitar-lo en alterna. | Document 01 |
| **187** | **V** | vs(0) − vs(T0/2) elimina la component contínua comuna. | Document 05 |
| **190** | **V** | Tant el logarítmic com l'antilogarítmic depenen fortament de la temperatura de la unió. | Document 04 |
| **191** | **F** | L'espectre s'expandeix en bandes laterals a f0 ± fm. | Document 03 |
| **195** | **F** | El condicionament lineal necessita precisament un oscil·lador que exciti el sensor i doni la referència. | Document 01 |
| **197** | **V** | A la banda de pas el circuit és un no inversor clàssic, G = 1 + R2/R1. | Document 03 |

<!-- FIN CAPÍTULO: 07_Unitat8_Entrenament -->

---

## 🎙️ Guía de Estudio y Audio Overview (Podcast) para NotebookLM

Para aprovechar al máximo este Cuaderno Maestro en **Google NotebookLM**, recomendamos personalizar el **Audio Overview** (Podcast educativo) con las siguientes directrices:

- **Rol y Tono:** Conversación dinámica y didáctica entre dos profesores de la UPC especializados en instrumentación electrónica y sistemas de medida.
- **Enfoque conceptual:** Explicar el trasfondo físico y matemático de las derivas, el ruido, las incertidumbres y los transductores, utilizando metáforas del mundo real en vez de limitarse a leer ecuaciones.
- **Punto de tensión pedagógica:** Analizar una de las preguntas complejas del banco de autoevaluación (marcada como Falsa por una sutil trampa técnica) y discutir por qué suele inducir a error en el examen.
- **Síntesis final:** Resumen de las 3 reglas de oro de diseño electrónico expuestas a lo largo de este tema.

---

## 📐 Formulario Resumen de Ecuaciones

| Nº / Ref | Expresión Matemática |
| :---: | :--- |
| **(8.1)** | $Z(f,x) = R(f,x) + j\,X(f,x)$ |
| **(8.2)** | $\frac{\|\Delta X_f(x)\|}{\|X_0\|} \gg \frac{\|\Delta R_f(x)\|}{\|R_0\|}$ |
| **(8.3)** | $Z_\mathrm{cap}(f,x) = \frac{R_d}{1 + j\,2\pi f R_d C(x)}$ |
| **(8.4)** | $f_\mathrm{res} = \frac{1}{2\pi\sqrt{L\,C_s(x)}}$ |
| **(8.5)** | $V_o = V\,\frac{Z_2}{Z_1+Z_2}$ |
| **(8.6)** | $V_o = V\,\frac{1+x}{2+x}$ |
| **(8.7)** | $V_o = V\,\frac{1+x}{2}$ |
| **(8.8)** | $\|Z_\mathrm{out}\| = \frac{1}{\omega \cdot 2C_0}$ |
| **(8.9)** | $H(j\omega) = -\,\frac{j\omega R_p C_1}{1 + j\omega R_p C_2}$ |
| **(8.10)** | $R_p \gg \frac{1}{2\pi f_0 C_2}$ |
| **(8.11)** | $V_\mathrm{sat} - V_{o,\max} > R_p\left(\frac{I_B + I_{\text{OS}}}{2}\right)$ |
| **(8.12)** | $V_\mathrm{diff} = V\left(\frac{Z_2}{Z_1+Z_2} - \frac{Z_4}{Z_3+Z_4}\right)$ |
| **(8.13)** | $\left.\frac{Z_2}{Z_1}\right\|_{x=0} = \left.\frac{Z_4}{Z_3}\right\|_{x=0}$ |
| **(8.14)** | $V_\mathrm{diff} = V\left(\frac{1+x}{2} - \frac{1}{2}\right) = V\,\frac{x}{2}$ |
| **(8.15)** | $Z_\mathrm{out} = \frac{j\omega L_0}{2} + \frac{R}{2}$ |
| **(8.16)** | $V_o = \frac{V}{Z_1}\cdot\frac{Z_3 Z_1 - Z_4 Z_2}{Z_3+Z_4}$ |
| **(8.17)** | $Z_3 Z_1 = Z_4 Z_2 \Leftrightarrow \left.\frac{Z_4}{Z_3}\right\|_{x=0} = \left.\frac{Z_1}{Z_2}\right\|_{x=0}$ |
| **(8.18)** | $f_{\min} = f_0 - f_{m,\max}, \qquad f_{\max} = f_0 + f_{m,\max}$ |
| **(8.19)** | $\|H(f_{\min})\| \geq G(1-\delta), \qquad \|H(f_{\max})\| \geq G(1-\delta)$ |
| **(8.20)** | $f_0 = \sqrt{f_{-3\mathrm{dB},\min}\cdot f_{-3\mathrm{dB},\max}}$ |
| **(8.21)** | $BW = f_{-3\mathrm{dB},\max} - f_{-3\mathrm{dB},\min} \geq 2\,k\,f_{m,\max}$ |
| **(8.22)** | $f_{-3\mathrm{dB},\min} = \frac{1}{2\pi R_1 C_1}, \qquad f_{-3\mathrm{dB},\max} = \frac{1}{2\pi R_2 C_2}$ |
| **(8.23)** | $G_\mathrm{total} = \left(1 + \frac{2R_2}{R_1}\right)\cdot G$ |
| **(8.24)** | $GBW \gg G\cdot f_{-3\mathrm{dB},\max}$ |
| **(8.25)** | $SR \geq 2\pi f_0\, G\, V_{in,\mathrm{pic}}$ |
| **(8.26)** | $\|Z_{\text{in}}(f)\| \approx \frac{1}{2\pi f\, C_{\text{in}}}$ |
| **(8.27)** | $v(t) = A(x)\cos(2\pi f_0 t + \varphi_0), \qquad A(x) > 0\ \ \forall x$ |
| **(8.28)** | $V_\mathrm{rms} = \sqrt{\frac{1}{T}\int_0^T v^2(t)\,dt}$ |
| **(8.29)** | $V_\mathrm{out} = \sqrt{V_s^2 + V_{\text{int}}^2 + V_n^2}$ |
| **(8.30)** | $V_\mathrm{out} = \overline{\left(\frac{v^2(t)}{V_\mathrm{out}}\right)} \Rightarrow V_\mathrm{out}^2 = \overline{v^2(t)} \Rightarrow V_\mathrm{out} = \sqrt{\overline{v^2(t)}}$ |
| **(8.31)** | $V_\mathrm{rms} = \frac{\pi}{2\sqrt{2}}\,\overline{\|v(t)\|} \approx 1{,}11\cdot\overline{\|v(t)\|}$ |
| **(8.32)** | $V_\mathrm{out}(t) = \frac{V_x(t)\cdot V_y(t)}{K}$ |
| **(8.33)** | $V_\mathrm{out} = -V_F \approx -\eta\,V_T \ln\!\left(\frac{V_{\text{in}}}{I_S R}\right)$ |
| **(8.34)** | $V_\mathrm{out} = I_C R_1 \approx R_1 I_{\text{ES}}\, e^{-V_i/V_T}$ |
| **(8.35)** | $\Delta I_c = I_Y\cdot\frac{\Delta I_x}{I_x}$ |
| **(8.36)** | $\Delta V \approx \frac{V_p T_0}{\tau} = \frac{V_p}{f_0\,\tau}$ |
| **(8.37)** | $\frac{1}{2\pi f_{m,\max}} \geq \tau \gg \frac{1}{f_0}$ |
| **(8.38)** | $v_i(t) = V_i \cos(2\pi f_0 t + \varphi)$ |
| **(8.39)** | $v_i\cdot v_{\text{ref}} = \frac{V_i V_r}{2}\left[\cos\varphi + \cos(4\pi f_0 t + \varphi)\right]$ |
| **(8.40)** | $V_\mathrm{out} = \frac{V_i V_r}{2}\cos\varphi$ |
| **(8.41)** | $\|H(f_{\text{int}}-f_0)\| \approx \frac{f_c}{\|f_{\text{int}}-f_0\|} \qquad \mathrm{per a } \|f_{\text{int}}-f_0\| \gg f_c$ |
| **(8.42)** | $v_i(t_n) = V_i\cos(2\pi n + 2\pi f_0\tau_0 + \varphi) = V_i\cos(2\pi f_0\tau_0 + \varphi)$ |
| **(8.43)** | $v_s(0) - v_s(T_0/2) = 2V_i\cos\varphi + 2B\sin\varphi$ |
| **(8.44)** | $v_s(T_0/4) - v_s(3T_0/4) = -2V_i\sin\varphi + 2B\cos\varphi$ |
| **(8.45)** | $f_s \geq 2\,f_{m,\max}$ |
| **(8.46)** | $T = \ln 2\,(R_1 + 2R_2)\,C, \qquad f = \frac{1}{T} \approx \frac{1{,}44}{(R_1+2R_2)\,C}$ |
| **(8.47)** | $f = \frac{1}{2\ln(3)\,R\,C}$ |
| **(8.48)** | $\tau < T_{\min} = \frac{1}{f_{\max}}$ |
| **(8.49)** | $V = V_{\text{DD}}\cdot\frac{\tau}{T} = V_{\text{DD}}\cdot\tau\cdot f$ |
| **(8.50)** | $N = f\cdot T_{\text{gate}}$ |