# 📚 Cuaderno Maestro: Tema 6

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 6` | 📄 **Capítulos incluidos:** 8  
> 📅 **Generado:** 2026-09-11 19:10

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 6 — Condicionament de sensors en contínua · Lectura prèvia](#unitat-6-condicionament-de-sensors-en-contínua-lectura-prèvia)
2. [La cadena de condicionament en contínua](#la-cadena-de-condicionament-en-contínua)
   - [1 Sensors de sortida en contínua](#1-sensors-de-sortida-en-contínua)
   - [2 L'objectiu: adequar el senyal a l'ADC](#2-lobjectiu-adequar-el-senyal-a-ladc)
   - [3 Blocs de la cadena](#3-blocs-de-la-cadena)
   - [4 AFE monolítics comercials](#4-afe-monolítics-comercials)
   - [5 Model del sensor i objecte de la mesura](#5-model-del-sensor-i-objecte-de-la-mesura)
   - [6 Els compromisos que cal tancar](#6-els-compromisos-que-cal-tancar)
3. [Conversió resistència–tensió: cables, fonts de corrent, divisor i pont](#conversió-resistènciatensió-cables-fonts-de-corrent-divisor-i-pont)
   - [1 Resistència dels cables: mesura a 2, 3 i 4 fils](#1-resistència-dels-cables-mesura-a-2-3-i-4-fils)
   - [2 Conversió amb font de corrent](#2-conversió-amb-font-de-corrent)
   - [3 Divisor de tensió](#3-divisor-de-tensió)
   - [4 El pont de Wheatstone](#4-el-pont-de-wheatstone)
   - [5 Ponts amb diversos sensors](#5-ponts-amb-diversos-sensors)
4. [Conversió corrent–tensió i amplificadors diferencials](#conversió-correnttensió-i-amplificadors-diferencials)
   - [1 Models de sensor amb sortida en corrent](#1-models-de-sensor-amb-sortida-en-corrent)
   - [2 Resistència de càrrega](#2-resistència-de-càrrega)
   - [3 Amplificador de transimpedància](#3-amplificador-de-transimpedància)
   - [4 L'amplificador diferencial](#4-lamplificador-diferencial)
   - [5 Impedàncies d'entrada i efecte de càrrega](#5-impedàncies-dentrada-i-efecte-de-càrrega)
5. [Amplificadors d'instrumentació](#amplificadors-dinstrumentació)
   - [1 L'estructura de tres amplificadors operacionals](#1-lestructura-de-tres-amplificadors-operacionals)
   - [2 Especificacions que cal llegir](#2-especificacions-que-cal-llegir)
   - [3 Un cas concret: l'INA317](#3-un-cas-concret-lina317)
   - [4 Criteris de selecció](#4-criteris-de-selecció)
6. [Interruptors, multiplexors analògics i PGA](#interruptors-multiplexors-analògics-i-pga)
   - [1 Interruptor ideal i interruptor real](#1-interruptor-ideal-i-interruptor-real)
   - [2 De MOSFET a CMOS](#2-de-mosfet-a-cmos)
   - [3 Errors en contínua](#3-errors-en-contínua)
   - [4 Limitacions en alterna i en commutació](#4-limitacions-en-alterna-i-en-commutació)
   - [5 Multiplexors i ús pràctic](#5-multiplexors-i-ús-pràctic)
   - [6 Amplificadors de guany programable](#6-amplificadors-de-guany-programable)
7. [Referències de tensió i de corrent i mesures ratiomètriques](#referències-de-tensió-i-de-corrent-i-mesures-ratiomètriques)
   - [1 Solucions elementals i les seves limitacions](#1-solucions-elementals-i-les-seves-limitacions)
   - [2 Referències sèrie i shunt](#2-referències-sèrie-i-shunt)
   - [3 Especificacions](#3-especificacions)
   - [4 Mesures ratiomètriques](#4-mesures-ratiomètriques)
8. [Entrenament V/F · Unitat 6: Condicionament de sensors en contínua](#entrenament-vf-unitat-6-condicionament-de-sensors-en-contínua)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_Unitat6_Index -->

# Unitat 6 — Condicionament de sensors en contínua · Lectura prèvia

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 6 — Condicionament de sensors en contínua

Materials de lectura prèvia · dedicació total estimada: 61 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents **substitueixen els apunts** i contenen tot el que cal per preparar la unitat.

Llegeix els sis documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor.

### [1. La cadena de condicionament en contínua](#la-cadena-de-condicionament-en-contínua)

Què vol dir sortida en contínua i quins criteris de disseny en deriven: precisió DC, deriva, soroll de baixa freqüència i autoescalfament. L'objectiu del condicionador en termes del marge dinàmic de l'ADC. Blocs de la cadena: excitació, conversió, front end analògic, multiplexatge, filtratge i conversió A/D. AFE monolítics comercials. Model R=R0(1+alfa·x) i per què interessa la variació i no el valor absolut. Contribucions a la incertesa global i interaccions entre blocs.

*⏱️ Dedicació estimada: 9 min*

### [2. Conversió resistència–tensió: cables, fonts de corrent, divisor i pont](#conversió-resistènciatensió-cables-fonts-de-corrent-divisor-i-pont)

Biaix de la resistència dels cables i mesura a 2, 3 i 4 fils, amb els criteris de tria. Conversió amb font de corrent: sensibilitat I·R0·alfa i la limitació de la component contínua gran; dues fonts aparellades per anul·lar-la. Divisor de tensió: no-linealitat, sensibilitat màxima Vref·alfa/4 amb R=R0 i el compromís amb l'autoescalfament. Pont de Wheatstone: equilibri, paràmetre k i el seu efecte simultani sobre sensibilitat, linealitat, consum i mode comú; mig pont i pont complet.

*⏱️ Dedicació estimada: 11 min*

### [3. Conversió corrent–tensió i amplificadors diferencials](#conversió-correnttensió-i-amplificadors-diferencials)

Models de sensor de corrent amb offset i proporcional. Resistència de càrrega: quan serveix i per què el soroll tèrmic creix amb l'arrel de R. Amplificador de transimpedància, massa virtual i Vout=Ip·Rf, amb els corrents de polarització com a limitació. Amplificador diferencial de quatre resistències: guany diferencial i en mode comú, la condició R1/R2=R3/R4 i un exemple resolt de combinació de CMRR. Impedàncies d'entrada i efecte de càrrega sobre el pont.

*⏱️ Dedicació estimada: 12 min*

### [4. Amplificadors d'instrumentació](#amplificadors-dinstrumentació)

Què resol respecte de l'amplificador diferencial simple. Estructura de tres amplificadors operacionals, guany G1=1+2Rf/Rg ajustable amb una sola resistència, i la impedància d'entrada elevada de la primera etapa no inversora. Especificacions DC: exactitud i no-linealitat de guany, offset referit a l'entrada, corrents de polarització, CMRR, PSRR, derives tèrmiques, soroll i producte guany–amplada de banda. L'INA317 com a cas concret i els criteris de selecció.

*⏱️ Dedicació estimada: 8 min*

### [5. Interruptors, multiplexors analògics i PGA](#interruptors-multiplexors-analògics-i-pga)

Interruptor ideal enfront del real: Ron, fuites i capacitats paràsites. Per què el CMOS combina canal N i canal P. Errors en contínua amb l'interruptor tancat i obert, i la resistència de càrrega de compromís. Limitacions en commutació: pol i zero, injecció de càrrega, crosstalk i temps d'establiment. Especificacions dels multiplexors i calibratge per canal. PGA i VGA: error de guany introduït per Ron amb exemple resolt i l'arquitectura que l'elimina.

*⏱️ Dedicació estimada: 13 min*

### [6. Referències de tensió i de corrent i mesures ratiomètriques](#referències-de-tensió-i-de-corrent-i-mesures-ratiomètriques)

Per què l'estabilitat de l'excitació limita l'exactitud global. Díodes, Zener i referències bandgap: la combinació de coeficients tèrmics oposats. Referències sèrie i shunt. Especificacions: exactitud inicial, deriva tèrmica, soroll, estabilitat a llarg termini i la distinció entre regulació de línia i de càrrega. Referències de corrent amb resistència de sensat i el rang de tensió de càrrega. Mesura ratiomètrica: la cancel·lació de l'excitació, les seves condicions i què no cancel·la.

*⏱️ Dedicació estimada: 8 min*

### [✓. Entrenament V/F](#entrenament-vf-unitat-6-condicionament-de-sensors-en-contínua)

50 afirmacions repartides entre els sis documents, en dues modalitats: simulacre en ordre aleatori amb cronòmetre i correcció al final, i entrenament lliure en l'ordre dels documents amb resposta immediata. Cada afirmació porta justificació i enllaç al document que la sustenta.

*⏱️ Simulacre cronometrat al ritme del qüestionari real*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

<!-- FIN CAPÍTULO: 00_Unitat6_Index -->

---

<!-- INICIO CAPÍTULO: 01_Unitat6_Cadena_de_condicionament_en_continua -->

# La cadena de condicionament en contínua

Sistemes de Mesura · **Unitat 6 — Condicionament de sensors en contínua** · Document 1 de 6

# La cadena de condicionament en contínua

Dedicació estimada: 9 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Delimitar què és un sensor de sortida en contínua i quins criteris de disseny en deriven.
> - Enunciar l'objectiu del condicionador en termes del marge dinàmic de l'ADC.
> - Identificar els blocs de la cadena de condicionament i la funció de cadascun.
> - Escriure el model lineal d'un sensor resistiu i justificar per què interessa  $\Delta R$
> i no  $R_0$
>.
> - Enumerar les contribucions a la incertesa global i els compromisos que les lliguen.

Aquesta unitat és la primera d'un bloc de tres dedicats al condicionament de sensors: el conjunt de circuits que transformen la sortida d'un sensor en un senyal apte per a l'adquisició digital. Aquí es tracta el cas de **sortida en contínua**. Els sensors reactius i el condicionament en alterna es veuen a les unitats 7 i 8, i els condicionadors singulars per a sensors de sensibilitat molt baixa, a la unitat 10.

## 1 Sensors de sortida en contínua

Un sensor té **sortida en contínua** quan la magnitud elèctrica que proporciona —tensió, corrent o resistència equivalent— té un contingut predominantment de baixa freqüència: des de senyals estrictament constants fins a variacions per sota de desenes o centenes d'hertzs. Si el mesurand es manté constant, la sortida elèctrica roman idealment constant; quan varia, ho fa sense components ràpides que exigeixin gran amplada de banda al condicionador.

Aquesta delimitació determina el criteri de disseny. En contínua el disseny se centra en la **precisió DC, la deriva, el soroll de baixa freqüència i l'autoescalfament**, no en la resposta en freqüència a l'escala de kHz o MHz. Quan el sensor genera senyal altern, o quan es decideix excitar-lo en alterna per motius metrològics —sensor reactiu, reducció de derives, detecció síncrona—, els criteris són radicalment diferents: amplada de banda, fase, resposta freqüencial d'amplificadors i filtres i limitacions en freqüència dels interruptors. El camp d'aquesta unitat inclou els sensors resistius excitats amb tensió o corrent continus —galgues extensomètriques, ponts de pressió, RTD, termistors NTC, LDR— i els sensors modelables com a fonts de tensió o de corrent continu.

## 2 L'objectiu: adequar el senyal a l'ADC

El condicionament en contínua té com a objectiu final proporcionar una **tensió analògica** que variï amb el mesurand de manera que, quan aquest recorre el seu rang d'interès, la tensió de sortida s'acosti tant com sigui possible al marge dinàmic utilitzable de l'ADC. D'això en deriven tres conseqüències immediates:

- La cadena ha de **convertir corrent o resistència a tensió**, perquè la majoria d'ADC treballen amb entrades de tensió.
- El **guany global** s'ha de dimensionar perquè el senyal ocupi una fracció elevada del rang de l'ADC, evitant saturacions però reduint el nombre de bits perduts. Un guany més gran no millora sempre la mesura: també amplifica offset, soroll i deriva, i pot excedir el rang admissible.
- Cal repartir les **incerteses** entre sensor, electrònica i ADC perquè cap bloc degradi innecessàriament la precisió global.

## 3 Blocs de la cadena

![Diagrama de blocs de la cadena de condicionament: transductor o pont, excitació, front end analògic amb amplificador d'instrumentació i PGA, filtre, ADC amb referència, i domini digital](assets/01_Unitat6_Cadena_de_condicionament_en_continua_img_1.png)

*Figura: Figura 6.1 Cadena de condicionament de sensors en contínua.*

La **primera etapa de precondicionament** transforma el paràmetre elèctric del sensor en una tensió contínua, generalment diferencial. Fa servir una **excitació** derivada d'una referència de tensió amb amplificadors operacionals, o generada per un convertidor digital a analògic. Al sensor se li injecta un corrent associat a aquesta excitació, o bé es munta en un pont de resistències o en un divisor de tensió. L'excitació ha de ser **tan estable com sigui possible**: qualsevol canvi en ella s'interpreta com un canvi del mesurand. A més, tots els components d'aquesta etapa poden derivar amb la temperatura, i per això no és estrany monitorar la temperatura del condicionador per corregir-ne les derives.

La segona etapa, el **front end analògic** (AFE) pròpiament dit, té al nucli un amplificador diferencial d'altes prestacions: un circuit que amplifica la diferència entre dos terminals i rebutja la component comuna a tots dos. Habitualment és un **amplificador d'instrumentació** (IA), d'impedància d'entrada molt elevada, per limitar l'efecte de càrrega sobre el sensor. Si l'amplificador es comparteix entre diversos canals de mesura, sol ser un **amplificador de guany programable** (PGA), i la selecció de canal es fa amb **multiplexors analògics**. Sigui quin sigui l'amplificador, es construeix sobre amplificadors operacionals amb limitacions en contínua que cal considerar; a més, el **rebuig del mode comú** no depèn només de l'amplificador sinó també de disposar de resistències d'alta precisió.

Un cop amplificada la tensió, la cadena la filtra, la digitalitza i hi opera; aquests darrers blocs no són objectiu del curs.

## 4 AFE monolítics comercials

![Diagrames de blocs de dos condicionadors comercials: a dalt un AFE d'Analog Devices amb ADC sigma-delta de 24 bits i PGA; a baix el PGA302 de Texas Instruments per a ponts de resistències](assets/01_Unitat6_Cadena_de_condicionament_en_continua_img_2.png)

*Figura: Figura 6.2 Dos condicionadors en contínua comercials: un AFE d'alta integració d'Analog Devices (a dalt) i el PGA302 de Texas Instruments (a baix).*

L'**AD4111** d'Analog Devices supera els 10 dòlars en compres de més de 1000 unitats: descartat en equips de consum, atractiu en sèries curtes amb mesures acurades i desenvolupament ràpid. La part digital arrenca amb un **ADC sigma-delta de 24 bits**, amb processament sincronitzat per rellotge extern i comunicació SPI. L'analògica admet RTD a dos, tres o quatre fils, llaços 4 mA – 20 mA, entrades de ±10 V i termoparells; excita els sensors amb fonts de corrent o de tensió, fa caure els corrents sobre resistències de sensat internes o externes i incorpora diagnòstic per comparació amb tensions generades internament. El nucli que condiciona les prestacions és un **PGA**, envoltat d'interruptors que adrecen els senyals.

El **PGA302** de Texas Instruments és més barat —poc més de 2 dòlars— i menys versàtil: està dedicat a sensors en **ponts de resistències**. Porta un ADC de 16 bits, compensació de derives amb sensor de temperatura intern o extern, i sortida digital (I²C o OWI) o analògica per un DAC de 14 bits, filtre passa-baixes i amplificador per quatre que compensa la diferència de bits entre ADC i DAC. Proporciona l'alimentació del pont, en mesura la sortida diferencial i compensa els errors de zero de l'amplificador. Com que la referència interna pot derivar, hi fa servir una **mesura ratiomètrica**: la mateixa tensió que excita el pont serveix de referència a l'ADC.

## 5 Model del sensor i objecte de la mesura

Per a molts sensors resistius de mesura —galgues, RTD, termistors en rang reduït, LDR en zones acotades— la dependència amb la magnitud física  $x$
 s'escriu com

$$
R_x(x) = R_0\,f(x) \approx R_0\,(1+\alpha x) \qquad (6.1)
$$

on  $R_0$
 és la resistència per al valor de referència  $x=0$
 i  $\alpha$
 és la **sensibilitat relativa**. La linealització val quan el marge de  $x$
 és prou petit o quan  $f(x)$
 és suau; fora d'aquestes condicions introdueix un **error de model** que forma part de la incertesa i que pot superar la contribució de moltes altres fonts. Cal, doncs, avaluar-lo explícitament i, si cal, recórrer a models de grau superior, a linealització analògica o a correcció digital.

En la majoria d'aplicacions l'objectiu **no** és conèixer  $R_x$
 en valor absolut, sinó mesurar petits canvis  $\Delta R = R_x - R_0$
, sovint de l'ordre de  $10^{-3}R_0$
 o menys. D'això en surten tres conseqüències de disseny:

- El condicionador s'ha de dimensionar per ser sensible a  $\Delta R$
   mantenint-se robust davant la incertesa en  $R_0$
   —tolerància del sensor, deriva, dispersió entre dispositius—, que no desapareix pel fet de connectar-lo a un circuit.
- Interessen les topologies que **anul·len la sortida per a  $x=0$**, perquè permeten aplicar guanys elevats sense saturar amb la component contínua de fons.
- L'ús de **més d'un sensor** permet combinacions que eliminen el terme associat a  $R_0$
, reforcen la dependència amb  $\Delta R$
   i compensen pertorbacions; alternativament, es pot mesurar directament la pertorbació i corregir-la per càlcul.

## 6 Els compromisos que cal tancar

Qualsevol circuit que mesuri una resistència hi ha de fer circular corrent o imposar-hi tensió, de manera que el sensor dissipa  $P = I^2R_x$
 o  $P = V^2/R_x$
 i s'escalfa. L'**autoescalfament** és un error sistemàtic, crític quan el sensor mesura precisament la temperatura del medi, i pot alterar les propietats mecàniques de l'estructura on s'adhereix una galga. Limitar el corrent o la tensió d'acord amb el fabricant, encara que costi sensibilitat, forma part del disseny.

La **sensibilitat efectiva** no depèn només del sensor: també del guany del condicionador i del rang de l'ADC. Massa baixa, dominen el soroll i l'error de quantització; massa alta, apareixen saturacions o un ús ineficient del rang. La incertesa total combina la del **sensor** —no-linealitat i dispersió entre dispositius—, la del **condicionador** —errors de guany, biaixos, soroll, efectes de càrrega, resistències paràsites, autoescalfament, derives tèrmiques— i la de l'**ADC** —resolució i no-linealitat integral. Els blocs interactuen, i per això la revisió final del disseny ha de considerar la càrrega que un amplificador imposa a un pont, la propagació d'offsets, les derives de les referències i els errors de commutació. Una mesura **traçable** exigeix precisament això: relacionar cada bloc electrònic amb el seu efecte sobre la incertesa.

La integració en un AFE monolític no dispensa de revisar les especificacions d'offset, soroll, guany i deriva. I el calibratge, que corregeix el que és estable, no elimina les derives tèrmiques posteriors; en un sistema multicanal, cada canal pot requerir les seves pròpies constants.

> [!TIP] **Síntesi**
>
> Un sensor de sortida en contínua té contingut de baixa freqüència, cosa que trasllada el disseny cap a la precisió DC, la deriva, el soroll de baixa freqüència i l'autoescalfament. L'objectiu del condicionador és lliurar a l'ADC una tensió que ocupi una fracció elevada del seu marge dinàmic sense saturar-lo, la qual cosa exigeix convertir resistència o corrent a tensió i dimensionar el guany. La cadena consta d'una etapa d'excitació i conversió, un front end analògic amb amplificador diferencial o d'instrumentació, multiplexors i PGA si hi ha diversos canals, i finalment filtratge i conversió A/D. Els sensors resistius es modelen com  $R_x = R_0(1+\alpha x)$
> i el que interessa mesurar és  $\Delta R$
>, no  $R_0$
>. La incertesa global suma sensor, condicionador i ADC, i les interaccions entre blocs.

[2. Conversió resistència–tensió: cables, fonts de corrent, divisor i pont →](#conversió-resistènciatensió-cables-fonts-de-corrent-divisor-i-pont)

---

<!-- FIN CAPÍTULO: 01_Unitat6_Cadena_de_condicionament_en_continua -->

---

<!-- INICIO CAPÍTULO: 02_Unitat6_Conversio_resistencia_tensio -->

# Conversió resistència–tensió: cables, fonts de corrent, divisor i pont

Sistemes de Mesura · **Unitat 6 — Condicionament de sensors en contínua** · Document 2 de 6

# Conversió resistència–tensió: cables, fonts de corrent, divisor i pont

Dedicació estimada: 11 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Quantificar el biaix que la resistència dels cables introdueix i decidir entre 2, 3 i 4 fils.
> - Calcular la sensibilitat de la conversió amb font de corrent i explicar-ne la limitació dominant.
> - Justificar per què dues fonts aparellades anul·len la component contínua de fons.
> - Deduir la sensibilitat del divisor de tensió i localitzar-ne el màxim.
> - Analitzar el pont de Wheatstone amb el paràmetre  $k$
> i el compromís entre sensibilitat, linealitat, consum i mode comú.

La conversió de resistència a tensió es fa amb un dels tres mètodes clàssics de mesura de resistència: **injectar un corrent** conegut i mesurar la caiguda de tensió, **muntar el sensor en un divisor de tensió** amb una font de tensió i una resistència fixa, o **incorporar-lo a un pont de resistències**, que fa servir dos divisors i lliura una sortida diferencial. El pont és, per la seva versatilitat, el més emprat en mesures de precisió.

> [!WARNING] **Convenció de notació**
>
> S'escriu  $R_x = R_0(1+\alpha x)$
> quan interessa mantenir explícita la sensibilitat relativa  $\alpha$
> respecte de la magnitud física, i  $R_x = R_0(1+x)$
> quan  $x$
> designa **directament la variació relativa de resistència**, que és la forma que s'adopta en l'anàlisi dels ponts. Els resultats són els mateixos amb el canvi  $x \rightarrow \alpha x$
>.

## 1 Resistència dels cables: mesura a 2, 3 i 4 fils

Quan el sensor és lluny de l'instrument, la resistència vista no és només la seva, sinó la suma amb les resistències de cables, connectors i soldadures del camí del corrent:  $R_{\text{mesura}} = R_x + R_{w,equiv}$
, on  $R_{w,equiv}$
 suma tots els conductors pels quals circula corrent, exclòs el sensor. És un **biaix sistemàtic** que es propaga al mesurand a través del model  $R_x(x)$
. Encara que en valor absolut siguin fraccions d'ohm o uns quants ohms, l'impacte és gran quan el sensor té un **valor baix**: galgues de 120 Ω o 350 Ω, Pt-100 amb cables llargs on uns quants ohms equivalen a desenes de graus aparents, o termistors on una petita variació s'interpreta com un canvi considerable de temperatura. **Com més baixa és la resistència nominal, més crític és l'error de cable**.

![Esquema de mesura a 2 fils: font de corrent i voltímetre connectats al sensor pel mateix parell de conductors, cadascun amb resistència Rw](assets/02_Unitat6_Conversio_resistencia_tensio_img_1.png)

*Figura: Figura 6.3 Mesura a 2 fils: el mateix parell de conductors injecta el corrent i serveix per mesurar la tensió.*

En la **mesura a 2 fils**, el corrent  $I$
 circula per les tres resistències en sèrie i la tensió als terminals externs val

$$
V_{\text{mes}} = I\,(R + 2R_w) \qquad (6.2)
$$

$$
R_{\text{mes}} = \frac{V_{\text{mes}}}{I} = R + 2R_w \qquad (6.3)
$$

L'error és exactament  $2R_w$
: les dues caigudes de cable **se sumen**, no es compensen per simetria. Es pot mitigar amb calibratge —mesurar en curtcircuit i restar—, però només val si la resistència dels cables es manté estable amb el temps i amb la temperatura, cosa que no sempre es pot garantir.

![Esquema de mesura a 4 fils: un parell de conductors injecta el corrent i un segon parell independent, d'alta impedància, mesura la tensió als terminals del sensor](assets/02_Unitat6_Conversio_resistencia_tensio_img_2.png)

*Figura: Figura 6.4 Mesura a 4 fils: camí de corrent i camí de mesura de tensió separats.*

En la **mesura a 4 fils** un parell de cables injecta el corrent i un altre parell, independent, mesura la tensió. La clau és que l'instrument de tensió té una **impedància d'entrada molt elevada**: pel parell de mesura circula corrent pràcticament nul i la caiguda en aquests cables és negligible. Aleshores

$$
R_{\text{mes}} = \frac{V}{I} = R \qquad (6.4)
$$

i l'error de cable s'elimina a la pràctica sempre que la impedància d'entrada del voltímetre sigui molt superior a  $R_w$
. És l'estàndard en metrologia i en sistemes industrials d'alta precisió, sobretot amb sensors llunyans, incertesa exigent en valor absolut o cables sotmesos a condicions ambientals variables.

La **mesura a 3 fils** és el compromís habitual en RTD muntats en pont: un extrem del sensor es connecta amb dos cables i l'altre amb un tercer, de manera que l'efecte dels cables es reparteix entre dues branques del pont. No l'elimina —no equival a una mesura ideal a 4 fils en qualsevol condició de cablejat i simetria—, però el redueix a nivells acceptables en moltes aplicacions industrials. L'elecció depèn de quatre factors, no només del cost del cablejat:

| Factor | Efecte |
|:--- |:--- |
| Valor nominal del sensor | Com més baix, més crític; centenars d'ohms o menys demanen 3 o 4 fils |
| Longitud i secció dels cables | Cables llargs o prims tenen més resistència; distàncies grans demanen 3 o 4 fils |
| Exactitud requerida | Metrologia i control crític porten naturalment cap als 4 fils |
| Cost i complexitat | Amb requisits moderats i calibratge in situ, 2 fils pot ser acceptable |

## 2 Conversió amb font de corrent

![Font de corrent que travessa el sensor resistiu, amb un voltímetre mesurant la tensió als seus borns](assets/02_Unitat6_Conversio_resistencia_tensio_img_3.png)

*Figura: Figura 6.5 Conversió resistència–tensió amb una font de corrent.*

El mètode més directe injecta un corrent conegut i mesura la tensió que apareix als borns del sensor. Aplicant la llei d'Ohm amb el model lineal,

$$
V_{\text{out}}(x) = I\,R_x(x) = I\,R_0\,(1+\alpha x) \qquad (6.5)
$$

$$
S_V = \frac{\partial V_{\text{out}}}{\partial x} = I\,R_0\,\alpha \qquad (6.6)
$$

La sortida és **proporcional** a la resistència del sensor. La sensibilitat creix amb  $I$
, amb  $R_0$
 i amb  $\alpha$
, però cada increment té el seu preu: més corrent implica més autoescalfament, un  $R_0$
 molt elevat pot limitar el rang útil de tensió i augmentar el soroll tèrmic, i  $\alpha$
 ve fixat pel sensor i pel rang de treball. Es combina habitualment amb la tècnica de 4 fils.

La limitació dominant apareix quan les variacions relatives de  $R_x$
 són molt petites, com en galgues o RTD en rangs estrets. Aleshores  $V_{\text{out}}$
 té una **component contínua gran**  $V_0 = I R_0$
 amb una variació  $\Delta V = I R_0 \alpha \Delta x$
 molt petita superposada. Qualsevol incertesa relativa del corrent —tolerància de la font, deriva, soroll— es tradueix directament en una incertesa proporcional sobre  $V_{\text{out}}$
 que es confon amb un canvi de  $x$
.

![Dues fonts de corrent aparellades: una alimenta el sensor Rx i l'altra una resistència de referència R, amb mesura de la diferència de tensió entre els dos nodes](assets/02_Unitat6_Conversio_resistencia_tensio_img_4.png)

*Figura: Figura 6.6 Conversió resistència–tensió amb dues fonts de corrent aparellades.*

La solució és fer servir **dues fonts de corrent aparellades**:  $I_1$
 alimenta el sensor  $R_x$
 i  $I_2 \approx I_1 = I$
 alimenta una resistència de referència  $R$
 de valor fix, sovint similar a  $R_0$
. La sortida útil és la diferència entre les dues branques:

$$
V_3 - V_4 \approx I\,(R_x - R) \qquad (6.7)
$$

La sortida és proporcional a la **diferència**  $R_x - R$
 i és **nul·la** per a  $x=0$
 quan  $R = R_0$
. En mesura a 2 fils, si els cables són del mateix tipus i longitud  $(R_{w1}\approx R_{w2})$
, els seus termes es compensen parcialment:

$$
V_1 - V_2 \approx I\,(R_{w1} + R_x - R - R_{w2}) \approx I\,(R_x - R) \qquad (6.8)
$$

L'avantatge és que la component contínua gran desapareix *sense* restar digitalment valors grans, cosa que permet aplicar guanys elevats sense saturar i millora la resolució efectiva. El mètode de fonts de corrent, en qualsevol de les dues versions, encaixa bé amb sensors de variació relativa gran —termistors NTC, LDR, sensors de posició de marge ampli— i amb integrats que ofereixen fonts programables. Per a variacions relatives petites (galgues, RTD de precisió) sol ser preferible el pont.

## 3 Divisor de tensió

![Divisor de tensió format per una resistència fixa R i el sensor Rx en sèrie, alimentat per Vref a través de dos cables amb resistències Rw1 i Rw2](assets/02_Unitat6_Conversio_resistencia_tensio_img_5.png)

*Figura: Figura 6.7 Conversió resistència–tensió amb divisor de tensió.*

$$
V_{\text{out}} = V_{\text{ref}}\,\frac{R_x}{R+R_x} \qquad (6.9)
$$

$$
V_{\text{out}}(x) = V_{\text{ref}}\,\frac{R_0(1+\alpha x)}{R+R_0(1+\alpha x)} \qquad (6.10)
$$

La relació és **clarament no lineal** en  $x$
, que apareix al numerador i al denominador. La no-linealitat es pot acceptar, restringir a una zona on la corba s'aproximi bé per una recta, o corregir amb topologies passives o digitalment. Derivant,

$$
S = \frac{\partial V_{\text{out}}}{\partial x} = V_{\text{ref}}\cdot\frac{R_0\,\alpha\,R}{\left(R+R_0(1+\alpha x)\right)^2} \qquad (6.11)
$$

que **depèn de  $x$** i decreix a mesura que  $R_x$
 s'allunya del valor òptim. Per a  $x$
 petit la sensibilitat és màxima quan  $R = R_0$
, és a dir, quan la resistència fixa iguala la del sensor al punt de referència:

$$
S_{\max} = V_{\text{ref}}\cdot\frac{\alpha}{4} \qquad (6.12)
$$

La potència dissipada pel sensor val

$$
P_x \approx \frac{V_{\text{ref}}^2\,R_x}{(R+R_x)^2} \qquad (6.13)
$$

i quan  $R \approx R_x \approx R_0$
 és de l'ordre de  $V_{\text{ref}}^2/(4R_0)$
. Augmentar  $V_{\text{ref}}$
 augmenta la sensibilitat *i* l'autoescalfament: el compromís és directe. A la pràctica es tria  $R$
 perquè el sensor treballi en zona segura de potència, la sensibilitat sigui adequada a l'ADC i la no-linealitat sigui compatible amb l'exactitud requerida o amb la correcció digital; amb termistors NTC,  $R$
 es pot escollir per maximitzar la linealitat al voltant d'una temperatura d'interès.

Amb cables llargs,  $V_{\text{out}}$
 depèn també de  $R_{w1}$
 i  $R_{w2}$
. Una millora senzilla és mesurar amb dos cables addicionals sense corrent la **tensió real** que arriba al divisor: així s'elimina l'efecte de les caigudes de cable i es compensa una  $V_{\text{ref}}$
 mal regulada. La relació continua essent no lineal: conèixer la tensió aplicada no substitueix el model del sensor.

## 4 El pont de Wheatstone

Tant la font de corrent simple com el divisor generen una component contínua significativa per a  $x=0$
, sobre la qual se superposa una variació petita. Els **ponts de resistències** permeten dissenyar la sortida perquè sigui nul·la al valor de referència i creixi amb  $x$
. Això permet aplicar guanys elevats sense saturar, redueix la sensibilitat a errors absoluts de l'excitació i facilita integrar diversos sensors. És la topologia més utilitzada a la primera etapa de condicionament de sensors resistius de precisió: galgues, cèl·lules de càrrega, transductors de pressió.

![Pont de Wheatstone amb quatre resistències R1, R2, R3, R4, alimentat per Vcc, amb sortida diferencial entre els nodes centrals; R4 és el sensor R0(1+x)](assets/02_Unitat6_Conversio_resistencia_tensio_img_6.png)

*Figura: Figura 6.8 Pont de Wheatstone: dos divisors de tensió en paral·lel amb sortida diferencial entre els nodes centrals.*

Són **dos divisors de tensió en paral·lel** alimentats per  $V_{\text{cc}}$
, amb sortida **diferencial** entre els punts centrals. Una o diverses resistències són sensors; a la figura,  $R_4 = R_0(1+x)$
.

$$
V_- = V_{\text{cc}}\,\frac{R_3}{R_1+R_3} \qquad (6.14)
$$

$$
V_+ = V_{\text{cc}}\,\frac{R_4}{R_2+R_4} \qquad (6.15)
$$

$$
V_{\text{out}} = V_+ - V_- = V_{\text{cc}}\left(\frac{R_4}{R_2+R_4}-\frac{R_3}{R_1+R_3}\right) \qquad (6.16)
$$

La **condició d'equilibri** a  $x=0$
 és la igualtat de les relacions de divisió de les dues branques, que operant es redueix a

$$
\frac{R_2}{R_0} = \frac{R_1}{R_3} \qquad (6.17)
$$

Es tria  $R_2 = k\,R_0$
, cosa que obliga  $R_1 = k\,R_3$
, i en molts dissenys  $R_3 = R_0$
. Amb  $R_4 = R_0(1+x)$
 s'obté

$$
V_{\text{out}} = V_{\text{cc}}\cdot\frac{k\,x}{(k+1+x)\,(k+1)} \qquad (6.18)
$$

que **no és lineal** amb  $x$
. Un únic paràmetre,  $k$
, controla simultàniament la sensibilitat, el corrent de consum, la tensió en mode comú i la linealitat. Per a  $k+1 \gg x$
 i després per a  $k \gg 1$
:

$$
V_{\text{out}} \approx V_{\text{cc}}\cdot\frac{k\,x}{(k+1)^2} \qquad (6.19)
$$

$$
V_{\text{out}} \approx V_{\text{cc}}\cdot\frac{x}{k} \qquad (6.20)
$$

El corrent per branca en condicions quasi equilibrades i la tensió en **mode comú** a la sortida —el valor mitjà dels dos nodes— valen

$$
I \approx \frac{V_{\text{cc}}}{(k+1)\,R_0} \qquad (6.21)
$$

$$
V_{\text{CM}} \approx \frac{V_{\text{cc}}}{k+1} \qquad (6.22)
$$

Una tensió en mode comú elevada es converteix en **error residual** proporcional a  $V_{\text{CM}}/CMRR$
 quan l'amplificador que llegeix el pont té un rebuig del mode comú finit, cosa que sempre passa. Dissenyar el pont perquè el mode comú sigui petit és, doncs, una estratègia directa per reduir l'error de zero del sistema.

Comparant l'expressió exacta amb l'aproximació lineal s'obté l'**error de no-linealitat**:

$$
E_l = V_{\text{cc}}\cdot\frac{k\,x^2}{(k+1)^2\,(k+1+x)} \qquad (6.23)
$$

$$
E_l \approx V_{\text{cc}}\cdot\frac{x^2}{k^2} \qquad (k \gg 1+x) \qquad (6.24)
$$

és a dir, l'error de no-linealitat **decau** aproximadament com  $\frac{1}{k}^2$
. Multiplicar  $k$
 per 10 el divideix per 100, al preu de dividir per 10 la sensibilitat, però també dividint per 10 el consum de corrent i la tensió en mode comú. Aquest és el compromís central del disseny del pont:

| Magnitud | En augmentar  $k$ | Conseqüència |
|:--- |:--- |:--- |
| Sensibilitat | disminueix  $(\propto \frac{1}{k})$ | Cal més guany posterior |
| Error de no-linealitat | disminueix  $(\propto \frac{1}{k}^2)$ | Millor linealitat |
| Corrent de consum | disminueix | Menys autoescalfament del sensor |
| Tensió en mode comú | disminueix | Menys error per CMRR finit |

Sensibilitat i linealitat, per tant, **no milloren alhora**. En aplicacions on la linealitat és crítica —cèl·lules de càrrega per a pesatge legalment controlat— convé un  $k$
 elevat, compensant la menor sensibilitat amb un amplificador de guany alt i soroll baix.

## 5 Ponts amb diversos sensors

Un pont pot incorporar més d'un element sensible, amb dos objectius. El primer és **augmentar la sensibilitat**: dos sensors idèntics sotmesos al mateix mesurand però en branques adequades dupliquen o multipliquen la variació de tensió per unitat de  $x$
 (mig pont, pont complet). El segon és **compensar pertorbacions**: una galga activa mesura la deformació d'interès i una galga compensadora, a la mateixa temperatura però no sotmesa a la força, permet cancel·lar la deriva tèrmica. La disposició simètrica fa que el mesurand i la pertorbació comuna entrin amb **signes diferents** a la sortida diferencial: aquí és on rau la compensació.

En un **pont complet** simètric amb deformacions oposades,  $R_1 = R_4 = R_0(1+x)$
 i  $R_2 = R_3 = R_0(1-x)$
, les contribucions útils se sumen mentre les variacions uniformes de temperatura es cancel·len, i la sortida esdevé **exactament lineal**:

$$
V_{\text{out}} = V_{\text{cc}}\cdot x \qquad (6.25)
$$

És la configuració habitual de transductors de pressió i cèl·lules de càrrega amb quatre galgues sobre un diafragma. La compensació per simetria no substitueix el calibratge del sistema, però elimina una part de l'error que cap calibratge estàtic corregiria.

> [!TIP] **Síntesi**
>
> La resistència dels cables suma un biaix  $2R_w$
> en mesura a 2 fils, tant més greu com més baixa és la resistència del sensor; els 4 fils l'eliminen separant el camí de corrent del de tensió, i els 3 fils són el compromís habitual en RTD i ponts. La font de corrent dona  $V_{\text{out}}=IR_x$
> amb sensibilitat  $IR_0\alpha$
>, però arrossega una component contínua gran; dues fonts aparellades la cancel·len donant  $I(R_x-R)$
>. El divisor és no lineal, amb sensibilitat màxima  $V_{\text{ref}}\alpha/4$
> quan  $R=R_0$
>, i lliga sensibilitat amb autoescalfament a través de  $V_{\text{ref}}$
>. El pont equilibra dos divisors per anul·lar la sortida al punt de referència; el paràmetre  $k$
> baixa alhora sensibilitat, no-linealitat (com  $\frac{1}{k}^2$
> ), consum i mode comú. Amb pont complet i deformacions oposades la resposta és  $V_{\text{out}}=V_{\text{cc}}x$
>, lineal i amb compensació tèrmica.

[← 1. La cadena de condicionament en contínua](#la-cadena-de-condicionament-en-contínua)[3. Conversió corrent–tensió i amplificadors diferencials →](#conversió-correnttensió-i-amplificadors-diferencials)

---

<!-- FIN CAPÍTULO: 02_Unitat6_Conversio_resistencia_tensio -->

---

<!-- INICIO CAPÍTULO: 03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials -->

# Conversió corrent–tensió i amplificadors diferencials

Sistemes de Mesura · **Unitat 6 — Condicionament de sensors en contínua** · Document 3 de 6

# Conversió corrent–tensió i amplificadors diferencials

Dedicació estimada: 12 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir els dos models de sensor amb sortida en corrent i les seves conseqüències.
> - Decidir entre resistència de càrrega i amplificador de transimpedància segons el rang de corrent.
> - Deduir el guany diferencial i el guany en mode comú de l'amplificador diferencial de quatre resistències.
> - Combinar el CMRR de les resistències amb el de l'amplificador operacional.
> - Avaluar l'efecte de càrrega d'un amplificador diferencial sobre un pont.

## 1 Models de sensor amb sortida en corrent

Un sensor que lliura un corrent continu proporcional al mesurand admet dos models. El primer és un **model amb offset**, anàleg al dels sensors resistius:

$$
I_x = I_0\,(1+\beta x) \qquad (6.26)
$$

on  $I_0$
 és el corrent per a  $x=0$
 i  $\beta$
 la sensibilitat relativa. Descriu sensors amb un corrent de fons no nul: un sensor de llum amb corrent de foscor, o un transductor amb llaç 4–20 mA que lliura 4 mA al valor mínim del rang i 20 mA al màxim. El segon és el **model proporcional**:

$$
I_x = I_0\cdot x \qquad (6.27)
$$

amb corrent estrictament nul a  $x=0$
, com en fotodíodes o fototransistors en zona lineal: si no hi ha llum, no hi ha corrent. En tots dos casos, l'objectiu del condicionador és transformar el corrent en una tensió amplificable i digitalitzable, preservant la relació amb  $x$
 tan fidelment com sigui possible.

## 2 Resistència de càrrega

![Sensor de corrent connectat a una resistència de càrrega fixa R, amb mesura de la tensió als seus borns](assets/03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials_img_1.png)

*Figura: Figura 6.9 Conversió corrent–tensió amb una resistència fixa.*

La manera més senzilla és fer circular el corrent per una resistència coneguda i mesurar-ne la caiguda:  $V = I_x R = I_0 R(1+\beta x)$
, amb sensibilitat

$$
\frac{\partial V}{\partial x} = I_0\,R\,\beta \qquad (6.28)
$$

Quan el corrent és petit —pA o fA en alguns fotodíodes o sensors electroquímics— cal una resistència molt elevada: un fotodíode de 10 pA que hagi de donar 1 mV demana  $R$
 de l'ordre de 100 MΩ. Valors així porten dos problemes simultanis, tots dos de signe contrari al que se sol suposar:

- **Efecte de càrrega.** La impedància d'entrada de l'etapa posterior pot no ser prou gran respecte de  $R$
: part del corrent es deriva cap a l'instrument en comptes de caure sobre  $R$
, i la lectura queda falsejada.
- **Soroll tèrmic.** El soroll generat per la mateixa resistència **creix** amb l'arrel quadrada del seu valor, i pot arribar a limitar la relació senyal–soroll:

$$
e_n = \sqrt{4\,k_B\,T\,R\,\Delta f} \qquad (6.29)
$$

La resistència de càrrega simple, per tant, només és pràctica quan el corrent és prou gran —microamperes o més— per treballar amb valors moderats, de kΩ a centenars de kΩ.

## 3 Amplificador de transimpedància

![Amplificador de transimpedància: amplificador operacional amb resistència de realimentació Rf entre sortida i entrada inversora, sensor de corrent connectat a l'entrada inversora i entrada no inversora a massa](assets/03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials_img_2.png)

*Figura: Figura 6.10 Amplificador de transimpedància.*

És un amplificador operacional amb una resistència de realimentació  $R_f$
 entre la sortida i l'entrada inversora. El sensor es connecta a l'entrada inversora; la no inversora va a massa o a una tensió de referència. Com que el guany en llaç obert és molt gran, la tensió entre les dues entrades és pràcticament nul·la —**curtcircuit virtual**— i el node d'entrada es manté **virtualment a massa** sigui quin sigui el corrent que hi arribi. Tot el corrent del sensor ha de circular per  $R_f$
, perquè no pot entrar a l'amplificador ideal. Això elimina el problema de càrrega i permet resistències de realimentació molt elevades sense degradar la impedància vista pel sensor.

$$
V_{\text{out}} = I_p\,R_f \qquad (6.30)
$$

La sortida és **proporcional** al corrent i a  $R_f$
, que actua com a guany de transimpedància en V/A. El valor de  $R_f$
 es tria per adaptar el rang de corrent del sensor al marge de tensió de l'etapa posterior; per a corrents de pA o fA pot arribar a GΩ o TΩ.

Les limitacions són les de l'amplificador operacional. Els **corrents de polarització** —picoamperes en entrades FET, nanoamperes en bipolars— circulen per  $R_f$
 i generen una tensió d'offset que es confon amb el senyal: el curtcircuit virtual no els cancel·la. S'hi afegeixen la tensió d'offset, les derives tèrmiques, el soroll i el guany en llaç obert finit. Situar-les totes per sota de les variacions de corrent a mesurar exigeix amplificadors molt més propers a l'ideal que els de propòsit general; per això el cas de corrents molt petits es reprèn a la **unitat 10**, dedicada als condicionadors singulars. És la topologia de referència per a fotodíodes, sensors electroquímics i fotodetectors en instrumentació biomèdica.

## 4 L'amplificador diferencial

Els ponts i molts sensors resistius lliuren una **sortida diferencial**: dos terminals amb una diferència de tensió típicament de mV o menys, superposada a un mode comú que pot ser de diversos volts. Cal amplificar la component diferencial fins al marge de l'ADC i rebutjar la comuna, que no conté informació. Els amplificadors unipolars referits a massa no serveixen: no rebutgen prou el mode comú i introdueixen errors si les entrades no comparteixen exactament el mateix potencial de massa.

![Amplificador diferencial clàssic amb un amplificador operacional i quatre resistències R1, R2, R3 i R4](assets/03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials_img_3.png)

*Figura: Figura 6.11 Amplificador diferencial amb un amplificador operacional i quatre resistències.*

L'entrada inversora rep  $V_1$
 a través de  $R_1$
, amb  $R_2$
 de realimentació; la no inversora rep  $V_2$
 a través de  $R_3$
, amb  $R_4$
 a massa. Definim

$$
V_d = V_2 - V_1 \qquad (6.31)
$$

$$
V_c = \frac{V_2+V_1}{2} \qquad (6.32)
$$

Resolent per superposició i agrupant termes,

$$
V_o = G_d\,V_d + G_c\,V_c \qquad (6.33)
$$

$$
G_d = \frac{1}{2}\left[\frac{R_2}{R_1}+\left(1+\frac{R_2}{R_1}\right)\frac{R_4}{R_4+R_3}\right] \qquad (6.34)
$$

$$
G_c = \left(1+\frac{R_2}{R_1}\right)\frac{R_4}{R_4+R_3}-\frac{R_2}{R_1} \qquad (6.35)
$$

Idealment voldríem  $G_d$
 finit i  $G_c = 0$
. Imposant  $G_c \approx 0$
 s'arriba a la condició clau:

$$
\frac{R_1}{R_2} = \frac{R_3}{R_4} \qquad (6.36)
$$

Les dues parelles de resistències han d'estar **escalades amb la mateixa relació**: no serveix qualsevol combinació. Quan es compleix, el terme en  $V_c$
 desapareix del model ideal i el guany diferencial queda fixat pel quocient de resistències:

$$
G_d = \frac{R_2}{R_1} \qquad (6.37)
$$

A la pràctica cal resistències de tolerància molt baixa, o bé un integrat amb resistències ajustades conjuntament. La majoria d'amplificadors diferencials comercials es dissenyen amb  $R_1=R_3=R$
 i  $R_2=R_4=G\,R$
.

El desajustament residual dona un CMRR finit associat a les resistències,  $CMRR_R = G_d/G_c$
, infinit només si (6.36) es compleix exactament. Però l'amplificador operacional també té un CMRR finit propi: el mode comú que arriba a les seves entrades s'atenua per  $CMRR_{\text{AO}}$
 i passa a la sortida multiplicat pel guany diferencial. Els dos efectes es combinen com

$$
CMRR_{\text{total}} = \frac{CMRR_R\cdot CMRR_{\text{AO}}}{CMRR_R+CMRR_{\text{AO}}} \qquad (6.38)
$$

> [!WARNING] **Unitats**
>
> L'expressió (6.38) exigeix els CMRR en **unitats lineals**. Els valors en dB no es poden sumar ni multiplicar directament: cal convertir-los a lineal amb  $CMRR = 10^{\,CMRR_{\text{dB}}/20}$
>, combinar-los i tornar a dB al final.

> [!EXAMPLE] **Exemple resolt: CMRR d'un amplificador diferencial amb resistències discretes**
>
> Amb un amplificador operacional de  $CMRR_{\text{AO}} = 90\ \mathrm{dB}$
> i resistències  $R_1 = 1\ \mathrm{k}\Omega$
>,  $R_2 = 10\ \mathrm{k}\Omega$
>,  $R_3 = 999\ \Omega$
>,  $R_4 = 10\ \mathrm{k}\Omega$
>, quin CMRR efectiu s'obté?
>
> 1. Guanys. Amb  $R_2/R_1 = 10$
> i  $R_4/(R_4+R_3) = 10/10{,}999$
>, les expressions (6.34) i (6.35) donen  $G_d = 10{,}0005$
> i  $G_c = 9{,}09\cdot10^{-4}$
>.
> 2. CMRR de les resistències.  $CMRR_R = G_d/G_c = 11\,000$
>, és a dir 80,83 dB. Un desajustament d'un sol ohm en  $R_3$
> ja limita el conjunt.
> 3. Combinació.  $CMRR_{\text{AO}} = 90\ \mathrm{dB} = 31\,623$
> en lineal. Per (6.38),  $CMRR_{\text{total}} = 11\,000\cdot31\,623/(11\,000+31\,623) = 8\,161$
>, és a dir **78,2 dB**.
> 4. Lectura. El resultat queda per sota del pitjor dels dos i el domina el **desajustament de resistències**, no l'amplificador. Amb resistències discretes de l'1 % o del 0,1 % això és el cas habitual; en aplicacions exigents s'utilitzen amplificadors diferencials integrats amb resistències ajustades per làser.

## 5 Impedàncies d'entrada i efecte de càrrega

En un amplificador diferencial integrat el fabricant no sol donar els valors de les resistències internes, sinó les **impedàncies d'entrada** en mode diferencial i en mode comú. Amb  $R_1=R_3=R$
 i  $R_2=R_4=G\,R$
 resulten

$$
Z_d = 2\,R \qquad (6.39)
$$

$$
Z_c = \frac{R\,(G+1)}{2} \qquad (6.40)
$$

Són valors **finits i moderats**: l'entrada d'un amplificador diferencial no és de corrent nul, encara que l'amplificador operacional ho sigui, perquè les resistències hi són. L'INA2143 té guany 10 o 0,1 segons la connexió, CMRR típic de 96 dB a baixa freqüència (mínim 86 dB), offset referit a l'entrada de 100 µV, soroll d'1 µV pic a pic entre 0,1 Hz i 10 Hz i amplada de banda de 150 kHz. Excel·lent en tot, excepte que les impedàncies d'entrada moderades poden causar efecte de càrrega.

![Pont de Wheatstone connectat a l'entrada d'un amplificador diferencial de quatre resistències](assets/03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials_img_4.png)

*Figura: Figura 6.12 Pont de Wheatstone connectat a un amplificador diferencial.*

Part del corrent que hauria de circular pel pont es deriva cap a les resistències d'entrada de l'amplificador. Per analitzar-ho, cada branca del pont es reemplaça pel seu **equivalent Thevenin**: una font de tensió en sèrie amb la resistència vista des del node central.

![Model equivalent del pont substituït per dos equivalents Thevenin connectats a les resistències d'entrada de l'amplificador diferencial](assets/03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials_img_5.png)

*Figura: Figura 6.13 Model equivalent per a l'estudi de l'efecte de càrrega.*

Apareixen dos efectes indesitjats. El primer és que, fins i tot amb  $x$
 nul·la, el guany diferencial no és  $G$
 sinó

$$
G_{\text{load}} = \frac{G\cdot R}{R+k\,R_0/(k+1)} = \frac{G}{1+\frac{k\,R_0}{R\,(k+1)}} < G \qquad (6.41)
$$

és a dir, la càrrega **redueix** el guany efectiu. El segon és que, per a  $x$
 diferent de zero, apareix una diferència entre les resistències vistes per les dues entrades que **creix amb el mesurand**: el CMRR es degrada a mesura que augmenta  $x$
. En aplicacions exigents cal assegurar que la impedància diferencial de l'amplificador sigui molt superior a la resistència Thevenin de qualsevol branca del pont. L'alternativa —més cara, però que estalvia el problema i sovint ofereix guany ajustable— és l'amplificador d'instrumentació.

> [!TIP] **Síntesi**
>
> Els sensors de corrent es modelen amb offset,  $I_0(1+\beta x)$
>, o de manera proporcional,  $I_0 x$
>. La resistència de càrrega serveix amb corrents de µA o més; per sota, la resistència necessària carrega el node i el seu soroll tèrmic creix com  $\sqrt{R}$
>, i cal l'amplificador de transimpedància, que manté l'entrada a massa virtual i dona  $V_{\text{out}}=I_pR_f$
>, amb els corrents de polarització com a limitació dominant. L'amplificador diferencial de quatre resistències amplifica  $V_d=V_2-V_1$
> i rebutja  $V_c=(V_1+V_2)/2$
>; el rebuig ideal exigeix  $R_1/R_2=R_3/R_4$
>, i aleshores  $G_d=R_2/R_1$
>. El CMRR real combina el de les resistències i el de l'amplificador operacional en unitats lineals, i sol quedar dominat pel desajustament resistiu. Les impedàncies d'entrada  $Z_d=2R$
> i  $Z_c=R(G+1)/2$
> són finites i carreguen el pont, reduint el guany efectiu i degradant el CMRR a mesura que creix el mesurand.

[← 2. Conversió resistència–tensió: cables, fonts de corrent, divisor i pont](#conversió-resistènciatensió-cables-fonts-de-corrent-divisor-i-pont)[4. Amplificadors d'instrumentació →](#amplificadors-dinstrumentació)

---

<!-- FIN CAPÍTULO: 03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials -->

---

<!-- INICIO CAPÍTULO: 04_Unitat6_Amplificadors_dinstrumentacio -->

# Amplificadors d'instrumentació

Sistemes de Mesura · **Unitat 6 — Condicionament de sensors en contínua** · Document 4 de 6

# Amplificadors d'instrumentació

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar què resol l'amplificador d'instrumentació respecte de l'amplificador diferencial simple.
> - Calcular el guany de l'estructura de tres amplificadors operacionals a partir de  $R_g$
>.
> - Interpretar les especificacions DC d'un amplificador d'instrumentació i el seu efecte sobre la mesura.
> - Seleccionar-ne un a partir del rang de mode comú, el guany, les impedàncies, el CMRR, el PSRR, l'offset, la deriva i el soroll.

L'amplificador diferencial clàssic és simple i econòmic, però en mesures de precisió sobre ponts arrossega tres limitacions: la impedància d'entrada finita carrega el pont, el CMRR depèn fortament del desajustament de resistències —difícil de mantenir alt i estable amb components discrets— i el mateix efecte de càrrega degrada el CMRR en funció del mesurand. L'**amplificador d'instrumentació** (IA) està dissenyat específicament per amplificar senyals diferencials de baixa amplitud amb **alta precisió, alta impedància d'entrada i excel·lent rebuig del mode comú**.

## 1 L'estructura de tres amplificadors operacionals

![Amplificador d'instrumentació de tres amplificadors operacionals: primera etapa amb dos amplificadors no inversors units per Rg i dues resistències Rf, i segona etapa amb un amplificador diferencial](assets/04_Unitat6_Amplificadors_dinstrumentacio_img_1.png)

*Figura: Figura 6.14 Amplificador d'instrumentació amb tres amplificadors operacionals.*

La **primera etapa** té dos amplificadors **no inversors**, un per entrada, que amplifiquen  $V_1$
 i  $V_2$
 respecte de massa. La **segona** és un amplificador diferencial que resta les sortides de la primera. Aquesta segona etapa sol tenir guany unitari, perquè és fàcil garantir  $R_1=R_2=R_3=R_4$
. El guany global es controla amb una **única resistència externa**  $R_g$
: sobre ella cau  $V_2-V_1$
 i el corrent que la travessa és el mateix que circula per les dues  $R_f$
, de manera que

$$
V_+ - V_- = \frac{V_2-V_1}{R_g}\,(R_g+2R_f) = (V_2-V_1)\left(1+\frac{2R_f}{R_g}\right) \qquad (6.42)
$$

$$
G_1 = 1+\frac{2R_f}{R_g} \qquad\qquad G = G_1\cdot G_2 \qquad (6.43)
$$

Ajustar el guany amb **un sol component** —cosa impossible amb l'amplificador diferencial, on cal canviar almenys dues resistències— és un dels atractius principals. Per fixar el guany no cal que les dues  $R_f$
 siguin exactament iguals: el guany és 1 més la seva suma dividida per  $R_g$
. Sí que cal que ho siguin, en canvi, perquè les tensions d'offset, els corrents de polarització i el CMRR finit dels dos amplificadors de la primera etapa es compensin mútuament.

Com que la primera etapa és no inversora, la **impedància d'entrada** és essencialment la de l'amplificador operacional multiplicada per l'efecte de la realimentació: molt elevada. El pont veu una càrrega molt lleugera i la tensió diferencial es manté pràcticament inalterada, de manera que el pont funciona segons el model teòric amb què s'han calculat sensibilitat, consum i mode comú. Això no vol dir que l'IA elimini els errors: l'offset, el soroll i les derives hi continuen essent, i excedir el **rang de mode comú** admissible té conseqüències encara que el guany diferencial sigui petit.

Molts fabricants ofereixen IA optimitzats per a ponts, amb rangs de mode comú compatibles amb la tensió del pont, guanys programables seleccionables per pins o per interfície digital, calibratge de zero i de guany, compensació de temperatura i proteccions. En AFE com el PGA302, aquest bloc és el nucli del front end, envoltat dels circuits d'excitació, les referències, l'ADC i la lògica digital de compensació.

## 2 Especificacions que cal llegir

| Paràmetre | Què descriu i com afecta |
|:--- |:--- |
| Exactitud de guany | Proximitat del guany real al nominal, en % o ppm. Es tradueix en **error de factor d'escala**; sovint es redueix amb calibratge sistemàtic |
| No-linealitat de guany | Desviació respecte d'una relació estrictament proporcional entre entrada diferencial i sortida. Crítica amb calibratge simple |
| Guany màxim i mínim | El mínim el fixa la segona etapa amb  $R_g$   en circuit obert; el màxim, la saturació d'alguna etapa o el consum |
| Tensió d'offset referida a l'entrada | Dona sortida no nul·la amb entrada diferencial zero: **error de zero** igual a l'offset multiplicat pel guany. S'expressa com un terme fix més un que depèn del guany, aquest darrer associat a la segona etapa |
| Corrents de polarització i d'offset | Mitjana i diferència en valor absolut dels corrents d'entrada. Circulen per les resistències de l'equivalent Thevenin del pont i generen tensions que després s'amplifiquen |
| CMRR | Capacitat de rebutjar el mode comú, molt gran en ponts comparat amb el senyal útil. Valors de 100 a 120 dB a baixa freqüència són habituals. **Depèn del guany i de la freqüència** |
| PSRR | Sensibilitat de la sortida a variacions de l'alimentació. Es modela com una font d'error en sèrie amb l'offset |
| Derives tèrmiques | Guany, offset, corrents, CMRR i PSRR depenen de la temperatura, amb coeficients en ppm/°C o µV/°C |
| Soroll | Tensions i corrents de soroll **referits a l'entrada**; la densitat depèn del guany configurat |

$$
\Delta V_{\text{os}} = \frac{\Delta V_{\text{cc}}}{PSRR} \qquad (6.44)
$$

El PSRR pot ser diferent per a l'alimentació positiva i la negativa, i aleshores el fabricant especifica tots dos. En rangs tèrmics amplis pot caldre mesurar la temperatura prop del dispositiu i compensar les derives per càlcul, o triar un IA amb especificacions més estrictes o compensació interna, cosa que encareix el producte.

## 3 Un cas concret: l'INA317

![Estructura interna de l'amplificador d'instrumentació INA317, amb la primera etapa de dos amplificadors, les resistències internes de 50 kΩ i la segona etapa diferencial de guany unitari](assets/04_Unitat6_Amplificadors_dinstrumentacio_img_2.png)

*Figura: Figura 6.15 Estructura interna de l'INA317, amplificador d'instrumentació de baix consum i alta precisió en contínua.*

La segona etapa té guany 1 i cada  $R_f$
 val 50 kΩ, de manera que  $G = 1 + 100\ \mathrm{k}\Omega/R_g$
, ajustable entre 1 i 1000. Les xifres il·lustren com **gairebé tot depèn del guany configurat**:

- **Guany:** exactitud del 0,01 % a guany unitari, que puja al 0,25 % al guany màxim. No-linealitat de 10 ppm, independent del guany. Deriva d'1 ppm/°C a guany unitari, més d'un ordre de magnitud pitjor a guanys alts.
- **Errors de zero:** offset típic de  $10\ \mu\mathrm{V}+25\ \mu\mathrm{V}/G$
, PSRR de  $1\ \mathrm{ppm}+5\ \mathrm{ppm}/G$
. Corrent de polarització típic de 70 pA i corrent d'offset de 50 pA.
- **Entrada:** impedàncies diferencial i en mode comú de 100 GΩ en paral·lel amb 3 pF —quatre ordres de magnitud per sobre de les d'un diferencial de quatre resistències. El mode comú a l'entrada ha de mantenir-se a més de 0,1 V dels dos rails d'alimentació.
- **CMRR:** 90 dB a guany unitari, creixent amb el guany fins a 115 dB a guany 100, valor que ja no millora al guany màxim de 1000.
- **Soroll:** densitat espectral de tensió d'uns 50 nV/√Hz a guany 100 i de corrent de 100 fA/√Hz.

En freqüència, el **producte guany per amplada de banda** es manté raonablement constant, al voltant de 300 kHz, per a guanys diferents d'1; a guany unitari poden aparèixer ressonàncies. El CMRR comença a degradar-se per sobre dels 100 Hz i el PSRR encara abans, i tant més aviat com més baix és el guany. En contínua això rarament limita, però és el motiu pel qual les especificacions s'han de llegir **al rang d'ús** i no com a valors universals.

## 4 Criteris de selecció

Triar un IA no es pot reduir al preu ni al guany màxim del full de dades. Cal comprovar que el **rang de tensió d'entrada i de mode comú** sigui compatible amb la sortida del pont i amb les alimentacions disponibles; que el **guany necessari** s'assoleixi sense penalitzar excessivament l'amplada de banda ni el soroll, i preferiblement amb una sola resistència; que la **impedància d'entrada** sigui prou alta per no carregar el pont, cosa crítica amb sensors de resistència de sortida elevada; que **CMRR i PSRR** siguin suficients perquè les fluctuacions del mode comú i de l'alimentació no es confonguin amb el mesurand; i que **offset, corrents de polarització, derives i soroll** quedin justificats dins del balanç d'incertesa per al rang de mesura previst. Segons l'aplicació, també el consum, el rang de temperatura i l'encapsulat.

> [!TIP] **Síntesi**
>
> L'amplificador d'instrumentació resol les limitacions del diferencial simple en impedància d'entrada i CMRR. L'estructura clàssica de tres amplificadors operacionals té una primera etapa no inversora, d'impedància d'entrada molt alta, amb guany  $G_1 = 1+2R_f/R_g$
> ajustable amb una sola resistència externa, i una segona etapa diferencial de guany habitualment unitari. Les especificacions decisives són exactitud i no-linealitat de guany, tensió d'offset referida a l'entrada, corrents de polarització i d'offset, CMRR i PSRR —tots dos dependents del guany i de la freqüència—, derives tèrmiques, soroll referit a l'entrada i producte guany–amplada de banda. L'INA317 il·lustra la dependència del guany en gairebé tots els paràmetres. La selecció s'ha de fer contra el balanç d'incertesa complet, no contra un únic número.

[← 3. Conversió corrent–tensió i amplificadors diferencials](#conversió-correnttensió-i-amplificadors-diferencials)[5. Interruptors, multiplexors analògics i PGA →](#interruptors-multiplexors-analògics-i-pga)

---

<!-- FIN CAPÍTULO: 04_Unitat6_Amplificadors_dinstrumentacio -->

---

<!-- INICIO CAPÍTULO: 05_Unitat6_Interruptors_multiplexors_i_PGA -->

# Interruptors, multiplexors analògics i PGA

Sistemes de Mesura · **Unitat 6 — Condicionament de sensors en contínua** · Document 5 de 6

# Interruptors, multiplexors analògics i PGA

Dedicació estimada: 13 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Enumerar les fonts d'error en contínua d'un interruptor analògic real i quantificar-ne l'efecte.
> - Explicar per què un interruptor CMOS té una resistència de conducció menor i més plana que un MOSFET.
> - Dimensionar la resistència de càrrega d'un interruptor com a compromís entre estat tancat i obert.
> - Distingir PGA i VGA i avaluar l'error de guany introduït per  $R_{\text{on}}$
> segons l'arquitectura.

Els amplificadors d'instrumentació i els AFE d'altes prestacions tenen un cost considerable, de manera que resulta atractiu **compartir un únic front end analògic** entre diversos canals. S'aconsegueix interposant interruptors i multiplexors analògics entre els sensors i l'amplificador. L'estratègia redueix cost i complexitat, però introdueix **noves fonts d'error** —resistència de conducció, fuites, capacitats paràsites— i no dispensa de calibrar cada canal.

## 1 Interruptor ideal i interruptor real

![A dalt, model ideal d'interruptor analògic amb senyal d'entrada igual al de sortida; a baix, model d'un interruptor CMOS real amb capacitats CioA, CioB, CF, CCHNL i resistència de conducció ron](assets/05_Unitat6_Interruptors_multiplexors_i_PGA_img_1.png)

*Figura: Figura 6.16 Interruptor ideal (a dalt) comparat amb el model d'un interruptor CMOS real (a baix).*

L'interruptor ideal és circuit obert quan està obert i curtcircuit quan està tancat, amb l'estat controlat per un senyal digital de dos nivells. El model real hi afegeix capacitats cap a massa a l'entrada i a la sortida, una capacitat de fuites entre totes dues, una capacitat associada al canal i, sobretot, una **resistència de conducció**  $R_{\text{on}}$
 en sèrie quan està tancat:

$$
V_{\text{SD}} = I_D\cdot R_{\text{on}} \qquad (6.45)
$$

La tensió de sortida és, doncs, **més petita** que la d'entrada segons la impedància de càrrega:  $R_{\text{on}}$
 interessa que sigui molt menor que la impedància d'entrada de l'etapa següent. Les capacitats no tenen efecte en contínua estricta, però provoquen un **transitori** a cada commutació. I hi ha una segona font d'error que el model dibuixat no recull: la circulació de **corrents de fuites**, que fa que l'aïllament en obert no sigui perfecte.

## 2 De MOSFET a CMOS

Els primers interruptors analògics eren MOSFET: la tensió entre porta i font crea o no el canal, i per sota de la tensió llindar el transistor està en tall. Amb el canal creat i sense curtcircuitar la sortida, el transistor treballa en **zona lineal** i la caiguda entre drenador i font és reduïda, com correspon a un interruptor. La resistència de conducció depèn de la mobilitat dels portadors, de la capacitat i la geometria de la porta i, de manera decisiva, de  $(V_{\text{GS}}-V_T)$
 i de la mateixa  $V_{\text{DS}}$
. Aquesta darrera dependència és el problema:  $R_{\text{on}}$
 **varia amb la tensió del senyal** i, si els canvis són grans, distorsiona.

![Estructura interna d'un interruptor CMOS amb quatre MOSFET: un inversor format per Q1 i Q2 que controla les portes de Q3 de canal P i Q4 de canal N, connectats en paral·lel i en oposició](assets/05_Unitat6_Interruptors_multiplexors_i_PGA_img_2.png)

*Figura: Figura 6.17 Estructura interna d'un interruptor CMOS.*

![Gràfica de la resistència de conducció d'un interruptor CMOS comparada amb la dels MOSFET de canal N i de canal P per separat, en funció de la tensió entre els terminals](assets/05_Unitat6_Interruptors_multiplexors_i_PGA_img_3.png)

*Figura: Figura 6.18 Resistència de conducció d'un interruptor CMOS comparada amb la dels MOSFET que el formen.*

Els MOSFET de canal N i de canal P tenen dependències **oposades** amb la tensió del canal. L'interruptor CMOS aprofita aquest fet posant-ne un de cada tipus **en paral·lel i en oposició** —font amb drenador i viceversa—, controlats per un inversor CMOS intern alimentat entre  $V_{\text{DD}}$
 i  $V_{\text{SS}}$
. La resistència resultant és el **paral·lel** de les dues: menor que qualsevol d'elles per separat i molt més estable amb la tensió. No és constant, però sí prou plana. Els valors típics van de dècimes d'ohm a centenars d'ohm segons preu i velocitat de commutació.

## 3 Errors en contínua

![Anàlisi d'errors en contínua amb l'interruptor tancat: font Thevenin Vin amb resistència Rg, resistència de conducció Ron, corrent de fuites i resistència de càrrega Rload](assets/05_Unitat6_Interruptors_multiplexors_i_PGA_img_4.png)

*Figura: Figura 6.19 Errors en contínua amb l'interruptor tancat.*

Amb l'interruptor **tancat**, per superposició sobre la resistència de càrrega:

$$
V_{\text{OUT}} = V_{\text{IN}}\,\frac{R_{\text{LOAD}}}{R_{\text{LOAD}}+R_{\text{ON}}+R_G} + I_{\text{LKG}}\,\frac{R_{\text{LOAD}}\,(R_{\text{ON}}+R_G)}{R_{\text{LOAD}}+R_{\text{ON}}+R_G} \qquad (6.46)
$$

Si  $R_{\text{ON}}$
 és molt menor que  $R_{\text{LOAD}}$
, els errors es redueixen i  $V_{\text{OUT}}\approx V_{\text{IN}}$
. Fer  $R_{\text{on}}$
 *més petita* respecte de la càrrega, per tant, **redueix** l'error de caiguda.

![Anàlisi d'errors en contínua amb l'interruptor obert: el corrent de fuites circula per la resistència de càrrega generant una tensió residual](assets/05_Unitat6_Interruptors_multiplexors_i_PGA_img_5.png)

*Figura: Figura 6.20 Errors en contínua amb l'interruptor obert.*

Amb l'interruptor **obert** el corrent de fuites persisteix —no desapareix— i produeix una tensió residual:

$$
V_{\text{OUT}} = I_{\text{LKG}}\cdot R_{\text{LOAD}} \qquad (6.47)
$$

Aquest error **augmenta** amb la resistència de càrrega. Els dos requisits són oposats, i d'aquí surt el criteri pràctic: a la sortida dels interruptors es col·loca una resistència de càrrega de **valor de compromís**, prou gran per transmetre bé la tensió en estat tancat i prou petita per limitar la tensió residual en estat obert. Cap dels dos extrems és òptim. Segons el procés de fabricació, els corrents de fuites en estat tancat i en obert poden ser diferents —el fabricant especifica *ON leakage* i *OFF leakage* per separat—, encara que del mateix ordre de magnitud, típicament d'alguns pA a alguns nA.

## 4 Limitacions en alterna i en commutació

Amb l'interruptor **tancat**, el guany en contínua és el divisor  $R_{\text{LOAD}}/(R_{\text{LOAD}}+R_{\text{ON}})$
; en pujar la freqüència, les capacitats de drenador i de càrrega curtcircuiten la resistència de càrrega i apareix un **pol**, i més amunt la capacitat entre drenador i font curtcircuita  $R_{\text{on}}$
 i apareix un **zero**: la resposta no és plana fins a freqüència infinita. Amb l'interruptor **obert**, l'aïllament és infinit en contínua però **empitjora** en pujar la freqüència, a mesura que baixa la impedància de les capacitats.

S'hi afegeixen la **injecció de càrrega** de la commutació dels transistors del driver, que altera temporalment la sortida després d'un canvi d'estat, i el **crosstalk** entre canals propers, rellevant amb senyals variables o commutació ràpida. En sistemes multiplexats ràpids cal verificar que el **temps d'establiment** sigui compatible amb el temps de conversió de l'ADC: no ho és automàticament.

## 5 Multiplexors i ús pràctic

![Multiplexor analògic amb quatre canals d'entrada i una sortida comuna, format per interruptors controlats digitalment](assets/05_Unitat6_Interruptors_multiplexors_i_PGA_img_6.png)

*Figura: Figura 6.21 Multiplexor amb quatre canals d'entrada i una sortida comuna.*

Un multiplexor no és més que un **conjunt d'interruptors** connectats per seleccionar un camí de senyal. L'alimentació pot ser unipolar o dual, generalment simètrica. Els dispositius *rail to rail* admeten tensions d'entrada dins del marge  $[V_{\text{SS}}, V_{\text{DD}}]$
 fins i tot molt a prop dels límits, i alguns encara més optimitzats en toleren de fora, però cap transfereix qualsevol tensió saltant-se tots els límits d'alimentació.

Les especificacions rellevants en contínua són  $R_{\text{on}}$
, la seva **planitud** —com varia amb la tensió del senyal, és a dir amb la tensió entre font i drenador—, el ***$R_{on}$ match*** —com s'assemblen entre canals, cosa que només té sentit en multiplexors— i els corrents de fuites en tots dos estats. Les recomanacions pràctiques que se'n deriven: triar  $R_{\text{on}}$
 petita en relació amb la càrrega, situar l'interruptor en punts de **bona impedància** —la sortida d'un buffer— i no entre el sensor i la referència si això degrada la sensibilitat, afegir la resistència de càrrega de compromís, respectar el rang de tensió d'entrada i preveure els efectes en alterna quan la commutació sigui freqüent. En sistemes multicanal exigents és habitual el **calibratge individual per canal**, per compensar diferències de  $R_{\text{on}}$
, fuites i impedàncies de sensor; és perfectament compatible amb compartir un únic ADC.

## 6 Amplificadors de guany programable

Un amplificador de guany ajustable és necessari quan el sistema té un marge dinàmic ampli o mesura magnituds amb escales diferents: serveix per **ajustar el nivell de senyal al marge dinàmic de l'ADC**. El guany ha de ser molt acurat, perquè el valor digitalitzat s'interpreta com una estimació del mesurand: un error de guany és un error de factor d'escala.

Es parla de **VGA** quan el guany es controla amb un senyal analògic continu —habitualment la tensió de porta d'un MOSFET en zona lineal, la resistència del qual entra a l'expressió del guany—, i de **PGA** quan es fixa amb una **entrada digital**. En un PGA el nombre de guanys és **finit** i sovint reduït, amb salts per dècades (10, 100, 1000) o per octaves (2, 4, 8, 16). Tots dos poden tenir entrades i sortides unipolars o diferencials. Els paràmetres que diferencien els models comercials són com se selecciona el guany, com hi afecta la  $R_{\text{on}}$
, l'exactitud, la linealitat i la deriva tèrmica del guany, la relació entre guany i amplada de banda, els errors de zero, el temps d'establiment en canviar de guany, el soroll i les impedàncies.

![Dues arquitectures d'amplificador no inversor programable: a dalt, interruptors en sèrie amb les resistències que fixen el guany; a baix, interruptors situats en un node sense corrent apreciable](assets/05_Unitat6_Interruptors_multiplexors_i_PGA_img_7.png)

*Figura: Figura 6.22 Dues arquitectures d'amplificador no inversor programable: amb l'interruptor en sèrie amb la xarxa de guany (a dalt) i amb l'interruptor en un node sense corrent (a baix).*

A l'arquitectura superior, amb una resistència de realimentació fixa  $R_F$
 i una única resistència  $R$
 commutada cap a massa, el guany real és

$$
G = 1+\frac{R_F}{R+R_{\text{on}}} \qquad (6.48)
$$

La  $R_{\text{on}}$
 queda **en sèrie** amb la resistència que fixa el guany. Pot ser de dècimes d'ohm, però en interruptors econòmics està entre 100 Ω i 500 Ω.

> [!EXAMPLE] **Exemple resolt: error de guany introduït per $R_{\text{on}}$**
>
> Un PGA amb  $R_F = 10\ \mathrm{k}\Omega$
> i interruptors de  $R_{\text{on}} = 25\ \Omega$
>. Quin error relatiu de guany s'obté als guanys nominals 2 i 16?
>
> 1. Guany 2. Cal  $R = 10\ \mathrm{k}\Omega$
>. El guany real és  $1+10\,000/10\,025 = 1{,}9975$
>, amb un error de  $0{,}12\ \%$
>.
> 2. Guany 16. Cal  $R = 666{,}66\ \Omega$
>. El guany real és  $1+10\,000/691{,}66 = 15{,}46$
>, amb un error de  $3{,}39\ \%$
>.
> 3. Tendència. El guany real és sempre **menor** que el nominal, i l'error **creix amb el guany seleccionat**, perquè  $R_{\text{on}}$
> pesa cada cop més sobre una  $R$
> més petita.
> 4. Solució descartada. Es podria reduir l'error augmentant totes les resistències, però és mala idea: el **soroll** del PGA augmentaria.

L'arquitectura inferior resol el problema d'arrel: **situar l'interruptor en un node pel qual no circuli corrent apreciable**. A guany unitari no hi circula corrent i el circuit actua com a seguidor; a guany 2, la tensió d'entrada s'aplica al divisor de dues resistències iguals i la sortida val el doble. En cap cas la  $R_{\text{on}}$
 no afecta el guany, perquè l'únic corrent que hi passa és el de polarització de l'entrada inversora, molt petit amb etapa d'entrada FET. És, per això, l'arquitectura més emprada en PGA comercials.

> [!TIP] **Síntesi**
>
> Compartir un front end entre canals exigeix interruptors i multiplexors, que aporten  $R_{\text{on}}$
>, fuites i capacitats paràsites. L'interruptor CMOS combina canal N i canal P en paral·lel per obtenir una  $R_{\text{on}}$
> menor i molt més plana amb la tensió del senyal. En estat tancat l'error de caiguda es redueix si  $R_{\text{on}}\ll R_{\text{LOAD}}$
>; en estat obert la tensió residual val  $I_{\text{LKG}}R_{\text{LOAD}}$
> i creix amb la càrrega, d'on la resistència de càrrega de compromís. Les especificacions clau són  $R_{\text{on}}$
>, la seva planitud, el *match* entre canals i les fuites en tots dos estats, i el calibratge per canal continua essent necessari. Un PGA fixa el guany amb control digital entre un conjunt finit de valors i un VGA amb control analògic continu. Si la  $R_{\text{on}}$
> queda en sèrie amb la xarxa de guany, l'error creix amb el guany seleccionat; situar l'interruptor en un node sense corrent l'elimina.

[← 4. Amplificadors d'instrumentació](#amplificadors-dinstrumentació)[6. Referències de tensió i de corrent i mesures ratiomètriques →](#referències-de-tensió-i-de-corrent-i-mesures-ratiomètriques)

---

<!-- FIN CAPÍTULO: 05_Unitat6_Interruptors_multiplexors_i_PGA -->

---

<!-- INICIO CAPÍTULO: 06_Unitat6_Referencies_i_mesures_ratiometriques -->

# Referències de tensió i de corrent i mesures ratiomètriques

Sistemes de Mesura · **Unitat 6 — Condicionament de sensors en contínua** · Document 6 de 6

# Referències de tensió i de corrent i mesures ratiomètriques

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Justificar per què l'estabilitat de l'excitació limita l'exactitud global del sistema.
> - Distingir referència sèrie i referència shunt, i el principi de la referència bandgap.
> - Diferenciar regulació de línia i regulació de càrrega i les altres especificacions clau.
> - Deduir la cancel·lació ratiomètrica i enunciar-ne les condicions i els límits.

Cada vegada que una magnitud del sensor es converteix en tensió —amb un pont, un divisor o una font de corrent— el resultat depèn d'una excitació que es pressuposa estable. Un pont alimentat per  $V$
 lliura una sortida proporcional a  $V\cdot f(x)$
: si  $V$
 fluctua, el sistema **confon la fluctuació amb el mesurand**. Qualsevol font d'alimentació —bateria, regulador lineal, convertidor DC–DC— varia amb el temps, la temperatura i el corrent de càrrega. La referència és, per tant, un component crític: pot ser el factor que limiti l'exactitud global si s'escull malament.

## 1 Solucions elementals i les seves limitacions

La més simple és un **díode en conducció directa**: uns 0,6 V per a silici, apilables en sèrie. És elemental i econòmica, però té un coeficient de temperatura de −2 mV/°C, de manera que un rang de treball de 50 °C dona una deriva de l'ordre de 100 mV, inacceptable en mesura. A més, el corrent de càrrega ha de ser molt inferior al de polarització o la sortida es desestabilitza, i només es poden generar múltiples de 0,6 V. Per això han caigut en desús.

El **díode Zener**, en conducció inversa, permet tensions ajustables en un rang molt més ampli, fixat per la tensió de ruptura de la unió. Combinant un Zener amb un díode en directa en sèrie es redueix la dependència tèrmica: el coeficient positiu del Zener i el negatiu del díode directe es compensen parcialment si es trien dispositius amb coeficients d'igual mòdul i signe contrari.

## 2 Referències sèrie i shunt

![Esquemes de referència de tensió sèrie, amb entrada i sortida, i de referència shunt, amb resistència de polarització Rbias des d'una font no regulada i càrrega entre el node de sortida i massa](assets/06_Unitat6_Referencies_i_mesures_ratiometriques_img_1.png)

*Figura: Figura 6.23 Referència de tensió de tipus sèrie i de tipus shunt.*

En una referència **shunt**, la càrrega es connecta entre el node de sortida i massa, i una resistència de polarització  $R_{\text{BIAS}}$
 connecta aquest node a una font no regulada:

$$
I_{\text{BIAS}} = \frac{V_{\text{in}}-V_{\text{ref}}}{R_{\text{BIAS}}} = I_{\text{SHUNT}}+I_{\text{LOAD}} \qquad (6.49)
$$

El corrent disponible es **reparteix** entre la càrrega i el dispositiu de referència. Quan la càrrega canvia, canvia el corrent per la referència —que és qui fixa la tensió—, cosa que pot introduir inestabilitat. Per minimitzar-ho es dimensiona  $R_{\text{BIAS}}$
 perquè el corrent per la referència sigui sempre prou gran i el seu canvi relatiu petit dins del rang previst de  $I_{\text{LOAD}}$
.

Una referència **sèrie** regula la tensió entre una entrada i una sortida i **alimenta directament la càrrega** dins d'un rang de corrent especificat.

![Estructura d'una referència de tensió sèrie basada en cel·la bandgap: la tensió de banda prohibida VBG es copia a l'entrada inversora d'un amplificador operacional amb xarxa R1-R2 i un transistor de sortida](assets/06_Unitat6_Referencies_i_mesures_ratiometriques_img_2.png)

*Figura: Figura 6.24 Referència de tensió sèrie basada en cel·la bandgap.*

Les referències de **banda prohibida** (bandgap) combinen dos efectes amb coeficients tèrmics **oposats** que s'equilibren. La tensió base–emissor d'un bipolar decreix uns −2 mV/°C, mentre que la diferència  $\Delta V_{\text{BE}}$
 entre dos transistors que operen a densitats de corrent molt diferents creix linealment amb la temperatura absoluta:

$$
\Delta V_{\text{BE}} = \frac{k_B T}{q}\ln(n) \qquad (6.50)
$$

Sumant-los amb els factors adequats s'obté una tensió de deriva molt baixa que tendeix al valor de la banda prohibida del silici, uns 1,25 V, d'on el nom. Aquesta tensió  $V_{\text{BG}}$
 es copia a l'entrada inversora d'un amplificador en llaç tancat i s'escala amb una xarxa resistiva,

$$
V_{\text{ref}} = V_{\text{BG}}\left(1+\frac{R_1}{R_2}\right) \qquad (6.51)
$$

amb un transistor que subministra el corrent de la càrrega en la versió sèrie, o que n'absorbeix el sobrant cap a massa en la versió shunt. S'assoleixen estabilitats tèrmiques d'1 a 50 ppm/°C, i per sota de 10 ppm/°C amb termes de compensació d'ordre superior que corregeixen les no-linealitats residuals.

## 3 Especificacions

| Paràmetre | Què descriu |
|:--- |:--- |
| Tensió nominal i rangs | Valor central en condicions nominals; rang de tensió d'entrada per a les sèrie, rang de corrent de polarització per a les shunt |
| Exactitud inicial | Proximitat al valor nominal a 25 °C. Dona la contribució de tipus B a la incertesa |
| Deriva tèrmica | Variació amb la temperatura, en µV/°C o ppm/°C. En 50 °C, 50 ppm/°C acumulen 2500 ppm (0,25 %), que passen directament a la sortida |
| Estabilitat a llarg termini | Envelliment, en ppm per 1000 hores o per any. Domina en sistemes que han de conservar el calibratge durant mesos |
| Soroll | Soroll de tensió de baixa freqüència, amb component 1/f en les bandgap: rellevant en mesures lentes o quasi estàtiques |
| Regulació de **càrrega** | Variació de  $V_{\text{ref}}$   quan canvia el **corrent** demanat per la càrrega, en ppm/mA |
| Regulació de **línia** | Variació de  $V_{\text{ref}}$   quan canvia la **tensió d'alimentació** dins del rang admissible, en ppm/V |

![Referència de corrent bàsica: una tensió de referència forçada sobre una resistència de sensat Rs mitjançant realimentació negativa i un transistor de sortida](assets/06_Unitat6_Referencies_i_mesures_ratiometriques_img_3.png)

*Figura: Figura 6.25 Referència de corrent bàsica.*

En mesures a 4 fils, polarització de sensors resistius o excitació de RTD calen **corrents constants** i ben coneguts. La manera més directa d'obtenir-los és forçar una tensió de referència sobre una **resistència de sensat**:

$$
I_{\text{sink}} = \frac{V_{\text{ref}}}{R_s} \qquad (6.52)
$$

—proporcional a  $V_{\text{ref}}$
 i inversament proporcional a  $R_s$
. Perquè la tensió sobre  $R_s$
 sigui efectivament  $V_{\text{ref}}$
 sense importar la càrrega, s'utilitza realimentació negativa amb transistors bipolars o FET. Una font de corrent real només manté les especificacions dins d'un **rang de tensió sobre la càrrega**: fora d'aquest rang deixa de regular. Les especificacions clau són el valor nominal, l'exactitud, aquest rang i les derives tèrmiques.

## 4 Mesures ratiomètriques

![Mesura ratiomètrica: pont de resistències excitat per V, amplificador d'instrumentació de guany G i ADC que utilitza la mateixa V com a tensió de referència](assets/06_Unitat6_Referencies_i_mesures_ratiometriques_img_4.png)

*Figura: Figura 6.26 Mesura ratiomètrica: la mateixa tensió excita el pont i serveix de referència a l'ADC.*

En la majoria de circuits estudiats la sortida és proporcional a l'excitació. La idea ratiomètrica és que, en lloc d'estabilitzar la referència fins a nivells de precisió costosos, **s'aprofita que la mateixa incertesa afecta dues parts del circuit** i es cancel·la en la relació que determina el resultat. Amb un pont excitat per  $V$
, un amplificador de guany  $G$
 i un ADC amb  $V_{\text{ref}}=V$
, la sortida de l'amplificador és  $V_{\text{AI}}\approx V\cdot G\cdot f(x;k)$
 i la paraula digital val

$$
D = \left[\frac{V_{\text{AI}}}{V_{\text{ref}}}\cdot 2^{N_{\text{bits}}}\right] = \left[G\cdot f(x;k)\cdot 2^{N_{\text{bits}}}\right] \qquad (6.53)
$$

El resultat **no depèn de  $V$**. Qualsevol canvi de l'excitació —deriva tèrmica de la referència, fluctuació de la font, descàrrega de la bateria— afecta proporcionalment la sortida de l'amplificador i la referència de l'ADC, i la divisió implícita que fa el convertidor els cancel·la. El codi depèn només del guany, del mesurand, del disseny del pont i de la resolució.

> [!WARNING] **Què no cancel·la la ratiometria**
>
> - La cancel·lació exigeix que l'excitació i la referència de l'ADC siguin **la mateixa tensió** o proporcionals amb un factor constant, independent de les fluctuacions. Si varien de manera independent, no hi ha cancel·lació.
> - Exigeix que  $V_{\text{AI}}$
> sigui **estrictament proporcional** a  $V$
>: la saturació o la no-linealitat de l'amplificador la limiten. Saturar no ajuda.
> - Els **errors de zero** —tensió d'offset, corrents de polarització i les seves derives— **no** es cancel·len, perquè no són proporcionals a  $V$
>: cal compensar-los per calibratge.
> - El **soroll ràpid** de la referència pot no ser comú a les dues parts en el mateix instant i introduir incertesa addicional.
> - El guany de l'amplificador **no** desapareix del resultat, a diferència de l'excitació.

La ratiometria, doncs, redueix l'exigència sobre l'*exactitud absoluta* de la referència, i és plenament compatible amb ponts i divisors excitats per la mateixa tensió que serveix de referència a l'ADC —és precisament el seu cas d'ús—, però no dispensa d'analitzar offsets, soroll i no-linealitat, ni de linealitzar el sensor.

> [!TIP] **Síntesi**
>
> L'excitació del sensor ha de ser estable perquè les seves fluctuacions es confonen amb el mesurand. Els díodes en directa no serveixen (−2 mV/°C); els Zener amplien el rang i les referències bandgap combinen  $V_{\text{BE}}$
> i  $\Delta V_{\text{BE}}$
>, de coeficients oposats, per assolir 1–50 ppm/°C al voltant d'1,25 V. Les shunt reparteixen el corrent de polarització entre càrrega i dispositiu; les sèrie alimenten la càrrega directament. Cal llegir exactitud inicial, deriva tèrmica, soroll, estabilitat a llarg termini i les dues regulacions: la de **càrrega** davant canvis de corrent i la de **línia** davant canvis d'alimentació. Una referència de corrent s'obté forçant  $V_{\text{ref}}$
> sobre  $R_s$
>, amb un rang de tensió de càrrega limitat. La mesura ratiomètrica fa que el codi digital no depengui de l'excitació, sempre que aquesta i la referència de l'ADC siguin proporcionals i la cadena sigui lineal; els errors de zero i el soroll no comú hi persisteixen.

[← 5. Interruptors, multiplexors analògics i PGA](#interruptors-multiplexors-analògics-i-pga)

---

<!-- FIN CAPÍTULO: 06_Unitat6_Referencies_i_mesures_ratiometriques -->

---

<!-- INICIO CAPÍTULO: 07_Unitat6_Entrenament -->

# Entrenament V/F · Unitat 6: Condicionament de sensors en contínua

Sistemes de Mesura (230920) · ETSETB-UPC · **Unitat 6 — Condicionament de sensors en contínua**

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

### Qüestió 02
> 📌 **Afirmació:** *En sensors de sortida en continua, el criteri dominant de disseny és sempre l'amplada de banda per sobre de MHz.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En contínua el criteri dominant és la precisió DC, la deriva, el soroll de baixa freqüència i l'autoescalfament, no l'amplada de banda.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *L'objectiu pràctic del condicionador és aprofitar el marge dinàmic de l'ADC sense saturar-lo.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'objectiu enunciat: ocupar una fracció elevada del rang de l'ADC evitant saturacions.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *Les derives de temperatura dels components del condicionador poden contribuir a la incertesa de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Tots els components de l'etapa de precondicionament poden derivar amb la temperatura, i per això se sol monitorar-la.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *En molts sensors resistius interessa mesurar sobretot variacions de resistència al voltant d'un valor de referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'objectiu no és R0 en valor absolut sinó ΔR, sovint de l'ordre de 10⁻³·R0 o menys.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *L'autoescalfament incrementa la sensibilitat del sensor sense introduir error sistemàtic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'autoescalfament és un error sistemàtic, crític quan el sensor mesura precisament la temperatura del medi.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *La sensibilitat efectiva depèn del sensor, del condicionador i del rang utilitzable de l'ADC.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La sensibilitat efectiva depèn del sensor, del guany del condicionador i del rang de l'ADC.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *En una mesura a 2 fils, la resistència mesurada coincideix amb la del sensor encara que els cables tinguin resistència apreciable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La resistència mesurada val R + 2Rw.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *La mesura a 4 fils separa el camí de corrent del camí de mesura de tensió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un parell de cables injecta el corrent i un altre, independent, mesura la tensió.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 40
> 📌 **Afirmació:** *Els sensors de valor resistiu baix són menys sensibles als errors de resistència de cable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Al revés: com més baixa és la resistència nominal, més crític és l'error de cable.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 42
> 📌 **Afirmació:** *Amb una font de corrent simple, la sortida queda automàticament centrada a zero per al valor R0.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La sortida arrossega una component contínua V0 = I·R0.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *En un divisor senzill, triar R propera a R0 sol maximitzar la sensibilitat local al voltant del punt de referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per a x petit el màxim és a R = R0, amb Smax = Vref·α/4.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 53
> 📌 **Afirmació:** *La condició d'equilibri del pont correspon a la igualtat de les relacions de divisió de les dues branques.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'equilibri és la igualtat de les relacions de divisió de les dues branques.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 63
> 📌 **Afirmació:** *Augmentar k tendeix a reduir la sensibilitat intrínseca del pont.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La sensibilitat decau aproximadament com 1/k.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 66
> 📌 **Afirmació:** *L'error de no-linealitat del pont augmenta aproximadament amb el quadrat de k.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Decau aproximadament com 1/k²; no creix com k².*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 73
> 📌 **Afirmació:** *Les galgues de compensació es poden utilitzar per reduir l'efecte d'una pertorbació comuna com la temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La galga compensadora, a la mateixa temperatura però no sotmesa a la força, cancel·la la deriva tèrmica.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 83
> 📌 **Afirmació:** *Per corrents molt petits, la resistència de càrrega necessària pot ser molt elevada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un fotodíode de 10 pA que hagi de donar 1 mV demana una resistència de l'ordre de 100 MΩ.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 84
> 📌 **Afirmació:** *Una resistència de càrrega molt gran redueix simultàniament el soroll tèrmic generat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El soroll tèrmic creix amb l'arrel quadrada del valor de la resistència.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 86
> 📌 **Afirmació:** *L'amplificador de transimpedància manté el node d'entrada inversora prop d'una massa virtual.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El curtcircuit virtual manté l'entrada inversora a massa virtual.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 87
> 📌 **Afirmació:** *En un amplificador de transimpedància ideal, la sortida depèn principalment de Ip/Rf.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La sortida val Ip·Rf, no Ip/Rf.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 88
> 📌 **Afirmació:** *Els corrents de polarització de l'operacional poden generar offsets a través de la resistència de realimentació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Circulen per Rf i generen una tensió d'offset a la sortida que es confon amb el senyal.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 92
> 📌 **Afirmació:** *La tensió diferencial es defineix com la suma algebraica de les dues entrades respecte a massa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La diferencial és la diferència de les entrades; el mode comú n'és el valor mitjà.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 94
> 📌 **Afirmació:** *En l'amplificador diferencial de quatre resistències, el CMRR ideal depèn de la igualtat exacta de relacions de resistències.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El guany en mode comú s'anul·la quan R1/R2 = R3/R4.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 99
> 📌 **Afirmació:** *Els CMRR s'han de combinar directament en dB mitjançant una suma algebraica simple.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal convertir-los a unitats lineals, combinar-los i tornar a dB al final.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 101
> 📌 **Afirmació:** *La impedància d'entrada d'un amplificador diferencial pot carregar la sortida d'un pont.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Zd = 2R és finita i pot carregar el pont.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 102
> 📌 **Afirmació:** *L'efecte de càrrega incrementa sempre el guany diferencial efectiu del conjunt pont-amplificador.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La càrrega redueix el guany efectiu per sota del valor nominal.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 113
> 📌 **Afirmació:** *El guany de la primera etapa es pot ajustar mitjançant una única resistència externa en moltes arquitectures.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *G1 = 1 + 2Rf/Rg, ajustable amb una sola resistència externa.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 114
> 📌 **Afirmació:** *La primera etapa d'un AI de tres operacionals carrega fortament el pont perquè és inversora.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És no inversora i presenta una impedància d'entrada molt elevada.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 117
> 📌 **Afirmació:** *El CMRR d'un AI és independent del guany i de la freqüència en qualsevol dispositiu real.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El CMRR depèn del guany i de la freqüència: cal llegir-lo al rang d'ús.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 123
> 📌 **Afirmació:** *La tensió d'offset referida a l'entrada pot aparèixer com un error de zero després de l'amplificació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb entrada diferencial zero la sortida val l'offset multiplicat pel guany.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 125
> 📌 **Afirmació:** *El PSRR quantifica la sensibilitat de la sortida a variacions de l'alimentació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de PSRR.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 129
> 📌 **Afirmació:** *Una especificació en ppm/°C indica sempre un offset absolut expressat en volts.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És una deriva relativa per grau, no un offset absolut en volts.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 131
> 📌 **Afirmació:** *Un multiplexor analògic suma simultàniament tots els canals d'entrada abans de l'amplificació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Un multiplexor selecciona un camí de senyal, no suma els canals.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 134
> 📌 **Afirmació:** *La resistència de conducció d'un interruptor real equival a un curtcircuit ideal per a qualsevol càrrega.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La sortida queda per sota de l'entrada segons la relació entre Ron i la impedància de càrrega.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 135
> 📌 **Afirmació:** *Els interruptors CMOS combinen dispositius de canal N i de canal P per obtenir una resistència de conducció més petita.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La resistència resultant és el paral·lel de les dues i, a més, molt més plana amb la tensió.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 136
> 📌 **Afirmació:** *El corrent de fuites pot produir una tensió residual a la sortida quan l'interruptor està obert.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La tensió residual val ILKG·RLOAD.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 140
> 📌 **Afirmació:** *Els interruptors rail-to-rail transfereixen qualsevol tensió del sistema encara que superi tots els límits d'alimentació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Admeten tensions dins del marge VSS–VDD, fins i tot molt a prop dels límits, però no fora de tots ells.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 142
> 📌 **Afirmació:** *La injecció de càrrega pot alterar temporalment la tensió de sortida després d'un canvi d'estat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la injecció de càrrega dels transistors del driver.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 144
> 📌 **Afirmació:** *En sistemes multiplexats ràpids, el temps d'establiment després de commutar és compatible automàticament amb qualsevol ADC.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal verificar-ho: no és automàticament compatible amb el temps de conversió de l'ADC.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 148
> 📌 **Afirmació:** *Les especificacions ON leakage i OFF leakage poden tenir valors diferents.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El fabricant especifica ON leakage i OFF leakage per separat.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 150
> 📌 **Afirmació:** *La commutació analògica elimina la necessitat de calibratge individual de canal en sistemes multicanal exigents.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En sistemes multicanal exigents continua essent habitual el calibratge individual per canal.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 152
> 📌 **Afirmació:** *En un PGA, el guany se selecciona habitualment amb una entrada digital discreta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El PGA fixa el guany amb una entrada digital, entre un conjunt finit de valors.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 157
> 📌 **Afirmació:** *Col·locar l'interruptor en un node sense corrent apreciable pot reduir l'efecte de Ron sobre el guany.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'arquitectura més emprada en PGA comercials, precisament per això.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 163
> 📌 **Afirmació:** *Un díode en conducció directa proporciona una referència d'alta estabilitat tèrmica per a mesures de precisió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Té un coeficient de −2 mV/°C, cosa que dona uns 100 mV de deriva en un rang de 50 °C.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 165
> 📌 **Afirmació:** *En una referència shunt, el corrent de polarització es reparteix entre la càrrega i el dispositiu de referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *IBIAS = ISHUNT + ILOAD.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 166
> 📌 **Afirmació:** *Les referències bandgap combinen termes amb coeficients tèrmics oposats per reduir la deriva.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *VBE decreix amb la temperatura i ΔVBE hi creix: sumats amb els factors adequats, la deriva es cancel·la.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 168
> 📌 **Afirmació:** *La regulació de línia descriu la variació de Vref amb el corrent de càrrega.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Això és la regulació de càrrega; la de línia descriu la variació amb la tensió d'alimentació.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 174
> 📌 **Afirmació:** *Els offsets de l'amplificador d'instrumentació es cancel·len completament perquè formen part de la mateixa referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Els offsets no són proporcionals a V i cal compensar-los per calibratge.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 177
> 📌 **Afirmació:** *El resultat digital d'una mesura ratiomètrica ideal depèn de l'excitació absoluta V.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El codi digital resulta independent de V.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 183
> 📌 **Afirmació:** *El calibratge elimina permanentment les derives tèrmiques posteriors de tots els blocs del sistema.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El calibratge corregeix el que és estable, no les derives tèrmiques posteriors.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 189
> 📌 **Afirmació:** *Un guany més gran millora sempre la incertesa final del sistema.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Un guany més gran també amplifica offset, soroll i deriva, i pot excedir el rang admissible de l'ADC.*

> **📚 Document de referència:** `Document 01`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **02** | **F** | En contínua el criteri dominant és la precisió DC, la deriva, el soroll de baixa freqüència i l'autoescalfament, no l... | Document 01 |
| **06** | **V** | És l'objectiu enunciat: ocupar una fracció elevada del rang de l'ADC evitant saturacions. | Document 01 |
| **08** | **V** | Tots els components de l'etapa de precondicionament poden derivar amb la temperatura, i per això se sol monitorar-la. | Document 01 |
| **13** | **V** | L'objectiu no és R0 en valor absolut sinó ΔR, sovint de l'ordre de 10⁻³·R0 o menys. | Document 01 |
| **22** | **F** | L'autoescalfament és un error sistemàtic, crític quan el sensor mesura precisament la temperatura del medi. | Document 01 |
| **26** | **V** | La sensibilitat efectiva depèn del sensor, del guany del condicionador i del rang de l'ADC. | Document 01 |
| **32** | **F** | La resistència mesurada val R + 2Rw. | Document 02 |
| **34** | **V** | Un parell de cables injecta el corrent i un altre, independent, mesura la tensió. | Document 02 |
| **40** | **F** | Al revés: com més baixa és la resistència nominal, més crític és l'error de cable. | Document 02 |
| **42** | **F** | La sortida arrossega una component contínua V0 = I·R0. | Document 02 |
| **48** | **V** | Per a x petit el màxim és a R = R0, amb Smax = Vref·α/4. | Document 02 |
| **53** | **V** | L'equilibri és la igualtat de les relacions de divisió de les dues branques. | Document 02 |
| **63** | **V** | La sensibilitat decau aproximadament com 1/k. | Document 02 |
| **66** | **F** | Decau aproximadament com 1/k²; no creix com k². | Document 02 |
| **73** | **V** | La galga compensadora, a la mateixa temperatura però no sotmesa a la força, cancel·la la deriva tèrmica. | Document 02 |
| **83** | **V** | Un fotodíode de 10 pA que hagi de donar 1 mV demana una resistència de l'ordre de 100 MΩ. | Document 03 |
| **84** | **F** | El soroll tèrmic creix amb l'arrel quadrada del valor de la resistència. | Document 03 |
| **86** | **V** | El curtcircuit virtual manté l'entrada inversora a massa virtual. | Document 03 |
| **87** | **F** | La sortida val Ip·Rf, no Ip/Rf. | Document 03 |
| **88** | **V** | Circulen per Rf i generen una tensió d'offset a la sortida que es confon amb el senyal. | Document 03 |
| **92** | **F** | La diferencial és la diferència de les entrades; el mode comú n'és el valor mitjà. | Document 03 |
| **94** | **V** | El guany en mode comú s'anul·la quan R1/R2 = R3/R4. | Document 03 |
| **99** | **F** | Cal convertir-los a unitats lineals, combinar-los i tornar a dB al final. | Document 03 |
| **101** | **V** | Zd = 2R és finita i pot carregar el pont. | Document 03 |
| **102** | **F** | La càrrega redueix el guany efectiu per sota del valor nominal. | Document 03 |
| **113** | **V** | G1 = 1 + 2Rf/Rg, ajustable amb una sola resistència externa. | Document 04 |
| **114** | **F** | És no inversora i presenta una impedància d'entrada molt elevada. | Document 04 |
| **117** | **F** | El CMRR depèn del guany i de la freqüència: cal llegir-lo al rang d'ús. | Document 04 |
| **123** | **V** | Amb entrada diferencial zero la sortida val l'offset multiplicat pel guany. | Document 04 |
| **125** | **V** | És la definició de PSRR. | Document 04 |
| **129** | **F** | És una deriva relativa per grau, no un offset absolut en volts. | Document 04 |
| **131** | **F** | Un multiplexor selecciona un camí de senyal, no suma els canals. | Document 05 |
| **134** | **F** | La sortida queda per sota de l'entrada segons la relació entre Ron i la impedància de càrrega. | Document 05 |
| **135** | **V** | La resistència resultant és el paral·lel de les dues i, a més, molt més plana amb la tensió. | Document 05 |
| **136** | **V** | La tensió residual val ILKG·RLOAD. | Document 05 |
| **140** | **F** | Admeten tensions dins del marge VSS–VDD, fins i tot molt a prop dels límits, però no fora de tots ells. | Document 05 |
| **142** | **V** | És la injecció de càrrega dels transistors del driver. | Document 05 |
| **144** | **F** | Cal verificar-ho: no és automàticament compatible amb el temps de conversió de l'ADC. | Document 05 |
| **148** | **V** | El fabricant especifica ON leakage i OFF leakage per separat. | Document 05 |
| **150** | **F** | En sistemes multicanal exigents continua essent habitual el calibratge individual per canal. | Document 05 |
| **152** | **V** | El PGA fixa el guany amb una entrada digital, entre un conjunt finit de valors. | Document 05 |
| **157** | **V** | És l'arquitectura més emprada en PGA comercials, precisament per això. | Document 05 |
| **163** | **F** | Té un coeficient de −2 mV/°C, cosa que dona uns 100 mV de deriva en un rang de 50 °C. | Document 06 |
| **165** | **V** | IBIAS = ISHUNT + ILOAD. | Document 06 |
| **166** | **V** | VBE decreix amb la temperatura i ΔVBE hi creix: sumats amb els factors adequats, la deriva es cancel·la. | Document 06 |
| **168** | **F** | Això és la regulació de càrrega; la de línia descriu la variació amb la tensió d'alimentació. | Document 06 |
| **174** | **F** | Els offsets no són proporcionals a V i cal compensar-los per calibratge. | Document 06 |
| **177** | **F** | El codi digital resulta independent de V. | Document 06 |
| **183** | **F** | El calibratge corregeix el que és estable, no les derives tèrmiques posteriors. | Document 01 |
| **189** | **F** | Un guany més gran també amplifica offset, soroll i deriva, i pot excedir el rang admissible de l'ADC. | Document 01 |

<!-- FIN CAPÍTULO: 07_Unitat6_Entrenament -->

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
| **(6.1)** | $R_x(x) = R_0\,f(x) \approx R_0\,(1+\alpha x)$ |
| **(6.2)** | $V_{\text{mes}} = I\,(R + 2R_w)$ |
| **(6.3)** | $R_{\text{mes}} = \frac{V_{\text{mes}}}{I} = R + 2R_w$ |
| **(6.4)** | $R_{\text{mes}} = \frac{V}{I} = R$ |
| **(6.5)** | $V_{\text{out}}(x) = I\,R_x(x) = I\,R_0\,(1+\alpha x)$ |
| **(6.6)** | $S_V = \frac{\partial V_{\text{out}}}{\partial x} = I\,R_0\,\alpha$ |
| **(6.7)** | $V_3 - V_4 \approx I\,(R_x - R)$ |
| **(6.8)** | $V_1 - V_2 \approx I\,(R_{w1} + R_x - R - R_{w2}) \approx I\,(R_x - R)$ |
| **(6.9)** | $V_{\text{out}} = V_{\text{ref}}\,\frac{R_x}{R+R_x}$ |
| **(6.10)** | $V_{\text{out}}(x) = V_{\text{ref}}\,\frac{R_0(1+\alpha x)}{R+R_0(1+\alpha x)}$ |
| **(6.11)** | $S = \frac{\partial V_{\text{out}}}{\partial x} = V_{\text{ref}}\cdot\frac{R_0\,\alpha\,R}{\left(R+R_0(1+\alpha x)\right)^2}$ |
| **(6.12)** | $S_{\max} = V_{\text{ref}}\cdot\frac{\alpha}{4}$ |
| **(6.13)** | $P_x \approx \frac{V_{\text{ref}}^2\,R_x}{(R+R_x)^2}$ |
| **(6.14)** | $V_- = V_{\text{cc}}\,\frac{R_3}{R_1+R_3}$ |
| **(6.15)** | $V_+ = V_{\text{cc}}\,\frac{R_4}{R_2+R_4}$ |
| **(6.16)** | $V_{\text{out}} = V_+ - V_- = V_{\text{cc}}\left(\frac{R_4}{R_2+R_4}-\frac{R_3}{R_1+R_3}\right)$ |
| **(6.17)** | $\frac{R_2}{R_0} = \frac{R_1}{R_3}$ |
| **(6.18)** | $V_{\text{out}} = V_{\text{cc}}\cdot\frac{k\,x}{(k+1+x)\,(k+1)}$ |
| **(6.19)** | $V_{\text{out}} \approx V_{\text{cc}}\cdot\frac{k\,x}{(k+1)^2}$ |
| **(6.20)** | $V_{\text{out}} \approx V_{\text{cc}}\cdot\frac{x}{k}$ |
| **(6.21)** | $I \approx \frac{V_{\text{cc}}}{(k+1)\,R_0}$ |
| **(6.22)** | $V_{\text{CM}} \approx \frac{V_{\text{cc}}}{k+1}$ |
| **(6.23)** | $E_l = V_{\text{cc}}\cdot\frac{k\,x^2}{(k+1)^2\,(k+1+x)}$ |
| **(k \gg 1+x)** | $E_l \approx V_{\text{cc}}\cdot\frac{x^2}{k^2} \qquad (6.24)$ |
| **(6.25)** | $V_{\text{out}} = V_{\text{cc}}\cdot x$ |
| **(6.26)** | $I_x = I_0\,(1+\beta x)$ |
| **(6.27)** | $I_x = I_0\cdot x$ |
| **(6.28)** | $\frac{\partial V}{\partial x} = I_0\,R\,\beta$ |
| **(6.29)** | $e_n = \sqrt{4\,k_B\,T\,R\,\Delta f}$ |
| **(6.30)** | $V_{\text{out}} = I_p\,R_f$ |
| **(6.31)** | $V_d = V_2 - V_1$ |
| **(6.32)** | $V_c = \frac{V_2+V_1}{2}$ |
| **(6.33)** | $V_o = G_d\,V_d + G_c\,V_c$ |
| **(6.34)** | $G_d = \frac{1}{2}\left[\frac{R_2}{R_1}+\left(1+\frac{R_2}{R_1}\right)\frac{R_4}{R_4+R_3}\right]$ |
| **(6.35)** | $G_c = \left(1+\frac{R_2}{R_1}\right)\frac{R_4}{R_4+R_3}-\frac{R_2}{R_1}$ |
| **(6.36)** | $\frac{R_1}{R_2} = \frac{R_3}{R_4}$ |
| **(6.37)** | $G_d = \frac{R_2}{R_1}$ |
| **(6.38)** | $CMRR_{\text{total}} = \frac{CMRR_R\cdot CMRR_{\text{AO}}}{CMRR_R+CMRR_{\text{AO}}}$ |
| **(6.39)** | $Z_d = 2\,R$ |
| **(6.40)** | $Z_c = \frac{R\,(G+1)}{2}$ |
| **(6.41)** | $G_{\text{load}} = \frac{G\cdot R}{R+k\,R_0/(k+1)} = \frac{G}{1+\frac{k\,R_0}{R\,(k+1)}} < G$ |
| **(6.42)** | $V_+ - V_- = \frac{V_2-V_1}{R_g}\,(R_g+2R_f) = (V_2-V_1)\left(1+\frac{2R_f}{R_g}\right)$ |
| **(6.43)** | $G_1 = 1+\frac{2R_f}{R_g} \qquad\qquad G = G_1\cdot G_2$ |
| **(6.44)** | $\Delta V_{\text{os}} = \frac{\Delta V_{\text{cc}}}{PSRR}$ |
| **(6.45)** | $V_{\text{SD}} = I_D\cdot R_{\text{on}}$ |
| **(6.46)** | $V_{\text{OUT}} = V_{\text{IN}}\,\frac{R_{\text{LOAD}}}{R_{\text{LOAD}}+R_{\text{ON}}+R_G} + I_{\text{LKG}}\,\frac{R_{\text{LOAD}}\,(R_{\text{ON}}+R_G)}{R_{\text{LOAD}}+R_{\text{ON}}+R_G}$ |
| **(6.47)** | $V_{\text{OUT}} = I_{\text{LKG}}\cdot R_{\text{LOAD}}$ |
| **(6.48)** | $G = 1+\frac{R_F}{R+R_{\text{on}}}$ |
| **(6.49)** | $I_{\text{BIAS}} = \frac{V_{\text{in}}-V_{\text{ref}}}{R_{\text{BIAS}}} = I_{\text{SHUNT}}+I_{\text{LOAD}}$ |
| **(6.50)** | $\Delta V_{\text{BE}} = \frac{k_B T}{q}\ln(n)$ |
| **(6.51)** | $V_{\text{ref}} = V_{\text{BG}}\left(1+\frac{R_1}{R_2}\right)$ |
| **(6.52)** | $I_{\text{sink}} = \frac{V_{\text{ref}}}{R_s}$ |
| **(6.53)** | $D = \left[\frac{V_{\text{AI}}}{V_{\text{ref}}}\cdot 2^{N_{\text{bits}}}\right] = \left[G\cdot f(x;k)\cdot 2^{N_{\text{bits}}}\right]$ |