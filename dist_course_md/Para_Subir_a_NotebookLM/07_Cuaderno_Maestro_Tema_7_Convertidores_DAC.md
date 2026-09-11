# 📚 Cuaderno Maestro: Tema 7

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 7` | 📄 **Capítulos incluidos:** 8  
> 📅 **Generado:** 2026-09-11 19:10

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 7 — Sensors reactius i electromagnètics · Lectura prèvia](#unitat-7-sensors-reactius-i-electromagnètics-lectura-prèvia)
2. [Fonaments dels sensors reactius](#fonaments-dels-sensors-reactius)
   - [1 Què és un sensor reactiu](#1-què-és-un-sensor-reactiu)
   - [2 Per què reactius i no resistius](#2-per-què-reactius-i-no-resistius)
   - [3 El cost: cal treballar en alterna](#3-el-cost-cal-treballar-en-alterna)
   - [4 La freqüència de treball com a paràmetre de disseny](#4-la-freqüència-de-treball-com-a-paràmetre-de-disseny)
   - [5 Els quatre mecanismes de transducció de la unitat](#5-els-quatre-mecanismes-de-transducció-de-la-unitat)
   - [6 On es troben aquests sensors](#6-on-es-troben-aquests-sensors)
3. [El sensor capacitiu: model, geometries i linealitat](#el-sensor-capacitiu-model-geometries-i-linealitat)
   - [1 La capacitat com a variable de mesura](#1-la-capacitat-com-a-variable-de-mesura)
   - [2 El condensador pla](#2-el-condensador-pla)
   - [3 Impedància i linealitat](#3-impedància-i-linealitat)
   - [4 Les tres variants del condensador pla](#4-les-tres-variants-del-condensador-pla)
   - [5 Altres geometries](#5-altres-geometries)
   - [6 La tria del dielèctric](#6-la-tria-del-dielèctric)
4. [El sensor capacitiu real: vores, guardes, fuita i freqüència de treball](#el-sensor-capacitiu-real-vores-guardes-fuita-i-freqüència-de-treball)
   - [1 Avantatges i limitacions](#1-avantatges-i-limitacions)
   - [2 L'efecte de vores](#2-lefecte-de-vores)
   - [3 Les guardes de Kelvin](#3-les-guardes-de-kelvin)
   - [4 La resistència de fuita del dielèctric](#4-la-resistència-de-fuita-del-dielèctric)
   - [5 La tria de la freqüència de treball](#5-la-tria-de-la-freqüència-de-treball)
   - [6 Conseqüències per al condicionador](#6-conseqüències-per-al-condicionador)
5. [Aplicacions dels sensors capacitius i el condensador diferencial](#aplicacions-dels-sensors-capacitius-i-el-condensador-diferencial)
   - [1 Distància, desplaçament i presència](#1-distància-desplaçament-i-presència)
   - [2 Força i pressió](#2-força-i-pressió)
   - [3 Angle, nivell i inclinació](#3-angle-nivell-i-inclinació)
   - [4 Acceleració: els acceleròmetres MEMS](#4-acceleració-els-acceleròmetres-mems)
   - [5 El condensador diferencial](#5-el-condensador-diferencial)
6. [Sensors inductius i corrents de Foucault](#sensors-inductius-i-corrents-de-foucault)
   - [1 L'autoinductància](#1-lautoinductància)
   - [2 Reluctància i entreferro](#2-reluctància-i-entreferro)
   - [3 Què fa variar la inductància](#3-què-fa-variar-la-inductància)
   - [4 Inductància mútua i necessitat d'excitació alterna](#4-inductància-mútua-i-necessitat-dexcitació-alterna)
   - [5 Objectiu metàl·lic: limitació i fortalesa](#5-objectiu-metàllic-limitació-i-fortalesa)
   - [6 La tria del nucli i del conductor](#6-la-tria-del-nucli-i-del-conductor)
   - [7 Aplicacions dels sensors de bobina](#7-aplicacions-dels-sensors-de-bobina)
   - [8 Corrents de Foucault](#8-corrents-de-foucault)
7. [Transformadors variables, efecte Hall i magnetostricció](#transformadors-variables-efecte-hall-i-magnetostricció)
   - [1 Transformadors variables](#1-transformadors-variables)
   - [2 La LVDT](#2-la-lvdt)
   - [3 El resolver](#3-el-resolver)
   - [4 Sensors d'efecte Hall](#4-sensors-defecte-hall)
   - [5 Sensors magnetostrictius](#5-sensors-magnetostrictius)
8. [Entrenament V/F · Unitat 7: Sensors reactius i electromagnètics](#entrenament-vf-unitat-7-sensors-reactius-i-electromagnètics)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_Unitat7_Index -->

# Unitat 7 — Sensors reactius i electromagnètics · Lectura prèvia

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 7 — Sensors reactius i electromagnètics

Materials de lectura prèvia · dedicació total estimada: 68 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents contenen tot el que cal per preparar la unitat.

Llegeix els sis documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor.

### [1. Fonaments dels sensors reactius](#fonaments-dels-sensors-reactius)

Què és un sensor reactiu i per quines raons físiques es prefereix al resistiu: mesura sense contacte, tolerància a entorns bruts, absència de soroll tèrmic i d'autoescalfament de l'element ideal. Per què cap dels dos tipus no es pot mesurar en contínua i què implica treballar en alterna. La freqüència de treball com a paràmetre de disseny i el que la condiciona. Sensors moduladors davant de generadors. Els quatre mecanismes de transducció de la unitat i on es troben aquests sensors.

*⏱️ Dedicació estimada: 8 min*

### [2. El sensor capacitiu: model, geometries i linealitat](#el-sensor-capacitiu-model-geometries-i-linealitat)

La capacitat com a variable de mesura i la funció de mesura C=g(x). El condensador pla C=epsilon·A/d, la condició d<<l i els ordres de magnitud. Impedància del condensador i l'asimetria de linealitat: si varia l'àrea o la permitivitat respon linealment C, i si varia la separació respon linealment el mòdul de la impedància. Les tres variants del condensador pla —àrea, separació i dielèctric variables— i les geometries esfèrica, coaxial, de cables paral·lels i de cable sobre pla. Criteris de tria del dielèctric.

*⏱️ Dedicació estimada: 8 min*

### [3. El sensor capacitiu real: vores, guardes, fuita i freqüència de treball](#el-sensor-capacitiu-real-vores-guardes-fuita-i-freqüència-de-treball)

Avantatges i limitacions respecte del sensor resistiu, incloses les capacitats paràsites i la seva deriva. L'efecte de vores: origen, error de Bromwich, dependència amb d/l i la no linealitat que introdueix. Modelat per elements finits i guardes de Kelvin, en una cara i en totes dues. La resistència de fuita del dielèctric, el model C en paral·lel amb Rp, el producte Rp·C=epsilon/sigma i la freqüència de tall. Tria de f0: per damunt de f-3dB i amb el mòdul d'impedància dins d'un rang manejable. Soroll i autoescalfament residuals.

*⏱️ Dedicació estimada: 12 min*

### [4. Aplicacions dels sensors capacitius i el condensador diferencial](#aplicacions-dels-sensors-capacitius-i-el-condensador-diferencial)

Distància i desplaçament amb resolució nanomètrica, detecció de presència per pertorbació del camp, força i pressió a través d'un element elàstic, angle per solapament, nivell per permitivitat, inclinació i acceleració. Acceleròmetres MEMS de dents interdigitades i sensibilitat de l'ordre de pF/g. El condensador diferencial: model C0±deltaC, el quocient diferencial normalitzat, i els tres avantatges —sensibilitat doble, rebuig de mode comú i linealitat millorada.

*⏱️ Dedicació estimada: 8 min*

### [5. Sensors inductius i corrents de Foucault](#sensors-inductius-i-corrents-de-foucault)

Autoinductància, model del solenoide i el significat de cada factor. Reluctància, entreferro i la relació L=N²/R. Què fa variar la inductància i com hi actuen els materials ferromagnètics i els conductors no ferromagnètics. Inductància mútua i la necessitat d'excitació alterna. L'objectiu metàl·lic com a limitació i com a fortalesa. Bobina d'aire davant de nucli ferromagnètic, ferrites i tria del conductor. Aplicacions de distància, força, gir, gruix i pressió. Corrents de Foucault, efecte pell, profunditat de penetració, mesura de distància a conductors no ferromagnètics i inspecció no destructiva.

*⏱️ Dedicació estimada: 15 min*

### [6. Transformadors variables, efecte Hall i magnetostricció](#transformadors-variables-efecte-hall-i-magnetostricció)

La LVDT: construcció en sèrie i oposició, sortida proporcional al desplaçament, posició de nul i tensió residual, fase de 0 o 180 graus per al signe, efectes no ideals i freqüència d'excitació òptima. El resolver: dependència en cosinus, dos secundaris en quadratura, atan2 i RDC, errors angulars; synchro i inductosyn. Efecte Hall: força de Lorentz, tensió Hall, per què semiconductors, compromís del gruix, comparació amb la magnetoresistència i aplicacions de presència, velocitat de rotació i mesura de corrent. Magnetostricció: efectes Joule, Villari, Wiedemann i Mateucci, Terfenol-D, sensors de temps de vol, de força i de torsió.

*⏱️ Dedicació estimada: 17 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

<!-- FIN CAPÍTULO: 00_Unitat7_Index -->

---

<!-- INICIO CAPÍTULO: 01_Unitat7_Fonaments_dels_sensors_reactius -->

# Fonaments dels sensors reactius

Sistemes de Mesura · **Unitat 7 — Sensors reactius i electromagnètics** · Document 1 de 6

# Fonaments dels sensors reactius

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Delimitar què és un sensor reactiu i per quines raons físiques es prefereix a un sensor resistiu.
> - Justificar per què un sensor reactiu no pot mesurar-se en contínua.
> - Situar la freqüència de treball  $f_0$
> com a paràmetre de disseny i enumerar què la condiciona.
> - Classificar els sensors del tema com a moduladors i distingir-los dels generadors.
> - Identificar els quatre mecanismes de transducció que es tracten en aquesta unitat.

A la unitat 5 s'han estudiat els sensors resistius, la família més coneguda històricament. Aquesta unitat tracta les altres dues del mateix grup —els **sensors capacitius** i els **sensors inductius**, que en conjunt reben el nom de **sensors reactius**— i, a més, dos grups basats en efectes electromagnètics que no encaixen en cap de les dues: els sensors d'**efecte Hall**, que donen una tensió transversal proporcional al camp magnètic que travessa una làmina conductora, i els sensors **magnetostrictius**, que exploten l'acoblament entre magnetització i deformació mecànica d'alguns materials ferromagnètics.

## 1 Què és un sensor reactiu

Un sensor és **reactiu** quan el seu element sensor és un condensador o una bobina, és a dir, un element de naturalesa **reactiva i no dissipativa**: emmagatzema energia en un camp —elèctric en el condensador, magnètic en la bobina— en lloc de convertir-la en calor. El mesurand actua modificant la capacitat, l'autoinductància o la inductància mútua de l'element, i el sistema de mesura llegeix aquesta variació d'impedància.

Tots els sensors d'aquesta unitat, inclosos els d'efecte Hall i els magnetostrictius, són **sensors moduladors**: el mesurand modifica alguna propietat del sensor però no aporta l'energia del senyal de sortida, que prové d'una **excitació externa**.

La distinció importa perquè alguns d'aquests sensors lliuren una tensió al terminal de sortida i podrien confondre's amb generadors. És el cas de la **LVDT**, un transformador de nucli mòbil que dona una tensió proporcional al desplaçament: sense excitació al seu bobinatge primari, però, no hi ha cap senyal. Els sensors que generen l'energia del senyal a partir del mesurand es tracten a la unitat 9.

## 2 Per què reactius i no resistius

La decisió de fer servir un condensador o una bobina com a element transductor, en lloc d'una resistència, respon a quatre avantatges físics concrets.

| Avantatge | Origen físic |
|:--- |:--- |
| **Mesura sense contacte** | Un condensador no necessita contacte físic: n'hi ha prou amb variar la separació entre plaques o la superfície de solapament. Una bobina detecta la proximitat d'un metall a través del camp magnètic. S'eliminen el desgast, la fricció i el soroll elèctric del contacte lliscant d'un potenciòmetre. |
| **Tolerància a la brutícia** | La pols, l'oli i altres substàncies sense resposta davant de camps magnètics no pertorben la mesura inductiva, cosa que fa aquests sensors especialment apreciats en entorns industrials agressius. |
| **Absència de soroll tèrmic** | Un element reactiu ideal no dissipa energia i per tant no genera soroll de Johnson-Nyquist. Qualsevol resistència a temperatura superior al zero absolut sí que en genera. D'aquí una resolució potencial superior, rellevant en metrologia i instrumentació científica. |
| **Absència d'autoescalfament** | Sense dissipació no hi ha escalfament propi, que és un dels errors sistemàtics principals dels sensors resistius. |

Aquests avantatges valen per a l'element **ideal**. El sensor real incorpora resistències, capacitats i inductàncies paràsites que reintrodueixen, atenuats, tant el soroll com la dissipació.

## 3 El cost: cal treballar en alterna

El preu d'utilitzar elements reactius és que la seva impedància **depèn de la freqüència del senyal d'excitació**. En contínua, la impedància d'un condensador ideal és infinita i la d'una inductància ideal és nul·la: en tots dos casos, el valor de la impedància no conté cap informació sobre el mesurand. Cal, doncs, **excitar el sensor amb un senyal sinusoïdal** a una freqüència determinada, que s'anomena **freqüència de treball**  $f_0$
.

En els elements reals el límit és el mateix per una altra via. Una bobina real presenta en contínua la resistència òhmica del seu bobinatge, i és aquesta —no la inductància— la que domina la impedància a freqüència molt baixa; cal pujar en freqüència perquè la reactància inductiva  $\omega L$
 sigui rellevant davant d'aquesta resistència. Un condensador real presenta en contínua la resistència de fuita del seu dielèctric, que tampoc no depèn del mesurand.

> [!WARNING] **Convenció**
>
> Al llarg de la unitat,  $f$
> designa una freqüència genèrica i  $f_0$
> la freqüència de treball escollida per al sistema de mesura. La freqüència angular és  $\omega = 2\pi f$
>.

## 4 La freqüència de treball com a paràmetre de disseny

L'elecció de  $f_0$
 és un dels paràmetres de disseny més rellevants del sistema de mesura, i no es pot decidir mirant només el sensor:

- Si es tria **massa baixa**, la impedància del condensador és molt elevada i el sistema esdevé vulnerable a interferències captades per acoblament capacitiu.
- Si es tria **massa alta**, apareixen pèrdues en el nucli ferromagnètic d'una bobina, pèrdues dielèctriques i efectes de capacitats paràsites que degraden la mesura.

El valor òptim depèn simultàniament del tipus de sensor, del material del nucli o del dielèctric, del mesurand, de les condicions de l'entorn i del **circuit de condicionament**, perquè la freqüència determina alhora la impedància que aquest circuit veu i el pes dels efectes paràsits. El dimensionament complet del condicionador en alterna es tracta a la unitat 8.

## 5 Els quatre mecanismes de transducció de la unitat

| Família | Mecanisme |
|:--- |:--- |
| **Capacitius** | Entre dos conductors separats per un dielèctric s'emmagatzema energia en el camp elèctric. La capacitat depèn de la geometria dels conductors i de la permitivitat del dielèctric; qualsevol magnitud que modifiqui la forma del sensor o la naturalesa del dielèctric és detectable. |
| **Inductius** | Inducció electromagnètica. La inductància d'una bobina es veu modificada per la presència o el moviment de materials conductors o ferromagnètics propers que interaccionen amb el camp que ella mateixa genera. Cas particular: els **corrents de Foucault**, induïts en un conductor massís per un camp magnètic variable. |
| **Efecte Hall** | Portadors de càrrega en moviment que travessen un material prim en presència d'un camp magnètic perpendicular experimenten una força de Lorentz que els desvia i genera una diferència de tensió transversal, proporcional al camp i al corrent. |
| **Magnetostrictius** | Acoblament bidireccional entre l'estat magnètic i la deformació mecànica d'alguns materials ferromagnètics: el material es deforma en presència d'un camp, i una deformació mecànica en modifica la magnetització. |

Els sensors reactius es divideixen, a més, segons quantes bobines o elèctrodes hi intervenen. Els **sensors d'un sol element** mesuren la variació de la pròpia autoinductància o capacitat; els **sensors basats en transformadors variables** —LVDT, resolver, synchro, inductosyn— mesuren la variació de la **inductància mútua** entre bobines separades.

## 6 On es troben aquests sensors

Els acceleròmetres dels telèfons mòbils són majoritàriament dispositius MEMS de principi **capacitiu**, i la pantalla tàctil del mateix telèfon és una matriu de sensors capacitius que detecten la pertorbació del camp elèctric produïda per la proximitat del dit, que és conductor. En l'àmbit industrial, els sensors **inductius** de proximitat, presents a gairebé qualsevol línia d'automatització robòtica, detecten sense contacte si una peça metàl·lica ha arribat a una posició determinada, i les LVDT mesuren en aeronàutica el desplaçament de les superfícies de control amb precisió de micròmetres. Els sensors d'**efecte Hall** són a cada motor elèctric de commutació electrònica, als comptadors d'energia i a les portes dels frigorífics, i els **magnetostrictius** mesuren el nivell de líquids en dipòsits industrials amb resolució de dècimes de mil·límetre, fins i tot a temperatura i pressió extremes.

> [!TIP] **Síntesi**
>
> Un sensor reactiu té com a element sensor un condensador o una bobina, que emmagatzemen energia en un camp elèctric o magnètic en lloc de dissipar-la. D'aquí surten la mesura sense contacte, la tolerància a entorns bruts i l'absència de soroll tèrmic i d'autoescalfament de l'element ideal. El preu és que la impedància depèn de la freqüència: en contínua, la d'un condensador ideal és infinita i la d'una bobina ideal nul·la, de manera que cal excitar el sensor en alterna a una freqüència de treball  $f_0$
> que depèn del sensor, del material, de l'entorn i del condicionador. Tots els sensors de la unitat són moduladors: el mesurand modula un senyal d'excitació extern i no n'aporta l'energia. Els mecanismes són quatre: variació de capacitat, variació d'autoinductància o d'inductància mútua, efecte Hall i magnetostricció.

[2. El sensor capacitiu: model, geometries i linealitat →](#el-sensor-capacitiu-model-geometries-i-linealitat)

<!-- FIN CAPÍTULO: 01_Unitat7_Fonaments_dels_sensors_reactius -->

---

<!-- INICIO CAPÍTULO: 02_Unitat7_El_sensor_capacitiu_model_i_geometries -->

# El sensor capacitiu: model, geometries i linealitat

Sistemes de Mesura · **Unitat 7 — Sensors reactius i electromagnètics** · Document 2 de 6

# El sensor capacitiu: model, geometries i linealitat

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Escriure el model del condensador pla i les condicions en què val.
> - Decidir, per a cada paràmetre variable, si la resposta lineal l'ofereix  $C$
> o el mòdul de la impedància.
> - Relacionar cada variant geomètrica del condensador pla amb la seva funció de mesura.
> - Reconèixer les geometries no planes i quan apareixen com a sensor o com a paràsit.
> - Justificar la tria del dielèctric en sensors de precisió.

## 1 La capacitat com a variable de mesura

Un **sensor capacitiu** és un transductor modulador la resposta del qual consisteix en un canvi de la seva capacitat elèctrica en funció de la magnitud que es vol mesurar. Físicament, un condensador és qualsevol configuració de dos conductors separats per un **dielèctric**: un material que no condueix el corrent en condicions normals però que permet l'existència de camps elèctrics al seu interior. Quan s'aplica una diferència de potencial entre els conductors, s'estableix un camp elèctric al dielèctric i s'acumula càrrega a les seves superfícies. La capacitat és la constant de proporcionalitat entre la càrrega acumulada  $Q$
 i la tensió aplicada  $V$
:

$$
C = \frac{Q}{V} \qquad (7.1)
$$

El valor d'aquesta constant depèn **exclusivament de la geometria** del condensador i de la **permitivitat**  $\varepsilon$
 del dielèctric que separa els conductors. Si qualsevol dels dos factors canvia a causa d'una magnitud física externa —un desplaçament, una pressió, un nivell de líquid, la presència d'un material— la capacitat canvia, i mesurar-la dona informació sobre la magnitud que l'ha causat. La relació entre el mesurand  $x$
 i la capacitat és la **funció de mesura**  $C = g(x)$
.

Aquesta funció **pot ser lineal o no lineal** segons la configuració geomètrica del sensor i el mecanisme pel qual  $x$
 actua sobre el condensador. Un cop mesurada  $C$
, o la impedància associada, s'obté  $x$
 invertint  $g$
. Que  $g$
 sigui lineal és desitjable perquè simplifica el circuit de condicionament i redueix els errors sistemàtics associats a la no linealitat.

## 2 El condensador pla

![Condensador pla: dues plaques conductores paral·leles d'àrea A separades una distància d per un dielèctric de permitivitat epsilon, amb càrregues +Q i −Q](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_1.png)

*Figura: Figura 7.1 El condensador pla.*

La configuració més àmpliament emprada és el **condensador pla**: dues plaques conductores planes, de superfície  $A$
 cadascuna, enfrontades paral·lelament i separades una distància  $d$
, amb un dielèctric de permitivitat  $\varepsilon$
 omplint l'espai entre elles. Sota la hipòtesi que les dimensions laterals de les plaques són molt més grans que la separació,  $d \ll l$
, la capacitat és

$$
C = \frac{\varepsilon A}{d} \qquad (7.2)
$$

La capacitat és, doncs, proporcional a l'àrea i a la permitivitat, i inversament proporcional a la separació. Qualsevol magnitud física que modifiqui  $A$
,  $d$
 o  $\varepsilon$
 modifica la capacitat del sensor, i aquesta sola equació cobreix desplaçaments lineals, girs, nivells de líquid i composicions de mescles.

Per fixar l'escala: unes plaques quadrades d'1 cm de costat  $(A = 10^{-4}\,\mathrm{m^2})$
, separades  $d = 1$
 mm i amb aire com a dielèctric  $(\varepsilon \approx \varepsilon_0 = 8{,}854\times10^{-12}\ \mathrm{F/m})$
, donen aproximadament **0,885 pF**. Els sensors capacitius treballen habitualment amb capacitats de desenes a centenars de picofarads, i en tecnologia MEMS baixen fins a uns pocs femtofarads. Aquest ordre de magnitud tan reduït condiciona tot el disseny del circuit de condicionament.

## 3 Impedància i linealitat

Com que el sensor s'opera en alterna a la freqüència de treball  $f_0$
, la variable que el circuit veu és la impedància. Per a un condensador ideal de capacitat  $C$
:

$$
Z_C = \frac{1}{j\,2\pi f C} \qquad (7.3)
$$

que és purament imaginària, i el seu mòdul, particularitzat per al condensador pla, val

$$
|Z| = \frac{1}{2\pi f C} = \frac{d}{2\pi f \varepsilon A} \qquad (7.4)
$$

El mòdul de la impedància és, per tant, **inversament proporcional al producte de la freqüència i la capacitat**, i a freqüència fixada és lineal amb la separació  $d$
 i inversament proporcional a l'àrea i a la permitivitat. D'aquí surt una asimetria fonamental: **la variable que respon linealment al mesurand no és la mateixa segons quin paràmetre variï**.

| El mesurand modifica… | Capacitat  $C$ | Mòdul  $|Z|$ |
|:--- |:--- |:--- |
| l'àrea  $A$   o la permitivitat  $\varepsilon$ | lineal amb  $x$ | inversament proporcional a  $x$ |
| la separació  $d$ | inversament proporcional a  $x$ | lineal amb  $x$ |

Decidir si el condicionador ha de lliurar una sortida proporcional a  $C$
 o a  $|Z|$
 és, doncs, una decisió de disseny amb conseqüències directes sobre la linealitat del sistema complet, i la resposta depèn de quin paràmetre del condensador varia amb el mesurand.

## 4 Les tres variants del condensador pla

### Àrea de solapament variable

![Condensador pla amb una placa que es desplaça paral·lelament a l'altra, canviant l'àrea de solapament](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_2.png)

*Figura: Figura 7.2 Condensador pla amb àrea variable.*

Una de les plaques es desplaça en direcció **paral·lela** a l'altra, de manera que el solapament passa de  $A_0$
 a  $A(x) = A_0 + \Delta A(x)$
, amb  $\Delta A$
 proporcional a  $x$
:

$$
C(x) = \frac{\varepsilon\,A(x)}{d} \propto x \qquad (7.5)
$$

La capacitat és lineal amb el desplaçament. És la configuració dels sensors d'angle de gir, on el solapament angular entre dues plaques semicirculars varia proporcionalment a l'angle.

### Separació variable

![Condensador pla amb una placa que es desplaça perpendicularment a l'altra, canviant la separació](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_3.png)

*Figura: Figura 7.3 Condensador pla amb distància variable.*

La placa mòbil es desplaça en direcció **perpendicular**. Si la posició d'equilibri és  $d_0$
 i el desplaçament és  $x$
, la separació passa a ser  $d_0 + x$
 i

$$
C(x) = \frac{\varepsilon A}{d_0 + x} \qquad (7.6)
$$

mentre que el mòdul de la impedància val

$$
|Z(x)| = \frac{d_0 + x}{2\pi f \varepsilon A} \propto d_0 + x \qquad (7.7)
$$

El mòdul de la impedància sí que és lineal amb el desplaçament, i és aquesta particularitat la que s'aprofita en sensors de desplaçament i de pressió, on el condicionament es dissenya per obtenir una tensió proporcional a  $|Z|$
.

### Dielèctric variable

![Condensador pla amb dos dielèctrics distribuïts lateralment entre les plaques, un dels quals és aire](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_4.png)

*Figura: Figura 7.4 Condensador pla amb dielèctric variable.*

Dos dielèctrics de permitivitats  $\varepsilon_1$
 i  $\varepsilon_2$
 es distribueixen lateralment entre les plaques i ocupen àrees  $xA$
 i  $(1-x)A$
, amb  $x$
 entre 0 i 1. El sistema es modela com dos condensadors plans en paral·lel:

$$
C(x) = \frac{\varepsilon_1\,xA}{d} + \frac{\varepsilon_2\,(1-x)A}{d} = \frac{A}{d}\left[\varepsilon_2 + (\varepsilon_1-\varepsilon_2)\,x\right] \qquad (7.8)
$$

La capacitat és lineal amb  $x$
 sempre que  $\varepsilon_1 \neq \varepsilon_2$
. És la base dels sensors d'inclinació i de nivell de líquids, on el grau d'ompliment del condensador per part d'un líquid en substitució de l'aire determina el valor de  $x$
.

## 5 Altres geometries

Al costat del condensador pla apareixen geometries que sorgeixen de manera natural en determinades aplicacions, o que s'adopten per adaptar el sensor a una forma constructiva particular. Totes elles serveixen alhora per estimar **capacitats paràsites** del muntatge.

| Geometria | Capacitat | On apareix |
|:--- |:--- |:--- |
| **Dues esferes**<br>radis  $a$   i  $b$, centres separats  $c$ | $C \cong \frac{4\pi\varepsilon}{\frac{a+b}{ab}-\frac{1}{c}}$ | Sensors de proximitat esfèrics; capacitat entre elements conductors arrodonits d'un circuit imprès. |
| **Coaxial**<br>radis  $a$   i  $b$, longitud  $L$ | $C = \frac{2\pi\varepsilon L}{\ln(b/a)}$ | Capacitat entre el conductor viu d'un cable coaxial i la seva malla. Sensors de nivell en tubs coaxials, apreciats per la simetria cilíndrica i la facilitat de neteja. |
| **Dos cables paral·lels**<br>radi  $a$, separació  $d$, longitud  $L$ | $C \cong \frac{\pi\varepsilon}{\ln(d/a)}\,L$ | Cables unifilars que discorren paral·lels, situació habitual entre sensor i condicionador. |
| **Cable sobre pla de massa**<br>radi  $r$, alçada  $h \gg r$, longitud  $L$ | $C = \frac{2\pi\varepsilon L}{\cosh^{-1}(h/r)} \approx \frac{2\pi\varepsilon L}{\ln(2h/r)}$ | Cable no apantallat sobre un pla de massa o una taula metàl·lica. |

![Dues esferes conductores de radis a i b amb els centres separats una distància c](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_5.png)

*Figura: Figura 7.5 Condensador format per dues esferes conductores.*

![Condensador coaxial: conductor intern de radi a envoltat d'un dielèctric i d'un conductor extern de radi b](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_6.png)

*Figura: Figura 7.6 Condensador amb geometria coaxial.*

![Dos conductors cilíndrics paral·lels de radi a amb els centres separats una distància d](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_7.png)

*Figura: Figura 7.7 Condensador format per dos cables cilíndrics paral·lels.*

![Cable cilíndric de radi r situat a una alçada h sobre un pla conductor infinit](assets/02_Unitat7_El_sensor_capacitiu_model_i_geometries_img_8.png)

*Figura: Figura 7.8 Condensador format per un cable cilíndric i un pla de massa infinit.*

## 6 La tria del dielèctric

La immensa majoria de sensors capacitius comercials fan servir com a dielèctric l'**aire** o un **líquid**.

- L'**aire** és el dielèctric per excel·lència en sensors de desplaçament i posició. La seva permitivitat,  $\varepsilon_{\mathrm{aire}} \approx \varepsilon_0$
, és gairebé independent de la temperatura en el rang habitual d'operació, no contamina i no introdueix pèrdues dielèctriques significatives. Aquesta estabilitat és la que dona als sensors capacitius d'aire la seva notable estabilitat tèrmica.
- Els **líquids** s'aprofiten en sensors de nivell: com que la permitivitat del líquid difereix de la de l'aire, la capacitat creix a mesura que el líquid ocupa l'espai entre les plaques.
- Els **sòlids d'alta permitivitat** —ceràmiques, polímers— són habituals en condensadors d'ús general, però en sensors de mesura precisa s'eviten: la seva permitivitat és sensible a la temperatura, la humitat i l'envelliment, i introdueix derives en la mesura.

La tria de la geometria tampoc no és un aspecte menor, perquè condiciona la sensibilitat, la linealitat de la funció de mesura, la facilitat de fabricació i la vulnerabilitat als efectes paràsits. El dissenyador busca simultàniament el màxim canvi de capacitat per unitat de canvi del mesurand, una relació  $C(x)$
 tan lineal com sigui possible dins del rang d'operació, i una geometria prou robusta per fabricar-se de manera reproduïble.

> [!TIP] **Síntesi**
>
> La capacitat relaciona la càrrega acumulada amb la tensió aplicada i depèn només de la geometria i de la permitivitat del dielèctric; la funció de mesura  $C=g(x)$
> pot ser lineal o no segons la configuració. El condensador pla val  $C=\varepsilon A/d$
> quan  $d \ll l$
>, amb capacitats típiques de pF. El mòdul de la impedància és  $\frac{1}{2\pi f C}$
>: si el mesurand modifica l'àrea o la permitivitat, la resposta lineal l'ofereix  $C$
>; si modifica la separació, l'ofereix  $|Z|$
>. Les tres variants del condensador pla —àrea, separació i dielèctric variables— cobreixen la major part de les aplicacions, i les geometries esfèrica, coaxial, de cables paral·lels i de cable sobre pla serveixen tant de sensor com d'estimació de capacitats paràsites. El dielèctric d'elecció en precisió és l'aire, per la seva estabilitat; els sòlids d'alta permitivitat s'eviten perquè deriven amb temperatura, humitat i envelliment.

[← 1. Fonaments dels sensors reactius](#fonaments-dels-sensors-reactius)[3. El sensor capacitiu real: vores, guardes, fuita i freqüència de treball →](#el-sensor-capacitiu-real-vores-guardes-fuita-i-freqüència-de-treball)

---

<!-- FIN CAPÍTULO: 02_Unitat7_El_sensor_capacitiu_model_i_geometries -->

---

<!-- INICIO CAPÍTULO: 03_Unitat7_El_sensor_capacitiu_real -->

# El sensor capacitiu real: vores, guardes, fuita i freqüència de treball

Sistemes de Mesura · **Unitat 7 — Sensors reactius i electromagnètics** · Document 3 de 6

# El sensor capacitiu real: vores, guardes, fuita i freqüència de treball

Dedicació estimada: 12 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Enumerar els avantatges i les limitacions del sensor capacitiu respecte del resistiu.
> - Quantificar l'error de l'efecte de vores i la seva dependència del punt d'operació.
> - Descriure el principi de la guarda de Kelvin i les seves dues configuracions.
> - Escriure el model del condensador amb resistència de fuita i el significat del producte  $R_p C$
>.
> - Justificar la tria de  $f_0$
> a partir de la freqüència de tall i del rang útil d'impedància.

Els models de la secció anterior descriuen el condensador ideal: camp perfectament confinat entre les plaques i dielèctric perfectament aïllant. Els models ideals serveixen per entendre el principi de mesura; el model real hi incorpora les pèrdues i els elements paràsits que fixen les prestacions assolibles i condicionen la tria de la freqüència de treball.

## 1 Avantatges i limitacions

| Avantatge | Fonament |
|:--- |:--- |
| **Estabilitat i reproductibilitat** | La capacitat depèn de magnituds geomètriques i de la permitivitat, de variabilitat molt menor que la resistivitat dels metalls i semiconductors, que depèn de temperatura, microestructura i procés de fabricació. |
| **Baix coeficient tèrmic** | Amb dielèctric d'aire, la permitivitat és pràcticament independent de la temperatura entre −40 °C i +150 °C, davant dels milers de ppm/°C dels materials resistius. Per aquesta mateixa raó els sensors capacitius no s'utilitzen habitualment per mesurar temperatura. |
| **Absència teòrica de soroll** | Un element purament reactiu no dissipa energia i no genera soroll tèrmic. A la pràctica hi ha una resistència paràsita en paral·lel que en genera, però molt menor que el d'una resistència equivalent. |
| **Absència d'autoescalfament** | El sensor capacitiu ideal no dissipa potència i per tant no s'escalfa. |
| **Facilitat de miniaturització** | La capacitat entre conductors plans s'obté en els processos de fabricació de circuits integrats. La tecnologia **MEMS** permet separacions de l'ordre del micròmetre i àrees de mm², amb capacitats d'uns pocs fF a uns centenars de fF reproduïdes amb gran precisió per fotolitografia: acceleròmetres, giroscopis, micròfons i sensors de pressió en silici. |

| Limitació | Efecte |
|:--- |:--- |
| **Efecte de vores** | La capacitat real supera la que prediu  $C = \varepsilon A/d$, amb un error que depèn del punt d'operació. |
| **Resistència de fuita del dielèctric** | Cap dielèctric és perfectament aïllant: apareixen soroll tèrmic i autoescalfament residuals. |
| **Capacitats molt petites** | Amb capacitats de pF o inferiors, qualsevol paràsita en paral·lel —cables, connectors, traces del circuit imprès— s'hi suma directament i pot ser del mateix ordre de magnitud, cosa que introdueix errors sistemàtics a corregir per calibratge. A més no són estables: un cable que es mou, una dilatació del circuit imprès o gotes d'humitat les alteren i produeixen deriva sense que hagi canviat el mesurand. |
| **Alta impedància a baixa freqüència** | Amb capacitats de pF,  $|Z|$   pot arribar a MΩ o GΩ, i un sistema d'alta impedància capta amb facilitat interferències per acoblament capacitiu —la xarxa a 50 Hz, per exemple— que s'injecten a través de les paràsites i emmascaren el senyal. |
| **Necessitat d'apantallament** | Els punts anteriors convergeixen en un disseny acurat del blindatge: pantalla connectada a un potencial de referència estable i condicionador físicament proper al sensor per limitar la longitud de cable i, per tant, les paràsites. |

## 2 L'efecte de vores

L'expressió  $C = \varepsilon A/d$
 s'obté suposant que les línies de camp parteixen perpendicularment d'una placa i arriben perpendicularment a l'altra sense escapar-se del volum que delimiten, hipòtesi que correspon a un condensador de dimensions infinites. En un condensador real, de dimensions finites, les línies que neixen prop dels extrems no resten confinades: és l'**efecte de vores**, i les línies que el manifesten són les **línies de camp de vora**.

L'energia emmagatzemada en aquest camp exterior es reflecteix en capacitat addicional, de manera que la **capacitat real supera** la ideal. L'efecte és tant menys rellevant com més petita és la separació respecte de les dimensions laterals: la condició d'aplicabilitat de la fórmula ideal és  $d \ll l$
, on  $l$
 és la dimensió lateral característica —el costat menor en plaques rectangulars, el diàmetre en plaques circulars.

Per a plaques quadrades de costat  $l$
 i separació  $d$
, amb dielèctric d'aire, Bromwich va demostrar el 1902 que l'error relatiu respecte del valor ideal s'aproxima per

$$
\epsilon_r \approx \frac{d}{\pi l}\left(1 + \ln\frac{2\pi l}{d}\right)\cdot 100\,\% \qquad (7.9)
$$

| Separació  $d$ | $d/l$ | Error  $\epsilon_r$ |
|:--- |:--- |:--- |
| 0,1 mm | 0,01 | ≈ 2,4 % |
| 1 mm | 0,1 | ≈ 16 % |

Una relació separació/costat de només 1/10 ja comporta un error del 16 %. En sensors de desplaçament que operen amb separacions d'entre uns centenars de micròmetres i uns pocs mil·límetres, amb plaques de mida centimètrica, l'error de vores no es pot ignorar en aplicacions de precisió.

L'aspecte especialment problemàtic per a un sensor és que **l'error depèn del punt d'operació**. Com que la separació varia amb el mesurand, l'error de vores hi varia també, i introdueix una **no linealitat addicional** que el model  $C = \varepsilon A/d$
 no recull.

## 3 Les guardes de Kelvin

Quan es requereix elevada exactitud, la primera opció és el **modelat numèric** per elements finits (MEF, o FEM en anglès): la capacitat calculada per simulació incorpora automàticament l'efecte de vores, i comparar-la amb el valor ideal permet establir funcions de correcció. Té límits pràctics, però: exigeix un model geomètric precís, té cost computacional i dona una correcció lligada a la geometria de cada exemplar, poc generalitzable.

Per això la solució preferida és la **guarda de Kelvin**, que elimina l'efecte de vores **físicament** en lloc de corregir-lo a posteriori. La idea, atribuïda a Lord Kelvin (William Thomson, 1824–1907), consisteix a afegir al perímetre de la placa un conductor auxiliar —la guarda— mantingut **exactament al mateix potencial** que la placa sensora.

![Guarda de Kelvin: a dalt, tall del condensador amb la placa sensora Cs envoltada per la guarda separada per una ranura g; a baix, implementació en plaques circulars](assets/03_Unitat7_El_sensor_capacitiu_real_img_1.png)

*Figura: Figura 7.9 Guarda de Kelvin a una cara del condensador. La figura superior mostra un tall amb les variables geomètriques i elèctriques; la inferior, la implementació en un condensador de plaques circulars.*

El principi físic és la **condició de contorn de Dirichlet**: si el conductor perifèric està al mateix potencial que el sensor, no hi ha diferència de potencial entre tots dos i per tant no hi ha camp elèctric a la zona de separació. Les línies que apunten cap a la perifèria no troben cap canvi de potencial en creuar la frontera, de manera que les de la zona central resten rectilínies i la capacitat  $C_s$
 és la d'un condensador pla ideal, sempre que la guarda sigui prou ampla.

A la pràctica, la guarda s'implementa tallant la placa conductora en una zona interior —el sensor  $C_s$
— i una d'exterior —la guarda—, separades per una **ranura molt estreta**: tots dos conductors al mateix pla però elèctricament separats, amb una connexió que mantingui la guarda al potencial de la placa interior en tot moment. Es distingeixen dues configuracions:

- **Guarda en una cara**: la placa superior és el sensor envoltat per la guarda i la inferior és solidària, connectada a massa o al terminal baix del circuit. Les vores de la placa inferior actuen elles mateixes com a guarda per als camps que fugen cap avall.
- **Guarda en les dues cares**: totes dues plaques es divideixen en zona interior i zona perifèrica. Dona el millor confinament de les línies de camp i la menor contribució de vores, a canvi de més complexitat constructiva.

L'error residual d'una guarda ben dissenyada pot fer-se inferior al **0,01 %** si la seva amplada supera dues o tres vegades la separació  $g$
 entre plaques, cosa que la converteix en la solució estàndard en ponts de capacitat de laboratori, sensors de desplaçament nanomètrics i sensors capacitius MEMS d'alta resolució.

## 4 La resistència de fuita del dielèctric

Qualsevol material dielèctric real posseeix una **conductivitat residual**  $\sigma$
, per petita que sigui. Fins i tot l'aire sec en té, a causa dels ions produïts per la radiació còsmica i la radioactivitat natural; els dielèctrics sòlids emprats en suports i encapsulats —poliimides, PTFE, PEEK— presenten conductivitats de l'ordre de  $10^{-16}$
 a  $10^{-12}$
 S/m.

![Model del condensador real: capacitat C en paral·lel amb una resistència paràsita Rp que representa la fuita del dielèctric](assets/03_Unitat7_El_sensor_capacitiu_real_img_2.png)

*Figura: Figura 7.10 Model del condensador incorporant la resistència del dielèctric.*

Aquesta conductivitat fa circular entre les plaques un **corrent de fuita** proporcional a la tensió aplicada, de manera que el sensor no es comporta com una capacitat pura sinó com la combinació **en paral·lel** d'una capacitat  $C$
 i una **resistència de fuita**  $R_p$
. Per a un condensador pla,

$$
R_p = \frac{\rho\,d}{A} = \frac{d}{\sigma A} \qquad (7.10)
$$

El corrent de fuita travessa el dielèctric igual que travessaria un material conductor de les mateixes dimensions. Una conseqüència notable és que  $R_p$
 varia **conjuntament** amb  $C$
: si el mesurand modifica la separació, la capacitat disminueix quan  $d$
 augmenta però la resistència de fuita augmenta en la mateixa proporció, de manera que el producte és independent de la geometria:

$$
R_p \cdot C = \frac{d}{\sigma A}\cdot\frac{\varepsilon A}{d} = \frac{\varepsilon}{\sigma} \qquad (7.11)
$$

Aquest producte és la **constant de temps dielèctrica** del material, que depèn únicament de les **propietats del dielèctric**. Si  $C$
 és petita,  $R_p$
 és gran, i a l'inrevés.

La impedància del conjunt paral·lel i el seu mòdul valen

$$
Z = \frac{R_p\cdot\frac{1}{j\omega C}}{R_p+\frac{1}{j\omega C}} = \frac{R_p}{1+j\omega R_p C} \qquad (7.12)
$$

$$
|Z| = \frac{R_p}{\sqrt{1+(2\pi f R_p C)^2}} \qquad (7.13)
$$

## 5 La tria de la freqüència de treball

Per extreure informació sobre  $C$
, i per tant sobre el mesurand, cal que la impedància del sensor estigui dominada per la part capacitiva. La condició és que la reactància del condensador sigui molt menor que la resistència de fuita,  $\frac{1}{\omega_0 C} \ll R_p$
, cosa que situa la freqüència de treball ben per damunt de la **freqüència de tall**

$$
f_{-3\mathrm{dB}} = \frac{1}{2\pi R_p C} = \frac{\sigma}{2\pi\varepsilon} \qquad (7.14)
$$

Per a dielèctrics de qualitat com l'aire o el PTFE,  $\sigma$
 és tan petita que aquesta freqüència pot ser de l'ordre de mHz o μHz, de manera que qualsevol freqüència de treball pràctica hi queda ben per damunt i la hipòtesi d'impedància capacitiva és excel·lent.

![Diagrama de Bode del mòdul de la impedància del sensor: pla i igual a Rp per sota de f-3dB, decreixent 20 dB per dècada per sobre, amb la regió de treball indicada](assets/03_Unitat7_El_sensor_capacitiu_real_img_3.png)

*Figura: Figura 7.11 Mòdul de la impedància del sensor en funció de la freqüència.*

El diagrama de Bode del model paral·lel resumeix els dos règims. Per a  $f \ll f_{-3\mathrm{dB}}$
 la impedància és pràcticament resistiva i  $|Z| \approx R_p$
, independent de la freqüència. Per a  $f \gg f_{-3\mathrm{dB}}$
 és pràcticament capacitiva,  $|Z| \approx \frac{1}{2\pi f C}$
, i decreix amb pendent de −20 dB/dècada. Això explica físicament per què no es pot mesurar un sensor capacitiu en contínua: a freqüència zero la impedància és simplement  $R_p$
, que no informa de la capacitat ni, per tant, del mesurand.

Superar  $f_{-3\mathrm{dB}}$
 no és, però, l'únic criteri. Cal també que el mòdul de la impedància tingui un valor manejable per al circuit de condicionament: si  $f_0$
 és massa baixa,  $|Z|$
 arriba a centenars de MΩ o a GΩ i el sistema és molt sensible a interferències; si és massa alta, apareixen efectes inductius paràsits, pèrdues dielèctriques que creixen amb la freqüència i limitacions del propi condicionador. A la pràctica s'escull  $f_0$
 de manera que

$$
100\ \Omega \lesssim |Z(f_0)| \lesssim 1\ \mathrm{M\Omega} \qquad (7.15)
$$

Per a un sensor de 100 pF, aquest rang correspon a freqüències de treball compreses entre uns **1,6 kHz i 16 MHz**. La zona de treball òptima és, doncs, la que queda alhora ben per damunt de  $f_{-3\mathrm{dB}}$
 i dins d'aquest rang d'impedància.

## 6 Conseqüències per al condicionador

La resistència de fuita és responsable dels dos efectes indesitjats ja anticipats. El **soroll tèrmic** podria semblar enorme perquè  $R_p$
 és molt gran (MΩ a GΩ), però queda filtrat per la impedància total del circuit i per una amplada de banda equivalent de soroll proporcional a  $f_{-3\mathrm{dB}}$
; com que  $R_p C = \varepsilon/\sigma$
, el soroll integrat depèn només de les propietats del dielèctric i no de la geometria, de manera que un  $\sigma$
 molt baix dona un soroll molt reduït. L'**autoescalfament residual** prové de la potència dissipada a  $R_p$
 per la tensió d'excitació i, atesa la magnitud de  $R_p$
, és pràcticament inapreciable.

D'aquí surten els requisits del circuit de condicionament, que es desenvolupen a la unitat 8: generar l'excitació sinusoïdal a la freqüència escollida, mesurar la variació de capacitat o de mòdul d'impedància com a canvi d'amplitud o de fase, presentar una impedància d'entrada prou alta per no carregar el sensor i incorporar blindatge actiu per minimitzar les capacitats paràsites del cable.

> [!TIP] **Síntesi**
>
> El sensor capacitiu aporta estabilitat, baix coeficient tèrmic, absència teòrica de soroll i d'autoescalfament i facilitat de miniaturització, i exigeix a canvi gestionar l'efecte de vores, la resistència de fuita, les capacitats paràsites i l'apantallament. L'efecte de vores fa que la capacitat real superi la ideal, amb un error que creix amb  $d/l$
> —del 2,4 % al 16 % en passar de 0,01 a 0,1— i que varia amb el punt d'operació quan el mesurand modifica la separació. Es corregeix per elements finits o, preferiblement, s'elimina amb una guarda de Kelvin al mateix potencial que la placa sensora. El dielèctric real afegeix una resistència de fuita en paral·lel, amb  $R_p = d/(\sigma A)$
> i  $R_p C = \varepsilon/\sigma$
>, que fixa la freqüència de tall  $f_{-3\mathrm{dB}} = \sigma/(2\pi\varepsilon)$
>. La freqüència de treball s'ha de situar ben per damunt d'aquesta i mantenir alhora el mòdul de la impedància entre uns 100 Ω i 1 MΩ.

[← 2. El sensor capacitiu: model, geometries i linealitat](#el-sensor-capacitiu-model-geometries-i-linealitat)[4. Aplicacions dels sensors capacitius i el condensador diferencial →](#aplicacions-dels-sensors-capacitius-i-el-condensador-diferencial)

---

<!-- FIN CAPÍTULO: 03_Unitat7_El_sensor_capacitiu_real -->

---

<!-- INICIO CAPÍTULO: 04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial -->

# Aplicacions dels sensors capacitius i el condensador diferencial

Sistemes de Mesura · **Unitat 7 — Sensors reactius i electromagnètics** · Document 4 de 6

# Aplicacions dels sensors capacitius i el condensador diferencial

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Relacionar cada aplicació capacitiva amb el paràmetre del condensador que hi varia.
> - Reconèixer l'element elàstic com a etapa intermèdia en la mesura de força i de pressió.
> - Escriure el model del condensador diferencial i la seva diferència normalitzada.
> - Enumerar els tres avantatges del principi diferencial.

## 1 Distància, desplaçament i presència

![Sensors capacitius de distància i desplaçament: configuracions amb separació variable i amb solapament variable](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_1.png)

*Figura: Figura 7.12 Sensors capacitius per a la mesura de distància i desplaçament.*

És l'aplicació més directa. Un condensador pla amb una placa mòbil respon a qualsevol desplaçament perpendicular a les plaques, que modifica  $d$
, o paral·lel a elles, que modifica el solapament i per tant  $A$
. Aquests sensors assoleixen resolucions de l'ordre del **nanòmetre** en rangs de micròmetres a mil·límetres, i s'utilitzen en màquines de mesura per coordenades i en instruments de nanolitografia.

![Detector de presència capacitiu: un objecte conductor o dielèctric pertorba el camp elèctric que envolta l'elèctrode sensor](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_2.png)

*Figura: Figura 7.13 Detector de presència capacitiu.*

La **detecció de presència** s'explota d'una manera diferent: en lloc de mesurar un canvi geomètric del sensor, es detecta la **pertorbació** que un objecte conductor o dielèctric provoca en el camp elèctric que l'envolta. Quan un dit s'apropa a una pantalla tàctil, altera la distribució del camp en la matriu de condensadors que la forma, i el circuit de detecció identifica quins elements de la matriu han vist modificada la capacitat. És la base de totes les pantalles tàctils capacitives actuals.

## 2 Força i pressió

El principi de transducció més emprat consisteix a convertir la magnitud mecànica en un **desplaçament** mitjançant un element elàstic —un ressort, una membrana, una biga en voladís— i detectar aquest desplaçament amb un sensor capacitiu. En sensors de pressió, una membrana fina de silici o d'acer inoxidable es deforma sota la pressió i la seva posició es monitora per la variació de capacitat entre la membrana i un elèctrode fix pròxim.

Els sensors de pressió capacitius assoleixen resolucions de l'ordre del pascal en rangs de fins a centenars de kPa, i s'usen en baròmetres d'alta precisió, sensors industrials i mesuradors de buit. La seva resolució i estabilitat tèrmica els fan preferibles a la galga extensomètrica quan les especificacions de soroll i de deriva són exigents.

![Microestructura planar per a mesura de força: marc superior fix, massa mòbil central suspesa per quatre molles i marc inferior fix, amb elèctrodes que formen dos condensadors](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_3.png)

*Figura: Figura 7.14 Mesura de força fent servir un condensador diferencial.*

La microestructura planar de la figura té una **massa mòbil central** (2) suspesa per quatre suspensions elàstiques entre dos marcs rígids ancorats al substrat, el superior (1) i l'inferior (3), que serveixen de referència mecànica. Quan la força de pinça  $F_c$
 desplaça la massa una distància  $\delta$
, la separació entre (2) i (1) disminueix en  $\delta$
 i la separació entre (2) i (3) augmenta en la mateixa quantitat. La lectura genera una tensió proporcional a  $C_1 - C_2$
, i per tant a  $\delta$
 i, en règim lineal de la suspensió, a la força.

![Sensor de pressió amb condensador únic: diafragma sensor, placa rígida, diafragma d'aïllament i oli de silicona](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_4.png)

*Figura: Figura 7.15 Mesura de pressió amb condensador variable.*

![Secció d'un sensor de pressió diferencial: diafragma sensor central banyat en oli de silicona amb una placa rígida a cada costat formant C1 i C2](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_5.png)

*Figura: Figura 7.16 Mesura de pressió amb condensador diferencial.*

En el sensor de pressió de condensador únic, el fluid actua pel port superior sobre el **diafragma sensor**, que és un dels elèctrodes: en augmentar la pressió el diafragma s'allunya de la placa rígida i la capacitat disminueix. La versió diferencial situa una **placa rígida a cada costat** del diafragma, de manera que quan la pressió diferencial el deflecta,  $C_1$
 augmenta i  $C_2$
 disminueix. En tots dos casos, l'oli de silicona que omple la cambra actua alhora de transmissor hidrostàtic de la pressió i de protecció mecànica del diafragma davant de fluids agressius i de sobrepressió.

## 3 Angle, nivell i inclinació

![Mesura d'angle: placa en forma d'arc de cercle solidària a l'eix mòbil enfrontada a una placa fixa](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_6.png)

*Figura: Figura 7.17 Mesura d'angle amb condensador variable.*

En sensors de posició angular, una placa en forma d'arc de cercle és solidària a l'eix mòbil i l'altra resta fixa. A mesura que l'eix gira, l'àrea de solapament canvia proporcionalment a l'angle i la capacitat hi varia linealment.

![Mesura de nivell: plaques verticals introduïdes en un dipòsit, amb el líquid substituint l'aire entre elles a mesura que puja](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_7.png)

*Figura: Figura 7.18 Mesura de nivell amb condensador variable.*

Els sensors de nivell aprofiten la diferència de permitivitat entre el líquid  $(\varepsilon_l \gg \varepsilon_0$
 per a la majoria de líquids polars $)$
 i l'aire. A mesura que el nivell puja, el líquid ocupa progressivament l'espai entre les plaques i la capacitat creix proporcionalment al nivell:

$$
C(h) = C_{\mathrm{aire}} + \left(C_{\mathrm{líquid}} - C_{\mathrm{aire}}\right)\cdot\frac{h}{H} \qquad (7.16)
$$

on  $H$
 és l'alçada total del sensor. La geometria coaxial és molt emprada aquí per la seva simetria cilíndrica i la seva facilitat de neteja. S'utilitzen en indústria química, farmacèutica i alimentària, fins i tot a pressions i temperatures elevades on altres tecnologies resulten impracticables.

![Sensor d'inclinació amb condensador diferencial: tub parcialment ple de líquid amb dos parells d'elèctrodes](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_8.png)

*Figura: Figura 7.19 Mesura d'inclinació amb condensador diferencial.*

Els sensors d'**inclinació** aprofiten el desplaçament d'una bombolla d'aire en un tub parcialment ple de líquid, o el moviment d'una massa de mercuri o d'un electròlit entre elèctrodes. Sense inclinació, totes dues capacitats són iguals; amb inclinació positiva, el condensador de la dreta augmenta perquè té més nivell de líquid i el de l'esquerra disminueix, i amb inclinació negativa el canvi és l'oposat.

## 4 Acceleració: els acceleròmetres MEMS

![Acceleròmetre capacitiu MEMS: massa inercial suspesa per bigues elàstiques amb elèctrodes mòbils enfrontats a elèctrodes fixos del substrat](assets/04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial_img_9.png)

*Figura: Figura 7.20 Mesura d'acceleració amb condensador diferencial.*

El principi s'inspira en la llei de Newton: una massa inercial suspesa per una estructura elàstica —bigues o ressorts en voladís de silici monocristal·lí— es deforma proporcionalment a l'acceleració, i la deformació es tradueix en un canvi de separació o de solapament entre els elèctrodes solidaris a la massa i els elèctrodes fixos del substrat. Un acceleròmetre MEMS típic conté **milers de dents interdigitades**, cadascuna un petit condensador pla entre la pinta mòbil i la fixa: quan la massa es desplaça, totes les capacitats varien alhora i la suma porta la sensibilitat a valors pràctics, de l'ordre de **pF/g**, amb resolucions de fins a μg i rangs de ±2 g en telèfons mòbils a ±200 g en automoció i airbags.

## 5 El condensador diferencial

En moltes de les aplicacions anteriors el sensor no és un condensador únic sinó una **parella** en configuració diferencial: quan el mesurand incrementa la capacitat d'un en una quantitat  $\Delta C$
, disminueix la de l'altre en la mateixa quantitat.

$$
C_1(x) = C_0 + \Delta C(x)\;\qquad C_2(x) = C_0 - \Delta C(x) \qquad (7.17)
$$

on  $C_0$
 és la capacitat de repòs. La diferència  $C_1 - C_2 = 2\Delta C(x)$
 és el doble de sensible que un condensador únic, i la suma  $C_1 + C_2 = 2C_0$
 és idealment constant i independent de  $x$
. Això permet condicionaments que exploten el **quocient diferencial normalitzat**

$$
\frac{C_1-C_2}{C_1+C_2} = \frac{\Delta C}{C_0} \qquad (7.18)
$$

que és lineal amb  $x$
 i independent de les derives de  $C_0$
 amb la temperatura. Els avantatges del principi diferencial són tres:

| Avantatge | Mecanisme |
|:--- |:--- |
| **Sensibilitat doble** | Per al mateix rang de mesura, la variació de la sortida diferencial és el doble de la de qualsevol dels dos condensadors per separat. |
| **Rebuig de mode comú** | Qualsevol pertorbació que afecti igual els dos condensadors —una variació de temperatura, una interferència electromagnètica, un canvi de geometria per desgast— s'elimina en fer la diferència. |
| **Linealitat millorada** | Un sol condensador de separació variable respon com  $C = \varepsilon A/(d_0+x)$. La combinació de dos condensadors, un amb  $d_0+x$   i l'altre amb  $d_0-x$, muntats en un divisor de tensió, dona una resposta diferencial que en primera aproximació sí que és lineal amb  $x$   per a desplaçaments petits respecte de  $d_0$. El desenvolupament d'aquests condicionadors es fa a la unitat 8. |

La compensació és, però, la que permet la simetria constructiva assolida: en un sensor real les dues branques no són idènticament iguals i el calibratge continua essent necessari.

Per aquestes raons, els acceleròmetres capacitius MEMS, els sensors de pressió diferencial, els sensors de posició d'alta precisió i una gran varietat d'instruments de laboratori fan del principi diferencial l'element central del seu disseny.

> [!TIP] **Síntesi**
>
> Les aplicacions capacitives es classifiquen segons el paràmetre que hi varia: la separació o el solapament en distància, desplaçament i angle; la permitivitat efectiva en nivell i inclinació; i la pertorbació del camp exterior en detecció de presència. Força i pressió es mesuren convertint-les primer en desplaçament amb un element elàstic —membrana, ressort o biga en voladís—, i l'acceleració amb una massa inercial suspesa, en acceleròmetres MEMS de milers de dents interdigitades i sensibilitat de l'ordre de pF/g. Moltes d'aquestes aplicacions adopten el condensador diferencial, amb  $C_1 = C_0+\Delta C$
> i  $C_2 = C_0-\Delta C$
>, que duplica la sensibilitat, rebutja les pertorbacions comunes a les dues branques i millora la linealitat mitjançant la diferència normalitzada  $\Delta C/C_0$
>.

[← 3. El sensor capacitiu real: vores, guardes, fuita i freqüència de treball](#el-sensor-capacitiu-real-vores-guardes-fuita-i-freqüència-de-treball)[5. Sensors inductius i corrents de Foucault →](#sensors-inductius-i-corrents-de-foucault)

---

<!-- FIN CAPÍTULO: 04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial -->

---

<!-- INICIO CAPÍTULO: 05_Unitat7_Sensors_inductius_i_corrents_de_Foucault -->

# Sensors inductius i corrents de Foucault

Sistemes de Mesura · **Unitat 7 — Sensors reactius i electromagnètics** · Document 5 de 6

# Sensors inductius i corrents de Foucault

Dedicació estimada: 15 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Escriure el model de la inductància d'una bobina i identificar què hi pot fer variar el mesurand.
> - Relacionar reluctància, entreferro i inductància.
> - Distingir el mecanisme dels materials ferromagnètics del dels conductors no ferromagnètics.
> - Contrastar bobina d'aire i bobina amb nucli ferromagnètic com a decisió de disseny.
> - Explicar l'origen dels corrents de Foucault, l'efecte pell i les seves dues aplicacions.

## 1 L'autoinductància

Un **sensor inductiu** és un transductor modulador la resposta del qual consisteix en un canvi de la seva autoinductància, o de la seva inductància mútua amb una altra bobina, en funció de la magnitud que es vol mesurar.

Quan un corrent circula per un conductor enrotllat en bobina, genera un camp magnètic proporcional al corrent. Part d'aquest camp travessa els propis enrotllaments i genera un flux concatenat  $\Phi$
. Per la llei de Faraday, una variació temporal d'aquest flux indueix a la pròpia bobina una força electromotriu que s'oposa a la variació que l'ha causada, que és la llei de Lenz. L'**autoinductància** és la constant de proporcionalitat entre el flux concatenat i el corrent que el genera:

$$
L = \frac{N\Phi}{I} \qquad (7.19)
$$

on  $N$
 és el nombre total de voltes. En aplicacions de sensors, els valors típics es troben entre μH i mH.

![Solenoide: bobinat cilíndric de longitud l i secció transversal A al voltant d'un nucli](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_1.png)

*Figura: Figura 7.21 Solenoide.*

Per a una geometria senzilla com el solenoide, la inductància s'estima com

$$
L = \mu_0\,\mu_r\,n^2\,F_c\,F_g \qquad (7.20)
$$

| Paràmetre | Significat |
|:--- |:--- |
| $\mu_0$ | Permeabilitat magnètica del buit,  $4\pi\times10^{-7}$   T·m/A. |
| $\mu_r$ | Permeabilitat relativa del nucli, adimensional: quantes vegades el material és més permeable al flux que el buit. Val aproximadament 1 per a l'aire i la majoria de materials no magnètics, i de centenars a centenars de milers en ferromagnètics —ferro dolç, ferrites, permalloy. |
| $n$ | Densitat d'enrotllament, en voltes per metre:  $n = N/l$. |
| $F_c$ | Factor de correcció de pèrdues del nucli, per histèresi i per corrents de Foucault. Val 1 en una bobina sense nucli; en nuclis ferromagnètics reals és inferior a 1 i depèn del corrent. |
| $F_g$ | Factor geomètric, que recull la forma del nucli —cilíndric, toroïdal, en U. Per a un solenoide ideal de longitud  $l$   i secció  $A$   val  $F_g = l\cdot A$, el volum de la bobina. |

## 2 Reluctància i entreferro

Una manera equivalent i sovint més còmoda de raonar sobre aquests sensors és mitjançant la **reluctància magnètica**  $\mathcal{R}$
, l'oposició que un camí magnètic ofereix a l'establiment del flux. Per a un tram de longitud  $l$
 i secció  $A$
 de material de permeabilitat  $\mu_0\mu_r$
:

$$
\mathcal{R} = \frac{l}{\mu_0\mu_r A}\;\qquad L = \frac{N^2}{\mathcal{R}} \qquad (7.21)
$$

La inductància és, doncs, **inversament proporcional a la reluctància** del camí magnètic. Un material ferromagnètic que completi el camí de flux hi aporta una permeabilitat elevada i, per tant, **redueix** la reluctància i augmenta la inductància. Els trams d'aire del camí —els **entreferros**— tenen  $\mu_r \approx 1$
 i dominen la reluctància total encara que siguin curts, de manera que qualsevol mesurand que en modifiqui la longitud produeix un canvi gran de la inductància. Aquest és el mecanisme de la major part dels sensors inductius de desplaçament, força i pressió.

## 3 Què fa variar la inductància

- **Canvis geomètrics**: qualsevol desplaçament o deformació que modifiqui la longitud, la secció o el factor geomètric altera la inductància, cosa que permet mesurar desplaçaments, pressions, forces i girs.
- **Canvis del nombre de voltes**: si part del bobinatge es connecta o desconnecta mecànicament,  $n$
   i per tant  $L$
   canvien. Implementació poc habitual, possible en sensors de posició de llarg recorregut.
- **Canvis de permeabilitat del camí**: un material ferromagnètic o conductor a prop de la bobina redistribueix el flux i modifica la inductància efectiva. És la base dels sensors de proximitat i distància sense contacte.

El mecanisme de la distorsió depèn del **tipus de material** objectiu:

| Material proper | Mecanisme i efecte sobre  $L$ |
|:--- |:--- |
| **Ferromagnètic** | Les línies de camp tendeixen a concentrar-se en el material, cosa que modifica el flux concatenat i **augmenta** la inductància efectiva. La magnitud del canvi depèn de la permeabilitat, de la geometria i de la distància. |
| **Conductor no ferromagnètic**<br>(alumini, coure, acer austenític) | Domina la generació de **corrents de Foucault**, que creen un camp contrari al de la bobina i **redueixen** el flux net concatenat i, per tant, la inductància efectiva. |

En tots dos casos la variació d'inductància és funció de la distància entre la bobina i l'objecte, cosa que permet construir sensors de distància o proximitat **sense cap contacte mecànic**.

## 4 Inductància mútua i necessitat d'excitació alterna

Quan dues bobines són prou properes, part del flux generat per la **primària** travessa les voltes de la **secundària** i hi indueix una tensió. La constant de proporcionalitat entre el flux que el primari crea al secundari i el corrent que hi circula és la **inductància mútua**  $M$
, i la tensió induïda val

$$
V_s = j\omega M I_p = j\omega M\,\frac{V_p}{j\omega L_p} = \frac{M}{L_p}\,V_p \qquad (7.22)
$$

Si la posició relativa entre primari i secundari varia —perquè un nucli ferromagnètic mòbil redistribueix el flux entre tots dos—,  $M$
 canvia i amb ella la tensió induïda. Aquest és el principi de la LVDT, el resolver, el synchro i l'inductosyn, que es tracten al document següent.

Els sensors inductius comparteixen amb els capacitius la impossibilitat de mesurar-se en contínua: la impedància d'una inductància ideal en contínua és nul·la i la bobina és simplement un curtcircuit. Cal excitar-la a una freqüència de treball tal que la **reactància inductiva**

$$
X_L = \omega L = 2\pi f_0 L \qquad (7.23)
$$

tingui un valor mesurable. En una bobina real la impedància en contínua és la resistència del bobinatge  $R_{\mathrm{bob}}$
, modelada en sèrie amb l'autoinductància, i cal pujar en freqüència perquè  $\omega L$
 sigui rellevant davant seu. Aquesta mateixa resistència sèrie és l'única font de soroll tèrmic del sensor inductiu real, ja que la inductància ideal no en genera.

Els sensors inductius s'agrupen, per tant, en dues famílies: els **basats en una sola bobina**, en què es mesura la variació de l'autoinductància —sensors de proximitat estàndard i sensors de corrents de Foucault—, i els **basats en transformadors variables**, en què es mesura la variació de la inductància mútua.

## 5 Objectiu metàl·lic: limitació i fortalesa

El principi de funcionament requereix que l'objecte a detectar sigui **metàl·lic**: els materials no metàl·lics —plàstics, gomes, vidre, fustes, ceràmiques seques, líquids no conductors— no pertorben de manera apreciable el camp de la bobina. La limitació és, paradoxalment, una de les fortaleses del sensor en entorns industrials, perquè permet discriminar amb fiabilitat entre objectes metàl·lics i no metàl·lics i fa que pols, oli, aigua, fang, vibracions i vapors químics no afectin la resposta.

La resposta, però, **no és idèntica per a tots els metalls**: la magnitud i el caràcter de la pertorbació depenen de la conductivitat i de la permeabilitat del material objectiu i de la freqüència de treball. Un sensor calibrat per a ferro dolç dona lectures diferents davant d'alumini; en alta precisió cal especificar el material objectiu i calibrar-hi el sensor.

## 6 La tria del nucli i del conductor

|  | Bobina d'aire  $(\mu_r\approx 1)$ | Nucli ferromagnètic  $(\mu_r\gg 1)$ |
|:--- |:--- |:--- |
| **Sensibilitat** | Menor: el flux és molt inferior per al mateix corrent i nombre de voltes, i cal augmentar voltes o excitació. | Major:  $L \propto \mu_r$, de  $10^3$   a  $10^5$, amb molta més variació de  $L$   per unitat de desplaçament a igualtat de dimensions. |
| **Linealitat** | Resposta reversible i lineal en un ampli rang de corrents: sense nucli ferromagnètic no hi ha histèresi magnètica. | La permeabilitat depèn del camp aplicat i presenta histèresi, cosa que introdueix no linealitats i deriva. |
| **Freqüència útil** | Sense pèrdues de nucli, s'excita a diversos MHz sense degradació apreciable. | Les pèrdues per corrents de Foucault al nucli creixen amb el quadrat de la freqüència: per damunt d'uns kHz —i d'uns 20 kHz en nuclis de ferro— dominen, la inductància efectiva cau i el factor de qualitat es degrada. Per a freqüències altes s'usen **ferrites**, ferromagnètics ceràmics de conductivitat molt menor, que permeten treballar fins a centenars de kHz o alguns MHz. |

El conductor del bobinatge sol ser **coure**, per la seva resistivitat molt baixa  $(\rho_{\mathrm{Cu}} \approx 1{,}7\times10^{-8}\ \Omega\cdot\mathrm{m})$
, que minimitza  $R_{\mathrm{bob}}$
 i, amb ella, el soroll i l'autoescalfament. Quan el pes és crític —instruments aeroespacials, sensors embarcats— es prefereix l'**alumini**, unes tres vegades menys dens, a canvi d'una resistivitat superior  $(\rho_{\mathrm{Al}} \approx 2{,}7\times10^{-8}\ \Omega\cdot\mathrm{m})$
 i, per tant, de més soroll i més autoescalfament.

## 7 Aplicacions dels sensors de bobina

![Sensor inductiu de nucli obert: bobina amb nucli ferromagnètic enfrontada a un disc ferromagnètic mòbil a distància x](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_2.png)

*Figura: Figura 7.22 Mesura de distància amb sensor inductiu amb nucli obert.*

![Corba de variació percentual de la inductància en funció de la distància, decreixent de forma hiperbòlica](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_3.png)

*Figura: Figura 7.23 Variació relativa de la inductància amb la distància.*

En la configuració de **nucli obert**, la variable mesurada és la distància  $x$
 entre la cara frontal de la bobina i un disc ferromagnètic. Quan l'objecte s'acosta, la permeabilitat efectiva del camí magnètic augmenta i la inductància creix. La corba de resposta és **hiperbòlica decreixent**: a la figura 7.23 s'acosta al 100 % per a  $x \to 0$
, cau al 55–60 % cap als 2 cm, al 20–25 % entre 4 i 5 cm, i s'aplana cap al 5–10 % per damunt dels 8–10 cm.

| Configuració | Principi |
|:--- |:--- |
| **Mig nucli toroïdal**<br>(figura 7.24) | Nucli toroïdal amb bobina helicoïdal i un entreferro orientat cap a l'objecte. Les línies de flux surten parcialment per l'entreferro i es tanquen a través de l'objecte ferromagnètic: com més a prop és, més flux s'hi canalitza i més gran és la inductància. El nucli tancat millora la linealitat i la sensibilitat respecte del nucli obert i redueix la influència de pertorbacions externes. |
| **Diferencial en pont**<br>(figura 7.25) | Dues bobines simètriques sobre dos nuclis en U enfrontats, amb una armadura mòbil central. En repòs els dos entreferros són iguals i les inductàncies coincideixen; en desplaçar-se l'armadura cap a  $L_1$, aquesta augmenta i  $L_2$   disminueix. Integrades en un pont de Wheatstone amb dues resistències, en equilibri la sortida és nul·la i el desequilibri dona una tensió proporcional al desplaçament. Les variacions de temperatura o de permeabilitat afecten igual les dues bobines i queden cancel·lades. |
| **Mesura de força**<br>(figures 7.26 a 7.28) | La força es converteix en desplaçament amb un element elàstic. Tres variants: el bobinatge es desplaça respecte d'un **imant permanent** i la interacció entre els dos camps fluctua amb la posició relativa; el desplaçament mou un **nucli ferromagnètic** dins de la bobina, amb un canvi de  $L$   força lineal; o **dos nuclis** se separen entre si, de manera que com més a prop són, més concentrat és el flux i més gran la inductància. |
| **Mesura de gir**<br>(figura 7.29) | Tacòmetre per a rodes dentades, engranatges o discs foradats. La roda ferromagnètica és solidària a l'eix i la bobina té un nucli imantat separat d'ella una distància que depèn de l'angle: el gir provoca augments i disminucions abruptes d'inductància síncrones amb la roda. |
| **Mesura de gruix**<br>(figura 7.30) | Per a materials **no ferromagnètics**, el gruix  $e$   s'interposa com un entreferro d'aire entre el nucli i una base ferromagnètica de referència, i la inductància disminueix en augmentar  $e$   perquè el flux es dispersa. Per a materials **ferromagnètics**, com més gran és  $e$   més flux pot conduir el material i més gran és la inductància. |
| **Mesura de pressió**<br>(figura 7.31) | En repòs el diafragma és pla a una distància nominal i el flux es distribueix uniformement pels tres pols d'un nucli en E, amb inductància màxima. En aplicar pressió, el diafragma es comba cap a l'exterior, l'entreferro creix i la inductància cau. |

![Sensor inductiu amb nucli toroïdal i entreferro orientat cap a un objecte ferromagnètic](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_4.png)

*Figura: Figura 7.24 Mesura de distància amb sensor inductiu amb mig nucli toroïdal.*

![Sensor inductiu diferencial: dues bobines sobre nuclis en U enfrontats amb armadura mòbil central, integrades en un pont de Wheatstone](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_5.png)

*Figura: Figura 7.25 Mesura de distància amb sensor inductiu diferencial.*

![Mesura de força amb bobinatge desplaçable respecte d'un imant permanent](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_6.png)

*Figura: Figura 7.26 Mesura de força amb inductància i imant permanent.*

![Mesura de força amb nucli ferromagnètic mòbil dins de la bobina](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_7.png)

*Figura: Figura 7.27 Mesura de força amb inductància i nucli ferromagnètic mòbil.*

![Mesura de força o distància amb dos nuclis ferromagnètics separats per una distància petita](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_8.png)

*Figura: Figura 7.28 Mesura de força o distància amb dos nuclis separats per una distància petita.*

![Tacòmetre inductiu: roda dentada ferromagnètica davant d'una bobina amb nucli imantat](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_9.png)

*Figura: Figura 7.29 Mesura inductiva de gir.*

![Mesura inductiva de gruix per a materials ferromagnètics i no ferromagnètics](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_10.png)

*Figura: Figura 7.30 Mesura inductiva de gruix.*

![Sensor de pressió inductiu amb nucli en E i diafragma, en repòs i amb pressió aplicada](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_11.png)

*Figura: Figura 7.31 Mesura inductiva de pressió.*

## 8 Corrents de Foucault

Els **corrents de Foucault** —*eddy currents* en anglès, en honor del físic francès Léon Foucault (1819–1868)— són corrents elèctrics que s'indueixen en la massa d'un conductor quan aquest s'exposa a un **camp magnètic variable en el temps**. És una conseqüència directa de la llei de Faraday: el camp magnètic variable genera un camp elèctric rotacional al conductor que hi fa circular corrent. Si el camp incident és perpendicular a la superfície, el corrent induït forma espirals circulars prop de la superfície del conductor.

Per la llei de Lenz, aquests corrents circulen en el sentit que genera un camp magnètic **contrari** al que els ha causat. La conseqüència directa sobre la bobina que genera el camp és que la seva inductància efectiva **disminueix** en presència del conductor, perquè el camp dels corrents induïts redueix el flux net concatenat.

Els corrents no es distribueixen uniformement pel volum del conductor: per l'**efecte pell** queden confinats en una capa superficial de **profunditat de penetració**

$$
\delta_s = \sqrt{\frac{2}{\omega\mu_0\mu_r\sigma}} = \frac{1}{\sqrt{\pi f \mu_0\mu_r\sigma}} \qquad (7.24)
$$

que decreix amb la freqüència, amb la permeabilitat i amb la conductivitat. Per a l'alumini  $(\sigma \approx 3{,}8\times10^7\ \mathrm{S/m})$
,  $\delta_s \approx 82$
 μm a 1 MHz i  $\approx 26$
 μm a 10 MHz; per al ferro  $(\sigma \approx 10^7\ \mathrm{S/m},\ \mu_r \approx 1000)$
 ja és de  $\approx 160$
 μm a només 1 kHz. La profunditat de penetració determina fins a quina profunditat el sensor és sensible a la microestructura del material i, per tant, la resolució en profunditat per a la detecció de defectes.

La intensitat dels corrents induïts, i per tant la pertorbació que introdueixen en la inductància, és proporcional a la conductivitat del material i a la freqüència del camp incident. D'aquí que aquests sensors treballin a freqüències de l'ordre de **MHz**: a freqüències baixes els corrents serien massa febles per produir una variació detectable, especialment en materials no ferromagnètics de conductivitat moderada. I com que les pèrdues d'un nucli ferromagnètic a MHz en degradarien el funcionament, empren **bobines sense nucli ferromagnètic**: l'absència de nucli redueix la inductància disponible, però l'alta freqüència ho compensa parcialment.

![Mesura de distància amb sensor de corrents de Foucault: bobina sensora fixa i conductor objectiu que s'hi aproxima](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_12.png)

*Figura: Figura 7.32 Mesura de distància amb sensors de corrent de Foucault.*

La primera aplicació és la **mesura de distància i proximitat de conductors no ferromagnètics** —alumini, coure, acer inoxidable austenític—, que els sensors inductius de nucli ferromagnètic no detecten bé. La bobina sensora es munta fixa i el conductor objectiu s'hi aproxima: com menor és la distància, més intensos són els corrents induïts i major la reducció d'inductància. S'hi afegeix habitualment una **bobina de referència**, idèntica però allunyada de l'objecte, en configuració de pont de Wheatstone: la mesura diferencial elimina les derives tèrmiques i les variacions de freqüència d'excitació comunes a les dues branques.

![Inspecció no destructiva amb corrents de Foucault: la bobina recorre la superfície i els corrents es redistribueixen en trobar una fissura](assets/05_Unitat7_Sensors_inductius_i_corrents_de_Foucault_img_13.png)

*Figura: Figura 7.33 Mesura de fissures amb sensors de corrent de Foucault.*

La segona és la **inspecció no destructiva** (NDT) de peces metàl·liques per detectar fissures, inclusions i porositats. Quan la bobina es desplaça paral·lelament a una superfície sense defectes, els corrents hi circulen sense interrupció; en arribar a una discontinuïtat no la poden creuar i es **redistribueixen**, cosa que altera el camp que retorna a la bobina i en canvia la inductància de manera detectable. La tècnica detecta fissures de profunditat molt inferior a la de penetració, amb una resolució que depèn de la freqüència, de la geometria de la bobina i del material. S'aplica en peces aeronàutiques, canonades, recipients a pressió, raïls i soldadures estructurals.

> [!TIP] **Síntesi**
>
> L'autoinductància relaciona el flux concatenat amb el corrent que el genera, i per a un solenoide val  $L = \mu_0\mu_r n^2 F_c F_g$
>, o equivalentment  $L = N^2/\mathcal{R}$
>: un ferromagnètic redueix la reluctància i augmenta  $L$
>, i l'entreferro la domina. El mesurand pot actuar sobre la geometria, sobre el nombre de voltes o sobre la permeabilitat del camí, i un conductor no ferromagnètic proper redueix  $L$
> per corrents de Foucault. Com que en contínua només queda  $R_{\mathrm{bob}}$
>, cal excitació alterna a una freqüència que faci  $\omega L$
> rellevant. L'objectiu ha de ser metàl·lic i la resposta depèn de la seva conductivitat i permeabilitat. La bobina d'aire aporta linealitat i freqüència alta; el nucli ferromagnètic, sensibilitat a canvi d'histèresi i de pèrdues creixents amb la freqüència. Els corrents de Foucault, confinats per l'efecte pell a una profunditat  $\delta_s$
> que decreix amb  $f$
>,  $\mu_r$
> i  $\sigma$
>, sostenen la mesura de distància a conductors no ferromagnètics i la inspecció no destructiva de fissures.

[← 4. Aplicacions dels sensors capacitius i el condensador diferencial](#aplicacions-dels-sensors-capacitius-i-el-condensador-diferencial)[6. Transformadors variables, efecte Hall i magnetostricció →](#transformadors-variables-efecte-hall-i-magnetostricció)

---

<!-- FIN CAPÍTULO: 05_Unitat7_Sensors_inductius_i_corrents_de_Foucault -->

---

<!-- INICIO CAPÍTULO: 06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio -->

# Transformadors variables, efecte Hall i magnetostricció

Sistemes de Mesura · **Unitat 7 — Sensors reactius i electromagnètics** · Document 6 de 6

# Transformadors variables, efecte Hall i magnetostricció

Dedicació estimada: 17 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar el funcionament diferencial de la LVDT i com se n'obté el signe del desplaçament.
> - Justificar la dependència sinusoïdal del resolver i la necessitat de dos secundaris en quadratura.
> - Escriure la tensió Hall i justificar per què s'empren semiconductors.
> - Distingir els quatre efectes magnetostrictius i les aplicacions que en deriven.

## 1 Transformadors variables

En aquesta família la variable de mesura és la inductància mútua  $M$
 entre una bobina primària, excitada amb una tensió sinusoïdal d'amplitud  $V$
 i freqüència  $f_0$
, i una o més secundàries. A diferència de les autoinductàncies,  $M$
 varia de manera molt ben controlada amb la posició relativa entre bobinatges, cosa que permet gran linealitat i repetibilitat. Els dos casos importants són el **desplaçament lineal** d'un nucli mòbil que acobla primari i secundari —principi de la LVDT— i el **gir angular** entre tots dos, amb dependència  $M \propto \cos\theta$
 —principi del resolver. La freqüència d'excitació, recomanada pel fabricant, ha de garantir una tensió induïda mesurable i la linealitat o la dependència trigonomètrica precisa.

## 2 La LVDT

![Model elèctric de la LVDT: bobina primària L1 al centre i dues secundàries L2 connectades en sèrie i oposició, amb nucli ferromagnètic mòbil](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_1.png)

*Figura: Figura 7.34 Model elèctric d'una LVDT.*

La **LVDT** (*Linear Variable Differential Transformer*) consisteix en tres bobines enrotllades coaxialment sobre un cilindre no conductor: una **primària** al centre i dues **secundàries** simètriques als dos costats. Les secundàries es connecten **en sèrie i en oposició** —fil continu, sentit d'enrotllament contrari—, de manera que les tensions induïdes es **resten**. A l'interior es desplaça axialment un **nucli ferromagnètic mòbil**, de ferrita o d'aliatge ferro-níquel de baixa histèresi, unit a l'objecte a mesurar; no toca les bobines i es mou amb fricció gairebé nul·la.

Quan el primari s'excita, el camp es canalitza preferentment pel nucli i la fracció de flux que arriba a cada secundari depèn de la seva posició. Per a desplaçaments  $x$
 petits respecte de la longitud del sensor, la dependència és lineal:

$$
M_1(x) = M_0 + K_1 x\;\qquad M_2(x) = M_0 - K_2 x \qquad (7.25)
$$

on  $M_0$
 és la inductància mútua en la posició central i  $K_1 = K_2 = K$
 en una LVDT simètrica ideal. Les tensions induïdes i la sortida diferencial valen

$$
V_{S1} = j\omega M_1 I\;\qquad V_{S2} = j\omega M_2 I \qquad (7.26)
$$

$$
V_{\mathrm{out}} = V_{S1} - V_{S2} = j\omega (M_1 - M_2) I \qquad (7.27)
$$

i, substituint-hi el corrent del primari  $I \approx V/(j\omega L_1)$
,

$$
V_{\mathrm{out}} \approx \frac{(K_1+K_2)}{L_1}\,x\,V = K\,x\,V \qquad (7.28)
$$

La tensió de sortida és, en l'aproximació lineal, **proporcional al desplaçament i a l'amplitud del senyal d'excitació**. La constant  $K$
 és la sensibilitat de la LVDT, s'expressa en V/mm o V/μm i l'especifica el fabricant.

### La posició de nul i el signe del desplaçament

En la posició central les dues inductàncies mútues són iguals per simetria, les tensions induïdes tenen la mateixa amplitud i, en oposició, es cancel·len: la sortida diferencial és **nul·la**. En una LVDT real, petites imperfeccions constructives hi deixen una tensió residual, la **tensió de nul** (*null voltage*), que un bon sensor manté per sota del 0,1 % del fons d'escala.

El comportament per a desplaçaments positius i negatius és **asimètric en fase**, i això permet recuperar el signe:

| Posició del nucli | Acoblament | Fase de  $V_{\mathrm{out}}$   respecte de l'excitació |
|:--- |:--- |:--- |
| $x>0$   (cap a S1) | $M_1 > M_2$ | 0° |
| $x=0$ | $M_1 = M_2$ | sortida nul·la |
| $x<0$   (cap a S2) | $M_2 > M_1$ | 180° |

En tots dos sentits l'amplitud de sortida és proporcional a  $|x|$
. Per obtenir el signe, el condicionador ha d'incorporar un **detector de fase** o un desmodulador síncron que compari la fase de la sortida amb la de l'excitació. Aquest processament conjunt d'amplitud i fase és propi dels sensors de transformador variable i es desenvolupa a la unitat 8.

### Efectes no ideals i freqüència òptima

| Efecte | Conseqüència |
|:--- |:--- |
| **Resistència dels bobinatges** | La del primari limita el corrent d'excitació i la dels secundaris hi introdueix una caiguda que no és funció de  $M$. En pujar la freqüència,  $\omega L$   creix i el pes relatiu de  $R_{\mathrm{bob}}$   disminueix. |
| **Dependència de la freqüència** | A freqüència molt baixa, les pèrdues resistives del primari redueixen el corrent i la tensió induïda; a freqüència molt alta, les capacitats paràsites entre bobines i les pèrdues del nucli alteren les inductàncies mútues. Existeix, doncs, un rang òptim. |
| **Resistència de càrrega** | Una càrrega finita als secundaris hi forma un divisor i en modifica amplitud i fase segons la freqüència i la posició del nucli. El condicionador ha de presentar impedància d'entrada molt elevada o corregir-ne l'efecte. |

Cada LVDT té, per això, una **freqüència d'excitació òptima** especificada pel fabricant, típicament entre **1 kHz i 20 kHz** segons les dimensions. Una regla pràctica és escollir-la de manera que  $\omega_0 L_1/R_{\mathrm{bob},1} \in [3{,}10]$
: així el corrent del primari és predominantment inductiu i el transformador s'acosta al model ideal, amb sortida estrictament proporcional a  $x$
, desfasament exacte de 0° o 180° i sensibilitat independent de la freqüència.

![Construcció física d'una LVDT: primari central, dos secundaris als extrems, nucli mòbil amb barra i carcassa](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_2.png)

*Figura: Figura 7.35 Exemple de construcció física d'una LVDT.*

![Funció de resposta d'una LVDT: recta dins del rang lineal normalitzat i pèrdua de linealitat per fora](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_3.png)

*Figura: Figura 7.36 Funció de resposta d'una LVDT.*

El nucli es connecta per una barra rígida que sobresurt per un extrem, i l'hermeticitat de la carcassa permet construir LVDT per a entorns submergits, alta pressió o temperatures extremes, amb rangs de ±0,25 mm fins a ±250 mm o més. La resolució no té límit mecànic intrínsec, perquè no hi ha contacte entre parts mòbils i fixes, i la limita el soroll del condicionador. Dins del **rang lineal** especificat l'error de linealitat no supera típicament el ±0,1 % o el ±0,25 % del fons d'escala; per damunt de  $x_{\max}$
 la resposta se n'aparta de manera creixent. Aquesta combinació fa de la LVDT un sensor de referència en metrologia de posició: patró de traçabilitat, màquines de mesura per coordenades, assajos de materials, barres de control de centrals nuclears i superfícies de control de vol.

## 3 El resolver

![Esquema del potenciòmetre d'inducció o resolver: bobinat del rotor i bobinat de l'estator acoblats a través d'un entreferro d'aire, amb angle relatiu alfa](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_4.png)

*Figura: Figura 7.37 El potenciòmetre d'inducció o resolver.*

El **potenciòmetre d'inducció**, o *resolver*, és l'equivalent angular de la LVDT: un sensor de transformador variable per a la mesura precisa d'angles de gir, també sense contacte entre primari i secundari. Els dos bobinatges són sobre parts físicament separades —el **rotor**, solidari a l'eix, i l'**estator**, fix— i l'acoblament es produeix a través d'un **entreferro d'aire**.

La clau física és que la inductància mútua depèn de l'alineament relatiu entre bobines: alineades, l'acoblament és màxim; perpendiculars, no hi ha flux net del primari que travessi el secundari. Per a un angle arbitrari  $\alpha$
 la dependència és sinusoïdal,

$$
M(\alpha) = M_{\max}\cos\alpha \qquad (7.29)
$$

i la tensió de sortida val  $V_{\mathrm{out}}(\alpha) = K V\cos\alpha$
, amb  $K = M_{\max}/L_1$
 adimensional i típicament entre 0,3 i 0,9.

Un sol secundari no permet una mesura unívoca en tot el cercle, perquè el cosinus pren el mateix valor per a  $\alpha$
 i per a  $-\alpha$
. Els resolvers comercials incorporen per això **dos secundaris desfasats 90°**, en quadratura:

$$
V_{s1}(\alpha) = KV\cos\alpha\;\qquad V_{s2}(\alpha) = KV\sin\alpha \qquad (7.30)
$$

La combinació dels dos senyals determina l'angle de manera unívoca en qualsevol quadrant mitjançant la funció arctangent de dos arguments,

$$
\alpha = \mathrm{atan2}(V_{s2},\,V_{s1}) \qquad (7.31)
$$

El circuit digital que fa aquesta descodificació és el **RDC** (*Resolver-to-Digital Converter*), component estàndard dels sistemes de control de motors de precisió: interpreta els senyals modulats del resolver i en dona una estimació digital de l'angle.

![Implementació física d'un resolver: bobinat toroïdal al rotor i bobinat a l'estator, separats per l'entreferro](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_5.png)

*Figura: Figura 7.38 Implementació física d'un resolver.*

| Efecte | Conseqüència |
|:--- |:--- |
| **Imperfeccions de simetria** | Si els secundaris no són exactament en quadratura, o si les seves sensibilitats no coincideixen, apareix un **error d'harmònic**: un error d'angle que depèn del valor de  $\alpha$. S'especifica en minuts d'arc: per sota de ±1′ en resolvers industrials i de ±10″ en els de precisió científica. |
| **Tensió de desequilibri** | A la posició de desacoblament màxim la tensió residual no és exactament zero, i es manifesta com un error de zero que cal compensar al condicionador. |
| **Dependència de la freqüència** | Sensibilitat i fases relatives depenen de la freqüència d'excitació per les mateixes raons que a la LVDT. Cada resolver té una freqüència òptima recomanada, típicament entre 400 Hz i 20 kHz. |

El resolver és la solució preferida quan la robustesa pesa més que el cost: vibracions, xocs, pols, oli o temperatures extremes el deixen pràcticament indemne. S'usa en control de posició de motors de precisió, robots, màquines-eina de control numèric, navegació inercial i superfícies de vol, de −55 °C a +125 °C i amb immunitat a radiacions ionitzants.

Dues variants completen la família. El **synchro** té un rotor lliure i tres bobinats estàtics desfasats 120°, en què s'indueixen tensions proporcionals a  $\sin\theta$
,  $\sin(\theta+120^\circ)$
 i  $\sin(\theta+240^\circ)$
 que determinen l'angle. L'**inductosyn** és una variant planar amb els bobinats com a pistes conductores sobre un substrat, amb resolucions de micròmetres o de fraccions de segon d'arc.

## 4 Sensors d'efecte Hall

![Efecte Hall: làmina de longitud l, amplada w i gruix th recorreguda per un corrent I en x, amb camp magnètic B en z i tensió Hall transversal en y](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_6.png)

*Figura: Figura 7.39 Efecte Hall.*

L'efecte Hall el va descobrir Edwin Herbert Hall el 1879 en metalls, on és molt feble; la seva aplicació de major impacte ha estat en **semiconductors**, on és centenars de milers de vegades més intens.

El principi és una conseqüència directa de la **força de Lorentz**: un portador de càrrega que es mou amb velocitat  $\mathbf{v}$
 en presència d'un camp magnètic  $\mathbf{B}$
 experimenta una força perpendicular a tots dos vectors,

$$
\mathbf{F}_L = q\,\mathbf{v}\times\mathbf{B} \qquad (7.32)
$$

En una làmina de gruix  $t_h$
 recorreguda per un corrent  $I$
 i sotmesa a un camp  $B_z$
 perpendicular, la força empeny els portadors cap a un extrem transversal, on s'acumulen fins que el camp elèctric resultant l'equilibra. Entre els dos extrems apareix la **tensió Hall**

$$
V_H = \frac{I\,B_z}{q\,N_c\,t_h} \qquad (7.33)
$$

on  $q \cong 1{,}6\times10^{-19}$
 C és la càrrega elemental i  $N_c$
 la densitat volumètrica de portadors. La tensió Hall és, doncs, **proporcional al corrent i al camp perpendicular**, i **inversament proporcional** a la densitat de portadors i al gruix.

> [!WARNING] **Ordres de magnitud**
>
> Amb  $I = 1$
> mA,  $B_z = 0{,}1$
> T i  $t_h = 100$
> μm: en coure, amb  $N_c \approx 8{,}5\times10^{28}\ \mathrm{m^{-3}}$
>, s'obtenen uns **70 pV**, completament indetectables. En GaAs poc dopat, amb  $N_c \approx 10^{21}\ \mathrm{m^{-3}}$
> —vuit ordres de magnitud menys—, s'obtenen uns **6,25 mV**, perfectament mesurables.

La baixa densitat de portadors dels semiconductors és, doncs, la que fa viables aquests sensors. A més,  $N_c$
 és **ajustable pel procés de dopat**: en un semiconductor intrínsec depèn de la temperatura, però amb impureses donadores o acceptadores en concentracions controlades el fabricant hi fixa un valor estable i gairebé independent de la temperatura. Els materials habituals són silici, arsenur de gal·li i arsenur d'indi; l'InAs interessa per a gran sensibilitat per la seva mobilitat elevada, i el GaAs domina en consum per la facilitat d'integració en CMOS.

Reduir el gruix augmenta la tensió Hall, però també la resistència de la làmina en la direcció del corrent,

$$
R_{\mathrm{làmina}} = \frac{\rho\,l}{w\,t_h} = \frac{l}{w\,\mu\,q\,N_c\,t_h} \qquad (7.34)
$$

Una làmina molt prima exigeix més tensió d'alimentació per al mateix corrent, genera més soroll tèrmic —proporcional a  $\sqrt{R}$
— i dissipa més per autoescalfament —proporcional a  $I^2R$
. El disseny és, doncs, un **compromís entre sensibilitat, soroll i dissipació**, que a la pràctica situa els gruixos entre 1 i 10 μm.

El competidor tecnològic principal és la **magnetoresistència** vista a la unitat 5, i en particular les variants gegant (GMR) i de túnel (TMR), de sensibilitat superior en alguns casos. El sensor Hall manté avantatges propis: integració en CMOS estàndard, linealitat de la resposta amb  $B$
 en un ampli rang, conservació de la **polaritat** del camp —de manera que el condicionament en pot recuperar el signe— i robustesa davant de camps intensos que saturarien una magnetoresistència.

### Aplicacions

![Detector de presència d'imant amb sensor d'efecte Hall i comparador de llindar](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_7.png)

*Figura: Figura 7.40 Detector de moviment amb sensors d'efecte Hall.*

![Mesurador de nivell de líquid amb imant sobre boia (esquerra) i sensor de pressió amb imant solidari al diafragma (dreta)](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_8.png)

*Figura: Figura 7.41 Mesurador de nivell (esquerra) i sensor de pressió (dreta) amb sensors d'efecte Hall.*

![Detecció del pas d'una bola ferromagnètica que pertorba el camp d'un imant fix davant del sensor Hall](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_9.png)

*Figura: Figura 7.42 Detecció de pas d'un objecte ferromagnètic amb sensors d'efecte Hall.*

![Sensor de velocitat de rotació: roda dentada ferromagnètica entre un imant i el sensor Hall, que genera un tren de polsos](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_10.png)

*Figura: Figura 7.43 Sensor de velocitat de rotació basat en sensors d'efecte Hall.*

![Sensor de corrent Hall amb nucli ferromagnètic toroïdal que canalitza el camp del conductor cap a la làmina Hall](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_11.png)

*Figura: Figura 7.44 Sensor de corrent basat en sensors d'efecte Hall.*

Totes les aplicacions mesuren un camp magnètic o les pertorbacions d'un camp preexistent, **inclosos els camps estàtics**, i es reparteixen en tres famílies.

**Presència d'un imant.** Si un imant s'aproxima,  $B$
 a la làmina creix i  $V_H$
 amb ell; un comparador de llindar en dona un senyal discret. És un sensor de proximitat sense parts mòbils ni desgast: botons i tancaments de telèfons, obertura de portelles, limitadors de posició i sensors d'arbre de lleves. Amb l'imant sobre una boia s'obté un detector de nivell de líquid; solidari a un diafragma, un sensor de pressió.

**Pertorbació d'un camp fix.** Amb el sensor situat en el camp d'un imant permanent, els materials ferromagnètics propers en distorsionen les línies. Així es detecta el pas d'una bola ferromagnètica o les dents d'una roda dentada: quan una dent s'interposa entre imant i sensor bloqueja les línies i  $V_H$
 baixa, i quan hi passa una cavitat puja. El resultat és un tren de polsos que permet comptar dents i calcular posició angular i velocitat de rotació.

**Mesura de corrent sense contacte.** Qualsevol corrent genera un camp magnètic al seu voltant, que a una distància  $r$
 d'un conductor rectilini val

$$
B(r) = \frac{\mu_0 I_{\mathrm{mesurat}}}{2\pi r} \qquad (7.35)
$$

Mesurant  $B$
 s'infereix el corrent sense tallar el circuit ni inserir-hi cap element en sèrie. Per a corrents de centenars o milers d'ampers és la solució estàndard, tant per seguretat —la làmina resta al potencial de massa del circuit de mesura, aïllada del conductor d'alta tensió— com per facilitat d'instal·lació. Per guanyar sensibilitat i reduir camps espuris, la làmina s'integra dins d'un **nucli ferromagnètic toroïdal** que hi canalitza i concentra el camp del conductor.

## 5 Sensors magnetostrictius

La **magnetostricció** és l'acoblament bidireccional entre l'estat magnètic i la deformació mecànica d'un material ferromagnètic: es deforma quan s'hi aplica un camp, perquè els dominis magnètics s'orienten i arrosseguen la xarxa cristal·lina, i recíprocament la seva magnetització canvia quan es deforma, perquè la reordenació cristal·lina altera l'orientació dels dominis.

![Efecte Joule magnetostrictiu: dominis magnètics orientats aleatòriament sense camp i alineats amb camp aplicat, amb el canvi de longitud associat](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_12.png)

*Figura: Figura 7.45 Efecte Joule magnetostrictiu.*

| Efecte | Descripció |
|:--- |:--- |
| **Joule** (1842) | Efecte directe: un ferromagnètic canvia de forma en aplicar-hi un camp. Sense camp, els dominis estan orientats aleatòriament i les seves deformacions s'anul·len estadísticament; en aplicar-lo s'orienten progressivament i el material s'allarga en la direcció del camp i es comprimeix en les perpendiculars, o a l'inrevés segons el material. La deformació relativa  $\lambda = \Delta l/l$   és el coeficient de magnetostricció. |
| **Villari** (1865) | Invers del Joule: una deformació de tracció o compressió canvia la magnetització i la permeabilitat del material. És la base dels sensors de força i pressió. |
| **Wiedemann** (1858) | Apareix una **torsió** en una barra ferromagnètica travessada simultàniament per un camp longitudinal i per un corrent, que genera un camp circular al seu voltant: la superposició dona un camp en espiral que indueix la torsió mecànica. |
| **Mateucci** | Invers del Wiedemann: una torsió mecànica altera la distribució dels dominis i, per tant, la magnetització del material. |

Tots els ferromagnètics presenten magnetostricció, però amb deformacions que rarament superen les desenes de ppm:  $\lambda_s \approx -7$
 ppm en ferro pur,  $-34$
 ppm en níquel i  $-60$
 ppm en cobalt, on el signe negatiu indica contracció en la direcció del camp. Són valors detectables però insuficients per a la majoria d'aplicacions, que demanen 0,1 % o més. El permalloy (Fe-Ni) i el Metglas, aliatge amorf de ferro, silici i bor, tenen coeficients força majors i s'usen en sensors comercials de força, pressió i vibració. El **Terfenol-D** —aliatge de ferro, terbi i disprosi desenvolupat als anys 1970 per a sonar submarí— els supera de molt:

| Propietat | Valor |
|:--- |:--- |
| Deformació màxima | Fins a 2000 ppm (0,2 %) abans de saturació: entre 50 i 100 vegades la del ferro o el níquel. |
| Velocitat d'ones longitudinals | De 1640 a 1940 m/s, molt inferior a la de l'acer (≈ 5900 m/s), per la densitat alta  $(\rho \approx 9250\ \mathrm{kg/m^3})$   i la baixa rigidesa en la direcció magnetostrictiva. |
| Permeabilitat relativa | Entre 4,5 i 10, baixa per a un ferromagnètic (el ferro dolç arriba a  $\mu_r \approx 5000$  ): limita la inductància de les bobines que l'empren com a nucli, sense afectar les propietats magnetostrictives. |
| Resistivitat elèctrica | $\approx 58\times10^{-8}\ \Omega\cdot\mathrm{m}$, molt superior a la del ferro  $(\approx 10\times10^{-8})$: limita els corrents de Foucault al material i n'estén el rang de freqüències d'operació. |

### Sensor de temps de vol

![Sensor magnetostrictiu de temps de vol: fil magnetostrictiu amb imant permanent mòbil sobre una boia i sistema de detecció a un extrem](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_13.png)

*Figura: Figura 7.46 Sensor de temps de vol magnetostrictiu.*

És una de les tecnologies de mesura de posició lineal de major exactitud entre centímetres i metres, i combina els efectes Wiedemann i Mateucci. El sensor és una barra o fil magnetostrictiu al llarg del qual es desplaça un **imant permanent** solidari a l'element mòbil; en un dipòsit de líquid, l'imant va sobre una boia.

En un extrem del material s'aplica un breu pols de corrent, de l'ordre de microsegons, que genera un camp magnètic circular al voltant del fil. A la posició de l'imant, aquest camp se superposa al camp axial de l'imant i, per l'**efecte Wiedemann**, genera una torsió localitzada que es propaga com una **ona acústica** en ambdues direccions a la velocitat del so en el material. El temps  $\Delta t$
 entre el pols i l'arribada de l'ona al detector dona la distància:

$$
d = v_s\cdot\Delta t \qquad (7.36)
$$

La detecció de l'ona es fa amb un **sensor piezoelèctric** que capta la vibració a l'extrem, o —molt més habitual a la indústria— aprofitant que la vibració canvia localment la permeabilitat del material per **efecte Mateucci**, de manera que una bobina que l'envolta veu un canvi d'inductància i genera un pols de tensió. La resolució típica és d'1 a 50 μm en rangs de fins a 2–3 m, amb linealitat millor del 0,05 % del fons d'escala i repetibilitat inferior al micròmetre.

### Força, pressió i torsió

![Sensor magnetostrictiu de força o pressió: bobina generadora i bobina receptora al voltant del material magnetostrictiu sotmès a esforç](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_14.png)

*Figura: Figura 7.47 Sensor de força o pressió magnetostrictiu.*

![Sensor magnetostrictiu de torsió: moment torçor aplicat sobre el material amb bobines generadora i receptora](assets/06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio_img_15.png)

*Figura: Figura 7.48 Sensor de torsió magnetostrictiu.*

La segona aplicació explota l'**efecte Villari**: una tensió mecànica sobre el material en fa variar la permeabilitat i, com que  $L \propto \mu_r$
, el canvi és directament detectable. La configuració té una **bobina generadora** (primari) al voltant del material, excitada en alterna, i una **bobina receptora** (secundari) que capta el flux que l'ha travessat: la variació de permeabilitat modifica la inductància mútua i la tensió induïda en proporció a la força aplicada. A diferència d'un sensor inductiu convencional, aquí la variació prové d'un **canvi intrínsec de propietat del material**, sense desplaçament apreciable.

La tercera és l'anàleg de torsió, per **efecte Mateucci**: un moment torçor altera la permeabilitat en proporció al moment, amb el mateix esquema de dues bobines. Mesuren el parell en arbres de transmissió de potència —automoció, turbines, motors elèctrics—, sobretot quan no es poden connectar cables al rotor. La seva virtut davant de les cel·les de càrrega és mesurar sense contacte i sense distorsionar mecànicament l'element mesurat, que continua transmetent potència.

> [!TIP] **Síntesi**
>
> Els sensors de transformador variable mesuren la inductància mútua. La LVDT té un primari central i dos secundaris en sèrie i oposició, amb sortida  $V_{\mathrm{out}} \approx K x V$
>, nul·la al centre llevat de la tensió de nul, i fase de 0° o 180° que dona el signe del desplaçament; la freqüència òptima, entre 1 i 20 kHz, equilibra resistències de bobinatge i capacitats paràsites. El resolver n'és l'equivalent angular, amb  $M(\alpha) = M_{\max}\cos\alpha$
> i dos secundaris en quadratura que resolen l'angle amb  $\mathrm{atan2}$
> en un RDC. El sensor Hall dona  $V_H = IB_z/(qN_c t_h)$
>: la baixa densitat de portadors dels semiconductors el fa viable i el gruix de la làmina compromet sensibilitat, soroll i dissipació. La magnetostricció acobla estat magnètic i deformació pels efectes Joule, Villari, Wiedemann i Mateucci, amb el Terfenol-D com a material de referència.

[← 5. Sensors inductius i corrents de Foucault](#sensors-inductius-i-corrents-de-foucault)

---

<!-- FIN CAPÍTULO: 06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio -->

---

<!-- INICIO CAPÍTULO: 07_Unitat7_Entrenament -->

# Entrenament V/F · Unitat 7: Sensors reactius i electromagnètics

Sistemes de Mesura (230920) · ETSETB-UPC · **Unitat 7 — Sensors reactius i electromagnètics**

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
> 📌 **Afirmació:** *La geometria del condensador condiciona la sensibilitat i la linealitat del sensor capacitiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La geometria fixa la sensibilitat, la linealitat de C(x) i la vulnerabilitat als paràsits.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 03
> 📌 **Afirmació:** *Els sensors capacitius s'utilitzen habitualment com a primera opció per mesurar temperatura directament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La permitivitat de l'aire és gairebé independent de la temperatura: per això no s'usen per mesurar-la.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *Un condensador diferencial pot duplicar la sensibilitat diferencial respecte d'un únic condensador equivalent.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La diferència C1−C2 = 2ΔC és el doble de sensible que un condensador únic.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *L'efecte Hall es basa en la desviació de portadors de càrrega per la força de Lorentz.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El portador en moviment dins d'un camp magnètic experimenta F = qv×B, que el desvia transversalment.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *La reluctància magnètica augmenta sempre quan un objecte ferromagnètic completa el camí de flux.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Un ferromagnètic aporta permeabilitat elevada i per tant redueix la reluctància del camí.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 07
> 📌 **Afirmació:** *La impedància d'un condensador ideal augmenta proporcionalment amb la freqüència d'excitació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El mòdul és 1/(2πfC): decreix en augmentar la freqüència.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *Les ferrites poden permetre treballar a freqüències més altes que nuclis metàl·lics ferromagnètics conductors.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Les ferrites tenen conductivitat molt menor i redueixen les pèrdues per corrents induïts.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 11
> 📌 **Afirmació:** *La selecció d'un sensor reactiu es pot fer ignorant completament el circuit de condicionament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La tria de f0 depèn simultàniament del sensor, del material, de l'entorn i del condicionador.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 14
> 📌 **Afirmació:** *La geometria del condensador només afecta la fabricació i és irrellevant per a la funció de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La geometria determina quant canvia C per unitat de mesurand i la linealitat de C(x).*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 15
> 📌 **Afirmació:** *En el model paral·lel C-Rp, a freqüències prou altes la impedància queda dominada pel comportament capacitiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per damunt de f−3dB el mòdul és ≈ 1/(2πfC) i el comportament és clarament capacitiu.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 19
> 📌 **Afirmació:** *En una configuració diferencial ideal, una pertorbació comuna pot cancel·lar-se parcialment en fer la diferència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Una pertorbació que afecta igual les dues branques s'elimina en fer la diferència.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *La freqüència de treball és un paràmetre de disseny rellevant en sensors capacitius i inductius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És un dels paràmetres de disseny més rellevants del sistema de mesura.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *El Terfenol-D és un dielèctric utilitzat per augmentar la permitivitat dels sensors capacitius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El Terfenol-D és un aliatge ferromagnètic de Fe, Tb i Dy, no un dielèctric.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *La conductivitat residual del dielèctric explica l'existència d'un corrent de fuita entre plaques.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La conductivitat residual σ del dielèctric fa circular un corrent proporcional a la tensió.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 37
> 📌 **Afirmació:** *Els corrents de Foucault són corrents induïts en un conductor per un camp magnètic variable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició: corrents induïts en la massa d'un conductor per un camp magnètic variable.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 47
> 📌 **Afirmació:** *En un resolver, la inductància mútua varia amb l'angle relatiu entre rotor i estator.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *M(α) = Mmax·cos α: l'acoblament depèn de l'alineament relatiu.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *Els sensors capacitius d'aire poden presentar bona estabilitat tèrmica perquè la permitivitat de l'aire varia poc.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb dielèctric d'aire la permitivitat és pràcticament independent de la temperatura.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 52
> 📌 **Afirmació:** *La sensibilitat d'un sensor inductiu és totalment independent de la distància entre la bobina i l'objecte.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La corba de resposta cau de forma hiperbòlica amb la distància a l'objecte.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 53
> 📌 **Afirmació:** *L'alta impedància d'un sensor capacitiu a baixa freqüència el fa més vulnerable a acoblaments capacitius externs.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb capacitats de pF, |Z| arriba a MΩ o GΩ i el sistema capta interferències per acoblament capacitiu.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 56
> 📌 **Afirmació:** *El resolver mesura desplaçament lineal mitjançant un diafragma capacitiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El resolver és l'equivalent angular de la LVDT i mesura angles per inductància mútua.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 59
> 📌 **Afirmació:** *La resposta d'un sensor inductiu pot dependre de la conductivitat i de la permeabilitat del material objectiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La magnitud de la pertorbació depèn de la conductivitat i de la permeabilitat del material objectiu.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 61
> 📌 **Afirmació:** *L'efecte pell distribueix els corrents de Foucault uniformement per tot el volum del conductor a alta freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Per l'efecte pell, els corrents queden confinats en una capa superficial de profunditat δs.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 65
> 📌 **Afirmació:** *La distància en un sensor de temps de vol magnetostrictiu és proporcional a la velocitat de propagació i al temps mesurat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *d = vs·Δt, amb vs la velocitat del so en el material.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 69
> 📌 **Afirmació:** *En una LVDT, els secundaris estan connectats de manera que les tensions induïdes es resten.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Els dos secundaris es connecten en sèrie i en oposició: les tensions es resten.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 71
> 📌 **Afirmació:** *L'efecte de vores fa que la capacitat real sigui sempre menor que la capacitat ideal d'un condensador pla.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'energia del camp exterior s'afegeix: la capacitat real supera la ideal.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 79
> 📌 **Afirmació:** *La capacitat d'un condensador pla ideal és inversament proporcional a la separació entre plaques.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *C = εA/d.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 84
> 📌 **Afirmació:** *La magnitud mesurada en un sensor modulador és la font principal d'energia del senyal de sortida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En un modulador l'energia del senyal de sortida prové de l'excitació externa.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 87
> 📌 **Afirmació:** *Augmentar la resistència del bobinament redueix simultàniament el soroll tèrmic i l'autoescalfament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Més resistència de bobinatge implica més soroll tèrmic i més autoescalfament.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 92
> 📌 **Afirmació:** *Un resolver amb dos secundaris en quadratura pot proporcionar senyals proporcionalment sinus i cosinus de l'angle.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Els dos secundaris en quadratura donen KV·cos α i KV·sin α.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 93
> 📌 **Afirmació:** *En una configuració diferencial ideal, la suma de les dues capacitats varia fortament amb el desplaçament útil.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *C1 + C2 = 2C0 és idealment constant i independent del desplaçament.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 94
> 📌 **Afirmació:** *L'efecte de vores pot introduir una no linealitat addicional quan la separació varia amb el mesurand.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Si d varia amb el mesurand, l'error de vores hi varia també i afegeix no linealitat.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 97
> 📌 **Afirmació:** *La sensibilitat Hall es maximitza sempre augmentant indefinidament el corrent sense cap penalització.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Més corrent dona més VH però també més dissipació I²R i més autoescalfament.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 99
> 📌 **Afirmació:** *Un condensador diferencial elimina per construcció qualsevol error de no linealitat en tot el rang mecànic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La linealitat diferencial val en primera aproximació i per a desplaçaments petits respecte de d0.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 100
> 📌 **Afirmació:** *Les imperfeccions d'ortogonalitat i de sensibilitat dels secundaris introdueixen errors angulars en sensors basats en transformadors.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Si els secundaris no són en quadratura o difereixen en sensibilitat apareix l'error d'harmònic.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 110
> 📌 **Afirmació:** *Els sensors Hall poden mesurar camps magnètics estàtics.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El sensor Hall respon també a camps estàtics, com el d'un imant permanent.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 111
> 📌 **Afirmació:** *L'autoescalfament és el mecanisme principal de funcionament d'un sensor capacitiu ideal.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El sensor capacitiu ideal no dissipa potència: l'autoescalfament és un efecte residual indesitjat.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 114
> 📌 **Afirmació:** *La linealitat pot dependre tant del principi físic com de la magnitud elèctrica que es mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La linealitat depèn del paràmetre que varia i de si es mesura C o |Z|.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 120
> 📌 **Afirmació:** *Una capacitat paràsita en paral·lel resta directament capacitat al sensor i sempre compensa l'error de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Les capacitats paràsites en paral·lel se sumen a la del sensor i n'alteren la mesura.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 121
> 📌 **Afirmació:** *Una variació de permeabilitat magnètica al voltant de la bobina pot modificar la inductància efectiva.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un canvi de permeabilitat del camí magnètic modifica la inductància efectiva.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 124
> 📌 **Afirmació:** *Un element capacitiu ideal presenta dissipació activa nul·la en el propi element reactiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un element purament reactiu emmagatzema energia i no la dissipa.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 129
> 📌 **Afirmació:** *Un RDC és una bobina auxiliar que substitueix completament l'estator del resolver.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El RDC és un circuit digital de descodificació, no una bobina.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 148
> 📌 **Afirmació:** *Una bobina ideal en contínua proporciona una reactància inductiva elevada que facilita la mesura de L.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En contínua la reactància inductiva és nul·la i la bobina és un curtcircuit.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 151
> 📌 **Afirmació:** *En un sensor reactiu ideal, l'element sensor és un element que emmagatzema energia en un camp elèctric o magnètic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'element sensor és un condensador o una bobina: camp elèctric o magnètic.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 152
> 📌 **Afirmació:** *Una guarda de Kelvin funciona mantenint la guarda a un potencial molt diferent del de l'elèctrode sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La guarda ha d'estar exactament al mateix potencial que la placa sensora.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 165
> 📌 **Afirmació:** *El coure és habitual en bobinaments per la seva baixa resistivitat elèctrica.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *ρCu ≈ 1,7×10⁻⁸ Ω·m minimitza Rbob i, amb ella, el soroll i l'autoescalfament.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 169
> 📌 **Afirmació:** *Els sensors de corrents de Foucault utilitzen normalment excitació en contínua per maximitzar els corrents induïts.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Calen freqüències elevades, de l'ordre de MHz, perquè els corrents siguin mesurables.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 176
> 📌 **Afirmació:** *Una densitat de portadors molt elevada afavoreix una tensió Hall gran per al mateix corrent i camp.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *VH és inversament proporcional a Nc: cal densitat baixa, no elevada.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 180
> 📌 **Afirmació:** *La capacitat d'un condensador pla ideal disminueix quan augmenta la permitivitat del dielèctric.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *C = εA/d: la capacitat és proporcional a la permitivitat.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 190
> 📌 **Afirmació:** *La mesura només de l'amplitud d'una LVDT distingeix automàticament el signe del desplaçament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'amplitud és proporcional a |x|: cal comparar la fase amb l'excitació.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 195
> 📌 **Afirmació:** *El condicionament de sensors reactius consisteix sempre en aplicar una tensió contínua fixa i llegir resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En contínua el sensor reactiu no dona informació del mesurand: cal excitació alterna.*

> **📚 Document de referència:** `Document 01`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | La geometria fixa la sensibilitat, la linealitat de C(x) i la vulnerabilitat als paràsits. | Document 02 |
| **03** | **F** | La permitivitat de l'aire és gairebé independent de la temperatura: per això no s'usen per mesurar-la. | Document 03 |
| **04** | **V** | La diferència C1−C2 = 2ΔC és el doble de sensible que un condensador únic. | Document 04 |
| **05** | **V** | El portador en moviment dins d'un camp magnètic experimenta F = qv×B, que el desvia transversalment. | Document 06 |
| **06** | **F** | Un ferromagnètic aporta permeabilitat elevada i per tant redueix la reluctància del camí. | Document 05 |
| **07** | **F** | El mòdul és 1/(2πfC): decreix en augmentar la freqüència. | Document 02 |
| **08** | **V** | Les ferrites tenen conductivitat molt menor i redueixen les pèrdues per corrents induïts. | Document 05 |
| **11** | **F** | La tria de f0 depèn simultàniament del sensor, del material, de l'entorn i del condicionador. | Document 01 |
| **14** | **F** | La geometria determina quant canvia C per unitat de mesurand i la linealitat de C(x). | Document 02 |
| **15** | **V** | Per damunt de f−3dB el mòdul és ≈ 1/(2πfC) i el comportament és clarament capacitiu. | Document 03 |
| **19** | **V** | Una pertorbació que afecta igual les dues branques s'elimina en fer la diferència. | Document 04 |
| **22** | **V** | És un dels paràmetres de disseny més rellevants del sistema de mesura. | Document 01 |
| **27** | **F** | El Terfenol-D és un aliatge ferromagnètic de Fe, Tb i Dy, no un dielèctric. | Document 06 |
| **32** | **V** | La conductivitat residual σ del dielèctric fa circular un corrent proporcional a la tensió. | Document 03 |
| **37** | **V** | És la definició: corrents induïts en la massa d'un conductor per un camp magnètic variable. | Document 05 |
| **47** | **V** | M(α) = Mmax·cos α: l'acoblament depèn de l'alineament relatiu. | Document 06 |
| **49** | **V** | Amb dielèctric d'aire la permitivitat és pràcticament independent de la temperatura. | Document 03 |
| **52** | **F** | La corba de resposta cau de forma hiperbòlica amb la distància a l'objecte. | Document 05 |
| **53** | **V** | Amb capacitats de pF, \|Z\| arriba a MΩ o GΩ i el sistema capta interferències per acoblament capacitiu. | Document 03 |
| **56** | **F** | El resolver és l'equivalent angular de la LVDT i mesura angles per inductància mútua. | Document 06 |
| **59** | **V** | La magnitud de la pertorbació depèn de la conductivitat i de la permeabilitat del material objectiu. | Document 05 |
| **61** | **F** | Per l'efecte pell, els corrents queden confinats en una capa superficial de profunditat δs. | Document 05 |
| **65** | **V** | d = vs·Δt, amb vs la velocitat del so en el material. | Document 06 |
| **69** | **V** | Els dos secundaris es connecten en sèrie i en oposició: les tensions es resten. | Document 06 |
| **71** | **F** | L'energia del camp exterior s'afegeix: la capacitat real supera la ideal. | Document 03 |
| **79** | **V** | C = εA/d. | Document 02 |
| **84** | **F** | En un modulador l'energia del senyal de sortida prové de l'excitació externa. | Document 01 |
| **87** | **F** | Més resistència de bobinatge implica més soroll tèrmic i més autoescalfament. | Document 05 |
| **92** | **V** | Els dos secundaris en quadratura donen KV·cos α i KV·sin α. | Document 06 |
| **93** | **F** | C1 + C2 = 2C0 és idealment constant i independent del desplaçament. | Document 04 |
| **94** | **V** | Si d varia amb el mesurand, l'error de vores hi varia també i afegeix no linealitat. | Document 03 |
| **97** | **F** | Més corrent dona més VH però també més dissipació I²R i més autoescalfament. | Document 06 |
| **99** | **F** | La linealitat diferencial val en primera aproximació i per a desplaçaments petits respecte de d0. | Document 04 |
| **100** | **V** | Si els secundaris no són en quadratura o difereixen en sensibilitat apareix l'error d'harmònic. | Document 06 |
| **110** | **V** | El sensor Hall respon també a camps estàtics, com el d'un imant permanent. | Document 06 |
| **111** | **F** | El sensor capacitiu ideal no dissipa potència: l'autoescalfament és un efecte residual indesitjat. | Document 03 |
| **114** | **V** | La linealitat depèn del paràmetre que varia i de si es mesura C o \|Z\|. | Document 02 |
| **120** | **F** | Les capacitats paràsites en paral·lel se sumen a la del sensor i n'alteren la mesura. | Document 03 |
| **121** | **V** | Un canvi de permeabilitat del camí magnètic modifica la inductància efectiva. | Document 05 |
| **124** | **V** | Un element purament reactiu emmagatzema energia i no la dissipa. | Document 01 |
| **129** | **F** | El RDC és un circuit digital de descodificació, no una bobina. | Document 06 |
| **148** | **F** | En contínua la reactància inductiva és nul·la i la bobina és un curtcircuit. | Document 05 |
| **151** | **V** | L'element sensor és un condensador o una bobina: camp elèctric o magnètic. | Document 01 |
| **152** | **F** | La guarda ha d'estar exactament al mateix potencial que la placa sensora. | Document 03 |
| **165** | **V** | ρCu ≈ 1,7×10⁻⁸ Ω·m minimitza Rbob i, amb ella, el soroll i l'autoescalfament. | Document 05 |
| **169** | **F** | Calen freqüències elevades, de l'ordre de MHz, perquè els corrents siguin mesurables. | Document 05 |
| **176** | **F** | VH és inversament proporcional a Nc: cal densitat baixa, no elevada. | Document 06 |
| **180** | **F** | C = εA/d: la capacitat és proporcional a la permitivitat. | Document 02 |
| **190** | **F** | L'amplitud és proporcional a \|x\|: cal comparar la fase amb l'excitació. | Document 06 |
| **195** | **F** | En contínua el sensor reactiu no dona informació del mesurand: cal excitació alterna. | Document 01 |

<!-- FIN CAPÍTULO: 07_Unitat7_Entrenament -->

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
| **(7.1)** | $C = \frac{Q}{V}$ |
| **(7.2)** | $C = \frac{\varepsilon A}{d}$ |
| **(7.3)** | $Z_C = \frac{1}{j\,2\pi f C}$ |
| **(7.4)** | $\|Z\| = \frac{1}{2\pi f C} = \frac{d}{2\pi f \varepsilon A}$ |
| **(7.5)** | $C(x) = \frac{\varepsilon\,A(x)}{d} \propto x$ |
| **(7.6)** | $C(x) = \frac{\varepsilon A}{d_0 + x}$ |
| **(7.7)** | $\|Z(x)\| = \frac{d_0 + x}{2\pi f \varepsilon A} \propto d_0 + x$ |
| **(7.8)** | $C(x) = \frac{\varepsilon_1\,xA}{d} + \frac{\varepsilon_2\,(1-x)A}{d} = \frac{A}{d}\left[\varepsilon_2 + (\varepsilon_1-\varepsilon_2)\,x\right]$ |
| **(7.9)** | $\epsilon_r \approx \frac{d}{\pi l}\left(1 + \ln\frac{2\pi l}{d}\right)\cdot 100\,\%$ |
| **(7.10)** | $R_p = \frac{\rho\,d}{A} = \frac{d}{\sigma A}$ |
| **(7.11)** | $R_p \cdot C = \frac{d}{\sigma A}\cdot\frac{\varepsilon A}{d} = \frac{\varepsilon}{\sigma}$ |
| **(7.12)** | $Z = \frac{R_p\cdot\frac{1}{j\omega C}}{R_p+\frac{1}{j\omega C}} = \frac{R_p}{1+j\omega R_p C}$ |
| **(7.13)** | $\|Z\| = \frac{R_p}{\sqrt{1+(2\pi f R_p C)^2}}$ |
| **(7.14)** | $f_{-3\mathrm{dB}} = \frac{1}{2\pi R_p C} = \frac{\sigma}{2\pi\varepsilon}$ |
| **(7.15)** | $100\ \Omega \lesssim \|Z(f_0)\| \lesssim 1\ \mathrm{M\Omega}$ |
| **(7.16)** | $C(h) = C_{\mathrm{aire}} + \left(C_{\mathrm{líquid}} - C_{\mathrm{aire}}\right)\cdot\frac{h}{H}$ |
| **(7.17)** | $C_1(x) = C_0 + \Delta C(x)\;\qquad C_2(x) = C_0 - \Delta C(x)$ |
| **(7.18)** | $\frac{C_1-C_2}{C_1+C_2} = \frac{\Delta C}{C_0}$ |
| **(7.19)** | $L = \frac{N\Phi}{I}$ |
| **(7.20)** | $L = \mu_0\,\mu_r\,n^2\,F_c\,F_g$ |
| **(7.21)** | $\mathcal{R} = \frac{l}{\mu_0\mu_r A}\;\qquad L = \frac{N^2}{\mathcal{R}}$ |
| **(7.22)** | $V_s = j\omega M I_p = j\omega M\,\frac{V_p}{j\omega L_p} = \frac{M}{L_p}\,V_p$ |
| **(7.23)** | $X_L = \omega L = 2\pi f_0 L$ |
| **(7.24)** | $\delta_s = \sqrt{\frac{2}{\omega\mu_0\mu_r\sigma}} = \frac{1}{\sqrt{\pi f \mu_0\mu_r\sigma}}$ |
| **(7.25)** | $M_1(x) = M_0 + K_1 x\;\qquad M_2(x) = M_0 - K_2 x$ |
| **(7.26)** | $V_{S1} = j\omega M_1 I\;\qquad V_{S2} = j\omega M_2 I$ |
| **(7.27)** | $V_{\mathrm{out}} = V_{S1} - V_{S2} = j\omega (M_1 - M_2) I$ |
| **(7.28)** | $V_{\mathrm{out}} \approx \frac{(K_1+K_2)}{L_1}\,x\,V = K\,x\,V$ |
| **(7.29)** | $M(\alpha) = M_{\max}\cos\alpha$ |
| **(7.30)** | $V_{s1}(\alpha) = KV\cos\alpha\;\qquad V_{s2}(\alpha) = KV\sin\alpha$ |
| **(7.31)** | $\alpha = \mathrm{atan2}(V_{s2},\,V_{s1})$ |
| **(7.32)** | $\mathbf{F}_L = q\,\mathbf{v}\times\mathbf{B}$ |
| **(7.33)** | $V_H = \frac{I\,B_z}{q\,N_c\,t_h}$ |
| **(7.34)** | $R_{\mathrm{làmina}} = \frac{\rho\,l}{w\,t_h} = \frac{l}{w\,\mu\,q\,N_c\,t_h}$ |
| **(7.35)** | $B(r) = \frac{\mu_0 I_{\mathrm{mesurat}}}{2\pi r}$ |
| **(7.36)** | $d = v_s\cdot\Delta t$ |