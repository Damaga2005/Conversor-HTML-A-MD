# 📚 Cuaderno Maestro: Tema 5

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 5` | 📄 **Capítulos incluidos:** 10  
> 📅 **Generado:** 2026-09-11 19:10

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 5 — Sensors resistius · Lectura prèvia](#unitat-5-sensors-resistius-lectura-prèvia)
2. [Sensors moduladors, fonaments físics i model general](#sensors-moduladors-fonaments-físics-i-model-general)
   - [1 Sensors generadors i moduladors](#1-sensors-generadors-i-moduladors)
   - [2 Fonaments físics](#2-fonaments-físics)
   - [3 Model general i excitació](#3-model-general-i-excitació)
   - [4 Panorama de la unitat](#4-panorama-de-la-unitat)
3. [Detectors de temperatura resistius (RTD)](#detectors-de-temperatura-resistius-rtd)
   - [1 Principi de funcionament](#1-principi-de-funcionament)
   - [2 Model resistència-temperatura](#2-model-resistència-temperatura)
   - [3 Valors nominals, marge i intercanviabilitat](#3-valors-nominals-marge-i-intercanviabilitat)
   - [4 Construcció i aplicacions](#4-construcció-i-aplicacions)
4. [Autoescalfament, excitació i resposta dinàmica](#autoescalfament-excitació-i-resposta-dinàmica)
   - [1 Coeficient de dissipació tèrmica](#1-coeficient-de-dissipació-tèrmica)
   - [2 Potència dissipada segons l'excitació](#2-potència-dissipada-segons-lexcitació)
   - [3 Com limitar-lo](#3-com-limitar-lo)
   - [4 Resposta dinàmica](#4-resposta-dinàmica)
5. [Termistors NTC: models i linealització](#termistors-ntc-models-i-linealització)
   - [1 Model exponencial](#1-model-exponencial)
   - [2 Linealització analògica](#2-linealització-analògica)
6. [Termistors: construcció, PTC i aplicacions](#termistors-construcció-ptc-i-aplicacions)
   - [1 Fabricació i formats de les NTC](#1-fabricació-i-formats-de-les-ntc)
   - [2 NTC enfront de RTD](#2-ntc-enfront-de-rtd)
   - [3 Aplicacions de les NTC](#3-aplicacions-de-les-ntc)
   - [4 Termistors PTC](#4-termistors-ptc)
7. [Sensors piezoresistius i galgues extensiomètriques](#sensors-piezoresistius-i-galgues-extensiomètriques)
   - [1 Tensió mecànica i deformació](#1-tensió-mecànica-i-deformació)
   - [2 El factor de galga](#2-el-factor-de-galga)
   - [3 Construcció i paràmetres geomètrics](#3-construcció-i-paràmetres-geomètrics)
   - [4 Temperatura, rosetes i muntatge](#4-temperatura-rosetes-i-muntatge)
   - [5 Aplicacions](#5-aplicacions)
8. [Magnetoresistències](#magnetoresistències)
   - [1 Les tres famílies](#1-les-tres-famílies)
   - [2 Magnetoresistència anisòtropa (AMR)](#2-magnetoresistència-anisòtropa-amr)
   - [3 Magnetoresistència gegant (GMR)](#3-magnetoresistència-gegant-gmr)
   - [4 Temperatura i aplicacions](#4-temperatura-i-aplicacions)
9. [Fotoresistències, higròmetres resistius i criteris de selecció](#fotoresistències-higròmetres-resistius-i-criteris-de-selecció)
   - [1 Fotoresistències (LDR)](#1-fotoresistències-ldr)
   - [2 Higròmetres resistius](#2-higròmetres-resistius)
   - [3 Recapitulació de la unitat](#3-recapitulació-de-la-unitat)
10. [Entrenament V/F · Unitat 5: Sensors resistius](#entrenament-vf-unitat-5-sensors-resistius)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_Unitat5_Index -->

# Unitat 5 — Sensors resistius · Lectura prèvia

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 5 — Sensors resistius

Materials de lectura prèvia · dedicació total estimada: 64 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents **substitueixen els apunts** i contenen tot el que cal per preparar la unitat.

Llegeix els vuit documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor.

### [1. Sensors moduladors, fonaments físics i model general](#sensors-moduladors-fonaments-físics-i-model-general)

Sensors generadors i moduladors; classificació per la impedància Z=R+jX; resistius enfront de reactius; R=rho·l/A i la descomposició de la variació relativa; efecte de Poisson i dilatació tèrmica; sigma=n·q·mu i el contrast entre metalls i semiconductors; model general R(x)=R0[1+g(x-x0)] i especificacions del fabricant; estratègies d'excitació i panorama de les famílies.

*⏱️ Dedicació estimada: 7 min*

### [2. Detectors de temperatura resistius (RTD)](#detectors-de-temperatura-resistius-rtd)

Mecanisme de la resistivitat en un metall; platí, coure i níquel; model polinòmic i Callendar-Van Dusen segons IEC 60751; model lineal i error de linealització (0,382 °C entre 0 i 100 °C); Pt-100, Pt-500 i Pt-1000; sensibilitat absoluta i relativa; classes d'exactitud i intercanviabilitat; construccions de pel·lícula metàl·lica i de fil enrotllat.

*⏱️ Dedicació estimada: 8 min*

### [3. Autoescalfament, excitació i resposta dinàmica](#autoescalfament-excitació-i-resposta-dinàmica)

Coeficient de dissipació tèrmica i error sistemàtic d'autoescalfament; potència dissipada amb corrent constant, tensió constant, divisor de tensió i divisor de corrent; la condició R=Rdiv; exemple resolt amb Pt-100; estratègies de reducció (corrent baix, excitació polsada, dissipació, disseny del condicionament); model tèrmic de primer ordre i constant de temps.

*⏱️ Dedicació estimada: 8 min*

### [4. Termistors NTC: models i linealització](#termistors-ntc-models-i-linealització)

NTC i PTC; model exponencial de dos paràmetres amb temperatures en kelvin; significat de beta; exemple resolt; coeficient de temperatura local; equació de Steinhart-Hart; linealització analògica amb resistència en paral·lel, amb la deducció completa del punt d'inflexió; linealització amb divisor de tensió i compromís entre linealitat i sensibilitat.

*⏱️ Dedicació estimada: 8 min*

### [5. Termistors: construcció, PTC i aplicacions](#termistors-construcció-ptc-i-aplicacions)

Fabricació ceràmica per sinterització i origen de la dispersió de R0 i beta; formats de forat passant i SMD; criteris de tria; comparació NTC-RTD; aplicacions de mesura, detecció de nivell i flux per autoescalfament, i limitació de transitoris de corrent; posistors i silistors; proteccions tèrmiques i circuits de desmagnetització.

*⏱️ Dedicació estimada: 7 min*

### [6. Sensors piezoresistius i galgues extensiomètriques](#sensors-piezoresistius-i-galgues-extensiomètriques)

Tensió mecànica i deformació unitària; zones elàstica, plàstica i de fallida; llei de Hooke i efecte de Poisson; deducció del factor de galga k=1+2nu+k1; galgues metàl·liques (k entre 2 i 3) i semiconductores (k entre 50 i 150); sensibilitat longitudinal i transversal; rosetes; compensació tèrmica; muntatge i adhesius; cèl·lules de càrrega, acceleròmetres i transductors de pressió.

*⏱️ Dedicació estimada: 8 min*

### [7. Magnetoresistències](#magnetoresistències)

AMR, GMR i TMR: mecanismes, sensibilitats i complexitat; permalloy i model de l'AMR bàsica; pèrdua d'informació de signe; estructura barber pole; dispersió dependent de l'espín i correspondència antiparal·lel-resistència alta; camp de saturació; compensació tèrmica amb ponts; posició sense contacte, encoders, lectura de discos durs i mesura de corrent amb aïllament galvànic.

*⏱️ Dedicació estimada: 8 min*

### [8. Fotoresistències, higròmetres resistius i criteris de selecció](#fotoresistències-higròmetres-resistius-i-criteris-de-selecció)

LDR: efecte fotoelèctric intern, condició sobre l'energia del fotó, resposta espectral segons material, elèctrodes interdigitats, llei de potència empírica i limitacions. Higròmetres resistius: conducció iònica, excitació en alterna, calibratge i compensació de temperatura, histèresi i contaminació. Recapitulació de la unitat, compromisos entre famílies, criteris de selecció i tendències.

*⏱️ Dedicació estimada: 10 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

<!-- FIN CAPÍTULO: 00_Unitat5_Index -->

---

<!-- INICIO CAPÍTULO: 01_Unitat5_Sensors_moduladors_i_model_general -->

# Sensors moduladors, fonaments físics i model general

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 1 de 8

# Sensors moduladors, fonaments físics i model general

Dedicació estimada: 7 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir sensors generadors i moduladors, i els resistius dels reactius a partir de  $Z=R+jX$
>.
> - Descompondre una variació de resistència en contribucions de resistivitat, longitud i secció.
> - Explicar, amb  $\sigma=n\,q\,\mu$
>, per què metalls i semiconductors responen de manera oposada a la temperatura.
> - Aplicar el model general  $R(x)=R_0[1+g(x-x_0)]$
> i reconèixer les estratègies d'excitació.

## 1 Sensors generadors i moduladors

- **Generadors**: converteixen energia associada al mesurand en energia elèctrica i no requereixen alimentació externa (termoparells, piezoelèctrics, cèl·lules fotovoltaiques). Unitat 9.
- **Moduladors**: el mesurand no genera cap força electromotriu, sinó que modifica un *paràmetre elèctric passiu* —resistència, capacitat, inductància— que cal excitar per observar-ne la variació.

Els d'aquesta unitat són tots moduladors: **un sensor resistiu no lliura cap senyal per si mateix**; sense excitació, una Pt-100 a 80 °C i una a 0 °C són indistingibles des dels terminals.

$$
Z = R + jX \qquad (5.1)
$$

$$
Z(x) = R(x) + jX(x) \qquad (5.2)
$$

La part imaginària recull capacitats i inductàncies, i en un sensor modulador la impedància depèn del mesurand  $x$
. Segons quina part afecti:

- **Sensors resistius**: afecta sobretot  $R$
; la part imaginària és petita o constant. Es modelen com una resistència variable i sovint n'hi ha prou amb models en contínua i la llei d'Ohm.
- **Sensors reactius**: afecta sobretot  $X$
   —capacitius o inductius. Requereixen excitació alterna i condicionament que tingui en compte el desfasament entre corrent i tensió (unitats 7 i 8).

> [!WARNING] **Matís important**
>
> Que un sensor resistiu admeti model en contínua no vol dir que la seva reactància sigui nul·la: tot dispositiu real té capacitats i inductàncies paràsites. Vol dir que, en les condicions habituals, són negligibles davant de  $R$
>. Quan no ho són —cablejats llargs, freqüències altes, sensors d'humitat excitats en alterna— l'anàlisi en alterna torna a ser necessària.

![Fotografies de cinc sensors moduladors: termistor, galga extensiomètrica, fotoresistència, acceleròmetre capacitiu i sensor inductiu de distància](assets/01_Unitat5_Sensors_moduladors_i_model_general_img_1.png)

*Figura: Figura 5.1 Exemples de sensors moduladors. De dalt a baix i d'esquerra a dreta: un termistor (mesura econòmica de temperatura), una galga extensiomètrica (la resistència canvia en estirar-se o comprimir-se), una fotoresistència (la resistència està modulada per la intensitat de fotons incidents dins d'una banda de longituds d'ona), un acceleròmetre capacitiu per a mesura de vibracions i un sensor inductiu de distància sense contacte. Els tres primers són resistius; els dos darrers, reactius.*

## 2 Fonaments físics

$$
R = \rho\,\frac{l}{A} \qquad (5.3)
$$

$$
\frac{\Delta R}{R} \approx \frac{\Delta \rho}{\rho} + \frac{\Delta l}{l} - \frac{\Delta A}{A} \qquad (5.4)
$$

La resistència creix amb la resistivitat  $\rho$
 (en  $\Omega\cdot\mathrm{m}$
) i amb la longitud, i decreix amb la secció: el mesurand pot actuar sobre la **geometria** o sobre la **resistivitat**, i els tres termes de (5.4) poden coexistir.

### Deformació mecànica

Sota una tensió mecànica  $\sigma = F/A$
 apareix una **deformació unitària**  $\varepsilon = \Delta l/l_0$
, lligada a la tensió en zona elàstica per la llei de Hooke:

$$
\sigma = E\,\varepsilon \qquad (5.5)
$$

$\sigma$
 s'expressa en pascals i  $\varepsilon$
 és **adimensional**. En estirar-se, la secció disminueix per **efecte de Poisson**:

$$
\frac{\Delta A}{A} \approx -2\nu\varepsilon \qquad (5.6)
$$

$$
\frac{\Delta R}{R} \approx (1+2\nu)\,\varepsilon \qquad (5.7)
$$

Amb  $\nu \approx 0{,}3$
 el factor geomètric val uns 1,6: en allargar-se la peça, la resistència de la galga augmenta. Als sensors piezoresistius reals s'hi suma una contribució de resistivitat, i el conjunt es recull en el *factor de galga* (document 6).

### Dilatació tèrmica

$$
\frac{\Delta l}{l_0} = \alpha\,\Delta T \qquad (5.8)
$$

$$
\frac{\Delta R}{R} \approx \alpha\Delta T - 2\alpha\Delta T = -\alpha\,\Delta T \qquad (5.9)
$$

Si l'expansió és isòtropa la secció creix uns  $2\alpha\Delta T$
, de manera que amb  $\rho$
 constant la resistència *disminuiria* lleugerament en escalfar-se. L'efecte és molt petit i queda dominat pel canvi de resistivitat, de signe contrari i molt més gran: **en un RTD el mecanisme dominant és la resistivitat, no la geometria**.

### Origen microscòpic de la resistivitat

$$
\sigma = n\,q\,\mu \qquad (5.10)
$$

Amb  $\rho = 1/\sigma$
 i  $n$
 densitat de portadors,  $q$
 càrrega elemental i  $\mu$
 mobilitat, el mesurand pot canviar *quants* portadors hi ha o *com de fàcilment* es mouen.

**En un metall** la densitat d'electrons lliures és molt elevada i pràcticament constant; el que canvia és la mobilitat: en pujar la temperatura la xarxa vibra més, els electrons es dispersen més i  $\rho$
 augmenta. En resulta un **coeficient positiu**, quasi lineal en marges moderats:

$$
R(T) \approx R_0\left[1+\alpha\,(T-T_0)\right] \qquad (5.11)
$$

És el principi dels RTD de platí. La resistivitat d'un metall també canvia amb la deformació i amb camps magnètics en materials anisòtrops.

**En un semiconductor**,  $n$
 i  $\mu$
 varien molt amb la temperatura, la llum o altres estímuls: en escalfar-se, més electrons salten a la banda de conducció i  $n$
 creix marcadament. Això explica els **termistors NTC** (coeficient negatiu), les **fotoresistències** (la llum promou electrons i la resistència pot baixar diversos ordres de magnitud), les **magnetoresistències** (el camp modifica la magnetització i la dispersió) i els **higròmetres resistius** (l'aigua absorbida crea camins iònics). En tots, el mesurand actua sobretot sobre  $n$
 i dona variacions grans i marcadament **no lineals**: els mecanismes més sensibles solen ser els menys lineals.

## 3 Model general i excitació

$$
R(x) = R_0\left[1+g(x-x_0)\right] \qquad (5.12)
$$

amb  $R_0$
 la resistència per a un valor de referència  $x_0$
 i  $g(0)=0$
. **La funció  $g$
 no ha de ser necessàriament lineal**: pot ser una recta, un polinomi (RTD d'alta exactitud), una exponencial (NTC) o una llei de potència (LDR). Els fabricants especifiquen la **resistència nominal** i el **punt de referència** —que no és universal: una Pt-100 s'especifica a 0 °C i un NTC, a 25 °C—, la **funció de resposta** amb coeficients i toleràncies, i el **marge de mesura**, fora del qual el model deixa de descriure el sensor i pot haver-hi dany permanent. La **inversa**  $x = f^{-1}(R)$
 converteix la resistència llegida en el valor de la magnitud física.

> [!WARNING] **Escollir el model: un criteri de sistema**
>
> Un model més complex no millora automàticament la mesura. Si la incertesa del condicionament, el convertidor i el calibratge és molt més gran que l'error de linealització, passar d'un model lineal a un de polinòmic només afegeix càlcul. El criteri és la coherència amb l'exactitud del *sistema complet* (unitat 2), i el mateix val per a la classe d'exactitud del sensor.

Les estratègies d'excitació (unitat 6) es fonamenten en la llei d'Ohm: amb **corrent constant**,  $V = I\,R(x)$
, la tensió és proporcional a la resistència; amb **tensió constant**,  $I = V/R(x)$
, el corrent és *inversament* proporcional; i el **divisor de tensió** és la base del **pont de Wheatstone**, que s'utilitza amb galgues, RTD i magnetoresistències. Les tres determinen la sensibilitat, la linealitat i la **potència dissipada dins del sensor** (document 3).

## 4 Panorama de la unitat

Les famílies es diferencien pel **mecanisme físic** que fa variar la resistència, i cadascuna té la seva pròpia llei  $R(x)$
.

| Família | Mesurand | Mecanisme dominant | Forma de  $R(x)$ | Doc. |
|:--- |:--- |:--- |:--- |:--- |
| RTD (Pt-100, Pt-1000) | Temperatura | Mobilitat en un metall | Polinòmica, quasi lineal | 2 i 3 |
| Termistors NTC | Temperatura | Densitat de portadors en un semiconductor | Exponencial | 4 i 5 |
| Termistors PTC | Temperatura | Transició de fase ceràmica o silici dopat | Abrupta o suau segons el tipus | 5 |
| Galgues i piezoresistències | Deformació, força, pressió, acceleració | Geometria i piezoresistivitat | Lineal en zona elàstica | 6 |
| Magnetoresistències (AMR, GMR, TMR) | Camp magnètic, posició, corrent | Dispersió dependent de la magnetització i de l'espín | No lineal, amb saturació | 7 |
| Fotoresistències (LDR) | Il·luminació | Fotogeneració de portadors | Llei de potència empírica | 8 |
| Higròmetres resistius | Humitat relativa | Conducció iònica en material higroscòpic | Fortament no lineal | 8 |

Un avís que val per a totes: **la temperatura és una magnitud d'influència gairebé universal**. Una galga, una magnetoresistència, una LDR o un higròmetre canvien de resistència amb la temperatura encara que no sigui el mesurand, i distingir les dues contribucions —amb configuracions diferencials, sensors auxiliars o calibratge— és un problema recurrent al llarg de la unitat.

> [!TIP] **Síntesi**
>
> Els sensors resistius són *moduladors*: necessiten excitació externa perquè el mesurand modifica un paràmetre passiu. Dins de  $Z=R+jX$
> n'afecten sobretot la part real. La resistència  $R=\rho l/A$
> varia per geometria, per resistivitat o per tots dos efectes;  $\sigma=nq\mu$
> explica el coeficient positiu i quasi lineal dels metalls i les variacions grans i no lineals dels semiconductors. El model  $R(x)=R_0[1+g(x-x_0)]$
>, amb  $g$
> no necessàriament lineal, es completa amb resistència nominal, punt de referència, funció de resposta i marge.

[2. Detectors de temperatura resistius (RTD) →](#detectors-de-temperatura-resistius-rtd)

---

<!-- FIN CAPÍTULO: 01_Unitat5_Sensors_moduladors_i_model_general -->

---

<!-- INICIO CAPÍTULO: 02_Unitat5_RTD -->

# Detectors de temperatura resistius (RTD)

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 2 de 8

# Detectors de temperatura resistius (RTD)

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar per què la resistència d'un metall augmenta amb la temperatura i per què el terme geomètric és negligible.
> - Aplicar el model de Callendar-Van Dusen i quantificar l'error de l'aproximació lineal.
> - Relacionar resistència nominal, sensibilitat absoluta i sensibilitat relativa en Pt-100, Pt-500 i Pt-1000.
> - Interpretar les classes d'exactitud de la IEC 60751, la intercanviabilitat i les dues construccions típiques.

Un **RTD** (*Resistive Temperature Detector*) és un sensor de temperatura basat en el canvi de resistivitat d'un conductor metàl·lic, habitualment platí. La **IEC 60751** en fixa models, coeficients i classes d'exactitud.

## 1 Principi de funcionament

En un metall, en pujar la temperatura els ions de la xarxa vibren més, els electrons pateixen més col·lisions amb aquestes vibracions (fonons), cau la mobilitat i **augmenta la resistivitat**. El canvi dominant és el de  $\rho$
: els geomètrics per dilatació són molt menors i de signe contrari (equació 5.9). En un RTD el mecanisme dominant no és, doncs, ni la dilatació ni la generació de portadors, que és el que passa en un semiconductor i dona el comportament contrari dels NTC.

$$
R(T) = f(T) \qquad (5.13)
$$

és una funció suau i quasi lineal en marges moderats. Com tot sensor modulador, cal excitar-lo per llegir-lo.

![Símbol d'un RTD: rectangle resistiu creuat per una línia diagonal recta amb la indicació t minúscula o](assets/02_Unitat5_RTD_img_1.png)

*Figura: Figura 5.2 Símbol d'un RTD. Al símbol d'una resistència s'hi superposa una línia recta diagonal creixent d'esquerra a dreta, que indica que l'increment de resistència amb la temperatura és raonablement lineal i amb coeficient positiu. La marca $t^{o}$
indica que el sensor canvia amb la temperatura.*

El **platí** és el material de referència: alta estabilitat química i mecànica, puresa molt elevada, coeficient constant i ben definit i marge ampli (uns −200 a 800 °C). El **coure** és barat, lineal, però de marge reduït i sensible a l'oxidació; el **níquel**, barat i de coeficient elevat però amb pitjor linealitat. Cap dels dos supera el platí en estabilitat o exactitud metrològica: l'avantatge decisiu del platí és la puresa assolible, que fa que sensors del mateix model tinguin coeficients molt similars i permet models normalitzats.

## 2 Model resistència-temperatura

$$
R(T) = R_0\left[1+\alpha_1\Delta T+\alpha_2(\Delta T)^2+\cdots+\alpha_n(\Delta T)^n\right] \qquad (5.14)
$$

amb  $\Delta T = T-T_0$
 i  $T_0$
 habitualment 0 °C; els coeficients es determinen per calibratge amb ajust per mínims quadrats. A la pràctica s'usen models compactes: Callendar-Van Dusen i la seva aproximació lineal.

La **Pt-100** té  $R_0 = 100\ \Omega$
 **a 0 °C** —no a 25 °C, que és el punt de referència habitual dels termistors—, prou baix per limitar la potència dissipada i prou alt per donar caigudes de tensió mesurables amb corrents modestos. El model normalitzat és, per a  $T \geq 0$
 °C,

$$
R(T) = R_0\left[1+A\,T+B\,T^2\right] \qquad (5.15)
$$

i per a  $T < 0$
 °C,

$$
R(T) = R_0\left[1+A\,T+B\,T^2+C\,(T-100)\,T^3\right] \qquad (5.16)
$$

amb  $T$
 en graus Celsius.

| Coeficient | Valor | Aplicabilitat |
|:--- |:--- |:--- |
| $R_0$ | 100 Ω a 0 °C | Tot el marge |
| $A$ | $3{,}9083\times10^{-3}\ ^\circ\mathrm{C}^{-1}$ | Tot el marge |
| $B$ | $-5{,}775\times10^{-7}\ ^\circ\mathrm{C}^{-2}$ | Tot el marge |
| $C$ | $-4{,}183\times10^{-12}\ ^\circ\mathrm{C}^{-4}$ | Només per a  $T<0$   °C |

El terme **quadràtic hi és sempre** — $B$
 és petit i negatiu, i és el que corba la característica per sota de la recta— i el **cúbic amb  $C$
 només s'aplica per sota de 0 °C**: per a temperatures positives, Callendar-Van Dusen és un polinomi de segon grau.

### Model lineal i error de linealització

$$
R(T) \approx R_0\left(1+\alpha\,T\right) \qquad (5.17)
$$

amb  $\alpha \approx 0{,}00385\ ^\circ\mathrm{C}^{-1}$
: la resistència augmenta un 0,385 % per kelvin, és a dir 100 Ω a 0 °C i uns 138,5 Ω a 100 °C, amb una sensibilitat de **0,385 Ω/°C**.

![Gràfic de resistència de Pt-100 enfront de temperatura de 0 a 200 graus, amb la corba de Callendar-Van Dusen lleugerament per sota de la recta a temperatures altes](assets/02_Unitat5_RTD_img_2.png)

*Figura: Figura 5.3 Comparació entre el model de Callendar-Van Dusen i el model lineal per a una Pt-100 entre 0 °C i 200 °C. A temperatures elevades, Callendar-Van Dusen prediu resistències inferiors a les del model lineal.*

![Dues corbes: diferència de resistència entre models i error equivalent en graus Celsius, positiu entre 0 i 100 graus i negatiu per sobre](assets/02_Unitat5_RTD_img_3.png)

*Figura: Figura 5.4 Diferència en resistència i en temperatura entre el model de Callendar-Van Dusen i el model lineal. L'error referit a l'entrada, en graus, s'obté dividint la diferència de resistència per la sensibilitat del sensor, aproximadament $R_0\alpha$
.*

Entre 0 i 100 °C l'error és **positiu**, **nul a 0 i a 100 °C** —on les corbes es creuen— i màxim cap a la meitat del marge, amb **0,382 °C**; per sobre de 100 °C canvia de signe i creix fins a prop de 3 °C a 200 °C. El model lineal serveix, doncs, en marges estrets amb errors admissibles de 0,3-0,5 °C; el quadràtic els redueix a dècimes de grau entre −50 i 250 °C; i per a metrologia exigent o temperatures negatives cal la forma completa amb  $C$
. La tria és un criteri de sistema: si l'A/D introdueix una incertesa equivalent a 0,1 °C, un model amb incertesa teòrica de 0,01 °C no millora el resultat.

## 3 Valors nominals, marge i intercanviabilitat

Existeixen també la **Pt-500** i la **Pt-1000** (500 i 1000 Ω a 0 °C). Totes comparteixen el mateix *coeficient de temperatura relatiu*, perquè el material és el mateix; el que escala amb  $R_0$
 és la *sensibilitat absoluta*: una Pt-1000 té uns 3,85 Ω/°C, deu vegades la de la Pt-100, amb el mateix 0,385 %/K. Les nominals altes convenen quan la **resistència dels cables** podria falsejar la mesura —tant més important com més baixa és la nominal, i rellevant en una Pt-100 amb cables llargs— i quan es volen corrents molt baixos. La compensació del cablejat (tres i quatre fils) pertany a la unitat 6.

El **marge** en platí va de −200 a 800 °C en sensors de laboratori i fins a uns 300 °C en molts RTD industrials; els de coure i níquel, de −50 a 150-300 °C. Enfront dels **termoparells**, els RTD tenen més sensibilitat (0,385 Ω/°C davant de poques desenes de µV/°C) i millor linealitat; enfront dels **termistors NTC**, coeficients molt repetibles però *sensibilitat relativa menor* i preu superior: no es trien per tenir resposta abrupta —això ho ofereix una NTC— sinó per la seva previsibilitat. L'error global combina classe d'exactitud, error de model, condicionament, autoescalfament i convertidor.

La IEC 60751 especifica  $R_0$
, els coeficients de referència, diverses **classes d'exactitud** (A, B, etc.) amb els seus límits d'error i els tipus de construcció mínims: formalitza i acota les toleràncies en lloc d'eliminar-les. La conseqüència és la **intercanviabilitat** —dos Pt-100 de la mateixa classe se substitueixen sense recalibrar completament el sistema—, que depèn de la classe d'exactitud i de la proximitat del sensor real a la corba normalitzada. Contrasta amb molts NTC i amb les LDR, on els paràmetres varien significativament entre dispositius i sovint cal calibratge individual.

## 4 Construcció i aplicacions

![Fotografies d'un RTD de pel·lícula metàl·lica amb pista serpentejant sobre substrat ceràmic i d'un RTD de fil enrotllat sobre suport cilíndric](assets/02_Unitat5_RTD_img_4.png)

*Figura: Figura 5.5 RTD de pel·lícula metàl·lica (esquerra) i de fil enrotllat (dreta).*

En un **RTD de pel·lícula metàl·lica** (*thin film*) el platí es diposita en capa fina sobre un substrat ceràmic, amb la pista en serpentina encapsulada amb vidre o resina: dimensions reduïdes, integrable sobre superfícies fins i tot conductores, **resposta ràpida** per la poca massa tèrmica —constants de l'ordre d'1 s— i cost moderat. En un **RTD de fil enrotllat** (*wire-wound*) un fil de platí molt fi s'enrotlla sobre un suport ceràmic recobert de massa ceràmica o acer inoxidable: **més lent**, amb constants de diversos segons, molt **robust** i més car.

> [!WARNING] **Quin dels dos és més ràpid**
>
> El que determina la constant de temps no és el gruix del fil sinó la *massa tèrmica del conjunt* —fil, suport i encapsulat— i la qualitat del contacte tèrmic amb el medi. Per això, amb muntatges comparables, el de pel·lícula metàl·lica sol ser el més ràpid; però un sensor de pel·lícula dins d'una beina industrial gruixuda pot respondre més lentament que un fil enrotllat nu.

En processos químics, alimentaris o farmacèutics —reactors, tancs, canonades i forns, amb marges de −50 a 250 °C i exactituds de dècimes de grau— la solució típica és un fil enrotllat en vareta d'acer inoxidable amb rosca normalitzada. En laboratoris, cambres climàtiques i climatització destaquen els de pel·lícula metàl·lica per rapidesa i facilitat d'integració; la seva estabilitat a llarg termini permet distribuir-ne diversos per controlar la uniformitat de temperatura.

> [!TIP] **Síntesi**
>
> Un RTD mesura temperatura per l'augment de resistivitat d'un metall, degut a la caiguda de mobilitat; la dilatació és negligible i de signe contrari. La Pt-100 té 100 Ω a 0 °C i 0,385 Ω/°C; les Pt-500 i Pt-1000 escalen la sensibilitat absoluta amb el mateix coeficient relatiu de 0,385 %/K. Callendar-Van Dusen és quadràtic per a  $T\geq 0$
> °C i afegeix un terme cúbic només per sota de 0 °C; el model lineal dona un error màxim de 0,382 °C entre 0 i 100 °C i uns 3 °C a 200 °C. Les classes de la IEC 60751 sustenten una intercanviabilitat superior a la de termistors i LDR. La pel·lícula metàl·lica és ràpida i econòmica; el fil enrotllat, lent i robust.

[← 1. Sensors moduladors, fonaments físics i model general](#sensors-moduladors-fonaments-físics-i-model-general)[3. Autoescalfament, excitació i resposta dinàmica →](#autoescalfament-excitació-i-resposta-dinàmica)

---

<!-- FIN CAPÍTULO: 02_Unitat5_RTD -->

---

<!-- INICIO CAPÍTULO: 03_Unitat5_Autoescalfament_i_resposta_dinamica -->

# Autoescalfament, excitació i resposta dinàmica

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 3 de 8

# Autoescalfament, excitació i resposta dinàmica

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar per què un sensor resistiu s'escalfa a si mateix i quin tipus d'error introdueix.
> - Utilitzar el coeficient de dissipació tèrmica  $\delta$
> per estimar l'increment de temperatura.
> - Calcular la potència dissipada en les quatre estratègies d'excitació i localitzar-ne el màxim.
> - Modelar la resposta tèrmica com un sistema de primer ordre.

Per mesurar la resistència d'un sensor cal fer-hi passar corrent, de manera que s'hi dissipa potència i s'escalfa per sobre del medi. És l'**autoescalfament**, un **error sistemàtic** i no soroll aleatori: sempre té el mateix signe i no es cancel·la promitjant lectures. Es descriu aquí amb RTD, però afecta igualment els termistors i qualsevol sensor resistiu alimentat elèctricament.

## 1 Coeficient de dissipació tèrmica

$$
T_{\text{sensor}} = T_{\text{ambient}} + \frac{P_{\text{sensor}}}{\delta} \qquad (5.18)
$$

El **coeficient de dissipació tèrmica**  $\delta$
, en mW/K, indica quanta potència cal dissipar perquè el sensor pugi 1 K per sobre del medi. Les unitats són de potència dividida per temperatura, i el valor depèn sobretot del sensor, del seu encapsulat i del medi, no només del circuit; el fabricant pot donar-ne la inversa, la resistència tèrmica  $R_\theta = 1/\delta$
 en K/mW.

La dependència del medi té un ordre clar: **en buit** la dissipació és només per radiació i és el cas més desfavorable; **en aire quiet** la convecció és limitada i l'autoescalfament important; **en líquids** la transferència és molt millor i l'autoescalfament menor. **Com millor és la transferència tèrmica, menys autoescalfament**: si el sistema es dimensiona per a aire quiet, en immersió l'error serà encara menor.

## 2 Potència dissipada segons l'excitació

![Quatre esquemes: sensor excitat amb font de corrent, sensor amb font de tensió, divisor de tensió amb resistència fixa i sensor en paral·lel amb resistència fixa excitat per font de corrent](assets/03_Unitat5_Autoescalfament_i_resposta_dinamica_img_1.png)

*Figura: Figura 5.6 Estratègies d'excitació de sensors resistius. A dalt a l'esquerra, corrent constant; a dalt a la dreta, tensió constant; a baix a l'esquerra, divisor de tensió amb resistència fixa; a baix a la dreta, divisor de corrent.*

$$
P_{\text{sensor}} = I^2 R \qquad (5.19)
$$

$$
P_{\text{sensor}} = \frac{V^2}{R} \qquad (5.20)
$$

Amb **corrent constant** (5.19) la potència és proporcional al **quadrat del corrent** i a la *primera* potència de la resistència —duplicar el corrent la multiplica per quatre—, de manera que en un RTD el pitjor cas és a la temperatura més alta del marge. Amb **tensió constant** (5.20) és **inversament** proporcional a la resistència i, per tant, màxima al valor *mínim* de  $R$
: en un RTD, a la temperatura més baixa. Les dues estratègies situen el pitjor cas en extrems oposats del rang.

Amb **divisor de tensió**, el sensor en sèrie amb una resistència fixa i alimentació  $V$
:

$$
V_R = V\,\frac{R}{R+R_{\text{div}}} \qquad (5.21)
$$

$$
P_{\text{sensor}} = \frac{V^2 R}{(R+R_{\text{div}})^2} \qquad (5.22)
$$

Aquesta expressió no és monòtona: s'anul·la tant per a  $R\to 0$
 com per a  $R\to\infty$
 i té un màxim entremig. Derivant respecte de  $R$
 i imposant la condició de màxim,

$$
R = R_{\text{div}} \qquad (5.23)
$$

L'error màxim es dona, per tant, a la temperatura on la resistència del sensor **iguala la resistència fixa del divisor**: és  $R_{\text{div}}$
 qui fixa on cau el pitjor cas. Si dins del marge no hi ha cap temperatura amb  $R=R_{\text{div}}$
, el màxim cau a l'extrem més proper: en una Pt-100 amb  $R_{\text{div}}=100\ \Omega$
 i rang 0-100 °C, a 0 °C; amb  $R_{\text{div}}=200\ \Omega$
, a 100 °C, perquè els 138,5 Ω són més propers a 200 Ω.

Amb **divisor de corrent**, el sensor en paral·lel amb  $R_{\text{div}}$
 i excitació de corrent constant,

$$
P_{\text{sensor}} = I^2\,\frac{R_{\text{div}}^2\,R}{(R+R_{\text{div}})^2} \qquad (5.24)
$$

que derivant dona la mateixa condició  $R=R_{\text{div}}$
: els dos divisors comparteixen el criteri.

> [!EXAMPLE] **Exemple resolt: autoescalfament d'una Pt-100**
>
> Una Pt-100 en aire quiet, amb  $\delta = 5\ \mathrm{mW/K}$
>, s'alimenta amb un corrent constant d'1 mA. Quin error per autoescalfament s'introdueix a 0 °C? I amb 5 mA?
>
> 1. Potència amb 1 mA. A 0 °C,  $R = R_0 = 100\ \Omega$
>, i per (5.19)  $P = I^2R = 100\ \mu\mathrm{W} = 0{,}1\ \mathrm{mW}$
>.
> 2. Increment de temperatura. Per (5.18),  $\Delta T = P/\delta = 0{,}1/5 = 0{,}02\ \mathrm{K}$
>: negligible en la major part d'aplicacions.
> 3. Amb 5 mA. Com que  $P\propto I^2$
>, la potència es multiplica per 25:  $P = 2{,}5\ \mathrm{mW}$
> i  $\Delta T = 0{,}5\ \mathrm{K}$
>, ja gens negligible si es busquen dècimes de grau.

## 3 Com limitar-lo

- **Reduir el corrent de mesura**: l'impacte és quadràtic, de manera que dividir-lo per dos redueix l'autoescalfament a la quarta part. El límit el posa el soroll.
- **Excitació polsada**: fer circular corrent només durant el temps mínim de lectura *redueix* l'escalfament mitjà respecte d'una excitació contínua equivalent, sempre que el pols sigui curt comparat amb la dinàmica tèrmica; si és llarg, el sensor arriba igualment a l'equilibri.
- **Millorar la dissipació**, amb un encapsulat de  $\delta$
   més gran: contacte directe amb líquids o amb metalls d'alta conductivitat tèrmica.
- **Dissenyar el condicionament** perquè el màxim de potència caigui fora del marge de mesura o en una zona menys sensible a l'error.

Cal avaluar sempre  $P_{\text{sensor}}/\delta$
 en les condicions més desfavorables: la comprovació és barata i evita errors sistemàtics difícils de diagnosticar, perquè no es manifesten com a soroll sinó com una desviació estable.

## 4 Resposta dinàmica

$$
\tau\,\frac{dT_{\text{sensor}}}{dt} + T_{\text{sensor}} = T_{\text{medi}} \qquad (5.25)
$$

La resposta temporal la governen la capacitat tèrmica del sensor i la resistència tèrmica cap al medi, i s'aproxima per un **sistema de primer ordre**: davant d'un salt, el sensor s'hi acosta exponencialment amb la **constant de temps tèrmica**  $\tau$
. No és instantània encara que la resistència elèctrica canviï sense retard: el retard l'introdueix la transferència de calor. Amb encapsulats de diverses capes s'assembla més a un segon ordre sobresmorteït.

$\tau$
 **no és una propietat del material resistiu**: depèn de l'encapsulat, del muntatge i de la transferència de calor amb el medi. És gran en aire quiet, menor amb flux d'aire, molt menor en líquids i curta si el sensor està adherit a un metall. Els RTD de pel·lícula poden estar per sota d'1 s i els de fil enrotllat encapsulats, en diversos segons en aire. Sovint —però no sempre— el procés evoluciona molt més lentament que el sensor i la limitació hi és; en canvis ràpids en fluids, en canvi, la dinàmica del sensor pot ser el factor limitant. El pols d'excitació ha de ser prou llarg perquè la lectura estabilitzi i prou curt perquè el sensor no s'escalfi.

> [!TIP] **Síntesi**
>
> L'autoescalfament és un error sistemàtic de signe conegut que afecta tots els sensors resistius. El coeficient  $\delta$
> relaciona potència i increment de temperatura,  $T_{\text{sensor}}=T_{\text{ambient}}+P/\delta$
>, i depèn de l'encapsulat i del medi: pitjor en buit, dolent en aire quiet, millor en líquids. La potència val  $I^2R$
> amb corrent constant (màxima a  $R$
> màxima) i  $V^2/R$
> amb tensió constant (màxima a  $R$
> mínima); en tots dos divisors és màxima quan  $R=R_{\text{div}}$
>. Es controla reduint el corrent, excitant per polsos curts i millorant la dissipació. Dinàmicament és un sistema de primer ordre amb una constant de temps que depèn del muntatge i del medi.

[← 2. Detectors de temperatura resistius (RTD)](#detectors-de-temperatura-resistius-rtd)[4. Termistors NTC: models i linealització →](#termistors-ntc-models-i-linealització)

---

<!-- FIN CAPÍTULO: 03_Unitat5_Autoescalfament_i_resposta_dinamica -->

---

<!-- INICIO CAPÍTULO: 04_Unitat5_Termistors_NTC -->

# Termistors NTC: models i linealització

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 4 de 8

# Termistors NTC: models i linealització

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir termistors NTC i PTC i situar-los enfront dels RTD.
> - Aplicar el model exponencial de dos paràmetres amb les temperatures en kelvin.
> - Obtenir el coeficient de temperatura local i reconèixer l'equació de Steinhart-Hart.
> - Dissenyar la resistència de linealització analògica i avaluar-ne el compromís amb la sensibilitat.

Els **termistors** són sensors resistius de temperatura basats en semiconductors, on la temperatura provoca variacions molt fortes de resistivitat a través del nombre de portadors. Enfront dels RTD de platí tenen **sensibilitat relativa molt més elevada** —el canvi relatiu per grau pot ser vint vegades superior—, **comportament molt menys lineal** (relació aproximadament exponencial), **cost i dimensions molt reduïts** i **pitjor exactitud i intercanviabilitat** sense calibratge individual. Es classifiquen en **NTC** (la resistència decreix amb la temperatura) i **PTC** (creix).

![Símbols de termistor NTC i PTC: rectangle resistiu amb línia trencada diagonal i les marques menys t o i més t o](assets/04_Unitat5_Termistors_NTC_img_1.png)

*Figura: Figura 5.7 Símbols de termistors. A l'esquerra, el símbol d'una NTC; a la dreta, el d'una PTC. La línia trencada indica el comportament no lineal, i el signe que acompanya $t^{o}$
distingeix el sentit de la variació.*

Aquest document tracta les NTC, que són les que s'utilitzen com a sensors; les PTC, emprades sobretot com a proteccions, es tracten al document 5.

## 1 Model exponencial

Una NTC és una resistència de material semiconductor —típicament òxids metàl·lics sinteritzats— en què la resistència disminueix en escalfar-se perquè augmenta el nombre de portadors: el mecanisme oposat al d'un RTD metàl·lic, on la densitat de portadors és constant i el que canvia és la mobilitat. S'apliquen en rangs moderats (0-100 °C) amb exactituds d'unes dècimes o d'algun grau.

$$
R_{\text{NTC}}(T) = R_0\,\exp\left[\beta\left(\frac{1}{T}-\frac{1}{T_0}\right)\right] \qquad (5.26)
$$

amb  $R_0$
 la resistència a la temperatura de referència  $T_0$
 —habitualment 298,15 K, és a dir 25 °C— i  $\beta$
 la temperatura característica.

> [!WARNING] **Les temperatures han d'anar en kelvin**
>
> $T$
> i  $T_0$
> són temperatures **absolutes**: introduir-hi graus Celsius no és una aproximació grollera sinó un error greu, perquè els quocients  $\frac{1}{T}$
> canvien completament de valor i el model deixa de tenir sentit prop de 0 °C. El paràmetre  $\beta$
> també s'expressa en **kelvin**. Es fa servir  $T[\mathrm{K}] = T[^\circ\mathrm{C}] + 273{,}15$
>.

$\beta$
 indica com d'abruptament decreix la resistència: **valors grans impliquen una caiguda més ràpida** i més sensibilitat. Es relaciona amb l'energia d'activació de la generació de portadors, i tant  $R_0$
 com  $\beta$
 depenen del procés de fabricació (document 5).

> [!EXAMPLE] **Exemple resolt: ús del model de dos paràmetres**
>
> Un NTC té  $R_0 = 10\ \mathrm{k\Omega}$
> a 25 °C i  $\beta = 4000\ \mathrm{K}$
>. Quina resistència presenta a 35 °C?
>
> 1. Conversió a kelvin i exponent. Amb  $T_0 = 298{,}15\ \mathrm{K}$
> i  $T = 308{,}15\ \mathrm{K}$
>,  $\beta\left(\frac{1}{T}-\frac{1}{T_0}\right) \approx -0{,}4353$
>, negatiu perquè  $T>T_0$
>.
> 2. Resistència.  $R = 10\,000\cdot e^{-0{,}4353} = 6470\ \Omega$
>.
> 3. Interpretació. 10 °C fan baixar la resistència un 35 %; una Pt-100, en el mateix salt, hauria canviat un 3,85 %.

![Corbes de resistència enfront de temperatura per a diversos termistors NTC amb diferents valors de R0 i beta, amb descens pronunciat entre 0 i 100 graus](assets/04_Unitat5_Termistors_NTC_img_2.png)

*Figura: Figura 5.8 Variació de la resistència de diversos models de NTC amb la temperatura, per a diferents combinacions de $R_0$
i $\beta$
.*

### Linealització local

En marges de pocs graus al voltant d'una temperatura  $T_x$
, la corba s'aproxima per la recta tangent:

$$
R_{\text{NTC}}(T) \approx R_x\left[1+\alpha\,(T-T_x)\right] \qquad (5.27)
$$

$$
\alpha \approx -\frac{\beta}{T_x^{\,2}} \qquad (5.28)
$$

amb  $R_x = R_{\text{NTC}}(T_x)$
,  $T_x$
 i  $\beta$
 en kelvin. El signe negatiu reflecteix que la resistència decreix amb la temperatura. Amb  $\beta=4000$
 K a 25 °C,  $\alpha \approx -0{,}045\ \mathrm{K^{-1}}$
: un −4,5 %/K, més de deu vegades el +0,385 %/K d'una Pt-100 i de signe contrari. És una aproximació **local**, vàlida en intervals estrets —per exemple temperatura corporal prop de 37 °C—, perquè el que s'aproxima és una exponencial.

### Equació de Steinhart-Hart

Per a marges amplis amb alta exactitud es relaciona la *inversa de la temperatura absoluta* amb un polinomi en el *logaritme de la resistència*:

$$
\frac{1}{T} = a + b\,\ln(R) + c\left[\ln(R)\right]^3 \qquad (5.29)
$$

amb  $a$
,  $b$
 i  $c$
 determinats per calibratge en diversos punts i  $R$
 en ohms. Ajusta la corba amb errors molt petits en un rang ampli a canvi de més càlcul i un calibratge acurat, i es reserva per a aplicacions metrològiques. Relaciona temperatura amb resistència, i el seu interès és descriure un comportament fortament no lineal.

## 2 Linealització analògica

![Esquema d'un termistor NTC amb una resistència fixa connectada en paral·lel](assets/04_Unitat5_Termistors_NTC_img_3.png)

*Figura: Figura 5.9 Linealització analògica d'un termistor amb una resistència fixa en paral·lel.*

Connectant una resistència fixa  $R$
 en paral·lel amb el termistor,

$$
R_{\text{eq}}(T) = \frac{R_{\text{th}}(T)\,R}{R_{\text{th}}(T)+R} \qquad (5.30)
$$

Quan la NTC té resistència molt gran o molt petita, la resistència fixa domina el paral·lel i suavitza la variació relativa, de manera que  $R_{\text{eq}}(T)$
 pot ser molt més lineal en un cert marge. El criteri de disseny és imposar un **punt d'inflexió** —segona derivada nul·la— a la temperatura d'interès  $T_x$
, i derivant dues vegades (5.30) amb el model exponencial s'arriba a

$$
R = R_{\text{th}}(T_x)\,\frac{\beta-2T_x}{\beta+2T_x} \qquad (5.31)
$$

Perquè  $R$
 sigui positiva cal  $\beta > 2T_x$
, cosa que es compleix folgadament amb valors habituals ( $\beta$
 de milers de kelvin i  $2T_x$
 de l'ordre de 600 K a temperatura ambient).

![Corbes de resistència del termistor sol i de la combinació en paral·lel enfront de la temperatura, amb la combinació clarament més recta prop de 60 graus](assets/04_Unitat5_Termistors_NTC_img_4.png)

*Figura: Figura 5.10 Resultat de linealitzar un termistor NTC ( $R_T$
) amb una resistència fixa $R_p$
en paral·lel. La resistència equivalent és molt més lineal que la del termistor sol, especialment a les proximitats de 60 °C.*

**El preu a pagar és una disminució de la sensibilitat**: la corba equivalent varia menys amb la temperatura que la NTC nua. Tampoc no s'obté una resposta exactament lineal, perquè el disseny només anul·la la segona derivada en un punt: la millora és local i el marge útil, encara que ampliat, continua sent finit.

### Divisor de tensió

![Esquema d'un divisor de tensió format per un termistor NTC i una resistència fixa alimentat per una font de tensió](assets/04_Unitat5_Termistors_NTC_img_5.png)

*Figura: Figura 5.11 Linealització analògica d'una NTC amb un divisor de tensió.*

Col·locant la NTC en un divisor i prenent com a sortida la tensió sobre la resistència fixa,

$$
V_{\text{out}}(T) = V\,\frac{R}{R+R_{\text{th}}(T)} \qquad (5.32)
$$

i imposant també aquí un punt d'inflexió a  $T_x$
 s'arriba a

$$
R = R_{\text{th}}(T_x)\,\frac{\beta-2T_x}{\beta+2T_x} \qquad (5.33)
$$

exactament la mateixa expressió que (5.31), perquè la no linealitat que es compensa és la de la mateixa exponencial.

![Gràfic amb la corba de resistència de la NTC, la tensió normalitzada del divisor i la recta d'aproximació prop de 50 graus](assets/04_Unitat5_Termistors_NTC_img_6.png)

*Figura: Figura 5.12 Exemple de linealització de NTC amb divisor de tensió. La variació de la NTC es mostra amb la corba taronja; la sortida del divisor, normalitzada respecte de la tensió d'alimentació, en púrpura. La recta verda és l'aproximació lineal prop de 50 °C, i la tensió del divisor és raonablement lineal entre 30 °C i 70 °C.*

Té dos avantatges: la sortida ja és una **tensió**, directament utilitzable per un convertidor A/D, i el signe queda invertit respecte de la NTC —si la temperatura puja,  $R_{\text{th}}$
 baixa i la tensió *augmenta*. La sortida depèn del valor de la resistència fixa, que és el paràmetre de disseny. S'utilitza en sistemes econòmics, on es vol una relació aproximadament lineal en un marge reduït sense càlculs complexos al microcontrolador; quan hi ha capacitat de càlcul, l'alternativa és la **linealització digital**, que aplica el model invertit o Steinhart-Hart sense sacrificar sensibilitat.

> [!TIP] **Síntesi**
>
> Les NTC baixen de resistència en escalfar-se perquè augmenta la densitat de portadors, amb sensibilitat relativa molt superior a la dels RTD però resposta exponencial i pitjor intercanviabilitat. El model de dos paràmetres exigeix temperatures absolutes en kelvin, i un  $\beta$
> més gran significa caiguda més abrupta. Localment s'aproxima per una recta amb  $\alpha\approx-\beta/T_x^2$
>, sempre negatiu. Steinhart-Hart relaciona  $\frac{1}{T}$
> amb un polinomi en  $\ln R$
> per a marges amplis. La linealització analògica, en paral·lel o en divisor, dona  $R=R_{\text{th}}(T_x)(\beta-2T_x)/(\beta+2T_x)$
> i millora la linealitat a canvi de perdre sensibilitat.

[← 3. Autoescalfament, excitació i resposta dinàmica](#autoescalfament-excitació-i-resposta-dinàmica)[5. Termistors: construcció, PTC i aplicacions →](#termistors-construcció-ptc-i-aplicacions)

---

<!-- FIN CAPÍTULO: 04_Unitat5_Termistors_NTC -->

---

<!-- INICIO CAPÍTULO: 05_Unitat5_Termistors_construccio_PTC_aplicacions -->

# Termistors: construcció, PTC i aplicacions

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 5 de 8

# Termistors: construcció, PTC i aplicacions

Dedicació estimada: 7 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Relacionar el procés de fabricació ceràmica d'una NTC amb la dispersió dels seus paràmetres.
> - Escollir el format i l'encapsulat segons el muntatge, la resposta dinàmica i el medi.
> - Comparar termistors NTC i RTD i explicar l'autoescalfament com a principi de mesura.
> - Distingir posistors i silistors i les aplicacions de protecció de les PTC.

## 1 Fabricació i formats de les NTC

![Fotografies de diversos encapsulats de termistors NTC: discs, perles, sondes i xips de muntatge superficial](assets/05_Unitat5_Termistors_construccio_PTC_aplicacions_img_1.png)

*Figura: Figura 5.13 Exemples d'encapsulats de NTC, tant de muntatge amb forat passant com de muntatge superficial.*

La major part de NTC es fabriquen amb **ceràmiques semiconductores d'òxids metàl·lics** —manganès, níquel, cobalt, coure—: preparació de la pols, premsat o extrusió, **sinterització** a alta temperatura que forma una ceràmica densa amb les propietats buscades, i aplicació d'elèctrodes i terminals.

Els paràmetres  $R_0$
 i  $\beta$
 **depenen fortament de la composició i del cicle de sinterització**: aquesta és l'arrel del problema d'intercanviabilitat. Obtenir NTC intercanviables amb toleràncies estretes exigeix un control molt més estricte i encareix el component; les ordinàries presenten dispersió apreciable entre unitats i sovint cal calibratge individual.

Els NTC de **forat passant** es presenten en **disc** (els clàssics de potència o de mesura general, usats també com a limitadors de transitoris en sèrie amb la línia), en **perla** (massa mínima i constant de temps molt baixa, muntable com a sonda d'immersió, típica en aplicacions mèdiques i climatització domèstica) i en **formats especials** com orella o anella, per cargolar a xassís i dissipadors. L'aïllament superficial i la geometria determinen el coeficient de dissipació  $\delta$
 i la potència màxima admissible.

Els NTC **SMD** s'encapsulen en xips rectangulars o cilíndrics amb capa protectora de vidre o resina. Ofereixen **compatibilitat total amb soldadura per *reflow* i muntatge automatitzat**, dimensions de fracció de mil·límetre amb resposta tèrmica molt ràpida, i integració al costat dels components crítics de la placa.

**Els encapsulats petits tenen menys massa tèrmica i responen més ràpid**, però admeten menys potència: la resposta dinàmica no és una propietat del material sinó del conjunt massa-encapsulat-muntatge.

## 2 NTC enfront de RTD

**Avantatges de les NTC**: cost molt inferior; **sensibilitat elevada**, amb un canvi relatiu per grau fins a vint vegades superior; dimensions i massa reduïdes amb respostes ràpides; i **resistència nominal elevada** —de kΩ a desenes de kΩ a 25 °C—, que minimitza l'efecte de les resistències de cablejat, el problema oposat al de la Pt-100.

**Desavantatges**: forta **no linealitat** exponencial, que obliga a linealitzar o calcular numèricament; **menor exactitud i pitjor intercanviabilitat**, amb  $(R_0,\beta)$
 variables entre dispositius del mateix model, de manera que l'alta exactitud demana calibratge individual o termistors intercanviables més cars; i **més soroll tèrmic i susceptibilitat a interferències**, perquè la resistència elevada implica més soroll Johnson —la densitat  $4kTR$
 de la unitat 4 creix amb  $R$
— i més sensibilitat a interferències capacitatives amb entrades d'alta impedància. La resistència alta elimina, doncs, el problema del cablejat però n'introdueix un altre.

En resum: per a exactitud i estabilitat en entorns exigents, els RTD; per a mesures econòmiques, sensibles i ràpides amb exactitud moderada, les NTC.

## 3 Aplicacions de les NTC

**Mesura de temperatura**: termòmetres digitals corporals (marge de 35-42 °C, fàcil de linealitzar), estacions meteorològiques i electrònica de consum, amb models simplificats o taules de conversió.

### Detecció de nivell i de flux per autoescalfament

Aquesta aplicació capgira el problema del document 3: en lloc de combatre l'autoescalfament, l'utilitza com a *principi de mesura*. El termistor fa alhora de calefactor i de sensor. Amb corrent constant, la temperatura s'ajusta fins que el flux de calor cap al medi iguala  $P=I^2R$
, segons  $\delta$
; si canvia el medi —d'aire a aigua, o si varia el flux— canvia  $\delta$
 i, amb ell, la temperatura d'equilibri i la resistència.

![Corbes corrent-tensió d'un termistor de 10 kilohm en aire quiet i en aigua, amb desviació respecte de la recta òhmica en augmentar el corrent](assets/05_Unitat5_Termistors_construccio_PTC_aplicacions_img_2.png)

*Figura: Figura 5.14 Corbes corrent-tensió d'un termistor de 10 kΩ a 25 °C exposat a aire quiet i a aigua sense flux. Amb corrents petits la dissipació és tan reduïda que no hi ha autoescalfament i el quocient tensió-corrent val exactament 10 kΩ; en augmentar el corrent, la corba queda per sota de la recta de 10 kΩ perquè la NTC està més calenta que l'entorn.*

Amb 3 mA en aire la tensió en borns és d'uns 7,5 V; submergit en aigua a la mateixa temperatura ambient, la dissipació és molt més efectiva, la temperatura interna baixa, la resistència augmenta i la tensió pot arribar als 15 V. Permet construir **detectors de nivell** i **anemòmetres tèrmics**: a corrent constant, més velocitat d'aire refreda el termistor i n'augmenta la resistència.

### Limitació de transitoris de corrent

![Esquema d'una NTC connectada en sèrie amb la càrrega i la font d'alimentació per limitar el corrent d'engegada](assets/05_Unitat5_Termistors_construccio_PTC_aplicacions_img_3.png)

*Figura: Figura 5.15 Limitació de transitoris de corrent amb una NTC en sèrie amb la càrrega.*

Amb la NTC **en sèrie amb la càrrega**, a temperatura ambient té resistència elevada i limita el pic de corrent inicial (*inrush*); en circular-hi corrent s'autoescalfa, la resistència *disminueix* i queda molt per sota de la de la càrrega, deixant passar pràcticament el corrent nominal. La NTC comença **freda i resistiva** i acaba **calenta i poc resistiva**. Amb càrrega capacitiva (en paral·lel amb una resistència Rl), en l'encesa la impedància pot ser molt baixa i el corrent enorme; la NTC en limita el valor i, un cop escalfada, el condensador es carrega normalment. És comú en fonts d'alimentació de potència, equips d'àudio i electrònica industrial.

## 4 Termistors PTC

Les PTC s'utilitzen sobretot com a **elements de protecció i compensació**, no com a sensors de precisió, i no substitueixen els RTD de platí en aquest paper.

![Corbes de resistència enfront de temperatura d'una família de posistors, amb creixement abrupte de diversos ordres de magnitud a partir de la temperatura de transició](assets/05_Unitat5_Termistors_construccio_PTC_aplicacions_img_4.png)

*Figura: Figura 5.16 Relació temperatura-resistència en una família de posistors.*

Els **posistors**, ceràmics, presenten un canvi **abruptament positiu** de resistència en un marge estret, de l'ordre de 50 °C: a temperatures baixes el coeficient és lleugerament negatiu o dèbilment positiu, i per damunt d'una **temperatura de transició** la resistència pot canviar fins a quatre ordres de magnitud, de manera que la característica no és ni suau ni lineal. L'augment es relaciona amb canvis de fase o de conducció del ceràmic, i al punt alt el corrent queda fortament limitat, que és l'efecte buscat.

![Dues corbes de resistència enfront de temperatura d'un silistor, una sense linealitzar i l'altra amb resistència de 2,37 kilohm en paral·lel, més recta](assets/05_Unitat5_Termistors_construccio_PTC_aplicacions_img_5.png)

*Figura: Figura 5.17 Relació temperatura-resistència d'un silistor sense i amb element de linealització analògica; en aquest cas, una resistència fixa de 2,37 kΩ en paral·lel.*

Els **silistors** són PTC de silici molt dopat, amb un canvi *més suau* que els posistors i sovint amb linealització integrada —la mateixa tècnica de resistència en paral·lel del document 4—, útils per a compensació tèrmica o mesura aproximada quan es vol un coeficient positiu moderat i previsible.

### Aplicacions de les PTC

![Esquema d'un transistor de potència amb una PTC en el circuit de polarització de base en contacte tèrmic amb el dissipador](assets/05_Unitat5_Termistors_construccio_PTC_aplicacions_img_6.png)

*Figura: Figura 5.18 Limitació de la potència dissipada per un transistor de potència mitjançant una PTC.*

**Protecció tèrmica d'un transistor de potència.** La PTC es col·loca en contacte tèrmic íntim amb el transistor i forma part del circuit de polarització de base. Si el transistor dissipa massa potència, la temperatura puja, la resistència de la PTC creix i *redueix* el corrent de base; això abaixa el corrent de col·lector i la potència dissipada, i el sistema s'estabilitza per **retroalimentació negativa**. Els processos són lents però suficients en règim quasi estacionari.

![Esquema del circuit de desmagnetització amb una PTC en sèrie amb el bobinat connectat a la xarxa](assets/05_Unitat5_Termistors_construccio_PTC_aplicacions_img_7.png)

*Figura: Figura 5.19 Circuit de desmagnetització amb PTC en sèrie amb el bobinat.*

**Desmagnetització per transitori de corrent decreixent.** Per desmagnetitzar un circuit magnètic —per exemple una pantalla de raigs catòdics— cal un corrent altern de gran amplitud que decreixi fins a zero. Amb una PTC en sèrie amb el bobinat, a l'instant inicial la resistència és baixa i el camp intens; en autoescalfar-se, la resistència augmenta fortament i el corrent cau a valors pràcticament nuls en menys d'un segon. El corrent s'extingeix tot sol, i això és el que fa útil el muntatge, aquí i allà on cal un corrent inicial fort que es redueixi sense control electrònic.

> [!TIP] **Síntesi**
>
> Els paràmetres  $R_0$
> i  $\beta$
> depenen del cicle de sinterització, cosa que explica la dispersió entre dispositius. Els encapsulats petits responen més ràpid però admeten menys potència. Enfront dels RTD, les NTC són més barates, sensibles i petites i menys afectades pel cablejat, però menys lineals, pitjor intercanviables i més sorolloses. Les aplicacions són la mesura en marges moderats, la detecció de nivell i flux per canvi del coeficient de dissipació, i la limitació del corrent d'engegada, on la NTC comença freda i resistiva i acaba calenta i conductora. Les PTC són proteccions: els posistors amb transició abrupta i els silistors, més suaus, per a compensació tèrmica.

[← 4. Termistors NTC: models i linealització](#termistors-ntc-models-i-linealització)[6. Sensors piezoresistius i galgues extensiomètriques →](#sensors-piezoresistius-i-galgues-extensiomètriques)

<!-- FIN CAPÍTULO: 05_Unitat5_Termistors_construccio_PTC_aplicacions -->

---

<!-- INICIO CAPÍTULO: 06_Unitat5_Sensors_piezoresistius_i_galgues -->

# Sensors piezoresistius i galgues extensiomètriques

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 6 de 8

# Sensors piezoresistius i galgues extensiomètriques

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Definir tensió mecànica i deformació unitària i situar les zones elàstica, plàstica i de fallida.
> - Deduir el factor de galga i aplicar  $R=R_0(1+k\varepsilon)$
> dins dels seus límits.
> - Interpretar la sensibilitat longitudinal i transversal i el paper de les rosetes.
> - Identificar els errors de temperatura i de muntatge i descriure les aplicacions típiques.

Un **sensor piezoresistiu** canvia de resistència quan el material es deforma sota una tensió mecànica; dins de la zona elàstica la variació és aproximadament proporcional a la deformació, i coneixent el model i les propietats de la peça se'n dedueixen deformació, força, pressió o acceleració. Es presenten com a **galgues extensiomètriques**: una graella resistiva en ziga-zaga sobre un substrat aïllant, adherit sobre la peça, amb la graella més elàstica que el substrat i aquest més que la peça. És un sensor **modulador**: no genera cap tensió en deformar-se —això seria un sensor piezoelèctric, de la unitat 9— sinó que modifica una resistència que cal excitar.

## 1 Tensió mecànica i deformació

$$
\sigma = \frac{F}{A} \qquad (5.34)
$$

$$
\varepsilon = \frac{\Delta l}{l_0} \qquad (5.35)
$$

La **tensió mecànica** és la força *dividida* per la secció, en pascals (habitualment MPa o GPa); la **deformació unitària** és un quocient de longituds i, per tant, **adimensional**, sovint en microdeformacions (µm/m, és a dir µε):  $1000\ \mu\varepsilon$
 equival a  $10^{-3}$
.

![Corba de tensió mecànica enfront de deformació amb la zona elàstica lineal, la zona plàstica amb enduriment, el punt de tensió màxima i la zona de fallida](assets/06_Unitat5_Sensors_piezoresistius_i_galgues_img_1.png)

*Figura: Figura 5.20 Relació entre tensió mecànica —representada aquí com a força— i elongació relativa d'un material, amb les zones elàstica, plàstica (que inclou la d'enduriment) i de fallida.*

- **Zona elàstica**: deformacions petites, relació pràcticament lineal i *reversible*.
- **Zona plàstica**: la relació deixa de ser lineal i poden quedar deformacions permanents. Inclou la *zona d'enduriment*, on per estirar més cal una força creixent i el material no s'allarga fins a superar el màxim aplicat abans.
- **Zona de fallida**: a partir de la tensió de trencament, la secció s'escanya de manera no proporcional i el material es pot trencar.

Les galgues s'han de fer treballar **sempre dins de la zona elàstica**: en zona plàstica es perd la reversibilitat i, amb ella, la mesura. Hi val la **llei de Hooke**:

$$
\sigma = E\,\varepsilon \qquad (5.36)
$$

amb  $E$
 el **mòdul de Young**, amb dimensions de pressió, que mesura la *rigidesa* —uns 200 GPa per a l'acer, 70 GPa per a l'alumini, 20-30 GPa per al formigó— i permet convertir deformació en tensió mecànica i, amb la geometria, en força. En estirar-se, la peça s'estreny transversalment per **efecte de Poisson**:

$$
\frac{\Delta A}{A} = -2\,\nu\,\varepsilon \qquad (5.37)
$$

amb  $\nu$
 entre 0,25 i 0,35 per a molts metalls; el signe negatiu indica que la secció *disminueix* quan la peça s'estira.

## 2 El factor de galga

Partint de

$$
R = \rho\,\frac{l}{A} \qquad (5.38)
$$

$$
\frac{\Delta R}{R} \approx \frac{\Delta\rho}{\rho} + \frac{\Delta l}{l} - \frac{\Delta A}{A} \qquad (5.39)
$$

amb els canvis geomètrics en zona elàstica

$$
\frac{\Delta l}{l} = \varepsilon \qquad (5.40)
$$

$$
\frac{\Delta A}{A} = -2\nu\,\varepsilon \qquad (5.41)
$$

i la variació de resistivitat amb la deformació —la piezoresistivitat pròpiament dita, sobretot en materials cristal·lins—

$$
\frac{\Delta\rho}{\rho} = k_1\,\varepsilon \qquad (5.42)
$$

amb  $k_1$
 una constant positiva del material, resulta

$$
\frac{\Delta R}{R} = k_1\varepsilon + \varepsilon + 2\nu\varepsilon = \left(1+2\nu+k_1\right)\varepsilon \qquad (5.43)
$$

La constant de proporcionalitat recull *tots dos* mecanismes, el geomètric i el de resistivitat. Es defineix el **factor de galga**

$$
k = \frac{\Delta R/R}{\varepsilon} \qquad (5.44)
$$

—quant canvia la resistència, en termes relatius, per unitat de deformació— de manera que

$$
k = 1+2\nu+k_1 \qquad (5.45)
$$

En **galgues metàl·liques** el terme geomètric val uns  $1+2\cdot 0{,}3 = 1{,}6$
 i  $k_1$
 és de l'ordre de 0,4 a 1, cosa que dona factors **entre 2 i 3**. En **semiconductores**, l'efecte de la deformació sobre la resistivitat és molt més gran i permet  $k$
 **entre 50 i 150**.

$$
R = R_0\left(1+k\,\varepsilon\right) \qquad (5.46)
$$

El model és lineal en  $\varepsilon$
 i vàlid dins dels límits del fabricant: **metàl·liques**, fins a uns 40 000 µε (4 %); **semiconductores**, de 1000 a 3000 µε. Aquesta és la contrapartida de la sensibilitat: les semiconductores admeten deformacions màximes molt *menors*, i a prop dels límits apareixen no linealitats i histèresi.

## 3 Construcció i paràmetres geomètrics

![Fotografia d'una galga extensiomètrica comercial amb graella en ziga-zaga sobre substrat flexible i dos terminals de connexió](assets/06_Unitat5_Sensors_piezoresistius_i_galgues_img_2.png)

*Figura: Figura 5.21 Exemple de galga extensiomètrica comercial: substrat aïllant flexible de poliimida o paper reforçat, pel·lícula resistiva en graella de ziga-zaga i zones de connexió soldables.*

La graella té una direcció de màxima sensibilitat, que ha de coincidir amb la direcció principal de deformació: una galga no és indiferent a l'orientació. Es distingeix entre **sensibilitat longitudinal**, en la direcció de la graella, i **sensibilitat transversal**, a deformacions ortogonals, que el fabricant dona com a percentatge de la longitudinal i que ha de ser tan baixa com sigui possible.

La **longitud de la graella** determina la *mitjana espacial* de la deformació i ha de ser petita respecte de la peça. La jerarquia de rigideses ho lliga tot: **el substrat ha de ser més elàstic que la peça**, i l'adhesiu més rígid que el substrat però menys que la peça; un substrat més rígid que la peça n'impediria la deformació lliure.

|  | Metàl·liques | Semiconductores |
|:--- |:--- |:--- |
| Material | Pel·lícules fines d'aliatges com constantan o karma | Silici dopat o ceràmiques semiconductores |
| Resistència nominal | 120 Ω a 350 Ω habitualment | Més elevada |
| Factor de galga  $k$ | 2 a 3 | 50 a 150 |
| Deformació màxima | Fins a 40 000 µε (4 %) | 1000 a 3000 µε (0,1-0,3 %) |
| Linealitat i repetibilitat | Molt bones | Resposta sovint no lineal |
| Intercanviabilitat | Toleràncies baixes; relativament intercanviables | Toleràncies més grans; menys intercanviables |

El constantan i el karma es trien pel seu **coeficient de temperatura molt baix**, primera defensa contra les derives tèrmiques. Les semiconductores convenen quan cal molta sensibilitat i poc rang, com en sensors integrats de pressió o acceleròmetres MEMS —la integració en MEMS admet, doncs, principis piezoresistius—, però **les metàl·liques dominen el mercat** per robustesa i facilitat d'ús.

## 4 Temperatura, rosetes i muntatge

La resistència d'una galga **depèn també de la temperatura** —ser metàl·lica no la immunitza: és el mecanisme dels RTD—, i si no es compensa s'interpreta com deformació. S'usen aliatges de coeficient molt baix; **galgues de referència** no carregades mecànicament connectades en pont, de manera que la seva variació tèrmica *compensi* la de les actives, ja que el pont cancel·la les variacions comunes; i correcció digital amb un sensor de temperatura (unitat 6).

![Tres configuracions comercials de galgues: parell de galgues idèntiques, semi-roseta a 0 i 90 graus i roseta de tres galgues a 0, 45 i 90 graus](assets/06_Unitat5_Sensors_piezoresistius_i_galgues_img_3.png)

*Figura: Figura 5.22 Configuracions comercials de galgues. Esquerra: dues galgues idèntiques que, en braços oposats d'un pont, dupliquen la sensibilitat. Centre: semi-roseta amb galgues a 0° i 90°, sensibles a direccions ortogonals. Dreta: roseta de tres galgues a 0°, 45° i 90°.*

Quan no es coneix la direcció de la tensió s'usen configuracions multiaxials, que serveixen també per compensar temperatura. La **roseta de tres galgues** permet inferir el mòdul i la direcció de la tensió: coneguts el mòdul de Young i el coeficient de Poisson, les tres lectures resolen les equacions de transformació de tensió plana i donen  $\sigma_1$
,  $\sigma_2$
 i l'angle principal. És fonamental en estructures civils.

El **muntatge físic és crític**: és la instal·lació la que decideix si el factor de galga és aplicable. S'usen cianoacrilats per a assajos curts i epoxis per a estabilitat a llarg termini; cal preparar la superfície, orientar la galga segons la direcció de tensió, aplicar l'adhesiu amb pressió controlada i protegir terminals i soldadures. Cal evitar bombolles d'aire, tensions per flexió del cablejat, gradients tèrmics i sobrecàrregues que treguin la peça de la zona elàstica, perquè degraden la resposta o introdueixen histèresi; els **fils de connexió** poden introduir tensions al punt de soldadura encara que la seva resistència sigui baixa. Això encareix el producte: una galga val unes unitats d'euro, però muntada i calibrada el conjunt puja a desenes o centenars.

## 5 Aplicacions

![Fotografies de galgues instal·lades en elements estructurals de construcció civil](assets/06_Unitat5_Sensors_piezoresistius_i_galgues_img_4.png)

*Figura: Figura 5.23 Mesura de deformació en aplicacions civils: rails ferroviaris, bigues de formigó, pilars metàl·lics.*

**Mesura de deformació en estructures.** En laboratori, per obtenir corbes tensió-deformació de provetes; en estructures civils, per detectar deformacions inusuals que indiquen danys, sobrecàrrega o fatiga en ponts o edificis.

![Fotografia d'una cèl·lula de càrrega metàl·lica amb galgues adherides a la zona dissenyada per deformar-se](assets/06_Unitat5_Sensors_piezoresistius_i_galgues_img_5.png)

*Figura: Figura 5.24 Cèl·lula de càrrega. La geometria de la peça metàl·lica està dissenyada perquè es deformi la part on s'instal·len els sensors.*

**Cèl·lules de càrrega.** Una peça mecànica —viga, bloc, anell— amb galgues: la deformació sota càrrega es converteix en variació de resistència i, finalment, en tensió. La peça es dissenya perquè, per al rang de forces especificat, la deformació es mantingui **dins de la zona elàstica**, amb resposta reversible i repetible. Les galgues es connecten sovint en pont de Wheatstone de quatre resistències, que augmenta la sensibilitat i compensa parcialment els efectes tèrmics. S'apliquen a bàscules industrials, balances de precisió, dinamòmetres i bancs d'assaig.

![Esquema d'un acceleròmetre piezoresistiu amb massa inercial sobre un voladís amb galgues](assets/06_Unitat5_Sensors_piezoresistius_i_galgues_img_6.png)

*Figura: Figura 5.25 Acceleròmetre piezoresistiu amb massa inercial sobre un voladís amb galgues.*

**Acceleròmetres piezoresistius.** Una **massa inercial** sobre una estructura elàstica amb galgues: sota acceleració  $a$
 la massa experimenta  $F=ma$
 i deforma el voladís, i un pont converteix la deformació en tensió. S'usen en vibracions, detecció de xocs, control d'estabilitat i aplicacions d'automoció i aeroespacials.

**Transductors de pressió.** Una **membrana deformable**, metàl·lica o de silici, amb galgues o piezoresistències integrades: la pressió sobre un costat la deforma i el model mecànic de la membrana relaciona el canvi de resistència amb la pressió. La cadena causal és pressió → deformació → canvi de resistència. Són comuns en instrumentació industrial, hidràulica, pneumàtica i automoció.

> [!TIP] **Síntesi**
>
> Una galga converteix deformació en variació de resistència i necessita excitació.  $\sigma=F/A$
> va en pascals i  $\varepsilon=\Delta l/l_0$
> és adimensional; en zona elàstica les lliga  $\sigma=E\varepsilon$
>. El factor de galga  $k=(\Delta R/R)/\varepsilon = 1+2\nu+k_1$
> val entre 2 i 3 en metàl·liques i entre 50 i 150 en semiconductores, que admeten deformacions molt menors. El model  $R=R_0(1+k\varepsilon)$
> val en zona elàstica. L'orientació importa i la sensibilitat transversal ha de ser mínima; les rosetes resolen direccions desconegudes. La temperatura es compensa amb aliatges de coeficient baix, galgues de referència en pont o correcció digital. S'hi basen cèl·lules de càrrega, acceleròmetres i transductors de pressió.

[← 5. Termistors: construcció, PTC i aplicacions](#termistors-construcció-ptc-i-aplicacions)[7. Magnetoresistències →](#magnetoresistències)

---

<!-- FIN CAPÍTULO: 06_Unitat5_Sensors_piezoresistius_i_galgues -->

---

<!-- INICIO CAPÍTULO: 07_Unitat5_Magnetoresistencies -->

# Magnetoresistències

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 7 de 8

# Magnetoresistències

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir els mecanismes de les AMR, les GMR i les TMR i els seus ordres de magnitud.
> - Interpretar el model d'una AMR bàsica i explicar per què perd la informació de signe.
> - Relacionar la configuració paral·lela o antiparal·lela d'una GMR amb la resistència.
> - Descriure les aplicacions de posició, velocitat angular, lectura magnètica i mesura de corrent.

Les **magnetoresistències** són sensors **resistius** la resistència dels quals varia amb el camp magnètic. Tots els conductors experimenten una modificació lleu de la resistivitat en presència de camp, però l'efecte només és útil en materials **anisòtrops i ferromagnètics**, on les propietats depenen de la direcció del camp. Responen igualment a camps continus i alterns, i moltes aplicacions —posició amb un imant permanent, mesura de corrent continu— es basen en camps estàtics.

## 1 Les tres famílies

- **AMR** (*Anisotropic Magnetoresistor*): materials ferromagnètics anisòtrops, com el permalloy, travessats per un corrent constant. Variacions relatives d'aproximadament el **2 %** abans de la saturació.
- **GMR** (*Giant Magnetoresistor*): estructures multicapa de ferromagnètic i conductor no ferromagnètic, amb gruixos de pocs nanòmetres. L'efecte, descobert el 1988, dona canvis típics del **20 %**, deu vegades els de l'AMR.
- **TMR** (*Tunnel Magnetoresistor*): evolució de la GMR en què la capa intermèdia esdevé una **aïllant** extremadament fina i el transport té lloc per efecte túnel quàntic, amb variacions encara més altes.

La sensibilitat creix en l'ordre AMR < GMR < TMR, i la **complexitat de fabricació segueix el mateix ordre**: una TMR exigeix un control nanomètric del gruix de la barrera que l'AMR no necessita. Les AMR són suficients per a camps moderats i posició; les GMR, quan cal molta sensibilitat en espais reduïts.

## 2 Magnetoresistència anisòtropa (AMR)

El material de referència és el **permalloy**, aliatge d'un 80 % de níquel i un 20 % de ferro, amb alta permeabilitat, baixa coercitivitat i anisotropia ben definida. La configuració més senzilla és una barra amb corrent constant, que genera un camp de polarització intern  $H_x$
 i una magnetització neta preferent; el camp a mesurar  $H_y$
, ortogonal, la desvia i modifica la resistència.

![Esquema d'una barra de permalloy amb corrent longitudinal, camp de polarització Hx i camp transversal Hy que desvia la magnetització](assets/07_Unitat5_Magnetoresistencies_img_1.png)

*Figura: Figura 5.26 Representació d'un sensor AMR bàsic.*

La resistència **depèn de l'angle entre el corrent i la magnetització neta**: els electrons es dispersen de manera diferent segons si circulen paral·lelament o perpendicularment a  $M$
, mentre que el nombre de portadors amb prou feines canvia.

$$
R = R_{\max} - \Delta R\,\frac{(H_y/H_x)^2}{1+(H_y/H_x)^2} \qquad (5.47)
$$

on  $R_{\max}$
 correspon a  $H_y=0$
 i  $\Delta R$
 és la variació màxima. A l'expressió,  $H_y$
 hi apareix **elevat al quadrat**: la funció és parell i, per tant, simètrica respecte de  $H_y=0$
, de manera que l'AMR bàsica en dona **el mòdul però no el signe**.

![Corba de resistència d'una AMR bàsica enfront del camp transversal, simètrica respecte de l'origen i plana al voltant de camp nul](assets/07_Unitat5_Magnetoresistencies_img_2.png)

*Figura: Figura 5.27 Variació de la resistència d'una AMR bàsica amb la intensitat de camp magnètic $H_y$
.*

L'increment relatiu és de l'ordre del 2 % i el rang útil es limita a  $|H_y| \lesssim H_x$
, amb  $H_x$
 de l'ordre de kA/m. Per a camps molt inferiors a  $H_x$
 la sensibilitat cau ràpidament, perquè la corba és **plana al voltant de l'origen**: la sensibilitat màxima es troba en camps de l'ordre de  $H_x$
.

### L'estructura *barber pole*

![Esquema d'una barra de permalloy amb bandes d'alumini inclinades 45 graus formant l'estructura barber pole](assets/07_Unitat5_Magnetoresistencies_img_3.png)

*Figura: Figura 5.28 AMR amb estructura barber pole: seccions de permalloy intercalades amb seccions d'alumini (paramagnètic), amb contactes inclinats 45° respecte dels extrems.*

El corrent s'injecta per les unions inclinades i, dins del permalloy, té una component a 45° respecte de la barra. Això obliga la magnetització de mínima resistència a un angle determinat i fa la dependència **lineal per a camps petits, amb signe distingible**:

$$
R = R_0 + \frac{\Delta R}{2}\,\frac{(H_y/H_0)}{\sqrt{1+(H_y/H_0)^2}} \qquad (5.48)
$$

amb  $H_0$
 un camp de referència relacionat amb  $H_x$
. Ara  $H_y$
 hi apareix en primera potència i la corba ja no és simètrica,  $R(H_y)\neq R(-H_y)$
, amb sensibilitat màxima prop de  $H_y=0$
: permet mesurar camps molt més petits, útils per a sensors d'angle o de petits desplaçaments.

![Comparació de les corbes de resistència d'una AMR bàsica, simètrica i plana a l'origen, i d'una AMR barber pole, monòtona i lineal prop de zero](assets/07_Unitat5_Magnetoresistencies_img_4.png)

*Figura: Figura 5.29 Comparació de la resposta entre una AMR amb estructura barber pole i una sense.*

Tots dos comparteixen el mateix ordre de variació (~2 %) i el mateix rang de camps. El *barber pole* és preferible quan cal signe i alta resolució prop de zero; continua requerint el camp de polarització intern i manté la dependència amb la temperatura.

## 3 Magnetoresistència gegant (GMR)

![Esquema de l'estructura multicapa d'una GMR amb dues capes ferromagnètiques separades per una capa conductora no ferromagnètica](assets/07_Unitat5_Magnetoresistencies_img_5.png)

*Figura: Figura 5.30 Estructura d'una GMR: dues capes ferromagnètiques —per exemple de ferro— separades per una capa conductora no ferromagnètica —per exemple de crom—, amb gruixos de pocs nanòmetres, sovint repetides en multicapes.*

Les GMR aprofiten efectes quàntics de l'**espín** en estructures nanomètriques: la probabilitat de dispersió dels electrons de conducció a les capes ferromagnètiques depèn de si el seu espín està alineat amb la magnetització local.

- **Sense camp extern**, les magnetitzacions de les dues capes són oposades; els electrons d'un espín determinat troben molta dispersió en almenys una capa i la **resistència creix**.
- **Amb camp extern**, s'alineen; en arribar al camp de saturació  $H_s$
   són pràcticament paral·leles, la dispersió cau i la **resistència disminueix**.

La correspondència és el nucli de l'efecte: **antiparal·lel → resistència alta; paral·lel → resistència baixa**. El canvi relatiu  $\Delta R/R$
 és de l'ordre del 20 % o més segons el gruix i la qualitat de les capes.

![Corba de resistència d'una GMR enfront del camp aplicat, amb transició des de resistència alta fins a resistència baixa al voltant del camp de saturació](assets/07_Unitat5_Magnetoresistencies_img_6.png)

*Figura: Figura 5.31 Resposta d'una GMR i magnetització.*

Com en l'AMR bàsica, la resposta no distingeix el signe del camp sinó el mòdul. La corba transita de resistència alta a baixa al voltant de  $H_s$
; per damunt ja no canvia, de manera que  **$H_s$
 defineix el marge de mesura útil**: la saturació marca el *final* del rang aprofitable, perquè un sensor saturat deixa de donar informació.

|  | Mecanisme | $\Delta R/R$ | Complexitat |
|:--- |:--- |:--- |:--- |
| AMR | Anisotropia de dispersió en un sol material ferromagnètic: la resistivitat depèn de l'angle entre corrent i magnetització | ~2 % | Baixa |
| GMR | Dispersió dependent de l'espín en dues capes ferromagnètiques separades per una capa conductora | ~20 % | Mitjana |
| TMR | Transport per túnel quàntic a través d'una barrera aïllant ultrafina; la probabilitat depèn de l'espín i de la configuració relativa de magnetitzacions | Superior a la GMR | Alta |

## 4 Temperatura i aplicacions

La resistència depèn també de la temperatura, i sense corregir-ho es pot interpretar com un canvi de camp. Els fabricants integren diverses magnetoresistències en un **pont de Wheatstone**, que cancel·la les variacions *comunes* i deixa passar el diferencial, i hi disposen elements de **referència** que vegin la mateixa temperatura però camp nul o constant. La majoria ofereixen mòduls precondicionats amb pont, polarització i amplificador integrats.

![Esquema d'un sensor magnetoresistiu enfront d'un imant que es desplaça, amb el camp variant amb la distància](assets/07_Unitat5_Magnetoresistencies_img_7.png)

*Figura: Figura 5.32 Aplicació d'una magnetoresistència per mesurar posició sense contacte.*

**Detecció de posició sense contacte.** El camp d'un imant, o d'una peça ferromagnètica dins d'un camp fix, varia amb la distància. El marge útil depèn del quocient  $H_y/H_x$
 en AMR o  $H/H_s$
 en GMR: massa a prop el sensor se satura, massa lluny el senyal queda enfonsat en el soroll. És el cas del tancament de porta en neveres o portàtils, on un petit imant fixa un llindar. Evita el contacte mecànic i funciona en entorns bruts o hermètics.

![Esquema de mesura de rotació d'un eix amb roda dentada ferromagnètica i sensor magnetoresistiu](assets/07_Unitat5_Magnetoresistencies_img_8.png)

*Figura: Figura 5.33 Mesura de rotació amb magnetoresistència i roda dentada.*

**Velocitat angular i angle.** Amb una **roda dentada ferromagnètica** o un disc amb imants, el pas de cada dent modifica el camp i genera un senyal cíclic del qual es dedueix la velocitat; en AMR *barber pole* el senyal és quasi sinusoïdal i distingeix el signe, útil per a angle continu. S'aplica en ABS, encoders i posicionament d'eixos.

![Esquema d'un capçal de lectura GMR sobre la superfície d'un disc dur amb dominis magnètics](assets/07_Unitat5_Magnetoresistencies_img_9.png)

*Figura: Figura 5.34 Aplicació d'una GMR per a la lectura de disc dur.*

**Lectura magnètica.** Els bits d'un disc creen dominis de camp molt petits que l'elevada sensibilitat de la GMR converteix en impulsos elèctrics. L'ús de GMR i, més tard, de TMR ha estat clau per augmentar la densitat d'emmagatzematge.

![Esquema d'un sensor GMR situat prop d'un conductor que transporta corrent, mesurant el camp magnètic que aquest genera](assets/07_Unitat5_Magnetoresistencies_img_10.png)

*Figura: Figura 5.35 Mesura de corrent sense contacte amb una GMR.*

**Mesura de corrent sense contacte.** Un conductor amb corrent crea un camp proporcional a la intensitat (llei de Biot-Savart) que un sensor GMR proper mesura. Aporta **aïllament galvànic complet**, **intrusivitat mínima** —el sensor substitueix la resistència *shunt*, sense haver d'interrompre el conductor— i capacitat de mesurar corrents continus i alterns. Es troba en alimentadors, convertidors de potència i electrònica industrial.

Els grans competidors, sobretot en contínua, són els **sensors d'efecte Hall** (unitat 7): es basen en la força de Lorentz sobre els portadors i generen una tensió transversal, de manera que el principi físic és diferent, però competeixen per les mateixes aplicacions.

> [!TIP] **Síntesi**
>
> Les magnetoresistències responen a camps continus i alterns. Les AMR de permalloy donen variacions del 2 %; el model depèn del quadrat del camp transversal, de manera que la resposta és parell, perd el signe i és plana a camp nul. L'estructura *barber pole* linealitza prop de zero i permet distingir el signe, mantenint la polarització i la deriva tèrmica. A les GMR, multicapes nanomètriques amb dispersió dependent de l'espín, antiparal·lel dona resistència alta i paral·lel, baixa, amb variacions del 20 %; la saturació delimita el marge útil. Les TMR, amb barrera aïllant i transport per túnel, són més sensibles i més complexes. La temperatura es compensa amb ponts i elements de referència. Aplicacions: posició, encoders, lectura magnètica i mesura de corrent amb aïllament galvànic i sense *shunt*.

[← 6. Sensors piezoresistius i galgues extensiomètriques](#sensors-piezoresistius-i-galgues-extensiomètriques)[8. Fotoresistències, higròmetres resistius i criteris de selecció →](#fotoresistències-higròmetres-resistius-i-criteris-de-selecció)

---

<!-- FIN CAPÍTULO: 07_Unitat5_Magnetoresistencies -->

---

<!-- INICIO CAPÍTULO: 08_Unitat5_LDR_higrometres_i_criteris -->

# Fotoresistències, higròmetres resistius i criteris de selecció

Sistemes de Mesura · **Unitat 5 — Sensors resistius** · Document 8 de 8

# Fotoresistències, higròmetres resistius i criteris de selecció

Dedicació estimada: 10 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar l'efecte fotoelèctric intern i la condició energètica que ha de complir un fotó.
> - Relacionar el material d'una LDR amb la resposta espectral i interpretar-ne el model empíric.
> - Descriure el mecanisme de conducció d'un higròmetre resistiu i justificar l'excitació en alterna.
> - Comparar les famílies de sensors resistius i aplicar criteris de selecció.

## 1 Fotoresistències (LDR)

Una **fotoresistència** o LDR (*Light Dependent Resistor*) és un sensor resistiu de semiconductor fotosensible la resistència del qual **disminueix** amb la il·luminació. En foscor gairebé total el material és pràcticament aïllant i la resistència pot superar les desenes de megaohm; sota il·luminació intensa cau diversos ordres de magnitud, fins als kΩ o menys. El material actiu és de banda prohibida estreta —sulfur de cadmi (CdS) o seleniür de cadmi (CdSe)—, i les LDR són senzilles i barates però d'exactitud limitada.

![Estructura d'una LDR: substrat ceràmic, capa de semiconductor fotosensible i elèctrodes interdigitats en forma de serpentina](assets/08_Unitat5_LDR_higrometres_i_criteris_img_1.png)

*Figura: Figura 5.36 Estructura típica d'una LDR: substrat ceràmic aïllant, capa fina de semiconductor fotosensible i elèctrodes interdigitats en forma de serpentina.*

La geometria interdigitada fa dues coses alhora: *escurça* el camí de corrent entre elèctrodes i *augmenta* l'àrea de material fotosensible actiu dins d'un xip reduït. La resistència en foscor la determinen la resistivitat intrínseca i la relació longitud/secció del camí conductor.

### Mecanisme físic i resposta espectral

El mecanisme és un **efecte fotoelèctric intern**: un fotó amb energia

$$
E_{fot\acute{o}} = h\nu = \frac{h\,c}{\lambda} \qquad (5.49)
$$

pot promoure un electró de la banda de valència a la de conducció, sempre que la seva energia sigui **superior a l'energia de banda prohibida**  $E_{\text{gap}}$
, creant un parell electró-forat que contribueix a la conducció. En augmentar el flux de fotons absorbits creix el nombre de portadors i la resistència baixa. El procés competeix amb la **recombinació**, amb una constant de temps que depèn dels defectes i les impureses, i això explica la resposta temporal *lenta* davant de canvis bruscos de llum.

![A dalt, esquema de la generació de parells electró-forat en un semiconductor per absorció de fotons; a baix, corbes de resposta espectral relativa de diversos materials en funció de la longitud d'ona](assets/08_Unitat5_LDR_higrometres_i_criteris_img_2.png)

*Figura: Figura 5.37 Mecanisme de generació de portadors i resposta espectral de diversos materials, per a diferents longituds d'ona i temperatures (en kelvin, entre parèntesis).*

Hi ha una longitud d'ona òptima de resposta màxima i la corba decau als dos costats: per a  $\lambda$
 massa gran —energia inferior a  $E_{\text{gap}}$
— els fotons no poden promoure electrons i la resposta és pràcticament nul·la; per a  $\lambda$
 massa curta augmenten la recombinació i les absorcions superficials. El material determina on cau el màxim: el **CdS**, clàssic de les LDR del visible, té el pic prop de **540 nm**, a la zona verda, coincidint aproximadament amb la màxima sensibilitat de l'ull humà; el **CdSe** el desplaça cap a longituds d'ona més llargues i el **PbS** cap a l'infraroig. La LDR és, doncs, un **detector espectralment selectiu**, i cal considerar la longitud d'ona de la font de llum.

### Model empíric, limitacions i aplicacions

$$
R_{\text{LDR}} = A\,L^{-\gamma} \qquad (5.50)
$$

amb  $L$
 la intensitat lumínica en lux i  $A$
 i  $\gamma$
 constants *pròpies de cada sensor*, amb toleràncies molt elevades: cal calibrar individualment cada dispositiu.

![Full d'especificacions tècniques d'una LDR comercial amb rangs de resistència, resistència de foscor i corbes característiques](assets/08_Unitat5_LDR_higrometres_i_criteris_img_3.png)

*Figura: Figura 5.38 Exemple d'especificacions tècniques d'una LDR comercial. Les fitxes donen el rang de resistència a una il·luminació de referència —per exemple de 8 a 20 kΩ a 10 lux, cosa que il·lustra la dispersió entre dispositius del mateix model— i la resistència de foscor, a 0 lux, de l'ordre d'1 MΩ o superior.*

Com que (5.50) prediu resistència infinita en foscor, aquesta es modela amb el paral·lel entre la resistència de foscor i l'expressió. Les fitxes especifiquen també la **potència màxima dissipable** i la **tensió màxima en borns**, ja que la LDR és un element resistiu excitat elèctricament, i les **temperatures de funcionament**. Es llegeix habitualment **en contínua**, amb un divisor de tensió.

Les limitacions són quatre: **no linealitat forta**; **toleràncies grans**, que obliguen a calibrar si es volen intensitats absolutes; **dependència amb la temperatura**, per l'activació tèrmica de portadors i la mobilitat; i **resposta lenta**, de mil·lisegons a segons, *més lenta* que la de fotodíodes o fototransistors. Les LDR no són, doncs, l'opció per a mesura ràpida ni precisa de llum, però són excel·lents per a detecció qualitativa de clar i fosc. Un divisor de tensió amb la LDR detecta quan la il·luminació travessa un **llindar**, activant un comparador: és la base de la **il·luminació automàtica** —fanals que s'encenen al vespre—, dels **detectors de nivell de líquid tèrbol** i de les **barreres lumíniques** d'alarma, on la interrupció del feix produeix una *pujada* brusca de resistència perquè el sensor passa d'il·luminat a fosc.

## 2 Higròmetres resistius

Els **higròmetres resistius** mesuren la **humitat relativa** (HR) a partir de la variació de resistència d'un material dielèctric higroscòpic: certs polímers on l'aigua penetra formant camins conductors microscòpics, i sals higroscòpiques. En sec la resistivitat és molt alta; quan augmenta la HR, les molècules adsorbides **faciliten camins iònics de conducció** i la resistivitat cau dràsticament. El que es mesura és, doncs, un canvi de *conductivitat efectiva*, de diversos ordres de magnitud. El sentit és **més humitat, menys resistència**, i la condició perquè funcioni és que el material pugui absorbir l'aigua.

![A l'esquerra, configuració interdigitada d'un higròmetre resistiu; al centre, encapsulament perforat; a la dreta, corbes de resistència enfront d'humitat relativa per a diverses temperatures](assets/08_Unitat5_LDR_higrometres_i_criteris_img_4.png)

*Figura: Figura 5.39 Exemple d'higròmetre resistiu. A l'esquerra, la configuració interdigitada bàsica sobre substrat aïllant rígid; al centre, l'encapsulament perforat que exposa el material higroscòpic a la humitat ambient; a la dreta, corbes típiques de relació HR-resistència amb la seva dependència de la temperatura.*

Els elèctrodes interdigitats augmenten la zona de contacte i faciliten mesurar canvis de conductivitat en una capa fina, i **formen també una capacitat paràsita**: molts fabricants especifiquen la component resistiva i la capacitiva. L'higròmetre es llegeix amb un senyal **altern** —per exemple 1 kHz— mesurant la part real de la impedància, cosa que redueix l'electròlisi i la polarització que apareixerien en contínua (unitat 8). El **rang de resistència és molt ampli**, de desenes de megaohm en sec a unitats de kΩ amb HR propera al 100 %: permet detectar humitats amb guanys modestos, però obliga a un circuit de rang dinàmic ampli.

La relació entre resistència i HR és fortament no lineal i depèn del material i de la temperatura, i **no hi ha un model universal senzill**, ni tan sols del tipus llei de potència de les LDR: els fabricants donen corbes  $R(\mathrm{HR})$
 per a diverses temperatures. Cal calibrar amb valors d'HR coneguts —un higròmetre de referència o solucions salines saturades— ajustant models empírics o interpolant sobre **taules de calibratge**. Per a una mateixa HR, la resistència varia fortament amb la temperatura per dues raons que s'acumulen: l'augment de  $T$
 incrementa la conductivitat iònica de l'aigua adsorbida, i la definició d'HR —quocient entre pressió parcial de vapor i pressió de saturació— fa que el contingut d'aigua per volum d'aire canviï amb  $T$
. A HR constant, doncs, escalfar acostuma a *disminuir* la resistència, i la compensació tèrmica continua sent necessària encara que la humitat sigui *relativa*: calen un **sensor de temperatura auxiliar** o un mòdul amb correcció interna.

Les limitacions són el **temps de resposta lent** —la difusió de l'aigua pot trigar de segons a minuts—, la **histèresi** entre cicles d'humitat creixent i decreixent, l'**envelliment** del dielèctric i la **contaminació** per vapors orgànics, pols o aerosols, que altera l'absorció i el calibratge i és una causa principal de deriva. Cal col·locar el sensor en un lloc representatiu però **protegit de la condensació directa** i recalibrar periòdicament. Mesura **humitat relativa**; la pressió absoluta de vapor requereix models addicionals. S'utilitzen en estacions meteorològiques, climatització, indústria alimentària i farmacèutica, i museus i arxius.

## 3 Recapitulació de la unitat

Darrere del terme "sensor resistiu" hi ha fenòmens molt diversos: la mobilitat dels electrons d'un metall (RTD), el nombre de portadors d'un semiconductor (termistors), la geometria i la resistivitat sota deformació (galgues), el camí i l'orientació d'espín dels electrons (magnetoresistències), la fotogeneració de portadors (LDR) i la conductivitat iònica (higròmetres). Malgrat això, **tots codifiquen el mesurand en el valor d'una resistència**: cal excitar-la, convertir-ne el canvi en tensió o corrent i digitalitzar-lo.

Cap família no és lineal pel sol fet d'ampliar el marge: la no linealitat és una propietat del mecanisme físic. Triar un sensor és decidir **quin sacrifici s'accepta**: els RTD de platí donen exactitud i intercanviabilitat a preu alt; les NTC, molta sensibilitat i rapidesa a preu baix amb no linealitat exponencial; les galgues metàl·liques, robustesa i linealitat amb poca sensibilitat, i les semiconductores el contrari; les GMR i TMR, grans canvis amb camps petits però amb fabricació complexa i saturació; les LDR i els higròmetres, senzillesa i preu baix amb toleràncies grans i lentitud.

Algunes regles travessen la unitat. Una sensibilitat elevada **no garanteix exactitud**, i com més gran és la dispersió entre unitats més important esdevé el calibratge individual, mentre que una intercanviabilitat alta l'estalvia. Les toleràncies del sensor i del condicionament formen part de la **incertesa global** (unitat 2). L'excitació en corrent o en tensió afecta alhora la sensibilitat i la potència dissipada. La **resposta dinàmica** la limita el fenomen físic —difusió tèrmica, difusió d'aigua, recombinació—, no la part elèctrica. I la compensació de magnituds d'influència es fa amb sensors auxiliars, configuracions diferencials o calibratge, amb el **pont de Wheatstone** aplicable a galgues, RTD i magnetoresistències.

> [!TIP] **Síntesi**
>
> Una LDR és una fotoresistència de semiconductor —CdS amb pic prop de 540 nm; CdSe o PbS cap a l'infraroig— on els fotons amb energia superior a la banda prohibida generen parells electró-forat i redueixen la resistència. Els elèctrodes interdigitats augmenten l'àrea activa i escurcen el camí de corrent. El model és  $R=AL^{-\gamma}$
> amb paràmetres propis de cada dispositiu; les limitacions són no linealitat, dispersió, deriva tèrmica i lentitud. Un higròmetre resistiu mesura HR perquè l'aigua absorbida crea camins iònics i redueix la resistivitat; s'excita en alterna per evitar electròlisi, té component capacitiva i pateix histèresi, envelliment i contaminació. Totes les famílies codifiquen el mesurand en una resistència que cal excitar, llegir i condicionar, i triar-ne una és un compromís entre exactitud, sensibilitat, cost, velocitat i robustesa.

[← 7. Magnetoresistències](#magnetoresistències)

---

<!-- FIN CAPÍTULO: 08_Unitat5_LDR_higrometres_i_criteris -->

---

<!-- INICIO CAPÍTULO: 09_Entrenament_Tema5 -->

# Entrenament V/F · Unitat 5: Sensors resistius

Encerts: **0** / 0Tots els blocs
Ordre aleatori
Reinicia

### Entrenament completat

Torna-ho a provar

---

## 🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)

> [!TIP] **Com utilitzar aquest material d'entrenament**
> Aquest banc conté **50 afirmacions clau** dissenyades per consolidar els conceptes de la unitat i preparar els qüestionaris d'avaluació continuada.
> Intenta respondre mentalment **Vertader (V)** o **Fals (F)** abans de desplegar la solució i la justificació tècnica.

### Qüestió 01
> 📌 **Afirmació:** *Els sensors capacitius i inductius requereixen excitació en corrent altern i condicionament que tingui en compte el desfasament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En els sensors reactius el mesurand afecta la part imaginària de la impedància, de manera que cal excitació alterna i condicionament sensible al desfasament (unitats 7 i 8).*

> **📚 Document de referència:** `1. Sensors moduladors, fonaments físics i model general`
> </details>

### Qüestió 02
> 📌 **Afirmació:** *La temperatura pot actuar com a magnitud d'influència en sensors resistius que mesuren magnituds diferents de la temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Una galga, una magnetoresistència, una LDR o un higròmetre canvien de resistència amb la temperatura encara que no sigui el mesurand: és un problema recurrent a tota la unitat.*

> **📚 Document de referència:** `1. Sensors moduladors, fonaments físics i model general`
> </details>

### Qüestió 03
> 📌 **Afirmació:** *Amb un coeficient de Poisson d'aproximadament 0,3, el factor geomètric 1+2nu val de l'ordre d'1,6.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb ν ≈ 0,3 resulta 1 + 2·0,3 = 1,6, que és la part geomètrica del factor de galga.*

> **📚 Document de referència:** `1. Sensors moduladors, fonaments físics i model general`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *El pont de Wheatstone només es pot utilitzar amb galgues extensiomètriques.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El pont s'utilitza amb galgues, però també amb RTD i amb magnetoresistències.*

> **📚 Document de referència:** `1. Sensors moduladors, fonaments físics i model general`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *En un sensor resistiu, el mesurand afecta sobretot la part imaginària de la impedància.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En un sensor resistiu el mesurand afecta sobretot la part real; si afectés la imaginària seria un sensor capacitiu o inductiu.*

> **📚 Document de referència:** `1. Sensors moduladors, fonaments físics i model general`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *Que un sensor resistiu admeti un model en contínua implica que la seva reactància paràsita és rigorosament nul·la.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Tot dispositiu real té capacitats i inductàncies paràsites. El model en contínua val perquè són negligibles davant de R en les condicions habituals, no perquè siguin nul·les.*

> **📚 Document de referència:** `1. Sensors moduladors, fonaments físics i model general`
> </details>

### Qüestió 07
> 📌 **Afirmació:** *El coeficient de temperatura nominal d'una Pt-100 val aproximadament 0,00385 per grau Celsius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És el valor nominal del platí normalitzat: la resistència augmenta un 0,385 % per kelvin, és a dir 0,385 Ω/°C en una Pt-100.*

> **📚 Document de referència:** `2. Detectors de temperatura resistius (RTD)`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *En un RTD metàl·lic, la generació de portadors és el mecanisme dominant de la variació de resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En un metall la densitat de portadors és pràcticament constant; el que canvia és la mobilitat. La generació de portadors és el mecanisme dels semiconductors, i dona el comportament contrari dels NTC.*

> **📚 Document de referència:** `2. Detectors de temperatura resistius (RTD)`
> </details>

### Qüestió 09
> 📌 **Afirmació:** *L'error referit a l'entrada s'obté multiplicant la diferència de resistència per la sensibilitat del sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *S'obté dividint la diferència de resistència per la sensibilitat del sensor, aproximadament R0·α. És el procediment general per referir un error de sortida a l'escala d'entrada.*

> **📚 Document de referència:** `2. Detectors de temperatura resistius (RTD)`
> </details>

### Qüestió 10
> 📌 **Afirmació:** *El coeficient B del model de Callendar-Van Dusen d'una Pt-100 és petit i negatiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *B ≈ −5,775·10⁻⁷ °C⁻²: és petit i negatiu, i és el que corba la característica per sota de la recta del model lineal.*

> **📚 Document de referència:** `2. Detectors de temperatura resistius (RTD)`
> </details>

### Qüestió 11
> 📌 **Afirmació:** *Els RTD de fil enrotllat encapsulats destaquen per la seva robustesa davant vibració i ambients agressius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Encapsulats en tub d'acer inoxidable resisteixen bé vibració, impactes i ambients agressius, a canvi de ser més lents i més cars que els de pel·lícula metàl·lica.*

> **📚 Document de referència:** `2. Detectors de temperatura resistius (RTD)`
> </details>

### Qüestió 12
> 📌 **Afirmació:** *El coeficient de dissipació tèrmica té unitats de volts per grau.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Les unitats són de potència dividida per temperatura, habitualment mW/K, i el valor depèn sobretot del sensor, l'encapsulat i el medi.*

> **📚 Document de referència:** `3. Autoescalfament, excitació i resposta dinàmica`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *Amb excitació a corrent constant, la potència dissipada és proporcional al corrent i al quadrat de la resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És proporcional al quadrat del corrent i a la primera potència de la resistència: P = I²R. Duplicar el corrent multiplica la potència per quatre.*

> **📚 Document de referència:** `3. Autoescalfament, excitació i resposta dinàmica`
> </details>

### Qüestió 14
> 📌 **Afirmació:** *Com millor és la transferència tèrmica amb el medi, menor és l'autoescalfament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En líquids la transferència és molt millor que en aire quiet, i pitjor que tot en buit, on només hi ha radiació.*

> **📚 Document de referència:** `3. Autoescalfament, excitació i resposta dinàmica`
> </details>

### Qüestió 15
> 📌 **Afirmació:** *En buit, la dissipació de calor del sensor es produeix principalment per radiació i és el cas més desfavorable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Sense convecció ni conducció cap al medi, només queda la radiació, i per això el buit és la situació més desfavorable.*

> **📚 Document de referència:** `3. Autoescalfament, excitació i resposta dinàmica`
> </details>

### Qüestió 16
> 📌 **Afirmació:** *La resposta temporal d'un RTD és instantània perquè la resistència elèctrica canvia sense retard.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El retard l'introdueix la transferència de calor, no l'electricitat: el sensor es comporta com un sistema de primer ordre amb una constant de temps tèrmica.*

> **📚 Document de referència:** `3. Autoescalfament, excitació i resposta dinàmica`
> </details>

### Qüestió 17
> 📌 **Afirmació:** *L'excitació polsada només redueix l'escalfament mitjà si el pols és curt comparat amb la dinàmica tèrmica del sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Si el pols és llarg comparat amb la constant de temps tèrmica, el sensor arriba igualment a la temperatura d'equilibri i no es guanya res.*

> **📚 Document de referència:** `3. Autoescalfament, excitació i resposta dinàmica`
> </details>

### Qüestió 18
> 📌 **Afirmació:** *El coeficient de temperatura local d'una NTC és negatiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El coeficient local val α ≈ −β/Tx², i el signe negatiu reflecteix que la resistència d'una NTC decreix quan puja la temperatura.*

> **📚 Document de referència:** `4. Termistors NTC: models i linealització`
> </details>

### Qüestió 19
> 📌 **Afirmació:** *Els termistors presenten una sensibilitat relativa més baixa que els RTD de platí.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al revés: el canvi relatiu de resistència per grau d'un termistor pot ser fins a vint vegades superior al d'un RTD.*

> **📚 Document de referència:** `4. Termistors NTC: models i linealització`
> </details>

### Qüestió 20
> 📌 **Afirmació:** *La temperatura de referència habitual d'una NTC és 298,15 K, és a dir 25 graus Celsius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El model exponencial de dos paràmetres es referencia habitualment a T0 = 298,15 K, i totes les temperatures hi han d'anar en kelvin.*

> **📚 Document de referència:** `4. Termistors NTC: models i linealització`
> </details>

### Qüestió 21
> 📌 **Afirmació:** *Un valor de beta més gran implica una variació de resistència més feble amb la temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al revés: un β més gran significa una caiguda més abrupta de la resistència amb la temperatura, és a dir més sensibilitat.*

> **📚 Document de referència:** `4. Termistors NTC: models i linealització`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *La linealització analògica manté exactament la mateixa sensibilitat que la NTC sense linealitzar.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La corba equivalent varia menys amb la temperatura que la NTC nua: es guanya linealitat a canvi de sensibilitat.*

> **📚 Document de referència:** `4. Termistors NTC: models i linealització`
> </details>

### Qüestió 23
> 📌 **Afirmació:** *Perquè la resistència de linealització sigui positiva cal que beta sigui més gran que dues vegades la temperatura d'interès.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *De R = Rth(Tx)·(β−2Tx)/(β+2Tx), el numerador ha de ser positiu. Amb valors habituals es compleix folgadament: β de milers de kelvin davant de 2Tx d'uns 600 K.*

> **📚 Document de referència:** `4. Termistors NTC: models i linealització`
> </details>

### Qüestió 24
> 📌 **Afirmació:** *Les NTC tenen resistències nominals de diversos kilohms a desenes de kilohms a 25 graus Celsius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Els valors típics van de diversos kΩ a desenes de kΩ a 25 °C, i és precisament el que minimitza l'efecte de les resistències de cablejat.*

> **📚 Document de referència:** `5. Termistors: construcció, PTC i aplicacions`
> </details>

### Qüestió 25
> 📌 **Afirmació:** *La sinterització a alta temperatura forma una ceràmica densa amb les propietats elèctriques buscades.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És el pas del procés que fixa les propietats elèctriques, i per això R0 i β depenen tant del cicle de sinterització: d'aquí ve la dispersió entre unitats.*

> **📚 Document de referència:** `5. Termistors: construcció, PTC i aplicacions`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *En augmentar el corrent, la corba tensió-corrent d'un termistor queda per damunt de la recta òhmica.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Queda per sota: en autoescalfar-se, la NTC baixa de resistència i el quocient tensió-corrent disminueix respecte del valor nominal en fred.*

> **📚 Document de referència:** `5. Termistors: construcció, PTC i aplicacions`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *Els encapsulats SMD de NTC són incompatibles amb el muntatge automatitzat en plaques de circuit imprès.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al contrari: els encapsulats SMD estan pensats per a la soldadura per reflow i el muntatge automatitzat.*

> **📚 Document de referència:** `5. Termistors: construcció, PTC i aplicacions`
> </details>

### Qüestió 28
> 📌 **Afirmació:** *Les NTC són més barates que els RTD de platí.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El cost molt inferior és el primer avantatge de les NTC enfront dels RTD de platí, juntament amb la sensibilitat i la mida.*

> **📚 Document de referència:** `5. Termistors: construcció, PTC i aplicacions`
> </details>

### Qüestió 29
> 📌 **Afirmació:** *El mòdul de Young té dimensions de pressió i mesura la rigidesa del material.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El mòdul de Young té dimensions de pressió —uns 200 GPa per a l'acer, 70 GPa per a l'alumini— i mesura la rigidesa, no cap propietat elèctrica.*

> **📚 Document de referència:** `6. Sensors piezoresistius i galgues extensiomètriques`
> </details>

### Qüestió 30
> 📌 **Afirmació:** *Un transductor de pressió piezoresistiu necessita que la pressió generi una tensió termoelèctrica.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La cadena causal és pressió → deformació de la membrana → canvi de resistència. La tensió termoelèctrica correspondria a un termoparell.*

> **📚 Document de referència:** `6. Sensors piezoresistius i galgues extensiomètriques`
> </details>

### Qüestió 31
> 📌 **Afirmació:** *Una roseta de tres galgues a 0, 45 i 90 graus permet inferir el mòdul i la direcció de la tensió aplicada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Coneguts el mòdul de Young i el coeficient de Poisson, les tres lectures resolen les equacions de transformació de tensió plana.*

> **📚 Document de referència:** `6. Sensors piezoresistius i galgues extensiomètriques`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *El factor de galga és la relació entre la tensió d'alimentació i la intensitat de corrent.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El factor de galga és el quocient entre el canvi relatiu de resistència i la deformació unitària; no hi intervenen ni tensions d'alimentació ni corrents.*

> **📚 Document de referència:** `6. Sensors piezoresistius i galgues extensiomètriques`
> </details>

### Qüestió 33
> 📌 **Afirmació:** *Les galgues de referència no carregades mecànicament permeten compensar derives tèrmiques en pont.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Situades on no reben tensió mecànica i connectades en pont, la seva variació tèrmica cancel·la la de les galgues actives.*

> **📚 Document de referència:** `6. Sensors piezoresistius i galgues extensiomètriques`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *El model R = R0(1+k·epsilon) és vàlid dins de la zona elàstica i dels límits del fabricant.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El model lineal val en zona elàstica i dins dels límits de deformació del fabricant: uns 40.000 µε en galgues metàl·liques i de 1000 a 3000 µε en semiconductores.*

> **📚 Document de referència:** `6. Sensors piezoresistius i galgues extensiomètriques`
> </details>

### Qüestió 35
> 📌 **Afirmació:** *La deformació unitària s'expressa en pascals.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La deformació unitària és un quocient de longituds i, per tant, adimensional; els pascals corresponen a la tensió mecànica.*

> **📚 Document de referència:** `6. Sensors piezoresistius i galgues extensiomètriques`
> </details>

### Qüestió 36
> 📌 **Afirmació:** *Els fabricants integren magnetoresistències en ponts de Wheatstone per amplificar les variacions comunes de temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El pont cancel·la les variacions comunes i deixa passar el diferencial: serveix per compensar la deriva tèrmica, no per amplificar-la.*

> **📚 Document de referència:** `7. Magnetoresistències`
> </details>

### Qüestió 37
> 📌 **Afirmació:** *Al model de l'AMR bàsica, el camp transversal apareix elevat al quadrat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El model conté (Hy/Hx)²: la funció és parell i, per tant, simètrica respecte de camp nul.*

> **📚 Document de referència:** `7. Magnetoresistències`
> </details>

### Qüestió 38
> 📌 **Afirmació:** *Les TMR són tecnològicament més simples que les AMR perquè no requereixen control de capes fines.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al revés: una TMR exigeix un control nanomètric del gruix de la barrera aïllant que l'AMR no necessita. La complexitat creix en el mateix ordre que la sensibilitat.*

> **📚 Document de referència:** `7. Magnetoresistències`
> </details>

### Qüestió 39
> 📌 **Afirmació:** *La resposta d'una AMR bàsica és una funció imparell del camp transversal.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És una funció parell: el model depèn del quadrat del camp, de manera que l'AMR bàsica dona el mòdul però no el signe.*

> **📚 Document de referència:** `7. Magnetoresistències`
> </details>

### Qüestió 40
> 📌 **Afirmació:** *En una GMR, la dispersió dependent de l'espín dels electrons és clau per entendre el canvi de resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La probabilitat de dispersió a les capes ferromagnètiques depèn de si l'espín està alineat amb la magnetització local: antiparal·lel dona resistència alta i paral·lel, baixa.*

> **📚 Document de referència:** `7. Magnetoresistències`
> </details>

### Qüestió 41
> 📌 **Afirmació:** *L'estructura barber pole intercala seccions de permalloy amb seccions d'alumini.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Les seccions d'alumini, paramagnètic, formen contactes inclinats 45° que obliguen el corrent efectiu a formar aquest angle dins del permalloy.*

> **📚 Document de referència:** `7. Magnetoresistències`
> </details>

### Qüestió 42
> 📌 **Afirmació:** *En una LDR, la conductivitat disminueix quan augmenta el flux de fotons absorbits.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En absorbir fotons amb prou energia es generen parells electró-forat: creix el nombre de portadors, la conductivitat augmenta i la resistència baixa.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 43
> 📌 **Afirmació:** *En un higròmetre resistiu, l'absorció d'aigua fa augmentar la resistència diversos ordres de magnitud.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al revés: l'aigua adsorbida facilita camins iònics de conducció i la resistivitat cau diversos ordres de magnitud. Més humitat, menys resistència.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 44
> 📌 **Afirmació:** *La resposta dinàmica d'un sensor resistiu la limita el fenomen físic, no la part elèctrica.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El que limita la velocitat és la difusió tèrmica, la difusió d'aigua o la recombinació de portadors segons la família; la resistència elèctrica canvia sense retard apreciable.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 45
> 📌 **Afirmació:** *La histèresi entre cicles d'humitat creixent i decreixent és una limitació dels higròmetres resistius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La corba R(HR) segueix camins diferents en pujada i en baixada. És una de les limitacions dels higròmetres, juntament amb la lentitud, l'envelliment i la contaminació.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 46
> 📌 **Afirmació:** *En foscor, una LDR presenta una resistència molt baixa perquè no es generen parells electró-forat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En foscor gairebé total el material és pràcticament aïllant i la resistència pot superar les desenes de megaohm; no és nul·la ni baixa.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 47
> 📌 **Afirmació:** *Un fotó genera portadors en una LDR només si la seva energia supera l'energia de banda prohibida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'efecte fotoelèctric intern exigeix que l'energia del fotó superi l'energia de banda prohibida; per sota, la resposta és pràcticament nul·la.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *Els elèctrodes interdigitats són habituals en higròmetres resistius perquè augmenten la zona de contacte.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Augmenten la zona de contacte amb el material sensible i faciliten mesurar canvis de conductivitat en una capa fina.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *Per a una mateixa humitat relativa, un augment de temperatura acostuma a disminuir la resistència del sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'augment de temperatura incrementa la conductivitat iònica de l'aigua adsorbida, de manera que a HR constant la resistència baixa. Per això cal compensació tèrmica.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

### Qüestió 50
> 📌 **Afirmació:** *Tots els fotons generen portadors útils en una LDR, independentment de la seva energia.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Els fotons amb energia inferior a l'energia de banda prohibida no poden promoure electrons a la banda de conducció.*

> **📚 Document de referència:** `8. Fotoresistències, higròmetres i criteris de selecció`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | En els sensors reactius el mesurand afecta la part imaginària de la impedància, de manera que cal excitació alterna i... | 1. Sensors moduladors, fonaments físics i model general |
| **02** | **V** | Una galga, una magnetoresistència, una LDR o un higròmetre canvien de resistència amb la temperatura encara que no si... | 1. Sensors moduladors, fonaments físics i model general |
| **03** | **V** | Amb ν ≈ 0,3 resulta 1 + 2·0,3 = 1,6, que és la part geomètrica del factor de galga. | 1. Sensors moduladors, fonaments físics i model general |
| **04** | **F** | El pont s'utilitza amb galgues, però també amb RTD i amb magnetoresistències. | 1. Sensors moduladors, fonaments físics i model general |
| **05** | **F** | En un sensor resistiu el mesurand afecta sobretot la part real; si afectés la imaginària seria un sensor capacitiu o ... | 1. Sensors moduladors, fonaments físics i model general |
| **06** | **F** | Tot dispositiu real té capacitats i inductàncies paràsites. El model en contínua val perquè són negligibles davant de... | 1. Sensors moduladors, fonaments físics i model general |
| **07** | **V** | És el valor nominal del platí normalitzat: la resistència augmenta un 0,385 % per kelvin, és a dir 0,385 Ω/°C en una ... | 2. Detectors de temperatura resistius (RTD) |
| **08** | **F** | En un metall la densitat de portadors és pràcticament constant; el que canvia és la mobilitat. La generació de portad... | 2. Detectors de temperatura resistius (RTD) |
| **09** | **F** | S'obté dividint la diferència de resistència per la sensibilitat del sensor, aproximadament R0·α. És el procediment g... | 2. Detectors de temperatura resistius (RTD) |
| **10** | **V** | B ≈ −5,775·10⁻⁷ °C⁻²: és petit i negatiu, i és el que corba la característica per sota de la recta del model lineal. | 2. Detectors de temperatura resistius (RTD) |
| **11** | **V** | Encapsulats en tub d'acer inoxidable resisteixen bé vibració, impactes i ambients agressius, a canvi de ser més lents... | 2. Detectors de temperatura resistius (RTD) |
| **12** | **F** | Les unitats són de potència dividida per temperatura, habitualment mW/K, i el valor depèn sobretot del sensor, l'enca... | 3. Autoescalfament, excitació i resposta dinàmica |
| **13** | **F** | És proporcional al quadrat del corrent i a la primera potència de la resistència: P = I²R. Duplicar el corrent multip... | 3. Autoescalfament, excitació i resposta dinàmica |
| **14** | **V** | En líquids la transferència és molt millor que en aire quiet, i pitjor que tot en buit, on només hi ha radiació. | 3. Autoescalfament, excitació i resposta dinàmica |
| **15** | **V** | Sense convecció ni conducció cap al medi, només queda la radiació, i per això el buit és la situació més desfavorable. | 3. Autoescalfament, excitació i resposta dinàmica |
| **16** | **F** | El retard l'introdueix la transferència de calor, no l'electricitat: el sensor es comporta com un sistema de primer o... | 3. Autoescalfament, excitació i resposta dinàmica |
| **17** | **V** | Si el pols és llarg comparat amb la constant de temps tèrmica, el sensor arriba igualment a la temperatura d'equilibr... | 3. Autoescalfament, excitació i resposta dinàmica |
| **18** | **V** | El coeficient local val α ≈ −β/Tx², i el signe negatiu reflecteix que la resistència d'una NTC decreix quan puja la t... | 4. Termistors NTC: models i linealització |
| **19** | **F** | És al revés: el canvi relatiu de resistència per grau d'un termistor pot ser fins a vint vegades superior al d'un RTD. | 4. Termistors NTC: models i linealització |
| **20** | **V** | El model exponencial de dos paràmetres es referencia habitualment a T0 = 298,15 K, i totes les temperatures hi han d'... | 4. Termistors NTC: models i linealització |
| **21** | **F** | És al revés: un β més gran significa una caiguda més abrupta de la resistència amb la temperatura, és a dir més sensi... | 4. Termistors NTC: models i linealització |
| **22** | **F** | La corba equivalent varia menys amb la temperatura que la NTC nua: es guanya linealitat a canvi de sensibilitat. | 4. Termistors NTC: models i linealització |
| **23** | **V** | De R = Rth(Tx)·(β−2Tx)/(β+2Tx), el numerador ha de ser positiu. Amb valors habituals es compleix folgadament: β de mi... | 4. Termistors NTC: models i linealització |
| **24** | **V** | Els valors típics van de diversos kΩ a desenes de kΩ a 25 °C, i és precisament el que minimitza l'efecte de les resis... | 5. Termistors: construcció, PTC i aplicacions |
| **25** | **V** | És el pas del procés que fixa les propietats elèctriques, i per això R0 i β depenen tant del cicle de sinterització: ... | 5. Termistors: construcció, PTC i aplicacions |
| **26** | **F** | Queda per sota: en autoescalfar-se, la NTC baixa de resistència i el quocient tensió-corrent disminueix respecte del ... | 5. Termistors: construcció, PTC i aplicacions |
| **27** | **F** | És al contrari: els encapsulats SMD estan pensats per a la soldadura per reflow i el muntatge automatitzat. | 5. Termistors: construcció, PTC i aplicacions |
| **28** | **V** | El cost molt inferior és el primer avantatge de les NTC enfront dels RTD de platí, juntament amb la sensibilitat i la... | 5. Termistors: construcció, PTC i aplicacions |
| **29** | **V** | El mòdul de Young té dimensions de pressió —uns 200 GPa per a l'acer, 70 GPa per a l'alumini— i mesura la rigidesa, n... | 6. Sensors piezoresistius i galgues extensiomètriques |
| **30** | **F** | La cadena causal és pressió → deformació de la membrana → canvi de resistència. La tensió termoelèctrica correspondri... | 6. Sensors piezoresistius i galgues extensiomètriques |
| **31** | **V** | Coneguts el mòdul de Young i el coeficient de Poisson, les tres lectures resolen les equacions de transformació de te... | 6. Sensors piezoresistius i galgues extensiomètriques |
| **32** | **F** | El factor de galga és el quocient entre el canvi relatiu de resistència i la deformació unitària; no hi intervenen ni... | 6. Sensors piezoresistius i galgues extensiomètriques |
| **33** | **V** | Situades on no reben tensió mecànica i connectades en pont, la seva variació tèrmica cancel·la la de les galgues acti... | 6. Sensors piezoresistius i galgues extensiomètriques |
| **34** | **V** | El model lineal val en zona elàstica i dins dels límits de deformació del fabricant: uns 40.000 µε en galgues metàl·l... | 6. Sensors piezoresistius i galgues extensiomètriques |
| **35** | **F** | La deformació unitària és un quocient de longituds i, per tant, adimensional; els pascals corresponen a la tensió mec... | 6. Sensors piezoresistius i galgues extensiomètriques |
| **36** | **F** | El pont cancel·la les variacions comunes i deixa passar el diferencial: serveix per compensar la deriva tèrmica, no p... | 7. Magnetoresistències |
| **37** | **V** | El model conté (Hy/Hx)²: la funció és parell i, per tant, simètrica respecte de camp nul. | 7. Magnetoresistències |
| **38** | **F** | És al revés: una TMR exigeix un control nanomètric del gruix de la barrera aïllant que l'AMR no necessita. La complex... | 7. Magnetoresistències |
| **39** | **F** | És una funció parell: el model depèn del quadrat del camp, de manera que l'AMR bàsica dona el mòdul però no el signe. | 7. Magnetoresistències |
| **40** | **V** | La probabilitat de dispersió a les capes ferromagnètiques depèn de si l'espín està alineat amb la magnetització local... | 7. Magnetoresistències |
| **41** | **V** | Les seccions d'alumini, paramagnètic, formen contactes inclinats 45° que obliguen el corrent efectiu a formar aquest ... | 7. Magnetoresistències |
| **42** | **F** | En absorbir fotons amb prou energia es generen parells electró-forat: creix el nombre de portadors, la conductivitat ... | 8. Fotoresistències, higròmetres i criteris de selecció |
| **43** | **F** | És al revés: l'aigua adsorbida facilita camins iònics de conducció i la resistivitat cau diversos ordres de magnitud.... | 8. Fotoresistències, higròmetres i criteris de selecció |
| **44** | **V** | El que limita la velocitat és la difusió tèrmica, la difusió d'aigua o la recombinació de portadors segons la família... | 8. Fotoresistències, higròmetres i criteris de selecció |
| **45** | **V** | La corba R(HR) segueix camins diferents en pujada i en baixada. És una de les limitacions dels higròmetres, juntament... | 8. Fotoresistències, higròmetres i criteris de selecció |
| **46** | **F** | En foscor gairebé total el material és pràcticament aïllant i la resistència pot superar les desenes de megaohm; no é... | 8. Fotoresistències, higròmetres i criteris de selecció |
| **47** | **V** | L'efecte fotoelèctric intern exigeix que l'energia del fotó superi l'energia de banda prohibida; per sota, la respost... | 8. Fotoresistències, higròmetres i criteris de selecció |
| **48** | **V** | Augmenten la zona de contacte amb el material sensible i faciliten mesurar canvis de conductivitat en una capa fina. | 8. Fotoresistències, higròmetres i criteris de selecció |
| **49** | **V** | L'augment de temperatura incrementa la conductivitat iònica de l'aigua adsorbida, de manera que a HR constant la resi... | 8. Fotoresistències, higròmetres i criteris de selecció |
| **50** | **F** | Els fotons amb energia inferior a l'energia de banda prohibida no poden promoure electrons a la banda de conducció. | 8. Fotoresistències, higròmetres i criteris de selecció |

<!-- FIN CAPÍTULO: 09_Entrenament_Tema5 -->

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
| **(5.1)** | $Z = R + jX$ |
| **(5.2)** | $Z(x) = R(x) + jX(x)$ |
| **(5.3)** | $R = \rho\,\frac{l}{A}$ |
| **(5.4)** | $\frac{\Delta R}{R} \approx \frac{\Delta \rho}{\rho} + \frac{\Delta l}{l} - \frac{\Delta A}{A}$ |
| **(5.5)** | $\sigma = E\,\varepsilon$ |
| **(5.6)** | $\frac{\Delta A}{A} \approx -2\nu\varepsilon$ |
| **(5.7)** | $\frac{\Delta R}{R} \approx (1+2\nu)\,\varepsilon$ |
| **(5.8)** | $\frac{\Delta l}{l_0} = \alpha\,\Delta T$ |
| **(5.9)** | $\frac{\Delta R}{R} \approx \alpha\Delta T - 2\alpha\Delta T = -\alpha\,\Delta T$ |
| **(5.10)** | $\sigma = n\,q\,\mu$ |
| **(5.11)** | $R(T) \approx R_0\left[1+\alpha\,(T-T_0)\right]$ |
| **(5.12)** | $R(x) = R_0\left[1+g(x-x_0)\right]$ |
| **(5.13)** | $R(T) = f(T)$ |
| **(5.14)** | $R(T) = R_0\left[1+\alpha_1\Delta T+\alpha_2(\Delta T)^2+\cdots+\alpha_n(\Delta T)^n\right]$ |
| **(5.15)** | $R(T) = R_0\left[1+A\,T+B\,T^2\right]$ |
| **(5.16)** | $R(T) = R_0\left[1+A\,T+B\,T^2+C\,(T-100)\,T^3\right]$ |
| **(5.17)** | $R(T) \approx R_0\left(1+\alpha\,T\right)$ |
| **(5.18)** | $T_{\text{sensor}} = T_{\text{ambient}} + \frac{P_{\text{sensor}}}{\delta}$ |
| **(5.19)** | $P_{\text{sensor}} = I^2 R$ |
| **(5.20)** | $P_{\text{sensor}} = \frac{V^2}{R}$ |
| **(5.21)** | $V_R = V\,\frac{R}{R+R_{\text{div}}}$ |
| **(5.22)** | $P_{\text{sensor}} = \frac{V^2 R}{(R+R_{\text{div}})^2}$ |
| **(5.23)** | $R = R_{\text{div}}$ |
| **(5.24)** | $P_{\text{sensor}} = I^2\,\frac{R_{\text{div}}^2\,R}{(R+R_{\text{div}})^2}$ |
| **(5.25)** | $\tau\,\frac{dT_{\text{sensor}}}{dt} + T_{\text{sensor}} = T_{\text{medi}}$ |
| **(5.26)** | $R_{\text{NTC}}(T) = R_0\,\exp\left[\beta\left(\frac{1}{T}-\frac{1}{T_0}\right)\right]$ |
| **(5.27)** | $R_{\text{NTC}}(T) \approx R_x\left[1+\alpha\,(T-T_x)\right]$ |
| **(5.28)** | $\alpha \approx -\frac{\beta}{T_x^{\,2}}$ |
| **(5.29)** | $\frac{1}{T} = a + b\,\ln(R) + c\left[\ln(R)\right]^3$ |
| **(5.30)** | $R_{\text{eq}}(T) = \frac{R_{\text{th}}(T)\,R}{R_{\text{th}}(T)+R}$ |
| **(5.31)** | $R = R_{\text{th}}(T_x)\,\frac{\beta-2T_x}{\beta+2T_x}$ |
| **(5.32)** | $V_{\text{out}}(T) = V\,\frac{R}{R+R_{\text{th}}(T)}$ |
| **(5.33)** | $R = R_{\text{th}}(T_x)\,\frac{\beta-2T_x}{\beta+2T_x}$ |
| **(5.34)** | $\sigma = \frac{F}{A}$ |
| **(5.35)** | $\varepsilon = \frac{\Delta l}{l_0}$ |
| **(5.36)** | $\sigma = E\,\varepsilon$ |
| **(5.37)** | $\frac{\Delta A}{A} = -2\,\nu\,\varepsilon$ |
| **(5.38)** | $R = \rho\,\frac{l}{A}$ |
| **(5.39)** | $\frac{\Delta R}{R} \approx \frac{\Delta\rho}{\rho} + \frac{\Delta l}{l} - \frac{\Delta A}{A}$ |
| **(5.40)** | $\frac{\Delta l}{l} = \varepsilon$ |
| **(5.41)** | $\frac{\Delta A}{A} = -2\nu\,\varepsilon$ |
| **(5.42)** | $\frac{\Delta\rho}{\rho} = k_1\,\varepsilon$ |
| **(5.43)** | $\frac{\Delta R}{R} = k_1\varepsilon + \varepsilon + 2\nu\varepsilon = \left(1+2\nu+k_1\right)\varepsilon$ |
| **(5.44)** | $k = \frac{\Delta R/R}{\varepsilon}$ |
| **(5.45)** | $k = 1+2\nu+k_1$ |
| **(5.46)** | $R = R_0\left(1+k\,\varepsilon\right)$ |
| **(5.47)** | $R = R_{\max} - \Delta R\,\frac{(H_y/H_x)^2}{1+(H_y/H_x)^2}$ |
| **(5.48)** | $R = R_0 + \frac{\Delta R}{2}\,\frac{(H_y/H_0)}{\sqrt{1+(H_y/H_0)^2}}$ |
| **(5.49)** | $E_{fot\acute{o}} = h\nu = \frac{h\,c}{\lambda}$ |
| **(5.50)** | $R_{\text{LDR}} = A\,L^{-\gamma}$ |