# U2·01 Concepte d'incertesa, la GUM i la diferència entre error i incertesa

## 📑 Índice de Contenidos

- [1 La definició d'incertesa segons la GUM](#1-la-definició-dincertesa-segons-la-gum)
- [2 Origen normatiu: per què calia estandarditzar el dubte](#2-origen-normatiu-per-què-calia-estandarditzar-el-dubte)
- [3 Error i incertesa: dos conceptes que no s'han de confondre](#3-error-i-incertesa-dos-conceptes-que-no-shan-de-confondre)
- [4 Per a què serveix calcular la incertesa](#4-per-a-què-serveix-calcular-la-incertesa)

---

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

[Índex de la unitat](2_00_index.md)[2. Marc teòric i definicions fonamentals →](2_02_marc_teoric.md)

---

## 📐 Formulario Resumen de Ecuaciones

| Nº / Ref | Expresión Matemática |
| :---: | :--- |
| **(2.1)** | $\mathrm{error} \;=\; x_{\mathrm{mesurat}} \;-\; x_{\mathrm{veritable}}$ |