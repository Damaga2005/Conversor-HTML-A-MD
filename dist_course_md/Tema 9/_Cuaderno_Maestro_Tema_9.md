# 📚 Cuaderno Maestro: Tema 9

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 9` | 📄 **Capítulos incluidos:** 8  
> 📅 **Generado:** 2026-09-11 19:10

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 9 — Sensors generadors i unions semiconductores · Lectura prèvia](#unitat-9-sensors-generadors-i-unions-semiconductores-lectura-prèvia)
2. [Sensors generadors i efectes termoelèctrics](#sensors-generadors-i-efectes-termoelèctrics)
   - [1 Sensor generador i sensor modulador](#1-sensor-generador-i-sensor-modulador)
   - [2 Conseqüències sobre el condicionament](#2-conseqüències-sobre-el-condicionament)
   - [3 L'efecte Seebeck](#3-lefecte-seebeck)
   - [4 Efectes Peltier i Thomson](#4-efectes-peltier-i-thomson)
3. [El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura](#el-termoparell-resposta-tipus-normalitzats-i-conversió-tensiótemperatura)
   - [1 Principi de funcionament](#1-principi-de-funcionament)
   - [2 Tipus normalitzats](#2-tipus-normalitzats)
   - [3 Conversió tensió–temperatura](#3-conversió-tensiótemperatura)
4. [Lleis termoelèctriques, compensació de la unió freda i prestacions](#lleis-termoelèctriques-compensació-de-la-unió-freda-i-prestacions)
   - [1 Lleis termoelèctriques](#1-lleis-termoelèctriques)
   - [2 Compensació de la unió freda](#2-compensació-de-la-unió-freda)
   - [3 Prestacions i limitacions](#3-prestacions-i-limitacions)
5. [Sensors piezoelèctrics: efecte, materials, model elèctric i resposta](#sensors-piezoelèctrics-efecte-materials-model-elèctric-i-resposta)
   - [1 L'efecte piezoelèctric](#1-lefecte-piezoelèctric)
   - [2 Coeficients piezoelèctrics de càrrega](#2-coeficients-piezoelèctrics-de-càrrega)
   - [3 Fabricació i compensació tèrmica](#3-fabricació-i-compensació-tèrmica)
   - [4 Materials](#4-materials)
   - [5 Model elèctric](#5-model-elèctric)
   - [6 Resposta freqüencial](#6-resposta-freqüencial)
   - [7 Aplicacions](#7-aplicacions)
6. [Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig](#sensors-piroelèctrics-polarització-espontània-dinàmica-i-detecció-dinfraroig)
   - [1 Polarització espontània i efecte piroelèctric](#1-polarització-espontània-i-efecte-piroelèctric)
   - [2 Estructura del sensor](#2-estructura-del-sensor)
   - [3 Coeficients piroelèctrics](#3-coeficients-piroelèctrics)
   - [4 Resposta dinàmica](#4-resposta-dinàmica)
   - [5 Detecció d'infraroig i detectors PIR](#5-detecció-dinfraroig-i-detectors-pir)
7. [Sensors de temperatura basats en unions semiconductores](#sensors-de-temperatura-basats-en-unions-semiconductores)
   - [1 Posició dins de les famílies de sensors de temperatura](#1-posició-dins-de-les-famílies-de-sensors-de-temperatura)
   - [2 La unió polaritzada a corrent constant](#2-la-unió-polaritzada-a-corrent-constant)
   - [3 Limitacions i calibratge](#3-limitacions-i-calibratge)
   - [4 Sensors PTAT amb sortida en corrent](#4-sensors-ptat-amb-sortida-en-corrent)
   - [5 Prestacions](#5-prestacions)
8. [Entrenament V/F · Unitat 9: Unitat 9](#entrenament-vf-unitat-9-unitat-9)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_Unitat_Index -->

# Unitat 9 — Sensors generadors i unions semiconductores · Lectura prèvia

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 9 — Sensors generadors i unions semiconductores

Materials de lectura prèvia · dedicació total estimada: 63 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen.

Llegeix els sis documents en ordre **abans de la primera sessió**.

### [1. Sensors generadors i efectes termoelèctrics](#sensors-generadors-i-efectes-termoelèctrics)

Què distingeix un sensor generador d'un sensor modulador: d'on prové l'energia del senyal de sortida i què implica per al condicionament —nivell de senyal, impedància de font, càrrega i banda de treball. Les tres famílies generadores i el fenomen físic de cadascuna. L'efecte Seebeck: el coeficient de Seebeck absolut com a propietat d'un conductor homogeni, la formulació en circuit obert, la unió calenta i la unió freda, i el coeficient de Seebeck diferencial. Els efectes Peltier i Thomson com a fonts d'error que s'eliminen llegint el sensor en obert.

*⏱️ Dedicació estimada: 9 min*

### [2. El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura](#el-termoparell-resposta-tipus-normalitzats-i-conversió-tensiótemperatura)

La tensió com a integral del coeficient de Seebeck diferencial i la seva aproximació lineal: el termoparell mesura diferència de temperatura. El model circuital i les tres conseqüències que se'n deriven. La normalització IEC 584-3 i ANSI, la intercanviabilitat i el seu preu en puresa dels materials. Els vuit tipus normalitzats amb materials, marge i sensibilitat, i els quatre criteris de tria. Taules i polinomis referits a una unió freda a 0 °C, i la interpolació.

*⏱️ Dedicació estimada: 7 min*

### [3. Lleis termoelèctriques, compensació de la unió freda i prestacions](#lleis-termoelèctriques-compensació-de-la-unió-freda-i-prestacions)

Les dues lleis dels metalls intermedis i la llei de les temperatures intermèdies, i què justifica cadascuna: intercalar cables i instruments, referir tots els materials al platí i tabular sempre amb la unió freda a 0 °C. Els cables d'extensió i de compensació. El muntatge pràctic sobre bloc isoterm. La compensació de la unió freda, la tensió corregida i la propagació de l'error de la mesura de la temperatura de referència. Avantatges i limitacions dels termoparells i el que exigeixen a l'amplificador.

*⏱️ Dedicació estimada: 8 min*

### [4. Sensors piezoelèctrics: efecte, materials, model elèctric i resposta](#sensors-piezoelèctrics-efecte-materials-model-elèctric-i-resposta)

La piezoelectricitat i la simetria cristal·lina: 32 classes, 20 piezoelèctriques, 10 piroelèctriques. Efecte directe i efecte invers. Els coeficients de càrrega, els seus índexs i les seves unitats, i per què importa l'orientació del tall. El poling, la temperatura de Curie i la compensació tèrmica amb estructures multicapa. Les tres famílies de materials i el criteri de tria segons si interessa la sensibilitat en càrrega o en tensió. El model de condensador amb resistència de fuita, la resposta passa-alt i l'efecte de la impedància d'entrada, la ressonància mecànica i les aplicacions.

*⏱️ Dedicació estimada: 14 min*

### [5. Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig](#sensors-piroelèctrics-polarització-espontània-dinàmica-i-detecció-dinfraroig)

La polarització espontània dependent de la temperatura i per què el sensor no dona senyal en règim estacionari. L'estructura de condensador amb capa absorbent, el desacoblament mecànic i la configuració diferencial de dues cel·les. Els coeficients piroelèctrics de càrrega i de tensió, la relació entre tots dos i l'estimació de la càrrega i la tensió generades. Les constants de temps tèrmica i elèctrica i la resposta de dues exponencials a un pols de radiació. La detecció d'infraroig, el chopping, la lent de Fresnel i les limitacions dels detectors PIR.

*⏱️ Dedicació estimada: 13 min*

### [6. Sensors de temperatura basats en unions semiconductores](#sensors-de-temperatura-basats-en-unions-semiconductores)

Per què desplacen les RTD i els termistors en el marge de l'electrònica integrada: cost, integrabilitat i intercanviabilitat. La unió polaritzada a corrent constant —díode o transistor NPN amb col·lector i base curtcircuitats—, l'equació de Shockley i per què la tensió directa baixa uns 2 mV/°C en pujar la temperatura, amb l'aproximació lineal i la seva inversa. Les quatre limitacions: repetibilitat del corrent de saturació, la seva variació amb la temperatura, autoescalfament i necessitat de corrent constant. La dispersió entre dispositius, el calibratge a dos punts i el pressupost d'error. Els sensors PTAT i la diferència de tensions base-emissor independent del corrent de saturació. Sortides digitals i prestacions.

*⏱️ Dedicació estimada: 12 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

<!-- FIN CAPÍTULO: 00_Unitat_Index -->

---

<!-- INICIO CAPÍTULO: 01_Unitat9_Sensors_generadors_i_efectes_termoelectrics -->

# Sensors generadors i efectes termoelèctrics

Sistemes de Mesura · **Unitat 9 — Sensors generadors i unions semiconductores** · Document 1 de 6

# Sensors generadors i efectes termoelèctrics

Dedicació estimada: 9 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir un sensor generador d'un sensor modulador a partir de l'origen de l'energia del senyal de sortida.
> - Associar cada família de sensors generadors al fenomen físic que hi fa la transducció.
> - Deduir del caràcter generador les exigències que recauen sobre el circuit de condicionament.
> - Escriure la tensió d'un termoparell en circuit obert a partir dels coeficients de Seebeck absoluts dels dos materials.
> - Justificar per què el disseny de la lectura d'un termoparell ha de mantenir el corrent per les unions pròxim a zero.

Els sensors resistius de la unitat 5 i els sensors reactius de la unitat 7 modulen una excitació elèctrica aplicada des de l'exterior. Els sensors d'aquesta unitat lliuren directament una tensió o un corrent: l'energia del senyal de sortida prové de la magnitud física mesurada.

## 1 Sensor generador i sensor modulador

|  | Sensor modulador | Sensor generador |
|:--- |:--- |:--- |
| **Excitació elèctrica** | Necessària: el mesurand modifica una excitació externa. | No necessària: la magnitud d'entrada genera el senyal. |
| **Energia del senyal** | Prové de la font d'excitació. | Prové de la magnitud física d'entrada, a través del fenomen de transducció del material. |
| **Magnitud de sortida** | Resistència, capacitat o inductància. | Tensió o càrrega en circuit obert; corrent en curtcircuit. |
| **Geometria** | La sortida hi depèn. | En el termoparell no hi depèn: la tensió la fixen els dos metalls i les temperatures de les unions. |

Les tres famílies de sensors generadors d'aquesta unitat es distingeixen pel fenomen físic que converteix la magnitud d'entrada en senyal elèctric.

| Família | Fenomen | Magnitud mesurada |
|:--- |:--- |:--- |
| **Termoelèctrica** (termoparells) | Efecte Seebeck | Diferència de temperatura entre les dues unions. |
| **Piezoelèctrica** | Efecte piezoelèctric directe | Tensió mecànica: força, pressió, acceleració, impacte. |
| **Piroelèctrica** | Efecte piroelèctric | Flux tèrmic no estacionari, típicament radiació infraroja. |

Els sensors de temperatura basats en unions semiconductores es tracten en aquesta unitat tot i requerir un corrent de polarització constant: aprofiten una propietat intrínseca del material —la dependència de la característica  $i$ – $v$  d'una unió  $p$ - $n$  amb la temperatura— i lliuren una sortida directament interpretable com a temperatura.

El senyal d'un sensor generador és la manifestació directa d'una propietat del material, sense cap amplificació prèvia dins del sensor que hi afegeixi soroll, derives o no linealitats. Aquest tret, sumat a la simplicitat constructiva —dos fils soldats, o una làmina dielèctrica amb dos elèctrodes—, permet fabricar sensors petits, ràpids i aptes per a entorns amb corrosió, vibracions o pressions elevades, i per a marges de temperatura que van de les proximitats de 0 K a més de 1500 °C. Com que no cal portar alimentació fins al punt de mesura, sinó només recollir-ne la tensió amb un parell de cables, el sensor és col·locable allà on alimentar un component seria complicat, costós o perillós.

## 2 Conseqüències sobre el condicionament

El caràcter generador no elimina el circuit de condicionament: en fixa les exigències. Cada família imposa les seves, i un condicionador dissenyat per a una no serveix per a una altra encara que el guany hi sigui el mateix.

| Aspecte | Exigència |
|:--- |:--- |
| **Nivell de senyal** | Desenes de μV/°C en un termoparell, unitats de pC en un sensor piroelèctric: l'offset i la deriva de l'amplificador referits a l'entrada són l'error dominant. |
| **Impedància de font** | Desenes d'ohm en un termoparell; GΩ o TΩ en paral·lel amb pocs pF en els sensors piezoelèctrics i piroelèctrics. |
| **Càrrega del sensor** | Cal llegir carregant tan poc com sigui possible. En els sensors capacitius d'alta impedància, la impedància d'entrada del circuit modifica directament la banda de treball. |
| **Banda de treball** | Els sensors piezoelèctrics i piroelèctrics tenen resposta passa-alt i no mesuren magnituds estàtiques; el termoparell respon en contínua. |

## 3 L'efecte Seebeck

En un metall, els electrons de conducció es comporten en primera aproximació com un gas d'electrons lliures amb una distribució d'energies que depèn de la temperatura. Si hi ha un gradient tèrmic, la difusió porta més electrons de la zona calenta cap a la freda que a l'inrevés; s'acumula càrrega negativa a la zona freda fins que el camp elèctric resultant compensa la difusió. Macroscòpicament apareix una diferència de tensió proporcional a la diferència de temperatura entre els extrems del conductor.

![Conductor homogeni amb un extrem a temperatura alta i l'altre a temperatura baixa; entre els extrems apareix una diferència de tensió proporcional a la diferència de temperatura.](assets/01_Unitat9_Sensors_generadors_i_efectes_termoelectrics_img_1.png)

*Figura: Figura 9.1 Tensió associada a un gradient de temperatura en un conductor homogeni.*

> [!WARNING] **Coeficient de Seebeck absolut**
>
> Constant de proporcionalitat entre la diferència de tensió i la diferència de temperatura entre dos punts d'un **conductor homogeni**, denotada  $\alpha$  o  $S$  i expressada en V/K. És una propietat local d'un únic material. En semiconductors pot ser molt més gran que en metalls, i el dopatge en fixa el signe, fet que els fa útils en termopiles i en cèl·lules Peltier.

Seebeck va observar el 1821 que, unint dos conductors diferents en dos punts mantinguts a temperatures diferents, apareix un corrent capaç de desviar l'agulla d'una brúixola propera. La lectura moderna és que els dos conductors, amb coeficients absoluts diferents, generen forces electromotrius diferents davant del mateix gradient, de manera que la suma al voltant del circuit tancat no és nul·la.

![Dos conductors diferents units en dues unions a temperatures diferents formen un circuit tancat pel qual circula un corrent, detectat pel camp magnètic que crea sobre una brúixola.](assets/01_Unitat9_Sensors_generadors_i_efectes_termoelectrics_img_2.png)

*Figura: Figura 9.2 Formulació original de l'efecte Seebeck.*

La formulació útil per al termoparell és la de circuit obert: els dos conductors s'uneixen en un sol punt, situat a la temperatura  $T_1$, i els dos extrems lliures es mantenen tots dos a la mateixa temperatura  $T_2$. El punt d'unió és la **unió calenta** o de mesura; els dos extrems oposats formen la **unió freda** o de referència, tot i que no estan units elèctricament entre ells. Entre els extrems oberts apareix

$$
V_y = (\alpha_1 - \alpha_2)(T_1 - T_2) \qquad (9.1)
$$

![Esquema de l'efecte Seebeck en circuit obert: dos conductors units en un punt a temperatura T1 i amb els dos extrems lliures a temperatura T2, entre els quals es mesura la tensió.](assets/01_Unitat9_Sensors_generadors_i_efectes_termoelectrics_img_3.png)

*Figura: Figura 9.3 Efecte Seebeck en circuit obert, aplicació directa als termoparells.*

![Termoparell comercial amb beina metàl·lica protectora i punta de mesura on es troben soldats els dos metalls.](assets/01_Unitat9_Sensors_generadors_i_efectes_termoelectrics_img_4.png)

*Figura: Figura 9.4 Exemple de termoparell comercial.*

La tensió mesurable queda determinada per la parella de materials i per les temperatures dels punts de connexió, i és independent del camí tèrmic que segueixen els cables entremig i de la geometria del sensor. Aquesta propietat és conseqüència directa del fet que el coeficient de Seebeck absolut és una propietat local, i és la que fa els termoparells utilitzables en entorns industrials on la distribució tèrmica al llarg del cablejat és incontrolable.

La magnitud rellevant per a un termoparell format pels materials 1 i 2 és el **coeficient de Seebeck diferencial**:

$$
\alpha_{12}(T) = \alpha_1(T) - \alpha_2(T) \qquad (9.2)
$$

![Taula de coeficients de Seebeck absoluts de diversos conductors a 0 °C, presa el coure com a referència, amb valors negatius per al bismut i positius per a l'antimoni.](assets/01_Unitat9_Sensors_generadors_i_efectes_termoelectrics_img_5.png)

*Figura: Figura 9.5 Coeficients de Seebeck absoluts de diversos conductors, prenent el coure com a referència.*

Els coeficients absoluts a l'entorn de 0 °C van de valors molt negatius, com el del bismut, a valors positius, com el de l'antimoni, i passen per zero en alguns metalls. Una sensibilitat elevada demana, doncs, dos materials amb coeficients de signe oposat, de manera que  $\alpha_{12}$  sigui tan gran com sigui possible: d'aquí que els termoparells normalitzats combinin parelles concretes d'aliatges dissenyats per a coeficients elevats i estables.

Tots dos coeficients absoluts depenen de la temperatura, i per tant  $\alpha_{12}(T)$  també: la resposta global del termoparell és no lineal. Per conveniència metrològica els coeficients absoluts es tabulen sovint respecte del **platí**, per la seva puresa i estabilitat química: el que es mesura experimentalment és la tensió del termoparell format pel material d'interès i el platí, i d'aquí se'n dedueix el coeficient absolut un cop descomptada la contribució del platí.

## 4 Efectes Peltier i Thomson

Quan un corrent  $I$  travessa la unió entre dos materials diferents, s'hi absorbeix o s'hi allibera calor amb una potència proporcional a  $\Pi_{12} I$, on  $\Pi_{12} = (\alpha_1 - \alpha_2) T$  és el coeficient de Peltier de la unió. El sentit del flux de calor depèn del sentit del corrent.

![Unió entre dos materials diferents travessada per un corrent: segons el sentit del corrent, la unió absorbeix o allibera calor.](assets/01_Unitat9_Sensors_generadors_i_efectes_termoelectrics_img_6.png)

*Figura: Figura 9.6 Efecte Peltier.*

L'efecte Thomson descriu l'intercanvi de calor associat a la circulació d'un corrent per un conductor *homogeni* sotmès a un gradient de temperatura: el conductor absorbeix o allibera calor al llarg del recorregut en proporció al producte del corrent pel gradient, amb el coeficient de Thomson del material com a constant. Els tres coeficients estan lligats per les relacions de Kelvin.

| Efecte | Origen | Paper en la mesura |
|:--- |:--- |:--- |
| **Seebeck** | Gradient de temperatura en un conductor. | Principi de mesura del termoparell. |
| **Peltier** | Corrent a través d'una unió entre dos materials. | Font d'error: escalfa o refreda la unió de mesura, que deixa d'estar a la temperatura que es vol mesurar. Creix amb la sensibilitat del termoparell, perquè  $\Pi_{12}$  és proporcional a  $\alpha_{12}$. |
| **Thomson** | Corrent en un conductor homogeni amb gradient tèrmic. | Font d'error del mateix ordre de tractament que el Peltier. |

Tots dos errors s'eliminen mantenint el corrent per les unions pròxim a zero, cosa que exigeix amplificadors amb corrents de polarització molt baixos i impedàncies d'entrada molt elevades. La restricció encaixa amb la naturalesa generadora del dispositiu: la informació s'extreu llegint la tensió en circuit obert.

> [!TIP] **Síntesi**
>
> Un sensor generador lliura tensió o càrrega sense excitació elèctrica externa, i l'energia del senyal prové de la magnitud mesurada: termoparells per efecte Seebeck, sensors piezoelèctrics per tensió mecànica i sensors piroelèctrics per flux tèrmic. El coeficient de Seebeck absolut  $\alpha$  és una propietat local d'un conductor homogeni; en un termoparell la magnitud rellevant és el diferencial  $\alpha_{12} = \alpha_1 - \alpha_2$, i la tensió en circuit obert queda determinada per la parella de materials i per les temperatures de les dues unions, amb independència de la geometria i del camí tèrmic dels cables. Com que  $\alpha_{12}$  depèn de la temperatura, la resposta és no lineal. Els efectes Peltier i Thomson apareixen quan circula corrent i són fonts d'error que es mantenen negligibles llegint el sensor en obert.

[2. El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura →](#el-termoparell-resposta-tipus-normalitzats-i-conversió-tensiótemperatura)

---

<!-- FIN CAPÍTULO: 01_Unitat9_Sensors_generadors_i_efectes_termoelectrics -->

---

<!-- INICIO CAPÍTULO: 02_Unitat_El_termoparell_tipus_i_conversio -->

# El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura

Sistemes de Mesura · **Unitat 9 — Sensors generadors i unions semiconductores** · Document 2 de 6

# El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura

Dedicació estimada: 7 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Escriure la tensió d'un termoparell com a integral del coeficient de Seebeck diferencial i identificar-ne l'aproximació lineal.
> - Justificar per què un termoparell mesura diferència de temperatura i no temperatura absoluta.
> - Emprar el model circuital del termoparell per anticipar el seu comportament davant del circuit de lectura.
> - Triar un tipus normalitzat a partir del marge de temperatura, l'entorn químic, la sensibilitat i el cost.
> - Convertir una tensió mesurada en temperatura amb les taules i els polinomis de la norma.

## 1 Principi de funcionament

Un termoparell són dos conductors de natura diferent units elèctricament en un punt. El punt d'unió física és la **unió calenta** o de mesura, i es col·loca allà on es vol conèixer la temperatura. Els dos extrems lliures constitueixen la **unió freda** o de referència, on no hi ha cap unió física entre els dos metalls; el requisit és que tots dos extrems estiguin a la *mateixa* temperatura. El sensor té, doncs, tres punts tèrmicament rellevants: dos a la temperatura de referència i un a la temperatura a mesurar.

La tensió entre els extrems lliures val

$$
V = \int_{T_r}^{T_o} \alpha_{12}(T)\,dT \qquad (9.3)
$$

és a dir, la integral del coeficient de Seebeck diferencial entre la temperatura de la unió freda  $T_r$  i la de la unió calenta  $T_o$. Si  $\alpha_{12}$  fos constant, l'expressió es reduiria a

$$
V \approx \alpha_{12}\,(T_o - T_r) \qquad (9.4)
$$

La tensió mesurable és proporcional a la **diferència** de temperatura entre les dues unions. Coneixent  $T_r$  es pot deduir  $T_o$; si  $T_r$  no es coneix, cal un mètode addicional per determinar-la.

Com que  $\alpha_{12}(T)$  depèn de la temperatura, la relació entre  $V$  i  $\Delta T$  presenta una curvatura que depèn del tipus de termoparell: el tipus J és bastant lineal dins del seu marge, mentre que el tipus T té una curvatura més pronunciada. L'exactitud requerida s'obté amb les taules o les aproximacions polinòmiques de la norma.

> [!WARNING] **Model circuital**
>
> Font de tensió ideal que lliura  $V$  en funció de  $T_o$  i  $T_r$, en sèrie amb la resistència òhmica dels fils metàl·lics, normalment inferior a algunes desenes d'ohm. Se'n deriven tres conseqüències: la impedància de sortida és negligible davant de la d'entrada de qualsevol amplificador raonable, de manera que la càrrega és poc crítica; la lectura s'ha de fer en obert perquè els efectes Peltier i Thomson es mantinguin negligibles; i qualsevol tensió termoelèctrica paràsita introduïda en sèrie per altres unions se suma directament a la del sensor.

## 2 Tipus normalitzats

La normalització dels termoparells —ANSI i IEC, amb la norma IEC 584-3— fixa la composició exacta dels materials, defineix els codis de colors que identifiquen cada tipus i la branca positiva i la negativa de cada parella, especifica el marge de temperatura d'utilització i proporciona taules i polinomis tensió–temperatura respecte d'una temperatura de referència, típicament 0 °C.

La conseqüència pràctica és la **intercanviabilitat**: un termoparell d'un tipus donat comprat a qualsevol fabricant que compleixi la norma es comporta pràcticament igual que qualsevol altre del mateix tipus, cosa que evita el calibratge individual en moltes aplicacions i permet substituir sensors al camp sense reajustar el condicionament. Aquest grau d'intercanviabilitat exigeix pureses i composicions d'aliatge molt controlades —la puresa del ferro en un tipus J, les toleràncies dels percentatges en un tipus K—, i és també l'origen del seu cost.

La norma IEC 584-3 reconeix vuit termoparells normalitzats: B, E, J, K, N, R, S i T. Per a aplicacions molt específiques s'empren altres tipus, com el C o el G.

![Taula dels termoparells normalitzats K, J, T, E, N, S, R i B amb el codi de colors ANSI i IEC del cable de termoparell i del cable d'extensió, la combinació d'aliatges de cada branca, el marge de temperatura i la tensió mínima i màxima de sortida.](assets/02_Unitat_El_termoparell_tipus_i_conversio_img_1.png)

*Figura: Figura 9.7 Termoparells normalitzats: codi de colors, aliatges, marge de temperatura i marge de tensió de sortida.*

![Corbes de tensió de sortida en funció de la temperatura de la unió calenta per als termoparells normalitzats, amb la unió freda a 0 °C.](assets/02_Unitat_El_termoparell_tipus_i_conversio_img_2.png)

*Figura: Figura 9.8 Funció de resposta dels termoparells normalitzats, amb la unió freda a 0 °C.*

| Tipus | Materials | Marge típic | Sensibilitat i tret distintiu |
|:--- |:--- |:--- |:--- |
| **J** | Ferro–constantan | −210 °C a +1200 °C | De l'ordre de 50 μV/°C i bona linealitat. Molt utilitzat a temperatures mitjanes. |
| **K** | Cromel–alumel | −270 °C a +1372 °C | De l'ordre de 40 μV/°C. El més utilitzat, per l'ampli rang, la resistència a l'oxidació i el cost moderat. |
| **T** | Coure–constantan | −270 °C a +400 °C | Més no linealitat que el J; molt bona resistència a entorns humits i útil a temperatures baixes. |
| **E** | Cromel–constantan | Temperatures mitjanes | Més de 70 μV/°C: la sensibilitat més alta dels tipus habituals. |
| **N** | Nicrosil–nisil | Fins a l'entorn de 1300 °C | Alternativa al K amb millor estabilitat a alta temperatura. |
| **R, S, B** | Platí i platí–rodi de diferents composicions | Fins a més de 1800 °C | Unes 10 μV/°C i cost elevat. Metal·lúrgia i forns de vidre. |

La tria del tipus la dominen quatre factors: el marge de temperatura requerit, la composició química de l'entorn —oxigen, atmosferes reductores, sofre—, la sensibilitat desitjada i el cost admissible. Com a regla general, temperatures mitjanes en ambients moderadament agressius demanen un J o un K; temperatures baixes, un T; temperatures molt elevades, un R, un S o un B; i precisió a alta temperatura amb estabilitat millorada, un N. Cal comprovar també la disponibilitat de cables d'extensió i de compensació del tipus escollit.

Els fabricants ofereixen els mateixos materials sensors encapsulats en beines d'acer inoxidable, Inconel o ceràmica, de manera que un mateix tipus serveix per a entorns molt diferents segons la protecció. La beina, però, augmenta la constant de temps del conjunt i alenteix la resposta temporal del sensor.

## 3 Conversió tensió–temperatura

Per a cada tipus, la norma proporciona dos instruments: les **taules** tensió–temperatura amb resolució típica d'1 °C i les **aproximacions polinòmiques** de la temperatura en funció de la tensió, i inverses. Tots dos assumeixen la unió freda a 0 °C.

$$
T = c_0 + c_1 x + c_2 x^2 + \cdots + c_n x^n \qquad (9.5)
$$

on  $x$  és la tensió mesurada amb la unió freda a 0 °C i  $T$  la temperatura de la unió calenta. L'ordre del polinomi i l'error màxim dins del marge de mesura depenen del tipus. Aquests polinomis es programen dins del firmware del sistema de mesura i són la manera més pràctica d'obtenir la temperatura un cop compensada la unió freda.

![Taula de referència d'un termoparell de tipus J amb la unió freda a 0 °C: per a cada temperatura de 0 a 150 °C, la tensió en microvolts, el coeficient de Seebeck i la seva derivada.](assets/02_Unitat_El_termoparell_tipus_i_conversio_img_3.png)

*Figura: Figura 9.9 Taula de referència d'un termoparell normalitzat de tipus J, amb la unió freda a 0 °C.*

| Dada | Resultat |
|:--- |:--- |
| Unió calenta a 137 °C | 7,294 mV |
| Tensió mesurada de 2,744 mV | 53 °C |
| Tensió mesurada de 2,500 mV, entre els 2,480 mV dels 48 °C i els 2,533 mV dels 49 °C | 48,38 °C per interpolació lineal |

La resolució de la taula és limitada: en molts casos la tensió mesurada cau entre dos valors tabulats i cal interpolar. La interpolació lineal, equivalent a suposar la relació tensió–temperatura lineal dins d'un interval d'1 °C, deixa l'error per resolució de taula molt per sota de 0,5 °C per a la majoria de tipus normalitzats. En una implementació digital és habitual partir directament del polinomi de la norma.

> [!TIP] **Síntesi**
>
> La tensió d'un termoparell és la integral del coeficient de Seebeck diferencial entre la temperatura de la unió freda i la de la unió calenta, i es redueix a  $V \approx \alpha_{12}\Delta T$  quan  $\alpha_{12}$  es pot considerar constant: el sensor lliura informació de la diferència de temperatura entre les dues unions. El model circuital és una font de tensió amb una resistència de sortida de desenes d'ohm, de manera que la càrrega és poc crítica però qualsevol tensió termoelèctrica paràsita en sèrie se suma a la del sensor. La norma IEC 584-3 reconeix vuit tipus —B, E, J, K, N, R, S, T—, en garanteix la intercanviabilitat i en proporciona taules i polinomis referits a una unió freda a 0 °C; la tria del tipus combina marge de temperatura, entorn químic, sensibilitat i cost.

[← 1. Sensors generadors i efectes termoelèctrics](#sensors-generadors-i-efectes-termoelèctrics)[3. Lleis termoelèctriques, compensació de la unió freda i prestacions →](#lleis-termoelèctriques-compensació-de-la-unió-freda-i-prestacions)

---

<!-- FIN CAPÍTULO: 02_Unitat_El_termoparell_tipus_i_conversio -->

---

<!-- INICIO CAPÍTULO: 03_Unitat9_Lleis_unio_freda_i_prestacions -->

# Lleis termoelèctriques, compensació de la unió freda i prestacions

Sistemes de Mesura · **Unitat 9 — Sensors generadors i unions semiconductores** · Document 3 de 6

# Lleis termoelèctriques, compensació de la unió freda i prestacions

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Aplicar les lleis dels metalls intermedis i de les temperatures intermèdies per justificar un muntatge real.
> - Distingir un cable d'extensió d'un cable de compensació.
> - Calcular la tensió corregida per compensació de la unió freda i identificar de què depèn l'exactitud del resultat.
> - Enumerar els avantatges i les limitacions dels termoparells i les exigències que imposen a l'amplificador.

Portar la tensió del sensor fins a l'aparell de mesura obliga a fer connexions amb altres metalls —coure dels cables, estany de les soldadures, terminals dels connectors—, cadascuna de les quals és una unió susceptible de generar la seva pròpia tensió termoelèctrica. Les lleis termoelèctriques, corol·laris de l'efecte Seebeck, permeten justificar rigorosament els muntatges pràctics i els productes comercials associats.

## 1 Lleis termoelèctriques

> [!WARNING] **Primera llei dels metalls intermedis**
>
> En un circuit amb un termoparell de metalls A i B amb unions a  $T_1$  i  $T_2$, intercalar un tercer conductor C en un punt intermedi d'un dels conductors no canvia la tensió mesurada sempre que les dues unions noves estiguin a la **mateixa** temperatura.

![Circuit de termoparell amb metalls A i B i unions a T1 i T2 en què s'intercala un tercer conductor C amb les seves dues unions a la mateixa temperatura T3; la tensió mesurada és la mateixa que sense el conductor intercalat.](assets/03_Unitat9_Lleis_unio_freda_i_prestacions_img_1.png)

*Figura: Figura 9.10 Primera llei dels metalls intermedis.*

Els dos punts de soldadura nous generen tensions termoelèctriques iguals i oposades, que es cancel·len. Aquesta llei justifica que es puguin intercalar instruments de mesura, cables de coure o cables d'extensió, i a la pràctica es compleix col·locant físicament pròxims els dos terminals a la zona de connexió.

| Tipus | Composició i motiu |
|:--- |:--- |
| **Cable d'extensió** | Mateix material que el termoparell amb puresa relaxada. El salt tèrmic entre els seus extrems és petit, de manera que la puresa reduïda hi introdueix errors menors. |
| **Cable de compensació** | Materials més barats, escollits perquè els seus coeficients de Seebeck s'aproximin als del termoparell dins del marge de 0 °C a 100 °C. Redueix cost en termoparells de materials nobles. |

> [!WARNING] **Segona llei dels metalls intermedis**
>
> Si un termoparell B-A amb unions a  $T_1$  i  $T_2$  produeix  $V_1$, i un termoparell A-C amb les mateixes unions produeix  $V_2$, aleshores un termoparell B-C amb les unions a les mateixes temperatures produeix  $V_3 = V_1 + V_2$.

![Dos circuits de termoparell amb un material comú i les mateixes temperatures d'unió, les tensions dels quals se sumen per donar la del termoparell format pels altres dos materials.](assets/03_Unitat9_Lleis_unio_freda_i_prestacions_img_2.png)

*Figura: Figura 9.11 Segona llei dels metalls intermedis.*

D'aquí que n'hi hagi prou amb mesurar cada material respecte d'un metall de referència —el platí— per reconstruir després la tensió termoelèctrica de qualsevol parella, sense haver de tabular experimentalment totes les combinacions.

> [!WARNING] **Llei de les temperatures intermèdies**
>
> Si un termoparell A-B amb unions a  $T_1$  i  $T_2$  produeix  $V_1$, i el mateix termoparell amb unions a  $T_2$  i  $T_3$  produeix  $V_2$, aleshores amb unions a  $T_1$  i  $T_3$  produeix  $V_3 = V_1 + V_2$.

![Dos circuits del mateix termoparell A-B, un amb unions a T1 i T2 i l'altre a T2 i T3, les tensions dels quals se sumen per donar la del termoparell amb unions a T1 i T3.](assets/03_Unitat9_Lleis_unio_freda_i_prestacions_img_3.png)

*Figura: Figura 9.12 Llei de les temperatures intermèdies.*

Aquesta llei permet tabular les tensions suposant sempre la unió freda a 0 °C i reconstruir després la tensió equivalent per a qualsevol temperatura real de la unió freda. Amb una sola taula per tipus n'hi ha prou, sigui quina sigui la temperatura ambient de la instal·lació.

![Equivalència entre l'esquema teòric del termoparell amb unió freda a Tr i el muntatge pràctic, on la unió freda es desdobla en dues unions amb cables de coure situades sobre un bloc isoterm connectat a l'instrument de mesura.](assets/03_Unitat9_Lleis_unio_freda_i_prestacions_img_4.png)

*Figura: Figura 9.13 Muntatge pràctic d'un termoparell.*

En el muntatge pràctic la unió freda es desdobla en dos punts d'unió entre els metalls del sensor i el metall de connexió, habitualment coure, sobre un bloc isoterm connectat a l'instrument. Per la primera llei dels metalls intermedis, aquestes dues unions no afecten la mesura si es mantenen a la mateixa temperatura  $T_r$; coneixent  $T_r$  i aplicant la llei de les temperatures intermèdies s'estima  $T_o$  amb el polinomi o la taula de la norma.

## 2 Compensació de la unió freda

Les taules i els polinomis suposen la unió freda a 0 °C, mentre que a la instal·lació real es troba a la temperatura de l'armari de connexions, normalment entre 15 °C i 40 °C. Llegir directament la tensió del sensor a la taula normalitzada donaria una temperatura sistemàticament més baixa: amb la unió freda a 25 °C i la calenta a 525 °C, la taula retornaria aproximadament 500 °C. La correcció es coneix com a **compensació de la unió freda** (*cold junction compensation*, CJC).

La tensió mesurada amb la unió calenta a  $T_o$  i la freda a  $T_r$  és

$$
V = V(T_o, 0) - V(T_r, 0) \qquad (9.6)
$$

on  $V(T,0)$  és la tensió del mateix termoparell amb la unió calenta a  $T$  i la freda a 0 °C. La tensió que es pot introduir directament a la taula o al polinomi és, doncs,

$$
V_\mathrm{corr} = V + V(T_r, 0) \qquad (9.7)
$$

Cal sumar a la tensió llegida la tensió tabulada corresponent a la temperatura actual de la unió freda respecte de 0 °C.

| Magnitud | Valor |
|:--- |:--- |
| Tensió mesurada  $V$ | 3,334 mV |
| Temperatura de la unió freda  $T_r$ | 22 °C |
| Tensió tabulada  $V(22\,^\circ\mathrm{C}, 0)$ | 1,122 mV |
| Tensió corregida  $V_\mathrm{corr}$ | 4,456 mV |
| Temperatura de la unió calenta  $T_o$ | 85 °C |
| Lectura sense corregir | entre 64 °C i 65 °C |

Determinar  $T_r$  demana un sensor de temperatura absolut —una RTD, un termistor o, el més habitual, un sensor integrat basat en unió semiconductora— en contacte tèrmic amb la caixa de connexions. Com que les temperatures ambientals són moderades, l'exactitud requerida és fàcilment assolible. L'exactitud final es propaga: un error de 0,5 °C en  $T_r$  dona un error del mateix ordre en  $T_o$, sigui quin sigui el termoparell. En sistemes de molt alta exactitud es distribueixen dues o tres sondes al voltant de la caixa de connexions per estimar-ne millor la temperatura mitjana.

![Esquema de compensació digital de la unió freda: la tensió del termoparell s'amplifica i es digitalitza amb un ADC, un sensor de temperatura mesura la unió freda i el bloc digital calcula la tensió corregida i hi aplica el polinomi invers.](assets/03_Unitat9_Lleis_unio_freda_i_prestacions_img_5.png)

*Figura: Figura 9.14 Circuit per a la compensació de la unió freda.*

En la pràctica moderna la compensació és digital: la tensió del termoparell s'amplifica i es digitalitza; la temperatura de la unió freda es llegeix d'un sensor amb sortida digital nativa —I²C o SPI— o a través d'un ADC addicional; el sistema digital calcula  $V(T_r,0)$  amb una expressió polinòmica en firmware, la suma a la tensió mesurada i aplica el polinomi invers per obtenir  $T_o$. Molts circuits integrats incorporen dins del mateix encapsulat l'amplificador d'instrumentació, l'ADC, el sensor de temperatura de la unió freda i la lògica de linealització, i lliuren la temperatura per una interfície sèrie.

## 3 Prestacions i limitacions

| Avantatges | Limitacions |
|:--- |:--- |
| Simplicitat i robustesa: dos fils metàl·lics units, senzills de construir i de reparar. | Sensibilitat reduïda: desenes de μV/°C. Resoldre 0,1 °C exigeix mesurar pocs μV. |
| Marge de mesura extens, de temperatures criogèniques pròximes a 0 K a més de 1500 °C segons el tipus, amb un sol principi de mesura. | No linealitat, que obliga a taules o a polinomis d'ordre elevat. |
| Estabilitat i fiabilitat, i exactitud suficient per a la majoria d'aplicacions industrials sense calibratge individual. | Necessitat de conèixer la temperatura de la unió freda, que afegeix un segon sensor i l'algorisme de compensació. |
| Resposta ràpida en sensors de dimensions petites: la constant de temps sol ser molt menor que la dels filtres que l'acompanyen. | Restriccions sobre l'amplificador per mantenir el corrent pel sensor pròxim a zero i evitar els efectes Peltier i Thomson. |
| Sense autoescalfament apreciable, perquè idealment no hi circula corrent. | Compatibilitat química limitada: alguns tipus es degraden ràpidament en atmosferes corrosives. |
| Materials disponibles per a entorns oxidants, reductors i químicament actius; la sortida no depèn de la geometria ni de la quantitat de material. | Cost elevat dels materials de puresa controlada, especialment en els tipus de metalls nobles. |

La sensibilitat reduïda es tradueix en una exigència concreta sobre l'amplificador: qualsevol deriva d'offset referida a l'entrada esdevé un error de temperatura. Una deriva de 10 μV a l'entrada equival, en un termoparell J, a uns 0,2 °C d'error sistemàtic. Per això s'hi empren amplificadors amb *chopper* o amb autozero, que cancel·len periòdicament l'offset i arriben a derives d'entrada de l'ordre de 0,05 μV/°C. Aquests amplificadors es tracten a la unitat 10.

> [!TIP] **Síntesi**
>
> La primera llei dels metalls intermedis permet intercalar cables i instruments sense alterar la mesura mentre les dues unions noves estiguin a la mateixa temperatura, i justifica els cables d'extensió i de compensació. La segona llei permet referir tots els materials al platí, i la llei de les temperatures intermèdies permet tabular sempre amb la unió freda a 0 °C. La compensació de la unió freda consisteix a sumar a la tensió llegida la tensió tabulada de la temperatura real de la unió freda,  $V_\mathrm{corr} = V + V(T_r,0)$, i l'exactitud del resultat hereta l'error de la mesura de  $T_r$. Els termoparells ofereixen robustesa, marge de mesura extens i absència d'autoescalfament, a canvi de baixa sensibilitat, no linealitat i la necessitat d'un segon sensor de temperatura.

[← 2. El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura](#el-termoparell-resposta-tipus-normalitzats-i-conversió-tensiótemperatura)[4. Sensors piezoelèctrics: efecte, materials, model elèctric i resposta →](#sensors-piezoelèctrics-efecte-materials-model-elèctric-i-resposta)

---

<!-- FIN CAPÍTULO: 03_Unitat9_Lleis_unio_freda_i_prestacions -->

---

<!-- INICIO CAPÍTULO: 04_Unitat9_Sensors_piezoelectrics -->

# Sensors piezoelèctrics: efecte, materials, model elèctric i resposta

Sistemes de Mesura · **Unitat 9 — Sensors generadors i unions semiconductores** · Document 4 de 6

# Sensors piezoelèctrics: efecte, materials, model elèctric i resposta

Dedicació estimada: 14 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Relacionar l'efecte piezoelèctric amb la simetria de l'estructura cristal·lina del material.
> - Interpretar els índexs dels coeficients piezoelèctrics de càrrega i les seves unitats.
> - Escriure la càrrega i la tensió generades per una força i identificar de quins paràmetres geomètrics depenen.
> - Triar el material piezoelèctric a partir de la sensibilitat en càrrega o en tensió que demana l'aplicació.
> - Determinar la banda útil del sensor a partir de la freqüència de tall inferior i de la ressonància mecànica.

## 1 L'efecte piezoelèctric

Descobert pels germans Pierre i Jacques Curie el 1880, l'efecte piezoelèctric consisteix que, en certs materials dielèctrics, una tensió mecànica que els deforma provoca l'aparició d'un camp elèctric en circuit obert o, equivalentment, d'una densitat de corrent en curtcircuit. La deformació modifica la distribució de càrregues del cristall i apareix una càrrega neta superficial proporcional a la deformació.

![Cel·la del quars amb els ions de silici i d'oxigen: en repòs els centres de càrrega coincideixen, i en aplicar una força es desplacen i apareix un moment dipolar net amb càrrega als elèctrodes.](assets/04_Unitat9_Sensors_piezoelectrics_img_1.png)

*Figura: Figura 9.15 Efecte piezoelèctric en el quars.*

El fenomen està lligat a la simetria de l'estructura cristal·lina. En un cristall centrosimètric els centres de càrrega positiva i negativa coincideixen a cada cel·la unitat, el moment dipolar net és nul i qualsevol deformació preserva la neutralitat elèctrica macroscòpica. En un cristall sense centre de simetria, en canvi, els centres de càrrega es poden desplaçar l'un respecte de l'altre sota l'acció d'una tensió mecànica i apareix un moment dipolar net a la cel·la.

| Classes | Propietat |
|:--- |:--- |
| **32** | Classes cristal·lines possibles. |
| **20** | Poden presentar efecte piezoelèctric: no tenen centre de simetria. |
| **10** | Presenten a més polarització espontània dependent de la temperatura: són piroelèctriques. |

El quars, SiO₂, té una estructura trigonal sense centre de simetria; en aplicar-hi una força al llarg d'un eix, els ions Si⁴⁺ i O²⁻ es desplacen i apareix un moment dipolar net, amb la polarització en un eix ortogonal al de la força aplicada. L'orientació del tall cristal·lí determina, doncs, la sensibilitat i l'estabilitat del sensor. Els materials policristal·lins sense tractament no mostren piezoelectricitat macroscòpica perquè les contribucions dels dominis es cancel·len en mitjana; per això els comercials són monocristalls, com el quars, o ceràmics tractats per orientar-ne els dominis, com el PZT.

A escala macroscòpica el comportament es recull en el vector de polarització  $\vec{P}$, moment dipolar per unitat de volum. En repòs pot ser nul, en materials paraelèctrics en equilibri, o tenir un valor residual anomenat **polarització espontània**, en els materials ferroelèctrics.

| Mode | Descripció i ús |
|:--- |:--- |
| **Efecte directe** (sensor) | Una força o tensió mecànica genera càrrega i una tensió mesurable als terminals. És el mode d'operació com a sensor de força, pressió, acceleració o impacte. |
| **Efecte invers** (actuador) | Una tensió elèctrica entre els elèctrodes provoca una deformació mecànica, governada pels mateixos coeficients. Posicionadors de precisió, emissors d'ultrasons i altaveus piezoelèctrics. |

Un mateix element s'utilitza sovint alternativament en mode emissor i en mode receptor, com en el transductor d'un sonar o d'una sonda d'ultrasons, que emet un pols excitant el material com a actuador i poc després en rep el ressò com a sensor.

## 2 Coeficients piezoelèctrics de càrrega

La tensió mecànica aplicada al material és un tensor amb sis components independents: tres normals  $(\sigma_x, \sigma_y, \sigma_z)$  i tres de cisalla o torsió  $(\tau_{\text{yz}}, \tau_{\text{xz}}, \tau_{\text{xy}})$, numerades amb índexs d'1 a 6. Cada component de la polarització hi respon amb una combinació lineal:

$$
P_i = \sum_j d_{\text{ij}}\,\sigma_j \qquad (9.8)
$$

![Làmina de material piezoelèctric amb elèctrodes a dues cares oposades i els tres eixos ortogonals x, y, z definits sobre el sensor.](assets/04_Unitat9_Sensors_piezoelectrics_img_2.png)

*Figura: Figura 9.16 Sensor piezoelèctric i definició dels eixos.*

> [!WARNING] **Coeficient piezoelèctric de càrrega $d_{\text{ij}}$**
>
> Relació entre la densitat de càrrega superficial que apareix a la cara perpendicular a l'eix  $i$  i la tensió mecànica aplicada al llarg de l'eix  $j$. L'índex  $i \in \{1{,}2,3\}$  és la direcció de la polarització generada i  $j \in \{1,\dots,6\}$  la de la tensió mecànica, torsions incloses: el tensor és de  $3 \times 6$. Unitats: C/N, o equivalentment m/V des del punt de vista de l'efecte invers.

Segons com es talli el material, les components dominants de  $d_{\text{ij}}$  són diferents, i també ho és la sensibilitat a força normal o a torsió. En els ceràmics fabricats per *poling* s'escullen orientacions concretes dels elèctrodes respecte del camp de polarització per maximitzar  $d_{33}$  o  $d_{31}$. Els valors tabulats depenen del material, del tall i del procés de fabricació.

## 3 Fabricació i compensació tèrmica

Els millors materials pel que fa a sensibilitat són ceràmics policristal·lins com el PZT, que en estat natural no mostren piezoelectricitat macroscòpica perquè els seus dominis ferroelèctrics estan orientats aleatòriament. El procés de **poling** els hi dona: es calenta el material fins a les proximitats del punt de Curie, s'hi aplica un camp elèctric molt intens que orienta els dipols en una direcció preferent i, mantenint el camp, es refreda lentament, de manera que l'alineament queda congelat. El material preserva llavors la polarització i respon amb càrrega quan es deforma.

![Procés de poling: material amb dominis ferroelèctrics orientats a l'atzar, aplicació d'un camp elèctric intens que els orienta en una direcció preferent, i material resultant amb polarització romanent.](assets/04_Unitat9_Sensors_piezoelectrics_img_3.png)

*Figura: Figura 9.17 Fabricació de material piezoelèctric mitjançant poling.*

Un canvi posterior de les condicions d'operació —temperatura, camp elèctric elevat, tensió mecànica extrema— pot despolaritzar parcialment el material i degradar-ne el rendiment.

> [!WARNING] **Temperatura de Curie $T_c$**
>
> Per sobre de  $T_c$  l'agitació tèrmica destrueix l'ordenació ferroelèctrica dels dipols i el material perd irreversiblement la polarització: encara que després es refredi, cal tornar a polaritzar-lo, cosa que sovint no és factible en un sensor ja encapsulat. Valors típics: uns 300 °C per al PZT, uns 100 °C per al PVDF i per damunt de 500 °C per al quars. Els fabricants recomanen temperatures de treball al voltant de  $T_c/2$  o inferiors per minimitzar la degradació lenta de les propietats.

Tant  $d_{\text{ij}}$  com  $\varepsilon_r$  creixen monòtonament amb la temperatura fins a les proximitats de  $T_c$, on tenen un increment brusc abans de col·lapsar. Com que la tensió generada depèn del quocient  $d_{\text{ij}}/\varepsilon_r$, tots dos factors creixen en el mateix sentit i la compensació és parcial; el quocient, però, no es manté rigorosament constant, de manera que les mesures precises de força exigeixen controlar o monitoritzar la temperatura del material. En alta precisió el sensor incorpora una sonda de temperatura interna i el circuit digital hi corregeix la mesura.

![Sensor piezoelèctric de dues capes separades per elèctrodes: en aplicar una força, la capa superior s'estira i la inferior es comprimeix, mentre que totes dues veuen el mateix canvi de temperatura.](assets/04_Unitat9_Sensors_piezoelectrics_img_4.png)

*Figura: Figura 9.18 Estructura bicapa per a la compensació de la deriva amb la temperatura.*

Una estratègia habitual és construir el sensor amb diverses capes separades per elèctrodes i connectades en sèrie o en paral·lel. Orientades de manera que es deformin en sentit oposat sota la força mecànica però vegin els canvis de temperatura en el mateix sentit, la contribució tèrmica es resta entre capes mentre que la mecànica se suma. S'empra en acceleròmetres i en sensors de flexió. Altres configuracions apilen multicapes primes en paral·lel per augmentar la capacitat i reduir la impedància de sortida, a canvi d'una tensió generada més petita per a la mateixa força.

## 4 Materials

| Família | Representants | Perfil |
|:--- |:--- |:--- |
| **Naturals** | Quars (SiO₂), turmalina, sal de Rochelle | Piezoelèctrics per estructura, sense processat. Coeficients de càrrega baixos, però estabilitat tèrmica i mecànica excel·lent i constants dielèctriques reduïdes. El quars s'usa en oscil·ladors, ressonadors i sensors d'alta estabilitat; la sal de Rochelle té coeficients molt grans però és soluble en aigua. |
| **Ceràmics** | PZT, BaTiO₃, TGS, niobats de sodi i potassi | Compostos inorgànics sintetitzats per exhibir piezoelectricitat després del *poling*. Coeficients de càrrega molt alts i constants dielèctriques també altes. El PZT és la referència en acceleròmetres industrials, transductors d'ultrasons, microposicionadors i hidròfons; la presència de plom ha motivat la recerca en alternatives sense plom. |
| **Orgànics** | PVDF | Polímers processats amb procediments anàlegs als dels ceràmics. Coeficients modestos, però elasticitat elevada, constant dielèctrica molt inferior a la dels ceràmics i mal·leabilitat: làmines primes, formes complexes, grans àrees. Micròfons, sensors de contacte, hidròfons i pel·lícules per a robòtica, amb  $T_c$  de l'ordre de 100 °C. |

| Material | $d_{\text{ij}}$  (pC/N) | $\varepsilon_r$ | Tipus | Característica distintiva |
|:--- |:--- |:--- |:--- |:--- |
| Quars | ≈ 2 | 4,5 | Natural | Estabilitat extrema, baixa sensibilitat |
| BaTiO₃ | ≈ 190 | 1700 | Ceràmic | Pioner, baix cost |
| PZT | 100–600 | 1000–3000 | Ceràmic | Sensibilitat molt alta |
| PVDF | 20–30 | 12 | Orgànic | Flexibilitat,  $d/\varepsilon_r$  alt |
| TGS | variable | ≈ 50 | Ceràmic | Piroelèctric molt utilitzat |

| Objectiu | Material |
|:--- |:--- |
| Màxima sensibilitat en tensió (V/N): interessa  $d/\varepsilon_r$  gran | PVDF |
| Màxima sensibilitat en càrrega (C/N) amb amplificador de càrrega: interessa  $d$  gran | PZT |
| Màxima estabilitat tèrmica i a llarg termini | Quars |
| Sensors flexibles, de gran àrea o de forma complexa | PVDF |
| Actuadors amb desplaçaments importants | PZT |

## 5 Model elèctric

El sensor és una làmina de dielèctric piezoelèctric amb dos elèctrodes metàl·lics dipositats sobre cares oposades: geomètricament, un condensador pla el dielèctric del qual genera càrrega neta a les superfícies quan es deforma. Amb una força  $F$  aplicada en la direcció  $z$  i els elèctrodes perpendiculars a l'eix  $x$, la càrrega que hi apareix és

$$
Q_x = P_x A_x = d_{\text{xz}}\,\sigma_z\,A_x = d_{\text{xz}}\,\frac{F}{A_z}\,A_x \qquad (9.9)
$$

![Bloc de material piezoelèctric amb els elèctrodes sobre les dues cares perpendiculars a l'eix x, acotat amb l'àrea a dels elèctrodes, l'amplada w, l'alçada h i el gruix l entre elèctrodes, i amb els eixos x, y, z.](assets/04_Unitat9_Sensors_piezoelectrics_img_5.png)

*Figura: Figura 9.19 Càlcul de la tensió desenvolupada per un sensor piezoelèctric en aplicar-hi una força.*

on  $A_x = a$  és l'àrea dels elèctrodes i  $A_z = l\,w$  la secció sobre la qual s'aplica la força, amb  $l$  el gruix entre elèctrodes i  $w$  l'amplada. La tensió en bornes és la càrrega dividida per la capacitat,

$$
V = \frac{Q_x}{C}, \qquad C = \varepsilon_0 \varepsilon_r \frac{A_x}{l} \qquad (9.10)
$$

amb  $\varepsilon_r$  la permitivitat relativa del material i  $l$  la separació entre elèctrodes, és a dir el gruix. Substituint-hi la càrrega i la capacitat,

$$
V = \frac{d_{\text{xz}}\,F\,l}{\varepsilon_0 \varepsilon_r A_z} \qquad (9.11)
$$

i, com que  $A_z = l\,w$,

$$
V = \frac{d_{\text{xz}}\,F}{\varepsilon_0 \varepsilon_r\, w} \qquad (9.12)
$$

de manera que la tensió generada depèn només d'una dimensió lateral del material. Si els elèctrodes es curtcircuiten, la càrrega flueix d'una placa a l'altra i el corrent és proporcional a la *variació* de la força,  $i(t) = d_{\text{xz}}\,\frac{\mathrm{d}F}{\mathrm{d}t}$.

El model es completa amb una **resistència de fuita**  $R_s$  en paral·lel amb el condensador, associada a la conductivitat residual del dielèctric, habitualment de gigaohms a teraohms: la càrrega generada acaba descarregant-s'hi. Les capacitats típiques van de pocs pF, en sensors petits o de quars, a algunes desenes de nF, en sensors grans de materials d'alta constant dielèctrica com el PZT. La combinació dona una impedància molt elevada a baixa freqüència, i en particular a la freqüència de la xarxa, amb els problemes d'acoblament capacitiu amb l'entorn que això comporta.

## 6 Resposta freqüencial

![Model elèctric simplificat del sensor piezoelèctric: font de tensió proporcional a la força en sèrie amb el condensador Cs, i la resistència Rs en paral·lel amb el conjunt.](assets/04_Unitat9_Sensors_piezoelectrics_img_6.png)

*Figura: Figura 9.20 Model elèctric simplificat d'un sensor piezoelèctric.*

Amb una font de tensió  $V = k\,F$  en sèrie amb la capacitat  $C_s$  del material i  $R_s$  en paral·lel amb el conjunt, la resposta entre la força aplicada i la tensió de sortida és

$$
\frac{V_\mathrm{out}(j\omega)}{F(j\omega)} = k \cdot \frac{j\omega R_s C_s}{1 + j\omega R_s C_s} \qquad (9.13)
$$

que és un filtre passa-alt de primer ordre amb freqüència de tall

$$
f_{-3\mathrm{dB}} = \frac{1}{2\pi R_s C_s} \qquad (9.14)
$$

El comportament passa-alt té una explicació física directa: amb una força constant, la càrrega generada inicialment es redistribueix a través de  $R_s$  fins que la tensió en bornes s'extingeix. El sensor piezoelèctric és intrínsecament dinàmic i no mesura forces estàtiques.

Quan el sensor es connecta a un circuit de mesura d'impedància d'entrada  $Z_\mathrm{in}$, aquesta queda en paral·lel amb  $R_s$  i la resistència equivalent és  $R_\mathrm{eq} = R_s \parallel Z_\mathrm{in}$, en general més petita que  $R_s$, de manera que la freqüència de tall puja:

$$
f'_{-3\mathrm{dB}} = \frac{1}{2\pi R_\mathrm{eq} C_s} \qquad (9.15)
$$

| Circuit de lectura | Freqüència de tall inferior |
|:--- |:--- |
| Cap: només  $R_s$ | ≈ 16 mHz |
| Oscil·loscopi amb  $Z_\mathrm{in} = 1$  MΩ | ≈ 160 Hz |

Una impedància d'entrada d'1 MΩ desplaça el tall inferior per damunt de 100 Hz. D'aquí que els sensors piezoelèctrics exigeixin circuits de condicionament d'impedància d'entrada extremament alta, anomenats amplificadors electromètrics, o bé amplificadors de càrrega, que mesuren la càrrega transferida en lloc de la tensió. Tots dos es tracten a la unitat 10.

![Resposta freqüencial d'un sensor piezoelèctric: zona plana útil per a l'ús com a sensor i pic de ressonància mecànica a freqüència elevada.](assets/04_Unitat9_Sensors_piezoelectrics_img_7.png)

*Figura: Figura 9.21 Resposta freqüencial d'un sensor piezoelèctric.*

Per l'extrem superior, l'elasticitat i la inèrcia del material introdueixen modes de ressonància mecànica. A la freqüència de ressonància  $f_r$  la deformació per a una força donada és màxima, i també ho és la tensió generada; per damunt, la resposta deixa de ser plana i apareixen pics de sensibilitat amb canvis de fase importants. Com a sensor, la norma és treballar molt per sota de  $f_r$, típicament a menys d' $f_r/5$. Com a actuador, en canvi, la ressonància s'explota: excitar el dispositiu a  $f_r$  dona la màxima deformació per a una excitació elèctrica donada, cosa que interessa en emissors d'ultrasò.

## 7 Aplicacions

![Sensor de força de làmina de PVDF amb elèctrode superior i inferior i fils de connexió, i secció d'un sensor de pressió amb cristall darrere d'un diafragma dins d'un cos roscat.](assets/04_Unitat9_Sensors_piezoelectrics_img_8.png)

*Figura: Figura 9.22 Sensors piezoelèctrics per a la mesura de força i de pressió.*

En la mesura de força o pressió dinàmiques el sensor es col·loca en sèrie amb la línia de força, de manera que tota la força es transmet a través del material: cèl·lules de càrrega dinàmiques de bancs d'assaig, sensors de pressió dins de motors de combustió, sensors de força en robòtica i sensors de tacte. Per a mesures quasi-estàtiques es recorre a amplificadors de càrrega amb constants de temps de desenes de segons.

![Acceleròmetre piezoelèctric amb una massa inercial entre dos cristalls de PZT i els terminals de sortida, i sensor de detonació muntat sobre el bloc d'un motor amb el seu element piezoelèctric i la seva massa.](assets/04_Unitat9_Sensors_piezoelectrics_img_9.png)

*Figura: Figura 9.23 Sensors piezoelèctrics per a la mesura d'acceleració i de vibracions.*

Els acceleròmetres piezoelèctrics són l'aplicació industrial més important. Una massa inercial en contacte amb l'element piezoelèctric hi exerceix una força  $F = m\,a$  quan el sensor s'accelera, de manera que la càrrega generada és proporcional a l'acceleració. La rapidesa de resposta, el rang dinàmic —fins a milers de *g*— i la sensibilitat els fan la base de la monitorització de vibracions de màquines rotatives, motors, compressors i turbines, i s'empren també en sensors d'impacte per al desplegament d'*airbags*, en seguretat sísmica i en botons d'activació per pressió.

L'efecte invers dona lloc a les aplicacions com a actuador: transductors d'ultrasons per a ecografia, sonar, neteja ultrasònica i soldadura; microposicionadors per a microscopis d'efecte túnel i de força atòmica; injectors de motors dièsel, i altaveus miniatura.

| Problema | Origen i mitigació |
|:--- |:--- |
| **Càrrega** | La impedància d'entrada del circuit de mesura retalla la banda baixa. Amplificadors electromètrics o amplificadors de càrrega. |
| **Interferències** | Qualsevol capacitat paràsita entre el sensor i l'entorn acobla la xarxa elèctrica o altres fonts d'EMI a l'entrada de l'amplificador. Apantallament triaxial amb pantalla connectada a guarda, cables curts, amplificador al costat del sensor o integrat dins del mateix encapsulat. |

> [!TIP] **Síntesi**
>
> La piezoelectricitat apareix en les 20 classes cristal·lines sense centre de simetria, i el coeficient  $d_{\text{ij}}$  relaciona la densitat de càrrega sobre la cara perpendicular a l'eix  $i$  amb la tensió mecànica al llarg de l'eix  $j$, en C/N. El sensor és un condensador amb dielèctric actiu: la càrrega val  $Q = d\,F$  i la tensió  $V = d\,F/(\varepsilon_0\varepsilon_r w)$. El *poling* dona resposta macroscòpica als ceràmics i la temperatura de Curie en marca el límit irreversible; les estructures multicapa cancel·len la deriva tèrmica. El PZT maximitza la sensibilitat en càrrega, el PVDF la sensibilitat en tensió gràcies al seu  $d/\varepsilon_r$, i el quars l'estabilitat. La resposta és passa-alt amb tall  $\frac{1}{2\pi R_\mathrm{eq}C_s}$, de manera que el sensor no mesura forces estàtiques i la impedància d'entrada del circuit determina la banda baixa; per dalt, la banda útil acaba molt per sota de la ressonància mecànica.

[← 3. Lleis termoelèctriques, compensació de la unió freda i prestacions](#lleis-termoelèctriques-compensació-de-la-unió-freda-i-prestacions)[5. Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig →](#sensors-piroelèctrics-polarització-espontània-dinàmica-i-detecció-dinfraroig)

---

<!-- FIN CAPÍTULO: 04_Unitat9_Sensors_piezoelectrics -->

---

<!-- INICIO CAPÍTULO: 05_Unitat9_Sensors_piroelectrics -->

# Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig

Sistemes de Mesura · **Unitat 9 — Sensors generadors i unions semiconductores** · Document 5 de 6

# Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig

Dedicació estimada: 13 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Situar la piroelectricitat respecte de la piezoelectricitat en termes de simetria cristal·lina i de magnitud mesurada.
> - Justificar per què el sensor no dona senyal en règim estacionari.
> - Emprar els coeficients piroelèctrics de càrrega i de tensió per estimar la càrrega i la tensió generades.
> - Interpretar la resposta a un pols de radiació a partir de les constants de temps tèrmica i elèctrica.
> - Explicar com un detector PIR modula el flux tèrmic i quines limitacions pràctiques comporta.

## 1 Polarització espontània i efecte piroelèctric

Els sensors piroelèctrics comparteixen materials, estructura i bona part del model circuital amb els piezoelèctrics, però responen al **flux de calor** que travessa el material: aprofiten la variació de la polarització espontània quan el material canvia de temperatura.

De les 32 classes de simetria cristal·lina, 20 mostren efecte piezoelèctric per manca de centre de simetria, i d'aquestes només 10 presenten a més polarització espontània dependent de la temperatura. Tot material piroelèctric és, doncs, piezoelèctric; el recíproc no és cert.

|  | Material piezoelèctric | Material piroelèctric |
|:--- |:--- |:--- |
| **Estat en repòs** | Sense polarització neta, o amb polarització romanent que no dona senyal. | Polarització espontània  $P_s$  present ja en repòs. |
| **Origen del senyal** | La deformació mecànica canvia la polarització. | El canvi de temperatura canvia  $P_s$. |
| **Sense excitació** | Sense deformació no apareix càrrega neta. | A temperatura constant la polarització és constant i la conductivitat del dielèctric compensa la càrrega. |

Formalment, un material piroelèctric és un dielèctric amb polarització espontània en absència de camp elèctric extern i amb

$$
P_s = P_s(T), \qquad \frac{dP_s}{dT} \neq 0 \qquad (9.16)
$$

![Bloc de material piroelèctric amb capa absorbent de calor i elèctrodes: amb les dues cares a la mateixa temperatura la tensió és nul·la, i amb un flux tèrmic infraroig que escalfa la cara frontal apareix una tensió en bornes.](assets/05_Unitat9_Sensors_piroelectrics_img_1.png)

*Figura: Figura 9.24 Efecte piroelèctric.*

A temperatura constant, la càrrega de polarització que apareixeria a les superfícies queda neutralitzada per càrregues lliures del propi dielèctric o de l'aire circumdant, i el sistema arriba a un estat estacionari sense senyal útil. Quan la temperatura canvia, la polarització canvia i les càrregues lliures no tenen temps d'equilibrar-ne la variació: apareix una càrrega neta superficial que es manifesta com un corrent pel circuit extern o com una tensió en bornes.

El sensor respon, doncs, al *canvi* de temperatura i no a la temperatura absoluta. Un cos calent immòbil davant del sensor deixa de produir senyal al cap de poca estona, i és precisament aquest comportament el que fa útils els detectors PIR per detectar moviment o l'aparició sobtada de cossos calents.

## 2 Estructura del sensor

L'estructura és la mateixa que la d'un sensor piezoelèctric: una làmina de material amb dos elèctrodes metàl·lics sobre cares oposades, que formen un condensador pla. Una cara s'orienta a rebre la radiació o el flux tèrmic i l'altra queda en contacte amb un dissipador o amb el substrat. La cara frontal es recobreix amb una capa absorbent d'alta emissivitat que maximitza l'absorció de la radiació incident i la seva conversió en energia tèrmica; mentre hi hagi diferència de temperatura entre les dues cares, la polarització canvia i apareix senyal.

Elèctricament és un condensador de capacitat  $C$  amb una resistència de fuita  $R$  deguda a la conductivitat del dielèctric, alimentat per una font de càrrega que lliura  $Q$  en funció del canvi de temperatura. Les tècniques de condicionament són, per tant, les mateixes: amplificadors electromètrics o amplificadors de càrrega.

Com que tot material piroelèctric és també piezoelèctric, qualsevol tensió mecànica aplicada al sensor hi genera càrrega d'origen piezoelèctric superposada a la d'origen piroelèctric, i si apareix a freqüències comparables a les del senyal útil, degrada la relació senyal-soroll i provoca falsos positius. El disseny ho evita amb un muntatge mecànicament desacoblat: el material es fixa al suport per zones molt petites de la perifèria a través d'elements flexibles, i l'encapsulat incorpora materials absorbidors de vibracions.

> [!WARNING] **Configuració diferencial de dues cel·les**
>
> Molts sensors comercials porten dues cel·les connectades en oposició, una exposada a la radiació i l'altra cega. Totes dues reben les mateixes vibracions mecàniques i els mateixos canvis de temperatura ambient, de manera que aquestes contribucions es cancel·len, mentre que una radiació direccional que només incideix sobre una de les cel·les hi genera un senyal net.

Els materials són en bona part els dels sensors piezoelèctrics —PZT, PVDF, TGS—, als quals s'afegeixen el tantalat de liti (LiTaO₃), molt utilitzat en detectors PIR comercials, i el niobat de liti (LiNbO₃), en sensors d'alta precisió i espectroscòpia. Els monocristalls com el LiTaO₃ tenen coeficients moderats però molt estables; alguns ceràmics arriben a coeficients més alts amb més deriva; el PVDF aporta flexibilitat i sensors grans i barats.

## 3 Coeficients piroelèctrics

El **coeficient piroelèctric de càrrega**  $p_q$  és la variació de la polarització espontània per unitat de canvi de temperatura:

$$
p_q = \frac{dP_s}{dT} = \frac{1}{A}\frac{dQ}{dT} \qquad (9.17)
$$

amb  $A$  la superfície del sensor. Les seves unitats són C/(m²·K), i es tabula habitualment en μC/(m²·K): indica quanta càrrega apareix per unitat d'àrea i per unitat de canvi de temperatura. Els valors van de pocs μC/(m²·K) per al PVDF a desenes o centenars per a materials com el TGS o el LiTaO₃. És el paràmetre que els fabricants destaquen als fulls de característiques, perquè la sensibilitat en càrrega hi és directament proporcional.

El **coeficient piroelèctric de tensió**  $p_v$  relaciona el camp elèctric generat amb el canvi de temperatura:

$$
p_v = \frac{1}{h}\frac{dV}{dT} = \frac{dE}{dT} \qquad (9.18)
$$

amb  $h$  el gruix del sensor, en V/(m·K). Tots dos coeficients estan lligats per la capacitat del sensor:

$$
p_v = \frac{p_q}{\varepsilon_0 \varepsilon_r} \qquad (9.19)
$$

de manera que, per a un mateix  $p_q$, un material de constant dielèctrica més petita, com el PVDF, dona més tensió per unitat de canvi de temperatura. La càrrega i la tensió generades davant d'un canvi de temperatura  $\Delta T$  són

$$
\Delta Q = p_q A\,\Delta T, \qquad \Delta V = p_v h\,\Delta T = \frac{p_q h\,\Delta T}{\varepsilon_0 \varepsilon_r} \qquad (9.20)
$$

i la capacitat s'estima, com en el cas piezoelèctric, a partir de la geometria —àrea dels elèctrodes i gruix de la làmina— i de la permitivitat relativa del material:

$$
C = \frac{\varepsilon_0 \varepsilon_r A}{h} \qquad (9.21)
$$

| Magnitud | Valor |
|:--- |:--- |
| Canvi de temperatura  $\Delta T$ | 0,01 °C |
| Càrrega generada  $\Delta Q$ | ≈ 2,3 pC |
| Tensió generada, amb  $h = 100$  μm i  $\varepsilon_r \approx 40$ | ≈ 650 mV |

Per als materials i les geometries dels detectors comercials les capacitats van de pocs pF a centenars de pF i, amb resistències de fuita de GΩ o TΩ, donen impedàncies de sortida molt elevades. Per això molts sensors integren dins del mateix encapsulat un FET seguidor que rep la càrrega del cristall i n'abaixa la impedància de sortida a un valor manejable.

El coeficient  $p_q$  creix monòtonament amb la temperatura i puja de manera abrupta prop de la temperatura de Curie, on la polarització espontània desapareix i l'efecte piroelèctric es perd. Treballar a prop de  $T_c$  dona sensibilitats elevades amb penalització en estabilitat, perquè petites variacions de temperatura ambient canvien significativament el coeficient; d'aquí que els sensors s'utilitzin força per sota de  $T_c$, i que en aplicacions científiques es mantinguin a temperatura fixa.

## 4 Resposta dinàmica

Davant d'un flux de calor  $\Phi$  constant a partir de  $t = 0$, el material s'escalfa fins a una temperatura més alta i, en règim estacionari, tota la calor absorbida flueix cap a l'entorn per la cara posterior: la polarització espontània torna a ser constant, encara que a un altre valor, i la càrrega generada és zero. El senyal apareix només durant el transitori, amb una constant de temps tèrmica

$$
\tau_T = R_T C_T = R_T\,c\,\rho\,A\,h \qquad (9.22)
$$

on  $R_T$  és la resistència tèrmica efectiva cap a l'entorn,  $c$  la calor específica,  $\rho$  la densitat i  $A\,h$  el volum del sensor. La càrrega generada es reparteix alhora entre la capacitat elèctrica i la resistència equivalent que veu el sensor —el paral·lel de la resistència del dielèctric amb la impedància d'entrada del circuit—, amb una constant de temps elèctrica

$$
\tau_E = R\,C \qquad (9.23)
$$

![Resposta d'un sensor piroelèctric a un pols de radiació: el flux incident en forma d'esglaó produeix una tensió de sortida que puja ràpidament, arriba a un màxim i decau exponencialment.](assets/05_Unitat9_Sensors_piroelectrics_img_2.png)

*Figura: Figura 9.25 Resposta dinàmica d'un sensor piroelèctric davant d'un pols de radiació.*

La tensió observable combina les dues dinàmiques:

$$
V(t) = V_0\left(e^{-t/\tau_E} - e^{-t/\tau_T}\right) \qquad (9.24)
$$

amb  $V_0$  funció del flux tèrmic, del coeficient piroelèctric, de la capacitat i de les dues constants de temps. El resultat és un pols amb una pujada determinada per la més petita de les dues constants i una caiguda determinada per la més gran. Els valors típics són  $\tau_T$  de fraccions de segon a segons i  $\tau_E$  de mil·lisegons a desenes de segons, segons el circuit de mesura.

La tensió de sortida és màxima en els instants en què el flux tèrmic canvia. Per maximitzar la sensibilitat davant d'una font de radiació constant, doncs, cal modular la radiació incident a una freqüència dins de la banda útil del sensor: és la tècnica coneguda com a ***chopping***.

La impedància d'entrada del circuit té aquí el mateix pes que en els sensors piezoelèctrics: si val 1 MΩ, és ella qui domina el paral·lel i fixa  $\tau_E$. Preservar la dinàmica natural a baixa freqüència exigeix amplificadors electromètrics amb corrents de polarització de l'ordre de fA o menys, basats en JFET o MOSFET, sovint integrats dins del mateix encapsulat del sensor.

## 5 Detecció d'infraroig i detectors PIR

Qualsevol cos per damunt del zero absolut emet radiació electromagnètica; els cossos a temperatura ambient ho fan majoritàriament a l'infraroig llunyà, centrat al voltant de 10 μm. El sensor piroelèctric respon a l'energia tèrmica absorbida independentment de la longitud d'ona, de manera que la seva resposta espectral és molt àmplia: és sensible a qualsevol radiació que absorbeixi el seu recobriment, visible, infraroja o fins i tot microones. Els detectors quàntics, com els fotodíodes d'InGaAs o els de HgCdTe, tenen una resposta molt selectiva en longitud d'ona i perden tota sensibilitat fora del seu rang. Els piroelèctrics tampoc no requereixen refrigeració, a diferència d'alguns detectors quàntics que operen a temperatures criogèniques: el sistema és més simple i barat, al preu d'una sensibilitat menor.

![Termòmetre sense contacte: la radiació infraroja de l'objecte arriba al sensor piroelèctric a través d'un disc rotatori amb zones opaques i transparents que la modula.](assets/05_Unitat9_Sensors_piroelectrics_img_3.png)

*Figura: Figura 9.26 Termòmetre sense contacte basat en un sensor piroelèctric i un chopper mecànic.*

![Detector de presència amb una lent de Fresnel que divideix el camp de visió en sectors alternats, de manera que un cos calent en moviment travessa zones sensibles i zones cegues.](assets/05_Unitat9_Sensors_piroelectrics_img_4.png)

*Figura: Figura 9.27 Detector de presència piroelèctric amb lent de Fresnel.*

| Mètode | Funcionament i context |
|:--- |:--- |
| ***Chopper* mecànic** | Un disc rotatori amb zones opaques i transparents entre la font i el sensor fa arribar la radiació en polsos a una freqüència fixada per la velocitat de rotació. És la tècnica clàssica en termometria sense contacte, en espectroscòpia infraroja i en mesures científiques de radiació, i permet aplicar detecció síncrona a l'amplificació per detectar senyals molt febles submergits en soroll. |
| **Lent de Fresnel** | Divideix el camp de visió en múltiples sectors amb sensibilitat alternada. Un cos calent que es mou hi passa alternativament per zones sensibles i cegues, cosa que modula el flux tèrmic de manera natural. És el principi dels detectors de moviment de consum. |

El detector **PIR** (*Passive InfraRed*) allotja un sensor piroelèctric diferencial de dues cel·les dins d'un encapsulat metàl·lic amb una finestra òptica transparent a l'infraroig, i hi col·loca al davant la lent de Fresnel. El moviment d'una persona dins del camp de visió provoca un canvi sobtat de la radiació rebuda, que es tradueix en un pols elèctric i, després d'amplificar-lo i filtrar-lo, en una sortida digital. S'alimenta amb pocs volts, consumeix pocs mA i costa pocs euros, d'aquí el seu ús massiu en il·luminació automàtica, alarmes, obertura de portes i comptadors de persones.

| Limitació | Conseqüència |
|:--- |:--- |
| **No detecta cossos immòbils** | Una persona quieta dins del camp de visió deixa de generar senyal al cap de pocs segons: el sensor no serveix com a comptador de presència. |
| **Sensibilitat a canvis ambientals** | Obertures de finestres, fluxos d'aire calent, llum solar directa o objectes calents en moviment poden provocar falsos positius. |
| **Immunitat limitada a EMI** | El senyal és petit i d'alta impedància. L'encapsulat metàl·lic connectat a massa actua com a gàbia de Faraday. |

| Element | Criteri |
|:--- |:--- |
| **Finestra òptica** | Filtre que talla el visible i l'ultraviolat i deixa passar la banda d'interès, típicament de 7 a 14 μm per a cossos a temperatura ambient. |
| **Filtre elèctric** | Passa-banda centrat a les modulacions esperades, de 0,2 a 5 Hz per al moviment humà. Per sota s'eliminen les derives tèrmiques lentes; per damunt, el soroll i les interferències. |
| **Muntatge mecànic** | Desacoblament de vibracions, que d'altra manera s'acoblarien per l'efecte piezoelèctric del mateix material. |
| **Velocitat** | Amb una banda útil de pocs Hz no es poden mesurar fenòmens ràpids. L'espectroscòpia polsada empra sensors dissenyats amb constants de temps molt petites, amb la corresponent pèrdua de sensibilitat. |

> [!TIP] **Síntesi**
>
> Les 10 classes cristal·lines piroelèctriques tenen polarització espontània dependent de la temperatura; tot material piroelèctric és piezoelèctric, però no a l'inrevés. El senyal apareix quan la temperatura canvia: en règim estacionari la càrrega generada és zero. El coeficient de càrrega  $p_q = dP_s/dT$  dona  $\Delta Q = p_q A \Delta T$, i el de tensió  $p_v = p_q/(\varepsilon_0\varepsilon_r)$  afavoreix els materials de constant dielèctrica baixa. La resposta a un pols de radiació és la diferència de dues exponencials governades per  $\tau_T = R_T C_T$  i  $\tau_E = RC$, i la sortida és màxima quan el flux canvia, cosa que obliga a modular la radiació amb un *chopper* o amb una lent de Fresnel. El detector PIR combina una cel·la diferencial, una finestra de 7 a 14 μm i un passa-banda de 0,2 a 5 Hz, i no detecta cossos immòbils.

[← 4. Sensors piezoelèctrics: efecte, materials, model elèctric i resposta](#sensors-piezoelèctrics-efecte-materials-model-elèctric-i-resposta)[6. Sensors de temperatura basats en unions semiconductores →](#sensors-de-temperatura-basats-en-unions-semiconductores)

---

<!-- FIN CAPÍTULO: 05_Unitat9_Sensors_piroelectrics -->

---

<!-- INICIO CAPÍTULO: 06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora -->

# Sensors de temperatura basats en unions semiconductores

Sistemes de Mesura · **Unitat 9 — Sensors generadors i unions semiconductores** · Document 6 de 6

# Sensors de temperatura basats en unions semiconductores

Dedicació estimada: 12 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Situar els sensors d'unió semiconductora davant de les RTD, els termistors i els termoparells.
> - Deduir de l'equació de Shockley per què la tensió directa d'una unió disminueix quan la temperatura augmenta.
> - Identificar l'origen de la dispersió entre dispositius i la manera de corregir-la.
> - Justificar per què la diferència de dues tensions base-emissor és proporcional a la temperatura absoluta.
> - Estimar l'autoescalfament d'un sensor i enumerar-ne les tècniques de mitigació.

Aquesta família necessita una excitació elèctrica en forma de corrent constant, però aprofita una propietat intrínseca del semiconductor —la dependència de la característica  $i$ – $v$  d'una unió  $p$ - $n$  amb la temperatura— i lliura directament una tensió o un corrent interpretables com a temperatura, sense ponts ni calibratges individuals en la majoria d'aplicacions. És, a més, la família més emprada per la compensació de la unió freda als termoparells.

## 1 Posició dins de les famílies de sensors de temperatura

| Família | Limitació en el context de l'electrònica integrada |
|:--- |:--- |
| **RTD** (unitat 5) | Excel·lent linealitat i exactitud, però exigeixen un bobinat metàl·lic voluminós o una pel·lícula prima amb procés propi, no integrable directament amb CMOS, i un condicionament amb excitació de corrent constant i amplificador d'alta qualitat. |
| **Termistors** (unitat 5) | Sensibilitat molt elevada i cost baix, però resposta fortament no lineal que obliga a taules o polinomis, i valor concret molt dependent del procés, que exigeix calibratge individual. |
| **Termoparells** | Marges de mesura enormes, però sensibilitat reduïda, amplificadors de baixa deriva i compensació de la unió freda. |

Els sensors d'unió semiconductora ocupen el marge de −55 °C a +150 °C, justament el de gairebé tota l'electrònica comercial, amb linealitat raonable, bona exactitud i integrabilitat total. Per damunt d'aquest marge la característica  $i$ – $v$  del material es degrada, i les aplicacions de forn, metal·lúrgia o combustió continuen essent territori dels termoparells.

| Avantatge | Motiu |
|:--- |:--- |
| **Cost** | Fabricació en processos estàndard de semiconductors. Un sensor independent pot costar pocs cèntims, i integrat en un microcontrolador o un SoC el cost marginal de silici és essencialment nul. |
| **Integrabilitat** | El sensor és un transistor bipolar o un díode, fabricable amb els mateixos processos CMOS, BiCMOS o bipolars que la resta del circuit. Permet posar sensors dins de microcontroladors, processadors, FPGA o amplificadors de potència i prendre decisions de control tèrmic en temps real. |
| **Intercanviabilitat** | Les dispersions dins d'un lot són petites i reproduïbles. En moltes aplicacions n'hi ha prou amb les especificacions del fabricant per a exactituds d'alguns graus, i un calibratge de dos punts dura tota la vida útil del sensor. |

Les aplicacions típiques són la monitorització tèrmica de circuits integrats, els termòmetres domèstics, industrials i mèdics, el control tèrmic de bateries, la climatització i la compensació de la unió freda dels termoparells.

## 2 La unió polaritzada a corrent constant

El sensor és una unió  $p$ - $n$  per la qual es fa circular un corrent constant i conegut, i el que es llegeix amb un circuit d'alta impedància és la tensió directa que hi cau.

| Dispositiu | Característiques |
|:--- |:--- |
| **Díode** | Aprofita directament la dependència de la tensió directa amb la temperatura. |
| **Transistor bipolar** | NPN amb col·lector i base curtcircuitats, elèctricament equivalent a un díode: la tensió entre els dos terminals és  $V_{\text{BE}}$. Característica  $i$ – $v$  més propera al model ideal, amb coeficient d'idealitat pròxim a 1 i menys efectes paràsits; fabricació més reproduïble; i admet configuracions de dos transistors que cancel·len  $I_S$. És l'opció dominant. |

![Dues configuracions de sensor amb sortida en tensió: un transistor NPN amb base i col·lector units polaritzat amb una font de corrent constant, i un transistor amb la base a una tensió de referència i el corrent aplicat pel col·lector.](assets/06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora_img_1.png)

*Figura: Figura 9.28 Sensors de temperatura d'unió semiconductora amb sortida en tensió.*

La font de corrent es pot implementar amb una resistència connectada a una alimentació ben regulada, amb un JFET autopolaritzat, amb un mirall de corrent o amb una font integrada. Una segona configuració connecta la base a una tensió de referència i aplica el corrent pel col·lector.

La corba  $i$ – $v$  ideal de la unió en conducció directa és l'equació de Shockley

$$
I = I_S(T)\left(e^{V_{\text{BE}}/V_T} - 1\right) \qquad (9.25)
$$

on  $V_T = kT/q$  és la tensió tèrmica, aproximadament 25,9 mV a 300 K, i  $I_S$  el corrent de saturació inversa, que depèn fortament de la temperatura a través d'una expressió del tipus  $I_S \propto T^3 e^{-E_g/(kT)}$, amb  $E_g$  l'energia de la banda prohibida. En polarització directa amb  $V_{\text{BE}} \gg V_T$  l'exponencial domina i, aïllant la tensió,

$$
V_{\text{BE}}(T, I) = \frac{kT}{q}\ln\frac{I}{I_S(T)} \qquad (9.26)
$$

que amb un corrent constant i conegut és una funció explícita de la temperatura. La tensió, però, *disminueix* en pujar la temperatura, a raó d'uns −2 mV/°C per a corrents de desenes de microamperes: la dependència d' $I_S$  amb la temperatura, a través del factor  $e^{-E_g/(kT)}$, domina sobre la dependència explícita de  $V_T$. Físicament, en pujar la temperatura la concentració de portadors intrínsecs creix ràpidament i cal menys tensió directa per mantenir el corrent que imposa el circuit extern. Combinant-ho tot, la dependència és aproximadament lineal:

$$
V_{\text{BE}}(T) \approx V_{BE0} - S_T\,(T - T_0), \qquad S_T = \frac{V_{g0} - V_{BE0}}{T_0} \qquad (9.27)
$$

amb  $V_{BE0}$  la tensió a la temperatura de referència  $T_0$  i  $V_{g0}$  la tensió corresponent a l'energia de la banda prohibida extrapolada a 0 K, aproximadament 1,2 V per al silici. Amb  $V_{BE0} \approx 0{,}6$  V a 300 K, la sensibilitat  $S_T$  surt de l'ordre de 2 mV/°C. Invertint l'expressió s'obté la temperatura a partir de la lectura:

$$
T = T_0 + \frac{V_{BE0} - V_{\text{BE}}}{S_T} \qquad (9.28)
$$

El pendent depèn logarítmicament del corrent aplicat, de manera que augmentar-lo el mou molt poc i, a partir de cert valor, l'autoescalfament que genera pesa més que el que s'hi guanya. Aquests pocs mV/°C són modestos davant dels centenars de mV/°C d'un termistor NTC muntat en un divisor, però unes deu vegades més grans que els d'un termoparell, cosa que relaxa molt els requeriments de l'amplificador.

## 3 Limitacions i calibratge

| Limitació | Origen |
|:--- |:--- |
| **Repetibilitat d' $I_S$** | El corrent de saturació depèn fortament del procés de fabricació i varia entre dispositius del mateix model, cosa que dispersa  $V_{BE0}$  i  $S_T$  d'un exemplar a un altre. |
| **Variació d' $I_S$  amb la temperatura** | El terme  $T^3 e^{-E_g/(kT)}$  introdueix a  $V_{\text{BE}}(T)$  una contribució d'ordre superior que la recta no recull. |
| **Autoescalfament** | El corrent multiplicat per la tensió és potència dissipada al propi dispositiu. Si és comparable a la capacitat de dissipació cap al medi, el sensor mesura la seva pròpia temperatura. |
| **Corrent constant** | La relació només és fiable amb un corrent constant i conegut: qualsevol variació del corrent es confondria amb un canvi de temperatura. |

![Corbes de tensió base-emissor en funció de la temperatura per a un transistor npn: corba típica amb les corbes mínima i màxima que limiten el comportament esperat dins d'un lot.](assets/06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora_img_2.png)

*Figura: Figura 9.29 Característica $V_{\text{BE}}(T)$ d'un sensor de temperatura amb sortida en tensió basat en transistor NPN.*

Els fabricants publiquen la corba «típica» acompanyada de les corbes «mín.» i «màx.» que limiten el comportament esperat de qualsevol exemplar del lot. La dispersió és considerable: una lectura de 500 mV pot correspondre a temperatures compreses entre uns 50 °C i uns 80 °C segons quin transistor concret s'utilitzi. Un marge de fins a 30 °C obliga a calibrar el sensor individualment, mesurant  $V_{\text{BE}}$  a dues temperatures conegudes per determinar-ne  $V_{BE0}$  i  $S_T$. Un cop calibrat, el dispositiu manté les seves característiques amb molta estabilitat —derives d'alguns mV a l'any—, de manera que un únic calibratge a dos o tres punts serveix per a tota la vida útil.

![Error de linealitat d'un sensor calibrat en funció de la temperatura: la corba d'error s'anul·la a les dues temperatures de calibratge, 10 °C i 120 °C, i s'aparta entremig i als extrems.](assets/06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora_img_3.png)

*Figura: Figura 9.30 Error de linealitat d'un sensor de temperatura calibrat amb sortida en tensió basat en transistor NPN.*

La recta ajustada talla la corba real als dos punts de calibratge i se n'aparta entremig i als extrems. A aquesta no linealitat residual s'hi sumen les variacions del corrent de polarització, l'autoescalfament i les fluctuacions de la tensió de referència o de l'ADC: tot plegat deixa el sensor calibrat entre ±0,5 i ±1 °C en el marge de −40 °C a +125 °C. Un model polinòmic de segon o tercer ordre, habitual en els sensors digitals d'alta precisió, baixa per sota de 0,1 °C.

Alguns productes comercials lliuren una tensió amb sensibilitat normalitzada: el LM35 dona 10 mV/°C sense offset, i el LM50 els mateixos 10 mV/°C amb un offset de 500 mV a 0 °C, que permet mesurar temperatures negatives amb una única alimentació positiva.

## 4 Sensors PTAT amb sortida en corrent

La família més utilitzada en circuits integrats moderns lliura un corrent proporcional a la temperatura absoluta. La idea de base: mentre que la  $V_{\text{BE}}$  d'un únic transistor depèn fortament d' $I_S$  i, per tant, del procés de fabricació, la *diferència*  $V_{BE1} - V_{BE2}$  entre dos transistors idèntics polaritzats amb corrents diferents n'és independent:

$$
V_{BE1} - V_{BE2} = \frac{kT}{q}\ln\frac{I_1}{I_2} \qquad (9.29)
$$

![Principi del sensor PTAT: dos transistors amb corrents o àrees en relació coneguda, la diferència de tensions base-emissor dels quals és una recta que passa per l'origen en temperatura absoluta.](assets/06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora_img_4.png)

*Figura: Figura 9.31 Principi de funcionament dels sensors PTAT.*

Si els dos corrents es mantenen en proporció constant,  $\Delta V_{\text{BE}}$  és una recta que passa per zero a  $T = 0$  K amb un pendent fixat per  $(k/q)\ln(I_1/I_2)$. Amb els mateixos corrents i una relació d'àrees  $n$  —un transistor davant d'un conjunt de  $n$  transistors idèntics en paral·lel— s'obté

$$
V_{BE1} - V_{BE2} = \frac{kT}{q}\ln n \qquad (9.30)
$$

formulació que és la més emprada, per la facilitat de fabricar  $n$  transistors idèntics en un circuit integrat.

![Circuit simplificat d'un sensor PTAT amb sortida en corrent: dos transistors NPN amb relació d'àrees vuit a un, polaritzats amb el mateix corrent per un mirall de corrent, i una resistència R sobre la qual cau la diferència de tensions base-emissor.](assets/06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora_img_5.png)

*Figura: Figura 9.32 Sensor PTAT amb sortida en corrent.*

Al circuit, dos transistors NPN amb relació d'àrees  $n$  es polaritzen amb el mateix corrent de col·lector mitjançant un mirall de corrent. La tensió que cau a la resistència  $R$  és  $V_{BE1} - V_{BE2}$, i com que el corrent total del sensor es reparteix per igual entre les dues branques,

$$
I_T = 2 I_C = \frac{2kT \ln n}{qR} \qquad (9.31)
$$

que és estrictament proporcional a la temperatura absoluta. El representant clàssic és l'**AD590**, que genera 1 μA/K: lliura 298,15 μA a 25 °C i 373,15 μA a 100 °C. La sortida en corrent és robusta davant de les caigudes de tensió en cables llargs i el condicionament es redueix a una resistència de càrrega.

Hi ha també sensors amb **sortida digital**, que integren en un mateix encapsulat el sensor analògic, l'amplificador, un ADC i una interfície de comunicació —I²C, SPI o 1-Wire—: el DS18B20 amb 1-Wire, 12 bits i ±0,5 °C; el TMP102 amb I²C i 13 bits; el MAX30208 amb I²C i ±0,1 °C. L'usuari llegeix un registre i obté la temperatura ja calibrada, compensada i convertida a °C, K o °F.

## 5 Prestacions

| Paràmetre | Valors |
|:--- |:--- |
| **Exactitud** | De ±0,5 a ±2 °C sense calibrar; ±0,1 °C amb calibratge individual. |
| **Resolució** | En sensors digitals, la de l'ADC integrat: típicament de 12 a 16 bits per al rang complet, és a dir 0,01 °C o millor. En sensors analògics, la de l'ADC extern. |
| **Cost** | Pocs cèntims per als analògics simples, poc més d'un euro per als digitals d'alta qualitat, i cost marginal essencialment nul quan s'integra en un xip més gran. |
| **Marge** | De −55 °C a +150 °C aproximadament. |

L'autoescalfament és la font d'error dominant, i especialment en aquests sensors pel seu volum petit. La potència dissipada val  $P = V_{\text{BE}} I$: amb  $V_{\text{BE}} \approx 0{,}6$  V i  $I = 100$  μA són uns 60 μW que, sobre un xip de pocs mm² amb una resistència tèrmica de 100 a 500 K/W cap a l'aire, causen un autoescalfament de 0,006 a 0,03 °C.

| Tècnica | Efecte |
|:--- |:--- |
| **Reduir el corrent de polarització** | Al mínim compatible amb una lectura fiable. |
| **Polaritzar intermitentment** | Moltes implementacions digitals encenen el sensor només durant la conversió i el deixen en repòs entre lectures, cosa que redueix el consum mitjà i l'autoescalfament. |
| **Millorar l'acoblament tèrmic** | Col·locar el sensor sobre un dissipador o triar un encapsulat de baixa resistència tèrmica. |
| **Calibrar-lo** | Mesurar la desviació respecte d'una referència en estat estable i corregir-la al firmware. |

En els sensors PTAT l'autoescalfament és especialment controlable: el corrent és petit, de centenars de μA com a màxim, i la tensió entre terminals es pot triar relativament baixa.

La intercanviabilitat és molt bona gràcies al control del procés de fabricació, però no perfecta. Per a alta precisió, els fabricants calibren cada dispositiu en producció i en desen els coeficients de correcció en una EEPROM interna, cosa que dona sensors intercanviables amb exactituds de fins a ±0,1 °C sense calibratge addicional, com el MAX30208 o el TMP117. En laboratori, quan l'exactitud absoluta és crítica, el calibratge individual amb un bany termostatat i una sonda de referència traçable permet arribar a ±0,05 °C o millor.

> [!TIP] **Síntesi**
>
> Els sensors d'unió semiconductora cobreixen de −55 °C a +150 °C amb cost molt baix, integrabilitat total i bona intercanviabilitat. La tensió directa d'una unió polaritzada amb corrent constant baixa uns 2 mV/°C perquè la dependència de  $I_S$  amb la temperatura domina sobre la de  $V_T$; la sensibilitat depèn logarítmicament del corrent i l'autoescalfament en marca el límit pràctic. La dispersió d' $I_S$  entre dispositius pot arribar a desenes de graus i obliga a calibrar, tot i que un calibratge a dos punts serveix per a tota la vida útil. Els sensors PTAT eviten aquesta dispersió perquè treballen amb la diferència  $\Delta V_{\text{BE}} = (kT/q)\ln n$, independent d' $I_S$, i donen un corrent proporcional a la temperatura absoluta com l'AD590 amb 1 μA/K. Les sortides digitals integren sensor, ADC i interfície i lliuren la temperatura ja calibrada.

[← 5. Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig](#sensors-piroelèctrics-polarització-espontània-dinàmica-i-detecció-dinfraroig)

---

<!-- FIN CAPÍTULO: 06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora -->

---

<!-- INICIO CAPÍTULO: 07_Unitat9_Entrenament -->

# Entrenament V/F · Unitat 9: Unitat 9

Sistemes de Mesura (230920) · ETSETB-UPC · **Unitat 9 — Unitat 9**

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
> 📌 **Afirmació:** *Un sensor generador produeix directament un senyal elèctric a partir de la magnitud física que es vol mesurar.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de sensor generador: la magnitud d'entrada genera directament el senyal.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *En un sensor generador, l'energia del senyal de sortida prové principalment de la font d'alimentació del condicionador.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'energia del senyal prové de la magnitud física d'entrada, a través de la transducció del material.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *Els termoparells, els sensors piezoelèctrics i els sensors piroelèctrics són exemples de sensors generadors.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Són les tres famílies generadores de la unitat, amb Seebeck, efecte piezoelèctric i efecte piroelèctric.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 07
> 📌 **Afirmació:** *Els termoparells poden ser adequats per a temperatures molt elevades on una unió semiconductora quedaria fora del seu marge d'ús.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El silici funciona entre −55 °C i +150 °C, mentre que els termoparells arriben a més de 1500 °C.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 09
> 📌 **Afirmació:** *L'efecte Seebeck associa una diferència de tensió a un gradient de temperatura en un conductor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la descripció de l'efecte: el gradient tèrmic dona una diferència de tensió entre els extrems.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 12
> 📌 **Afirmació:** *La sensibilitat d'un termoparell augmenta quan els dos materials tenen coeficients de Seebeck absoluts molt semblants.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal que els coeficients absoluts siguin de signe oposat perquè α₁₂ sigui tan gran com sigui possible.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *La unió calenta és el punt del termoparell situat a la temperatura que es vol mesurar.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La unió calenta o de mesura és el punt d'unió física, situat a la temperatura que es vol conèixer.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 17
> 📌 **Afirmació:** *La tensió ideal d'un termoparell és la integral del coeficient de Seebeck diferencial entre la temperatura de referència i la de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (9.3): la integral d'α₁₂(T) entre T_r i T_o.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 20
> 📌 **Afirmació:** *Els polinomis de termoparells normalitzats solen prescindir de la temperatura de referència assumida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Els polinomis assumeixen sempre la unió freda a 0 °C.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *Els efectes Peltier i Thomson desapareixen com a fonts d'error quan es força un corrent elevat pel termoparell.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *S'eliminen mantenint el corrent per les unions pròxim a zero, no forçant-hi corrent.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 29
> 📌 **Afirmació:** *Els termoparells normalitzats faciliten la intercanviabilitat entre sensors del mateix tipus.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La norma fixa composicions i corbes, de manera que dos sensors del mateix tipus són equivalents.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *Els termoparells de platí-rodi es fan servir principalment per mesures de baixa temperatura i baix cost.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *R, S i B arriben a més de 1800 °C i tenen cost elevat.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *El tipus T és habitual en aplicacions de molt alta temperatura per sobre dels termoparells de platí-rodi.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El tipus T arriba fins a +400 °C.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 37
> 📌 **Afirmació:** *El tipus N es pot considerar una alternativa al tipus K amb millor estabilitat a alta temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El nicrosil–nisil és l'alternativa al K amb millor estabilitat a alta temperatura.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 41
> 📌 **Afirmació:** *La primera llei dels metalls intermedis justifica introduir un tercer metall si les dues noves unions estan a la mateixa temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'enunciat de la primera llei dels metalls intermedis.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *La llei de les temperatures intermèdies obliga a disposar d'una taula diferent per a cada temperatura ambiental possible.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Precisament permet tabular sempre amb la unió freda a 0 °C i corregir després.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *La compensació de la unió freda es basa en sumar a la tensió mesurada la tensió equivalent de la unió de referència respecte a 0 °C.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (9.7): V_corr = V + V(T_r, 0).*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 52
> 📌 **Afirmació:** *La CJC només es pot fer amb un bany de gel físic a 0 °C.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Qualsevol sensor absolut serveix; el més habitual és un sensor integrat d'unió semiconductora.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 55
> 📌 **Afirmació:** *L'error en la mesura de la temperatura de la unió freda es propaga directament a l'estimació final de la unió calenta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un error de 0,5 °C en T_r dona un error del mateix ordre en T_o.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 62
> 📌 **Afirmació:** *L'offset de l'amplificador és negligible en termoparells perquè el senyal de sortida és de gran amplitud.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El senyal és de desenes de μV/°C: l'offset hi és l'error dominant.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 81
> 📌 **Afirmació:** *L'efecte piezoelèctric directe converteix una tensió mecànica en càrrega elèctrica mesurable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de l'efecte directe: tensió mecànica en càrrega elèctrica.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 84
> 📌 **Afirmació:** *Tots els cristalls amb simetria central presenten una resposta piezoelèctrica macroscòpica intensa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En un cristall centrosimètric el moment dipolar net és nul i la deformació preserva la neutralitat.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 89
> 📌 **Afirmació:** *El mateix element piezoelèctric pot funcionar com a sensor per efecte directe i com a actuador per efecte invers.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'efecte és reversible i el mateix element pot fer d'emissor i de receptor.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 92
> 📌 **Afirmació:** *El model elèctric bàsic d'un sensor piezoelèctric és una resistència metàl·lica pura de valor gairebé zero.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El model és un condensador amb una resistència de fuita en paral·lel, no una resistència metàl·lica.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 95
> 📌 **Afirmació:** *En circuit obert, la càrrega piezoelèctrica generada pot donar lloc a una tensió en bornes.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació V = Q/C.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 98
> 📌 **Afirmació:** *Els sensors piezoelèctrics són l'opció natural per mesurar forces completament estàtiques durant temps indefinit.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La resposta és passa-alt: amb força constant la tensió en bornes s'extingeix.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 101
> 📌 **Afirmació:** *El model dinàmic elèctric d'un piezoelèctric té comportament de filtre passa-alt a baixa freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (9.13), un passa-alt de primer ordre.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 104
> 📌 **Afirmació:** *Connectar una entrada d'1 MΩ a un sensor piezoelèctric sempre millora la resposta a baixa freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Amb 1 MΩ i 1 nF el tall puja a uns 160 Hz, davant dels 16 mHz del sensor sol.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 109
> 📌 **Afirmació:** *Per mesura lineal, un sensor piezoelèctric se sol fer treballar prou per sota de la seva ressonància mecànica.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La norma com a sensor és treballar per sota d'f_r/5.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 116
> 📌 **Afirmació:** *El PZT és un material orgànic flexible caracteritzat per una constant dielèctrica molt baixa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El PZT és un ceràmic amb constant dielèctrica de 1000 a 3000.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 120
> 📌 **Afirmació:** *El PVDF té una temperatura de Curie tan alta que és ideal per a forns industrials de molt alta temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La temperatura de Curie del PVDF és de l'ordre de 100 °C.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 121
> 📌 **Afirmació:** *Els sensors piroelèctrics aprofiten la variació de la polarització espontània amb la temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de l'efecte piroelèctric.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 126
> 📌 **Afirmació:** *La sortida piroelèctrica és màxima quan el flux tèrmic és constant durant un temps molt llarg.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En règim estacionari la polarització torna a ser constant i la càrrega generada és zero.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 127
> 📌 **Afirmació:** *L'estructura bàsica d'un sensor piroelèctric és similar a un condensador amb dielèctric actiu i elèctrodes.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Làmina de material amb dos elèctrodes sobre cares oposades: un condensador pla.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 130
> 📌 **Afirmació:** *La radiació absorbida genera càrrega piroelèctrica sense cap canvi de temperatura del material.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El senyal apareix perquè el material canvia de temperatura i amb ell la polarització.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 133
> 📌 **Afirmació:** *El coeficient de tensió piroelèctric augmenta quan el coeficient de càrrega és gran i la permitivitat és petita.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (9.19): p_v = p_q/(ε₀ε_r).*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 141
> 📌 **Afirmació:** *La constant de temps tèrmica depèn de la resistència tèrmica i de la capacitat tèrmica efectiva del sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'equació (9.22): τ_T = R_T C_T = R_T c ρ A h.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 144
> 📌 **Afirmació:** *La constant de temps elèctrica augmenta quan es redueix dràsticament la impedància d'entrada del condicionador.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Una impedància d'entrada baixa domina el paral·lel i redueix τ_E.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 148
> 📌 **Afirmació:** *El chopping redueix la detectabilitat perquè transforma el senyal en una component purament contínua.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El chopping fa justament el contrari: converteix una radiació contínua en un senyal periòdic.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 153
> 📌 **Afirmació:** *Els sensors piroelèctrics diferencials de dues cel·les poden reduir la influència de vibracions i canvis ambientals comuns.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Les dues cel·les veuen les mateixes vibracions i el mateix canvi ambiental, que es cancel·len.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 158
> 📌 **Afirmació:** *Els sensors piroelèctrics requereixen habitualment refrigeració criogènica per funcionar en detecció d'infraroig de consum.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *No requereixen refrigeració, a diferència d'alguns detectors quàntics d'infraroig.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 163
> 📌 **Afirmació:** *Els sensors de temperatura de silici aprofiten la dependència de la característica d'una unió p-n amb la temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la propietat que aprofiten: la dependència de la característica i–v amb la temperatura.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 166
> 📌 **Afirmació:** *Els sensors semiconductors són la tecnologia preferent per mesurar temperatures de més de 1000 °C en forns industrials.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Per damunt de +150 °C la característica es degrada; els forns són territori dels termoparells.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 171
> 📌 **Afirmació:** *La sensibilitat típica de VBE amb temperatura és de l'ordre de pocs mil·livolts per grau Celsius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És de l'ordre de −2 mV/°C amb corrents de desenes de microamperes.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 174
> 📌 **Afirmació:** *El corrent de saturació inversa d'una unió de silici és pràcticament constant amb la temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *I_S depèn fortament de la temperatura, com T³e^(−E_g/kT).*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 182
> 📌 **Afirmació:** *Augmentar indefinidament el corrent de polarització millora la mesura perquè l'autoescalfament desapareix.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Més corrent vol dir més potència dissipada i més autoescalfament.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 187
> 📌 **Afirmació:** *Els sensors PTAT generen una magnitud proporcional a la temperatura absoluta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *PTAT vol dir proporcional a la temperatura absoluta.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 190
> 📌 **Afirmació:** *La diferència de VBE entre dos transistors idèntics depèn fortament del valor absolut del corrent de saturació IS.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *I_S es cancel·la en restar les dues tensions base-emissor.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 193
> 📌 **Afirmació:** *En un sensor PTAT amb sortida en corrent, una resistència pot convertir el corrent en una tensió mesurable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Una resistència de càrrega converteix el corrent en una tensió interpretable.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 198
> 📌 **Afirmació:** *Els sensors semiconductors són difícils d'integrar perquè necessiten bobinats de platí de gran volum.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El bobinat de platí és de les RTD; el sensor semiconductor és un transistor o un díode.*

> **📚 Document de referència:** `Document 06`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | És la definició de sensor generador: la magnitud d'entrada genera directament el senyal. | Document 01 |
| **04** | **F** | L'energia del senyal prové de la magnitud física d'entrada, a través de la transducció del material. | Document 01 |
| **05** | **V** | Són les tres famílies generadores de la unitat, amb Seebeck, efecte piezoelèctric i efecte piroelèctric. | Document 01 |
| **07** | **V** | El silici funciona entre −55 °C i +150 °C, mentre que els termoparells arriben a més de 1500 °C. | Document 06 |
| **09** | **V** | És la descripció de l'efecte: el gradient tèrmic dona una diferència de tensió entre els extrems. | Document 01 |
| **12** | **F** | Cal que els coeficients absoluts siguin de signe oposat perquè α₁₂ sigui tan gran com sigui possible. | Document 01 |
| **13** | **V** | La unió calenta o de mesura és el punt d'unió física, situat a la temperatura que es vol conèixer. | Document 01 |
| **17** | **V** | És l'equació (9.3): la integral d'α₁₂(T) entre T_r i T_o. | Document 02 |
| **20** | **F** | Els polinomis assumeixen sempre la unió freda a 0 °C. | Document 02 |
| **26** | **F** | S'eliminen mantenint el corrent per les unions pròxim a zero, no forçant-hi corrent. | Document 01 |
| **29** | **V** | La norma fixa composicions i corbes, de manera que dos sensors del mateix tipus són equivalents. | Document 02 |
| **32** | **F** | R, S i B arriben a més de 1800 °C i tenen cost elevat. | Document 02 |
| **34** | **F** | El tipus T arriba fins a +400 °C. | Document 02 |
| **37** | **V** | El nicrosil–nisil és l'alternativa al K amb millor estabilitat a alta temperatura. | Document 02 |
| **41** | **V** | És l'enunciat de la primera llei dels metalls intermedis. | Document 03 |
| **48** | **F** | Precisament permet tabular sempre amb la unió freda a 0 °C i corregir després. | Document 03 |
| **49** | **V** | És l'equació (9.7): V_corr = V + V(T_r, 0). | Document 03 |
| **52** | **F** | Qualsevol sensor absolut serveix; el més habitual és un sensor integrat d'unió semiconductora. | Document 03 |
| **55** | **V** | Un error de 0,5 °C en T_r dona un error del mateix ordre en T_o. | Document 03 |
| **62** | **F** | El senyal és de desenes de μV/°C: l'offset hi és l'error dominant. | Document 03 |
| **81** | **V** | És la definició de l'efecte directe: tensió mecànica en càrrega elèctrica. | Document 04 |
| **84** | **F** | En un cristall centrosimètric el moment dipolar net és nul i la deformació preserva la neutralitat. | Document 04 |
| **89** | **V** | L'efecte és reversible i el mateix element pot fer d'emissor i de receptor. | Document 04 |
| **92** | **F** | El model és un condensador amb una resistència de fuita en paral·lel, no una resistència metàl·lica. | Document 04 |
| **95** | **V** | És l'equació V = Q/C. | Document 04 |
| **98** | **F** | La resposta és passa-alt: amb força constant la tensió en bornes s'extingeix. | Document 04 |
| **101** | **V** | És l'equació (9.13), un passa-alt de primer ordre. | Document 04 |
| **104** | **F** | Amb 1 MΩ i 1 nF el tall puja a uns 160 Hz, davant dels 16 mHz del sensor sol. | Document 04 |
| **109** | **V** | La norma com a sensor és treballar per sota d'f_r/5. | Document 04 |
| **116** | **F** | El PZT és un ceràmic amb constant dielèctrica de 1000 a 3000. | Document 04 |
| **120** | **F** | La temperatura de Curie del PVDF és de l'ordre de 100 °C. | Document 04 |
| **121** | **V** | És la definició de l'efecte piroelèctric. | Document 05 |
| **126** | **F** | En règim estacionari la polarització torna a ser constant i la càrrega generada és zero. | Document 05 |
| **127** | **V** | Làmina de material amb dos elèctrodes sobre cares oposades: un condensador pla. | Document 05 |
| **130** | **F** | El senyal apareix perquè el material canvia de temperatura i amb ell la polarització. | Document 05 |
| **133** | **V** | És l'equació (9.19): p_v = p_q/(ε₀ε_r). | Document 05 |
| **141** | **V** | És l'equació (9.22): τ_T = R_T C_T = R_T c ρ A h. | Document 05 |
| **144** | **F** | Una impedància d'entrada baixa domina el paral·lel i redueix τ_E. | Document 05 |
| **148** | **F** | El chopping fa justament el contrari: converteix una radiació contínua en un senyal periòdic. | Document 05 |
| **153** | **V** | Les dues cel·les veuen les mateixes vibracions i el mateix canvi ambiental, que es cancel·len. | Document 05 |
| **158** | **F** | No requereixen refrigeració, a diferència d'alguns detectors quàntics d'infraroig. | Document 05 |
| **163** | **V** | És la propietat que aprofiten: la dependència de la característica i–v amb la temperatura. | Document 06 |
| **166** | **F** | Per damunt de +150 °C la característica es degrada; els forns són territori dels termoparells. | Document 06 |
| **171** | **V** | És de l'ordre de −2 mV/°C amb corrents de desenes de microamperes. | Document 06 |
| **174** | **F** | I_S depèn fortament de la temperatura, com T³e^(−E_g/kT). | Document 06 |
| **182** | **F** | Més corrent vol dir més potència dissipada i més autoescalfament. | Document 06 |
| **187** | **V** | PTAT vol dir proporcional a la temperatura absoluta. | Document 06 |
| **190** | **F** | I_S es cancel·la en restar les dues tensions base-emissor. | Document 06 |
| **193** | **V** | Una resistència de càrrega converteix el corrent en una tensió interpretable. | Document 06 |
| **198** | **F** | El bobinat de platí és de les RTD; el sensor semiconductor és un transistor o un díode. | Document 06 |

<!-- FIN CAPÍTULO: 07_Unitat9_Entrenament -->

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
| **(9.1)** | $V_y = (\alpha_1 - \alpha_2)(T_1 - T_2)$ |
| **(9.2)** | $\alpha_{12}(T) = \alpha_1(T) - \alpha_2(T)$ |
| **(9.3)** | $V = \int_{T_r}^{T_o} \alpha_{12}(T)\,dT$ |
| **(9.4)** | $V \approx \alpha_{12}\,(T_o - T_r)$ |
| **(9.5)** | $T = c_0 + c_1 x + c_2 x^2 + \cdots + c_n x^n$ |
| **(9.6)** | $V = V(T_o, 0) - V(T_r, 0)$ |
| **(9.7)** | $V_\mathrm{corr} = V + V(T_r, 0)$ |
| **(9.8)** | $P_i = \sum_j d_{\text{ij}}\,\sigma_j$ |
| **(9.9)** | $Q_x = P_x A_x = d_{\text{xz}}\,\sigma_z\,A_x = d_{\text{xz}}\,\frac{F}{A_z}\,A_x$ |
| **(9.10)** | $V = \frac{Q_x}{C}, \qquad C = \varepsilon_0 \varepsilon_r \frac{A_x}{l}$ |
| **(9.11)** | $V = \frac{d_{\text{xz}}\,F\,l}{\varepsilon_0 \varepsilon_r A_z}$ |
| **(9.12)** | $V = \frac{d_{\text{xz}}\,F}{\varepsilon_0 \varepsilon_r\, w}$ |
| **(9.13)** | $\frac{V_\mathrm{out}(j\omega)}{F(j\omega)} = k \cdot \frac{j\omega R_s C_s}{1 + j\omega R_s C_s}$ |
| **(9.14)** | $f_{-3\mathrm{dB}} = \frac{1}{2\pi R_s C_s}$ |
| **(9.15)** | $f'_{-3\mathrm{dB}} = \frac{1}{2\pi R_\mathrm{eq} C_s}$ |
| **(9.16)** | $P_s = P_s(T), \qquad \frac{dP_s}{dT} \neq 0$ |
| **(9.17)** | $p_q = \frac{dP_s}{dT} = \frac{1}{A}\frac{dQ}{dT}$ |
| **(9.18)** | $p_v = \frac{1}{h}\frac{dV}{dT} = \frac{dE}{dT}$ |
| **(9.19)** | $p_v = \frac{p_q}{\varepsilon_0 \varepsilon_r}$ |
| **(9.20)** | $\Delta Q = p_q A\,\Delta T, \qquad \Delta V = p_v h\,\Delta T = \frac{p_q h\,\Delta T}{\varepsilon_0 \varepsilon_r}$ |
| **(9.21)** | $C = \frac{\varepsilon_0 \varepsilon_r A}{h}$ |
| **(9.22)** | $\tau_T = R_T C_T = R_T\,c\,\rho\,A\,h$ |
| **(9.23)** | $\tau_E = R\,C$ |
| **(9.24)** | $V(t) = V_0\left(e^{-t/\tau_E} - e^{-t/\tau_T}\right)$ |
| **(9.25)** | $I = I_S(T)\left(e^{V_{\text{BE}}/V_T} - 1\right)$ |
| **(9.26)** | $V_{\text{BE}}(T, I) = \frac{kT}{q}\ln\frac{I}{I_S(T)}$ |
| **(9.27)** | $V_{\text{BE}}(T) \approx V_{BE0} - S_T\,(T - T_0), \qquad S_T = \frac{V_{g0} - V_{BE0}}{T_0}$ |
| **(9.28)** | $T = T_0 + \frac{V_{BE0} - V_{\text{BE}}}{S_T}$ |
| **(9.29)** | $V_{BE1} - V_{BE2} = \frac{kT}{q}\ln\frac{I_1}{I_2}$ |
| **(9.30)** | $V_{BE1} - V_{BE2} = \frac{kT}{q}\ln n$ |
| **(9.31)** | $I_T = 2 I_C = \frac{2kT \ln n}{qR}$ |