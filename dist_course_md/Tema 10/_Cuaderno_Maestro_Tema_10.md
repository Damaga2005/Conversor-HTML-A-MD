# 📚 Cuaderno Maestro: Tema 10

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 10` | 📄 **Capítulos incluidos:** 7  
> 📅 **Generado:** 2026-09-11 19:10

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 10 — Condicionament singular de senyals · Lectura prèvia](#unitat-10-condicionament-singular-de-senyals-lectura-prèvia)
2. [Condicionament singular: sensors, l'operacional real i les seves derives](#condicionament-singular-sensors-loperacional-real-i-les-seves-derives)
   - [1 Sensors singulars](#1-sensors-singulars)
   - [2 L'operacional real: errors estàtics](#2-loperacional-real-errors-estàtics)
   - [3 Derives: temperatura i envelliment](#3-derives-temperatura-i-envelliment)
   - [4 Soroll: blanc i 1/f](#4-soroll-blanc-i-1f)
   - [5 Tecnologies d'entrada](#5-tecnologies-dentrada)
3. [Amplificadors de baixes derives: compensació de la polarització i ajust d'offset](#amplificadors-de-baixes-derives-compensació-de-la-polarització-i-ajust-doffset)
   - [1 L'especificació del problema](#1-lespecificació-del-problema)
   - [2 Compensació dels corrents de polarització](#2-compensació-dels-corrents-de-polarització)
   - [3 Compensació de la tensió d'offset](#3-compensació-de-la-tensió-doffset)
4. [Amplificadors chopper i amplificadors amb autozero](#amplificadors-chopper-i-amplificadors-amb-autozero)
   - [1 Amplificadors chopper](#1-amplificadors-chopper)
   - [2 Amplificadors amb autozero](#2-amplificadors-amb-autozero)
   - [3 Criteris de selecció](#3-criteris-de-selecció)
5. [Amplificadors electromètrics i de transimpedància](#amplificadors-electromètrics-i-de-transimpedància)
   - [1 Thevenin o Norton: quina topologia](#1-thevenin-o-norton-quina-topologia)
   - [2 Amplificadors electromètrics](#2-amplificadors-electromètrics)
   - [3 Amplificadors de transimpedància](#3-amplificadors-de-transimpedància)
   - [4 La xarxa en T](#4-la-xarxa-en-t)
   - [5 Disseny físic del node d'alta impedància](#5-disseny-físic-del-node-dalta-impedància)
6. [Amplificadors de càrrega](#amplificadors-de-càrrega)
   - [1 Model del sensor en càrrega](#1-model-del-sensor-en-càrrega)
   - [2 L'amplificador de càrrega](#2-lamplificador-de-càrrega)
   - [3 La resistència de realimentació](#3-la-resistència-de-realimentació)
   - [4 Errors de contínua](#4-errors-de-contínua)
   - [5 L'efecte triboelèctric](#5-lefecte-triboelèctric)
7. [Entrenament V/F · Unitat 10: Condicionament singular de senyals](#entrenament-vf-unitat-10-condicionament-singular-de-senyals)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_Unitat10_Index -->

# Unitat 10 — Condicionament singular de senyals · Lectura prèvia

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 10 — Condicionament singular de senyals

Materials de lectura prèvia · dedicació total estimada: 54 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen.

Llegeix els cinc documents en ordre **abans de la primera sessió**.

### [1. Condicionament singular: sensors, l'operacional real i les seves derives](#condicionament-singular-sensors-loperacional-real-i-les-seves-derives)

Què fa singular un sensor: la classificació electrònica, complementària de la física, en dos blocs segons si el problema dominant és el nivell de senyal o la impedància de sortida, i les tres famílies de circuits que se'n deriven. Tres mesures on l'operacional de propòsit general queda curt. El model de l'operacional real: tensió d'offset, corrents de polarització i d'offset, i l'error que produeixen en circular per les resistències del circuit. Deriva tèrmica i envelliment, i la diferència pràctica entre un error constant i un que deriva. Soroll blanc i soroll 1/f, la freqüència de cantonada i la integral sobre la banda útil. Ordres de magnitud per tecnologia d'entrada.

*⏱️ Dedicació estimada: 12 min*

### [2. Amplificadors de baixes derives: compensació de la polarització i ajust d'offset](#amplificadors-de-baixes-derives-compensació-de-la-polarització-i-ajust-doffset)

L'especificació del problema del termoparell: sensibilitats, resolució exigida i contingut freqüencial fins a la contínua, amb les cinc condicions simultànies que ha de satisfer l'amplificador i el criteri d'error referit a l'entrada. La resistència auxiliar que canvia un error proporcional al corrent de polarització per un de proporcional al corrent d'offset, i en quines tecnologies compensa. El guany de soroll com a factor que multiplica l'offset. L'ajust intern amb pins d'offset null i la seva degradació tèrmica. La compensació externa en les topologies inversora i no inversora, la doble compensació simultània i el dimensionament de la tensió de referència.

*⏱️ Dedicació estimada: 10 min*

### [3. Amplificadors chopper i amplificadors amb autozero](#amplificadors-chopper-i-amplificadors-amb-autozero)

La modulació a la freqüència de commutació, l'amplificació lluny de la zona de soroll 1/f i la desmodulació síncrona, seguides en el temps als cinc punts interns i en el domini freqüencial. El guany en llaç tancat i la seva equivalència amb el d'un amplificador convencional. Les tres limitacions intrínseques: banda útil, plegament de soroll de bandes laterals i residus de commutació. Els amplificadors amb autozero: les dues fases, l'emmagatzematge capacitiu de les correccions i la tensió d'offset efectiva reduïda pel factor de correcció. Arquitectures híbrides i els sis criteris de selecció d'un amplificador.

*⏱️ Dedicació estimada: 10 min*

### [4. Amplificadors electromètrics i de transimpedància](#amplificadors-electromètrics-i-de-transimpedància)

El model de Thevenin i el de Norton com a descripcions equivalents d'un mateix sensor, i la topologia que cadascun suggereix. L'amplificador electromètric: condicions de funcionament, divisor amb la impedància d'entrada finita i aplicació a l'elèctrode de vidre. L'amplificador de transimpedància: curtcircuit virtual, transimpedància en ohms o volts per ampere, estabilitat i la capacitat de realimentació. Errors de contínua i soroll de totes dues topologies, amb el guany de soroll que creix amb la freqüència. La xarxa en T per sintetitzar transimpedàncies de gigaohms i el seu preu en offset i soroll. Guardes, apantallament, aïllants, neteja i control d'humitat.

*⏱️ Dedicació estimada: 14 min*

### [5. Amplificadors de càrrega](#amplificadors-de-càrrega)

El model del sensor amb sortida en càrrega i les capacitats paràsites del cable i de l'entrada, comparables o superiors a la del sensor. La relació entre corrent i càrrega, l'integrador amb condensador de realimentació i la sortida proporcional a la càrrega, independent de les capacitats paràsites mentre el guany en llaç obert ho permeti. La resistència en paral·lel que evita la saturació, la condició que ha de complir a la freqüència mínima d'interès i la freqüència de tall inferior que en resulta. Errors de contínua en el model amb els condensadors oberts, i la tecnologia d'entrada que se'n dedueix. L'efecte triboelèctric i les mesures que el mitiguen.

*⏱️ Dedicació estimada: 8 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

<!-- FIN CAPÍTULO: 00_Unitat10_Index -->

---

<!-- INICIO CAPÍTULO: 01_Unitat10_Condicionament_singular_i_limits_de_loperacional -->

# Condicionament singular: sensors, l'operacional real i les seves derives

Sistemes de Mesura · **Unitat 10 — Condicionament singular de senyals** · Document 1 de 5

# Condicionament singular: sensors, l'operacional real i les seves derives

Dedicació estimada: 12 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Justificar per què determinats sensors exigeixen una electrònica de condicionament amb prestacions especials.
> - Classificar un sensor singular segons si el problema dominant és el nivell de senyal o la impedància de sortida.
> - Identificar les fonts d'error estàtiques d'un amplificador operacional real i quantificar-ne l'efecte a la sortida.
> - Relacionar la tecnologia de l'etapa d'entrada amb l'ordre de magnitud de l'offset, del corrent de polarització, de les derives i del soroll.
> - Distingir el soroll blanc del soroll 1/f i situar la freqüència de cantonada.

Hi ha mesures on les topologies genèriques de condicionament —amplificadors inversors i no inversors amb un operacional de propòsit general, ponts resistius— no arriben: la temperatura d'un forn industrial amb un termoparell, una radiació infraroja feble amb un sensor piroelèctric, el corrent d'un fotodíode en un espectrofotòmetre o les vibracions d'un rodament amb un acceleròmetre piezoelèctric. La tensió a amplificar pot quedar soterrada sota els errors de contínua de l'electrònica; la impedància de sortida del sensor pot ser prou alta perquè qualsevol amplificador convencional el carregui i en faci desaparèixer el senyal; o el mesurand pot venir representat per una càrrega elèctrica que fuig per qualsevol camí resistiu mal dimensionat. L'objectiu del condicionament, en tots tres casos, és preservar la relació entre el mesurand i el senyal elèctric que arriba al convertidor, de manera que l'electrònica no hi introdueixi una deformació dominant.

## 1 Sensors singulars

> [!WARNING] **Sensor singular**
>
> Sensor que, **per les característiques elèctriques de la seva sortida**, exigeix una electrònica amb prestacions especials i escollida amb cura. La singularitat és una propietat del senyal elèctric que lliura —nivell, impedància o càrrega—, i és compatible amb topologies de circuit d'aparença modesta.

Aquesta classificació és electrònica i complementa la classificació física habitual —termoparells, piezoelèctrics, piroelèctrics, fotodíodes—, que agrupa els sensors per la magnitud que mesuren i pel fenomen que hi intervé. Des del punt de vista del circuit, els sensors d'interès es reparteixen en dos blocs segons quin sigui el problema dominant.

| Bloc | Exemples | Problema dominant |
|:--- |:--- |:--- |
| **Tensió molt petita fins a la contínua** | Termoparells; ponts de galgues extensiomètriques piezorresistives en mesures d'esforços reduïts. | El senyal útil, de microvolts a alguns mil·livolts i concentrat entre la contínua i fraccions d'hertz, conviu amb els errors de contínua i les derives lentes de l'electrònica. Un canvi de la tensió d'offset és indistingible d'un canvi del mesurand. El soroll 1/f hi és màxim. |
| **Impedància de sortida molt elevada** | Piezoelèctrics, piroelèctrics, fotodíodes i fototransistors; sondes de pH i elèctrodes de ió selectiu, amb impedàncies de desenes de MΩ a alguns GΩ. | L'entrada de l'amplificador carrega el sensor i en redueix la sensibilitat efectiva. Com que la impedància del sensor sovint és capacitiva, la càrrega també en deforma la resposta freqüencial. Cal, alhora, gestionar les capacitats i les fuites paràsites del cablejat i de la placa. |

Els dos blocs porten a tres famílies de circuits: els **amplificadors de baixes derives**, per a tensions molt petites amb contingut fins a la contínua; els **amplificadors electromètrics i de transimpedància**, per a impedàncies de sortida extraordinàriament elevades; i els **amplificadors de càrrega**, que donen una tensió proporcional a la càrrega generada pel sensor i s'empren sobretot amb piezoelèctrics i piroelèctrics.

### El límit de l'amplificador de propòsit general

Un amplificador de propòsit general és un operacional pensat per a un ventall ampli d'aplicacions, amb prestacions equilibrades: guany en llaç obert de l'ordre de $10^{5}$, tensió d'offset que pot arribar a alguns mil·livolts, corrent de polarització de desenes o centenars de nanoampers amb entrada bipolar i de picoampers amb entrada FET, i amplada de banda d'alguns MHz. Per a moltíssimes aplicacions aquestes prestacions són suficients, i deixen de ser-ho en tres situacions representatives.

| Mesura | Senyal útil | Error de l'electrònica |
|:--- |:--- |:--- |
| Termoparell tipus K, resolució d'una dècima de grau | Sensibilitat de 41 μV/°C: cal discriminar 4 μV | Una tensió d'offset típica de 3 mV és tres ordres de magnitud més gran. Fins i tot ajustada, petits canvis de temperatura del circuit integrat en desplacen el valor desenes o centenars de μV. |
| Fotodíode en mode fotoconductor | Corrents fotogenerats molt reduïts, amb corrents d'obscuritat d'alguns pA | Un corrent de polarització de 100 nA és desenes de milers de vegades superior al senyal, i les seves variacions són ja de l'ordre del corrent que es vol mesurar. |
| Sensor piezoelèctric | Càrrega sobre una capacitat d'alguns nF amb resistència de fuita molt elevada | La impedància d'entrada de l'amplificador carrega el sensor, en redueix la sensibilitat efectiva i n'altera la resposta freqüencial. |

Quan el senyal útil és comparable als errors intrínsecs del component, o quan la impedància del sensor és prou alta perquè l'amplificador hi interfereixi apreciablement, calen circuits especialitzats amb prestacions millorades en aspectes molt concrets: tensió d'offset i les seves derives, corrent de polarització, impedància d'entrada, soroll i estabilitat temporal. El que fa singulars aquests circuits és l'elecció acurada dels components, les xarxes de compensació, l'ús d'operacionals especials i, sovint, tècniques de disseny físic —guardes, apantallaments, cables triboelèctricament estables, control de la humitat— innecessàries en aplicacions convencionals.

> [!WARNING] **Punt de partida del disseny**
>
> L'arquitectura es tria a partir del **model elèctric del sensor** —nivell de senyal, impedància de sortida i la seva naturalesa, banda útil— i del paràmetre d'error que hi domina. El guany, el repartiment en etapes i la banda passant se'n deriven.

## 2 L'operacional real: errors estàtics

Al símbol de l'amplificador operacional ideal, el model real hi afegeix una font de tensió en sèrie amb una de les entrades, que modela la tensió d'offset  $V_{\text{os}}$; dues fonts de corrent que modelen els corrents de polarització  $I_{B+}$  i  $I_{B-}$  que entren pels terminals no inversor i inversor; fonts de soroll de tensió i de corrent referides a l'entrada; i un guany diferencial en llaç obert  $A_{\text{OL}}$  modelat com una funció de transferència amb un o diversos pols.

![Símbol de l'amplificador operacional amb dues fonts de corrent que injecten els corrents de polarització I_B+ i I_B− als terminals no inversor i inversor.](assets/01_Unitat10_Condicionament_singular_i_limits_de_loperacional_img_1.png)

*Figura: Figura 10.1 Modelització dels corrents de polarització.*

> [!WARNING] **Corrent de polarització i corrent d'offset**
>
> El **corrent de polarització**  $I_B$  és la mitjana dels corrents que entren pels dos terminals d'entrada. El **corrent d'offset**  $I_{\text{OS}}$  és la **diferència** entre tots dos, i té l'origen en les asimetries del parell diferencial d'entrada. Tots dos són corrents: es mesuren en ampers.

L'ordre de magnitud d'aquests corrents depèn dràsticament de la tecnologia de l'etapa d'entrada. En operacionals d'entrada bipolar,  $I_B$  arriba a centenars de nanoampers en dispositius antics —el μA741 té una  $I_B$  típica de 80 nA— i baixa a alguns nanoampers amb tècniques de cancel·lació interna. Amb etapa d'entrada JFET o CMOS,  $I_B$  és de l'ordre de picoampers, i de femtoampers en components electromètrics específics. La relació entre tots dos corrents també hi canvia: en bipolars,  $I_{\text{OS}}$  sol quedar entre el 10 % i el 25 % de  $I_B$; en FET i CMOS,  $I_B$  és ja tan petit que les asimetries el fan comparable a  $I_{\text{OS}}$.

![Amplificador amb R1 d'entrada, R2 de realimentació i una resistència R3 igual al paral·lel de R1 i R2 entre el terminal no inversor i massa; els corrents de polarització I_B− i I_B+ hi circulen i generen tensió d'error a la sortida.](assets/01_Unitat10_Condicionament_singular_i_limits_de_loperacional_img_2.png)

*Figura: Figura 10.2 Efecte dels corrents de polarització associat a les resistències del circuit.*

Els corrents de polarització es tradueixen en error de contínua només quan circulen per les resistències del circuit. Amb  $R_1$  i  $R_2$  a la xarxa de realimentació i una resistència  $R_3$  entre el terminal no inversor i massa, la tensió d'error a la sortida és

$$
V_{out,err} = -I_B^{+}\cdot R_3\cdot\left(1+\frac{R_2}{R_1}\right) + I_B^{-}\cdot R_2 \qquad (10.1)
$$

Escollint  $R_3 = R_1\|R_2$, els dos termes es compensen fins a deixar només la part deguda a l'asimetria:

$$
V_{out,err} = -I_{\text{OS}}\cdot R_2 \qquad (10.2)
$$

La reducció és real quan  $I_B \gg I_{\text{OS}}$, és a dir, en amplificadors d'entrada bipolar. En qualsevol cas, el producte del corrent per la resistència apareix a la sortida com un terme additiu —un desplaçament del zero— el valor del qual depèn de les resistències externes del circuit.

![Model de la tensió d'offset: un amplificador ideal precedit d'una font de tensió V_os en sèrie amb el terminal no inversor.](assets/01_Unitat10_Condicionament_singular_i_limits_de_loperacional_img_3.png)

*Figura: Figura 10.3 Modelització de la tensió d'offset.*

La tensió d'offset es modela com una font de tensió referida a l'entrada, de manera que a la sortida hi apareix multiplicada pel guany que el circuit aplica a una tensió present entre els terminals d'entrada. Els bipolars presenten típicament desenes de microvolts a alguns mil·livolts; els JFET i CMOS, centenars de microvolts fins a desenes de mil·livolts en el pitjor cas; els de precisió, desenes de microvolts; i els chopper i autozero baixen per sota del microvolt.

## 3 Derives: temperatura i envelliment

Els errors de contínua no són constants. Un error constant es calibra una vegada i es corregeix numèricament; un error que deriva exigeix correcció dinàmica o estratègies de mesura especials. La deriva tèrmica de  $V_{\text{os}}$  és el paràmetre que separa les famílies d'amplificadors, i recorre tres ordres de magnitud entre els bipolars de propòsit general i els dispositius de correcció dinàmica.

L'envelliment provoca canvis lents de  $V_{\text{os}}$, quantificats en μV/mes o μV per cada 1000 h. En sistemes de llarga durada —monitorització industrial, equipament mèdic— aquests canvis són rellevants i imposen calibratges periòdics: el zero d'avui no és el zero d'un any vista.

El corrent de polarització també deriva. En bipolars,  $I_B$  disminueix lleugerament amb la temperatura. En JFET i CMOS creix exponencialment, doblant-se aproximadament cada 10 °C: un component electromètric amb 5 fA a 25 °C arriba a uns tres-cents femtoampers a 85 °C.

## 4 Soroll: blanc i 1/f

El soroll aleatori dels components interns es modela com una font de tensió en sèrie amb l'entrada i dues fonts de corrent en paral·lel amb cada terminal d'entrada. Les seves densitats espectrals tenen dues contribucions.

| Contribució | Densitat espectral | Origen |
|:--- |:--- |:--- |
| **Soroll blanc** | Plana amb la freqüència; domina a freqüències mitjanes i altes | Soroll tèrmic de les resistències internes del parell diferencial i soroll de *shot* dels corrents de base o de porta. |
| **Soroll 1/f** | Inversament proporcional a la freqüència; domina a freqüències baixes | Captures i alliberaments aleatoris de portadors en defectes de les interfícies Si-$SiO_{2}$ i en imperfeccions de les unions. |

> [!WARNING] **Freqüència de cantonada**
>
> Freqüència a la qual les densitats espectrals de les dues contribucions s'igualen (*corner frequency*). És un paràmetre característic de cada amplificador i separa a la pràctica la zona dominada pel soroll 1/f de la dominada pel soroll blanc.

El que arriba a la sortida és la **integral** de la densitat espectral sobre la banda passant del sistema, i és aquesta tensió de soroll RMS la que s'ha de comparar amb la resolució de mesura. D'aquí surt un criteri de disseny que travessa tota la unitat: la banda útil es limita al necessari per capturar la dinàmica del mesurand, perquè eixamplar-la afegeix soroll sense afegir informació. Per a senyals lents —el condicionament de termoparells n'és el cas paradigmàtic— el soroll 1/f s'integra sobre tota la banda útil i se suma a les derives lentes.

## 5 Tecnologies d'entrada

| Tecnologia | $V_{\text{os}}$  típic | Deriva | $I_B$  típic | Soroll de tensió @1 kHz | Soroll 1/f |
|:--- |:--- |:--- |:--- |:--- |:--- |
| Bipolar general | 1–5 mV | 5–20 μV/°C | 10–500 nA | 10–30 nV/√Hz | Moderat |
| Bipolar precisió | 10–50 μV | 0,1–1 μV/°C | 1–20 nA | 2–10 nV/√Hz | Baix |
| JFET | 0,5–5 mV | 5–20 μV/°C | 10–100 pA | 10–30 nV/√Hz | Moderat |
| CMOS | 1–20 mV | 5–30 μV/°C | 0,1–10 pA | 20–100 nV/√Hz | Alt |
| CMOS precisió | 50–500 μV | 1–5 μV/°C | 0,1–5 pA | 10–30 nV/√Hz | Moderat |
| Chopper / autozero | 0,1–5 μV | 0,005–0,05 μV/°C | 1–100 pA | 20–60 nV/√Hz | Negligible |

Cap tecnologia és òptima en tots els paràmetres alhora, i l'elecció depèn de quin domina en l'aplicació concreta. Els valors concrets varien notablement entre dispositius d'una mateixa família, de manera que el full de característiques del component escollit és la font vàlida per al pressupost d'error.

En les aplicacions d'aquesta unitat, les limitacions crítiques són les **estàtiques i el soroll**, perquè els senyals són de molt baix nivell i de baixa freqüència. Les limitacions dinàmiques hi tenen un paper concret: el guany en llaç obert finit i la seva caiguda amb la freqüència condicionen la resposta freqüencial dels amplificadors de càrrega i l'estabilitat de les topologies d'alta impedància.

> [!TIP] **Síntesi**
>
> Un sensor és singular per les característiques elèctriques de la seva sortida, i es classifica segons si el problema dominant és el nivell de senyal —tensions de microvolts amb contingut fins a la contínua— o la impedància de sortida, sovint capacitiva. El model de l'operacional real hi afegeix  $V_{\text{os}}$,  $I_{B+}$  i  $I_{B-}$, fonts de soroll de tensió i de corrent i un guany en llaç obert finit amb pols. Els corrents de polarització es tradueixen en error només en circular per resistències, i amb  $R_3 = R_1\|R_2$  l'error residual queda en  $I_{\text{OS}}\cdot R_2$. Els errors de contínua deriven amb la temperatura i amb l'envelliment: l'error constant es calibra, el que deriva exigeix correcció dinàmica. El soroll té una component blanca i una component 1/f que s'igualen a la freqüència de cantonada, i el que compta és la seva integral sobre la banda útil. La tecnologia de l'etapa d'entrada fixa simultàniament offset, corrent de polarització, deriva i soroll, sense que cap sigui òptima en tots alhora.

[2. Amplificadors de baixes derives: compensació de la polarització i ajust d'offset →](#amplificadors-de-baixes-derives-compensació-de-la-polarització-i-ajust-doffset)

---

<!-- FIN CAPÍTULO: 01_Unitat10_Condicionament_singular_i_limits_de_loperacional -->

---

<!-- INICIO CAPÍTULO: 02_Unitat10_Amplificadors_de_baixes_derives -->

# Amplificadors de baixes derives: compensació de la polarització i ajust d'offset

Sistemes de Mesura · **Unitat 10 — Condicionament singular de senyals** · Document 2 de 5

# Amplificadors de baixes derives: compensació de la polarització i ajust d'offset

Dedicació estimada: 10 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Escriure les condicions que ha de satisfer un amplificador destinat a un senyal de microvolts amb contingut fins a la contínua.
> - Decidir si la compensació dels corrents de polarització amb una resistència auxiliar és aplicable a una tecnologia d'entrada donada.
> - Reconèixer el guany de soroll com el factor que multiplica la tensió d'offset a la sortida.
> - Dimensionar una xarxa externa de compensació d'offset i la seva tensió de referència.
> - Justificar les limitacions de qualsevol compensació estàtica davant d'excursions tèrmiques i d'envelliment.

La mesura de temperatura amb termoparells és l'aplicació industrial més estesa del problema que motiva aquest document: amplificar una tensió contínua amb variacions de l'ordre del microvolt sense que els errors i les derives de l'electrònica enfosqueixin el senyal útil.

## 1 L'especificació del problema

Les sensibilitats dels termoparells van d'uns 5 μV/°C per al tipus B (platí-rodi) a uns 60 μV/°C per al tipus E (crom-constantà), amb els valors intermedis dels tipus K (41 μV/°C), J (52 μV/°C), T (43 μV/°C) i N (39 μV/°C). Resoldre una dècima de grau amb un tipus K vol dir discriminar canvis de 4,1 μV; resoldre una centèsima —exigència gens excepcional en metrologia o en calorimetria— desplaça la resolució a 0,41 μV, ja dins del terreny on el soroll tèrmic d'una resistència de pocs kΩ i l'agitació tèrmica del parell diferencial d'entrada són comparables al senyal.

El contingut freqüencial del senyal agreuja el problema. Les dinàmiques tèrmiques dels forns industrials, dels processos químics, dels rodaments d'una màquina o d'un cos humà rarament presenten variacions significatives per sobre d'alguns hertzs, de manera que gran part de la potència espectral es concentra entre la contínua i fraccions d'hertz. Aquesta és exactament la regió on l'operacional real presenta els seus pitjors defectes: les derives d'offset són contínues per definició i ocupen exactament la mateixa banda que el senyal útil —de manera que la separació entre totes dues per filtratge lineal queda descartada—, el soroll 1/f hi és màxim i els errors associats als corrents de polarització són estrictament de contínua. Amb derives d'uns quants μV/°C i sensibilitats de μV/°C, la lectura final pot acabar informant de la temperatura de la pròpia electrònica.

> [!WARNING] **Especificació de l'amplificador**
>
> Entrada diferencial  $V_{\text{in}}(t)$  contínua o de molt baixa freqüència, de microvolts a desenes de microvolts, portada al rang d'un convertidor A/D (0–3,3 V, 0–5 V o ±10 V) amb un guany  $G$  que sovint se situa entre 100 i 1000, repartit en una cascada de diverses etapes. La resposta freqüencial ha d'incloure la contínua i l'amplada de banda útil es limita a uns quants hertzs, que és on hi ha el senyal. Cinc condicions simultànies:
>
> 1. La tensió d'offset referida a l'entrada ha de ser molt menor que el senyal mínim a detectar, típicament almenys deu vegades menor.
> 2. La deriva d $V_{\text{os}}$ /d $T$, multiplicada per l'excursió tèrmica previsible de l'electrònica, ha d'introduir un error inferior a la resolució desitjada.
> 3. Els corrents  $I_{B+}$,  $I_{B-}$  i  $I_{\text{OS}}$, multiplicats per les resistències del circuit, han de produir errors de contínua menyspreables davant del senyal útil.
> 4. El soroll integrat sobre la banda passant del sistema ha de ser menor que la resolució de mesura.
> 5. Les derives amb l'envelliment s'han de mantenir per sota del llindar acceptable entre calibratges successius.

Si la resolució requerida és  $r$  i el guany  $G$, la primera condició es tradueix en  $V_{\text{os}} \ll r/G$: el criteri de tolerància es refereix sempre a l'entrada i es compara amb el senyal mínim que es vol distingir. Les estratègies disponibles es poden ordenar per complexitat creixent: compensació amb components passius sobre operacionals discrets de qualitat raonable, ajust d'offset intern amb els pins de *trimming* que ofereixen alguns dispositius, i amplificadors de molt baixes derives que corregeixen dinàmicament els errors. Una solució del primer tipus exigeix recalibratge periòdic, però és molt més econòmica.

## 2 Compensació dels corrents de polarització

La tècnica més clàssica afegeix una resistència auxiliar  $R_3$  en sèrie amb el terminal no inversor, de valor igual al paral·lel de les resistències que veu el terminal inversor. Substitueix un error proporcional a  $I_B$  per un error proporcional a  $I_{\text{OS}}$, i per tant és efectiva exactament quan  $I_{\text{OS}}$  és apreciablement menor que  $I_B$.

| Tecnologia d'entrada | Relació  $I_{\text{OS}}/I_B$ | Conseqüència |
|:--- |:--- |:--- |
| Bipolar | 0,1 a 0,25 | La substitució redueix l'error entre quatre i deu vegades. És la situació en què la tècnica té sentit. |
| FET i CMOS | Del mateix ordre que 1 | $I_B$  és ja molt reduït (pA o fA) i les asimetries del parell diferencial fan  $I_{\text{OS}}$  comparable. Es prefereix ometre  $R_3$  i triar un amplificador amb  $I_B$  prou petit perquè els errors siguin acceptables. |

La resistència afegida té dos costos propis: aporta el seu soroll tèrmic i pot captar interferències electromagnètiques, especialment si el seu valor és elevat. En amplificadors de precisió moderns amb cancel·lació interna de polarització la tècnica ha perdut bona part del seu interès; era crucial en bipolars antics com el μA741 i continua essent necessària per comprendre disseny heretat i per a projectes on l'amplificador escollit no disposa de cancel·lació interna.

## 3 Compensació de la tensió d'offset

> [!WARNING] **Guany de soroll**
>
> Factor pel qual queda multiplicada, a la sortida, una tensió present entre els terminals d'entrada de l'amplificador. Per a les topologies inversora i no inversora amb  $R_1$  i  $R_2$  val  $1 + R_2/R_1$. La tensió d'offset i les fonts de soroll de tensió referides a l'entrada hi queden afectades, mentre que el senyal d'entrada rep el guany de senyal, que en la topologia inversora és  $-R_2/R_1$.

Amb guanys alts, l'efecte de  $V_{\text{os}}$  a la sortida pot consumir una part significativa del rang dinàmic o portar a la saturació un amplificador realimentat. Hi ha dues famílies d'estratègies d'ajust: interna, dins del mateix integrat, i externa, amb una xarxa de components addicionals.

### Ajust intern

![Amplificador operacional en càpsula de 8 pins amb un potenciòmetre connectat entre els pins 1 i 8 d'offset null i el terminal central a l'alimentació negativa.](assets/02_Unitat10_Amplificadors_de_baixes_derives_img_1.png)

*Figura: Figura 10.4 Compensació interna de $V_{\text{os}}$ amb potenciòmetre extern.*

Alguns amplificadors —típicament els de precisió en càpsules DIP de 8 pins— disposen de dos pins addicionals d'*offset null*, tradicionalment l'1 i el 8. S'hi connecta un potenciòmetre extern, habitualment de 10 a 100 kΩ, amb el terminal central a l'alimentació negativa o positiva segons el fabricant. Ajustant-lo amb les entrades curtcircuitades es modifiquen les tensions en nodes interns del parell diferencial d'entrada i s'anul·la  $V_{\text{os}}$  amb una precisió típica de centenars de nanovolts. L'operació és senzilla i eficaç a una temperatura donada, i té dues limitacions rellevants.

- **Degradació tèrmica.** L'ajust elimina  $V_{\text{os}}$  a la temperatura del calibratge. Si la temperatura del xip canvia,  $V_{\text{os}}$  reapareix amb un coeficient d $V_{\text{os}}$ /d $T$  que sovint és més gran que el del dispositiu sense ajustar: el fabricant especifica el coeficient en la configuració sense ajust, i l'ajust el pot empitjorar fins a un factor 2 o 3.
- **Marge d'ajust finit i intervenció manual.** Requereix accés físic al potenciòmetre, i si l'envelliment porta  $V_{\text{os}}$  fora del marge d'ajust la correcció deixa de ser possible.

L'ajust intern és, doncs, recomanable en aplicacions amb temperatura ambient estable —laboratoris, instrumentació de camp amb recintes termostatitzats— i amb recalibratges planificats. Per a aplicacions industrials amb excursions tèrmiques amples, les estratègies dinàmiques donen millor resultat.

### Compensació externa

La compensació externa injecta, a través d'una xarxa de resistències, una petita tensió de correcció al terminal adequat, dissenyada per cancel·lar l'efecte de  $V_{\text{os}}$. S'implementa amb un potenciòmetre format per dues resistències  $R_A$  i  $R_B$  alimentat entre dues tensions simètriques  $+V_r$  i  $-V_r$  derivades d'una referència estable. La tensió del punt central,  $V_x$, s'introdueix al circuit a través d'una resistència  $R_3$  de valor molt superior a  $R_A$  i  $R_B$. Funciona amb qualsevol amplificador operacional, sense necessitat de pins de *trimming* específics.

![Amplificador inversor amb R1 d'entrada i R2 de realimentació; la tensió Vx del punt central d'un potenciòmetre RA-RB alimentat entre −VR i +VR s'injecta al terminal inversor a través de R3.](assets/02_Unitat10_Amplificadors_de_baixes_derives_img_2.png)

*Figura: Figura 10.5 Compensació externa de $V_{\text{os}}$ en un amplificador inversor.*

Per a l'amplificador inversor de guany  $-R_2/R_1$, la superposició de  $V_{\text{in}}$,  $V_x$  i  $V_{\text{os}}$  dona

$$
V_{\text{out}} = -V_{\text{in}}\cdot\frac{R_2}{R_1} - V_x\cdot\frac{R_2}{R_3} + V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.3)
$$

El segon i el tercer terme s'anul·len mútuament quan

$$
V_x = V_{\text{OS}}\cdot\frac{R_3}{R_2}\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.4)
$$

i, sempre que  $V_x$  caigui dins del marge d'ajust  $(-V_r, +V_r)$, la sortida recupera el guany de senyal nominal:

$$
V_{\text{out}} = -V_{\text{in}}\cdot\frac{R_2}{R_1} \qquad (10.5)
$$

![Amplificador inversor amb la mateixa xarxa de compensació d'offset i, a més, una resistència Rp entre el terminal no inversor i massa; R3 hi arriba des del potenciòmetre.](assets/02_Unitat10_Amplificadors_de_baixes_derives_img_3.png)

*Figura: Figura 10.6 Compensació externa simultània de $V_{\text{os}}$ i dels corrents de polarització.*

Una versió més completa incorpora alhora la correcció del corrent de polarització amb una resistència  $R_p$  al terminal no inversor, on ara arriba també la tensió de correcció. La superposició dona

$$
V_{\text{out}} = -V_{\text{in}}\cdot\frac{R_2}{R_1} + V_x\cdot\frac{R_p}{R_p+R_3}\cdot\left(1+\frac{R_2}{R_1}\right) + V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.6)
$$

i la compensació de l'offset es produeix quan

$$
V_x = -V_{\text{OS}}\cdot\left(1+\frac{R_3}{R_p}\right) \qquad (10.7)
$$

Triant  $R_p = R_1\|R_2 \ll R_3$, l'efecte dels corrents de polarització queda cancel·lat fins al residu  $I_{\text{OS}}\cdot R_2$. La topologia ofereix, doncs, doble compensació simultània, i és la indicada per a amplificadors bipolars antics o per a aplicacions on tots dos errors són rellevants.

![Amplificador no inversor amb Vin al terminal no inversor, R1 a massa i R2 de realimentació; la tensió Vx del potenciòmetre s'injecta al terminal inversor a través de R3.](assets/02_Unitat10_Amplificadors_de_baixes_derives_img_4.png)

*Figura: Figura 10.7 Compensació externa de $V_{\text{os}}$ en un amplificador no inversor.*

Per a l'amplificador no inversor, amb  $V_{\text{in}}$  al terminal no inversor i  $V_x$  introduïda al terminal inversor a través de  $R_3$, sota la condició  $R_3 \gg R_1$:

$$
V_{\text{out}} = V_{\text{in}}\cdot\left(1+\frac{R_2}{R_1}\right) - V_x\cdot\frac{R_2}{R_3} + V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.8)
$$

La compensació requereix

$$
V_x = V_{\text{OS}}\cdot\frac{R_3}{R_2}\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.9)
$$

que és la mateixa condició que en el cas inversor.

### Tria de la tensió de referència

El marge d'ajust de  $V_x$  ha de cobrir qualsevol  $V_{\text{os}}$  dins de l'interval especificat pel fabricant, amb els dos signes. Si  $V_{os\,\max}$  és el valor màxim especificat:

$$
V_r \geq |V_{OS\,\max}|\cdot\frac{R_3}{R_2}\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.10)
$$

El marge d'ajust queda lligat, doncs, a les resistències de la mateixa xarxa d'amplificació. A la pràctica es tria  $V_r$  amb un marge addicional del 20 % al 50 % per absorbir derives temporals i dispersions de producció, i s'obté d'una referència de tensió estable —LM4040, REF02 o equivalents— en comptes dels busos d'alimentació: qualsevol soroll o variació de  $V_r$  entra al senyal com un error propi de la correcció.

> [!WARNING] **Abast de qualsevol compensació estàtica**
>
> L'ajust —intern o extern— cancel·la  $V_{\text{os}}$  a la temperatura i en l'instant del calibratge. La deriva tèrmica d $V_{\text{os}}$ /d $T$  del propi amplificador i l'envelliment tornen a generar error quan les condicions canvien, de manera que el pressupost d'error i la periodicitat de recalibratge s'han de calcular igualment.

> [!TIP] **Síntesi**
>
> Amplificar microvolts amb contingut fins a la contínua imposa cinc condicions simultànies sobre offset, deriva tèrmica, corrents de polarització, soroll integrat i envelliment, amb el criteri de tolerància referit sempre a l'entrada. La resistència auxiliar  $R_3 = R_1\|R_2$  canvia un error proporcional a  $I_B$  per un de proporcional a  $I_{\text{OS}}$, cosa que compensa en bipolars, on  $I_{\text{OS}}/I_B$  val entre 0,1 i 0,25, i aporta soroll tèrmic propi. La tensió d'offset queda multiplicada pel guany de soroll  $1+R_2/R_1$, i amb guanys alts pot consumir rang dinàmic o saturar la sortida. L'ajust intern amb pins d'*offset null* anul·la  $V_{\text{os}}$  en un punt de treball i pot empitjorar la deriva tèrmica fins a un factor 2 o 3; la compensació externa injecta  $V_x$  a través de  $R_3$  i funciona amb qualsevol operacional, amb la mateixa condició de compensació en les topologies inversora i no inversora. La tensió de referència del potenciòmetre ha de ser estable i el seu marge ha de cobrir el pitjor offset especificat més un marge del 20 % al 50 %.

[← 1. Condicionament singular: sensors, l'operacional real i les seves derives](#condicionament-singular-sensors-loperacional-real-i-les-seves-derives)[3. Amplificadors chopper i amplificadors amb autozero →](#amplificadors-chopper-i-amplificadors-amb-autozero)

---

<!-- FIN CAPÍTULO: 02_Unitat10_Amplificadors_de_baixes_derives -->

---

<!-- INICIO CAPÍTULO: 03_Unitat10_Chopper_i_autozero -->

# Amplificadors chopper i amplificadors amb autozero

Sistemes de Mesura · **Unitat 10 — Condicionament singular de senyals** · Document 3 de 5

# Amplificadors chopper i amplificadors amb autozero

Dedicació estimada: 10 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar per què modular el senyal a una freqüència de commutació redueix l'efecte dels errors de baixa freqüència.
> - Seguir el senyal i els errors al llarg de la cadena d'un amplificador chopper, en el temps i en la freqüència.
> - Deduir el guany en llaç tancat d'un chopper i relacionar-lo amb el d'un amplificador convencional.
> - Descriure les dues fases d'un amplificador amb autozero i obtenir-ne la tensió d'offset efectiva.
> - Aplicar un procediment de selecció d'amplificador a partir de l'error dominant i de les restriccions pràctiques.

Quan ni la compensació passiva ni el *trimming* intern redueixen les derives al nivell requerit, cal recórrer a amplificadors que corregeixin dinàmicament els seus propis errors. Els dos grans tipus són els amplificadors chopper i els amplificadors amb autozero.

## 1 Amplificadors chopper

La idea dels amplificadors chopper, o trossejats, és traslladar el senyal útil a una zona freqüencial lliure dels errors de baixa freqüència de l'amplificador, amplificar-lo allà i tornar-lo a la banda base.

![Diagrama intern d'un amplificador chopper: commutador d'entrada S1 governat per un oscil·lador, desacoblament de contínua, amplificador de banda ampla A1, segon desacoblament, commutador desmodulador S2, filtre passabaixes amb l'integrador A2 i xarxa de realimentació R1-R2; a sota, les formes d'ona als punts interns.](assets/03_Unitat10_Chopper_i_autozero_img_1.png)

*Figura: Figura 10.8 Diagrama intern d'un amplificador chopper i senyals interns.*

> [!WARNING] **Freqüència de commutació**
>
> Freqüència  $f_{\text{ch}}$  de l'oscil·lador intern que governa els dos commutadors, habitualment entre algunes centenes de Hz i algunes desenes de kHz. Se selecciona prou alta perquè el senyal modulat quedi lluny de la zona de soroll 1/f i de les derives.

El commutador d'entrada modula  $V_{\text{in}}$  amb un senyal quadrat de freqüència  $f_{\text{ch}}$  i converteix la component contínua o de baixa freqüència en una oscil·lació a  $f_{\text{ch}}$  d'amplitud proporcional a  $V_{\text{in}}$. L'amplificador intern  $A_1$  l'amplifica amb un guany elevat, i hi afegeix els seus propis errors de contínua, derives i soroll 1/f, que apareixen com a contínua o baixa freqüència a la seva sortida. Un segon commutador, el desmodulador síncron, opera amb la mateixa fase que el primer: retorna el senyal útil a contínua i, simultàniament, trasllada els errors de banda base cap a  $f_{\text{ch}}$  i els seus harmònics. Un filtre passabaixes posterior els elimina juntament amb els residus de la modulació. Com que el gruix del guany correspon a  $A_1$, els errors de baixa freqüència del filtre de sortida —sobretot els de  $A_2$  si el filtre és actiu— gairebé no afecten la deriva de la tensió de sortida.

| Punt | Contingut |
|:--- |:--- |
| $V_1$ | Ona quadrada que pren el valor  $V_{\text{in}}$  durant el 50 % del temps i  $V_{\text{out}}\cdot R_1/(R_1+R_2)$  l'altre 50 %; valor mitjà  $[V_{\text{in}} + V_{\text{out}}R_1/(R_1+R_2)]/2$. |
| $V_2$ | La mateixa ona després del desacoblament de contínua: quadrada sense component contínua, de valors  $\pm[V_{\text{in}} - V_{\text{out}}R_1/(R_1+R_2)]/2$. |
| $V_3$ | $A_1 V_2 + e_3$, on  $e_3$  recull els errors de contínua, les derives i el soroll 1/f referits a la sortida de  $A_1$. |
| $V_4$ | Idealment  $A_1 V_2$, després del filtratge passaalt que retira  $e_3$. |
| $V_5$ | Ona quadrada de sortida del desmodulador, de valor mínim 0 i valor màxim  $A_1 V_{2\,\max}$; el seu valor mitjà,  $A_1 V_{2\,\max}/2$, és el senyal de sortida després del filtre passabaixes. |

D'aquí,  $V_{\text{out}} = A_1\cdot[V_{\text{in}} - V_{\text{out}}R_1/(R_1+R_2)]/2$  i, aïllant,

$$
V_{\text{out}} = \frac{A_1/2}{1 + A_1\cdot R_1/[2(R_1+R_2)]}\cdot V_{\text{in}} \qquad (10.11)
$$

que amb  $A_1 \gg 1$, com correspon al guany en llaç obert d'un operacional real, tendeix a

$$
V_{\text{out}} = V_{\text{in}}\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.12)
$$

És l'expressió del guany d'un amplificador no inversor convencional: l'arquitectura chopper hi afegeix la cancel·lació dels errors de contínua i el guany en llaç tancat continua fixat per la xarxa de realimentació externa.

![Model freqüencial del chopper: multiplicador M1 a f_CH, suma del soroll amb densitat 1/f, amplificador A1, multiplicador M2 a f_CH i filtre passabaixes; a sota, els espectres de V_IN, V_M1, V_M2 i V_OUT en múltiples de f/f_CH.](assets/03_Unitat10_Chopper_i_autozero_img_2.png)

*Figura: Figura 10.9 Amplificador chopper en el domini freqüencial.*

En el domini freqüencial, la modulació converteix  $V_{\text{in}}$  —continu o de molt baixa freqüència— en un senyal amb contingut a  $f_{\text{ch}}$  i als seus harmònics imparells. Els errors i el soroll de baixa freqüència de l'amplificador se sumen en banda base, mentre que el senyal útil amplificat es troba centrat a  $f_{\text{ch}}$. El desmodulador síncron, multiplicant de nou per l'ona quadrada, porta el senyal útil de tornada a contínua i puja els errors cap a  $f_{\text{ch}}$  i harmònics; el filtre passabaixes, amb freqüència de tall molt per sota de  $f_{\text{ch}}$, deixa passar només el senyal útil recuperat i atenua dràsticament tant els errors com els residus de modulació. Com que el soroll 1/f cau a mesura que s'allunya de la contínua i la modulació l'envia a freqüències de l'ordre del kHz, la potència residual en banda base és extraordinàriament reduïda.

| Limitació | Abast |
|:--- |:--- |
| **Amplada de banda útil** | Queda limitada a una fracció de  $f_{\text{ch}}$, perquè el filtre de sortida ha de tallar molt per sota de la freqüència de commutació. Amb  $f_{\text{ch}}$  = 10 kHz, la banda útil és típicament inferior a 1 kHz. Per a senyals més ràpids cal triar dispositius amb  $f_{\text{ch}}$  elevada. |
| **Soroll blanc efectiu** | Pot ser una mica més alt que en amplificadors convencionals equivalents, perquè el procés de modulació i desmodulació plega soroll de bandes laterals cap a la banda base. |
| **Residus de commutació** | La commutació interna deixa a la sortida artefactes o *ripple* a  $f_{\text{ch}}$  i harmònics, que el filtre atenua i que cal considerar en sistemes de molt alta resolució. |

## 2 Amplificadors amb autozero

Els amplificadors amb autozero resten dinàmicament els errors de zero dels seus amplificadors interns mitjançant un sistema de doble fase i emmagatzematge capacitiu de les correccions.

![Principi de l'amplificador d'autozero: amplificador principal Am amb entrada de correcció Vc2, amplificador de correcció An amb entrada Vc1, dos commutadors S1 i S2 governats per un oscil·lador i dos condensadors C1 i C2 que emmagatzemen les tensions de correcció.](assets/03_Unitat10_Chopper_i_autozero_img_3.png)

*Figura: Figura 10.10 Principi de funcionament dels amplificadors amb autozero.*

El circuit consta de dos amplificadors interns: el principal  $A_m$  (*main*) i el de correcció o de *nulling*,  $A_n$. Cadascun té una entrada diferencial per al senyal i una entrada unipolar de correcció d'offset — $V_{c1}$  per a  $A_n$  i  $V_{c2}$  per a  $A_m$ —, i dos condensadors, externs o integrats, hi emmagatzemen aquestes tensions entre cicles. Es caracteritzen pel guany diferencial ( $A_m$,  $A_n$ ) i pel guany respecte de la tensió d'ajust unipolar ( $B_m$  per a  $A_m$  i  $-B_n$  per a  $A_n$, amb signe oposat per raons de correcció). El disseny imposa  $A_m = A_n = A$,  $B_m = B_n = B$  i  $B \gg 1$.

Un oscil·lador intern alterna dues fases a una freqüència de l'ordre del kHz. En la **fase d'autozero**, amb els commutadors a la posició 1,  $A_n$  té les entrades curtcircuitades internament i la seva sortida val

$$
V_{c1} = A_n\cdot V_{\text{osn}} - B_n\cdot V_{c1} \qquad (10.13)
$$

d'on

$$
V_{c1} = V_{\text{osn}}\cdot\frac{A_n}{1+B_n} \qquad (10.14)
$$

En la **fase d'amplificació**, amb els commutadors a la posició 2,  $A_n$  mesura  $V_{\text{in}} + V_{\text{osn}}$  i actualitza  $V_{c2}$:

$$
V_{c2} = A_n\cdot(V_{\text{in}}+V_{\text{osn}}) - B_n\cdot V_{c1} \qquad (10.15)
$$

Substituint-hi  $V_{c1}$,

$$
V_{c2} = A_n\cdot V_{\text{in}} + A_n\cdot V_{\text{osn}}\cdot\frac{1}{1+B_n} \qquad (10.16)
$$

La tensió de sortida no canvia entre les dues fases, perquè les entrades d' $A_m$  no commuten:

$$
V_{\text{out}} = A_m\cdot(V_{\text{in}}+V_{\text{osm}}) + B_m\cdot V_{c2} \qquad (10.17)
$$

i amb  $V_{c2}$  substituïda,

$$
V_{\text{out}} = A_m\cdot(V_{\text{in}}+V_{\text{osm}}) + B_m\cdot A_n\cdot V_{\text{in}} + \frac{B_m\cdot A_n\cdot V_{\text{osn}}}{1+B_n} \qquad (10.18)
$$

Agrupant termes,

$$
V_{\text{out}} = (A_m + B_m\cdot A_n)\cdot V_{\text{in}} + A_m\cdot V_{\text{osm}} + \frac{B_m\cdot A_n\cdot V_{\text{osn}}}{1+B_n} \qquad (10.19)
$$

i imposant  $A_m = A_n = A$,  $B_m = B_n = B$  amb  $B \gg 1$,

$$
V_{\text{out}} \approx A\cdot B\cdot V_{\text{in}} + A\cdot(V_{\text{osm}}+V_{\text{osn}}) \qquad (10.20)
$$

Escrit en la forma estàndard  $V_{\text{out}} \approx k\cdot(V_{\text{in}}+V_{\text{oeff}})$, el guany de senyal és  $k = A\cdot B$  i

$$
V_{\text{oeff}} = \frac{V_{\text{osm}}+V_{\text{osn}}}{B} \qquad (10.21)
$$

La tensió d'offset efectiva és un factor  $B$  més petita que la dels amplificadors interns: amb  $B$  = 1000, un  $V_{\text{osm}}$  d'1 mV es redueix a 1 μV. El guany del conjunt,  $A\cdot B$, és extraordinàriament gran, i per fer-lo servir com a amplificador operacional cal tancar una xarxa de realimentació entre  $V_{\text{out}}$  i l'entrada, que és qui fixa el guany en llaç tancat.

> [!WARNING] **Arquitectures híbrides**
>
> Molts amplificadors comercials moderns combinen autozero i chopper en el mateix dispositiu —*chopper stabilized*, o amplificadors de zero estabilitzat—, i n'aprofiten els avantatges respectius. El fabricant no sempre en detalla l'arquitectura interna; el resultat és una oferta de components amb  $V_{\text{os}}$  de l'ordre del microvolt i derives de desenes de nanovolts per grau. Un exemple clàssic, el LTC1050, dona  $V_{\text{os}}$  màxima de 5 μV, deriva de 0,05 μV/°C,  $I_B$  típica d'1 pA, soroll d'1,6 μV pic a pic a la banda de 0,1 a 10 Hz i freqüència interna de modulació d'uns 500 Hz.

| Aspecte | Chopper | Autozero |
|:--- |:--- |:--- |
| Mecanisme | Modulació del senyal a  $f_{\text{ch}}$, amplificació i desmodulació síncrona. | Mesura periòdica de l'error de zero i resta dinàmica amb dos amplificadors interns. |
| On es guarda la correcció | El desplaçament freqüencial no en necessita cap: els errors surten de la banda amb la desmodulació. | En dos condensadors, que conserven les tensions  $V_{c1}$  i  $V_{c2}$  entre fases. |
| Efecte sobre el soroll 1/f | El senyal s'amplifica fora de la zona de pitjor soroll, i el residu en banda base és molt petit. | La resta periòdica de l'error cancel·la també la component lenta. |
| Guany en llaç tancat | El fixa la xarxa de realimentació externa en totes dues arquitectures. |  |
| Preu a pagar | Banda útil limitada a una fracció de  $f_{\text{ch}}$, plegament de soroll de bandes laterals i residus de commutació. | Artefactes de la commutació entre fases i corrent de polarització de picoampers, procedent dels commutadors i dels condensadors. |

## 3 Criteris de selecció

1. **Tensió d'offset màxima tolerable**, a partir del nivell mínim de senyal i del guany del circuit: amb resolució  $r$  i guany  $G$,  $V_{\text{os}} \ll r/G$.
2. **Deriva tèrmica** multiplicada per l'excursió tèrmica previsible, amb el mateix criteri.
3. **Corrent de polarització** en relació amb les impedàncies del circuit —sensor i xarxa de guany—. Si el producte  $I_B\cdot R$  és comparable al nivell de senyal, cal optar per tecnologies FET o CMOS, o afegir la compensació amb resistència auxiliar en bipolars.
4. **Soroll integrat** sobre la banda passant del sistema, amb atenció particular al soroll 1/f si la banda inclou freqüències molt baixes. La banda del condicionador s'ha de limitar al necessari, també en dispositius de correcció dinàmica.
5. **Compatibilitat de les tensions d'alimentació** amb l'arquitectura del sistema.
6. **Consum, cost i disponibilitat comercial**, que formen part dels criteris reals de selecció al costat de les especificacions metrològiques. La solució de menor deriva i la més econòmica rarament coincideixen.

| Situació | Família indicada |
|:--- |:--- |
| Termoparells amb resolucions millors que 0,1 °C en marges tèrmics ambientals amplis | Autozero, com a primera opció, per l'estabilitat de zero. |
| Temperatura ambient controlada | Bipolar de precisió, alternativa vàlida i sovint més econòmica. |
| Sensors d'impedància alta, on domina el corrent de polarització | FET o CMOS, escollits pel seu  $I_B$. |

> [!TIP] **Síntesi**
>
> Els amplificadors chopper modulen el senyal a la freqüència de commutació  $f_{\text{ch}}$, l'amplifiquen lluny de la zona de soroll 1/f i el retornen a banda base amb un desmodulador síncron, mentre els errors de l'etapa interna es traslladen a  $f_{\text{ch}}$  i els elimina el filtre passabaixes. El guany en llaç tancat continua essent  $1+R_2/R_1$, fixat per la xarxa externa. A canvi, la banda útil queda limitada a una fracció de  $f_{\text{ch}}$, el soroll blanc efectiu pot pujar pel plegament de bandes laterals i la commutació deixa residus a la sortida. Els amplificadors amb autozero alternen una fase de mesura de l'error de zero i una d'amplificació, guarden les correccions en condensadors i deixen una tensió d'offset efectiva  $(V_{\text{osm}}+V_{\text{osn}})/B$, un factor  $B$  per sota de la dels amplificadors interns. La selecció d'un dispositiu concret encadena sis criteris: offset tolerable referit a l'entrada, deriva per l'excursió tèrmica, corrent de polarització per les impedàncies del circuit, soroll integrat a la banda, alimentació, i consum, cost i disponibilitat.

[← 2. Amplificadors de baixes derives: compensació de la polarització i ajust d'offset](#amplificadors-de-baixes-derives-compensació-de-la-polarització-i-ajust-doffset)[4. Amplificadors electromètrics i de transimpedància →](#amplificadors-electromètrics-i-de-transimpedància)

---

<!-- FIN CAPÍTULO: 03_Unitat10_Chopper_i_autozero -->

---

<!-- INICIO CAPÍTULO: 04_Unitat10_Electrometrics_i_transimpedancia -->

# Amplificadors electromètrics i de transimpedància

Sistemes de Mesura · **Unitat 10 — Condicionament singular de senyals** · Document 4 de 5

# Amplificadors electromètrics i de transimpedància

Dedicació estimada: 14 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Triar entre el model de Thevenin i el de Norton d'un sensor d'alta impedància segons la topologia de condicionament.
> - Enunciar les condicions de funcionament d'un amplificador electromètric i el seu efecte sobre la resposta freqüencial.
> - Obtenir la relació entrada–sortida d'un amplificador de transimpedància i identificar-ne les fonts d'error de contínua i de soroll.
> - Calcular la transimpedància equivalent d'una xarxa en T i valorar-ne el cost en offset i en soroll.
> - Justificar les tècniques de disseny físic que fan viable una mesura a impedàncies de teraohms.

D'aquests sensors, el que condiciona el disseny no és el nivell de tensió —que pot ser de desenes de mil·livolts o de volts, perfectament manejable— sinó que qualsevol amplificador convencional, en connectar-s'hi, els carrega dràsticament: imposa una impedància de càrrega paral·lela comparable o menor a la de sortida del sensor, que desvia gran part del senyal cap a massa. Els exemples canònics són els sensors piezoelèctrics i piroelèctrics, modelables com a fonts de tensió o de càrrega amb una capacitat i una resistència de fuita molt elevada en paral·lel; els fotodíodes, que en certs modes es comporten com a fonts de corrent d'impedància molt alta; els fototransistors; i els sensors químics com les sondes de pH o els elèctrodes de ió selectiu, amb impedàncies internes que poden arribar als gigaohms.

Amb impedàncies d'entrada de MΩ i corrents de polarització de nanoampers, l'operacional de propòsit general hi falla per partida doble: el producte  $I_B\cdot R$  del propi amplificador supera la tensió útil del sensor, i la impedància d'entrada deriva el senyal cap a massa fins a fer-lo desaparèixer. Quan la impedància de sortida és capacitiva, el conjunt sensor–amplificador es comporta a més com un filtre passaalt la freqüència de tall del qual depèn dels paràmetres paràsits del cablejat i de l'entrada, de manera que les components lentes del senyal poden quedar filtrades. Cal, doncs, impedàncies d'entrada de l'ordre de TΩ, corrents de polarització de fA o pA i un bon control de les capacitats i fuites paràsites del circuit imprès.

## 1 Thevenin o Norton: quina topologia

Qualsevol sensor lineal admet les dues representacions equivalents: font de tensió  $V_s$  amb  $Z_s$  en sèrie, o font de corrent  $I_s = V_s/Z_s$  amb  $Z_s$  en paral·lel. Són dues descripcions del mateix sensor, i la tria és de conveniència: amb  $Z_s$  petita el model Thevenin és el natural, i amb  $Z_s$  gran, que és el cas dels sensors d'alta impedància, el model Norton sol resultar més útil perquè  $I_s$  és un paràmetre relativament estable i ben caracteritzat.

| Model | Què es demana a l'amplificador | Topologia |
|:--- |:--- |:--- |
| **Thevenin** ( $V_s$,  $Z_s$  en sèrie) | Impedància d'entrada molt més gran que  $Z_s$, perquè el divisor de tensió no degradi el senyal. | Amplificador **electromètric** en configuració no inversora o seguidora, amb  $Z_{\text{in}}$  de TΩ. |
| **Norton** ( $I_s$,  $Z_s$  en paral·lel) | Impedància d'entrada molt petita, idealment un curtcircuit, perquè tot  $I_s$  flueixi cap a l'amplificador. | Amplificador de **transimpedància**, basat en el curtcircuit virtual de l'operacional. |

Sota hipòtesis generoses les dues topologies són equivalents, i triar-ne una o l'altra depèn de les prestacions concretes de l'operacional disponible. A la pràctica, la de transimpedància és la més utilitzada amb fotodíodes i amb sensors piezoelèctrics en règim de corrent, pels avantatges que presenta en resposta freqüencial.

## 2 Amplificadors electromètrics

![Amplificador no inversor amb el sensor modelat com a font de tensió Vs en sèrie amb Zs connectada al terminal no inversor, i R1 a massa i R2 de realimentació al terminal inversor.](assets/04_Unitat10_Electrometrics_i_transimpedancia_img_1.png)

*Figura: Figura 10.11 Amplificador electromètric.*

Un amplificador electromètric és un operacional no inversor on el component escollit presenta una impedància d'entrada extraordinàriament elevada —TΩ o superior— i un corrent de polarització molt reduït, de fA a pA. Aquestes prestacions s'aconsegueixen gairebé sempre amb etapes d'entrada FET o CMOS, sovint amb tècniques addicionals. El funcionament correcte demana dues condicions.

- La impedància d'entrada de l'amplificador ha de superar  $Z_s$  com a mínim en dos o tres ordres de magnitud, de manera que el divisor format per  $Z_s$  i  $Z_{\text{in}}$  no degradi apreciablement el senyal.
- El corrent  $I_{B+}$  ha de ser prou petit perquè la caiguda  $I_{B+}\cdot R_s$, amb  $R_s$  la part resistiva de  $Z_s$  en contínua, deixi prou marge dinàmic per amplificar  $V_s$.

Sota aquestes hipòtesis el comportament és el d'un no inversor convencional:

$$
V_{\text{out}} = V_s\cdot\left(1+\frac{R_2}{R_1}\right) \qquad (10.22)
$$

Si la impedància d'entrada finita és comparable a  $Z_s$, la tensió efectiva del sensor passa a ser

$$
V_{s\,eff} = V_s\cdot\frac{Z_{\text{in}}}{Z_s+Z_{\text{in}}} \qquad (10.23)
$$

i, quan  $Z_s$  i  $Z_{\text{in}}$  tenen dependències freqüencials diferents, el sistema deixa de tenir resposta plana.

| Magnitud | Valor |
|:--- |:--- |
| Sensibilitat teòrica a 25 °C (equació de Nernst) | 59,16 mV/pH |
| Excursió de sortida entre pH 0 i pH 14 | de +414 mV a −414 mV |
| Impedància de sortida de l'elèctrode de vidre | de 10 MΩ a 1 GΩ |
| Error de contínua amb  $I_B$  = 40 fA sobre 1 GΩ | 40 μV |

El senyal no demana gaire amplificació per poder-se digitalitzar; el problema és la impedància, que varia amb el disseny, l'envelliment i la temperatura. Amb un error de contínua de desenes de microvolts davant de centenars de mil·livolts de senyal, un component electromètric hi és perfectament adequat, connectat en configuració seguidora —guany unitat— per desacoblar la sonda de la resta del sistema, i amplificant i digitalitzant després amb tècniques convencionals.

## 3 Amplificadors de transimpedància

![Amplificador de transimpedància: el sensor modelat com a font de corrent Is amb Zs en paral·lel s'injecta al terminal inversor, amb R de realimentació entre sortida i terminal inversor i el terminal no inversor a massa.](assets/04_Unitat10_Electrometrics_i_transimpedancia_img_2.png)

*Figura: Figura 10.12 Amplificador de transimpedància.*

L'amplificador de transimpedància (TIA) és una configuració inversora on el corrent del sensor s'injecta directament al terminal inversor i la realimentació es tanca amb una resistència  $R$  entre la sortida i aquest mateix terminal; el terminal no inversor va a massa. Amb les dues hipòtesis de l'operacional ideal —cap corrent entra pels terminals d'entrada i la tensió entre ells és zero—, el node inversor queda virtualment a massa, el sensor hi veu una impedància d'entrada nul·la, tot el corrent  $I_s$  circula per  $R$  i la llei d'Ohm dona

$$
V_{\text{out}} = I_s\cdot R \qquad (10.24)
$$

> [!WARNING] **Transimpedància**
>
> Constant de conversió corrent–tensió del circuit, igual a  $R$  en el cas resistiu ideal. La funció de transferència és un quocient V/I, és a dir una impedància, i es mesura en ohms o, més generalment, en volts per ampere.

El TIA anul·la l'efecte de  $Z_s$  sobre el guany de senyal, cosa que el fa particularment útil quan  $Z_s$  és capacitiva i, per tant, dependent de la freqüència. L'operacional real, però, té un guany en llaç obert finit que decreix amb la freqüència, un corrent de polarització no nul, una capacitat d'entrada paràsita  $C_{\text{in}}$  i soroll propi. La combinació de  $R$  amb les capacitats del node inversor forma un pol al llaç de realimentació que pot provocar inestabilitat, i per això és habitual afegir una capacitat  $C_f$  en paral·lel amb  $R$, que estabilitza el circuit i limita la banda útil. Se'n deriven dues conseqüències pràctiques: l'amplada de banda útil del TIA sovint és força inferior a la de l'operacional subjacent, especialment amb  $Z_s$  molt capacitiva; i el soroll a la sortida augmenta a altes freqüències pel factor  $1+C_s/C_f$  —el *noise gain peak*—, cosa que reforça la conveniència de limitar la banda al mínim necessari.

### Errors de contínua i soroll

![Model del TIA per a l'anàlisi d'errors: Zs a l'entrada, font de corrent Ib−+In−(f) al node inversor, font Vos i font de soroll en(f) al terminal no inversor, i R de realimentació amb la seva font de soroll eR.](assets/04_Unitat10_Electrometrics_i_transimpedancia_img_3.png)

*Figura: Figura 10.13 Model per a l'anàlisi dels errors de contínua i del soroll en un amplificador de transimpedància.*

Aplicant superposició amb el senyal útil anul·lat, la tensió de sortida deguda als errors és

$$
V_{\text{out}} = V_{\text{OS}}\cdot\left(1+\frac{R}{Z_s}\right) - I_{B-}\cdot R \qquad (10.25)
$$

El primer terme queda pròxim a  $V_{\text{OS}}$  perquè  $Z_s$  sol ser molt més gran que  $R$. El segon,  $I_{B-}\cdot R$, és sovint el dominant en amplificadors FET i CMOS d'alta impedància, i és la raó principal per la qual s'exigeixen corrents de polarització de femtoampers quan  $R$  és molt gran: amb  $I_B$  = 1 pA i  $R$  = 1 GΩ, l'error de contínua a la sortida és d'1 mV.

![Model de l'amplificador electromètric per a l'anàlisi d'errors: Zs al terminal no inversor amb les fonts Vos, en(f) i Ib++In+(f), R1 i R2 amb les seves fonts de soroll eR1 i eR2 i la font Ib−+In−(f) al terminal inversor.](assets/04_Unitat10_Electrometrics_i_transimpedancia_img_4.png)

*Figura: Figura 10.14 Model per a l'anàlisi dels errors de contínua i del soroll en un amplificador electromètric.*

Per a l'amplificador electromètric no inversor, l'anàlisi anàloga dona

$$
V_{\text{out}} = V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right) + I_{B+}\cdot R_s\cdot\left(1+\frac{R_2}{R_1}\right) - I_{B-}\cdot R_2 \qquad (10.26)
$$

on el terme  $I_{B+}\cdot R_s\cdot(1+R_2/R_1)$  pot dominar quan  $R_s$  és molt gran, cosa habitual en elèctrodes de pH i en sensors piezoelèctrics. La tensió d'offset hi és present amb el guany de soroll, com en qualsevol topologia realimentada.

El soroll de sortida del TIA té tres contribucions principals: el soroll de tensió de l'amplificador  $e_n(f)$, amplificat pel guany de soroll  $1+R/Z_s(f)$, que amb  $Z_s$  capacitiva creix amb la freqüència; el soroll de corrent de l'entrada inversora  $I_{n-}(f)$, multiplicat per  $R$  i molt baix —de l'ordre de fA/√Hz— en amplificadors JFET o CMOS de baixa  $I_B$; i el soroll tèrmic de la resistència,  $e_R = \sqrt{4kTR}$. La densitat espectral total a la sortida és

$$
e_{\text{nout}}(f) = \sqrt{e_n(f)^2\left(1+\frac{R}{Z_s(f)}\right)^{2} + I_{n-}(f)^2 R^{2} + e_R^{2}} \qquad (10.27)
$$

El soroll tèrmic creix amb  $\sqrt{R}$  mentre que el senyal creix amb  $R$: augmentar la transimpedància millora la relació senyal-soroll, i és una de les raons per les quals els TIA tendeixen a valors de  $R$  grans. El soroll de la resistència pot ser rellevant igualment, especialment a freqüències baixes.

Per a l'amplificador electromètric, el model de la figura 10.14 dona

$$
e_{\text{nout}}(f) = \sqrt{\left(e_n(f)^2 + (I_{n+}(f)Z_s(f))^2\right)\left(1+\frac{R_2}{R_1}\right)^{2} + I_{n-}(f)^2 R_2^{2} + e_{R1}^{2}\left(\frac{R_2}{R_1}\right)^{2} + e_{R2}^{2}} \qquad (10.28)
$$

Com que  $R_1$  i  $R_2$  no acostumen a tenir valors extraordinàriament grans, el soroll hi sol estar dominat per les fonts de l'operacional, i la seva elecció és primordial per a un disseny de baix soroll. El terme  $I_{n+}(f)\cdot Z_s(f)$  mostra que els corrents de soroll d'entrada, multiplicats per una impedància de sensor molt elevada, hi contribueixen de manera apreciable.

Integrant qualsevol d'aquestes densitats espectrals sobre la banda útil s'obté la tensió de soroll RMS a la sortida, que és la magnitud que permet calcular la relació senyal-soroll del sistema.

> [!WARNING] **Criteri de tria**
>
> Per a fotodíodes, piezoelèctrics i piroelèctrics el TIA és superior, perquè cancel·la l'efecte de  $C_s$  en contínua i a baixes freqüències. Per a sensors resistius d'alta impedància, com els de pH, l'amplificador electromètric és preferible, perquè estalvia el soroll addicional de la resistència de transimpedància. La decisió es pren comparant el model del sensor, la banda i les fonts dominants d'error i de soroll; per a corrents molt petits, la selecció de l'operacional ha d'incloure alhora corrent de polarització, soroll de corrent, soroll de tensió i producte guany-amplada de banda.

## 4 La xarxa en T

Aconseguir valors molt grans de  $R$  és un dels reptes pràctics del TIA: convertir 1 pA en 10 mV demana una transimpedància de 10 GΩ. Les resistències físiques per sobre de 100 MΩ presenten toleràncies estàndard del 5 % al 10 %, coeficients de temperatura que poden arribar a 500 ppm/°C, fuites per la superfície del component i de la placa que poden ser comparables al seu propi valor en ambients humits, soroll d'excés per sobre del tèrmic teòric —especialment les de pel·lícula de carboni— i un cost elevat amb disponibilitat limitada.

![Amplificador de transimpedància amb xarxa en T: R1 entre el terminal inversor i el node intern Vx, R3 entre Vx i la sortida, i R2 entre Vx i massa.](assets/04_Unitat10_Electrometrics_i_transimpedancia_img_5.png)

*Figura: Figura 10.15 Amplificador de transimpedància amb xarxa en T.*

La xarxa en T substitueix la resistència única per tres:  $R_1$  entre el terminal inversor i un node intern  $V_x$,  $R_3$  entre aquest node i la sortida, i  $R_2$  entre el node i massa. Pel curtcircuit virtual, tot el corrent que entra pel node inversor circula per  $R_1$  cap al node intern, de manera que  $V_x = I_s\cdot R_1$  en valor absolut. Aplicant la llei de corrents de Kirchhoff al node  $V_x$,

$$
\frac{V_{\text{out}}-V_x}{R_3} = \frac{V_x}{R_2} + I_s \qquad (10.29)
$$

i resolent,

$$
V_{\text{out}} = I_s\cdot\left[R_3 + R_1\left(1+\frac{R_3}{R_2}\right)\right] = I_s\cdot R_{\text{eq}} \qquad (10.30)
$$

amb la transimpedància equivalent

$$
R_{\text{eq}} = R_3 + R_1\cdot\left(1+\frac{R_3}{R_2}\right) \qquad (10.31)
$$

Amb  $R_3 \gg R_2$  es poden sintetitzar transimpedàncies enormes amb components de valors moderats: amb  $R_1 = R_3$  = 1 MΩ i  $R_2$  = 100 Ω, la transimpedància equivalent és d'uns 10 GΩ. El valor depèn, doncs, de la relació entre les resistències que formen el divisor intern de la T.

![Model de la xarxa en T per a l'anàlisi d'errors: Zs a l'entrada, font Ib−+In−(f) al node inversor, fonts Vos i en(f) al terminal no inversor, i les tres resistències R1, R2 i R3 amb les seves fonts de soroll eR1, eR2 i eR3.](assets/04_Unitat10_Electrometrics_i_transimpedancia_img_6.png)

*Figura: Figura 10.16 Model per a l'anàlisi dels errors de contínua i del soroll en una xarxa en T.*

La xarxa té un preu. La superposició dona, per als errors de contínua,

$$
V_{\text{out}} = V_{\text{OS}}\left[\left(1+\frac{R_1}{R_s}\right)\left(1+\frac{R_3}{R_2}\right)+\frac{R_3}{R_s}\right] - I_{B-}\cdot R_{\text{eq}} \qquad (10.32)
$$

i, quan la resistència del sensor és molt més gran que  $R_3$,

$$
V_{\text{out}} \approx V_{\text{OS}}\left(1+\frac{R_3}{R_2}\right) - I_{B-}\cdot R_{\text{eq}} \qquad (10.33)
$$

La tensió d'offset queda multiplicada pel factor  $1+R_3/R_2$, que per disseny de la xarxa és molt més gran que 1: amb amplificadors FET i CMOS això pot donar ràpidament tensions capaces de saturar la sortida. I com que la transimpedància equivalent és molt gran, el corrent de polarització continua havent de ser molt baix. L'anàlisi de soroll dona

$$
e_{\text{nout}}(f) \approx \sqrt{e_n(f)^2\left(1+\frac{R_3}{R_2}\right)^{2} + I_{n-}(f)^2 R_{\text{eq}}^{2} + e_{R1}^{2}\left(1+\frac{R_3}{R_2}\right)^{2} + e_{R2}^{2}\left(\frac{R_3}{R_2}\right)^{2} + e_{R3}^{2}} \qquad (10.34)
$$

La diferència respecte del TIA amb una sola resistència és que ara la densitat espectral de soroll de tensió de l'operacional queda multiplicada per un factor molt superior a 1, i que les densitats de  $R_1$  i  $R_2$  hi entren també amb guanys grans. A igualtat de fonts de soroll de l'operacional, la xarxa en T és una solució més sorollosa; el seu lloc és allà on una resistència física del valor requerit resulta impracticable.

## 5 Disseny físic del node d'alta impedància

A les impedàncies que es manegen aquí —fins a TΩ—, les fuites superficials de la placa, l'absorció d'humitat dels dielèctrics i les interferències electromagnètiques són problemes de primer ordre, capaços de degradar un disseny teòricament correcte.

| Tècnica | Descripció |
|:--- |:--- |
| **Guarda** | Pista de placa que envolta el node d'alta impedància, mantinguda al mateix potencial que el pin sensible, habitualment amb un buffer. Actua com a pantalla activa: les fuites superficials i les capacitats paràsites es refereixen al potencial de la guarda i, com que la diferència de tensió respecte del node sensible és pràcticament nul·la, el corrent parasitari que hi circula és molt petit. Com més a prop del node sensible, més efectiva. |
| **Apantallament** | Blindatge conductor al voltant del cablejat d'alta impedància —cable coaxial o triaxial— que intercepta les interferències electromagnètiques i les deriva cap a un potencial de referència. En cable triaxial, la malla interna porta la guarda activa i l'externa fa de pantalla connectada a la referència, de manera que les dues funcions conviuen en el mateix cable. |
| **Aïllants d'alta qualitat** | Plaques de tefló (PTFE), poliimida o materials ceràmics a les zones crítiques. En casos extrems, els components es munten a l'aire sobre terminals de tefló per minimitzar les fuites. |
| **Neteja de la placa** | Els residus de flux, les sals i els greixos formen camins conductors mesurables a l'escala del picoampere i del femtoampere. Es netegen amb alcohol isopropílic i, idealment, amb bany ultrasònic. |
| **Control d'humitat** | La humitat absorbida pels dielèctrics redueix significativament les resistències d'aïllament. En aplicacions crítiques el circuit se segella amb un recobriment hidròfob o es munta en un recinte hermètic amb dessecant. |

> [!TIP] **Síntesi**
>
> El model Thevenin porta a l'amplificador electromètric, que demana  $Z_{\text{in}} \gg Z_s$  i dona  $V_{\text{out}} = V_s(1+R_2/R_1)$; el model Norton porta al de transimpedància, que imposa un curtcircuit virtual al sensor i dona  $V_{\text{out}} = I_s R$, amb la transimpedància mesurada en ohms o en V/A. El TIA cancel·la l'efecte de  $Z_s$  sobre el guany, a canvi d'una banda sovint més estreta que la de l'operacional i d'un guany de soroll  $1+R/Z_s$  que creix amb la freqüència quan  $Z_s$  és capacitiva; la capacitat  $C_f$  hi estabilitza el llaç i en limita la banda. Els errors de contínua estan dominats per  $I_{B-}R$  al TIA i per  $I_{B+}R_s(1+R_2/R_1)$  a l'electromètric. La xarxa en T sintetitza transimpedàncies de gigaohms amb resistències moderades,  $R_{\text{eq}} = R_3 + R_1(1+R_3/R_2)$, i en paga el preu multiplicant l'offset i el soroll de l'operacional pel factor  $1+R_3/R_2$. A impedàncies de teraohms, guardes, apantallaments, aïllants de qualitat, neteja i control d'humitat formen part del disseny tant com l'elecció del component.

[← 3. Amplificadors chopper i amplificadors amb autozero](#amplificadors-chopper-i-amplificadors-amb-autozero)[5. Amplificadors de càrrega →](#amplificadors-de-càrrega)

---

<!-- FIN CAPÍTULO: 04_Unitat10_Electrometrics_i_transimpedancia -->

---

<!-- INICIO CAPÍTULO: 05_Unitat10_Amplificadors_de_carrega -->

# Amplificadors de càrrega

Sistemes de Mesura · **Unitat 10 — Condicionament singular de senyals** · Document 5 de 5

# Amplificadors de càrrega

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Escriure el model elèctric en càrrega d'un sensor piezoelèctric o piroelèctric i identificar-ne les capacitats paràsites associades.
> - Deduir la relació càrrega–tensió d'un amplificador de càrrega i l'abast de la seva independència respecte de les capacitats paràsites.
> - Dimensionar la resistència de realimentació a partir de la freqüència mínima d'interès.
> - Avaluar l'offset de sortida degut a la tensió d'offset i al corrent de polarització, i decidir la tecnologia d'entrada.
> - Reconèixer l'efecte triboelèctric i les mesures que el mitiguen.

Els sensors piezoelèctrics generen un desplaçament de càrregues proporcional a la deformació del material, i els piroelèctrics en generen en resposta a una variació de flux tèrmic. En tots dos casos la magnitud primària que descriu la física del sensor és la **càrrega**  $Q_s$, i no la tensió ni el corrent. Els amplificadors de càrrega parteixen d'aquesta lectura i donen a la sortida una tensió proporcional a la càrrega generada, amb una constant de conversió que depèn d'un condensador de realimentació  $C_f$  i que és essencialment independent de les capacitats paràsites del sensor, del cablejat i de l'entrada de l'operacional. És l'estàndard de facto en instrumentació piezoelèctrica.

## 1 Model del sensor en càrrega

![Model elèctric del sensor generador amb sortida en càrrega: una font de càrrega Qs en paral·lel amb la capacitat Cs i amb la resistència Rs.](assets/05_Unitat10_Amplificadors_de_carrega_img_1.png)

*Figura: Figura 10.17 Model de sensor generador amb sortida en càrrega.*

| Element | Valors típics | Significat |
|:--- |:--- |:--- |
| $Q_s$ | — | Càrrega generada en resposta al mesurand: força mecànica als piezoelèctrics, flux tèrmic als piroelèctrics. |
| $C_s$ | Desenes de pF a alguns nF | Capacitat intrínseca del sensor, associada a la geometria de les cares metal·litzades i a la constant dielèctrica del material. |
| $R_s$ | GΩ o TΩ | Pèrdues finites del dielèctric del material. |
| $C_c$ | 50–100 pF per metre | Capacitat del cable que uneix el sensor i l'amplificador. Amb cables de diversos metres pot assolir centenars de pF i dominar  $C_s$. |
| $C_{\text{in}}$ | Alguns pF | Capacitat d'entrada de l'operacional. |

En una topologia que depengués de  $C_s$  —un seguidor electromètric simple, per exemple— aquestes capacitats paràsites introduirien una dependència freqüencial i, sobretot, una dependència de la longitud del cable, de manera que caldria recalibrar el sistema cada vegada que es modifiqués la instal·lació.

## 2 L'amplificador de càrrega

El punt de partida és la relació entre càrrega i corrent. El corrent és la derivada temporal de la càrrega, cosa que en el domini freqüencial es tradueix en un factor  $j\omega$:

$$
I(j\omega) = j\omega\cdot Q(j\omega) \qquad (10.35)
$$

Si el circuit converteix el corrent  $I$  lliurat pel sensor en una tensió proporcional a  $I/(j\omega)$, el resultat serà una tensió proporcional a  $Q$; i la funció de transferència  $\frac{1}{j\omega}$  és precisament la d'un integrador ideal.

![Amplificador de càrrega: el sensor modelat amb Qs, Cs i Rs es connecta pel cable de capacitat Cc al terminal inversor, amb Cin a massa; la realimentació es tanca amb Cf en paral·lel amb Rf i el terminal no inversor va a massa.](assets/05_Unitat10_Amplificadors_de_carrega_img_2.png)

*Figura: Figura 10.18 Amplificador de càrrega.*

La topologia és estructuralment idèntica a la de transimpedància, amb una sola diferència crítica: en lloc d'una resistència a la realimentació s'hi col·loca un condensador  $C_f$, en paral·lel amb una resistència  $R_f$  d'alt valor que polaritza l'operacional. El sensor es connecta al terminal inversor i el terminal no inversor va a massa. Sota la hipòtesi d'operacional ideal, el node inversor es manté virtualment a massa:  $C_s$,  $C_c$  i  $C_{\text{in}}$, totes connectades entre aquest terminal i massa, tenen els dos extrems al mateix potencial i no hi flueix cap corrent. Tot el corrent que surt de la font de càrrega circula per  $C_f$  —suposant  $R_f$  infinita— i

$$
V_{\text{out}}(j\omega) = -\frac{I(j\omega)}{j\omega\cdot C_f} = -\frac{Q(j\omega)}{C_f} \qquad (10.36)
$$

La tensió de sortida és directament proporcional a la càrrega del sensor, amb un factor de proporcionalitat  $-\frac{1}{C_f}$: augmentar  $C_f$  redueix la tensió obtinguda per unitat de càrrega. Aquesta independència respecte de  $C_s$,  $C_c$  i  $C_{\text{in}}$  es basa en la hipòtesi de guany en llaç obert infinit, que és la que manté el node inversor al potencial de massa. A freqüències on aquest guany ha decrescut significativament, les capacitats paràsites hi tornen a tenir efecte, de manera que la tria de l'operacional ha de garantir un guany en llaç obert elevat en tota la banda d'interès.

## 3 La resistència de realimentació

Un integrador ideal acumula indefinidament sobre  $C_f$  qualsevol corrent de contínua no nul present a l'entrada, i porta la sortida a la saturació en un temps finit. La resistència  $R_f$  en paral·lel amb  $C_f$  proporciona un camí de fuita per a la càrrega acumulada i estabilitza el punt de treball en contínua. Perquè no tingui cap efecte apreciable dins de la banda d'interès —cosa que faria que la transferència deixés de ser un integrador pur—, la seva impedància ha de ser molt més gran que la de  $C_f$  a la freqüència mínima d'interès  $f_{\min}$:

$$
R_f \gg \frac{1}{2\pi\cdot f_{\min}\cdot C_f} \qquad (10.37)
$$

Amb aquesta condició, per a freqüències superiors a  $f_{\min}$  la resistència es comporta com un circuit obert i la transferència recupera la forma  $-Q/C_f$. Per a freqüències molt inferiors a  $\frac{1}{2\pi R_f C_f}$, en canvi,  $R_f$  domina: el circuit esdevé un amplificador de transimpedància d'aproximadament  $R_f$  ohms i respon proporcionalment a la derivada de la càrrega, de manera que la resposta a càrrega constant és nul·la. La freqüència de tall inferior del conjunt queda, doncs, fixada pel producte  $R_f C_f$. És la contrapartida necessària per a la viabilitat pràctica del circuit, i és compatible amb el fet que els sensors piezoelèctrics i piroelèctrics no tenen resposta útil en contínua.

## 4 Errors de contínua

En contínua tots els condensadors del model són circuits oberts, de manera que el punt de treball el fixen els camins resistius. La tensió a la sortida és

$$
V_{\text{out}} = V_{\text{OS}}\cdot\left(1+\frac{R_f}{R_s}\right) + I_{B-}\cdot R_f \qquad (10.38)
$$

| Condició | Resultat |
|:--- |:--- |
| $R_f$  = 1 GΩ amb  $R_s$  = 100 GΩ | Factor 1,01 sobre  $V_{\text{OS}}$ |
| $R_f$  = 1 GΩ amb  $R_s$  = 10 MΩ | Factor 101: una  $V_{\text{OS}}$  d'1 mV dona 101 mV d'offset |
| $R_f$  = 1 GΩ amb  $I_{B-}$  = 10 pA | 10 mV d'offset, tolerable |
| $R_f$  = 1 GΩ amb  $I_{B-}$  = 10 nA | 10 V d'offset, inacceptable |

El primer terme multiplica  $V_{\text{OS}}$  per un factor d'offset que creix quan  $R_s$  baixa. A més,  $R_s$  és la combinació en paral·lel de la resistència intrínseca del sensor amb totes les fuites del sistema —placa, connectors i entrada de l'operacional—, de manera que controlar-la exigeix les mateixes tècniques de disseny físic que qualsevol node d'alta impedància: guardes, neteja, aïllants de qualitat i segellat contra la humitat.

El segon terme és directament proporcional al corrent de polarització i a la resistència de realimentació, i és el que fixa la tecnologia d'entrada. Amb els valors habituals de  $R_f$, els nanoampers dels bipolars són incompatibles amb el marge dinàmic de sortida, de manera que l'operacional d'un amplificador de càrrega ha de tenir etapa d'entrada JFET o CMOS. Els fabricants especialitzats en instrumentació piezoelèctrica ofereixen components amb  $I_b$  de femtoampers i  $V_{\text{OS}}$  moderada —típicament de mil·livolts— dissenyats específicament per a aquesta aplicació.

## 5 L'efecte triboelèctric

> [!WARNING] **Efecte triboelèctric**
>
> Generació de càrregues elèctriques paràsites pel frec mecànic entre el dielèctric i els conductors d'un cable coaxial quan aquest es flexiona. En un sistema que detecta càrregues de l'ordre del picocoulomb, aquestes càrregues poden ser ordres de magnitud més grans que el senyal útil.

Els fabricants especialitzats ofereixen **cables de baix soroll triboelèctric**: cables coaxials amb un recobriment conductor de grafit entre el dielèctric i la malla externa, que curtcircuita les càrregues generades per fricció i les retorna a terra abans que arribin al conductor de senyal. Són identificables per la seva major flexibilitat i pel seu tacte gomós característic. A més, el cable s'ha de fixar mecànicament al llarg del seu recorregut amb brides o suports, de manera que les vibracions ambientals no el facin oscil·lar i generin senyals espuris: el control mecànic del cablejat forma part del disseny de la mesura tant com l'elecció del component.

> [!TIP] **Síntesi**
>
> El sensor piezoelèctric o piroelèctric es modela com una font de càrrega  $Q_s$  amb una capacitat  $C_s$  i una resistència de fuita  $R_s$  en paral·lel, a les quals el muntatge real afegeix la capacitat del cable i la d'entrada de l'operacional, comparables o superiors a  $C_s$. Partint de  $I(j\omega)=j\omega Q(j\omega)$, un integrador amb  $C_f$  a la realimentació dona  $V_{\text{out}}=-Q/C_f$, independent de les capacitats paràsites mentre el guany en llaç obert mantingui el node inversor a massa virtual, i amb sensibilitat inversament proporcional a  $C_f$. La resistència  $R_f$  en paral·lel evita la saturació per acumulació i fixa la freqüència de tall inferior; per conservar el comportament integrador dins de la banda útil, la seva impedància ha de superar àmpliament la de  $C_f$  a  $f_{\min}$. En contínua, els condensadors s'obren i la sortida queda amb  $V_{\text{OS}}(1+R_f/R_s)+I_{B-}R_f$: el primer terme obliga a controlar totes les fuites que redueixen  $R_s$  i el segon imposa entrada JFET o CMOS. L'efecte triboelèctric del cable flexionat es mitiga amb cables de baix soroll i amb la seva fixació mecànica.

[← 4. Amplificadors electromètrics i de transimpedància](#amplificadors-electromètrics-i-de-transimpedància)

---

<!-- FIN CAPÍTULO: 05_Unitat10_Amplificadors_de_carrega -->

---

<!-- INICIO CAPÍTULO: 06_Unitat10_Entrenament -->

# Entrenament V/F · Unitat 10: Condicionament singular de senyals

Sistemes de Mesura (230920) · ETSETB-UPC · **Unitat 10 — Condicionament singular de senyals**

# Entrenament V/F

50 afirmacions repartides entre els cinc documents de la unitat. Tot el càlcul es fa al vostre navegador: les respostes no s'envien enlloc.

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
> 📌 **Afirmació:** *Els sensors singulars requereixen electrònica específica perquè el seu senyal, la seva impedància o la seva càrrega generada imposen restriccions severes al condicionament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de sensor singular: la singularitat és una propietat elèctrica de la seva sortida.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *Quan el senyal útil arriba fins a la contínua, un filtre passaalt és la solució natural per eliminar les derives sense alterar la mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Les derives d'offset ocupen exactament la mateixa banda que el senyal útil, que arriba fins a la contínua.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *Els termoparells i alguns ponts de galgues són exemples de sensors que poden generar tensions diferencials molt petites.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Són els dos exemples del bloc de tensions molt petites: termoparells i ponts de galgues piezorresistives.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *La impedància d'entrada de l'amplificador resulta irrellevant quan la sortida del sensor és capacitiva.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Amb sortida capacitiva, la càrrega de l'entrada altera també la resposta freqüencial del conjunt.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 11
> 📌 **Afirmació:** *El soroll 1/f és especialment crític en mesures lentes perquè concentra més potència a freqüències baixes.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El soroll 1/f té densitat espectral inversament proporcional a la freqüència i domina a freqüències baixes.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 15
> 📌 **Afirmació:** *La compensació de corrents de polarització amb una resistència auxiliar té més sentit en amplificadors bipolars que en amplificadors FET o CMOS.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En bipolars, la relació I_OS/I_B val entre 0,1 i 0,25; en FET i CMOS és de l'ordre de la unitat.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 18
> 📌 **Afirmació:** *La tensió d'offset només modifica el guany de l'amplificador, però no introdueix cap error de zero.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La tensió d'offset apareix a la sortida multiplicada pel guany de soroll, com un error de zero.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 19
> 📌 **Afirmació:** *En aplicacions de baix nivell, el soroll integrat sobre la banda útil s'ha de comparar amb la resolució de mesura requerida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El que compta és la integral de la densitat espectral sobre la banda passant, comparada amb la resolució.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *Un amplificador de baixes derives es defineix principalment pel seu slew rate elevat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'especificació el defineix per offset, deriva, corrents de polarització, soroll i envelliment.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 24
> 📌 **Afirmació:** *Els amplificadors CMOS convencionals ofereixen sempre el menor soroll de tensió a baixa freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La taula de tecnologies dona soroll 1/f alt i soroll de tensió de 20 a 100 nV/√Hz als CMOS convencionals.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 25
> 📌 **Afirmació:** *Els amplificadors chopper i autozero són útils quan la correcció estàtica de l'offset resulta insuficient.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És el punt de partida dels amplificadors chopper i autozero: correcció dinàmica dels propis errors.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *Un termoparell obliga a considerar la contínua perquè la temperatura pot variar molt lentament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Les dinàmiques tèrmiques concentren la potència espectral entre la contínua i fraccions d'hertz.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 31
> 📌 **Afirmació:** *El producte entre corrent de polarització i resistència equivalent del circuit permet estimar una contribució d'error de contínua.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'estimació directa a partir de l'equació (10.1).*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *La resistència auxiliar de compensació és una tècnica recomanable de manera indiscriminada en qualsevol tecnologia d'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La substitució compensa quan I_OS és força menor que I_B, i la resistència aporta soroll tèrmic propi.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 35
> 📌 **Afirmació:** *L'ajust intern d'offset mitjançant pins de trimming pot anul·lar l'offset en una temperatura concreta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'ajust anul·la la tensió d'offset amb una precisió típica de centenars de nanovolts a la temperatura del calibratge.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 41
> 📌 **Afirmació:** *El marge d'ajust de la xarxa de compensació ha de cobrir la dispersió esperada de Vos.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (10.10): el marge ha de cobrir el pitjor offset especificat més un marge del 20 % al 50 %.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 44
> 📌 **Afirmació:** *En un amplificador inversor, l'offset queda multiplicat exactament pel guany de senyal inversor i mai pel guany de soroll.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El guany de senyal de la topologia inversora és −R_2/R_1, i el que afecta l'offset és el guany de soroll.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 46
> 📌 **Afirmació:** *Els guanys alts redueixen l'efecte de l'offset sobre el rang dinàmic de sortida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'offset queda multiplicat pel guany de soroll, que creix amb el guany en llaç tancat.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *En un amplificador chopper, el senyal útil roman sempre en contínua durant totes les etapes internes.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *A la sortida d'A1 el senyal útil és a f_ch, i els errors de l'etapa hi són en banda base.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *La desmodulació síncrona d'un chopper retorna el senyal útil a banda base.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El desmodulador síncron opera amb la mateixa fase que el modulador i retorna el senyal a contínua.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 55
> 📌 **Afirmació:** *La freqüència de commutació limita la banda útil possible d'un amplificador chopper.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La banda útil queda limitada a una fracció de f_ch: amb f_ch = 10 kHz, típicament per sota d'1 kHz.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 58
> 📌 **Afirmació:** *La modulació chopper incrementa deliberadament el soroll 1/f dins la banda útil.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La modulació allunya el senyal útil de la zona on el soroll 1/f és màxim.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 61
> 📌 **Afirmació:** *En un autozero, els condensadors de correcció permeten conservar la informació d'offset entre fases de commutació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Dos condensadors emmagatzemen V_c1 i V_c2 entre les fases d'autozero i d'amplificació.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 64
> 📌 **Afirmació:** *L'offset efectiu d'un autozero creix amb el factor de correcció intern B.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'equació (10.21) divideix la suma dels offsets interns pel factor B.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 68
> 📌 **Afirmació:** *La selecció d'un amplificador de precisió es pot fer mirant només el guany en llaç obert de contínua.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La selecció encadena sis criteris: offset, deriva, corrent de polarització, soroll, alimentació i cost.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 71
> 📌 **Afirmació:** *Els amplificadors autozero acostumen a ser una opció adequada per a termoparells quan es requereix alta estabilitat de zero.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per a termoparells amb resolucions millors que 0,1 °C en marges tèrmics amplis, l'autozero és la primera opció.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 73
> 📌 **Afirmació:** *Els sensors d'alta impedància es poden analitzar amb models de Thevenin o de Norton segons la topologia de condicionament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Tot sensor lineal admet les dues representacions, i la tria és de conveniència topològica.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 80
> 📌 **Afirmació:** *Un amplificador electromètric típic força el terminal sensible a massa virtual com un TIA.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És el TIA qui imposa massa virtual; l'electromètric presenta una impedància d'entrada enorme.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 84
> 📌 **Afirmació:** *El divisor entre impedància del sensor i impedància d'entrada manté sempre una resposta freqüencial plana.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Si Z_s i Z_in tenen dependències freqüencials diferents, la resposta del sistema deixa de ser plana.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 89
> 📌 **Afirmació:** *En el TIA ideal, el node inversor es manté a massa virtual i el sensor veu una impedància d'entrada efectiva molt petita.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El curtcircuit virtual manté el node inversor a massa i el sensor hi veu impedància nul·la.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 92
> 📌 **Afirmació:** *La sortida ideal d'un TIA resistiu depèn directament de la capacitat interna del sensor encara que el node sigui virtualment a massa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El TIA anul·la l'efecte de Z_s sobre el guany de senyal, també quan Z_s és capacitiva.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 97
> 📌 **Afirmació:** *Una capacitat en paral·lel amb la resistència de realimentació pot estabilitzar el TIA i limitar la seva banda.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la funció de C_f: estabilitza el circuit i limita la banda útil.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 100
> 📌 **Afirmació:** *En un TIA, el corrent de polarització queda cancel·lat automàticament pel curtcircuit virtual.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'equació (10.25) conté el terme I_B−·R: amb I_B = 1 pA i R = 1 GΩ, 1 mV a la sortida.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 105
> 📌 **Afirmació:** *El guany de soroll d'un TIA pot créixer amb la freqüència quan la impedància del sensor és capacitiva.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El guany de soroll és 1 + R/Z_s(f), que creix amb la freqüència quan Z_s és capacitiva.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 110
> 📌 **Afirmació:** *Per a sensors resistius d'alta impedància, el TIA és sempre superior perquè elimina qualsevol soroll de resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El TIA hi afegeix el soroll tèrmic de la resistència de realimentació.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 115
> 📌 **Afirmació:** *En una xarxa en T, la resistència equivalent depèn de la relació entre les resistències que formen el divisor intern.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (10.31): R_eq = R_3 + R_1(1 + R_3/R_2).*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 118
> 📌 **Afirmació:** *La xarxa en T elimina l'efecte de Vos independentment del valor de les resistències.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'equació (10.33) multiplica V_os pel factor 1 + R_3/R_2, molt més gran que 1 per disseny.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 125
> 📌 **Afirmació:** *Una guarda activa al voltant del node sensible redueix corrents de fuita perquè manté l'entorn al mateix potencial que el node.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La diferència de tensió respecte del node sensible és pràcticament nul·la i el corrent parasitari, molt petit.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 128
> 📌 **Afirmació:** *La neteja de la PCB és un aspecte cosmètic sense incidència en mesures electromètriques.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Els residus de flux formen camins conductors mesurables a l'escala del picoampere i del femtoampere.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 136
> 📌 **Afirmació:** *El model de càrrega d'un sensor piezoelèctric prescindeix sempre de la capacitat interna del sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *C_s és la capacitat intrínseca associada a la geometria de les cares metal·litzades i al dielèctric.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 139
> 📌 **Afirmació:** *L'amplificador de càrrega ideal dona una sortida proporcional a la càrrega del sensor i inversament proporcional al condensador de realimentació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (10.36): V_out = −Q/C_f.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 144
> 📌 **Afirmació:** *La càrrega és la derivada temporal del corrent generat pel sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El corrent és la derivada temporal de la càrrega, i no a l'inrevés.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 151
> 📌 **Afirmació:** *Perquè el circuit es comporti com un amplificador de càrrega dins la banda útil, Rf ha de presentar una impedància molt gran respecte a Cf a la freqüència mínima d'interès.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (10.37): R_f ≫ 1/(2π·f_min·C_f).*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 158
> 📌 **Afirmació:** *El corrent de polarització té poca importància en un amplificador de càrrega perquè només circula per capacitats ideals.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El terme I_B−·R_f de l'equació (10.38) dona 10 V d'offset amb I_B− = 10 nA i R_f = 1 GΩ.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 165
> 📌 **Afirmació:** *L'efecte triboelèctric pot generar càrregues paràsites en cables sotmesos a flexió o vibració.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de l'efecte triboelèctric: frec entre dielèctric i conductors en flexionar el cable.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 170
> 📌 **Afirmació:** *En un amplificador de càrrega, augmentar Cf incrementa sempre la tensió de sortida per a una mateixa càrrega.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El factor de proporcionalitat de l'equació (10.36) és −1/C_f.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 174
> 📌 **Afirmació:** *En sensors singulars, la topologia dibuixada és sempre més important que les prestacions reals dels components.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El que fa singulars aquests circuits és l'elecció acurada dels components i el disseny físic.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 175
> 📌 **Afirmació:** *La classificació entre baix nivell de tensió i alta impedància ajuda a escollir l'estratègia de condicionament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la classificació en dos blocs: nivell de senyal o impedància de sortida.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 194
> 📌 **Afirmació:** *En aplicacions lentes, el paràmetre dominant és sempre la velocitat de pujada de la sortida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Amb senyals de molt baix nivell i baixa freqüència dominen les limitacions estàtiques i el soroll.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 197
> 📌 **Afirmació:** *Els errors de contínua poden consumir rang dinàmic de sortida i provocar saturació en circuits de guany elevat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb guanys alts l'efecte de V_os pot consumir rang dinàmic o portar l'amplificador a la saturació.*

> **📚 Document de referència:** `Document 02`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | És la definició de sensor singular: la singularitat és una propietat elèctrica de la seva sortida. | Document 01 |
| **04** | **F** | Les derives d'offset ocupen exactament la mateixa banda que el senyal útil, que arriba fins a la contínua. | Document 02 |
| **05** | **V** | Són els dos exemples del bloc de tensions molt petites: termoparells i ponts de galgues piezorresistives. | Document 01 |
| **08** | **F** | Amb sortida capacitiva, la càrrega de l'entrada altera també la resposta freqüencial del conjunt. | Document 01 |
| **11** | **V** | El soroll 1/f té densitat espectral inversament proporcional a la freqüència i domina a freqüències baixes. | Document 01 |
| **15** | **V** | En bipolars, la relació I_OS/I_B val entre 0,1 i 0,25; en FET i CMOS és de l'ordre de la unitat. | Document 02 |
| **18** | **F** | La tensió d'offset apareix a la sortida multiplicada pel guany de soroll, com un error de zero. | Document 01 |
| **19** | **V** | El que compta és la integral de la densitat espectral sobre la banda passant, comparada amb la resolució. | Document 01 |
| **22** | **F** | L'especificació el defineix per offset, deriva, corrents de polarització, soroll i envelliment. | Document 02 |
| **24** | **F** | La taula de tecnologies dona soroll 1/f alt i soroll de tensió de 20 a 100 nV/√Hz als CMOS convencionals. | Document 01 |
| **25** | **V** | És el punt de partida dels amplificadors chopper i autozero: correcció dinàmica dels propis errors. | Document 03 |
| **27** | **V** | Les dinàmiques tèrmiques concentren la potència espectral entre la contínua i fraccions d'hertz. | Document 02 |
| **31** | **V** | És l'estimació directa a partir de l'equació (10.1). | Document 01 |
| **34** | **F** | La substitució compensa quan I_OS és força menor que I_B, i la resistència aporta soroll tèrmic propi. | Document 02 |
| **35** | **V** | L'ajust anul·la la tensió d'offset amb una precisió típica de centenars de nanovolts a la temperatura del calibratge. | Document 02 |
| **41** | **V** | És l'equació (10.10): el marge ha de cobrir el pitjor offset especificat més un marge del 20 % al 50 %. | Document 02 |
| **44** | **F** | El guany de senyal de la topologia inversora és −R_2/R_1, i el que afecta l'offset és el guany de soroll. | Document 02 |
| **46** | **F** | L'offset queda multiplicat pel guany de soroll, que creix amb el guany en llaç tancat. | Document 02 |
| **48** | **F** | A la sortida d'A1 el senyal útil és a f_ch, i els errors de l'etapa hi són en banda base. | Document 03 |
| **49** | **V** | El desmodulador síncron opera amb la mateixa fase que el modulador i retorna el senyal a contínua. | Document 03 |
| **55** | **V** | La banda útil queda limitada a una fracció de f_ch: amb f_ch = 10 kHz, típicament per sota d'1 kHz. | Document 03 |
| **58** | **F** | La modulació allunya el senyal útil de la zona on el soroll 1/f és màxim. | Document 03 |
| **61** | **V** | Dos condensadors emmagatzemen V_c1 i V_c2 entre les fases d'autozero i d'amplificació. | Document 03 |
| **64** | **F** | L'equació (10.21) divideix la suma dels offsets interns pel factor B. | Document 03 |
| **68** | **F** | La selecció encadena sis criteris: offset, deriva, corrent de polarització, soroll, alimentació i cost. | Document 03 |
| **71** | **V** | Per a termoparells amb resolucions millors que 0,1 °C en marges tèrmics amplis, l'autozero és la primera opció. | Document 03 |
| **73** | **V** | Tot sensor lineal admet les dues representacions, i la tria és de conveniència topològica. | Document 04 |
| **80** | **F** | És el TIA qui imposa massa virtual; l'electromètric presenta una impedància d'entrada enorme. | Document 04 |
| **84** | **F** | Si Z_s i Z_in tenen dependències freqüencials diferents, la resposta del sistema deixa de ser plana. | Document 04 |
| **89** | **V** | El curtcircuit virtual manté el node inversor a massa i el sensor hi veu impedància nul·la. | Document 04 |
| **92** | **F** | El TIA anul·la l'efecte de Z_s sobre el guany de senyal, també quan Z_s és capacitiva. | Document 04 |
| **97** | **V** | És la funció de C_f: estabilitza el circuit i limita la banda útil. | Document 04 |
| **100** | **F** | L'equació (10.25) conté el terme I_B−·R: amb I_B = 1 pA i R = 1 GΩ, 1 mV a la sortida. | Document 04 |
| **105** | **V** | El guany de soroll és 1 + R/Z_s(f), que creix amb la freqüència quan Z_s és capacitiva. | Document 04 |
| **110** | **F** | El TIA hi afegeix el soroll tèrmic de la resistència de realimentació. | Document 04 |
| **115** | **V** | És l'equació (10.31): R_eq = R_3 + R_1(1 + R_3/R_2). | Document 04 |
| **118** | **F** | L'equació (10.33) multiplica V_os pel factor 1 + R_3/R_2, molt més gran que 1 per disseny. | Document 04 |
| **125** | **V** | La diferència de tensió respecte del node sensible és pràcticament nul·la i el corrent parasitari, molt petit. | Document 04 |
| **128** | **F** | Els residus de flux formen camins conductors mesurables a l'escala del picoampere i del femtoampere. | Document 04 |
| **136** | **F** | C_s és la capacitat intrínseca associada a la geometria de les cares metal·litzades i al dielèctric. | Document 05 |
| **139** | **V** | És l'equació (10.36): V_out = −Q/C_f. | Document 05 |
| **144** | **F** | El corrent és la derivada temporal de la càrrega, i no a l'inrevés. | Document 05 |
| **151** | **V** | És l'equació (10.37): R_f ≫ 1/(2π·f_min·C_f). | Document 05 |
| **158** | **F** | El terme I_B−·R_f de l'equació (10.38) dona 10 V d'offset amb I_B− = 10 nA i R_f = 1 GΩ. | Document 05 |
| **165** | **V** | És la definició de l'efecte triboelèctric: frec entre dielèctric i conductors en flexionar el cable. | Document 05 |
| **170** | **F** | El factor de proporcionalitat de l'equació (10.36) és −1/C_f. | Document 05 |
| **174** | **F** | El que fa singulars aquests circuits és l'elecció acurada dels components i el disseny físic. | Document 01 |
| **175** | **V** | És la classificació en dos blocs: nivell de senyal o impedància de sortida. | Document 01 |
| **194** | **F** | Amb senyals de molt baix nivell i baixa freqüència dominen les limitacions estàtiques i el soroll. | Document 01 |
| **197** | **V** | Amb guanys alts l'efecte de V_os pot consumir rang dinàmic o portar l'amplificador a la saturació. | Document 02 |

<!-- FIN CAPÍTULO: 06_Unitat10_Entrenament -->

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
| **(10.1)** | $V_{out,err} = -I_B^{+}\cdot R_3\cdot\left(1+\frac{R_2}{R_1}\right) + I_B^{-}\cdot R_2$ |
| **(10.2)** | $V_{out,err} = -I_{\text{OS}}\cdot R_2$ |
| **(10.3)** | $V_{\text{out}} = -V_{\text{in}}\cdot\frac{R_2}{R_1} - V_x\cdot\frac{R_2}{R_3} + V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.4)** | $V_x = V_{\text{OS}}\cdot\frac{R_3}{R_2}\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.5)** | $V_{\text{out}} = -V_{\text{in}}\cdot\frac{R_2}{R_1}$ |
| **(10.6)** | $V_{\text{out}} = -V_{\text{in}}\cdot\frac{R_2}{R_1} + V_x\cdot\frac{R_p}{R_p+R_3}\cdot\left(1+\frac{R_2}{R_1}\right) + V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.7)** | $V_x = -V_{\text{OS}}\cdot\left(1+\frac{R_3}{R_p}\right)$ |
| **(10.8)** | $V_{\text{out}} = V_{\text{in}}\cdot\left(1+\frac{R_2}{R_1}\right) - V_x\cdot\frac{R_2}{R_3} + V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.9)** | $V_x = V_{\text{OS}}\cdot\frac{R_3}{R_2}\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.10)** | $V_r \geq \|V_{OS\,\max}\|\cdot\frac{R_3}{R_2}\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.11)** | $V_{\text{out}} = \frac{A_1/2}{1 + A_1\cdot R_1/[2(R_1+R_2)]}\cdot V_{\text{in}}$ |
| **(10.12)** | $V_{\text{out}} = V_{\text{in}}\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.13)** | $V_{c1} = A_n\cdot V_{\text{osn}} - B_n\cdot V_{c1}$ |
| **(10.14)** | $V_{c1} = V_{\text{osn}}\cdot\frac{A_n}{1+B_n}$ |
| **(10.15)** | $V_{c2} = A_n\cdot(V_{\text{in}}+V_{\text{osn}}) - B_n\cdot V_{c1}$ |
| **(10.16)** | $V_{c2} = A_n\cdot V_{\text{in}} + A_n\cdot V_{\text{osn}}\cdot\frac{1}{1+B_n}$ |
| **(10.17)** | $V_{\text{out}} = A_m\cdot(V_{\text{in}}+V_{\text{osm}}) + B_m\cdot V_{c2}$ |
| **(10.18)** | $V_{\text{out}} = A_m\cdot(V_{\text{in}}+V_{\text{osm}}) + B_m\cdot A_n\cdot V_{\text{in}} + \frac{B_m\cdot A_n\cdot V_{\text{osn}}}{1+B_n}$ |
| **(10.19)** | $V_{\text{out}} = (A_m + B_m\cdot A_n)\cdot V_{\text{in}} + A_m\cdot V_{\text{osm}} + \frac{B_m\cdot A_n\cdot V_{\text{osn}}}{1+B_n}$ |
| **(10.20)** | $V_{\text{out}} \approx A\cdot B\cdot V_{\text{in}} + A\cdot(V_{\text{osm}}+V_{\text{osn}})$ |
| **(10.21)** | $V_{\text{oeff}} = \frac{V_{\text{osm}}+V_{\text{osn}}}{B}$ |
| **(10.22)** | $V_{\text{out}} = V_s\cdot\left(1+\frac{R_2}{R_1}\right)$ |
| **(10.23)** | $V_{s\,eff} = V_s\cdot\frac{Z_{\text{in}}}{Z_s+Z_{\text{in}}}$ |
| **(10.24)** | $V_{\text{out}} = I_s\cdot R$ |
| **(10.25)** | $V_{\text{out}} = V_{\text{OS}}\cdot\left(1+\frac{R}{Z_s}\right) - I_{B-}\cdot R$ |
| **(10.26)** | $V_{\text{out}} = V_{\text{OS}}\cdot\left(1+\frac{R_2}{R_1}\right) + I_{B+}\cdot R_s\cdot\left(1+\frac{R_2}{R_1}\right) - I_{B-}\cdot R_2$ |
| **(10.27)** | $e_{\text{nout}}(f) = \sqrt{e_n(f)^2\left(1+\frac{R}{Z_s(f)}\right)^{2} + I_{n-}(f)^2 R^{2} + e_R^{2}}$ |
| **(10.28)** | $e_{\text{nout}}(f) = \sqrt{\left(e_n(f)^2 + (I_{n+}(f)Z_s(f))^2\right)\left(1+\frac{R_2}{R_1}\right)^{2} + I_{n-}(f)^2 R_2^{2} + e_{R1}^{2}\left(\frac{R_2}{R_1}\right)^{2} + e_{R2}^{2}}$ |
| **(10.29)** | $\frac{V_{\text{out}}-V_x}{R_3} = \frac{V_x}{R_2} + I_s$ |
| **(10.30)** | $V_{\text{out}} = I_s\cdot\left[R_3 + R_1\left(1+\frac{R_3}{R_2}\right)\right] = I_s\cdot R_{\text{eq}}$ |
| **(10.31)** | $R_{\text{eq}} = R_3 + R_1\cdot\left(1+\frac{R_3}{R_2}\right)$ |
| **(10.32)** | $V_{\text{out}} = V_{\text{OS}}\left[\left(1+\frac{R_1}{R_s}\right)\left(1+\frac{R_3}{R_2}\right)+\frac{R_3}{R_s}\right] - I_{B-}\cdot R_{\text{eq}}$ |
| **(10.33)** | $V_{\text{out}} \approx V_{\text{OS}}\left(1+\frac{R_3}{R_2}\right) - I_{B-}\cdot R_{\text{eq}}$ |
| **(10.34)** | $e_{\text{nout}}(f) \approx \sqrt{e_n(f)^2\left(1+\frac{R_3}{R_2}\right)^{2} + I_{n-}(f)^2 R_{\text{eq}}^{2} + e_{R1}^{2}\left(1+\frac{R_3}{R_2}\right)^{2} + e_{R2}^{2}\left(\frac{R_3}{R_2}\right)^{2} + e_{R3}^{2}}$ |
| **(10.35)** | $I(j\omega) = j\omega\cdot Q(j\omega)$ |
| **(10.36)** | $V_{\text{out}}(j\omega) = -\frac{I(j\omega)}{j\omega\cdot C_f} = -\frac{Q(j\omega)}{C_f}$ |
| **(10.37)** | $R_f \gg \frac{1}{2\pi\cdot f_{\min}\cdot C_f}$ |
| **(10.38)** | $V_{\text{out}} = V_{\text{OS}}\cdot\left(1+\frac{R_f}{R_s}\right) + I_{B-}\cdot R_f$ |