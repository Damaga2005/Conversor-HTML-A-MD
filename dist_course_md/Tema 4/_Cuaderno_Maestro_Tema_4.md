# 📚 Cuaderno Maestro: Tema 4

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 4` | 📄 **Capítulos incluidos:** 8  
> 📅 **Generado:** 2026-09-11 19:09

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 4 — Soroll · Lectura prèvia](#unitat-4-soroll-lectura-prèvia)
2. [Introducció al soroll i caracterització estadística](#introducció-al-soroll-i-caracterització-estadística)
   - [1 Què és el soroll en un sistema de mesura](#1-què-és-el-soroll-en-un-sistema-de-mesura)
3. [Soroll tèrmic](#soroll-tèrmic)
   - [1 Origen i models del soroll tèrmic](#1-origen-i-models-del-soroll-tèrmic)
   - [2 Les expressions fonamentals](#2-les-expressions-fonamentals)
   - [3 Soroll en excés i xarxes passives](#3-soroll-en-excés-i-xarxes-passives)
4. [Amplada de banda equivalent de soroll](#amplada-de-banda-equivalent-de-soroll)
   - [1 Per què una amplada de banda «equivalent»](#1-per-què-una-amplada-de-banda-equivalent)
   - [2 Definició formal i càlcul](#2-definició-formal-i-càlcul)
   - [3 Exemple resolt: soroll tèrmic d'un sensor](#3-exemple-resolt-soroll-tèrmic-dun-sensor)
5. [Altres fonts de soroll: shot i 1/f](#altres-fonts-de-soroll-shot-i-1f)
   - [1 Soroll shot (Schottky)](#1-soroll-shot-schottky)
   - [2 Soroll de contacte, soroll en excés i soroll 1/f](#2-soroll-de-contacte-soroll-en-excés-i-soroll-1f)
6. [Modelatge de soroll en dispositius actius](#modelatge-de-soroll-en-dispositius-actius)
   - [1 Model de soroll d'un dispositiu actiu](#1-model-de-soroll-dun-dispositiu-actiu)
   - [2 Exemple 1: valor eficaç de soroll d'un operacional](#2-exemple-1-valor-eficaç-de-soroll-dun-operacional)
7. [Soroll en amplificadors i disseny de baix soroll](#soroll-en-amplificadors-i-disseny-de-baix-soroll)
   - [1 Exemple 2: soroll en un amplificador inversor](#1-exemple-2-soroll-en-un-amplificador-inversor)
   - [2 Guia de disseny de circuits de baix soroll](#2-guia-de-disseny-de-circuits-de-baix-soroll)
8. [Entrenament V/F · Unitat 4: Soroll](#entrenament-vf-unitat-4-soroll)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_Unitat4_Index -->

# Unitat 4 — Soroll · Lectura prèvia

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 4 — Soroll en sistemes de mesura

Materials de lectura prèvia · dedicació total estimada: 62 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents **substitueixen els apunts** i contenen tot el que cal per preparar la unitat.

Llegeix els sis documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor. Cada document acaba amb unes qüestions de reflexió, sense lliurament, per fixar les idees.

### [1. Introducció al soroll i caracterització estadística](#introducció-al-soroll-i-caracterització-estadística)

Soroll enfront d'errors sistemàtics i interferències; soroll intrínsec i extrínsec; el soroll com a procés estocàstic estacionari i ergòdic; mitjana, variància i valor eficaç; FDP i histograma; autocorrelació, espectre de potència i procés blanc; Parseval i densitats espectrals.

*⏱️ Dedicació estimada: 8 min*

### [2. Soroll tèrmic](#soroll-tèrmic)

Origen (Johnson-Nyquist); models de Thévenin i Norton; les expressions 4kTBR; potència disponible; densitats espectrals; caràcter blanc, distribució normal i promitjat 1/√N; soroll en excés i xarxes passives.

*⏱️ Dedicació estimada: 7 min*

### [3. Amplada de banda equivalent de soroll](#amplada-de-banda-equivalent-de-soroll)

Definició i interpretació geomètrica; sistemes ideals i reals; factors 1,57 (1r ordre) i 1,11 (Butterworth 2n ordre); passabanda; exemple resolt del soroll tèrmic d'un sensor.

*⏱️ Dedicació estimada: 11 min*

### [4. Altres fonts de soroll: shot i 1/f](#altres-fonts-de-soroll-shot-i-1f)

Soroll shot (Schottky): origen, condicions i model; densitat 2qI i valor eficaç. Soroll de contacte / 1/f: espectre K/f, integració logarítmica, divergència i freqüència corner.

*⏱️ Dedicació estimada: 7 min*

### [5. Modelatge de soroll en dispositius actius](#modelatge-de-soroll-en-dispositius-actius)

Model de quadripol amb fonts referides a l'entrada; font de tensió i fonts de corrent; suma quadràtica; interpretació de datasheets; Exemple 1 (LT6020) per a dues amplades de banda.

*⏱️ Dedicació estimada: 15 min*

### [6. Soroll en amplificadors i disseny de baix soroll](#soroll-en-amplificadors-i-disseny-de-baix-soroll)

Exemple 2: soroll en un amplificador inversor amb i sense condensador de retroalimentació; guany de soroll; guia de disseny de baix soroll (resistències, banda, dispositius actius, arquitectura, corrents, temperatura).

*⏱️ Dedicació estimada: 14 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

<!-- FIN CAPÍTULO: 00_Unitat4_Index -->

---

<!-- INICIO CAPÍTULO: 01_Unitat4_Introduccio_i_estadistica -->

# Introducció al soroll i caracterització estadística

Sistemes de Mesura · **Unitat 4 — Soroll** · Document 1 de 6

# Introducció al soroll i caracterització estadística

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir el soroll dels errors sistemàtics i de les interferències, i relacionar-lo amb la incertesa de mesura.
> - Separar el soroll *intrínsec* del *extrínsec* i entendre per què el soroll fixa el límit de detecció.
> - Descriure el soroll com un procés estocàstic estacionari i ergòdic, i estimar-ne mitjana, variància i valor eficaç d'una sola realització.
> - Interpretar la FDP, l'autocorrelació i l'espectre de potència, i reconèixer un procés blanc.
> - Relacionar la variància amb l'àrea de l'espectre (Parseval) i obtenir valors eficaços de densitats en V/√Hz i A/√Hz.

## 1 Què és el soroll en un sistema de mesura

En un sistema de mesura real, el senyal observat mai coincideix exactament amb la magnitud que volem mesurar. Els errors **sistemàtics** (offset, no-linealitat, deriva, guany) es poden caracteritzar i corregir amb calibratge. El **soroll**, en canvi, és un component *aleatori* superposat al senyal que fa que cada mesura sigui lleugerament diferent encara que la magnitud sigui constant; per això no s'elimina calibrant.

Anomenem soroll un senyal aleatori, de mitjana habitualment nul·la, associat a limitacions físiques del sistema o de l'entorn. És inevitable i s'ha d'integrar en el càlcul de la incertesa: **si el soroll és additiu, de mitjana nul·la i no correlacionat amb el senyal, la seva incertesa típica és igual al seu valor eficaç (RMS) a la sortida**. Que la mitjana sigui nul·la no vol dir que no contribueixi a la incertesa: la contribució la fixa la dispersió, no la mitjana. És la font principal de la incertesa típica de *tipus A*, la que surt de la variabilitat en repetir una mesura en condicions idèntiques.

### Soroll intrínsec i extrínsec

El **soroll intrínsec** es genera *dins* del sistema: agitació tèrmica a les resistències, soroll dels semiconductors, soroll de contacte, soroll 1/f dels dispositius actius. Es pot modificar redissenyant el circuit o triant components. El **soroll extrínsec** prové de fonts *externes*: interferències electromagnètiques, acoblament de la xarxa, transitoris. Sovint és determinista (el 50 Hz de la xarxa, ràdiofreqüències, acoblaments capacitius o inductius) i es va tractar a la Unitat 3. Una interferència de 50 Hz captada de la xarxa **no** és soroll tèrmic de les resistències internes, encara que totes dues contribucions se sumin a la sortida. En el model de circuit, el soroll extrínsec també es representa com una tensió o corrent addicional que se suma al senyal, però el seu origen i les tècniques de mitigació són diferents; reduir l'un no garanteix reduir l'altre.

### El soroll fixa el límit de detecció

El soroll total d'un sistema imposa un límit inferior de magnitud detectable. Augmentar el guany *no* millora per si sol la relació senyal-soroll (SNR): el soroll d'entrada s'amplifica igual que el senyal. Un sistema pot tenir molt de guany i, alhora, ser inadequat per a senyals petits si el soroll referit a l'entrada és massa gran; per sota del fons de soroll, cap variació del senyal té significació estadística. La SNR empitjora sempre que el valor eficaç del soroll creix sense que augmenti el senyal.

L'amplada de banda hi és clau: en ampliar-la, integrem més soroll. Per a soroll blanc, el valor eficaç creix amb l'**arrel quadrada** de la banda (duplicar la banda el multiplica per √2, no per 2). Per detectar senyals petits sovint cal limitar la banda al mínim compatible amb la dinàmica del senyal —un compromís entre velocitat i soroll que reprendrem als documents 3 i 6.

## 2 El soroll com a procés estocàstic

El soroll es modela com un procés **estocàstic**  $x(t)$
: una família de funcions, cadascuna amb una certa probabilitat. Una **realització** és el registre temporal concret d'una mesura —una d'aquestes funcions, no el conjunt de totes. En repetir l'experiment obtenim realitzacions diferents amb la mateixa estadística subjacent.

Sovint el soroll és **estacionari** (les propietats estadístiques —mitjana, variància, espectre— no canvien amb el temps; no varien periòdicament) i **ergòdic** (podem substituir la mitjana sobre moltes realitzacions per una mitjana temporal sobre una sola realització prou llarga). L'ergodicitat permet estimar variància i FDP a partir d'una única sèrie mostrejada, sense necessitat de moltes realitzacions independents. A la pràctica tenim  $x[n]=x(nT_s)$
, amb període de mostreig  $T_s$
 i freqüència de mostreig  $f_s=\frac{1}{T_s}$
.

### Mitjana, variància i valor eficaç

La **mitjana**  $\mu$
 és l'esperança; en soroll electrònic s'assumeix sovint  $\mu=0$
. La **variància**  $\sigma^2$
 és l'esperança del *quadrat* de la desviació respecte a la mitjana; amb mitjana nul·la, l'esperança de  $x^2$
. La desviació estàndard  $\sigma$
 **coincideix amb el valor eficaç (RMS)** per a soroll de mitjana nul·la. Amb  $N$
 mostres:

$$
\sigma \approx \sqrt{\frac{1}{N-1}\sum_{i=0}^{N-1} x[i]^2} \qquad (4.1)
$$

Per això, en aquest tema, «desviació estàndard» i «valor eficaç del soroll» s'usen indistintament, i  $\sigma$
 és directament la incertesa típica associada al soroll.

### Funció de densitat de probabilitat

La **FDP** descriu com es reparteixen els valors *instantanis* del soroll. S'estima amb un **histograma**, que cal **normalitzar** (àrea total = 1) perquè sigui una densitat de probabilitat. Amb prou mostres convergeix cap a la FDP real.

En molts sorolls físics, especialment el tèrmic, la FDP és **normal** de mitjana nul·la, per el *teorema central del límit*: el soroll és la suma de moltíssimes contribucions microscòpiques independents (no d'una partícula dominant). El caràcter gaussià relaciona  $\sigma$
 amb intervals de confiança: aproximadament el **68 %** de les mostres cauen dins de  $\pm\sigma$
, el **95 %** dins de  $\pm 2\sigma$
 i el **99,7 %** dins de  $\pm 3\sigma$
 —la base dels factors de cobertura  $k=2$
 (~95 %) i  $k=3$
 (~99,73 %). No tots els sorolls són normals: n'hi ha d'impulsius o amb cues pesades, i llavors cal prudència amb els intervals de confiança.

### Autocorrelació, espectre i soroll blanc

La FDP descriu l'amplitud, però no l'evolució temporal. La **funció d'autocorrelació** mesura la similitud entre el senyal i una còpia retardada  $\tau$
; per a mitjana nul·la,

$$
R_{\text{xx}}(\tau) = E\left[\, x(t)\, x(t+\tau)\,\right]
$$

Si  $R_{\text{xx}}(\tau)=0$
 per a tot  $\tau\neq 0$
, el procés és **blanc**: mostres independents. L'**espectre de potència**  $P_{\text{xx}}(f)$
 descriu com es reparteix la variància en freqüència i, per a processos estacionaris, és la **transformada de Fourier de l'autocorrelació**. En l'estimació pràctica s'aplica sovint una **finestra** (per exemple, de Hann) per reduir les fuites espectrals de l'observació finita.

Un **procés blanc ideal** té autocorrelació nul·la i espectre de potència *constant* (pla) a totes les freqüències; el soroll tèrmic d'una resistència n'és un bon exemple aproximat dins d'una banda finita. El **soroll 1/f**, en canvi, té densitat que decreix amb la inversa de la freqüència: no és blanc perquè la seva densitat *depèn* de la freqüència. En processos blancs, promitjar mostres redueix clarament la incertesa; en processos amb memòria, la reducció és més lenta (document 2).

### Parseval i densitats espectrals

El **teorema de Parseval** iguala la variància a l'àrea sota l'espectre:

$$
\sigma^2 = \int_{0}^{\infty} P_{\text{xx}}(f)\, df \qquad (4.2)
$$

$$
\sigma = \sqrt{\int_{0}^{\infty} P_{\text{xx}}(f)\, df} \qquad (4.3)
$$

(considerant freqüències positives). L'espectre ha d'estar ben normalitzat perquè la igualtat es compleixi. Sovint el soroll s'especifica per la **densitat espectral de tensió**  $e_n(f)$
 (V/√Hz) o de corrent  $i_n(f)$
 (A/√Hz); el valor eficaç s'obté integrant-ne el *quadrat*:

$$
\sigma_V = \sqrt{\int_{f_{\min}}^{f_{\max}} e_n^2(f)\, df}, \qquad \sigma_I = \sqrt{\int_{f_{\min}}^{f_{\max}} i_n^2(f)\, df} \qquad (4.4)
$$

No es pot multiplicar  $e_n$
 (V/√Hz) directament per la banda (Hz): les unitats no quadren. Quan la densitat és *constant* (blanc), n'hi ha prou de multiplicar per  $\sqrt{B}$
, i d'aquí que el valor eficaç del soroll blanc creixi amb  $\sqrt{B}$
. Avançant el document 2: per a una resistència,  $P_{\text{xx}}=4kTR$
 (V²/Hz),  $e_n=\sqrt{4kTR}$
 i  $i_n=\sqrt{\frac{4kT}{R}}$
.

![Caracterització d'un senyal de soroll: temporal, FDP, autocorrelació i espectre](assets/01_Unitat4_Introduccio_i_estadistica_img_1.png)

*Figura: Figura 4.1 Caracterització de soroll: senyal temporal ( $\sigma=2{,}89\,\mu\mathrm{V}$
), FDP aproximadament normal, autocorrelació i espectre. Ací l'autocorrelació (no nul·la a retards petits) i l'espectre (no pla) indiquen que el procés no és blanc, tot i tenir FDP gaussiana: gaussià i blanc són propietats independents.*

> [!TIP] **Síntesi**
>
> El soroll és la component aleatòria que, si és additiva, de mitjana nul·la i no correlacionada, té incertesa típica igual al seu valor eficaç. Es distingeix de les interferències (extrínsec) i marca el límit de detecció, que empitjora en ampliar la banda ( $\sigma\propto\sqrt{B}$
> per a blanc). Com a procés estocàstic estacionari i ergòdic, es caracteritza en amplitud per mitjana, variància/RMS i FDP (sovint normal: 68/95/99,7 % dins de  $\pm\sigma,\pm2\sigma,\pm3\sigma$
> ) i en temps/freqüència per l'autocorrelació i l'espectre (TF de l'autocorrelació). Blanc = autocorrelació nul·la i espectre pla. Parseval iguala la variància a l'àrea de l'espectre; les densitats  $e_n$
> (V/√Hz) i  $i_n$
> (A/√Hz) s'integren al quadrat.

[2. Soroll tèrmic →](#soroll-tèrmic)

---

<!-- FIN CAPÍTULO: 01_Unitat4_Introduccio_i_estadistica -->

---

<!-- INICIO CAPÍTULO: 02_Unitat4_Soroll_termic -->

# Soroll tèrmic

Sistemes de Mesura · **Unitat 4 — Soroll** · Document 2 de 6

# Soroll tèrmic

Dedicació estimada: 7 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar l'origen del soroll tèrmic (Johnson-Nyquist) i per què apareix en qualsevol resistència per sobre del zero absolut.
> - Utilitzar els models de Thévenin i Norton i conèixer-ne l'equivalència.
> - Aplicar  $V_t=\sqrt{4kTBR}$
>,  $I_t=\sqrt{\frac{4kTB}{R}}$
> i les densitats espectrals, i entendre-ne les dependències.
> - Distingir el soroll tèrmic (irreductible) del soroll en excés (evitable) i el paper de la tecnologia.
> - Estendre el càlcul a xarxes passives (part real de la impedància) i relacionar el caràcter blanc amb el promitjat  $1/\sqrt{N}$
>.

## 1 Origen i models del soroll tèrmic

El **soroll tèrmic** (soroll de Johnson o Johnson-Nyquist) és la font de soroll més fonamental en circuits electrònics. El seu origen és l'**agitació tèrmica dels portadors de càrrega**: per sobre del zero absolut, els electrons es mouen aleatòriament, i les fluctuacions microscòpiques de tensió i corrent, sumades, donen un senyal aleatori mesurable als terminals d'una resistència. Com que és tèrmic, apareix *encara que no hi circuli corrent continu*: només depèn de la temperatura. Una resistència ideal a  $T>0$
 genera soroll tèrmic encara que estigui desconnectada, i el seu valor no és nul pel fet de ser petita. Apareix inevitablement en qualsevol resistència real i marca un **límit físic inferior** de sensibilitat: encara que eliminéssim les altres fonts, el soroll tèrmic hi continuaria. Per això, en molt baix soroll (biomèdica, radioastronomia, detectors de partícules) es minimitzen resistència i amplada de banda.

### Models de Thévenin i de Norton

Una resistència real es modela com una **resistència ideal sense soroll** més un generador que representa les fluctuacions tèrmiques, de tensió (Thévenin) o de corrent (Norton). Així es tracten per separat la resistència i el soroll: es pot aplicar superposició i combinar fonts independents per **suma pitagòrica** (arrel quadrada de la suma dels quadrats dels valors eficaços).

![Component real, model Thévenin amb font de tensió en sèrie i model Norton amb font de corrent en paral·lel](assets/02_Unitat4_Soroll_termic_img_1.png)

*Figura: Figura 4.2 Models de soroll tèrmic d'una resistència: component real (esquerra), Thévenin —resistència ideal en sèrie amb la font de tensió $V_t$
— (centre) i Norton —resistència ideal en paral·lel amb la font de corrent $I_t$
— (dreta), a temperatura absoluta $T$
.*

En el **model de Thévenin**, la resistència es representa com una resistència ideal  $R$
 *en sèrie* amb una font de tensió de soroll  $V_t$
, de mitjana nul·la. Correspon a la tensió en circuit obert i és útil quan la resistència es connecta a una entrada d'alta impedància (preamplificadors, entrada no inversora d'un operacional), perquè  $V_t$
 es propaga multiplicada pel guany. En el **model de Norton**, es representa com  $R$
 ideal *en paral·lel* amb una font de corrent de soroll  $I_t$
; correspon al corrent en curtcircuit i és convenient en nodes de baixa impedància (inversors, transimpedància). Totes dues es relacionen per  $I_t = V_t/R$
.

## 2 Les expressions fonamentals

La tensió eficaç de soroll d'una resistència  $R$
 a temperatura  $T$
 en circuit obert és

$$
V_t = \sqrt{4kTBR} \qquad (4.5)
$$

amb  $k \approx 1{,}38\times 10^{-23}\ \mathrm{J/K}$
 (constant de Boltzmann),  $T$
 en kelvin,  $B$
 l'amplada de banda equivalent de soroll (document 3) i  $R$
 en ohms. Creix amb l'**arrel quadrada** de  $T$
,  $B$
 i  $R$
: reduir el soroll un factor 10 exigiria reduir-ne algun un factor 100. La tensió de soroll *augmenta* amb  $R$
. Per exemple,  $R=100\ \mathrm{k\Omega}$
 a 298 K i  $B=1\ \mathrm{kHz}$
 dona  $V_t\approx 1{,}3\ \mu\mathrm{V}$
 —crític si el senyal útil és de l'ordre del microvolt (ECG, termoparells).

En curtcircuit, el corrent de soroll és

$$
I_t = \sqrt{\frac{4kTB}{R}} \qquad (4.6)
$$

de manera que una resistència gran genera *més* tensió però *menys* corrent de soroll:  $I_t$
 disminueix en augmentar  $R$
 (amb els valors anteriors,  $\approx 13\ \mathrm{pA}$
). Això condiciona la topologia: en alta impedància (domina la tensió) convé  $R$
 petita; en baixa impedància (domina el corrent),  $R$
 gran.

### Potència de soroll disponible

La **potència de soroll disponible** (màxima transferible a una càrrega adaptada) és

$$
P_t = V_t \cdot I_t = \sqrt{4kTBR}\,\sqrt{\frac{4kTB}{R}} = 4kTB \qquad (4.7)
$$

**independent del valor de la resistència** (teorema de màxima transferència).

### Densitats espectrals

El soroll tèrmic és **blanc** fins a freqüències extremadament altes (THz). Les densitats espectrals de potència de tensió i de corrent són

$$
P_{\text{xx}}(f) = 4kTR \quad [\mathrm{V^2/Hz}] \qquad (4.8)
$$

proporcional a la temperatura absoluta. Integrant la constant sobre la banda,

$$
\sigma_V^2 = \int_{f_{\min}}^{f_{\max}} P_{\text{xx}}(f)\, df = 4kTR\,(f_{\max}-f_{\min}) = 4kTRB \qquad (4.9)
$$

i recuperem (4.5). La densitat espectral de potència de corrent és

$$
P_{\text{ii}}(f) = \frac{4kT}{R} \quad [\mathrm{A^2/Hz}] \qquad (4.10)
$$

A la pràctica es fan servir les densitats de tensió i corrent (arrel de les anteriors):

$$
e_n(f) = \sqrt{4kTR} \quad [\mathrm{V/\sqrt{Hz}}] \qquad (4.11)
$$

$$
i_n(f) = \sqrt{\frac{4kT}{R}} \quad [\mathrm{A/\sqrt{Hz}}] \qquad (4.12)
$$

$e_n(f)$
 és el valor eficaç en una banda d'1 Hz. Per al total en una banda  $B$
 cal integrar-ne el *quadrat*; si és constant (blanc), n'hi ha prou de multiplicar per  $\sqrt{B}$
:

$$
V_t = e_n\sqrt{B} = \sqrt{4kTR}\,\sqrt{B} = \sqrt{4kTRB} \qquad (4.13)
$$

Aquest és el format dels fabricants: donen la densitat en V/√Hz o A/√Hz, independent de la banda, i el dissenyador calcula el valor eficaç. Per exemple, a 298 K una resistència de 10 kΩ té  $e_n\approx 12{,}8\ \mathrm{nV/\sqrt{Hz}}$
. La densitat s'integra al *quadrat*; no es multiplica directament per la banda en Hz. (La densitat de corrent de soroll tèrmic és  $i_n=\sqrt{\frac{4kT}{R}}$
, que *disminueix* amb  $R$
, i la de tensió  $e_n=\sqrt{4kTR}$
, que hi *augmenta*.)

### Caràcter blanc, distribució normal i promitjat

Com que és blanc, l'autocorrelació és pràcticament una delta: mostres separades més d'un temps característic (invers de la banda) són independents. Per això, si promitgem  $N$
 mesures d'una magnitud constant afectada per soroll blanc, la incertesa de la mitjana **decreix amb  $1/\sqrt{N}$**. En un procés amb forta correlació temporal, el promitjat redueix la incertesa més lentament. En amplitud, el soroll tèrmic és **normal** de mitjana nul·la (teorema central del límit), amb els factors de cobertura habituals (68/95/99,7 % dins de  $\pm\sigma,\pm2\sigma,\pm3\sigma$
).

## 3 Soroll en excés i xarxes passives

$V_t=\sqrt{4kTBR}$
 és el soroll *mínim* d'una resistència. Moltes en presenten més: el **soroll en excés**, sense origen tèrmic, associat a contactes, defectes o inhomogeneïtats, que apareix *quan hi circula corrent continu*. És important en resistències de **carbó o composició** (el corrent salta entre grans a través de barreres), amb espectre 1/f que creix cap a baixes freqüències (document 4). Les de **pel·lícula metàl·lica** s'acosten al límit tèrmic teòric; per això, en baix soroll es recomana pel·lícula metàl·lica i *no* carbó, sobretot en mesures lentes. El soroll en excés **augmenta amb la tensió (o corrent) contínua** aplicada —al contrari que el tèrmic, independent del corrent— i depèn de la tecnologia i dels defectes; convé, doncs, minimitzar tensions i corrents continus per les resistències crítiques, i en aplicacions extremes seleccionar-les mesurant-ne el soroll.

### Extensió a xarxes passives

Per a una xarxa passiva d'impedància  $Z(f)=R(f)+jX(f)$
, la densitat espectral de tensió de soroll és

$$
P_{\text{xx}}(f) = 4kT\,R(f) \quad [\mathrm{V^2/Hz}] \qquad (4.14)
$$

on  $R(f)$
 és la **part real**: només la component *resistiva* (dissipativa) contribueix al soroll tèrmic. Els components reactius ideals (condensadors, inductors) **no generen soroll tèrmic propi** perquè no dissipen energia, encara que modifiquen l'espectre alterant la impedància. En un filtre RC, per exemple, la part real varia amb la freqüència i la potència total s'obté integrant  $P_{\text{xx}}(f)$
 sobre la banda. En resum, el soroll tèrmic és inevitable però predictible, i el soroll en excés és evitable amb bons components i condicions de funcionament controlades.

> [!TIP] **Síntesi**
>
> El soroll tèrmic (Johnson-Nyquist) prové de l'agitació tèrmica i apareix en qualsevol resistència per sobre del zero absolut, fins i tot sense corrent. Es modela amb Thévenin (font de tensió  $V_t=\sqrt{4kTBR}$
> en sèrie) o Norton (font de corrent  $I_t=\sqrt{\frac{4kTB}{R}}$
> en paral·lel), via  $I_t=V_t/R$
>. La tensió creix amb  $\sqrt{R}$
> i el corrent decreix amb  $\sqrt{R}$
>; la potència disponible  $4kTB$
> és independent de  $R$
>. Densitats:  $4kTR$
> (V²/Hz) i  $4kT/R$
> (A²/Hz); blanc i gaussià, amb promitjat  $1/\sqrt{N}$
>. El soroll en excés (1/f, lligat al corrent continu i a la tecnologia) s'afegeix al tèrmic i és menor en pel·lícula metàl·lica. En xarxes passives, només la part real  $4kT\,R(f)$
> genera soroll.

[← 1. Introducció al soroll i caracterització estadística](#introducció-al-soroll-i-caracterització-estadística)[3. Amplada de banda equivalent de soroll →](#amplada-de-banda-equivalent-de-soroll)

---

<!-- FIN CAPÍTULO: 02_Unitat4_Soroll_termic -->

---

<!-- INICIO CAPÍTULO: 03_Unitat4_Amplada_banda_equivalent -->

# Amplada de banda equivalent de soroll

Sistemes de Mesura · **Unitat 4 — Soroll** · Document 3 de 6

# Amplada de banda equivalent de soroll

Dedicació estimada: 11 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Entendre per què cal una amplada de banda equivalent de soroll  $B_{\text{eq}}$
> i què significa geomètricament.
> - Reconèixer que  $B_{\text{eq}}$
> integra el *quadrat* de la resposta en freqüència i que, en sistemes reals, no coincideix amb la freqüència de tall a −3 dB.
> - Aplicar els resultats  $B_{\text{eq}}=\frac{\pi}{2}f_{-3\,\mathrm{dB}}\approx 1{,}57\,f_{-3\,\mathrm{dB}}$
> (1r ordre) i  $B_{\text{eq}}=1{,}11\,f_{-3\,\mathrm{dB}}$
> (Butterworth 2n ordre).
> - Resoldre un càlcul complet de soroll tèrmic a l'entrada i la sortida d'un sistema passabaixes.

## 1 Per què una amplada de banda «equivalent»

El valor eficaç de soroll d'una font —tèrmic o d'un altre tipus— depèn sempre d'un paràmetre anomenat **amplada de banda equivalent de soroll**,  $B_{\text{eq}}$
. És un dels pilars de l'anàlisi de soroll, perquè connecta la resposta freqüencial real d'un sistema amb la potència total de soroll que deixa passar. La idea és substituir la forma complexa de la resposta real per un **filtre ideal rectangular** que produeixi exactament la mateixa potència de soroll a la sortida. Així els càlculs es simplifiquen enormement.

![Respostes ideals i reals de sistemes passabaixes i passabanda](assets/03_Unitat4_Amplada_banda_equivalent_img_1.png)

*Figura: Figura 4.3 Amplada de banda equivalent de soroll en sistemes passabaixes (a dalt) i passabanda (a baix). A l'esquerra, les respostes ideals rectangulars; a la dreta, les respostes reals, amb banda de transició i pendents que depenen de l'ordre del sistema.*

Un sistema **passabaixes ideal** presenta guany constant  $A_0$
 des de contínua fins a una freqüència límit  $f_c$
, i guany nul per damunt:

$$
|A(f)| = A_0 \;\;(0\leq f\leq f_c); \qquad |A(f)| = 0 \;\;(f>f_c) \qquad (4.15)
$$

Un sistema **passabanda ideal** té guany  $A_0$
 entre  $f_{c,\min}$
 i  $f_{c,\max}$
 i nul fora d'aquest interval:

$$
|A(f)| = A_0 \;\;(f_{c,\min}\leq f\leq f_{c,\max}); \qquad |A(f)| = 0 \;\;\mathrm{(altrament)} \qquad (4.16)
$$

Un passabanda ideal, doncs, deixa passar les freqüències *compreses entre* les dues freqüències de tall. En aquests casos ideals,  $B_{\text{eq}}$
 coincideix amb l'amplada geomètrica:  $B_{\text{eq}}=f_c$
 (passabaixes) i  $B_{\text{eq}}=f_{c,\max}-f_{c,\min}$
 (passabanda). El problema és que cap sistema físic real té una resposta rectangular perfecta.

### Sistemes reals: banda de transició

Tot sistema real té una **banda de transició** entre la zona de pas i la d'eliminació, on el guany decreix gradualment. La rapidesa depèn de l'ordre: un sistema de primer ordre (un pol) cau a −20 dB/dècada (−6 dB/octava); un de segon ordre a −40 dB/dècada; en general, un d'ordre  $k$
 cau a −20 $k$
 dB/dècada.

La freqüència de tall a −3 dB,  $f_{-3\,\mathrm{dB}}$
, és aquella on el guany ha caigut a  $A_0/\sqrt{2}$
 (la potència s'ha reduït a la meitat). A causa de la banda de transició, usar simplement  $f_{-3\,\mathrm{dB}}$
 com a amplada de banda per als càlculs de soroll condueix a errors sistemàtics —generalment una *subestimació*— perquè les freqüències lleugerament superiors a  $f_{-3\,\mathrm{dB}}$
 encara contribueixen amb soroll. Com més gran és l'ordre, més abrupta és la transició i més s'aproxima la resposta a la ideal; en el límit  $k\to\infty$
,  $B_{\text{eq}}\to f_{-3\,\mathrm{dB}}$
. L'ordre del filtre, per tant, sí que influeix en la relació entre  $B_{\text{eq}}$
 i la freqüència de tall.

## 2 Definició formal i càlcul

L'amplada de banda equivalent de soroll d'un sistema amb resposta  $A(f)$
 i guany màxim  $A_0$
 es defineix com

$$
B_{\text{eq}} = \frac{1}{A_0^2}\int_{0}^{\infty} |A(f)|^2\, df \qquad (4.17)
$$

Geomètricament,  $B_{\text{eq}}$
 és l'amplada d'un rectangle d'alçada  $A_0^2$
 amb la mateixa àrea que la corba  $|A(f)|^2$
:

$$
A_0^2\cdot B_{\text{eq}} = \int_{0}^{\infty} |A(f)|^2\, df \qquad (4.18)
$$

És crucial que la integral involucra el **mòdul al quadrat**, no el mòdul directament: la potència de soroll a la sortida és proporcional a  $|A(f)|^2$
 per a cada component. Per a una font de soroll blanc de densitat  $S_n$
 constant, la potència total a la sortida és

$$
V_{n,out}^2 = \int_{0}^{\infty} S_n\,|A(f)|^2\, df = S_n\,A_0^2\,B_{\text{eq}} \qquad (4.19)
$$

que és exactament la que donaria un filtre ideal rectangular de guany  $A_0$
 i amplada  $B_{\text{eq}}$
:

$$
V_{n,out,\,ideal}^2 = S_n\,A_0^2\,B_{\text{eq}} \qquad (4.20)
$$

Aquesta és la interpretació física:  $B_{\text{eq}}$
 és l'amplada que hauria de tenir un sistema ideal per produir el mateix soroll a la sortida que el sistema real.

![Resistència sorollosa a l'entrada d'un bloc A(f), amb el soroll referit a entrada i sortida](assets/03_Unitat4_Amplada_banda_equivalent_img_2.png)

*Figura: Figura 4.4 Amplada de banda equivalent aplicada al soroll tèrmic d'una resistència: el soroll d'entrada es propaga pel bloc $A(f)$
i el valor eficaç de sortida s'obté amb $B_{\text{eq}}$
.*

Per al soroll tèrmic d'una resistència  $R$
 a temperatura  $T$
, la tensió eficaç a la sortida queda

$$
V_{n,out} = A_0\sqrt{4kTR\,B_{\text{eq}}} \qquad (4.21)
$$

i, referida a l'entrada dividint pel guany,

$$
V_{n,in} = \sqrt{4kTR\,B_{\text{eq}}} \qquad (4.22)
$$

condicionada per l'amplada de banda equivalent del sistema que fa servir aquesta resistència.

### Casos analítics habituals

Per a un passabaixes de primer ordre amb guany  $A_0$
 i freqüència de tall  $f_0=f_{-3\,\mathrm{dB}}$
:

$$
A(f) = \frac{A_0}{1+j\,f/f_0} \qquad (4.23)
$$

$$
|A(f)|^2 = \frac{A_0^2}{1+(f/f_0)^2} \qquad (4.24)
$$

Substituint a la definició i amb el canvi  $x=f/f_0$
:

$$
B_{\text{eq}} = \frac{1}{A_0^2}\int_{0}^{\infty}\frac{A_0^2}{1+(f/f_0)^2}\,df = f_0\int_{0}^{\infty}\frac{dx}{1+x^2} = f_0\cdot\frac{\pi}{2} \qquad (4.25)
$$

és a dir,

$$
B_{\text{eq}} = \frac{\pi}{2}\,f_{-3\,\mathrm{dB}} \approx 1{,}57\,f_{-3\,\mathrm{dB}} \qquad (4.26)
$$

Un passabaixes de primer ordre deixa passar, doncs, un **57 % més** de potència de soroll que un filtre ideal amb la mateixa freqüència de tall. La causa és la cua que decreix lentament (−20 dB/dècada) i continua deixant passar soroll per damunt de  $f_{-3\,\mathrm{dB}}$
. Per a un **Butterworth de segon ordre** ( $Q=1/\sqrt{2}\approx 0{,}707$
), maximalment pla a la banda de pas,

$$
B_{\text{eq}} = 1{,}11\,f_{-3\,\mathrm{dB}} \qquad (4.27)
$$

només un 11 % superior, reflex de la caiguda molt més ràpida (−40 dB/dècada). Per a segon ordre amb  $Q$
 diferent,  $B_{\text{eq}}$
 depèn de  $Q$
:  $Q$
 alts (amortiment baix) presenten pics de ressonància que augmenten l'àrea sota  $|A(f)|^2$
 i, per tant,  $B_{\text{eq}}$
. En augmentar l'ordre del Butterworth, la relació  $B_{\text{eq}}/f_{-3\,\mathrm{dB}}$
 tendeix a 1.

En sistemes **passabanda** amb  $f_{c,\min}\ll f_{c,\max}$
,  $B_{\text{eq}}$
 s'aproxima per la del passabaixes de freqüència de tall  $f_{c,\max}$
: el límit superior domina l'estimació del soroll blanc integrat, perquè el límit inferior és negligible. Per exemple, un passabanda entre 10 Hz i 1 kHz té una  $B_{\text{eq}}$
 pràcticament igual a la d'un passabaixes de 1 kHz.

## 3 Exemple resolt: soroll tèrmic d'un sensor

> [!EXAMPLE] **Exemple resolt**
>
> Es vol mesurar un sensor modelable com una resistència  $R=100\ \mathrm{k\Omega}$
> amb un sistema que es comporta com un passabaixes de primer ordre amb  $f_0=f_{-3\,\mathrm{dB}}=100\ \mathrm{Hz}$
> i guany en contínua  $A_0=1000$
>. La temperatura del sensor és de 37 °C. Es demana: (a) l'expressió del mòdul de la resposta freqüencial; (b) l'amplada de banda equivalent de soroll; (c) la tensió eficaç de soroll a l'entrada i a la sortida.
>
> 1. Mòdul de la resposta. Amb  $s=j2\pi f$
>,  $A(f)=A_0/(1+jf/f_0)$
>, de manera que
>

$$
|A(f)| = \frac{A_0}{\sqrt{1+(f/f_0)^2}} = \frac{1000}{\sqrt{1+(f/100)^2}}
$$

> Verificació:  $|A(0)|=1000$
> i  $|A(100)|=1000/\sqrt{2}\approx 707$
>, la caiguda de −3 dB esperada.
> 2. Amplada de banda equivalent. Aplicant (4.17) i el canvi  $x=f/f_0$
>,
>

$$
B_{\text{eq}} = f_0\int_{0}^{\infty}\frac{dx}{1+x^2} = f_0\cdot\frac{\pi}{2} = \frac{\pi}{2}\cdot 100\ \mathrm{Hz} = 157\ \mathrm{Hz}
$$

> Malgrat que el sistema talla a 100 Hz, la cua acumula soroll equivalent a una finestra rectangular de 157 Hz.
> 3. Temperatura en kelvin.  $T = 273{,}15 + 37 = 310{,}15\ \mathrm{K}$
>.
> 4. Soroll referit a l'entrada. Amb (4.22),
>

$$
V_{n,in} = \sqrt{4kTR\,B_{\text{eq}}} = \sqrt{4\cdot 1{,}38\times 10^{-23}\cdot 310{,}15\cdot 10^{5}\cdot 157} \approx 0{,}52\ \mu\mathrm{V}
$$

> 5. Soroll referit a la sortida. Multiplicant pel guany,
>

$$
V_{n,out} = A_0\cdot V_{n,in} = 1000\cdot 0{,}52\ \mu\mathrm{V} = 0{,}52\ \mathrm{mV}
$$

> 6. Interpretació. Si el sensor dona un senyal útil de 10 μV, la SNR és d'uns 20 (≈26 dB), modesta per a precisió. Per reduir el soroll: (i) reduir la banda —passar de 100 Hz a 10 Hz baixa  $B_{\text{eq}}$
> a 15,7 Hz i el soroll un factor  $\sqrt{10}\approx 3{,}16$
>, a canvi d'una resposta 10 vegades més lenta—; (ii) reduir  $R$
> si el disseny ho permet; (iii) refrigerar el sensor, poc pràctic normalment.

Aquest exemple mostra el paper central de  $B_{\text{eq}}$
: connecta la resposta freqüencial del sistema amb la potència de soroll observada, i el seu control és una de les eines més potents per optimitzar la qualitat de les mesures. Al document 6 el retrobarem en un cas amb amplificador operacional i condensador de retroalimentació.

> [!TIP] **Síntesi**
>
> L'amplada de banda equivalent de soroll  $B_{\text{eq}}=\frac{1}{A_0^2}\int_0^\infty |A(f)|^2 df$
> és l'amplada d'un filtre rectangular ideal que deixaria passar la mateixa potència de soroll que el sistema real. Integra el mòdul *al quadrat*, i en sistemes reals és més gran que  $f_{-3\,\mathrm{dB}}$
>:  $1{,}57\,f_{-3\,\mathrm{dB}}$
> en primer ordre i  $1{,}11\,f_{-3\,\mathrm{dB}}$
> en Butterworth de segon, tendint a 1 en augmentar l'ordre. El soroll tèrmic referit a l'entrada val  $\sqrt{4kTR\,B_{\text{eq}}}$
> i a la sortida es multiplica per  $A_0$
>. En passabanda amb  $f_{c,\min}\ll f_{c,\max}$
>, domina el límit superior. Reduir la banda redueix el soroll amb  $\sqrt{B_{\text{eq}}}$
> a costa de la velocitat de resposta.

[← 2. Soroll tèrmic](#soroll-tèrmic)[4. Altres fonts de soroll: shot i 1/f →](#altres-fonts-de-soroll-shot-i-1f)

---

<!-- FIN CAPÍTULO: 03_Unitat4_Amplada_banda_equivalent -->

---

<!-- INICIO CAPÍTULO: 04_Unitat4_Soroll_shot_i_1f -->

# Altres fonts de soroll: shot i 1/f

Sistemes de Mesura · **Unitat 4 — Soroll** · Document 4 de 6

# Altres fonts de soroll: shot i 1/f

Dedicació estimada: 7 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar l'origen del soroll shot (Schottky) i les dues condicions necessàries perquè aparegui.
> - Aplicar  $S_i=2qI_{\text{dc}}$
> i  $i_{n,rms}=\sqrt{2qI_{\text{dc}}B}$
>, i reconèixer-lo com a soroll blanc.
> - Descriure el soroll de contacte 1/f, el seu espectre  $K/f^\alpha$
> i la seva integració logarítmica.
> - Comprendre per què el soroll 1/f divergeix matemàticament quan  $f_{\min}\to 0$
> però té un efecte pràctic moderat.

A banda del soroll tèrmic (document 2), els dispositius —sobretot els actius— presenten dues fonts més: el **soroll shot** (o Schottky) i el **soroll de contacte 1/f** (flicker). Cal entendre-les per modelar i dissenyar correctament sistemes de baix soroll.

## 1 Soroll shot (Schottky)

El soroll shot és intrínsec a qualsevol dispositiu on hi ha **pas discret de càrrega a través d'una barrera de potencial** quan circula corrent continu. És de naturalesa quàntica, relacionat amb la quantització de la càrrega (càrrega elemental  $q$
) i amb l'estadística de Poisson del pas aleatori de portadors.

En una unió PN polaritzada en directa (díode, unió base-emissor d'un BJT, fotodíode) els portadors creuen la regió de depleció de manera discreta: cada electró o forat aporta una càrrega  $q$
. Encara que el corrent mitjà sigui constant ( $I_{\text{dc}}$
), el nombre d'esdeveniments en un interval curt fluctua aleatòriament: si de mitjana hi passen  $N$
 portadors, la desviació típica és aproximadament  $\sqrt{N}$
. Aquestes fluctuacions es perceben com a soroll. El soroll shot apareix, doncs, sempre que hi ha (1) una barrera de potencial i (2) un corrent continu que la travessa. **Sense corrent DC apreciable, el soroll shot d'aquella unió és negligible** —fet molt útil per reduir soroll a les etapes d'entrada. No té, per tant, el mateix origen que el soroll tèrmic (agitació tèrmica en un conductor, sense barrera) ni la mateixa dependència: el shot no depèn de  $R$
 sinó del corrent.

![Díode ideal amb una font de corrent de soroll Ish en paral·lel](assets/04_Unitat4_Soroll_shot_i_1f_img_1.png)

*Figura: Figura 4.5 Modelització del soroll shot: el corrent continu es modela amb la branca ideal (model exponencial del díode) i el soroll shot s'afegeix com una font de corrent aleatori $i_{\text{sh}}(t)$
en paral·lel amb la unió.*

En anàlisi de petits senyals i de soroll, el soroll shot es modela com una **font de corrent de soroll en paral·lel** amb la unió (o amb el corrent DC equivalent). El mateix esquema serveix per als corrents de col·lector en BJT, els corrents de fuites en díodes i els corrents fotoinduïts en fotodíodes. La densitat espectral de potència de corrent és aproximadament constant amb la freqüència —és a dir, **soroll blanc** dins de la banda de treball:

$$
S_i(f) = 2\,q\,I_{\text{dc}} \quad [\mathrm{A^2/Hz}] \qquad (4.28)
$$

on  $q$
 és la càrrega elemental i  $I_{\text{dc}}$
 el corrent continu. La densitat és *proporcional* al corrent continu. Integrant sobre una amplada de banda equivalent  $B$
:

$$
i_{n,rms}^2 = \int_{f_{\min}}^{f_{\max}} S_i(f)\,df \approx \int_{0}^{B} 2qI_{\text{dc}}\,df = 2qI_{\text{dc}}B \qquad (4.29)
$$

$$
i_{n,rms} = \sqrt{2qI_{\text{dc}}B} \qquad (4.30)
$$

El valor eficaç creix amb l'arrel quadrada del corrent i amb l'arrel quadrada de l'amplada de banda; per tant, *augmenta* en ampliar la banda. Com que la densitat és essencialment constant, es pot considerar blanc en l'interval habitual dels sistemes de mesura (de pocs Hz a centenars de kHz). Els fotodíodes il·luminats presenten també soroll shot, precisament perquè el corrent fotoinduït és un corrent continu que travessa una unió.

**Exemple ràpid.** Un fotodíode amb  $I_{\text{dc}}=10\ \mu\mathrm{A}$
 en un sistema amb  $B=100\ \mathrm{kHz}$
:

$$
i_{n,rms} = \sqrt{2qI_{\text{dc}}B} \approx \sqrt{2\cdot 1{,}6\times 10^{-19}\cdot 10^{-5}\cdot 10^{5}} \approx 570\ \mathrm{pA}
$$

Sembla petit, però amb una transimpedància elevada ( $R_f=100\ \mathrm{k\Omega}$
) donaria dècimes de μV a la sortida, comparable amb el senyal en aplicacions sensibles.

## 2 Soroll de contacte, soroll en excés i soroll 1/f

El **soroll 1/f** (o de contacte, o en excés, o flicker) domina generalment a **baixes freqüències** i té un espectre que decreix aproximadament com  $\frac{1}{f}$
. Apareix típicament quan s'uneixen materials diferents (contactes metall-semiconductor, metall-metall), quan hi ha barreja de materials (resistències de carbó) o quan el material té imperfeccions, defectes o inhomogeneïtats. Com el soroll en excés que vam veure al document 2, necessita que hi circuli un **corrent continu**  $I_{\text{dc}}$
: aquest corrent posa en joc mecanismes de captura i emissió de portadors, migració d'ions i variacions locals de resistivitat que generen fluctuacions lentes.

Escenaris típics: resistències de carbó, contactes mecànics (relés, connectors, potenciòmetres, sobretot amb oxidacions) i dispositius actius (MOSFET, BJT), on les trampes a l'òxid o a la interfície generen soroll 1/f. A diferència del soroll tèrmic —intrínsec i present encara que no circuli corrent—, el soroll 1/f **augmenta amb el corrent continu** i és molt sensible a la tecnologia i la qualitat dels materials; no depèn només de la temperatura ni és independent dels contactes i defectes.

El comportament espectral es modela amb una densitat espectral de potència (per exemple, de tensió)

$$
S_v(f) = \frac{K}{f^{\alpha}} \quad \mathrm{amb } \alpha\approx 1 \qquad (4.31)
$$

on  $K$
 depèn del dispositiu, la tecnologia, el corrent DC i la geometria, i  $\alpha$
 és molt propera a 1. Com que la densitat *canvia* amb la freqüència, és un soroll **no blanc**, especialment rellevant a baixes freqüències, en contrast amb el tèrmic i el shot, que són plans dins de la banda d'interès.

### Integració logarítmica

La variància en una banda  $[f_{\min},f_{\max}]$
 és

$$
v_{n,rms}^2 = \int_{f_{\min}}^{f_{\max}} \frac{K}{f}\,df = K\,\ln\!\left(\frac{f_{\max}}{f_{\min}}\right) \qquad (4.32)
$$

$$
v_{n,rms} = \sqrt{K\,\ln\!\left(\frac{f_{\max}}{f_{\min}}\right)} \qquad (4.33)
$$

La contribució eficaç del soroll 1/f, doncs, depèn del *logaritme* del quocient de freqüències, no de la diferència lineal  $f_{\max}-f_{\min}$
 (això seria el cas blanc). D'aquí dues conseqüències:

- El soroll 1/f **divergeix logarítmicament** quan  $f_{\min}\to 0$
: integrar des de freqüència zero donaria soroll infinit.
- Creix molt **lentament** amb  $f_{\max}$
   (només amb el logaritme), molt més a poc a poc que el soroll blanc, que creix linealment amb la banda.

En un sistema real,  $f_{\max}$
 el fixa l'amplada de banda equivalent (document 3), i  $f_{\min}$
 **no és zero**: el determina el temps total d'observació ( $f_{\min}\approx 1/T_{\text{obs}}$
), els filtres passaaltes del sistema o l'acoblament AC. En una mesura de durada finita no es poden observar fluctuacions de període infinit; la divergència matemàtica no implica un soroll infinit real. Sovint es prenen valors típics de  $f_{\min}$
 de l'ordre de 0,1 Hz o 0,01 Hz per a observacions llargues.

El caràcter logarítmic fa que  $f_{\min}$
 influeixi poc: baixar  $f_{\min}$
 des de 0,1 Hz fins a valors extraordinàriament petits (ordre de  $10^{-20}$
 Hz, períodes comparables a l'edat de l'univers) només augmenta el valor eficaç un factor d'aproximadament **2,4**. Tot i la divergència, doncs, l'efecte pràctic de considerar freqüències tan baixes és moderat.

Els fabricants d'amplificadors solen proporcionar la densitat de soroll blanc  $e_{n,white}$
 (constant per damunt d'una certa freqüència) i la densitat a una freqüència de referència (per exemple,  $e_n(10\ \mathrm{Hz})$
). Amb aquestes dades es descompon la densitat total en una part blanca i una 1/f, i s'integra sobre  $[f_{\min},f_{\max}]$
: ho farem en detall als exemples del document 5. La freqüència on totes dues components s'igualen s'anomena **freqüència corner**, i separa aproximadament la zona dominada pel soroll 1/f (per sota) de la dominada pel soroll blanc (per damunt).

> [!TIP] **Síntesi**
>
> El soroll shot apareix quan un corrent continu travessa una barrera de potencial; es modela com una font de corrent en paral·lel, és blanc, amb densitat  $S_i=2qI_{\text{dc}}$
> i valor eficaç  $i_{n,rms}=\sqrt{2qI_{\text{dc}}B}$
>. Sense corrent DC és negligible. El soroll 1/f (contacte / excés / flicker) domina a baixes freqüències, té densitat  $K/f^\alpha$
> amb  $\alpha\approx 1$
>, és no blanc, augmenta amb el corrent continu i depèn de la tecnologia. La seva variància integra com  $K\ln(f_{\max}/f_{\min})$
>: divergeix quan  $f_{\min}\to 0$
> però creix molt lentament, de manera que  $f_{\min}$
> (fixat pel temps d'observació) hi influeix poc. La freqüència corner separa la zona 1/f de la zona blanca.

[← 3. Amplada de banda equivalent de soroll](#amplada-de-banda-equivalent-de-soroll)[5. Modelatge de soroll en dispositius actius →](#modelatge-de-soroll-en-dispositius-actius)

---

<!-- FIN CAPÍTULO: 04_Unitat4_Soroll_shot_i_1f -->

---

<!-- INICIO CAPÍTULO: 05_Unitat4_Dispositius_actius -->

# Modelatge de soroll en dispositius actius

Sistemes de Mesura · **Unitat 4 — Soroll** · Document 5 de 6

# Modelatge de soroll en dispositius actius

Dedicació estimada: 15 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Representar el soroll d'un dispositiu actiu amb el model de quadripol i fonts referides a l'entrada (una de tensió i dues de corrent).
> - Combinar fonts de soroll independents per suma quadràtica.
> - Interpretar les dades de soroll d'un datasheet i separar la component blanca de la 1/f.
> - Calcular el valor eficaç de tensió i corrent de soroll d'un operacional per a diferents amplades de banda (Exemple 1).

## 1 Model de soroll d'un dispositiu actiu

Els dispositius actius —BJT, FET/MOSFET/JFET, amplificadors operacionals i d'instrumentació— són essencials en qualsevol sistema de mesura. A diferència dels passius, que només presenten soroll tèrmic (i, si escau, soroll en excés), els actius generen **simultàniament** diverses fonts internes: soroll tèrmic de resistències internes, soroll shot a totes les unions i soroll 1/f a trampes i interfícies. Modelar-lo bé és fonamental per predir el soroll total, comparar dispositius, identificar la font dominant i establir límits de detecció i SNR.

Un dispositiu actiu es representa de manera genèrica com un **quadripol** (xarxa de dos ports). El dispositiu real té múltiples fonts internes distribuïdes, però per a l'anàlisi externa no cal conèixer-les una a una —ni tan sols cal conèixer cada transistor intern del circuit integrat: n'hi ha prou de caracteritzar-ne l'efecte global vist des dels terminals. El model estàndard consisteix a considerar el dispositiu com un **quadripol ideal sense soroll** i afegir-hi fonts de soroll externes connectades a l'entrada, que representen tot el soroll intern referit a l'entrada.

![Dispositiu ideal sense soroll amb una font de tensió Vn en sèrie i una font de corrent In a l'entrada](assets/05_Unitat4_Dispositius_actius_img_1.png)

*Figura: Figura 4.6 Modelització del soroll a dispositius actius genèrics: el bloc és un dispositiu ideal sense soroll, i les fonts de soroll referides a l'entrada en representen tot el soroll intern.*

En el cas d'amplificadors (operacionals o d'instrumentació), el model sol incorporar **una font de tensió de soroll**  $e_n$
 (o  $V_n$
) en sèrie amb un terminal d'entrada —habitualment el no inversor— i **dues fonts de corrent de soroll** que deriven cap a massa, una per terminal.

![Amplificador operacional ideal amb en al terminal no inversor i dues fonts de corrent inn i inp](assets/05_Unitat4_Dispositius_actius_img_2.png)

*Figura: Figura 4.7 Modelització del soroll a amplificadors operacionals: font de tensió $e_n$
en sèrie a l'entrada i dues fonts de corrent $i_{\text{np}}$
, $i_{\text{nn}}$
, una a cada terminal.*

La **font de tensió**  $e_n$
, injectada a l'entrada del dispositiu ideal, produeix a la sortida el mateix efecte de soroll que el dispositiu real. Es caracteritza pel valor eficaç  $v_{n,rms}$
 o, més habitualment, per la densitat espectral  $e_n(f)$
 en **nV/√Hz**. Pot dependre de la freqüència, reflectint soroll blanc (constant) i soroll 1/f (creixent cap a baixes freqüències). Si el guany del dispositiu és  $A_v$
, la contribució a la sortida és  $A_v\cdot e_n$
. Aquesta font engloba soroll tèrmic de resistències internes, soroll shot de corrents interns i soroll 1/f d'interfícies (rellevant en MOSFET) o de la base en BJT.

A més, hi ha **dues fonts de corrent**  $i_{\text{np}}$
 (terminal no inversor) i  $i_{\text{nn}}$
 (terminal inversor), especificades amb una densitat espectral  $i_n(f)$
 en A/√Hz (sovint pA/√Hz o fA/√Hz). Provenen del soroll associat als corrents de polarització d'entrada: en BJT, soroll shot de la corrent de base; en FET/MOSFET, soroll shot i 1/f del corrent de fuita de porta. El model, per tant, *sí* que inclou fonts de corrent a les entrades, i aquestes es relacionen amb els corrents de polarització (no en són independents). Una font de corrent de soroll es converteix en tensió de soroll quan circula per una impedància de font o de retroalimentació; per això, si les impedàncies de font són baixes (pocs ohms) la contribució de les fonts de corrent pot ser negligible davant la de tensió, però amb impedàncies altes pot dominar.

### Combinació de fonts: suma quadràtica

Si tenim diverses fonts de soroll **independents** (no correlacionades), el valor eficaç total es calcula per **suma quadràtica** (pitagòrica) dels valors eficaços:

$$
v_{n,total} = \sqrt{v_{n,1}^2 + v_{n,2}^2 + \dots + v_{n,N}^2} \qquad (4.34)
$$

Això deriva del fet que, per a variables independents de mitjana nul·la, la variància total és la suma de les variàncies. La superposició de fonts de soroll és vàlida en circuits *lineals* de petit senyal: permet estudiar cada font per separat i combinar-ne després les contribucions quadràticament. Els fabricants proporcionen la informació de soroll en forma de gràfiques de  $e_n(f)$
 o  $i_n(f)$
, valors numèrics a freqüències representatives i, ocasionalment, soroll integrat per a una banda concreta —que *no* és aplicable a qualsevol altra banda sense recalcular.

### Quan el datasheet no ho diu tot: hipòtesis i aproximacions

Les dades de catàleg solen ser incompletes: el fabricant pot donar la densitat de tensió  $e_n(f)$
 a un parell de freqüències i la de corrent  $i_n(f)$
 a una de sola, sense indicar com evolucionen amb la freqüència. Per obtenir un valor eficaç cal, doncs, adoptar algunes **hipòtesis explícites**, deixar-les clares i comprovar com afecten el resultat.

Sobre la **densitat espectral de corrent**, quan només se'n coneix un valor a una freqüència prou alta (on el soroll 1/f ja és negligible), es poden considerar dues hipòtesis:

- **Hipòtesi A**: la densitat de corrent és proporcional a la de tensió,  $i_n(f)=k\,e_n(f)$
; totes dues comparteixen la mateixa forma freqüencial (la mateixa proporció de component 1/f).
- **Hipòtesi B**: la densitat de corrent és blanca, igual al valor especificat a totes les freqüències (sense component 1/f,  $K_i=0$
  ).

Per **separar la component blanca de la 1/f** d'una densitat (de tensió o de corrent) en modelem la suma quadràtica,  $e_n(f)=\sqrt{e_{n,white}^2+K_e/f}$
, i n'estimem els dos paràmetres a partir de dades de catàleg. Segons de quins punts disposem, hi ha dues aproximacions:

- **Aproximació 1**: usar dues dades numèriques a freqüències diferents (per exemple, 10 Hz i 1 kHz) i resoldre el sistema per obtenir  $e_{n,white}$
   i  $K_e$
.
- **Aproximació 2**: prendre la component blanca directament del valor a alta freqüència (1 kHz) i estimar  $K_e$
   a partir d'un punt a molt baixa freqüència de la gràfica, on domina el soroll 1/f.

A l'exemple següent es desenvolupa el cas de la **Hipòtesi A amb l'Aproximació 1**, i després es comparen els resultats amb la Hipòtesi B i l'Aproximació 2 (taula 4.1) per veure quan la tria és rellevant i quan no.

## 2 Exemple 1: valor eficaç de soroll d'un operacional

> [!EXAMPLE] **Exemple resolt**
>
> Estimar el valor eficaç de les fonts de tensió i de corrent de soroll d'un amplificador LT6020 per a dues amplades de banda equivalent de soroll: entre 0,1 Hz i 150 kHz, i entre 0,1 Hz i 10 Hz. Del datasheet (figura 4.8):  $e_n(10\ \mathrm{Hz})=50\ \mathrm{nV/\sqrt{Hz}}$
>,  $e_n(1\ \mathrm{kHz})=46\ \mathrm{nV/\sqrt{Hz}}$
> i  $i_n(1\ \mathrm{kHz})=37\ \mathrm{fA/\sqrt{Hz}}$
>.
>
>![Corba de densitat espectral de tensió vs freqüència i taula de valors del LT6020](assets/05_Unitat4_Dispositius_actius_img_3.png)
>
> *Figura: Figura 4.8 Especificacions de soroll de l'LT6020: densitat espectral de tensió en funció de la freqüència i valors tabulats.*
>
> El fabricant no indica com evoluciona  $i_n$
> amb la freqüència; només en dona un valor a 1 kHz. Se seguirà la **Hipòtesi A** (la densitat de corrent és proporcional a la de tensió) i l'**Aproximació 1** (usar les dades a 10 Hz i 1 kHz per separar les components blanca i 1/f).
>
> 1. Corrent a 10 Hz (Hipòtesi A).
>

$$
i_n(10\ \mathrm{Hz}) = e_n(10\ \mathrm{Hz})\cdot\frac{i_n(1\ \mathrm{kHz})}{e_n(1\ \mathrm{kHz})} = 50\cdot\frac{37}{46} = 40{,}2\ \mathrm{fA/\sqrt{Hz}}
$$

> 2. Model de dues components. A cada freqüència, la densitat és la suma quadràtica de la component blanca (constant) i la 1/f:
>

$$
e_n(f) = \sqrt{e_{n,white}^2 + \frac{K_e}{f}}, \qquad i_n(f) = \sqrt{i_{n,white}^2 + \frac{K_i}{f}}
$$

> 3. Separació de la tensió. De  $(50\ \mathrm{nV})^2=e_{n,white}^2+K_e/10$
> i  $(46\ \mathrm{nV})^2=e_{n,white}^2+K_e/1000$
>, restant s'obté
>

$$
K_e = 3{,}88\times 10^{-15}\ \mathrm{V^2}, \qquad e_{n,white} \approx 46\ \mathrm{nV/\sqrt{Hz}}
$$

> A 1 kHz, doncs, la component dominant és el soroll blanc.
> 4. Valor eficaç de tensió, banda 0,1 Hz–150 kHz.
>

$$
\sigma_{e,white} = e_{n,white}\sqrt{B} \approx 46\ \mathrm{nV}\cdot\sqrt{150\ \mathrm{kHz}} = 17{,}8\ \mu\mathrm{V}
$$

>

$$
\sigma_{e,\frac{1}{f}} = \sqrt{K_e\,\ln\!\left(\frac{150\ \mathrm{kHz}}{0{,}1\ \mathrm{Hz}}\right)} = 0{,}23\ \mu\mathrm{V}
$$

>

$$
\sigma_e = \sqrt{\sigma_{e,white}^2 + \sigma_{e,\frac{1}{f}}^2} \approx 17{,}8\ \mu\mathrm{V}
$$

> 5. Valor eficaç de corrent, mateixa banda. De manera anàloga s'obté  $K_i=2{,}5\times 10^{-27}\ \mathrm{A^2}$
>,  $i_{n,white}\approx 37\ \mathrm{fA/\sqrt{Hz}}$
>, i
>

$$
\sigma_{i,white} = 37\ \mathrm{fA}\cdot\sqrt{150\ \mathrm{kHz}} = 14{,}3\ \mathrm{pA}, \quad \sigma_{i,\frac{1}{f}} = 0{,}2\ \mathrm{pA}, \quad \sigma_i \approx 14{,}3\ \mathrm{pA}
$$

> 6. Banda estreta 0,1 Hz–10 Hz. Repetint els càlculs:
>

$$
\sigma_{e,white} = 46\ \mathrm{nV}\cdot\sqrt{10} = 145\ \mathrm{nV}, \quad \sigma_{e,\frac{1}{f}} = 134\ \mathrm{nV}, \quad \sigma_e = 197\ \mathrm{nV}
$$

>

$$
\sigma_{i,white} = 117\ \mathrm{fA}, \quad \sigma_{i,\frac{1}{f}} = 107\ \mathrm{fA}, \quad \sigma_i = 159\ \mathrm{fA}
$$

> 7. Lectura del resultat. En reduir la banda, el valor eficaç cau (tant de tensió com de corrent) i, alhora, la contribució del soroll 1/f esdevé *comparable* a la del soroll blanc: a banda ampla domina el blanc; a banda estreta i propera a contínua, tots dos hi pesen. La component 1/f, per tant, no es pot ignorar sempre a baixes freqüències.

Si en lloc de la Hipòtesi A s'usa la Hipòtesi B ( $i_n$
 blanc de 37 fA/√Hz, sense component 1/f,  $K_i=0$
), l'única diferència apreciable és el corrent a banda estreta, que baixa a 107 fA. I si s'usa l'Aproximació 2 (estimar la densitat 1/f a partir d'un punt a molt baixa freqüència,  $e_n(0{,}1\ \mathrm{Hz})=80\ \mathrm{nV/\sqrt{Hz}}$
), s'obté un  $K_e$
 força diferent però valors eficaços del mateix ordre. La taula 4.1 resumeix els quatre casos.

| Model de  $i_n$ | $\sigma_e$   (0,1 Hz–150 kHz) | $\sigma_i$   (0,1 Hz–150 kHz) | $\sigma_e$   (0,1 Hz–10 Hz) | $\sigma_i$   (0,1 Hz–10 Hz) |
|:--- |:--- |:--- |:--- |:--- |
| $i_n=k\,e_n$   · 10 Hz+1 kHz | 17,8 μV | 14,3 pA | 197 nV | 159 fA |
| $i_n=37\ \mathrm{fA/\sqrt{Hz}}$   · 10 Hz+1 kHz | 17,8 μV | 14,3 pA | 197 nV | 107 fA |
| $i_n=k\,e_n$   · 0,1 Hz+1 kHz | 17,8 μV | 14,3 pA | 151 nV | 122 fA |
| $i_n=37\ \mathrm{fA/\sqrt{Hz}}$   · 0,1 Hz+1 kHz | 17,8 μV | 14,3 pA | 151 nV | 107 fA |

Per a la banda ampla, qualsevol hipòtesi i aproximació dona el mateix resultat; a baixes freqüències hi ha canvis lleugers deguts a estimacions diferents del soroll 1/f, que —com que prové de defectes i inhomogeneïtats— està sotmès a una alta variabilitat. Aquesta insensibilitat en banda ampla és útil: en la pràctica, per a bandes de mesura amplies n'hi ha prou amb la component blanca del datasheet. Al document 6 aplicarem aquestes idees a un circuit complet amb amplificador inversor.

> [!TIP] **Síntesi**
>
> El soroll d'un amplificador es modela amb fonts referides a l'entrada: una de tensió  $e_n$
> (nV/√Hz) en sèrie i dues de corrent  $i_{\text{np}}, i_{\text{nn}}$
> (pA/fA/√Hz), aquestes lligades als corrents de polarització. Les fonts independents es combinen per suma quadràtica. Del datasheet se separa la component blanca de la 1/f resolent el sistema a dues freqüències. En l'exemple de l'LT6020, a banda ampla (0,1 Hz–150 kHz) domina el soroll blanc ( $\sigma_e\approx 17{,}8\ \mu\mathrm{V}$
>,  $\sigma_i\approx 14{,}3\ \mathrm{pA}$
> ) i el resultat és insensible a les hipòtesis; a banda estreta (0,1 Hz–10 Hz) la component 1/f esdevé comparable a la blanca i el resultat depèn més del model triat.

[← 4. Altres fonts de soroll: shot i 1/f](#altres-fonts-de-soroll-shot-i-1f)[6. Soroll en amplificadors i disseny de baix soroll →](#soroll-en-amplificadors-i-disseny-de-baix-soroll)

---

<!-- FIN CAPÍTULO: 05_Unitat4_Dispositius_actius -->

---

<!-- INICIO CAPÍTULO: 06_Unitat4_Amplificador_inversor_i_disseny -->

# Soroll en amplificadors i disseny de baix soroll

Sistemes de Mesura · **Unitat 4 — Soroll** · Document 6 de 6

# Soroll en amplificadors i disseny de baix soroll

Dedicació estimada: 14 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Propagar totes les fonts de soroll d'un amplificador inversor cap a la sortida i referir-les a l'entrada.
> - Veure com el producte guany-amplada de banda (GBW) i un condensador de retroalimentació fixen l'amplada de banda i, per tant, el soroll.
> - Identificar la font dominant i el paper del guany de soroll.
> - Sintetitzar una guia de disseny de baix soroll: resistències, amplada de banda, dispositius actius, arquitectura, corrents de polarització i temperatura.

## 1 Exemple 2: soroll en un amplificador inversor

> [!EXAMPLE] **Exemple resolt**
>
> Calcular la tensió eficaç de soroll d'un amplificador inversor amb  $R_1=100\ \Omega$
> i  $R_2=10\ \mathrm{k\Omega}$
> (guany ideal  $-100$
> ), tots els components a 25 °C, referida a la sortida i al terminal no inversor de l'operacional. Es considera primer el cas sense condensador (banda limitada pel GBW) i després amb un condensador  $C=16\ \mathrm{nF}$
> de retroalimentació. Es pren que les resistències només tenen soroll tèrmic. Del datasheet:  $e_{n,white}=12\ \mathrm{nV/\sqrt{Hz}}$
>,  $i_{n,white}=200\ \mathrm{fA/\sqrt{Hz}}$
>,  $e_n(10\ \mathrm{Hz})\approx 50\ \mathrm{nV/\sqrt{Hz}}$
>,  $i_n(10\ \mathrm{Hz})\approx 2\ \mathrm{pA/\sqrt{Hz}}$
>, i GBW amb guany unitari a ~20 MHz.
>
>![Esquema de l'amplificador inversor amb R1, R2 i condensador C de retroalimentació](assets/06_Unitat4_Amplificador_inversor_i_disseny_img_1.png)
>
> *Figura: Figura 4.9 Amplificador inversor. El condensador $C$
> limita l'amplada de banda del circuit.*
>
> 1. Components 1/f del datasheet. Restant quadràticament la part blanca:
>

$$
e_{n,\frac{1}{f}}(10\ \mathrm{Hz}) = \sqrt{50^2-12^2} = 48{,}5\ \mathrm{nV/\sqrt{Hz}} \;\Rightarrow\; e_{n,\frac{1}{f}}(f)=\frac{153\ \mathrm{nV}}{\sqrt{f}}
$$

>

$$
i_{n,\frac{1}{f}}(10\ \mathrm{Hz}) = \sqrt{2^2-0{,}2^2} = 1{,}99\ \mathrm{pA/\sqrt{Hz}} \;\Rightarrow\; i_{n,\frac{1}{f}}(f)=\frac{6{,}3\ \mathrm{pA}}{\sqrt{f}}
$$

> 2. Amplada de banda sense condensador. Amb el pol dominant,  $f_{-3\,\mathrm{dB}}=\mathrm{GBW}/(1+R_2/R_1)$
>. De la corba de guany en llaç obert (figura 4.10), el guany unitari és a ~20 MHz:
>

$$
f_{-3\,\mathrm{dB}} = \frac{20\ \mathrm{MHz}}{101} = 198\ \mathrm{kHz}, \qquad B = \frac{\pi}{2}f_{-3\,\mathrm{dB}} = 311\ \mathrm{kHz}
$$

> Amb el condensador,  $f_{-3\,\mathrm{dB}}=\frac{1}{2\pi R_2 C}=995\ \mathrm{Hz}$
> i  $B=\frac{\pi}{2}\cdot 995=1{,}56\ \mathrm{kHz}$
>.
> 3. Propagació de les cinc fonts a la sortida. Aplicant superposició (cada resistència aporta  $\sqrt{4kTRB}$
>;  $\sigma_{en\,OpAmp}$
> és la tensió de soroll de l'operacional al terminal no inversor;  $\sigma_{inx\,OpAmp}$
> la font de corrent del terminal  $x$
> cap a massa):
>

$$
\sigma_{en\,R1}(V_{\text{out}}) = \sqrt{4kTR_1 B}\cdot\frac{R_2}{R_1}, \qquad \sigma_{en\,R2}(V_{\text{out}}) = \sqrt{4kTR_2 B}
$$

>

$$
\sigma_{en\,OpAmp}(V_{\text{out}}) = \sigma_{en\,OpAmp}\cdot\left(1+\frac{R_2}{R_1}\right), \quad \sigma_{inp\,OpAmp}(V_{\text{out}}) = 0, \quad \sigma_{inn\,OpAmp}(V_{\text{out}}) = \sigma_{inn\,OpAmp}\cdot R_2
$$

> 4. Fonts de l'operacional (sense C, B=311 kHz).
>

$$
\sigma_{en\,OpAmp,\,white} = 12\ \mathrm{nV}\cdot\sqrt{311\ \mathrm{kHz}} = 6{,}69\ \mu\mathrm{V}, \quad \sigma_{en\,OpAmp,\,\frac{1}{f}} = 153\ \mathrm{nV}\sqrt{\ln\frac{311\,\mathrm{kHz}}{0{,}1\,\mathrm{Hz}}} = 0{,}59\ \mu\mathrm{V}
$$

>

$$
\sigma_{en\,OpAmp} = 6{,}72\ \mu\mathrm{V}, \qquad \sigma_{in\,OpAmp} = \sqrt{(111{,}5\ \mathrm{pA})^2+(24{,}4\ \mathrm{pA})^2} = 114{,}1\ \mathrm{pA}
$$

> (Nota: prendre  $f_{\min}=0{,}1\ \mathrm{Hz}$
> en lloc de l'edat de l'univers només canviaria  $\sigma_{en\,\frac{1}{f}}$
> un factor ~2; la tria no és crítica.)
> 5. Resistències (sense C).
>

$$
\sigma_{en\,R1} = \sqrt{4kTR_1 B} = 715\ \mathrm{nV}, \qquad \sigma_{en\,R2} = \sqrt{4kTR_2 B} = 7{,}15\ \mu\mathrm{V}
$$

> 6. Soroll total a la sortida (sense C).
>

$$
\sigma_{n,total}(V_{\text{out}}) = \sqrt{\left(\sigma_{en\,R1}\frac{R_2}{R_1}\right)^2+\sigma_{en\,R2}^2+\left(\sigma_{en\,OpAmp}(1+\frac{R_2}{R_1})\right)^2+(\sigma_{in\,OpAmp}R_2)^2} = 683\ \mu\mathrm{V}
$$

> La font principal és  $\sigma_{en\,OpAmp}$
>, que es propaga multiplicada per 101. El soroll de  $R_2$
>, tot i tenir un valor eficaç similar, hi pesa menys perquè passa directament a la sortida (guany 1). Referit al terminal no inversor:
>

$$
\sigma_{n,total}(V_+) = \frac{\sigma_{n,total}(V_{\text{out}})}{1+R_2/R_1} = 6{,}8\ \mu\mathrm{V} \approx \sigma_{en\,OpAmp}
$$

> 7. Amb el condensador (B=1,56 kHz). Recalculant amb la banda reduïda:  $\sigma_{en\,OpAmp}=671\ \mathrm{nV}$
>,  $\sigma_{in\,OpAmp}=21{,}1\ \mathrm{pA}$
>,  $\sigma_{en\,R1}=50{,}7\ \mathrm{nV}$
>,  $\sigma_{en\,R2}=507\ \mathrm{nV}$
>, i
>

$$
\sigma_{n,total}(V_{\text{out}}) = 68\ \mu\mathrm{V}, \qquad \sigma_{n,total}(V_+) = 680\ \mathrm{nV} \approx \sigma_{en\,OpAmp}
$$

![Guany en llaç obert de l'operacional en funció de la freqüència](assets/06_Unitat4_Amplificador_inversor_i_disseny_img_2.png)

*Figura: Figura 4.10 Guany en llaç obert de l'amplificador operacional; el guany unitari (0 dB) es dona cap als 20 MHz.*

![Densitat espectral de tensió (vermell) i de corrent (blau) de l'operacional](assets/06_Unitat4_Amplificador_inversor_i_disseny_img_3.png)

*Figura: Figura 4.11 Densitat espectral de tensió (en vermell) i de corrent (en blau) de l'amplificador operacional.*

Dos resultats clau. Primer: la font de tensió de soroll de l'operacional es propaga cap a la sortida multiplicada pel **guany de soroll**  $1+R_2/R_1$
 (aquí 101), *no* pel valor absolut del guany de senyal inversor  $R_2/R_1$
 (100). Segon: reduir la banda amb el condensador redueix clarament el soroll (de 683 μV a 68 μV a la sortida), tot i que  $\sigma_{en\,OpAmp}$
 continua sent la font dominant. Cal notar que la resistència de retroalimentació  $R_2$
 *sí* que genera soroll tèrmic que contribueix directament a la sortida —no queda «anul·lada» per estar connectada al node de sortida—, i que afegir el condensador *redueix* el soroll blanc integrat perquè *redueix* la banda. Si es volgués rebaixar el soroll sense tocar la banda, caldria un operacional amb una densitat de tensió de soroll més petita.

## 2 Guia de disseny de circuits de baix soroll

L'objectiu del disseny de baix soroll és reduir el valor eficaç de soroll **referit a l'entrada** fins que sigui clarament inferior al senyal mínim que cal mesurar, mantenint consum, cost i prestacions dins dels requeriments. Cal combinar decisions sobre components passius, dispositius actius, arquitectura i condicions de funcionament.

### Resistències

El soroll tèrmic apareix a totes les resistències i a la part real de qualsevol impedància, amb  $S_v=4kTR$
 i valor eficaç  $v_n=\sqrt{4kTRB_{\text{eq}}}$
. Reduir-lo passa per actuar sobre  $R$
 i sobre  $B_{\text{eq}}$
. Reduir  $R$
 disminueix la tensió de soroll ( $v_n\propto\sqrt{R}$
), però amb una alimentació donada, resistències més petites impliquen més corrent i, per tant, més consum i escalfament: **reduir totes les resistències a zero no és una solució pràctica sense inconvenients**. Directrius: en etapes d'entrada d'alta impedància, resistències de pocs kΩ o menys per limitar la tensió de soroll; en transimpedància (fotodíodes), la resistència de retroalimentació  $R_f$
 (que pot ser de molts MΩ) sol ser una contribució principal de soroll tèrmic i cal buscar un compromís entre soroll i sensibilitat.

També importa la **tecnologia**: la pel·lícula metàl·lica té soroll en excés molt baix i s'acosta al límit tèrmic pur, mentre que el carbó o composició en té molt més, amb espectre 1/f, que degrada les mesures lentes.

### Amplada de banda

Com que el soroll blanc integrat creix amb  $\sqrt{B_{\text{eq}}}$
, limitar l'amplada de banda és una de les estratègies més eficients. Ara bé, una banda massa estreta degrada la resposta temporal (constants de temps llargues). Principis: definir la banda útil del senyal (0,1–100 Hz per a biomèdica, 10 Hz–20 kHz per a àudio); dimensionar el passabaixes perquè  $f_{-3\,\mathrm{dB}}$
 sigui només lleugerament superior a la freqüència màxima útil; si el senyal és en una banda estreta lluny de contínua, usar **filtres passabanda** per limitar alhora el soroll 1/f a molt baixa freqüència i el soroll blanc a alta. Ampliar la banda molt per sobre del contingut útil *empitjora* la SNR. Un condensador de retroalimentació o de desacoblament és una manera pràctica d'ajustar la banda.

### Dispositius actius i arquitectura

Un cop optimitzats resistències i banda, el soroll dels dispositius actius sol ser dominant. Un operacional de baix soroll es caracteritza per una densitat de tensió de soroll baixa (pocs nV/√Hz), una densitat de corrent reduïda (crítica amb resistències de font grans) i una freqüència de corner 1/f tan baixa com sigui possible. Tot i així, **l'operacional amb la menor  $e_n$
 no sempre és òptim**: si la impedància de font és molt alta, pot dominar el soroll de corrent, i llavors interessa una  $i_n$
 baixa (entrades FET o CMOS, amb corrents de polarització mínims). Per triar un dispositiu cal considerar simultàniament  $e_n$
,  $i_n$
, la banda útil, la impedància de font i el soroll 1/f.

L'arquitectura de la cadena té un impacte decisiu. El soroll d'una etapa posterior, referit a l'entrada, es divideix pel guany de les etapes anteriors:

$$
e_{n,tot}^2 \approx e_{n1}^2 + \left(\frac{e_{n2}}{G_1}\right)^2 + \dots \qquad (4.35)
$$

Per tant, una **primera etapa d'alt guany i baix soroll** tan a prop del sensor com sigui possible fa que el soroll de les etapes següents (filtres, amplificadors intermedis, convertidor A/D) sigui minoritari. La regla és: «la primera etapa fixa el soroll del sistema». En canvi, si la primera etapa té guany insuficient o soroll elevat, el de les posteriors pot esdevenir dominant. Per això la primera etapa és *crítica*, no pas poc important pel fet que les posteriors tinguin molt de guany.

### Corrents de polarització i temperatura

El soroll shot i el 1/f estan lligats als corrents continus per unions i contactes. Per al shot,  $i_n=\sqrt{2qI_{\text{dc}}B_{\text{eq}}}$
: reduir  $I_{\text{dc}}$
 el redueix amb l'arrel quadrada. Per al 1/f, limitar corrents continus per resistències crítiques (reconfigurant divisors o usant acoblament AC) ajuda. Però reduir massa els corrents té **compromisos**: menys marge dinàmic, resposta més lenta, més distorsió i menys linealitat. No sempre millora totes les prestacions; cal un punt de funcionament òptim, sovint recomanat pel fabricant.

La temperatura intervé directament en el soroll tèrmic ( $4kTRB_{\text{eq}}$
, amb  $v_n\propto\sqrt{T}$
). El **refredament criogènic** (nitrogen o heli líquids) pot reduir-lo, però comporta cost, complexitat mecànica, requisits de buit, condensació i possible degradació d'altres prestacions; per tant, *no* és una solució senzilla, barata ni habitual en equips docents, ni la primera estratègia en sistemes de baix cost, ni redueix el soroll total a zero. Només es justifica en casos extrems (radioastronomia, detectors de partícules, bolòmetres). En sistemes convencionals, és preferible optimitzar resistències, banda, dispositius i arquitectura a temperatura ambient controlada abans de plantejar refrigeració, i reservar-la per quan el soroll tèrmic és clarament el límit dominant i ja s'han esgotat les altres tècniques.

> [!WARNING] **Recordatori**
>
> El soroll extrínsec (interferències) i l'intrínsec no es redueixen sempre amb les mateixes tècniques: apantallament, disposició de cables i masses per al primer; selecció de components, banda i arquitectura per al segon. Reduir un no garanteix reduir l'altre.

> [!TIP] **Síntesi**
>
> En un amplificador inversor, la tensió de soroll de l'operacional es propaga a la sortida amb el guany de soroll  $1+R_2/R_1$
> i sol ser la font dominant;  $R_2$
> aporta soroll tèrmic directe i un condensador de retroalimentació redueix el soroll en reduir la banda. La guia de baix soroll: resistències petites de pel·lícula metàl·lica als camins crítics (sense caure en consums excessius), banda ajustada al senyal útil ( $\propto\sqrt{B_{\text{eq}}}$
>, amb passabanda si cal), dispositius actius triats considerant  $e_n$
>,  $i_n$
>, corner 1/f i impedància de font, primera etapa d'alt guany i baix soroll ( $e_{n,tot}^2\approx e_{n1}^2+(e_{n2}/G_1)^2$
> ), corrents de polarització mínims amb compromís de linealitat, i refredament només en casos extrems. Reduir soroll intrínsec i extrínsec requereix tècniques diferents.

[← 5. Modelatge de soroll en dispositius actius](#modelatge-de-soroll-en-dispositius-actius)

---

<!-- FIN CAPÍTULO: 06_Unitat4_Amplificador_inversor_i_disseny -->

---

<!-- INICIO CAPÍTULO: 07_Entrenament_Tema4 -->

# Entrenament V/F · Unitat 4: Soroll

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
> 📌 **Afirmació:** *El soroll és un component aleatori superposat al senyal que, si és additiu i no correlacionat, contribueix a la incertesa amb el seu valor eficaç.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El valor eficaç (RMS) del soroll additiu i no correlacionat és directament la incertesa típica associada (document 1).*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 02
> 📌 **Afirmació:** *Un calibratge prou acurat elimina el soroll d'un sistema de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El calibratge corregeix els errors sistemàtics; el soroll és aleatori i no s'elimina calibrant.*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 03
> 📌 **Afirmació:** *El soroll intrínsec d'un sistema de mesura prové exclusivament de fonts externes, com la xarxa elèctrica o equips propers.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Això és el soroll extrínsec. L'intrínsec es genera dins del sistema (resistències, semiconductors, contactes).*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *Augmentar el guany d'un amplificador millora sempre la relació senyal-soroll, encara que s'amplifiqui també el soroll d'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El guany amplifica per igual senyal i soroll d'entrada; no millora per si sol la SNR.*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *Per a soroll blanc, el valor eficaç integrat creix amb l'arrel quadrada de l'amplada de banda.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En integrar una densitat constant sobre B, el valor eficaç resulta proporcional a √B.*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *Un procés estocàstic estacionari té una mitjana que varia periòdicament amb el temps.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Estacionari vol dir que les propietats estadístiques (mitjana, variància, espectre) no canvien amb el temps.*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 07
> 📌 **Afirmació:** *La hipòtesi d'ergodicitat permet estimar la variància del soroll a partir d'una única realització prou llarga.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'ergodicitat substitueix la mitjana sobre moltes realitzacions per una mitjana temporal sobre una de sola.*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *Per a un soroll de mitjana nul·la, la desviació estàndard coincideix amb el valor eficaç (RMS).*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Totes dues es defineixen com l'arrel quadrada de la mitjana del quadrat del senyal.*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 09
> 📌 **Afirmació:** *En una distribució normal, aproximadament el 95 % de les mostres cauen dins de l'interval ±2σ.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Els percentatges gaussians de referència són 68 % (±σ), 95 % (±2σ) i 99,7 % (±3σ).*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 10
> 📌 **Afirmació:** *Un procés blanc ideal té un espectre de potència nul a totes les freqüències excepte a freqüència zero.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El procés blanc té espectre de potència constant (pla) a totes les freqüències, no nul.*

> **📚 Document de referència:** `1. Soroll, incertesa i caracterització estadística`
> </details>

### Qüestió 11
> 📌 **Afirmació:** *El soroll tèrmic (Johnson-Nyquist) s'origina en l'agitació tèrmica dels portadors de càrrega als materials conductors.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Les fluctuacions microscòpiques de tensió i corrent per agitació tèrmica generen el soroll als terminals de la resistència.*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 12
> 📌 **Afirmació:** *Qualsevol resistència real a temperatura superior al zero absolut genera soroll tèrmic, encara que no hi circuli corrent continu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El soroll tèrmic només depèn de la temperatura; apareix fins i tot amb la resistència desconnectada.*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *El soroll tèrmic d'una resistència només apareix quan hi circula un corrent continu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És independent del corrent; només depèn de la temperatura, la resistència i la banda.*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 14
> 📌 **Afirmació:** *La tensió eficaç de soroll tèrmic d'una resistència augmenta amb l'arrel quadrada de la resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *De Vt=√(4kTBR), la tensió creix amb √R (i el corrent In=√(4kTB/R) decreix amb √R).*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 15
> 📌 **Afirmació:** *La tensió eficaç de soroll tèrmic d'una resistència és proporcional a R, no a l'arrel quadrada de R.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És proporcional a √R: Vt=√(4kTBR).*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 16
> 📌 **Afirmació:** *El corrent eficaç de soroll tèrmic d'una resistència disminueix quan augmenta el valor de la resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *In=√(4kTB/R): una resistència gran genera més tensió però menys corrent de soroll.*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 17
> 📌 **Afirmació:** *La potència de soroll disponible d'una resistència adaptada és proporcional al quadrat del valor de la resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És independent de R i val 4kTB (conseqüència del teorema de màxima transferència de potència).*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 18
> 📌 **Afirmació:** *En el model de Thévenin del soroll tèrmic, la font de soroll es posa en paral·lel amb la resistència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En Thévenin la font de tensió va en sèrie; és en Norton on la font de corrent va en paral·lel.*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 19
> 📌 **Afirmació:** *Els condensadors i inductors ideals no generen soroll tèrmic propi perquè no dissipen energia.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Només la part real (dissipativa) de la impedància, 4kT·R(f), contribueix al soroll tèrmic.*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 20
> 📌 **Afirmació:** *Les resistències de carbó són preferibles a les de pel·lícula metàl·lica en circuits de baix soroll.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És a l'inrevés: la pel·lícula metàl·lica té molt menys soroll en excés i s'acosta al límit tèrmic teòric.*

> **📚 Document de referència:** `2. Soroll tèrmic i models de resistència`
> </details>

### Qüestió 21
> 📌 **Afirmació:** *L'amplada de banda equivalent de soroll substitueix la resposta freqüencial real per un filtre rectangular ideal que deixa passar la mateixa potència de soroll.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició del concepte: un rectangle d'alçada A₀² amb la mateixa àrea sota |A(f)|².*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *La definició formal de l'amplada de banda equivalent integra el mòdul al quadrat de la resposta freqüencial.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Beq = (1/A₀²)·∫|A(f)|² df; la potència de soroll a la sortida és proporcional a |A(f)|².*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 23
> 📌 **Afirmació:** *En un sistema real, l'amplada de banda equivalent de soroll coincideix exactament amb la freqüència de tall a −3 dB.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En sistemes reals Beq és més gran que f−3dB per la contribució de la banda de transició.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 24
> 📌 **Afirmació:** *Un filtre passabaixes de primer ordre té una amplada de banda equivalent igual a (π/2)·f−3dB ≈ 1,57·f−3dB.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La integral de 1/(1+x²) dona π/2; el filtre deixa passar un 57 % més de potència que un rectangular ideal.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 25
> 📌 **Afirmació:** *Un filtre passabaixes de primer ordre deixa passar menys soroll que un filtre rectangular ideal amb la mateixa freqüència de tall a −3 dB.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En deixa passar més (un 57 % més) per la cua que decreix lentament a −20 dB/dècada.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *Per a un filtre Butterworth passabaixes de segon ordre, l'amplada de banda equivalent és aproximadament 1,11·f−3dB.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La caiguda més ràpida (−40 dB/dècada) redueix Beq respecte al primer ordre.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *A mesura que augmenta l'ordre del filtre Butterworth, la relació entre amplada de banda equivalent i f−3dB tendeix a la unitat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Com més abrupta és la transició, més s'aproxima la resposta a la del filtre ideal.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 28
> 📌 **Afirmació:** *Un filtre passabaixes de primer ordre cau a −40 dB/dècada immediatament després de la freqüència de tall.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Un filtre de primer ordre cau a −20 dB/dècada; el de segon ordre a −40 dB/dècada.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 29
> 📌 **Afirmació:** *En un sistema passabanda amb la freqüència inferior molt menor que la superior, l'amplada de banda equivalent queda dominada pel límit superior.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *S'aproxima per la del passabaixes de freqüència de tall igual a la superior.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 30
> 📌 **Afirmació:** *Per a un sistema passabanda ideal, l'amplada de banda equivalent és la suma de les dues freqüències de tall.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És la diferència entre la freqüència superior i la inferior de pas, no la suma.*

> **📚 Document de referència:** `3. Amplada de banda equivalent de soroll`
> </details>

### Qüestió 31
> 📌 **Afirmació:** *El soroll shot apareix quan un corrent continu travessa una barrera de potencial, com en una unió PN.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Està associat al pas discret de càrrega (estadística de Poisson) a través de la barrera.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *El soroll shot apareix amb la mateixa intensitat encara que no circuli corrent continu per la unió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Sense corrent continu apreciable, el soroll shot associat a la unió és negligible.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 33
> 📌 **Afirmació:** *La densitat espectral de potència del corrent de soroll shot és Si = 2·q·Idc, proporcional al corrent continu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És un soroll blanc amb densitat proporcional al corrent continu que travessa la unió.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *El soroll shot es modela habitualment com una font de corrent de soroll en paral·lel amb la unió que el genera.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El corrent continu es modela amb la branca ideal i el soroll shot com una font de corrent en paral·lel.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 35
> 📌 **Afirmació:** *Un fotodíode il·luminat no pot presentar soroll shot perquè el corrent és d'origen òptic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El corrent fotoinduït és un corrent continu que travessa una unió i, per tant, presenta soroll shot.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 36
> 📌 **Afirmació:** *El soroll 1/f té una densitat espectral que decreix aproximadament amb la inversa de la freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Es modela com Sv(f)=K/f^α amb α proper a 1; per això no és blanc.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 37
> 📌 **Afirmació:** *El soroll 1/f és un soroll blanc perquè la seva densitat espectral és constant amb la freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La seva densitat depèn de la freqüència (∝1/f); per definició, doncs, no és blanc.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 38
> 📌 **Afirmació:** *El soroll 1/f domina generalment a baixes freqüències.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En créixer cap a baixes freqüències, és especialment rellevant en mesures lentes.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 39
> 📌 **Afirmació:** *Per a un model 1/f de densitat K/f, la variància integrada entre fmin i fmax és K·ln(fmax/fmin).*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La integral de K/f dona una dependència logarítmica del quocient de freqüències.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 40
> 📌 **Afirmació:** *El soroll 1/f es pot integrar des de freqüència zero sense cap problema físic ni matemàtic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Divergeix logarítmicament quan fmin→0; a la pràctica fmin el fixa el temps d'observació o un filtre passaaltes.*

> **📚 Document de referència:** `4. Soroll shot i soroll 1/f`
> </details>

### Qüestió 41
> 📌 **Afirmació:** *El soroll d'un dispositiu actiu es modela amb fonts equivalents referides a l'entrada: una de tensió i, típicament, dues de corrent.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El dispositiu es tracta com un quadripol ideal sense soroll amb les fonts referides a l'entrada.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 42
> 📌 **Afirmació:** *La densitat espectral de tensió de soroll d'un amplificador operacional s'expressa habitualment en A/√Hz.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La densitat de tensió s'expressa en V/√Hz (sovint nV/√Hz); l'A/√Hz és per a la densitat de corrent.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 43
> 📌 **Afirmació:** *Les fonts de soroll independents es combinen per suma quadràtica: l'arrel de la suma dels quadrats dels valors eficaços.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per a fonts independents de mitjana nul·la, la variància total és la suma de variàncies.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 44
> 📌 **Afirmació:** *Dues fonts de soroll independents es combinen sumant aritmèticament els seus valors eficaços.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Es combinen per suma quadràtica (pitagòrica), no aritmètica.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 45
> 📌 **Afirmació:** *Amb impedàncies de font molt elevades, el soroll de corrent d'entrada d'un amplificador és sempre irrellevant.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Amb impedàncies de font altes, el soroll de corrent (convertit en tensió) pot esdevenir la contribució dominant.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 46
> 📌 **Afirmació:** *En un amplificador inversor, la tensió de soroll de l'operacional es propaga a la sortida multiplicada pel guany de soroll (1+R2/R1).*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El guany de soroll (1+R2/R1) no coincideix amb el valor absolut del guany de senyal inversor (R2/R1).*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 47
> 📌 **Afirmació:** *En un amplificador inversor, la resistència de retroalimentació no genera soroll tèrmic perquè està connectada al node de sortida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Sí que genera soroll tèrmic, que contribueix directament a la sortida.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *Afegir un condensador de retroalimentació en un amplificador inversor pot reduir l'amplada de banda i, per tant, el soroll blanc integrat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En limitar la banda es redueix el soroll blanc integrat, que creix amb √Beq.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *La primera etapa d'una cadena de mesura és poc important per al soroll si les etapes posteriors tenen molt de guany.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És crítica: el seu soroll queda referit directament a l'entrada, mentre que el de les posteriors es divideix pel guany previ.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

### Qüestió 50
> 📌 **Afirmació:** *El refredament criogènic és la primera estratègia que s'ha d'aplicar en qualsevol sistema de mesura de baix cost.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Es reserva per a casos molt exigents; primer s'optimitzen resistències, banda, dispositius i arquitectura a temperatura ambient.*

> **📚 Document de referència:** `5. Dispositius actius, amplificadors i disseny de baix soroll`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | El valor eficaç (RMS) del soroll additiu i no correlacionat és directament la incertesa típica associada (document 1). | 1. Soroll, incertesa i caracterització estadística |
| **02** | **F** | El calibratge corregeix els errors sistemàtics; el soroll és aleatori i no s'elimina calibrant. | 1. Soroll, incertesa i caracterització estadística |
| **03** | **F** | Això és el soroll extrínsec. L'intrínsec es genera dins del sistema (resistències, semiconductors, contactes). | 1. Soroll, incertesa i caracterització estadística |
| **04** | **F** | El guany amplifica per igual senyal i soroll d'entrada; no millora per si sol la SNR. | 1. Soroll, incertesa i caracterització estadística |
| **05** | **V** | En integrar una densitat constant sobre B, el valor eficaç resulta proporcional a √B. | 1. Soroll, incertesa i caracterització estadística |
| **06** | **F** | Estacionari vol dir que les propietats estadístiques (mitjana, variància, espectre) no canvien amb el temps. | 1. Soroll, incertesa i caracterització estadística |
| **07** | **V** | L'ergodicitat substitueix la mitjana sobre moltes realitzacions per una mitjana temporal sobre una de sola. | 1. Soroll, incertesa i caracterització estadística |
| **08** | **V** | Totes dues es defineixen com l'arrel quadrada de la mitjana del quadrat del senyal. | 1. Soroll, incertesa i caracterització estadística |
| **09** | **V** | Els percentatges gaussians de referència són 68 % (±σ), 95 % (±2σ) i 99,7 % (±3σ). | 1. Soroll, incertesa i caracterització estadística |
| **10** | **F** | El procés blanc té espectre de potència constant (pla) a totes les freqüències, no nul. | 1. Soroll, incertesa i caracterització estadística |
| **11** | **V** | Les fluctuacions microscòpiques de tensió i corrent per agitació tèrmica generen el soroll als terminals de la resist... | 2. Soroll tèrmic i models de resistència |
| **12** | **V** | El soroll tèrmic només depèn de la temperatura; apareix fins i tot amb la resistència desconnectada. | 2. Soroll tèrmic i models de resistència |
| **13** | **F** | És independent del corrent; només depèn de la temperatura, la resistència i la banda. | 2. Soroll tèrmic i models de resistència |
| **14** | **V** | De Vt=√(4kTBR), la tensió creix amb √R (i el corrent In=√(4kTB/R) decreix amb √R). | 2. Soroll tèrmic i models de resistència |
| **15** | **F** | És proporcional a √R: Vt=√(4kTBR). | 2. Soroll tèrmic i models de resistència |
| **16** | **V** | In=√(4kTB/R): una resistència gran genera més tensió però menys corrent de soroll. | 2. Soroll tèrmic i models de resistència |
| **17** | **F** | És independent de R i val 4kTB (conseqüència del teorema de màxima transferència de potència). | 2. Soroll tèrmic i models de resistència |
| **18** | **F** | En Thévenin la font de tensió va en sèrie; és en Norton on la font de corrent va en paral·lel. | 2. Soroll tèrmic i models de resistència |
| **19** | **V** | Només la part real (dissipativa) de la impedància, 4kT·R(f), contribueix al soroll tèrmic. | 2. Soroll tèrmic i models de resistència |
| **20** | **F** | És a l'inrevés: la pel·lícula metàl·lica té molt menys soroll en excés i s'acosta al límit tèrmic teòric. | 2. Soroll tèrmic i models de resistència |
| **21** | **V** | És la definició del concepte: un rectangle d'alçada A₀² amb la mateixa àrea sota \|A(f)\|². | 3. Amplada de banda equivalent de soroll |
| **22** | **V** | Beq = (1/A₀²)·∫\|A(f)\|² df; la potència de soroll a la sortida és proporcional a \|A(f)\|². | 3. Amplada de banda equivalent de soroll |
| **23** | **F** | En sistemes reals Beq és més gran que f−3dB per la contribució de la banda de transició. | 3. Amplada de banda equivalent de soroll |
| **24** | **V** | La integral de 1/(1+x²) dona π/2; el filtre deixa passar un 57 % més de potència que un rectangular ideal. | 3. Amplada de banda equivalent de soroll |
| **25** | **F** | En deixa passar més (un 57 % més) per la cua que decreix lentament a −20 dB/dècada. | 3. Amplada de banda equivalent de soroll |
| **26** | **V** | La caiguda més ràpida (−40 dB/dècada) redueix Beq respecte al primer ordre. | 3. Amplada de banda equivalent de soroll |
| **27** | **V** | Com més abrupta és la transició, més s'aproxima la resposta a la del filtre ideal. | 3. Amplada de banda equivalent de soroll |
| **28** | **F** | Un filtre de primer ordre cau a −20 dB/dècada; el de segon ordre a −40 dB/dècada. | 3. Amplada de banda equivalent de soroll |
| **29** | **V** | S'aproxima per la del passabaixes de freqüència de tall igual a la superior. | 3. Amplada de banda equivalent de soroll |
| **30** | **F** | És la diferència entre la freqüència superior i la inferior de pas, no la suma. | 3. Amplada de banda equivalent de soroll |
| **31** | **V** | Està associat al pas discret de càrrega (estadística de Poisson) a través de la barrera. | 4. Soroll shot i soroll 1/f |
| **32** | **F** | Sense corrent continu apreciable, el soroll shot associat a la unió és negligible. | 4. Soroll shot i soroll 1/f |
| **33** | **V** | És un soroll blanc amb densitat proporcional al corrent continu que travessa la unió. | 4. Soroll shot i soroll 1/f |
| **34** | **V** | El corrent continu es modela amb la branca ideal i el soroll shot com una font de corrent en paral·lel. | 4. Soroll shot i soroll 1/f |
| **35** | **F** | El corrent fotoinduït és un corrent continu que travessa una unió i, per tant, presenta soroll shot. | 4. Soroll shot i soroll 1/f |
| **36** | **V** | Es modela com Sv(f)=K/f^α amb α proper a 1; per això no és blanc. | 4. Soroll shot i soroll 1/f |
| **37** | **F** | La seva densitat depèn de la freqüència (∝1/f); per definició, doncs, no és blanc. | 4. Soroll shot i soroll 1/f |
| **38** | **V** | En créixer cap a baixes freqüències, és especialment rellevant en mesures lentes. | 4. Soroll shot i soroll 1/f |
| **39** | **V** | La integral de K/f dona una dependència logarítmica del quocient de freqüències. | 4. Soroll shot i soroll 1/f |
| **40** | **F** | Divergeix logarítmicament quan fmin→0; a la pràctica fmin el fixa el temps d'observació o un filtre passaaltes. | 4. Soroll shot i soroll 1/f |
| **41** | **V** | El dispositiu es tracta com un quadripol ideal sense soroll amb les fonts referides a l'entrada. | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **42** | **F** | La densitat de tensió s'expressa en V/√Hz (sovint nV/√Hz); l'A/√Hz és per a la densitat de corrent. | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **43** | **V** | Per a fonts independents de mitjana nul·la, la variància total és la suma de variàncies. | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **44** | **F** | Es combinen per suma quadràtica (pitagòrica), no aritmètica. | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **45** | **F** | Amb impedàncies de font altes, el soroll de corrent (convertit en tensió) pot esdevenir la contribució dominant. | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **46** | **V** | El guany de soroll (1+R2/R1) no coincideix amb el valor absolut del guany de senyal inversor (R2/R1). | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **47** | **F** | Sí que genera soroll tèrmic, que contribueix directament a la sortida. | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **48** | **V** | En limitar la banda es redueix el soroll blanc integrat, que creix amb √Beq. | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **49** | **F** | És crítica: el seu soroll queda referit directament a l'entrada, mentre que el de les posteriors es divideix pel guan... | 5. Dispositius actius, amplificadors i disseny de baix soroll |
| **50** | **F** | Es reserva per a casos molt exigents; primer s'optimitzen resistències, banda, dispositius i arquitectura a temperatu... | 5. Dispositius actius, amplificadors i disseny de baix soroll |

<!-- FIN CAPÍTULO: 07_Entrenament_Tema4 -->

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
| **(4.1)** | $\sigma \approx \sqrt{\frac{1}{N-1}\sum_{i=0}^{N-1} x[i]^2}$ |
| **(4.2)** | $\sigma^2 = \int_{0}^{\infty} P_{\text{xx}}(f)\, df$ |
| **(4.3)** | $\sigma = \sqrt{\int_{0}^{\infty} P_{\text{xx}}(f)\, df}$ |
| **(4.4)** | $\sigma_V = \sqrt{\int_{f_{\min}}^{f_{\max}} e_n^2(f)\, df}, \qquad \sigma_I = \sqrt{\int_{f_{\min}}^{f_{\max}} i_n^2(f)\, df}$ |
| **(4.5)** | $V_t = \sqrt{4kTBR}$ |
| **(4.6)** | $I_t = \sqrt{\frac{4kTB}{R}}$ |
| **(4.7)** | $P_t = V_t \cdot I_t = \sqrt{4kTBR}\,\sqrt{\frac{4kTB}{R}} = 4kTB$ |
| **(4.8)** | $P_{\text{xx}}(f) = 4kTR \quad [\mathrm{V^2/Hz}]$ |
| **(4.9)** | $\sigma_V^2 = \int_{f_{\min}}^{f_{\max}} P_{\text{xx}}(f)\, df = 4kTR\,(f_{\max}-f_{\min}) = 4kTRB$ |
| **(4.10)** | $P_{\text{ii}}(f) = \frac{4kT}{R} \quad [\mathrm{A^2/Hz}]$ |
| **(4.11)** | $e_n(f) = \sqrt{4kTR} \quad [\mathrm{V/\sqrt{Hz}}]$ |
| **(4.12)** | $i_n(f) = \sqrt{\frac{4kT}{R}} \quad [\mathrm{A/\sqrt{Hz}}]$ |
| **(4.13)** | $V_t = e_n\sqrt{B} = \sqrt{4kTR}\,\sqrt{B} = \sqrt{4kTRB}$ |
| **(4.14)** | $P_{\text{xx}}(f) = 4kT\,R(f) \quad [\mathrm{V^2/Hz}]$ |
| **(4.15)** | $\|A(f)\| = A_0 \;\;(0\leq f\leq f_c); \qquad \|A(f)\| = 0 \;\;(f>f_c)$ |
| **(4.16)** | $\|A(f)\| = A_0 \;\;(f_{c,\min}\leq f\leq f_{c,\max}); \qquad \|A(f)\| = 0 \;\;\mathrm{(altrament)}$ |
| **(4.17)** | $B_{\text{eq}} = \frac{1}{A_0^2}\int_{0}^{\infty} \|A(f)\|^2\, df$ |
| **(4.18)** | $A_0^2\cdot B_{\text{eq}} = \int_{0}^{\infty} \|A(f)\|^2\, df$ |
| **(4.19)** | $V_{n,out}^2 = \int_{0}^{\infty} S_n\,\|A(f)\|^2\, df = S_n\,A_0^2\,B_{\text{eq}}$ |
| **(4.20)** | $V_{n,out,\,ideal}^2 = S_n\,A_0^2\,B_{\text{eq}}$ |
| **(4.21)** | $V_{n,out} = A_0\sqrt{4kTR\,B_{\text{eq}}}$ |
| **(4.22)** | $V_{n,in} = \sqrt{4kTR\,B_{\text{eq}}}$ |
| **(4.23)** | $A(f) = \frac{A_0}{1+j\,f/f_0}$ |
| **(4.24)** | $\|A(f)\|^2 = \frac{A_0^2}{1+(f/f_0)^2}$ |
| **(4.25)** | $B_{\text{eq}} = \frac{1}{A_0^2}\int_{0}^{\infty}\frac{A_0^2}{1+(f/f_0)^2}\,df = f_0\int_{0}^{\infty}\frac{dx}{1+x^2} = f_0\cdot\frac{\pi}{2}$ |
| **(4.26)** | $B_{\text{eq}} = \frac{\pi}{2}\,f_{-3\,\mathrm{dB}} \approx 1{,}57\,f_{-3\,\mathrm{dB}}$ |
| **(4.27)** | $B_{\text{eq}} = 1{,}11\,f_{-3\,\mathrm{dB}}$ |
| **(4.28)** | $S_i(f) = 2\,q\,I_{\text{dc}} \quad [\mathrm{A^2/Hz}]$ |
| **(4.29)** | $i_{n,rms}^2 = \int_{f_{\min}}^{f_{\max}} S_i(f)\,df \approx \int_{0}^{B} 2qI_{\text{dc}}\,df = 2qI_{\text{dc}}B$ |
| **(4.30)** | $i_{n,rms} = \sqrt{2qI_{\text{dc}}B}$ |
| **(4.31)** | $S_v(f) = \frac{K}{f^{\alpha}} \quad \mathrm{amb } \alpha\approx 1$ |
| **(4.32)** | $v_{n,rms}^2 = \int_{f_{\min}}^{f_{\max}} \frac{K}{f}\,df = K\,\ln\!\left(\frac{f_{\max}}{f_{\min}}\right)$ |
| **(4.33)** | $v_{n,rms} = \sqrt{K\,\ln\!\left(\frac{f_{\max}}{f_{\min}}\right)}$ |
| **(4.34)** | $v_{n,total} = \sqrt{v_{n,1}^2 + v_{n,2}^2 + \dots + v_{n,N}^2}$ |
| **(4.35)** | $e_{n,tot}^2 \approx e_{n1}^2 + \left(\frac{e_{n2}}{G_1}\right)^2 + \dots$ |