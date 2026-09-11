# 📚 Cuaderno Maestro: Tema 2

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 2` | 📄 **Capítulos incluidos:** 10  
> 📅 **Generado:** 2026-09-11 19:09

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 2 — Estimació de la incertesa a la mesura](#unitat-2-estimació-de-la-incertesa-a-la-mesura)
   - [Dedicació estimada](#dedicació-estimada)
2. [U2·01 Concepte d'incertesa, la GUM i la diferència entre error i incertesa](#u201-concepte-dincertesa-la-gum-i-la-diferència-entre-error-i-incertesa)
   - [1 La definició d'incertesa segons la GUM](#1-la-definició-dincertesa-segons-la-gum)
   - [2 Origen normatiu: per què calia estandarditzar el dubte](#2-origen-normatiu-per-què-calia-estandarditzar-el-dubte)
   - [3 Error i incertesa: dos conceptes que no s'han de confondre](#3-error-i-incertesa-dos-conceptes-que-no-shan-de-confondre)
   - [4 Per a què serveix calcular la incertesa](#4-per-a-què-serveix-calcular-la-incertesa)
3. [U2·02 Marc teòric i definicions fonamentals](#u202-marc-teòric-i-definicions-fonamentals)
   - [1 El resultat de mesura com a variable aleatòria](#1-el-resultat-de-mesura-com-a-variable-aleatòria)
   - [2 Valor veritable, estimació i interval de confiança](#2-valor-veritable-estimació-i-interval-de-confiança)
   - [3 Paràmetres estadístics fonamentals](#3-paràmetres-estadístics-fonamentals)
   - [4 Incertesa típica, incertesa expandida i factor de cobertura](#4-incertesa-típica-incertesa-expandida-i-factor-de-cobertura)
4. [U2·03 El model matemàtic de la mesura](#u203-el-model-matemàtic-de-la-mesura)
   - [1 La funció de mesura](#1-la-funció-de-mesura)
   - [2 El model ha de ser complet](#2-el-model-ha-de-ser-complet)
   - [3 Mesures directes i indirectes](#3-mesures-directes-i-indirectes)
   - [4 Tipus A i tipus B: una classificació pel mètode](#4-tipus-a-i-tipus-b-una-classificació-pel-mètode)
   - [5 Hipòtesis del model](#5-hipòtesis-del-model)
5. [U2·04 Avaluació de la incertesa de tipus A](#u204-avaluació-de-la-incertesa-de-tipus-a)
   - [1 Requisits per aplicar l'avaluació de tipus A](#1-requisits-per-aplicar-lavaluació-de-tipus-a)
   - [2 Neteja de dades: valors aberrants](#2-neteja-de-dades-valors-aberrants)
   - [3 Estimació del mesurand i dispersions](#3-estimació-del-mesurand-i-dispersions)
   - [4 La incertesa típica de tipus A](#4-la-incertesa-típica-de-tipus-a)
   - [5 La llei de l'arrel de N i els seus límits](#5-la-llei-de-larrel-de-n-i-els-seus-límits)
6. [U2·05 Avaluació de la incertesa de tipus B](#u205-avaluació-de-la-incertesa-de-tipus-b)
   - [1 Fonts d'informació](#1-fonts-dinformació)
   - [2 Com escollir la distribució: màxima entropia](#2-com-escollir-la-distribució-màxima-entropia)
   - [3 Les quatre distribucions](#3-les-quatre-distribucions)
   - [4 Comparació per a un mateix semi-interval](#4-comparació-per-a-un-mateix-semi-interval)
7. [U2·06 Combinació d'incerteses en mesures indirectes](#u206-combinació-dincerteses-en-mesures-indirectes)
   - [1 Linealització del model](#1-linealització-del-model)
   - [2 Coeficients de sensibilitat](#2-coeficients-de-sensibilitat)
   - [3 La incertesa típica combinada](#3-la-incertesa-típica-combinada)
   - [4 Variables correlacionades: termes de covariància](#4-variables-correlacionades-termes-de-covariància)
   - [5 Quan la linealització no és fiable: Monte Carlo](#5-quan-la-linealització-no-és-fiable-monte-carlo)
8. [U2·07 Incertesa expandida, factor de cobertura i graus de llibertat](#u207-incertesa-expandida-factor-de-cobertura-i-graus-de-llibertat)
   - [1 Definició i expressió del resultat](#1-definició-i-expressió-del-resultat)
   - [2 El factor de cobertura en el cas normal](#2-el-factor-de-cobertura-en-el-cas-normal)
   - [3 Poques dades: la distribució t de Student](#3-poques-dades-la-distribució-t-de-student)
   - [4 Graus de llibertat efectius: Welch-Satterthwaite](#4-graus-de-llibertat-efectius-welch-satterthwaite)
9. [U2·08 Expressió final del resultat i balanç d'incertesa](#u208-expressió-final-del-resultat-i-balanç-dincertesa)
   - [1 El balanç d'incertesa](#1-el-balanç-dincertesa)
   - [2 Anàlisi de dominància](#2-anàlisi-de-dominància)
   - [3 Regles de format del resultat final](#3-regles-de-format-del-resultat-final)
10. [SM · Unitat 2 · Entrenament](#sm-unitat-2-entrenament)
   - [Tria com vols entrenar](#tria-com-vols-entrenar)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 2_00_index -->

# Unitat 2 — Estimació de la incertesa a la mesura

> [!NOTE] **Com treballar aquesta unitat**
>
> Aquests documents substitueixen els apunts per a la lectura prèvia de la Unitat 2. Segueixen la metodologia d'**aula inversa**: cal llegir-los **abans** de la sessió presencial, on es resoldran activitats que en pressuposen el contingut.
>
> **Abans de la primera sessió** d'aquesta unitat cal haver llegit els materials i resoldre el qüestionari corresponent disponible a Atenea.

La Unitat 2 desenvolupa l'estimació de la incertesa a la mesura seguint la *Guide to the Expression of Uncertainty in Measurement* (GUM): des del concepte d'incertesa i el model de mesura fins a l'avaluació de tipus A i B, la combinació d'incerteses, la incertesa expandida i l'expressió final del resultat, amb dos exemples resolts pas a pas.

### [1. Concepte d'incertesa, GUM i error vs. incertesa](#u201-concepte-dincertesa-la-gum-i-la-diferència-entre-error-i-incertesa)

Definició d'incertesa de la GUM, origen normatiu i distinció rigorosa entre error i incertesa.

### [2. Marc teòric i definicions fonamentals](#u202-marc-teòric-i-definicions-fonamentals)

El resultat com a variable aleatòria; valor veritable i estimació; incertesa típica, expandida i factor de cobertura.

### [3. El model matemàtic de la mesura](#u203-el-model-matemàtic-de-la-mesura)

El model Y=f(X); mesures directes i indirectes; avaluacions tipus A i B; hipòtesis i mètode de Monte Carlo.

### [4. Avaluació de la incertesa de tipus A](#u204-avaluació-de-la-incertesa-de-tipus-a)

Repetibilitat, independència i biaix; valors aberrants; la mitjana i uA = s/√N, amb la seva deducció.

### [5. Avaluació de la incertesa de tipus B](#u205-avaluació-de-la-incertesa-de-tipus-b)

Fonts d'informació, principi de màxima entropia i les distribucions uniforme, triangular, normal i en U.

### [6. Combinació d'incerteses en mesures indirectes](#u206-combinació-dincerteses-en-mesures-indirectes)

Llei de propagació, coeficients de sensibilitat, suma en quadratura, covariància i Monte Carlo.

### [7. Incertesa expandida i graus de llibertat](#u207-incertesa-expandida-factor-de-cobertura-i-graus-de-llibertat)

Factor de cobertura, distribució t de Student i graus de llibertat efectius (Welch-Satterthwaite).

### [8. Expressió final del resultat i balanç d'incertesa](#u208-expressió-final-del-resultat-i-balanç-dincertesa)

Construcció del balanç, anàlisi de dominància i regles d'arrodoniment del resultat.

## Dedicació estimada

| # | Document | Minuts |
|:--- |:--- | ---: |
| 1 | Concepte d'incertesa, GUM i error vs. incertesa | 8 |
| 2 | Marc teòric i definicions fonamentals | 7 |
| 3 | El model matemàtic de la mesura | 6 |
| 4 | Avaluació de la incertesa de tipus A | 6 |
| 5 | Avaluació de la incertesa de tipus B | 7 |
| 6 | Combinació d'incerteses en mesures indirectes | 7 |
| 7 | Incertesa expandida i graus de llibertat | 5 |
| 8 | Expressió final del resultat i balanç d'incertesa | 4 |
| Total |  | 50 min |

Sistemes de Mesura (230920) · ETSETB–UPC

<!-- FIN CAPÍTULO: 2_00_index -->

---

<!-- INICIO CAPÍTULO: 2_01_introduccio -->

# U2·01 Concepte d'incertesa, la GUM i la diferència entre error i incertesa

> [!NOTE] **Objectius d'aprenentatge**
>
> - Enunciar la definició d'incertesa de mesura de la GUM i interpretar-ne les tres implicacions (és un nombre, quantifica dispersió, és atribuïble al mesurand).
> - Distingir amb precisió els conceptes d'**error** i d'**incertesa**, i justificar per què el valor veritable d'un mesurand és, en sentit estricte, incognoscible.
> - Situar l'origen normatiu de la GUM i reconèixer per què l'expressió de la incertesa és avui un requisit de traçabilitat metrològica.
> - Identificar les dues finalitats pràctiques del càlcul de la incertesa: la interpretació inequívoca del resultat i el diagnòstic del sistema de mesura.

Quan un enginyer declara que una resistència val 47,3 kΩ, o que la temperatura d'un procés industrial és de 85,2 °C, comunica quelcom més que un nombre: afirma tenir coneixement sobre una propietat física del món real. Tanmateix, aquest coneixement mai no pot ser absolut. El valor *veritable* de la resistència o de la temperatura roman, en sentit estricte, desconegut i incognoscible. El que realment posseïm és una **estimació** d'aquest valor, acompanyada d'un dubte quantificable sobre la seva bondat.

Durant dècades, diferents comunitats científiques i industrials van expressar aquest dubte de maneres diverses —marges d'error, intervals de confiança, desviacions estàndard, toleràncies, exactituds relatives—, cosa que va generar confusió, especialment quan laboratoris de països diferents havien d'intercanviar resultats o validar mesures crítiques per a la seguretat, el comerç o la recerca. Calia un llenguatge comú per descriure la qualitat de les mesures.

## 1 La definició d'incertesa segons la GUM

La resposta a aquesta necessitat va arribar amb la formalització del concepte d'**incertesa en la mesura**, recollida per la *International Organization for Standardization* (ISO) el 1995 a la *Guide to the Expression of Uncertainty in Measurement* (GUM), que estableix:

> [!NOTE] **Definició (GUM)**
>
> La incertesa en la mesura és un nombre que quantifica la dispersió de valors que és atribuïble al mesurand.

La definició és compacta però rica en implicacions. Convé desglossar-la:

- **És un nombre.** La incertesa no és una impressió qualitativa («aquesta mesura sembla bona»), sinó una magnitud quantitativa, expressada en les mateixes unitats que el mesurand i calculada mitjançant procediments matemàtics ben definits.
- **Quantifica la dispersió de valors.** Si repetíssim la mesura en condicions ideals, obtindríem una distribució de resultats possibles. La incertesa en descriu l'amplitud: com més petita és la incertesa, més estreta és la funció de densitat de probabilitat dels resultats possibles i millor és l'estimació.
- **És atribuïble al mesurand.** L'objectiu últim és caracteritzar el dubte sobre el valor veritable de la magnitud que es mesura, no sobre la lectura de l'instrument, que és només un mitjà.

La incertesa és, doncs, l'indicador fonamental de la qualitat d'un resultat metrològic. Una mesura sense incertesa associada és, en la pràctica professional moderna, difícilment interpretable: sense saber fins a quin punt es pot confiar en el valor declarat, el resultat no és útil per prendre decisions tècniques, comercials o científiques.

## 2 Origen normatiu: per què calia estandarditzar el dubte

La incertesa es va formalitzar amb la publicació de la GUM (1993), fruit d'un consorci internacional d'organismes de metrologia, normalització i ciència, i adoptada per la ISO el 1995 com a estàndard. Avui la conformitat amb la GUM és un requisit explícit de normes com la ISO 9001 (gestió de la qualitat) i la ISO/IEC 17025 (competència de laboratoris d'assaig i calibratge), i de regulacions sectorials (dispositius mèdics, aeronàutica, energia nuclear, metrologia legal): sense una expressió adequada de la incertesa no hi ha traçabilitat metrològica reconeguda internacionalment.

Convé remarcar que la GUM no substitueix el Sistema Internacional d'Unitats, sinó que n'estandarditza l'expressió del dubte, i que s'aplica a qualsevol domini de mesura —també l'elèctric i l'electrònic—, no només a les mesures mecàniques.

## 3 Error i incertesa: dos conceptes que no s'han de confondre

Un dels malentesos més persistents, fins i tot entre enginyers amb experiència, és la confusió entre **error** i **incertesa**. La GUM hi dedica un esforç considerable perquè la distinció és conceptualment crucial. L'error de mesura es defineix formalment com la diferència entre el resultat de la mesura i el valor veritable del mesurand:

$$
\mathrm{error} \;=\; x_{\mathrm{mesurat}} \;-\; x_{\mathrm{veritable}} \qquad (2.1)
$$

El problema rau en el segon terme: el valor veritable no es pot conèixer mai exactament. Si es pogués conèixer, no caldria fer cap mesura. Per definició, el valor veritable és allò que obtindríem amb un instrument perfecte —resolució infinita, soroll nul, sensibilitat i linealitat perfectes, cap efecte de càrrega, immunitat total a interferències, resposta instantània—, i aquest instrument ideal no existeix. Per tant, **l'error és una quantitat desconeguda i, en principi, incognoscible**. En el millor dels casos, si disposem d'un patró de referència de qualitat superior, podem *estimar* l'error, però aquesta estimació arrossega la incertesa pròpia del patró.

La incertesa, per contra, no és l'error, sinó una caracterització de la nostra ignorància sobre el valor veritable. És un paràmetre positiu (típicament una desviació estàndard) que descriu un interval al voltant del resultat declarat; aquest interval conté el valor veritable amb una probabilitat coneguda (el nivell de confiança). I, a diferència de l'error, la incertesa **sí** que es pot calcular: mitjançant procediments estadístics (avaluació de tipus A) o mitjançant el judici científic informat per especificacions i lleis físiques (avaluació de tipus B), tots dos tractats en documents posteriors d'aquesta unitat.

> [!NOTE] **Il·lustració: la bàscula**
>
> Si pesem un patró certificat de 10,000 kg i la bàscula marca 10,580 kg, **l'error és +0,580 kg**: ara el coneixem, perquè disposem del patró.
>
> Si tot seguit pesem un objecte desconegut i obtenim 15,234 kg, ja **no** podem calcular l'error (no sabem el pes veritable). Però sí que podem estimar la **incertesa**: a partir de la caracterització prèvia de la bàscula (resolució, repetibilitat, biaixos) i d'altres factors com la temperatura, podem declarar, per exemple, 15,234 kg ± 0,12 kg amb un nivell de confiança del 95 %.

La metodologia GUM ens ensenya, doncs, a abandonar l'error com a objectiu de càlcul directe —perquè no és factible— i a centrar-nos en l'estimació rigorosa de la incertesa, que és el que realment podem oferir a l'usuari de la mesura. Aquest plantejament connecta amb el que s'ha vist a la **Unitat 1**: un sistema de mesura pot tenir error sistemàtic (biaix) i soroll aleatori; un bon procés metrològic corregeix el biaix i caracteritza el soroll. Les fonts concretes d'aquest dubte s'estudiaran amb detall en les unitats d'**interferències** (Unitat 3) i de **soroll** (Unitat 4).

## 4 Per a què serveix calcular la incertesa

L'esforç de calcular i documentar la incertesa no és un exercici acadèmic. Té dues finalitats pràctiques fonamentals.

La **primera** és la **interpretació inequívoca del resultat**. Quan un laboratori certifica que un termòmetre indica «25,00 °C amb una incertesa expandida de ±0,05 °C (k = 2, nivell de confiança del 95 %)», qualsevol enginyer familiaritzat amb la terminologia GUM entén immediatament que la millor estimació és 25,00 °C, que hi ha un 95 % de probabilitat que el valor veritable estigui entre 24,95 °C i 25,05 °C, i que el factor k = 2 assumeix una distribució aproximadament normal. Aquesta claredat és essencial per comparar resultats de laboratoris o instruments diferents, prendre decisions de conformitat respecte d'especificacions tècniques o legals, establir traçabilitat metrològica i evitar disputes comercials quan comprador i venedor obtenen resultats lleugerament diferents.

La **segona** finalitat, sovint menys evident, és l'**anàlisi de la cadena metrològica per millorar el sistema de mesura**. Calcular la incertesa obliga a identificar totes les fonts de dubte (resolució, deriva tèrmica, soroll electrònic, efecte de càrrega, incertesa dels patrons, variabilitat del mesurand) i a quantificar-ne la contribució. Mitjançant un **balanç d'incertesa** —una taula que llista les fonts, les incerteses individuals i les seves contribucions ponderades— el dissenyador veu d'un cop d'ull quins factors dominen. Així, l'estimació de la incertesa esdevé una eina de diagnòstic i d'optimització: es focalitzen els recursos on realment importen i no es malgasten en millores irrellevants. Aquest balanç es construeix al document sobre l'expressió final del resultat.

> [!TIP] **Síntesi**
>
> El valor veritable d'un mesurand és incognoscible; per això tota mesura és una estimació acompanyada d'un dubte quantificat. La GUM defineix la incertesa com un nombre, expressat en les unitats del mesurand, que quantifica la dispersió de valors atribuïble al mesurand, i la distingeix nítidament de l'error (que requeriria conèixer el valor veritable). Nascuda d'un consorci metrològic internacional i adoptada per la ISO el 1995, la GUM és avui un requisit de traçabilitat. Calcular la incertesa serveix, alhora, per interpretar el resultat sense ambigüitats i per diagnosticar i millorar el sistema de mesura.

[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)[2. Marc teòric i definicions fonamentals →](#u202-marc-teòric-i-definicions-fonamentals)

---

<!-- FIN CAPÍTULO: 2_01_introduccio -->

---

<!-- INICIO CAPÍTULO: 2_02_marc_teoric -->

# U2·02 Marc teòric i definicions fonamentals

> [!NOTE] **Objectius d'aprenentatge**
>
> - Justificar per què, en metrologia moderna, el resultat d'una mesura s'interpreta com una **variable aleatòria** i identificar-ne les fonts de variabilitat.
> - Distingir la millor estimació del mesurand ( $y$ ) del valor veritable incognoscible ( $q$ ).
> - Diferenciar la **dispersió de les lectures** ( $s$ ) de la **dispersió de la mitjana** ( $s/\sqrt{N}$ ).
> - Definir amb precisió la incertesa típica, la incertesa expandida, el factor de cobertura i l'interval de confiança.

## 1 El resultat de mesura com a variable aleatòria

Un dels canvis conceptuals més importants de la instrumentació moderna és acceptar que el resultat d'una mesura no és un valor determinista, sinó la manifestació d'un procés subjecte a variabilitat. Dit d'una altra manera: el resultat d'una mesura s'ha d'entendre com una **variable aleatòria**.

Això no és un recurs retòric, sinó una conseqüència directa del funcionament físic dels instruments. En qualsevol mesura hi intervenen múltiples fonts de variació: soroll aleatori als circuits electrònics (per exemple, soroll tèrmic), quantització en els sistemes digitals (passos finits de l'ADC i de la visualització), interferències externes (camps electromagnètics, acoblaments), variacions ambientals (temperatura, humitat, vibració) i variabilitat del procediment (operador, connexions, contacte mecànic). Així, encara que el mesurand fos perfectament constant, repetir la mesura moltes vegades produiria una *distribució* de resultats: un núvol de valors al voltant d'un centre, amb una dispersió que depèn de la qualitat del sistema i de les condicions.

La GUM formalitza aquesta visió assumint que qualsevol resultat de mesura és una realització d'una variable aleatòria associada al procés. Convé no confondre *variabilitat estadística* amb *manca de rigor*: al contrari, el rigor metrològic consisteix precisament a modelar la variabilitat, estimar-ne la magnitud i documentar-la.

## 2 Valor veritable, estimació i interval de confiança

Denotem el valor veritable del mesurand com  $q$. Aquest valor és el que obtindria un sistema de mesura perfecte, i la idea central és que  **$q$  no es pot conèixer exactament**: si es conegués, la mesura seria innecessària; i fins i tot els patrons primaris tenen incertesa, de manera que només permeten aproximar  $q$, mai revelar-lo. Per això el treball metrològic no consisteix a «trobar  $q$ », sinó a produir una **estimació** del mesurand —que denotem  $y$ — i associar-li un interval amb una probabilitat explícita que contingui  $q$.

![Il·lustració del concepte d'incertesa: la millor estimació y del mesurand i l'interval que conté el valor veritable q amb una probabilitat determinada](assets/2_02_marc_teoric_img_1.png)

*Figura: Figura 2.1. Il·lustració del concepte d'incertesa a la mesura. A partir del coneixement del procediment, la GUM permet estimar un interval al voltant de $y$ que conté el valor veritable $q$ amb una probabilitat determinada.*

En termes pràctics,  $y$  pot ser una lectura directa d'un instrument (mesura directa) o el resultat d'una funció que combina diverses lectures i paràmetres (mesura indirecta), mitjançant un model de mesura  $Y=f(X_1,X_2,\dots)$  que s'estudia al document següent. En tots dos casos,  $y$  és la millor estimació disponible sota la informació i les condicions existents: si es fan  $N$  observacions repetides sense biaix, el millor estimador habitual és la mitjana aritmètica; si es fa una mesura única amb informació del fabricant o de calibratge,  $y$  continua essent la millor estimació, però la incertesa s'infereix per altres vies (avaluació de tipus B). Aquest plantejament és coherent amb la **Unitat 1**: un sistema pot tenir error sistemàtic (biaix) i soroll aleatori, i un bon procés corregeix el biaix i caracteritza el soroll.

## 3 Paràmetres estadístics fonamentals

Un cop acceptat que el resultat s'ha d'interpretar probabilísticament, cal quantificar la dispersió dels resultats possibles. Suposem  $N$  observacions repetides del mateix mesurand, en condicions comparables,  $x_1,\dots,x_N$. La **mitjana aritmètica** és:

$$
\bar{x}=\frac{1}{N}\sum_{i=1}^{N} x_i \qquad (2.2)
$$

Quan la distribució és simètrica i no hi ha biaix,  $\bar{x}$  és un estimador natural del valor del mesurand. La **variància mostral** (amb l'estimador no esbiaixat, que utilitza  $N-1$  al denominador) és:

$$
s^2=\frac{1}{N-1}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2 \qquad (2.3)
$$

i la **desviació estàndard mostral**:

$$
s=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2} \qquad (2.4)
$$

Aquests dos paràmetres descriuen la dispersió de les observacions *individuals* al voltant de la mitjana. Ara bé, en metrologia sovint el resultat que es reporta no és una observació individual, sinó la mitjana  $\bar{x}$. El dubte rellevant és aleshores: quant variaria  $\bar{x}$  si repetíssim l'experiment complet amb un altre conjunt de  $N$  mesures? Sota la hipòtesi d'observacions independents, la **desviació estàndard de la mitjana** és:

$$
s_{\bar{x}}=\frac{s}{\sqrt{N}} \qquad (2.5)
$$

A diferència de  $s$, aquesta dispersió **es redueix** en augmentar  $N$. El resultat es fonamenta en una propietat clau —la variància de la suma de variables aleatòries independents és la suma de les variàncies—, que és precisament el que fa tan útil expressar la incertesa com una desviació estàndard, perquè després permet combinar incerteses. L'expressió (2.5) és la base de l'avaluació de la incertesa de tipus A, que es tracta al document corresponent.

## 4 Incertesa típica, incertesa expandida i factor de cobertura

La GUM defineix la **incertesa típica** (o estàndard) com la desviació estàndard dels possibles resultats de mesura. Si el resultat es modela com una variable aleatòria  $Y$, la incertesa típica és:

$$
u(y)=\sigma[Y] \qquad (2.6)
$$

En la pràctica,  $\sigma[Y]$  no és coneguda i s'estima. El primer pas de qualsevol avaluació és, doncs, estimar la desviació estàndard associada al resultat: aquest valor és la incertesa típica, i s'expressa sempre en les mateixes unitats que el mesurand (mai com un simple percentatge).

La incertesa típica té un significat estadístic clar, però per a moltes decisions d'enginyeria es prefereixen intervals amb probabilitats més elevades que el 68 % aproximat associat a una desviació estàndard en el cas normal. Per això es defineix la **incertesa expandida**  $U$  com el producte de la incertesa típica combinada per un **factor de cobertura**  $k$:

$$
U=k\,u_c(y) \qquad (2.7)
$$

i l'interval de confiança que en resulta,

$$
y-U \;\leq\; q \;\leq\; y+U \qquad (2.8)
$$

conté el valor veritable  $q$  amb una probabilitat preestablerta anomenada **nivell de confiança**. Com més gran és el nivell de confiança, més ample ha de ser l'interval i, per tant, més gran ha de ser  $k$. No existeix, doncs, una «incertesa única» independent del context: el mateix resultat es pot comunicar amb diferents  $k$  segons si interessa un 90 %, un 95 % o un 99 % de confiança. El factor  $k$  és el multiplicador que connecta la incertesa típica amb un interval d'un determinat nivell, i el seu valor depèn de la distribució de probabilitat assumida; la seva determinació s'aborda al document sobre la incertesa expandida.

> [!TIP] **Síntesi**
>
> El resultat de mesura s'interpreta com una variable aleatòria: encara amb un mesurand constant, múltiples fonts (soroll, quantització, interferències, ambient, procediment) en dispersen les lectures. El valor veritable  $q$  és incognoscible; el treball metrològic produeix una estimació  $y$  i un interval que conté  $q$  amb una probabilitat coneguda. Cal distingir la dispersió de les lectures  $s$  de la dispersió de la mitjana  $s/\sqrt{N}$, que sí que decreix amb  $N$. La incertesa típica és una desviació estàndard; multiplicada per un factor de cobertura  $k$  dona la incertesa expandida  $U$, que defineix l'interval  $y\pm U$  amb el nivell de confiança desitjat.

[← 1. Concepte d'incertesa, la GUM i la diferència entre error i incertesa](#u201-concepte-dincertesa-la-gum-i-la-diferència-entre-error-i-incertesa)[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)[3. El model matemàtic de la mesura →](#u203-el-model-matemàtic-de-la-mesura)

---

<!-- FIN CAPÍTULO: 2_02_marc_teoric -->

---

<!-- INICIO CAPÍTULO: 2_03_model_matematic -->

# U2·03 El model matemàtic de la mesura

> [!NOTE] **Objectius d'aprenentatge**
>
> - Escriure el model de mesura  $Y=f(X_1,\dots,X_N)$  i identificar-ne les magnituds d'entrada i la funció.
> - Reconèixer la necessitat d'un model **complet**, que inclogui les correccions sistemàtiques rellevants.
> - Distingir mesures directes i indirectes, i les avaluacions de tipus A i tipus B segons el mètode.
> - Enunciar les hipòtesis habituals: independència, linealitat local i estacionarietat.

L'estimació de la incertesa s'ha de fonamentar en una descripció matemàtica precisa de com s'obté el resultat: el **model de mesura**. Sense un model clar no podem saber quines variables afecten el resultat, ni com es propaguen els seus dubtes, ni quina importància relativa tenen. Per això el primer pas de qualsevol anàlisi d'incertesa, segons la GUM, no és calcular estadístiques, sinó **escriure una equació**.

## 1 La funció de mesura

El nucli del model és una funció que relaciona el mesurand amb totes les magnituds de les quals depèn el seu valor. Formalment, el mesurand  $Y$  no es mesura directament, sinó que es determina a partir de  $N$  quantitats d'entrada a través d'una relació funcional  $f$:

$$
Y=f(X_1,X_2,\dots,X_N) \qquad (2.9)
$$

Aquesta expressió, aparentment simple, conté tota la física del sistema de mesura:

- **$Y$  (mesurand):** la quantitat que volem determinar. No és necessàriament el que «llegim» a la pantalla. Si volem la potència dissipada en una resistència però mesurem la tensió i el corrent, aleshores  $Y$  és la potència.
- **$X_i$  (magnituds d'entrada o factors d'influència):** totes les variables que intervenen en la determinació de  $Y$. Inclouen les lectures directes dels instruments, valors de constants físiques, correccions per efectes sistemàtics (calibratge, temperatura) i factors ambientals que modifiquen la resposta encara que no els mesurem expressament.
- **$f$  (la funció):** l'algoritme o llei física que combina les entrades per donar la sortida (llei d'Ohm, llei de Hooke, un model empíric o una seqüència de càlculs).

Aquest model és l'eina que permet traslladar el dubte sobre les entrades cap al dubte final sobre la sortida: si coneixem  $f$, podem predir com una petita variació en una  $X_i$  afectarà  $Y$.

## 2 El model ha de ser complet

Les magnituds d'entrada no són només «el que mesurem». Sovint el model teòric ideal s'ha d'ampliar per incloure factors d'influència que en un món ideal no hi serien. Per exemple, si mesurem una longitud  $L$  amb una regla metàl·lica a una temperatura  $T$  diferent de la de calibratge  $T_0$, el model simple és insuficient; el model complet ha d'incloure la dilatació tèrmica:

$$
L=L_m\left[1+\alpha\left(T-T_0\right)\right] \qquad (2.10)
$$

on  $\alpha$  és el coeficient de dilatació tèrmica. Ara la temperatura  $T$  i el coeficient  $\alpha$  s'han convertit en magnituds d'entrada, i les seves incerteses contribuiran a la incertesa total, encara que la correcció esperada sigui petita. Un bon model explicita totes les correccions rellevants fins i tot quan el seu valor esperat és zero (per exemple, assumim que un angle d'alineació és nul, però la incertesa en l'angle afegeix un error de cosinus). Ignorar una magnitud d'influència rellevant condueix a subestimar la incertesa final. A més, una correcció aplicada al resultat porta la seva pròpia incertesa, associada al fet que no coneixem exactament els paràmetres de la correcció.

## 3 Mesures directes i indirectes

Un cop definit el model, l'estratègia d'avaluació depèn de la naturalesa de la mesura:

- **Mesures directes:** el resultat s'obté de la lectura d'un instrument o per comparació directa amb un patró, sense càlculs intermedis. El model és trivialment  $Y=X$  (per exemple, mesurar una tensió amb un multímetre). La incertesa prové exclusivament de les propietats de l'instrument i de la repetibilitat.
- **Mesures indirectes:** el resultat s'obté combinant diverses mesures directes mitjançant un model no trivial (per exemple, la densitat com a massa dividida per volum). La tasca principal és la *combinació d'incerteses*, que requereix la llei de propagació estudiada al document corresponent.

La majoria de mesures en enginyeria són, de fet, indirectes: fins i tot quan semblen directes, sovint hi ha factors de correcció (temperatura, calibratge) que, sota un model rigorós, les converteixen en indirectes.

## 4 Tipus A i tipus B: una classificació pel mètode

La GUM classifica les incerteses no per la naturalesa de l'error, sinó pel **mètode** emprat per avaluar-les:

- **Avaluació de tipus A:** es basa en mètodes estadístics aplicats a una sèrie d'observacions reals i repetides (mitjana, desviació estàndard, desviació estàndard de la mitjana). Requereix fer l'experiment diverses vegades en condicions de repetibilitat i s'associa, en general, a fenòmens aleatoris.
- **Avaluació de tipus B:** es basa en el judici científic i en tota la informació disponible que no prové de la sèrie d'observacions actual (fulls de característiques, certificats de calibratge, manuals, constants de referència, experiència). No es calculen estadístiques *in situ*, sinó que s'assignen distribucions de probabilitat.

És crucial entendre que **ambdós tipus es tracten igual matemàticament** un cop avaluats: tant una incertesa de tipus A com una de tipus B s'expressen com una desviació estàndard, i això permet combinar-les sense problemes. La GUM resol així el vell dubte de com sumar «un error estadístic» amb «una tolerància de fabricant»: es converteix tot a una unitat comuna, la incertesa típica.

## 5 Hipòtesis del model

Perquè el model i la posterior combinació siguin manejables (especialment amb la fórmula simplificada de propagació), sovint s'assumeixen certes hipòtesis, i és responsabilitat de l'enginyer verificar que es compleixen raonablement:

- **Independència** de les variables d'entrada: si dues variables es mesuren amb el mateix instrument esbiaixat, els errors estaran correlacionats i caldrà afegir termes de covariància al càlcul, tal com es veu al document sobre la combinació d'incerteses. En aquest curs assumirem independència llevat que es digui el contrari.
- **Linealitat local** del model: la llei de propagació (basada en sèries de Taylor) assumeix que  $f$  és aproximadament lineal dins del petit interval d'incertesa. Si la funció és molt no lineal, cal recórrer a mètodes numèrics com el mètode de Monte Carlo, que s'introdueix al document sobre la combinació d'incerteses.
- **Estacionarietat**: s'assumeix que les condicions estadístiques no canvien durant la mesura; caracteritzem un estat, no un transitori descontrolat.

> [!TIP] **Síntesi**
>
> Tota anàlisi d'incertesa comença escrivint el model de mesura  $Y=f(X_1,\dots,X_N)$, que ha de ser complet i incloure les correccions sistemàtiques rellevants encara que el seu valor esperat sigui petit. Les mesures poden ser directes o indirectes, i les incerteses es classifiquen en tipus A (estadístiques) o tipus B (per judici i informació prèvia), però totes s'expressen finalment com a desviacions estàndard i es combinen igual. El càlcul es fa sota hipòtesis d'independència, linealitat local i estacionarietat; quan la linealitat falla, s'utilitza el mètode de Monte Carlo.

[← 2. Marc teòric i definicions fonamentals](#u202-marc-teòric-i-definicions-fonamentals)[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)[4. Avaluació de la incertesa de tipus A →](#u204-avaluació-de-la-incertesa-de-tipus-a)

---

<!-- FIN CAPÍTULO: 2_03_model_matematic -->

---

<!-- INICIO CAPÍTULO: 2_04_tipus_A -->

# U2·04 Avaluació de la incertesa de tipus A

> [!NOTE] **Objectius d'aprenentatge**
>
> - Enunciar els tres requisits per aplicar l'avaluació de tipus A: repetibilitat, independència estadística i absència de biaix.
> - Reconèixer l'efecte dels valors aberrants i la necessitat de netejar les dades.
> - Calcular la incertesa típica de tipus A com  $u_A=s/\sqrt{N}$  i distingir la dispersió de les lectures de la dispersió de la mitjana.
> - Deduir l'expressió  $u_A=s/\sqrt{N}$  i comprendre el paper crític de la hipòtesi d'independència.
> - Interpretar la llei de  $\sqrt{N}$  i els seus límits pràctics.

L'avaluació de tipus A utilitza l'estadística per transformar una sèrie de lectures repetides en una estimació del mesurand i una quantificació del seu dubte. Es basa en una premissa: el millor predictor del comportament futur d'un sistema és el seu comportament passat observat estadísticament. Perquè la incertesa calculada tingui sentit, però, cal que es compleixin certes condicions.

## 1 Requisits per aplicar l'avaluació de tipus A

- **Condicions de repetibilitat.** Les mesures s'han de prendre en un període curt, pel mateix operador, amb el mateix instrument, al mateix lloc i sota condicions ambientals constants, de manera que l'única font de variació sigui l'error aleatori. Si les condicions canvien (per exemple, si la temperatura puja durant l'experiment), la dispersió ja no reflectirà només l'aleatorietat, sinó una deriva sistemàtica, i invalidarà l'anàlisi.
- **Independència estadística.** El valor d'una lectura no ha de condicionar el de la següent; el soroll ha de ser «blanc» (sense memòria). Si el sistema té una constant de temps llarga i mesurem molt de pressa, les lectures estaran correlacionades i l'estadística estàndard *subestimarà* greument la incertesa real.
- **Mesura sense biaix.** Perquè l'estimació del mesurand i la incertesa siguin representatives, el sistema no ha de tenir cap biaix (o aquest ha d'haver estat corregit prèviament).

Si es compleixen aquestes condicions, la dispersió dels resultats és una mesura directa de la qualitat del sistema i, juntament amb el nombre de mesures, determina la incertesa de tipus A.

## 2 Neteja de dades: valors aberrants

Abans d'estimar res, cal netejar les dades. En qualsevol sèrie poden aparèixer valors anòmals (*outliers*) causats per errors grollers. Un outlier té un efecte devastador sobre la mitjana i, especialment, sobre la desviació estàndard (els errors s'eleven al quadrat): un sol valor aberrant pot multiplicar la incertesa aparent per un factor de 10 o 100 sense cap justificació real. Un cop identificats —per inspecció visual o per criteris estadístics—, s'han d'eliminar del conjunt abans de procedir.

## 3 Estimació del mesurand i dispersions

Amb  $N$  dades vàlides i independents, si el sistema no té biaix el millor estimador del mesurand és la mitjana aritmètica, que serà el nostre resultat  $y$:

$$
\bar{x}=\frac{1}{N}\sum_{i=1}^{N} x_i \qquad (2.11)
$$

Els errors aleatoris, positius i negatius amb igual probabilitat, tendeixen a cancel·lar-se en sumar moltes mesures. Ara cal distingir dos conceptes de dispersió ben diferents:

- **Dispersió de la mostra** ( $s$ ): quant s'allunyen els punts individuals de la mitjana; ens diu com de sorollós és l'instrument. Si fem més mesures, no es redueix, sinó que s'estabilitza al voltant del soroll real del procés. Es calcula com la desviació estàndard experimental:

$$
s=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2} \qquad (2.12)
$$

- **Dispersió de la mitjana** ( $s_{\bar{x}}$ ): quant variaria la mitjana calculada si repetíssim tot l'experiment moltes vegades. Aquesta dispersió *sí* que es redueix en augmentar  $N$.

La incertesa de la mesura no es refereix a com de dispersa és una lectura individual, sinó a quant dubtem del resultat final, que és la mitjana. Per tant, la magnitud rellevant és la dispersió de la mitjana.

![25 lectures d'una quantitat representades com a punts, amb una línia horitzontal que marca la mitjana; les lectures es dispersen dins d'un marge estret](assets/2_04_tipus_A_img_1.png)

*Figura: Figura 2.2. Il·lustració del procediment de l'avaluació de tipus A: 25 lectures independents (punts) i la seva mitjana (línia). Si es repetís el procediment, la mitjana es desplaçaria; la incertesa de tipus A estima, a partir d'una sola sèrie, la desviació estàndard d'aquests possibles valors de la mitjana.*

## 4 La incertesa típica de tipus A

La GUM defineix la incertesa típica de tipus A com la desviació estàndard de la mitjana experimental:

$$
u_A=\frac{s}{\sqrt{N}} \qquad (2.13)
$$

on  $s$  és la desviació estàndard de les lectures individuals i  $N$  el nombre de mesures vàlides. Aquesta equació ens diu que podem reduir la incertesa del resultat augmentant  $N$, fins i tot amb un instrument sorollós.

### D'on surt l'expressió

Considerem que cada mesura  $X_i$  és una variable aleatòria; totes provenen del mateix procés (repetibilitat) i tenen la mateixa desviació estàndard teòrica  $\sigma$. El resultat és la mitjana:

$$
\bar{X}=\frac{1}{N}\sum_{i=1}^{N} X_i \qquad (2.14)
$$

Volem la variància de  $\bar{X}$. Aplicant l'operador variància:

$$
\mathrm{Var}\!\left[\bar{X}\right]=\mathrm{Var}\!\left[\frac{1}{N}\sum_{i=1}^{N} X_i\right] \qquad (2.15)
$$

Com que la variància d'una constant per una variable és la constant al quadrat per la variància:

$$
\mathrm{Var}\!\left[\bar{X}\right]=\frac{1}{N^2}\,\mathrm{Var}\!\left[\sum_{i=1}^{N} X_i\right] \qquad (2.16)
$$

Aquí entra la hipòtesi clau: si les  $X_i$  són **estadísticament independents**, la variància de la seva suma és igual a la suma de les variàncies, perquè els termes de covariància creuada són nuls:

$$
\mathrm{Var}\!\left[\sum_{i=1}^{N} X_i\right]=\sum_{i=1}^{N}\mathrm{Var}\!\left[X_i\right] \qquad (2.17)
$$

Com que totes les mesures es fan en les mateixes condicions i tenen la mateixa variància  $\sigma^2$:

$$
\mathrm{Var}\!\left[\sum_{i=1}^{N} X_i\right]=N\sigma^2 \qquad (2.18)
$$

Substituint en (2.16):

$$
\mathrm{Var}\!\left[\bar{X}\right]=\frac{1}{N^2}\,N\sigma^2=\frac{\sigma^2}{N} \qquad (2.19)
$$

La desviació estàndard és l'arrel quadrada de la variància:

$$
\sigma_{\bar{X}}=\frac{\sigma}{\sqrt{N}} \qquad (2.20)
$$

i, substituint el paràmetre poblacional  $\sigma$  pel seu estimador mostral  $s$, s'arriba a l'expressió pràctica de la incertesa de tipus A:

$$
u_A=\frac{s}{\sqrt{N}} \qquad (2.21)
$$

La demostració evidencia per què la independència és crítica: si les mesures no fossin independents, els termes de covariància no s'anul·larien, l'expressió (2.17) deixaria de ser vàlida i la fórmula  $s/\sqrt{N}$  subestimaria la incertesa real.

## 5 La llei de l'arrel de N i els seus límits

La millora de la incertesa va amb  $\sqrt{N}$: augmentar  $N$  és molt eficaç al principi, però esdevé ràpidament ineficient (multiplicar  $N$  per quatre només redueix  $u_A$  a la meitat). Matemàticament, si  $N\to\infty$,  $u_A\to 0$; a la pràctica, això és fals. Mai reduirem la incertesa a zero només fent mitjanes: sempre hi haurà límits imposats per errors sistemàtics residuals (incertesa de tipus B), deriva temporal o resolució finita. **La incertesa de tipus A només combat la component aleatòria; no soluciona un mal calibratge.**

> [!TIP] **Síntesi**
>
> L'avaluació de tipus A estima la incertesa a partir de  $N$  lectures repetides, sempre que es compleixin repetibilitat, independència i absència de biaix, i després d'eliminar els valors aberrants. El resultat és la mitjana (2.11), i la incertesa típica és la desviació estàndard de la mitjana,  $u_A=s/\sqrt{N}$  (2.13), que cal no confondre amb la dispersió de les lectures  $s$. La deducció (2.14)–(2.21) mostra que la independència és el que permet sumar variàncies; sense ella, els termes de covariància no s'anul·len i  $s/\sqrt{N}$  subestimaria la incertesa. La reducció segueix la llei de  $\sqrt{N}$, amb rendiments decreixents, i mai elimina el biaix ni les components de tipus B.

[← 3. El model matemàtic de la mesura](#u203-el-model-matemàtic-de-la-mesura)[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)[5. Avaluació de la incertesa de tipus B →](#u205-avaluació-de-la-incertesa-de-tipus-b)

---

<!-- FIN CAPÍTULO: 2_04_tipus_A -->

---

<!-- INICIO CAPÍTULO: 2_05_tipus_B -->

# U2·05 Avaluació de la incertesa de tipus B

> [!NOTE] **Objectius d'aprenentatge**
>
> - Reconèixer les fonts d'informació per a una avaluació de tipus B i el paper del judici científic.
> - Assignar una funció de densitat de probabilitat (fdp) segons la informació disponible, aplicant el principi de màxima entropia.
> - Convertir toleràncies, especificacions i certificats en una incertesa típica equivalent.
> - Aplicar els divisors característics de les distribucions uniforme ( $\sqrt{3}$ ), triangular ( $\sqrt{6}$ ), normal ( $k$ ) i en U ( $\sqrt{2}$ ).
> - Comparar la dispersió que aporta cada distribució per a un mateix semi-interval d'error.

Sovint no és possible ni pràctic fer múltiples lectures per caracteritzar cada variable. Si fem servir una resistència patró, no la mesurarem mil vegades: confiarem en el valor nominal i la tolerància del fabricant. Aquí entra l'**avaluació de tipus B**, que no es basa en l'estadística de noves observacions, sinó en el judici científic i el coneixement previ. Segons la GUM, una incertesa de tipus B no és menys rigorosa que una de tipus A; de fet, en molts calibratges industrials és la component dominant. El repte és traduir informació qualitativa o semiquantitativa en una desviació estàndard equivalent  $u$.

A diferència del tipus A, partim d'una **única estimació** del mesurand (una lectura, un valor nominal) i li associem una fdp centrada en aquesta estimació, generalment simètrica. La desviació estàndard d'aquesta fdp és la incertesa típica de tipus B.

![Corba de densitat de probabilitat centrada en la lectura y, amb la desviació típica u(y) que en marca l'amplada](assets/2_05_tipus_B_img_1.png)

*Figura: Figura 2.3. Procés d'avaluació de la incertesa de tipus B: a partir d'una mesura $y$ s'assigna una fdp centrada al voltant seu, i la seva desviació típica $u(y)$ és la incertesa típica.*

## 1 Fonts d'informació

La GUM llista diverses fonts vàlides que l'avaluador ha d'explorar i documentar:

- **Especificacions del fabricant** (datasheets): garanties d'exactitud o tolerància. És la font més habitual en electrònica.
- **Certificats de calibratge**: proporcionen l'error mesurat i, crucialment, la incertesa expandida  $U$  i el factor de cobertura  $k$. Són informació de màxima qualitat.
- **Dades de mesures anteriors**: històrics de control de qualitat o caracteritzacions prèvies (per exemple, una deriva coneguda d'un termoparell).
- **Lleis físiques i constants de referència**: valors amb incerteses publicades. Ara bé, les constants fonamentals que *defineixen* el SI, usades amb tots els seus dígits, no tenen incertesa associada.
- **Experiència i coneixement general**: comportament conegut dels materials (histèresi, coeficients tèrmics) o de l'operador.

## 2 Com escollir la distribució: màxima entropia

Com que no tenim un histograma de dades reals, hem de suposar com es distribueixen els valors possibles dins de l'interval d'incertesa. El principi rector és el **criteri de màxima entropia** (principi d'indiferència): triar la distribució que incorpori tota la informació que tenim, però *cap informació que no tinguem*. Afegir hipòtesis no justificades per reduir la incertesa seria inventar informació.

- Si només coneixem uns límits  $\pm a$  i res més, no hi ha motiu per pensar que el centre és més probable que els extrems: la distribució de màxima entropia és la **uniforme**.
- Si tenim raons físiques per creure que els valors centrals són més probables (un procés que apunta al centre), es justifica la **triangular**.
- Si coneixem una dispersió característica i l'error és suma de moltes causes petites, el teorema del límit central porta a la **normal**.

## 3 Les quatre distribucions

### Distribució uniforme (rectangular)

És l'opció «per defecte» quan la informació prové de fulls de dades o toleràncies que només donen uns límits  $\pm a$  sense nivell de confiança. Assumeix que el valor pot trobar-se amb igual probabilitat en qualsevol punt de l'interval. La incertesa típica és:

$$
u=\frac{a}{\sqrt{3}} \qquad (2.22)
$$

![Distribució uniforme: rectangle de probabilitat constant entre -a i +a](assets/2_05_tipus_B_img_2.png)

*Figura: Figura 2.4. Distribució uniforme.*

Per exemple, un voltímetre digital que mostra «5,000 V» té un error de quantificació limitat a mig dígit de l'últim dígit. Si la resolució és d'1 mV, la semiamplada és  $a=0{,}5$  mV i la incertesa típica de resolució és  $u=0{,}5/\sqrt{3}\approx 0{,}29$  mV. De la mateixa manera, una resistència de 1 kΩ amb tolerància del ±5 % té una semiamplada  $a=50$  Ω, de manera que  $u=50/\sqrt{3}\approx 29$  Ω.

### Distribució triangular

S'utilitza quan tenim uns límits  $\pm a$  però tenim evidència que els valors extrems són molt menys probables que els centrals; la probabilitat creix linealment des dels extrems fins al centre. La incertesa típica és:

$$
u=\frac{a}{\sqrt{6}} \qquad (2.23)
$$

![Distribució triangular: probabilitat que creix linealment des dels extrems fins al centre](assets/2_05_tipus_B_img_3.png)

*Figura: Figura 2.5. Distribució triangular.*

La incertesa resultant és menor que en la uniforme perquè estem «premiant» la informació sobre la centralitat. És adequada, per exemple, en una lectura analògica interpolada (l'ull tendeix a centrar la lectura), en la suma de dues variables uniformes de la mateixa amplada (la convolució de dos rectangles és un triangle) o en un ajust manual on l'operador apunta al centre.

### Distribució normal (gaussiana)

S'assigna quan la informació de partida ja ve en termes probabilístics, típicament amb un nivell de confiança o un factor de cobertura. No té límits estrictes (les cues s'estenen a l'infinit). Si ens donen una incertesa expandida  $U$  i un factor  $k$, desfem el camí:

$$
u=\frac{U}{k} \qquad (2.24)
$$

![Distribució normal: campana de Gauss centrada, amb cues que s'estenen a l'infinit](assets/2_05_tipus_B_img_4.png)

*Figura: Figura 2.6. Distribució normal.*

Si ens donen  $U$  al 95 % de confiança prenem  $k\approx 2$  (més exactament 1,96); si ens el donen al 99,7 % («3 sigma»), prenem  $k=3$. Cada cop és més freqüent que els fabricants indiquin el factor de cobertura per poder aplicar (2.24). La norma ISO/IEC 17025 obliga els laboratoris a reportar  $U$  i  $k$. Un altre cas natural és el soroll Johnson-Nyquist d'una resistència: com que és resultat de milions de col·lisions aleatòries d'electrons, pel teorema del límit central segueix una distribució normal, i la seva incertesa típica és igual al valor eficaç (RMS) del soroll.

### Distribució en forma de U (arcsinus)

Menys comuna, però crucial en instrumentació elèctrica: apareix quan la variable oscil·la sinusoidalment entre dos límits i es mostreja en un instant aleatori. És molt més probable trobar el valor a prop dels pics (on el sinus es mou a poc a poc) que al pas per zero. Per a una amplitud de pic  $A$, la incertesa típica (valor RMS) és:

$$
u=\frac{A}{\sqrt{2}} \qquad (2.25)
$$

![Distribució en forma de U: densitat de probabilitat que creix cap als dos extrems formant una U](assets/2_05_tipus_B_img_5.png)

*Figura: Figura 2.7. Distribució en forma de U.*

És la distribució amb més dispersió de totes per a una mateixa cota. Un cas típic és una interferència de xarxa (50 Hz) d'amplitud  $A$  superposada a un senyal de contínua que l'instrument no filtra completament: l'error màxim és  $A$  i la incertesa típica,  $A/\sqrt{2}$.

## 4 Comparació per a un mateix semi-interval

Per a un mateix semi-interval d'error  $a$, la incertesa típica varia segons el que sabem de la distribució:

| Distribució | Coneixement implícit | Incertesa típica |
|:--- |:--- |:--- |
| En U | Valors extrems més probables (oscil·lació) | $a/\sqrt{2}\approx 0{,}707\,a$ |
| Uniforme | Cap coneixement (màxima entropia) | $a/\sqrt{3}\approx 0{,}577\,a$ |
| Triangular | Valors centrals més probables | $a/\sqrt{6}\approx 0{,}408\,a$ |
| Normal | Probabilitat definida ( $U$,  $k$ ) | $U/k$  (variable) |

La taula il·lustra la importància del judici: davant una mateixa especificació de «error màxim», un enginyer que esculli la distribució en U estimarà una incertesa gairebé el doble de gran que un que pugui justificar una triangular. La GUM recomana la uniforme quan no hi ha informació per decantar-se, i insisteix a **documentar sempre la fdp emprada**: així, si més endavant es troba que no era l'adient, es pot recuperar el semi-interval  $a$  i recalcular la incertesa amb una altra distribució.

> [!TIP] **Síntesi**
>
> L'avaluació de tipus B tradueix informació prèvia (datasheets, certificats, històrics, lleis, experiència) en una incertesa típica, assignant una fdp centrada en l'estimació segons el principi de màxima entropia. Els quatre models bàsics donen  $u=a/\sqrt{3}$  (uniforme),  $u=a/\sqrt{6}$  (triangular),  $u=U/k$  (normal) i  $u=A/\sqrt{2}$  (en U). Per a un mateix semi-interval, la distribució en U és la més dispersa i la triangular la menys. Cal documentar sempre la distribució escollida per poder revisar el càlcul.

[← 4. Avaluació de la incertesa de tipus A](#u204-avaluació-de-la-incertesa-de-tipus-a)[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)[6. Combinació d'incerteses en mesures indirectes →](#u206-combinació-dincerteses-en-mesures-indirectes)

---

<!-- FIN CAPÍTULO: 2_05_tipus_B -->

---

<!-- INICIO CAPÍTULO: 2_06_combinacio -->

# U2·06 Combinació d'incerteses en mesures indirectes

> [!NOTE] **Objectius d'aprenentatge**
>
> - Deduir la llei de propagació de la incertesa a partir de la linealització de Taylor del model de mesura.
> - Calcular els coeficients de sensibilitat i interpretar-ne la magnitud, el signe i les unitats.
> - Combinar les contribucions en quadratura per a variables independents.
> - Reconèixer quan cal afegir termes de covariància i quin efecte hi té el signe de la correlació.
> - Identificar les situacions en què la linealització deixa de ser fiable i què aporta el mètode de Monte Carlo.

La majoria de mesures s'obtenen de manera indirecta: mesurem diverses magnituds  $X_i$  i les combinem mitjançant un model per obtenir el resultat  $Y$. Ja sabem estimar la incertesa de cada variable (tipus A o B); ara abordem el problema central: com es combinen aquestes incerteses individuals per obtenir la incertesa del resultat final. El procés s'anomena **combinació d'incerteses** i es fonamenta en la **llei de propagació de la incertesa**.

## 1 Linealització del model

El fonament teòric és el càlcul diferencial. Suposem uns valors mesurats  $x_i$  (les millors estimacions) i el resultat  $y=f(x_1,\dots,x_N)$. Si el valor real de cada entrada es desvia lleugerament del mesurat, el de la sortida també ho farà. Per trobar la relació, expandim  $f$  en sèrie de Taylor al voltant del punt de mesura i ens quedem amb els termes de primer ordre:

$$
\Delta y \approx \sum_{i=1}^{N}\frac{\partial f}{\partial x_i}\,\Delta x_i \qquad (2.26)
$$

Aquesta aproximació és vàlida sempre que les incerteses siguin petites comparades amb la curvatura (no-linealitat) de  $f$.

![Funció de mesura aproximada per la recta tangent en el punt nominal; el pendent transmet la incertesa d'entrada al resultat](assets/2_06_combinacio_img_1.png)

*Figura: Figura 2.8. Definició dels coeficients de sensibilitat: la funció $f$ s'aproxima per la recta tangent en el punt nominal, i el seu pendent determina com la incertesa d'entrada es transmet al resultat.*

## 2 Coeficients de sensibilitat

Les derivades parcials que apareixen en l'expansió reben el nom de **coeficients de sensibilitat**:

$$
c_i=\frac{\partial f}{\partial x_i} \qquad (2.27)
$$

Cada  $c_i$  es calcula derivant el model respecte a la variable  $x_i$  i substituint-hi després els valors nominals. Per exemple, si mesurem potència amb  $P=V\cdot I$, aleshores  $c_V=\partial P/\partial V=I$  i  $c_I=\partial P/\partial I=V$.

El coeficient  $c_i$  indica com de sensible és el resultat als errors d'aquella variable: si  $c_i$  és gran, una petita incertesa en  $x_i$  provocarà una gran incertesa en  $y$  (variable crítica); si és petit, aquella variable afecta poc. Les seves unitats són les del mesurand dividides per les de l'entrada (per exemple, W/V = A per al coeficient de la tensió en calcular la potència): així, quan multipliquem la incertesa d'entrada  $u(x_i)$  pel seu coeficient, el producte  $c_i\,u(x_i)$  queda en les unitats de sortida.

## 3 La incertesa típica combinada

Si les variables d'entrada són independents, la variància total és la suma de les variàncies individuals ponderades pels quadrats dels coeficients de sensibilitat:

$$
u_c^2(y)=\sum_{i=1}^{N} c_i^{\,2}\,u^2(x_i) \qquad (2.28)
$$

i la incertesa típica combinada és l'arrel quadrada d'aquesta suma (suma en quadratura):

$$
u_c(y)=\sqrt{\sum_{i=1}^{N} c_i^{\,2}\,u^2(x_i)} \qquad (2.29)
$$

Aquesta fórmula és la pedra angular de la GUM. Pressuposa **independència** entre les variables d'entrada (en el curs, dissenyem els experiments per assegurar-la) i té una propietat important: **penalitza els termes grans**. Si una font és molt més gran que les altres (per exemple, 10 enfront d'1), la petita esdevé insignificant en la suma quadràtica ( $\sqrt{10^2+1^2}=\sqrt{101}\approx 10{,}05$ ). Això indica on cal focalitzar els esforços: reduir la incertesa dominant és l'única manera eficaç de millorar el sistema.

## 4 Variables correlacionades: termes de covariància

Quan les variables d'entrada **no** són independents —per exemple, si es mesuren amb el mateix instrument, que té una deriva tèrmica, o si depenen d'una referència comuna—, la suma simple de variàncies falla i cal afegir termes que tinguin en compte la correlació:

$$
u_c^2(y)=\sum_{i=1}^{N} c_i^{\,2}\,u^2(x_i)+2\sum_{i=1}^{N-1}\sum_{j=i+1}^{N} c_i\,c_j\,u(x_i,x_j) \qquad (2.30)
$$

on  $u(x_i,x_j)=r(x_i,x_j)\,u(x_i)\,u(x_j)$  és la **covariància** entre  $x_i$  i  $x_j$, i  $r$  el coeficient de correlació. L'efecte del terme creuat depèn del signe:

- Si la correlació és **positiva** i els coeficients de sensibilitat tenen el **mateix signe**, el terme creuat és positiu i la incertesa combinada *augmenta* respecte al cas independent.
- Si la correlació és **negativa** (o els coeficients tenen signes oposats), el terme creuat és negatiu i les contribucions es poden *compensar parcialment*, de manera que la incertesa combinada es redueix. Aquesta compensació és parcial: no anul·la la incertesa.

La GUM no prohibeix tractar variables correlacionades, sinó que en proporciona la formulació completa (2.30). Ara bé, en la pràctica habitual d'enginyeria —i en aquest curs, llevat que es digui el contrari— dissenyem els experiments per assegurar la independència i utilitzem la fórmula simplificada (2.29).

## 5 Quan la linealització no és fiable: Monte Carlo

Hi ha situacions en què la propagació basada en derivades no és fiable: quan el model és fortament no lineal respecte a la magnitud de les incerteses (la curvatura és important dins de l'interval d'error), quan la fdp de sortida no s'assembla a una normal (per límits físics abruptes) o quan el càlcul de derivades parcials és intractable.

![Funció no lineal amb una incertesa d'entrada gran; l'interval de sortida queda descentrat respecte de f(q) i l'aproximació lineal falla](assets/2_06_combinacio_img_2.png)

*Figura: Figura 2.9. Exemple on la linealització no és vàlida: amb una incertesa gran en $x$, l'aproximació lineal és errònia i l'interval de sortida no queda centrat en $f(q)$.*

En aquests casos, la GUM (suplement 1) recomana el **mètode de Monte Carlo**, que propaga incerteses sense substituir el model per una aproximació lineal. El procediment és conceptualment senzill: s'assigna una fdp a cada magnitud d'entrada (amb valor mitjà igual al nominal i desviació igual a  $u(x_i)$ ); es generen moltes realitzacions aleatòries de les entrades, on cada conjunt representa possibles valors reals de les magnituds; es calcula el resultat amb el model *exacte* per a cada conjunt; i s'analitza l'histograma dels milers de resultats. D'aquest histograma s'obtenen directament la **mitjana** (millor estimació del mesurand), la **desviació estàndard** (que és la incertesa típica combinada  $u_c$ ) i els **percentils** (per exemple, 2,5 % i 97,5 % per a un interval del 95 %).

El mètode és universal i, a més, mostra la forma real de la distribució de sortida —si és simètrica, asimètrica o multimodal—, cosa que la fórmula analítica no pot veure. Quan diverses fonts independents es combinen, el teorema del límit central fa que la sortida s'aproximi a una normal; però si una única font domina, la distribució pot conservar trets de la seva fdp. Per a incerteses petites, Monte Carlo i la llei de propagació coincideixen gairebé perfectament, cosa que valida l'ús de la fórmula analítica —més ràpida— per al dia a dia.

> [!TIP] **Síntesi**
>
> La llei de propagació linealitza el model amb una sèrie de Taylor de primer ordre. Els coeficients de sensibilitat  $c_i=\partial f/\partial x_i$  mesuren com cada entrada afecta la sortida i homogeneïtzen les unitats. Per a variables independents, les contribucions  $c_i\,u(x_i)$  es combinen en quadratura fins a  $u_c(y)=\sqrt{\sum c_i^2 u^2(x_i)}$, fórmula que penalitza les fonts grans i assenyala on convé millorar. Si hi ha correlació cal afegir termes de covariància (2.30): una correlació positiva amb coeficients del mateix signe augmenta la incertesa, i una de negativa la pot compensar parcialment. Quan la linealització falla —forta no-linealitat, distribucions no normals o derivades intractables— s'utilitza el mètode de Monte Carlo, que assigna una fdp a cada entrada, genera moltes realitzacions i n'obté la mitjana, la desviació estàndard ( $u_c$ ) i els percentils a partir de l'histograma de sortida.

[← 5. Avaluació de la incertesa de tipus B](#u205-avaluació-de-la-incertesa-de-tipus-b)[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)[7. Incertesa expandida, factor de cobertura i graus de llibertat →](#u207-incertesa-expandida-factor-de-cobertura-i-graus-de-llibertat)

---

<!-- FIN CAPÍTULO: 2_06_combinacio -->

---

<!-- INICIO CAPÍTULO: 2_07_incertesa_expandida -->

# U2·07 Incertesa expandida, factor de cobertura i graus de llibertat

> [!NOTE] **Objectius d'aprenentatge**
>
> - Calcular la incertesa expandida  $U=k\,u_c$  i triar el factor de cobertura segons la distribució i el nivell de confiança.
> - Associar els factors  $k=2$  i  $k=3$  als nivells del 95 % i del 99,7 % en el cas normal.
> - Reconèixer quan cal la distribució t de Student (poques mesures de tipus A).
> - Aplicar la fórmula de Welch-Satterthwaite per estimar els graus de llibertat efectius.

La incertesa típica combinada  $u_c$  és perfecta per als càlculs intermedis, però sovint insuficient per comunicar el resultat final: una desviació estàndard només cobreix aproximadament el 68 % de probabilitat (en el cas normal). Si diem «el valor és  $y\pm u_c$ », hi ha un 32 % de possibilitats que el valor real quedi fora, un risc d'1 de cada 3 inacceptable en la majoria d'aplicacions. Per això el pas final sol ser calcular la **incertesa expandida**  $U$, que amplia l'interval fins a un nivell de confiança superior.

## 1 Definició i expressió del resultat

La incertesa expandida és el producte de la incertesa típica combinada per un **factor de cobertura**  $k$:

$$
U=k\,u_c(y) \qquad (2.31)
$$

i el resultat final s'expressa aleshores com:

$$
Y=y\pm U \qquad (2.32)
$$

El nivell de confiança és la probabilitat que l'interval  $y\pm U$  contingui el valor veritable. No n'hi ha cap de «correcte» universal; depèn de l'aplicació: el **95 %** (o 95,45 %) és l'estàndard de facto en indústria i calibratge, i sovint es llegeix « $k=2$ »; el **99 %** (o 99,73 %) s'usa en aplicacions crítiques (seguretat, aeroespacial, salut), habitualment amb  $k=3$; en física de partícules es busquen certeses de «5 sigma». Un nivell de confiança més alt implica, en general, un interval més ample.

## 2 El factor de cobertura en el cas normal

El valor de  $k$  depèn de la distribució del resultat final i del nivell de confiança. Per avaluacions de tipus A la mitjana tendeix a una normal; per mesures indirectes, si cap font domina, pel teorema del límit central la sortida tendeix a una normal independentment de si les entrades eren uniformes o triangulars. Assumint normalitat, els factors són:

| Nivell de confiança | Factor  $k$ |
|:--- |:--- |
| 68,27 % | 1 |
| 90 % | 1,645 |
| 95 % | 1,96 |
| 95,45 % | 2 |
| 99 % | 2,576 |
| 99,73 % | 3 |

La regla pràctica més comuna és, doncs: «multiplica la incertesa combinada per 2 per obtenir aproximadament el 95 % de confiança». Per a nivells arbitraris, si s'assumeix normalitat el factor s'obté, en Python amb SciPy (`from scipy.stats import norm`), com `k = -norm.ppf((1-Conf/100)/2)` (per exemple, per al 99,9 % dona  $k=3{,}29$ ).

## 3 Poques dades: la distribució t de Student

La regla del  $k=2$  assumeix que la nostra estimació de la incertesa és sòlida i que la distribució és normal. Això és cert si les avaluacions de tipus A s'han fet amb moltes mostres i les de tipus B es coneixen amb precisió. Però si la incertesa dominant prové d'una repetibilitat de tipus A amb només 3 o 4 mesures, l'estimació de la dispersió és poc fiable: la distribució real no és normal, sinó una **t de Student** amb pocs graus de llibertat, que té *cues més amples*. Aleshores  $k$  ha de ser més gran que 2 per garantir el mateix 95 %. Per exemple, al 95 %: per  $\nu\to\infty$,  $k=1{,}96$; per  $\nu=9$,  $k\approx 2{,}26$; per  $\nu=3$,  $k\approx 3{,}18$. Usar  $k=2$  amb només 4 mesures donaria un nivell de confiança real molt inferior al 95 %. En Python amb SciPy (`from scipy.stats import t`) s'obté amb `k = -t.ppf((1-Conf/100)/2, N-1)`, on  $N$  és el nombre de mesures i  $\nu=N-1$  els graus de llibertat.

## 4 Graus de llibertat efectius: Welch-Satterthwaite

Quan combinem fonts, algunes poden ser molt sòlides (tipus B de full de dades, o tipus A amb  $N$  gran) i d'altres molt febles (tipus A amb poques mesures). Quin  $k$  fem servir per a la  $u_c$  global? La GUM ho resol calculant els **graus de llibertat efectius**  $\nu_{\text{ef}}$, una mena de mitjana ponderada que representa quanta informació equivalent tenim sobre la incertesa combinada:

$$
\nu_{\text{ef}}=\frac{u_c^{\,4}(y)}{ \sum_{i=1}^{N}\frac{u_i^{\,4}}{\nu_i}} \qquad (2.33)
$$

on  $u_i=c_i\,u(x_i)$  és la contribució de la font  $i$ -èsima i  $\nu_i$  els seus graus de llibertat. Per a les fonts de **tipus A**,  $\nu_i=N_i-1$. Per a les de **tipus B** basades en límits ben establerts, s'assumeix  $\nu_i\to\infty$, de manera que el seu terme al denominador s'anul·la. Si la font dominant té molts graus de llibertat,  $\nu_{\text{ef}}$  és gran i podem usar el  $k$  de la normal; si en té pocs,  $\nu_{\text{ef}}$  baixa i ens força a usar un  $k$  més gran (t de Student).

El procediment per a la incertesa expandida en mesures indirectes és, doncs: (1) calcular totes les contribucions  $u_i$  i la  $u_c$; (2) calcular  $\nu_{\text{ef}}$  amb Welch-Satterthwaite; (3) buscar el  $k$  corresponent a  $\nu_{\text{ef}}$  i al nivell de confiança desitjat (taula t de Student o funció de càlcul); i (4) calcular  $U=k\,u_c$.

> [!TIP] **Síntesi**
>
> La incertesa expandida  $U=k\,u_c$  amplia l'interval fins al nivell de confiança desitjat. En el cas normal,  $k=2$  correspon a ≈95 % i  $k=3$  a ≈99,73 %. Quan la incertesa dominant prové de poques mesures de tipus A, la distribució és una t de Student amb cues més amples. Els graus de llibertat efectius es calculen amb Welch-Satterthwaite (2.33), amb  $\nu_i=N_i-1$  per al tipus A i  $\nu_i\to\infty$  per al tipus B; el seu valor determina el  $k$  adequat per a la incertesa combinada.

[← 6. Combinació d'incerteses en mesures indirectes](#u206-combinació-dincerteses-en-mesures-indirectes)[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)[8. Expressió final del resultat i balanç d'incertesa →](#u208-expressió-final-del-resultat-i-balanç-dincertesa)

---

<!-- FIN CAPÍTULO: 2_07_incertesa_expandida -->

---

<!-- INICIO CAPÍTULO: 2_08_expressio_final -->

# U2·08 Expressió final del resultat i balanç d'incertesa

> [!NOTE] **Objectius d'aprenentatge**
>
> - Construir un balanç d'incertesa i interpretar-ne la columna de contribucions per identificar la font dominant.
> - Calcular la incertesa combinada com l'arrel de la suma de quadrats de les contribucions.
> - Aplicar les regles d'arrodoniment i de format en l'expressió final del resultat.

La documentació del procés és tan important com el resultat numèric. Un sol número final no permet a ningú auditar el procés, detectar errors o saber què cal millorar. Per això la GUM recomana presentar els resultats en forma de **balanç d'incertesa** (*uncertainty budget*): una taula que mostra, fila per fila, com cada magnitud d'entrada contribueix a la incertesa final.

## 1 El balanç d'incertesa

Les columnes estàndard són: la **magnitud** d'entrada; la seva **estimació** (valor nominal); la seva **incertesa típica**  $u(x_i)$; la **fdp** que se li presumeix; el **coeficient de sensibilitat**  $c_i$; i la **contribució**, producte (en valor absolut) de la incertesa típica pel coeficient de sensibilitat, que indica com la incertesa de cada magnitud es propaga cap a la sortida. A l'última fila s'hi indica l'estimació de la mesura indirecta  $y$, obtinguda substituint els valors nominals en el model.

![Taula genèrica de balanç d'incertesa amb columnes de magnitud, estimació, incertesa típica, fdp, coeficient de sensibilitat i contribució](assets/2_08_expressio_final_img_1.png)

*Figura: Figura 2.10. Taula genèrica per al balanç d'incertesa.*

| Magnitud | Estimació | $u(x_i)$ | fdp | $c_i$ | Contribució  $|c_i|\,u(x_i)$ |
|:--- |:--- |:--- |:--- |:--- |:--- |
| $x_1$ | $x_1$ | $u(x_1)$ | — | $c_1$ | $|c_1|\,u(x_1)$ |
| $x_2$ | $x_2$ | $u(x_2)$ | — | $c_2$ | $|c_2|\,u(x_2)$ |
| $\vdots$ |  |  |  |  | $\vdots$ |
| $y$ | $f(x_1,x_2,\dots)$ |  |  |  | $u_c(y)$ |

La cel·la inferior dreta no és la suma aritmètica, sinó l'arrel quadrada de la suma de quadrats de la columna de contribucions:

$$
u_c(y)=\sqrt{\sum_{i=1}^{N}\left[\,c_i\,u(x_i)\,\right]^2} \qquad (2.34)
$$

## 2 Anàlisi de dominància

El valor principal de la taula és visual: permet una anàlisi de dominància immediata mirant la columna de contribucions. Si una contribució és, per exemple, de 5 unitats i la següent d'1, la suma quadràtica és  $\sqrt{5^2+1^2}\approx 5{,}10$: la font petita és pràcticament irrellevant. Per millorar el sistema cal atacar primer la font principal. Així, el balanç transforma la metrologia d'una tasca burocràtica en una eina de disseny: indica exactament on invertir (un sensor millor, més control de temperatura) i on es pot estalviar (un component més barat sense empitjorar la qualitat global).

## 3 Regles de format del resultat final

El resultat s'ha d'escriure seguint unes regles estrictes per evitar ambigüitats:

- La incertesa expandida  $U$  s'arrodoneix, normalment, a dues xifres significatives (per exemple, 0,012 V, no 0,01234 V). No té sentit donar cinc decimals sobre un dubte.
- El resultat  $y$  s'arrodoneix per tenir el mateix dígit menys significatiu que la incertesa. Si  $U=0{,}012$  V, aleshores  $y$  ha de tenir tres decimals (per exemple 1,530 V, no 1,5304 V ni 1,53 V).
- Sempre s'ha d'indicar el factor de cobertura  $k$  utilitzat (i, convé, el nivell de confiança associat).

Un exemple de report adequat seria: «El valor mesurat de la resistència és  $R=84{,}9\pm 2{,}9$  kΩ. La incertesa expandida es basa en una incertesa típica multiplicada per un factor de cobertura  $k=2$, que proporciona un nivell de confiança d'aproximadament el 95 %.» Amb aquesta frase, dades disperses s'han convertit en una afirmació tècnica precisa, acotada i útil per a la presa de decisions.

> [!TIP] **Síntesi**
>
> El balanç d'incertesa documenta, fila per fila, l'estimació, la incertesa típica, la fdp, el coeficient de sensibilitat i la contribució de cada magnitud d'entrada. La incertesa combinada és l'arrel de la suma de quadrats de les contribucions (2.34), i la columna de contribucions permet identificar la font dominant i decidir on millorar. El resultat final s'expressa arrodonint  $U$  a dues xifres significatives, ajustant  $y$  al mateix dígit menys significatiu i indicant sempre el factor de cobertura  $k$.

[← 7. Incertesa expandida, factor de cobertura i graus de llibertat](#u207-incertesa-expandida-factor-de-cobertura-i-graus-de-llibertat)[Índex de la unitat](#unitat-2-estimació-de-la-incertesa-a-la-mesura)

---

<!-- FIN CAPÍTULO: 2_08_expressio_final -->

---

<!-- INICIO CAPÍTULO: 2_09_entrenament -->

# SM · Unitat 2 · Entrenament

Sistemes de Mesura · Unitat 2

# Entrenament d'afirmacions vertader/fals

Les 50 afirmacions sobre els documents de lectura prèvia

25:00

Corregir

## Tria com vols entrenar

Les dues modalitats presenten **les 50 afirmacions senceres**; el que canvia és l'ordre, el cronòmetre i el moment de veure la solució. En acabar, cada resposta mostra la justificació i el document on tornar.

**Simulacre cronometrat**
Les 50 en ordre aleatori i en menys de 25 minuts, amb correcció al final. És el mateix ritme que exigeix el qüestionari d'Atenea: 20 qüestions en 10 minuts.
**Entrenament lliure**
Les 50 en l'ordre dels documents, amb resposta immediata i sense cronòmetre. Per estudiar amb calma.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC
Unitat 2 · Material d'entrenament · Curs 2026-T

---

## 🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)

> [!TIP] **Com utilitzar aquest material d'entrenament**
> Aquest banc conté **50 afirmacions clau** dissenyades per consolidar els conceptes de la unitat i preparar els qüestionaris d'avaluació continuada.
> Intenta respondre mentalment **Vertader (V)** o **Fals (F)** abans de desplegar la solució i la justificació tècnica.

### Qüestió 01
> 📌 **Afirmació:** *La incertesa de mesura quantifica la dispersió de valors atribuïble al mesurand.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de la GUM: un nombre que quantifica la dispersió de valors atribuïble al mesurand, expressat en les unitats del mesurand.*

> **📚 Document de referència:** `2_01_introduccio.md`
> </details>

### Qüestió 02
> 📌 **Afirmació:** *L'error de mesura es pot calcular exactament sempre que la mesura es repeteixi moltes vegades.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'error exigeix conèixer el valor veritable, que és incognoscible. Repetir mesures redueix la component aleatòria, però no revela el valor veritable.*

> **📚 Document de referència:** `2_01_introduccio.md`
> </details>

### Qüestió 03
> 📌 **Afirmació:** *El valor veritable del mesurand es considera, en sentit estricte, desconegut i incognoscible.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Conèixer-lo requeriria un instrument perfecte, que no existeix; fins i tot els patrons primaris tenen incertesa.*

> **📚 Document de referència:** `2_01_introduccio.md`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *La incertesa i l'error de mesura són conceptes equivalents.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'error és la diferència respecte del valor veritable i és desconegut; la incertesa és un paràmetre positiu que quantifica el dubte i sí que es pot calcular.*

> **📚 Document de referència:** `2_01_introduccio.md`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *Un patró de referència també té una incertesa associada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per això un patró permet estimar l'error, però l'estimació arrossega la incertesa pròpia del patró.*

> **📚 Document de referència:** `2_01_introduccio.md`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *La GUM només s'aplica a mesures mecàniques i no a mesures elèctriques.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La GUM s'aplica a qualsevol domini de mesura; de fet és un requisit de la ISO/IEC 17025 també en calibratge elèctric i electrònic.*

> **📚 Document de referència:** `2_01_introduccio.md`
> </details>

### Qüestió 07
> 📌 **Afirmació:** *La incertesa s'expressa habitualment en les mateixes unitats que el mesurand.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És una magnitud quantitativa en les unitats del mesurand, no un simple percentatge.*

> **📚 Document de referència:** `2_01_introduccio.md`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *El resultat d'una mesura es pot interpretar com una realització d'una variable aleatòria.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És el marc probabilístic de la GUM: soroll, quantització, interferències i variacions ambientals fan que cada resultat sigui una realització.*

> **📚 Document de referència:** `2_02_marc_teoric.md`
> </details>

### Qüestió 09
> 📌 **Afirmació:** *Si el mesurand és constant, les lectures repetides d'un instrument real han de ser exactament iguals.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Encara amb un mesurand constant, les fonts de variació dispersen les lectures i en resulta una distribució de resultats.*

> **📚 Document de referència:** `2_02_marc_teoric.md`
> </details>

### Qüestió 10
> 📌 **Afirmació:** *La variància mostral no esbiaixada utilitza N−1 al denominador.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'estimador no esbiaixat de l'expressió (2.3).*

> **📚 Document de referència:** `2_02_marc_teoric.md`
> </details>

### Qüestió 11
> 📌 **Afirmació:** *La desviació estàndard de la mitjana augmenta quan augmenta el nombre de mesures independents.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Disminueix com s/√N. El que no es redueix en augmentar N és la dispersió de les lectures individuals.*

> **📚 Document de referència:** `2_02_marc_teoric.md`
> </details>

### Qüestió 12
> 📌 **Afirmació:** *El factor de cobertura k connecta la incertesa típica amb un interval de confiança.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *U = k·uc: el factor determina quantes desviacions estàndard calen per cobrir la probabilitat desitjada.*

> **📚 Document de referència:** `2_02_marc_teoric.md`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *La incertesa expandida U s'obté dividint la incertesa típica combinada pel factor de cobertura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Es multiplica: U = k·uc. Dividir per k és el pas invers, per passar d'una U donada a la incertesa típica.*

> **📚 Document de referència:** `2_02_marc_teoric.md`
> </details>

### Qüestió 14
> 📌 **Afirmació:** *Un nivell de confiança més alt requereix, en general, un interval de cobertura més ample.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Com més probabilitat es vol cobrir, més gran ha de ser k i, per tant, més ample l'interval.*

> **📚 Document de referència:** `2_02_marc_teoric.md`
> </details>

### Qüestió 15
> 📌 **Afirmació:** *El model de mesura relaciona el mesurand amb les magnituds d'entrada que l'afecten.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'expressió Y = f(X₁,…,X_N) (2.9), i escriure-la és el primer pas de tota anàlisi d'incertesa.*

> **📚 Document de referència:** `2_03_model_matematic.md`
> </details>

### Qüestió 16
> 📌 **Afirmació:** *Les magnituds d'entrada només poden ser lectures directes d'instruments.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *També hi entren constants físiques, correccions per efectes sistemàtics i factors ambientals que modifiquen la resposta.*

> **📚 Document de referència:** `2_03_model_matematic.md`
> </details>

### Qüestió 17
> 📌 **Afirmació:** *Les correccions per calibratge o temperatura poden formar part del model de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un bon model explicita les correccions rellevants, com la dilatació tèrmica de l'expressió (2.10).*

> **📚 Document de referència:** `2_03_model_matematic.md`
> </details>

### Qüestió 18
> 📌 **Afirmació:** *La classificació d'una incertesa com a tipus A o tipus B depèn del signe de l'error produït.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Depèn del mètode d'avaluació: estadística sobre observacions repetides (tipus A) o judici i informació prèvia (tipus B).*

> **📚 Document de referència:** `2_03_model_matematic.md`
> </details>

### Qüestió 19
> 📌 **Afirmació:** *Les incerteses de tipus A i de tipus B s'expressen finalment com a incerteses típiques i es poden combinar.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Totes dues acaben sent desviacions estàndard, i és això el que permet combinar-les matemàticament.*

> **📚 Document de referència:** `2_03_model_matematic.md`
> </details>

### Qüestió 20
> 📌 **Afirmació:** *En una mesura indirecta no cal definir cap model matemàtic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És precisament el que la defineix: combinar diverses mesures directes mitjançant un model no trivial.*

> **📚 Document de referència:** `2_03_model_matematic.md`
> </details>

### Qüestió 21
> 📌 **Afirmació:** *Una correcció aplicada al resultat pot tenir una incertesa associada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *No coneixem exactament els paràmetres de la correcció, i aquest dubte es propaga al resultat final.*

> **📚 Document de referència:** `2_03_model_matematic.md`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *La incertesa típica de tipus A de la mitjana es calcula com s/√N.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la desviació estàndard de la mitjana (2.13), que no s'ha de confondre amb la de les lectures individuals.*

> **📚 Document de referència:** `2_04_tipus_A.md`
> </details>

### Qüestió 23
> 📌 **Afirmació:** *L'avaluació de tipus A es basa exclusivament en les especificacions del fabricant.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Això és una avaluació de tipus B. La de tipus A es basa en l'anàlisi estadística d'observacions repetides.*

> **📚 Document de referència:** `2_04_tipus_A.md`
> </details>

### Qüestió 24
> 📌 **Afirmació:** *Els valors aberrants poden alterar de manera important la mitjana i la desviació estàndard.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Els errors s'eleven al quadrat, de manera que un sol outlier pot multiplicar la incertesa aparent.*

> **📚 Document de referència:** `2_04_tipus_A.md`
> </details>

### Qüestió 25
> 📌 **Afirmació:** *Fer més mesures permet reduir la incertesa total fins a fer-la nul·la.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Només combat la component aleatòria; hi queden el biaix residual, la deriva i les components de tipus B.*

> **📚 Document de referència:** `2_04_tipus_A.md`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *La dispersió de la mitjana descriu quant variaria la mitjana si es repetís l'experiment complet.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la magnitud rellevant per a la incertesa i, a diferència de s, decreix en augmentar N.*

> **📚 Document de referència:** `2_04_tipus_A.md`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *L'expressió s/√N continua essent vàlida encara que les lectures estiguin fortament correlacionades.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La deducció necessita que s'anul·lin els termes de covariància; amb lectures correlacionades, s/√N subestima la incertesa real.*

> **📚 Document de referència:** `2_04_tipus_A.md`
> </details>

### Qüestió 28
> 📌 **Afirmació:** *Multiplicar per quatre el nombre de mesures redueix la incertesa de tipus A aproximadament a la meitat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La millora va amb l'arrel quadrada de N: √4 = 2. D'aquí els rendiments decreixents d'augmentar N.*

> **📚 Document de referència:** `2_04_tipus_A.md`
> </details>

### Qüestió 29
> 📌 **Afirmació:** *Per a una distribució uniforme de semiamplada a, la incertesa típica és a/√3.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Expressió (2.22); és l'opció per defecte quan només es coneixen uns límits sense nivell de confiança.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 30
> 📌 **Afirmació:** *Per a una distribució triangular de semiamplada a, la incertesa típica és a/√2.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És a/√6 (2.23). El divisor √2 correspon a la distribució en forma de U.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 31
> 📌 **Afirmació:** *Per a una oscil·lació sinusoïdal d'amplitud de pic A, la incertesa típica és A/√2.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Expressió (2.25): és el valor eficaç d'una sinusoide, el cas de la distribució en forma de U.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *La distribució triangular concentra més probabilitat als extrems que al centre.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al revés: la probabilitat creix linealment des dels extrems cap al centre. La que carrega als extrems és la distribució en U.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 33
> 📌 **Afirmació:** *Si es coneixen la incertesa expandida U i el factor k, la incertesa típica associada és U/k.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Expressió (2.24): es desfà el camí de l'expansió, tal com permeten els certificats de calibratge.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *El principi de màxima entropia recomana afegir hipòtesis no justificades per obtenir una incertesa més petita.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Recomana just el contrari: incorporar tota la informació que es té i cap que no es tingui.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 35
> 📌 **Afirmació:** *Per a un mateix semi-interval a, la distribució en U dona una incertesa típica més petita que la triangular.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És la més dispersa de totes: a/√2 ≈ 0,707a, enfront de a/√6 ≈ 0,408a de la triangular.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 36
> 📌 **Afirmació:** *La tolerància d'una resistència comercial es pot convertir en una incertesa típica de tipus B.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La tolerància fixa la semiamplada; assumint distribució rectangular, u = a/√3.*

> **📚 Document de referència:** `2_05_tipus_B.md`
> </details>

### Qüestió 37
> 📌 **Afirmació:** *Els coeficients de sensibilitat són derivades parcials de la funció de mesura respecte de les variables d'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *cᵢ = ∂f/∂xᵢ (2.27), avaluades als valors nominals de les entrades.*

> **📚 Document de referència:** `2_06_combinacio.md`
> </details>

### Qüestió 38
> 📌 **Afirmació:** *La incertesa típica combinada s'obté sumant aritmèticament totes les contribucions.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Es combinen en quadratura (2.29): l'arrel quadrada de la suma dels quadrats de les contribucions.*

> **📚 Document de referència:** `2_06_combinacio.md`
> </details>

### Qüestió 39
> 📌 **Afirmació:** *Per a variables independents, les contribucions d'incertesa es combinen en quadratura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Expressions (2.28)-(2.29). La independència és el que permet sumar variàncies sense termes creuats.*

> **📚 Document de referència:** `2_06_combinacio.md`
> </details>

### Qüestió 40
> 📌 **Afirmació:** *Un coeficient de sensibilitat gran indica que aquella magnitud d'entrada és irrellevant per al resultat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Al contrari: com més gran és cᵢ, més crítica és aquella variable, perquè una petita incertesa seva provoca una gran incertesa a la sortida.*

> **📚 Document de referència:** `2_06_combinacio.md`
> </details>

### Qüestió 41
> 📌 **Afirmació:** *El mètode de Monte Carlo permet propagar incerteses sense substituir el model per una aproximació lineal.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Calcula el resultat amb el model exacte per a moltes realitzacions aleatòries de les entrades.*

> **📚 Document de referència:** `2_06_combinacio.md`
> </details>

### Qüestió 42
> 📌 **Afirmació:** *En una simulació de Monte Carlo no cal assignar cap distribució a les magnituds d'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Assignar una fdp a cada magnitud d'entrada és justament el primer pas del mètode.*

> **📚 Document de referència:** `2_06_combinacio.md`
> </details>

### Qüestió 43
> 📌 **Afirmació:** *La linealització és exacta encara que la funció presenti una curvatura molt elevada dins de l'interval d'incertesa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És una aproximació de primer ordre: amb curvatura important deixa de ser fiable i cal recórrer a Monte Carlo.*

> **📚 Document de referència:** `2_06_combinacio.md`
> </details>

### Qüestió 44
> 📌 **Afirmació:** *Per a una distribució normal, k = 3 s'associa aproximadament amb una cobertura del 99,73 %.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Taula 2.2 dels factors de cobertura; k = 2 correspon a aproximadament el 95 %.*

> **📚 Document de referència:** `2_07_incertesa_expandida.md`
> </details>

### Qüestió 45
> 📌 **Afirmació:** *El factor de cobertura és independent del nivell de confiança desitjat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Depèn tant del nivell de confiança com de la distribució de probabilitat assumida.*

> **📚 Document de referència:** `2_07_incertesa_expandida.md`
> </details>

### Qüestió 46
> 📌 **Afirmació:** *Amb poques mesures de tipus A, la distribució t de Student pot ser més adequada que la normal.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb pocs graus de llibertat l'estimació de la dispersió és poc fiable, i la t té cues més amples per compensar-ho.*

> **📚 Document de referència:** `2_07_incertesa_expandida.md`
> </details>

### Qüestió 47
> 📌 **Afirmació:** *Els graus de llibertat d'una avaluació de tipus A basada en N mesures són N + 1.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Són N − 1, i és el valor que entra a la fórmula de Welch-Satterthwaite.*

> **📚 Document de referència:** `2_07_incertesa_expandida.md`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *Amb pocs graus de llibertat, el factor k per al 95 % és sempre menor que 1,96.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És més gran: per exemple, amb ν = 3 cal k ≈ 3,18. L'interval s'ha d'eixamplar per compensar la manca d'informació.*

> **📚 Document de referència:** `2_07_incertesa_expandida.md`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *El resultat numèric s'ha d'arrodonir sempre a més decimals que la incertesa expandida.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *S'arrodoneix al mateix dígit menys significatiu que la incertesa: si U = 0,012 V, el resultat porta tres decimals.*

> **📚 Document de referència:** `2_08_expressio_final.md`
> </details>

### Qüestió 50
> 📌 **Afirmació:** *La columna de contribucions d'un balanç d'incertesa impedeix identificar les fonts dominants.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És justament el que permet: l'anàlisi de dominància es fa mirant aquesta columna per decidir on millorar.*

> **📚 Document de referència:** `2_08_expressio_final.md`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | És la definició de la GUM: un nombre que quantifica la dispersió de valors atribuïble al mesurand, expressat en les u... | 2_01_introduccio.md |
| **02** | **F** | L'error exigeix conèixer el valor veritable, que és incognoscible. Repetir mesures redueix la component aleatòria, pe... | 2_01_introduccio.md |
| **03** | **V** | Conèixer-lo requeriria un instrument perfecte, que no existeix; fins i tot els patrons primaris tenen incertesa. | 2_01_introduccio.md |
| **04** | **F** | L'error és la diferència respecte del valor veritable i és desconegut; la incertesa és un paràmetre positiu que quant... | 2_01_introduccio.md |
| **05** | **V** | Per això un patró permet estimar l'error, però l'estimació arrossega la incertesa pròpia del patró. | 2_01_introduccio.md |
| **06** | **F** | La GUM s'aplica a qualsevol domini de mesura; de fet és un requisit de la ISO/IEC 17025 també en calibratge elèctric ... | 2_01_introduccio.md |
| **07** | **V** | És una magnitud quantitativa en les unitats del mesurand, no un simple percentatge. | 2_01_introduccio.md |
| **08** | **V** | És el marc probabilístic de la GUM: soroll, quantització, interferències i variacions ambientals fan que cada resulta... | 2_02_marc_teoric.md |
| **09** | **F** | Encara amb un mesurand constant, les fonts de variació dispersen les lectures i en resulta una distribució de resultats. | 2_02_marc_teoric.md |
| **10** | **V** | És l'estimador no esbiaixat de l'expressió (2.3). | 2_02_marc_teoric.md |
| **11** | **F** | Disminueix com s/√N. El que no es redueix en augmentar N és la dispersió de les lectures individuals. | 2_02_marc_teoric.md |
| **12** | **V** | U = k·uc: el factor determina quantes desviacions estàndard calen per cobrir la probabilitat desitjada. | 2_02_marc_teoric.md |
| **13** | **F** | Es multiplica: U = k·uc. Dividir per k és el pas invers, per passar d'una U donada a la incertesa típica. | 2_02_marc_teoric.md |
| **14** | **V** | Com més probabilitat es vol cobrir, més gran ha de ser k i, per tant, més ample l'interval. | 2_02_marc_teoric.md |
| **15** | **V** | És l'expressió Y = f(X₁,…,X_N) (2.9), i escriure-la és el primer pas de tota anàlisi d'incertesa. | 2_03_model_matematic.md |
| **16** | **F** | També hi entren constants físiques, correccions per efectes sistemàtics i factors ambientals que modifiquen la resposta. | 2_03_model_matematic.md |
| **17** | **V** | Un bon model explicita les correccions rellevants, com la dilatació tèrmica de l'expressió (2.10). | 2_03_model_matematic.md |
| **18** | **F** | Depèn del mètode d'avaluació: estadística sobre observacions repetides (tipus A) o judici i informació prèvia (tipus B). | 2_03_model_matematic.md |
| **19** | **V** | Totes dues acaben sent desviacions estàndard, i és això el que permet combinar-les matemàticament. | 2_03_model_matematic.md |
| **20** | **F** | És precisament el que la defineix: combinar diverses mesures directes mitjançant un model no trivial. | 2_03_model_matematic.md |
| **21** | **V** | No coneixem exactament els paràmetres de la correcció, i aquest dubte es propaga al resultat final. | 2_03_model_matematic.md |
| **22** | **V** | És la desviació estàndard de la mitjana (2.13), que no s'ha de confondre amb la de les lectures individuals. | 2_04_tipus_A.md |
| **23** | **F** | Això és una avaluació de tipus B. La de tipus A es basa en l'anàlisi estadística d'observacions repetides. | 2_04_tipus_A.md |
| **24** | **V** | Els errors s'eleven al quadrat, de manera que un sol outlier pot multiplicar la incertesa aparent. | 2_04_tipus_A.md |
| **25** | **F** | Només combat la component aleatòria; hi queden el biaix residual, la deriva i les components de tipus B. | 2_04_tipus_A.md |
| **26** | **V** | És la magnitud rellevant per a la incertesa i, a diferència de s, decreix en augmentar N. | 2_04_tipus_A.md |
| **27** | **F** | La deducció necessita que s'anul·lin els termes de covariància; amb lectures correlacionades, s/√N subestima la incer... | 2_04_tipus_A.md |
| **28** | **V** | La millora va amb l'arrel quadrada de N: √4 = 2. D'aquí els rendiments decreixents d'augmentar N. | 2_04_tipus_A.md |
| **29** | **V** | Expressió (2.22); és l'opció per defecte quan només es coneixen uns límits sense nivell de confiança. | 2_05_tipus_B.md |
| **30** | **F** | És a/√6 (2.23). El divisor √2 correspon a la distribució en forma de U. | 2_05_tipus_B.md |
| **31** | **V** | Expressió (2.25): és el valor eficaç d'una sinusoide, el cas de la distribució en forma de U. | 2_05_tipus_B.md |
| **32** | **F** | És al revés: la probabilitat creix linealment des dels extrems cap al centre. La que carrega als extrems és la distri... | 2_05_tipus_B.md |
| **33** | **V** | Expressió (2.24): es desfà el camí de l'expansió, tal com permeten els certificats de calibratge. | 2_05_tipus_B.md |
| **34** | **F** | Recomana just el contrari: incorporar tota la informació que es té i cap que no es tingui. | 2_05_tipus_B.md |
| **35** | **F** | És la més dispersa de totes: a/√2 ≈ 0,707a, enfront de a/√6 ≈ 0,408a de la triangular. | 2_05_tipus_B.md |
| **36** | **V** | La tolerància fixa la semiamplada; assumint distribució rectangular, u = a/√3. | 2_05_tipus_B.md |
| **37** | **V** | cᵢ = ∂f/∂xᵢ (2.27), avaluades als valors nominals de les entrades. | 2_06_combinacio.md |
| **38** | **F** | Es combinen en quadratura (2.29): l'arrel quadrada de la suma dels quadrats de les contribucions. | 2_06_combinacio.md |
| **39** | **V** | Expressions (2.28)-(2.29). La independència és el que permet sumar variàncies sense termes creuats. | 2_06_combinacio.md |
| **40** | **F** | Al contrari: com més gran és cᵢ, més crítica és aquella variable, perquè una petita incertesa seva provoca una gran i... | 2_06_combinacio.md |
| **41** | **V** | Calcula el resultat amb el model exacte per a moltes realitzacions aleatòries de les entrades. | 2_06_combinacio.md |
| **42** | **F** | Assignar una fdp a cada magnitud d'entrada és justament el primer pas del mètode. | 2_06_combinacio.md |
| **43** | **F** | És una aproximació de primer ordre: amb curvatura important deixa de ser fiable i cal recórrer a Monte Carlo. | 2_06_combinacio.md |
| **44** | **V** | Taula 2.2 dels factors de cobertura; k = 2 correspon a aproximadament el 95 %. | 2_07_incertesa_expandida.md |
| **45** | **F** | Depèn tant del nivell de confiança com de la distribució de probabilitat assumida. | 2_07_incertesa_expandida.md |
| **46** | **V** | Amb pocs graus de llibertat l'estimació de la dispersió és poc fiable, i la t té cues més amples per compensar-ho. | 2_07_incertesa_expandida.md |
| **47** | **F** | Són N − 1, i és el valor que entra a la fórmula de Welch-Satterthwaite. | 2_07_incertesa_expandida.md |
| **48** | **F** | És més gran: per exemple, amb ν = 3 cal k ≈ 3,18. L'interval s'ha d'eixamplar per compensar la manca d'informació. | 2_07_incertesa_expandida.md |
| **49** | **F** | S'arrodoneix al mateix dígit menys significatiu que la incertesa: si U = 0,012 V, el resultat porta tres decimals. | 2_08_expressio_final.md |
| **50** | **F** | És justament el que permet: l'anàlisi de dominància es fa mirant aquesta columna per decidir on millorar. | 2_08_expressio_final.md |

<!-- FIN CAPÍTULO: 2_09_entrenament -->

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
| **(2.1)** | $\mathrm{error} \;=\; x_{\mathrm{mesurat}} \;-\; x_{\mathrm{veritable}}$ |
| **(2.2)** | $\bar{x}=\frac{1}{N}\sum_{i=1}^{N} x_i$ |
| **(2.3)** | $s^2=\frac{1}{N-1}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2$ |
| **(2.4)** | $s=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2}$ |
| **(2.5)** | $s_{\bar{x}}=\frac{s}{\sqrt{N}}$ |
| **(2.6)** | $u(y)=\sigma[Y]$ |
| **(2.7)** | $U=k\,u_c(y)$ |
| **(2.8)** | $y-U \;\leq\; q \;\leq\; y+U$ |
| **(2.9)** | $Y=f(X_1,X_2,\dots,X_N)$ |
| **(2.10)** | $L=L_m\left[1+\alpha\left(T-T_0\right)\right]$ |
| **(2.11)** | $\bar{x}=\frac{1}{N}\sum_{i=1}^{N} x_i$ |
| **(2.12)** | $s=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(x_i-\bar{x}\right)^2}$ |
| **(2.13)** | $u_A=\frac{s}{\sqrt{N}}$ |
| **(2.14)** | $\bar{X}=\frac{1}{N}\sum_{i=1}^{N} X_i$ |
| **(2.15)** | $\mathrm{Var}\!\left[\bar{X}\right]=\mathrm{Var}\!\left[\frac{1}{N}\sum_{i=1}^{N} X_i\right]$ |
| **(2.16)** | $\mathrm{Var}\!\left[\bar{X}\right]=\frac{1}{N^2}\,\mathrm{Var}\!\left[\sum_{i=1}^{N} X_i\right]$ |
| **(2.17)** | $\mathrm{Var}\!\left[\sum_{i=1}^{N} X_i\right]=\sum_{i=1}^{N}\mathrm{Var}\!\left[X_i\right]$ |
| **(2.18)** | $\mathrm{Var}\!\left[\sum_{i=1}^{N} X_i\right]=N\sigma^2$ |
| **(2.19)** | $\mathrm{Var}\!\left[\bar{X}\right]=\frac{1}{N^2}\,N\sigma^2=\frac{\sigma^2}{N}$ |
| **(2.20)** | $\sigma_{\bar{X}}=\frac{\sigma}{\sqrt{N}}$ |
| **(2.21)** | $u_A=\frac{s}{\sqrt{N}}$ |
| **(2.22)** | $u=\frac{a}{\sqrt{3}}$ |
| **(2.23)** | $u=\frac{a}{\sqrt{6}}$ |
| **(2.24)** | $u=\frac{U}{k}$ |
| **(2.25)** | $u=\frac{A}{\sqrt{2}}$ |
| **(2.26)** | $\Delta y \approx \sum_{i=1}^{N}\frac{\partial f}{\partial x_i}\,\Delta x_i$ |
| **(2.27)** | $c_i=\frac{\partial f}{\partial x_i}$ |
| **(2.28)** | $u_c^2(y)=\sum_{i=1}^{N} c_i^{\,2}\,u^2(x_i)$ |
| **(2.29)** | $u_c(y)=\sqrt{\sum_{i=1}^{N} c_i^{\,2}\,u^2(x_i)}$ |
| **(2.30)** | $u_c^2(y)=\sum_{i=1}^{N} c_i^{\,2}\,u^2(x_i)+2\sum_{i=1}^{N-1}\sum_{j=i+1}^{N} c_i\,c_j\,u(x_i,x_j)$ |
| **(2.31)** | $U=k\,u_c(y)$ |
| **(2.32)** | $Y=y\pm U$ |
| **(2.33)** | $\nu_{\text{ef}}=\frac{u_c^{\,4}(y)}{ \sum_{i=1}^{N}\frac{u_i^{\,4}}{\nu_i}}$ |
| **(2.34)** | $u_c(y)=\sqrt{\sum_{i=1}^{N}\left[\,c_i\,u(x_i)\,\right]^2}$ |