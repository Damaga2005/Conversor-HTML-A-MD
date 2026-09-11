# 📚 Cuaderno Maestro: Tema 1

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 1` | 📄 **Capítulos incluidos:** 8  
> 📅 **Generado:** 2026-09-11 19:09

---

## 📑 Índice General del Cuaderno Maestro

1. [SM · Unitat 1 · Introducció als sistemes de mesura](#sm-unitat-1-introducció-als-sistemes-de-mesura)
   - [Presentació de la unitat](#presentació-de-la-unitat)
   - [Metodologia de treball](#metodologia-de-treball)
   - [Documents de la unitat](#documents-de-la-unitat)
2. [SM · Unitat 1 · 1. Concepte de mesura](#sm-unitat-1-1-concepte-de-mesura)
   - [1 Definició](#1-definició)
   - [2 Mesurar és comparar](#2-mesurar-és-comparar)
   - [3 Atributs d'objectes i esdeveniments](#3-atributs-dobjectes-i-esdeveniments)
   - [4 El resultat i la unitat](#4-el-resultat-i-la-unitat)
   - [5 Mesura directa i mesura indirecta](#5-mesura-directa-i-mesura-indirecta)
3. [SM · Unitat 1 · 2. El Sistema Internacional d'Unitats](#sm-unitat-1-2-el-sistema-internacional-dunitats)
   - [1 De l'artefacte a la constant](#1-de-lartefacte-a-la-constant)
   - [2 Unitats base](#2-unitats-base)
   - [3 Unitats derivades i coherència](#3-unitats-derivades-i-coherència)
   - [4 Les set constants](#4-les-set-constants)
   - [5 Prefixos](#5-prefixos)
   - [6 El Mars Climate Orbiter](#6-el-mars-climate-orbiter)
   - [▤ Annex de consulta](#annex-de-consulta)
4. [SM · Unitat 1 · 3. Estructura dels sistemes de mesura](#sm-unitat-1-3-estructura-dels-sistemes-de-mesura)
   - [1 Del mesurand al resultat](#1-del-mesurand-al-resultat)
   - [2 Adquisició i efecte de càrrega](#2-adquisició-i-efecte-de-càrrega)
   - [3 Condicionament](#3-condicionament)
   - [4 Conversió analògica-digital](#4-conversió-analògica-digital)
   - [5 Processament digital](#5-processament-digital)
   - [6 Presentació](#6-presentació)
5. [SM · Unitat 1 · 4. Sensors: definició i classificació](#sm-unitat-1-4-sensors-definició-i-classificació)
   - [1 Sensor, transductor i actuador](#1-sensor-transductor-i-actuador)
   - [2 Classificacions](#2-classificacions)
   - [3 Principis de transducció](#3-principis-de-transducció)
   - [4 Model elèctric](#4-model-elèctric)
   - [5 Sensibilitat creuada](#5-sensibilitat-creuada)
   - [6 Selecció](#6-selecció)
6. [SM · Unitat 1 · 5. Característiques estàtiques](#sm-unitat-1-5-característiques-estàtiques)
   - [1 Règim permanent i funció de resposta](#1-règim-permanent-i-funció-de-resposta)
   - [2 Sensibilitat i error de zero](#2-sensibilitat-i-error-de-zero)
   - [3 Error de linealitat](#3-error-de-linealitat)
   - [4 Exactitud, veracitat i fidelitat](#4-exactitud-veracitat-i-fidelitat)
   - [5 Errors sistemàtics i aleatoris](#5-errors-sistemàtics-i-aleatoris)
   - [6 Histèresi, zona morta i resolució](#6-histèresi-zona-morta-i-resolució)
7. [SM · Unitat 1 · 6. Característiques dinàmiques](#sm-unitat-1-6-característiques-dinàmiques)
   - [1 Quan el mesurand varia](#1-quan-el-mesurand-varia)
   - [2 Tres models](#2-tres-models)
   - [3 Resposta del sistema de primer ordre](#3-resposta-del-sistema-de-primer-ordre)
   - [4 Estimació de la constant de temps d'un primer ordre](#4-estimació-de-la-constant-de-temps-dun-primer-ordre)
   - [5 Una excepció](#5-una-excepció)
8. [SM · Unitat 1 · Entrenament](#sm-unitat-1-entrenament)
   - [Tria com vols entrenar](#tria-com-vols-entrenar)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: SM_U1_00_INDEX -->

# SM · Unitat 1 · Introducció als sistemes de mesura

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB

# Unitat 1 · Introducció als sistemes de mesura

Materials de treball previ. Sis documents, amb una dedicació estimada
d'**una hora** en conjunt.

## Presentació de la unitat

Mesurar no consisteix únicament a assignar un número a una magnitud: és l'operació que
estableix el vincle entre el món físic i les decisions tècniques que se'n deriven. Tot sistema
electrònic que interacciona amb el seu entorn —un control de procés industrial, un equip de
diagnòstic mèdic, un vehicle, una estació base— depèn de la qualitat amb què aquest vincle
s'ha establert. Aquesta unitat construeix el marc conceptual que la resta de l'assignatura
donarà per conegut.

El recorregut segueix una progressió deliberada, del concepte abstracte a la seva
quantificació experimental:

1. S'estableix **què és una mesura** i quines condicions ha de satisfer un
   procediment per merèixer aquest nom.
2. S'introdueix el **sistema de referència** —el SI— sense el qual la comparació
   que tota mesura implica no seria possible.
3. Es descriu la **realització física** d'aquesta operació: la cadena de blocs
   que transforma una magnitud física en informació utilitzable.
4. S'analitza el **component crític** de la cadena, el sensor, i els criteris
   que en governen la selecció.
5. Es defineixen els paràmetres que permeten **quantificar la qualitat** del
   sistema, primer en règim permanent i després en règim dinàmic.

> [!NOTE] **Relació amb la resta de l'assignatura**
>
> Les unitats posteriors s'organitzen segons el *model elèctric* del sensor —resistiu,
> capacitiu, inductiu, generador de tensió, de corrent o de càrrega— i estudien el circuit de
> condicionament corresponent a cadascun. Aquesta organització només té sentit un cop assumits
> els conceptes que es presenten aquí.
>
> El vocabulari d'aquesta unitat, per tant, no s'abandona en acabar-la: sensibilitat,
> linealitat, veracitat, fidelitat, error dinàmic o efecte de càrrega són termes que
> reapareixeran de manera constant al llarg del curs i en la pràctica professional posterior.

## Metodologia de treball

L'assignatura segueix una metodologia d'aula inversa. Les sessions presencials no es
dediquen a exposar aquests continguts, sinó a plantejar i resoldre **activitats
d'anàlisi sobre dades reals** que els pressuposen: detecció d'errors aberrants en
registres de temperatura, comparació de la veracitat i la fidelitat de dos instruments,
quantificació de la no-linealitat d'un termistor i caracterització de la resposta temporal
d'un sistema de mesura de pressió.

En conseqüència, **el treball previ d'aquests materials és un requisit d'entrada a la
sessió**, no un complement opcional. La dedicació prevista fora de l'aula és equivalent
a la presencial.

> [!IMPORTANT] **Abans de la primera sessió**
>
> Cal haver treballat els sis documents i haver resolt el **qüestionari de la unitat
> disponible a Atenea**. Les condicions de realització i el criteri de correcció
> s'explicaran el primer dia de classe.
>
> Es disposa com a mínim d'una setmana. Es recomana distribuir la lectura en diverses
> sessions curtes en lloc de concentrar-la: el rendiment de l'estudi distribuït és
> sensiblement superior al de l'estudi massiu per a un mateix temps total de dedicació.

## Documents de la unitat

[1

### Concepte de mesura

Estableix què és una mesura i quins requisits ha de complir. Introdueix la noció d'atribut, la distinció entre mesura directa i indirecta, i la necessitat de la unitat com a part inseparable del resultat.

- Definició de mesura: caràcter empíric, objectiu i representatiu
- Atributs d'objectes i esdeveniments
- Resultat de mesura i necessitat d'unitats
- Mesura directa i mesura indirecta

8 min](#sm-unitat-1-1-concepte-de-mesura)
[2

### El Sistema Internacional d'Unitats

Presenta el marc de referència sobre el qual es construeix tota comparació metrològica: les set unitats base, el mecanisme de derivació d'unitats i la redefinició de 2019 a partir de constants fonamentals.

- Motivació i evolució històrica del SI
- Magnituds base i magnituds derivades. Coherència
- Les set constants fonamentals com a base de les definicions
- Prefixos decimals i convencions de notació

11 min](#sm-unitat-1-2-el-sistema-internacional-dunitats)
[3

### Estructura dels sistemes de mesura

Descriu l'arquitectura funcional comuna a qualsevol instrument, bloc a bloc, i identifica on s'origina cada contribució d'error. Inclou el tractament dels models de processament com a part integrant del procés de mesura.

- Quantitat sota mesura, mesurand i soroll d'entrada
- Condicionament de senyal i transmissió
- Conversió A/D: mostreig, quantificació i aliàsing
- Processament digital i models de processament

13 min](#sm-unitat-1-3-estructura-dels-sistemes-de-mesura)
[4

### Sensors: definició i classificació

Analitza el component que efectua la transducció primària. Estudia quatre principis físics representatius, les limitacions que cap sensor no pot evitar, i els criteris de classificació que condicionen el disseny del circuit de lectura.

- Sensor, actuador i transductor
- Galga extensomètrica, sensor inductiu, efecte Hall i termoparell
- Sensibilitat creuada i efecte de càrrega
- Criteris de classificació i model elèctric

11 min](#sm-unitat-1-4-sensors-definició-i-classificació)
[5

### Característiques estàtiques

Defineix els paràmetres amb què s'especifica el comportament d'un sistema de mesura en règim permanent. Constitueix el vocabulari amb què la indústria descriu els seus productes als fulls de característiques.

- Funció de resposta i aproximació lineal
- Sensibilitat, error de zero i error de linealitat
- Exactitud, veracitat i fidelitat. Errors sistemàtics i aleatoris
- Histèresi, zona morta i resolució

12 min](#sm-unitat-1-5-característiques-estàtiques)
[6

### Característiques dinàmiques

Estudia el comportament del sistema quan el mesurand varia amb el temps. Introdueix els models d'ordre zero, primer i segon, l'error dinàmic i els mètodes experimentals d'estimació de la constant de temps.

- Models dinàmics bàsics i resposta freqüencial
- Error dinàmic davant esglaó i rampa
- Estimació experimental de la constant de temps

9 min](#sm-unitat-1-6-característiques-dinàmiques)

> [!NOTE] **Distribució recomanada**
>
>

| Sessió 1 | Documents 1 i 2 · Concepte de mesura i Sistema Internacional | 21 min |
|:--- |:--- |:--- |
| Sessió 2 | Documents 3 i 4 · Estructura del sistema i sensors | 24 min |
| Sessió 3 | Documents 5 i 6 · Caracterització estàtica i dinàmica | 21 min |
| Sessió 4 | Repàs i resolució del qüestionari | — |

>
> Distribució orientativa. Repartir la lectura en diverses sessions separades
> per un dia o més és preferible a concentrar-la: la represa obliga a recuperar el que s'havia
> llegit, i aquest esforç de recuperació és el que consolida la retenció.

> [!TIP] **Entrenament**
>
> A la mateixa carpeta hi ha la pàgina [**Entrenament**](#sm-unitat-1-entrenament),
> amb 50 afirmacions vertader/fals sobre els sis documents. Totes dues modalitats presenten les 50 senceres:
> un simulacre cronometrat de 25 minuts, en ordre aleatori i amb correcció al final, i un entrenament lliure
> sense cronòmetre i amb resposta immediata. En corregir, cada afirmació mostra la justificació i enllaça amb
> el document que la sustenta.
>
> No es lliura ni es puntua: serveix per comprovar si els continguts s'han entès.

> [!TIP] **Com treballar aquests materials**
>
> Els documents estan escrits en **format dens**: definicions, relacions clau,
> taules i llistes. Cada concepte hi apareix una sola vegada i amb l'extensió mínima necessària,
> de manera que **no hi ha text de farciment que es pugui llegir en diagonal**. Convé
> llegir-los a poc a poc i tornar enrere quan calgui, més que no pas de pressa una sola vegada.
>
> Diversos documents contenen **exercicis resolts pas a pas**, presentats de
> manera que es pugui intentar cada pas abans de consultar-ne la solució. S'aconsella fer-ho:
> llegir una resolució ja feta produeix una sensació de comprensió que sovint no es correspon
> amb la capacitat de reproduir-la.
>
> Al llarg del text hi ha **referències creuades a les unitats posteriors**.
> Assenyalen on es reprendrà cada qüestió amb més profunditat i no cal consultar-les ara.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC

Unitat 1 · Materials de treball previ · Curs 2026-T

<!-- FIN CAPÍTULO: SM_U1_00_INDEX -->

---

<!-- INICIO CAPÍTULO: SM_U1_01_Concepte_de_mesura -->

# SM · Unitat 1 · 1. Concepte de mesura

[← Índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura)
1[2](SM_U1_02_El_Sistema_Internacional_dUnitats.md "El Sistema Internacional d'Unitats")[3](SM_U1_03_Estructura_dels_sistemes_de_mesura.md "Estructura dels sistemes de mesura")[4](SM_U1_04_Sensors_definicio_i_classificacio.md "Sensors: definició i classificació")[5](SM_U1_05_Caracteristiques_estatiques.md "Característiques estàtiques")[6](SM_U1_06_Caracteristiques_dinamiques.md "Característiques dinàmiques")

Sistemes de Mesura · Unitat 1 · Document 1 de 6

# Concepte de mesura

Dedicació estimada: 9 minuts

> [!NOTE] **Objectius**
>
> 1. Enunciar la definició de mesura i el paper dels seus tres requisits.
> 2. Distingir objecte i atribut, i justificar l'elecció de l'atribut com a decisió de disseny.
> 3. Justificar per què el resultat és inseparable de la unitat.
> 4. Classificar una mesura com a directa o indirecta i relacionar-ho amb la incertesa.

## 1 Definició

Una **mesura** és el resultat d'assignar un nombre a un **atribut** d'un objecte o d'un esdeveniment d'una manera **empírica**, **objectiva** i **representativa**. Cada requisit exclou una família de procediments que superficialment ho semblarien.

- **Empírica**: Fonamentada en l'observació del món real i en la comparació amb un artefacte o procés de referència. Un valor obtingut només per simulació, per exacte que sigui el model, és una predicció i no una mesura.
- **Objectiva**: El resultat depèn del procediment i dels instruments, no de qui mesura. Dos operadors amb el mateix protocol i instruments calibrats han d'obtenir resultats compatibles.
- **Representativa**: L'assignació ha de reflectir les relacions reals entre objectes: si un edifici és més alt, el seu nombre ha de ser més gran. Es defineix respecte d'un atribut concret, no en absolut.

> [!IMPORTANT]
>
> L'objectivitat **no** implica correcció. Un procediment pot ser perfectament objectiu i sistemàticament erroni: els errors que tingui no depenen de l'opinió de l'observador, però hi són. Es formalitza al document 5 amb la veracitat i la fidelitat.

## 2 Mesurar és comparar

Dir que una longitud és 42,3 m significa que conté 42,3 vegades el patró «metre». **El nombre sol no té significat**: només l'adquireix amb la unitat de comparació, qüestió que ocupa el document 2.

D'aquí que s'accepti l'existència d'error. L'atribut existeix al marge del sistema de mesura, que només n'ofereix una aproximació. **Una mesura no és el valor veritable**, sinó un resultat que aspira a estar-hi prou a prop per a la decisió que s'ha de prendre.

> [!TIP] **Les tres preguntes**
>
> 1. **Què es mesura exactament?** Quin atribut, sobre quin objecte o esdeveniment.
> 2. **Amb què es compara?** Quina referència o unitat s'adopta.
> 3. **Quines garanties hi ha** que l'assignació sigui empírica, objectiva i representativa dins d'uns límits acceptables?

## 3 Atributs d'objectes i esdeveniments

Es mesuren **atributs, no objectes**. Un mateix objecte admet moltes mesures segons el context: massa, volum, densitat, color, temperatura, rugositat, rigidesa, conductivitat elèctrica.

![Fotografia d'una poma vermella envoltada de línies de mesura, escales graduades i cercles concèntrics que suggereixen les diferents magnituds que se'n poden quantificar.](assets/SM_U1_01_Concepte_de_mesura_img_1.jpg)

*Figura: Figura 1.1 — Un mateix objecte admet mesures de naturalesa diferent.*

Els atributs es poden ordenar per complexitat de mesura. La **massa** es compara directament amb un patró. El **volum** admet procediments diferents —desplaçament de líquid, escaneig geomètric— que mesuren el mateix atribut amb avantatges distints. La **densitat** no es mesura: es calcula a partir de massa i volum. El **color** exigeix decidir prèviament quin model el representa.

El resultat no ha de ser necessàriament un únic escalar. Una càmera calibrada produeix una mesura formada per **molts valors organitzats en píxels**, cadascun amb el seu triplet de components de color: el concepte de mesura s'estén a col·leccions de nombres organitzats.

El raonament val igual per a **esdeveniments**. De la transmissió d'un paquet se'n poden mesurar el retard, la seva variació —el *jitter*—, la taxa d'error de bits, la potència rebuda o la transferència efectiva.

> [!TIP]
>
> **L'elecció de l'atribut és una decisió de disseny** que condiciona tota l'arquitectura del sistema: determina el sensor, el condicionament, el processament i el significat del resultat. Un sistema de mesura és sempre una proposta parcial sobre el món.

## 4 El resultat i la unitat

El resultat s'expressa com una **parella de nombre i unitat**, i els dos elements són inseparables: el nombre sense unitat no té context, i la unitat sense nombre no conté informació quantitativa. El resultat complet respon a tres coses: *quant* (el nombre), *de què* (la unitat i el sistema de referència) i *amb quina confiança* (la incertesa, que s'aborda a la **unitat 2**).

> [!IMPORTANT]
>
> Les unitats implícites en programari són una font documentada d'errors silenciosos. Una variable anomenada `temp` amb valor 298 pot contenir graus Celsius, kelvins o una codificació del fabricant. El cas del document 2 mostra què costa aquesta ambigüitat.

Per adaptar-se a l'ordre de magnitud s'utilitzen múltiples i submúltiples, i per no atribuir al resultat més precisió de la que té s'apliquen les **xifres significatives**: el resultat d'un producte o d'un quocient no en pot tenir més que el factor que menys en té. És una regla pràctica; el tractament rigorós és la propagació d'incerteses de la **unitat 2**.

> [!EXAMPLE] **Exercici resolt — Xifres significatives en una mesura indirecta**
>
> Un voltímetre indica 12,45 V i un amperímetre 0,842 A sobre la mateixa càrrega. Es demana la potència.
>
> <details>
> <summary><b>🔍 Desplegar Resolució</b></summary>
>
> El càlcul directe dona $P$ = 12,45 × 0,842 = 10,4829 W.
>
> El factor amb menys xifres significatives és 0,842, amb tres. El resultat s'ha d'expressar, doncs, com **10,5 W**. Escriure 10,4829 W atribuiria a la mesura una precisió que els instruments no tenen.
>
> </details>

## 5 Mesura directa i mesura indirecta

El criteri adoptat en aquesta assignatura es defineix **des del punt de vista de l'usuari**:

- **Mesura directa**: S'obté per comparació immediata amb una referència i proporciona el valor final sense càlculs explícits per part de l'usuari. Llegir 12,6 V en un multímetre o la massa en una bàscula calibrada.
- **Mesura indirecta**: S'obté combinant matemàticament una o més mesures directes. Calcular $P$ = $V$ · $I$, o la densitat a partir de massa i volum.

$$
P = V \cdot I \qquad (1.1)
$$

Que el multímetre faci internament mostreig, conversió A/D i visualització no altera la classificació: per a l'usuari el procés és directe. **La classificació no és una propietat de la magnitud sinó del procediment**: amb un wattímetre, la potència passaria a ser directa. Un ohmímetre que injecta un corrent i mesura la tensió és directe per a l'usuari i indirecte per al dissenyador, que ha de conèixer la incertesa de totes dues etapes.

També és indirecta la **mitjana** de  $N$  lectures repetides per reduir el soroll aleatori, perquè s'obté aplicant un algoritme a un conjunt de dades primàries.

> [!TIP]
>
> La distinció és crucial per a la **incertesa**. En una mesura directa prové de l'instrument; en una d'indirecta cal aplicar la llei de propagació d'incerteses (**unitat 2**) per veure com es combinen els errors de cada variable d'entrada.
>
> En una mesura indirecta **la fórmula forma part del procés de mesura**: la qualitat del resultat depèn tant de les mesures d'entrada com de la **validesa de la fórmula** i del model matemàtic emprats. Un model inadequat produeix un resultat erroni encara que totes les mesures directes siguin impecables, i unes dades d'entrada incorrectes es propaguen al resultat per correcta que sigui la fórmula.
>
> Una mesura indirecta pot tenir una incertesa **menor o major** que les que la componen, segons l'estructura de la relació i la correlació entre variables: les mitjanes redueixen la component aleatòria, els productes tendeixen a acumular-la.

> [!TIP] **Síntesi**
>
> 1. Mesura = assignar un nombre a un atribut de manera **empírica, objectiva i representativa**.
> 2. Objectivitat ≠ correcció: un procediment objectiu pot ser sistemàticament erroni.
> 3. Es mesuren **atributs**, no objectes; triar l'atribut és una decisió de disseny.
> 4. El resultat és **nombre + unitat**, i les xifres significatives no han d'excedir les del factor més pobre.
> 5. **Directa** = sense càlculs per a l'usuari; **indirecta** = combinació de mesures directes. És una propietat del procediment, no de la magnitud.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC

Unitat 1 · Document 1 de 6 · Materials de treball previ · Curs 2026-T

---
[← Tornar Índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura) • [Document 2 → El Sistema Internacional d'Unitats](#sm-unitat-1-2-el-sistema-internacional-dunitats)

---

<!-- FIN CAPÍTULO: SM_U1_01_Concepte_de_mesura -->

---

<!-- INICIO CAPÍTULO: SM_U1_02_El_Sistema_Internacional_dUnitats -->

# SM · Unitat 1 · 2. El Sistema Internacional d'Unitats

[← Índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura)
[1](SM_U1_01_Concepte_de_mesura.md "Concepte de mesura")2[3](SM_U1_03_Estructura_dels_sistemes_de_mesura.md "Estructura dels sistemes de mesura")[4](SM_U1_04_Sensors_definicio_i_classificacio.md "Sensors: definició i classificació")[5](SM_U1_05_Caracteristiques_estatiques.md "Característiques estàtiques")[6](SM_U1_06_Caracteristiques_dinamiques.md "Característiques dinàmiques")

Sistemes de Mesura · Unitat 1 · Document 2 de 6

# El Sistema Internacional d'Unitats

Dedicació estimada: 9 minuts

> [!NOTE] **Objectius**
>
> 1. Enumerar les set unitats base i les particularitats del quilogram, l'ampere i el kelvin.
> 2. Explicar què vol dir que el SI sigui *coherent*.
> 3. Descriure la lògica de la redefinició de 2019.
> 4. Aplicar les regles de notació i d'ús de prefixos.
> 5. Argumentar per què documentar les unitats a les interfícies és una exigència de disseny.

## 1 De l'artefacte a la constant

Com que tota mesura és una comparació, cal un acord universal sobre les referències. El **SI** no és una llista de símbols: és una estructura coherent que connecta les magnituds entre elles i les ancora a constants fonamentals.

Les unitats antigues derivaven de l'anatomia humana i patien de **variabilitat**. El **Sistema Mètric Decimal** (1799) va introduir dos principis: **decimalització** —tots els múltiples són potències de deu— i **referències naturals** —el metre com a fracció del meridià, el quilogram com la massa d'un decímetre cúbic d'aigua. Per fer-lo pràctic es van fabricar **artefactes** de platí, i la **Convenció del Metre** (1875) va crear el BIPM per vetllar per la uniformitat mundial. El nom «Sistema Internacional d'Unitats» data de **1960**.

> [!IMPORTANT]
>
> Els artefactes no eren prou estables: podien canviar amb la temperatura, envellir, guanyar o perdre àtoms, i si es destruïen la unitat es perdia. Per això es van substituir progressivament per fenòmens físics invariants. El **1983** es va fixar la velocitat de la llum com a valor exacte i el metre va passar a dependre del segon.

La reforma final va entrar en vigor el **20 de maig de 2019**: s'abandona tota referència a objectes materials i el SI es defineix fixant el valor numèric exacte de **set constants fonamentals**. Un quilogram ja no és un cilindre sinó la massa necessària perquè la constant de Planck valgui exactament el valor fixat. **L'estàndard ha passat de la caixa forta a les lleis de la física.**

## 2 Unitats base

| Magnitud base | Unitat | Símbol |
|:--- |:--- |:--- |
| Longitud | metre | m |
| Massa | quilogram | kg |
| Temps | segon | s |
| Corrent elèctric | ampere | A |
| Temperatura termodinàmica | kelvin | K |
| Quantitat de substància | mol | mol |
| Intensitat lluminosa | candela | cd |

**Taula 1.1 — Les set unitats base.** Convé conèixer-les de memòria.

- El **quilogram** és l'única unitat base que **incorpora un prefix al nom**. La unitat base és el quilogram i no el gram, cosa que indueix errors de càlcul.
- L'**ampere** connecta el món mecànic amb l'elèctric. El SI va triar el corrent com a base i no la càrrega ni la tensió, per raons pràctiques de realització; des de 2019 es defineix comptant càrregues elementals.
- El **kelvin** és la temperatura termodinàmica. El grau Celsius és una unitat derivada acceptada, però les equacions termodinàmiques rigoroses exigeixen kelvins —per exemple el soroll tèrmic d'una resistència, a la **unitat 4**. La denominació correcta és *kelvin*, mai «grau Kelvin».
- El **mol** compta entitats elementals i connecta el món macroscòpic amb el microscòpic. És essencial en semiconductors i sensors electroquímics.
- La **candela** és l'única unitat base que depèn de la **percepció humana**: pondera la sensibilitat de l'ull als colors. Per això en enginyeria sovint es prefereixen unitats radiomètriques, purament energètiques.

> [!IMPORTANT] **Notació**
>
> - Els **noms** van sempre en minúscula: metre, newton, ampere.
> - Els **símbols** van en minúscula (m, s, kg) excepte si la unitat prové d'un nom propi: A d'Ampère, K de Kelvin, V de Volta, N de Newton.
> - El **litre** admet L i l, excepció tolerada per evitar confondre la ela amb el número u.
>
> No és estil: permet distingir el prefix «m» de mil·li de la unitat «m» de metre.

## 3 Unitats derivades i coherència

Una unitat derivada es forma amb **productes i potències de les unitats base, sense cap factor numèric**. Aquesta propietat és la **coherència**.

> [!TIP]
>
> Gràcies a la coherència, si s'introdueixen valors en unitats coherents en una fórmula física correcta, el resultat surt en la unitat coherent corresponent **sense factors de conversió**. Al sistema imperial, passar de cavalls a lliures-peu per segon exigeix multiplicar per 550, i cada factor és una oportunitat d'error.

Una mateixa unitat derivada admet expressions equivalents: el **volt** és W/A o J/C; l'**ohm** és V/A i el **siemens**, el seu invers, és A/V —el primer mesura resistència i el segon conductància, de manera que no són comparables en magnitud sinó recíprocs. Els noms propis simplifiquen la comunicació: un ampere-segon per volt és un **farad**, un newton-metre un **joule**, un invers de segon un **hertz**.

Dues unitats derivades són adimensionals però conserven nom propi: el **radian** (angle pla, arc dividit per radi), imprescindible per distingir la freqüència angular en rad/s de la freqüència en Hz —un factor 2π omès té conseqüències greus—, i l'**estereoradian** (angle sòlid), important en fotometria i en el guany directiu d'antenes.

La llista d'unitats derivades és a l'[annex](#annex).

## 4 Les set constants

| Constant | Valor fixat | Defineix |
|:--- |:--- |:--- |
| Δ $\nu_{\text{Cs}}$  · transició hiperfina del cesi-133 | 9 192 631 770 Hz | segon |
| $c$  · velocitat de la llum en el buit | 299 792 458 m/s | metre |
| $h$  · constant de Planck | 6,626 070 15 × $10^{-34}$ J·s | quilogram |
| $e$  · càrrega elemental | 1,602 176 634 × $10^{-19}$ C | ampere |
| $k_{B}$  · constant de Boltzmann | 1,380 649 × $10^{-23}$ J/K | kelvin |
| $N_{A}$  · constant d'Avogadro | 6,022 140 76 × $10^{23}$ $mol^{-1}$ | mol |
| $K_{\text{cd}}$  · eficàcia lluminosa a 540 THz | 683 lm/W | candela |

> [!TIP]
>
> L'enfocament **inverteix la lògica tradicional**: abans es tenia un metre patró i es mesurava la velocitat de la llum; ara es fixa la velocitat de la llum i se'n dedueix el metre.

- **Segon**: 9 192 631 770 períodes de la transició entre els dos nivells hiperfins de l'estat fonamental del cesi-133. És la base del GPS i de la sincronització de xarxes.
- **Metre**: el que recorre la llum en 1/299 792 458 s. Deriva del segon.
- **Quilogram**: es realitza amb la balança de Kibbletambé anomenada balança de Watt, que compara potència mecànica i elèctrica; com que la potència elèctrica es mesura amb l'efecte Josephson i l'efecte Hall quàntic, tots dos dependents de  $h$  i  $e$, la massa queda lligada a la constant de Planck.
- **Ampere**: flux d'un nombre determinat de càrregues elementals per segon, molt més intuïtiu que l'antiga definició per forces entre conductors.
- **Kelvin**: es fixa l'energia tèrmica equivalent  $k_{B}$  $T$, cosa que elimina la dependència del punt triple de l'aigua.

![Diagrama de cercles de colors on les set constants fonamentals apunten mitjançant fletxes cap a les set unitats base, amb fletxes creuades que indiquen les dependències mútues.](assets/SM_U1_02_El_Sistema_Internacional_dUnitats_img_1.png)

*Figura: Figura 1.2 — Constants fonamentals i unitats base. Cada constant defineix una unitat, però les unitats també depenen entre elles.*

La interconnexió fa el sistema robust: una mesura de massa d'alta precisió empra implícitament la freqüència del cesi i la constant de Planck. **El SI ha deixat de ser una col·lecció de patrons independents per ser una xarxa de constants.**

## 5 Prefixos

En electrònica es treballa amb rangs enormes —de picowatts a gigahertzs— i escriure zeros indueix errors de lectura. Els **prefixos decimals** multipliquen la unitat per potències de deu. El 2022 s'hi van afegir **ronna** i **quetta** per als valors grans i **ronto** i **quecto** per als petits, perquè yotta i yocto s'havien quedat curts. La taula completa és a l'[annex](#annex).

> [!IMPORTANT] **Normes**
>
> - **Cap prefix en cascada.** Mai «milimicrofarad»: és nanofarad (nF).
> - **Excepció del quilogram.** Els prefixos s'apliquen al gram: $10^{-6}$ kg és un mil·ligram, no un «microquilogram».
> - **Preferents** els prefixos que són potències de mil. Hecto, deca, deci i centi es desaconsellen en context tècnic, tret d'àrees consolidades com els decibels.
> - **Elecció:** triar el prefix perquè el valor quedi entre **0,1 i 1000**.
>
> El criteri operatiu és la **llegibilitat**: «10 nF» es classifica mentalment a l'instant; «0,00000001 F» obliga a comptar zeros, i cada aturada és una oportunitat d'error.

## 6 El Mars Climate Orbiter

La sonda de la NASA, llançada el desembre de 1998, havia d'inserir-se en òrbita marciana a **226 km** d'altitud. El 23 de setembre de 1999 va passar a **57 km** i es va desintegrar per estrès tèrmic i mecànic.

> [!IMPORTANT]
>
> **Lockheed Martin**, el contractista, lliurava l'impuls dels propulsors en **lliures-força segon**. El programari de navegació del **Jet Propulsion Laboratory** el llegia assumint **newton segon**. El factor entre les dues unitats és 4,45, de manera que cada correcció de rumb es va subestimar per aquest factor durant mesos. Cost: **327,6 milions de dòlars**.

> [!TIP] **Tres principis**
>
> 1. **La unitat és part de la dada.** No s'ha de transmetre, emmagatzemar ni processar mai un número sense certesa absoluta sobre la seva unitat.
> 2. **El risc és a les interfícies.** Els dos programaris eren internament correctes; l'error va passar a la frontera entre subsistemes.
> 3. **Cal verificació d'extrem a extrem.** Hi va haver senyals d'alerta, però sense comprovacions creuades d'unitats no es van interpretar.

> [!TIP] **Síntesi**
>
> 1. **Set unitats base.** El quilogram és l'anomalia: única amb prefix al nom.
> 2. **Coherència** = unitats derivades sense factors numèrics, i per tant sense conversions internes.
> 3. Des de **2019** el SI fixa set **constants fonamentals** en lloc de conservar objectes.
> 4. Notació i prefixos són eines de **prevenció d'errors**, no convencions estètiques.
> 5. El punt crític d'un sistema complex és la **interfície entre subsistemes**.

## ▤ Annex de consulta

| Magnitud | Unitat | Símbol | En unitats base |
|:--- |:--- |:--- |:--- |
| Freqüència | hertz | Hz | $s^{-1}$ |
| Força | newton | N | m·kg·$s^{-2}$ |
| Pressió, tensió mecànica | pascal | Pa | $m^{-1}$·kg·$s^{-2}$ |
| Energia, treball, calor | joule | J | $m^{2}$·kg·$s^{-2}$ |
| Potència | watt | W | $m^{2}$·kg·$s^{-3}$ |
| Angle pla / angle sòlid | radian / estereoradian | rad / sr | 1 (adimensional) |
| Càrrega elèctrica | coulomb | C | s·A |
| Tensió | volt | V | $m^{2}$·kg·$s^{-3}$·$A^{-1}$ |
| Capacitat | farad | F | $m^{-2}$·$kg^{-1}$·$s^{4}$·$A^{2}$ |
| Resistència | ohm | Ω | $m^{2}$·kg·$s^{-3}$·$A^{-2}$ |
| Conductància | siemens | S | $m^{-2}$·$kg^{-1}$·$s^{3}$·$A^{2}$ |
| Flux magnètic | weber | Wb | $m^{2}$·kg·$s^{-2}$·$A^{-1}$ |
| Densitat de flux magnètic | tesla | T | kg·$s^{-2}$·$A^{-1}$ |
| Inductància | henry | H | $m^{2}$·kg·$s^{-2}$·$A^{-2}$ |
| Temperatura Celsius | grau Celsius | °C | K (amb desplaçament) |
| Flux lluminós / il·luminància | lumen / lux | lm / lx | cd·sr / $m^{-2}$·cd |

**Taula 1.2 — Unitats derivades amb nom propi.**

| Factor | Nom | Símbol | Factor | Nom | Símbol |
|:--- |:--- |:--- |:--- |:--- |:--- |
| $10^{1}$ | deca | da | $10^{-1}$ | deci | d |
| $10^{2}$ | hecto | h | $10^{-2}$ | centi | c |
| $10^{3}$ | quilo | k | $10^{-3}$ | mil·li | m |
| $10^{6}$ | mega | M | $10^{-6}$ | micro | µ |
| $10^{9}$ | giga | G | $10^{-9}$ | nano | n |
| $10^{12}$ | tera | T | $10^{-12}$ | pico | p |
| $10^{15}$ | peta | P | $10^{-15}$ | femto | f |
| $10^{18}$ | exa | E | $10^{-18}$ | atto | a |
| $10^{21}$ | zetta | Z | $10^{-21}$ | zepto | z |
| $10^{24}$ | yotta | Y | $10^{-24}$ | yocto | y |
| $10^{27}$ | ronna | R | $10^{-27}$ | ronto | r |
| $10^{30}$ | quetta | Q | $10^{-30}$ | quecto | q |

**Taula 1.3 — Prefixos del SI.** Ressaltats, els més freqüents en electrònica.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC

Unitat 1 · Document 2 de 6 · Materials de treball previ · Curs 2026-T

---
[← Document 1 Concepte de mesura](#sm-unitat-1-1-concepte-de-mesura) • [Document 3 → Estructura dels sistemes de mesura](#sm-unitat-1-3-estructura-dels-sistemes-de-mesura)

<!-- FIN CAPÍTULO: SM_U1_02_El_Sistema_Internacional_dUnitats -->

---

<!-- INICIO CAPÍTULO: SM_U1_03_Estructura_dels_sistemes_de_mesura -->

# SM · Unitat 1 · 3. Estructura dels sistemes de mesura

[← Índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura)
[1](SM_U1_01_Concepte_de_mesura.md "Concepte de mesura")[2](SM_U1_02_El_Sistema_Internacional_dUnitats.md "El Sistema Internacional d'Unitats")3[4](SM_U1_04_Sensors_definicio_i_classificacio.md "Sensors: definició i classificació")[5](SM_U1_05_Caracteristiques_estatiques.md "Característiques estàtiques")[6](SM_U1_06_Caracteristiques_dinamiques.md "Característiques dinàmiques")

Sistemes de Mesura · Unitat 1 · Document 3 de 6

# Estructura dels sistemes de mesura

Dedicació estimada: 13 minuts

> [!NOTE] **Objectius**
>
> 1. Distingir mesurand i quantitat sota mesura.
> 2. Identificar les etapes del sistema i la funció de cadascuna.
> 3. Explicar l'efecte de càrrega i com es minimitza.
> 4. Aplicar el criteri de Nyquist i relacionar l'aliàsing amb el filtratge previ.
> 5. Calcular la resolució d'un ADC.
> 6. Comparar models de processament explícits i basats en aprenentatge.

## 1 Del mesurand al resultat

Un **sistema de mesura** transforma una magnitud del món real en una dada útil per decidir. **Cada etapa hi afegeix el seu error**: un sensor excel·lent amb un condicionament deficient dona mesures deficients, i un convertidor de setze bits no aporta res si el senyal ja porta soroll a partir del vuitè.

- **Mesurand**: La magnitud que es vol conèixer, definida amb prou precisió. No n'hi ha prou de dir «temperatura»: cal dir de quin element, en quin punt i en quines condicions.
- **Quantitat sota mesura**: L'atribut físic que el sistema realment detecta. És allò a què el sensor és sensible i, en general, no coincideix amb el mesurand.

Si es vol la temperatura del nucli d'un component i el sensor és a l'encapsulat, entre l'una i l'altra hi ha una resistència tèrmica: la diferència no és soroll, és un **error sistemàtic** derivat del muntatge. Molts errors greus no vénen d'instruments defectuosos sinó d'una **identificació incorrecta del mesurand**: un instrument perfecte que mesura amb exactitud la magnitud equivocada és inservible.

![Diagrama de blocs en cadena: el mesurand entra al sensor, segueix el condicionament, el convertidor analògic-digital, el processament digital i finalment la presentació o l'actuació.](assets/SM_U1_03_Estructura_dels_sistemes_de_mesura_img_1.png)

*Figura: Figura 1.3 — Estructura general. Cada bloc transforma el senyal i hi afegeix la seva contribució d'error.*

1. **Adquisició.** El sensor interacciona amb el mesurand i en produeix una representació elèctrica.
2. **Condicionament.** S'adapta el senyal a l'etapa següent.
3. **Conversió.** Mostreig i quantificació.
4. **Processament.** Escalat, correcció, filtratge, càlculs derivats.
5. **Presentació.** Operador, emmagatzematge o llaç de control.

No tots els sistemes tenen les cinc etapes explícites i sovint s'integren en un sol component, però l'esquema serveix com a marc d'anàlisi.

## 2 Adquisició i efecte de càrrega

A l'adquisició es produeix la **transducció**, objecte del document 4. Aquí interessa que **tota mesura pertorba el sistema mesurat**: és l'**efecte de càrrega**, conseqüència inevitable d'haver d'extreure energia o informació del sistema.

- Un voltímetre de resistència d'entrada finita sobre un circuit d'alta impedància forma un divisor amb la font i llegeix menys tensió de la que hi havia.
- Un termoparell de massa considerable en un volum petit de líquid n'absorbeix calor i altera la temperatura que acaba mesurant.

No s'elimina, però es minimitza: el sensor ha d'intercanviar **la mínima energia possible** —impedància d'entrada alta per mesurar tensió, baixa per mesurar corrent, massa tèrmica reduïda per mesurar temperatura.

> [!TIP]
>
> Quan no n'hi ha prou, la segona estratègia és **caracteritzar l'efecte i corregir-lo**. **Un error conegut i quantificat és molt menys perillós que un error petit però ignorat**: el primer es corregeix, el segon es propaga fins a la decisió final.

## 3 Condicionament

El senyal del sensor rarament és utilitzable: pot ser de nivell molt baix —desenes de microvolts en un termoparell—, tenir impedància inadequada, portar mode comú elevat o soroll.

- **Amplificació.** Aprofitar tot el marge de l'etapa següent. Els amplificadors d'instrumentació, coneguts de circuits i sistemes electrònics, es reprenen a la **unitat 6**.
- **Adaptació d'impedàncies** i **filtratge** de components que no són informació útil.
- **Excitació.** Els sensors moduladors modifiquen una propietat elèctrica i no generen energia: necessiten una font externa, i **la seva estabilitat determina l'estabilitat de la mesura**.
- **Linealització analògica**, avui sovint traslladada al domini digital.

### 3.1 · Pont de Wheatstone

Una galga extensomètrica canvia de resistència un 0,1 % del valor nominal, i mesurar-ho directament exigiria resoldre parts per milió sobre un fons molt més gran. El **pont de Wheatstone** —quatre resistències amb sortida nul·la en equilibri— fa que el senyal útil sigui el **desequilibri** i no el valor absolut, cosa que permet amplificar amb guany elevat sense saturar. A més, si totes les resistències són a la mateixa temperatura, **les derives tèrmiques es compensen mútuament**. Les configuracions de quart, mig i pont complet són de la **unitat 6**.

### 3.2 · Llaç de 4-20 mA i alternativa 0-10 V

En instrumentació industrial el senyal es transmet sovint com un **llaç de corrent de 4-20 mA**, amb el mínim del mesurand a 4 mA. Tres avantatges:

1. **Immunitat a la caiguda de tensió**: el corrent en un llaç sèrie és el mateix a tot arreu i la resistència del cable no altera el valor.
2. **Detecció d'avaries**: com que el zero és 4 mA, una lectura de 0 mA indica llaç obert. Un senyal de 0-20 mA no distingiria un mesurand nul d'una **avaria**.
3. **Alimentació pel mateix parell**: els 4 mA de repòs alimenten el transmissor, cosa que permet instal·lacions de dos fils.

L'alternativa és la transmissió en **tensió de 0-10 V**, més senzilla i econòmica, adequada en **distàncies curtes** i entorns benignes, però sense cap de les tres garanties: la caiguda al cable degrada el valor en trajectes llargs i 0 V és ambigu entre mesurand nul i cable tallat.

Convé recordar que **els cables i els connectors formen part del sistema de mesura**: resistència de contacte, unions dissimilars, acoblament capacitiu i moviment mecànic introdueixen errors de transmissió que poden superar els del sensor.

## 4 Conversió analògica-digital

El **convertidor analògic-digital** (ADC) implica dues discretitzacions independents.

### 4.1 · Mostreig i Nyquist

El **mostreig** discretitza el **temps**: el senyal s'avalua cada **període de mostreig**  $T_{s}$, i la **freqüència de mostreig** n'és la inversa.

$$
f_{s} = 1 / T_{s} \qquad (1.2)
$$

El teorema del mostreig, conegut de senyals i sistemes, estableix que si el senyal té contingut fins a  $f_{\max}$, les mostres el determinen completament sempre que

$$
f_{s} > 2f_{\text{\max}} \qquad (1.3)
$$

> [!IMPORTANT]
>
> Conviuen dues convencions. La **freqüència de Nyquist** designa habitualment  $f_{s}$ /2, és a dir **la meitat de la freqüència de mostreig**; la **taxa de Nyquist** designa 2 $f_{\max}$. En aquesta assignatura s'adopta la primera:  $f_{N}$  =  $f_{s}$ /2.

Els components per sobre de  $f_{s}$ /2 no desapareixen: queden **plegats** sobre la banda útil com a components de freqüència més baixa. És l'**aliàsing**, i un component així es diu **aliasat**.

> [!TIP]
>
> L'aliàsing **és irreversible**: un cop preses les mostres, un component aliasat no és separable del contingut genuí. La informació no està degradada, està destruïda.
>
> Per això cal un **filtre antialiàsing analògic** situat necessàriament **abans** del convertidor. Un filtre digital posterior elimina banda alta però no desfà un plegament ja produït.

### 4.2 · Quantificació i resolució

La **quantificació** discretitza l'**amplitud**. Per a  $n$  bits i fons d'escala  $V_{\text{FE}}$, hi ha $2^{n}$ nivells i la **resolució** val

$$
q = V_{\text{FE}} / 2^{n} \qquad (1.4)
$$

L'**error de quantificació** està acotat per ± $q$ /2: a diferència de l'aliàsing, és predictible. **Augmentar bits no millora indefinidament**: si el soroll del senyal supera  $q$, els bits inferiors només codifiquen soroll. I resolució no és exactitud: un convertidor pot resoldre molt fi i tenir un error sistemàtic considerable (document 5).

> [!EXAMPLE] **Exercici resolt — Dimensionament d'una cadena d'adquisició**
>
> Un sensor de pressió lliura 0-5 V per a 0-10 bar, amb components fins a 400 Hz i 2 mV de soroll eficaç.
>
> <details>
> <summary><b>🔍 Desplegar Resolució</b></summary>
>
> **Mostreig.** Nyquist exigeix $f_{s}$ > 800 Hz; amb el marge habitual de dues a cinc vegades —els filtres reals no tallen abruptament— s'adopten **2 kHz**.
>
> **Bits.** No té sentit resoldre per sota del soroll: 5 / 0,002 ≈ 2500 nivells distingibles, poc més d'11 bits. Amb **12 bits**, $q$ = 5/4096 = 1,22 mV, del mateix ordre que el soroll. Amb 16 bits, $q$ = 76 µV i els quatre bits inferiors només serien soroll.
>
> **En unitats del mesurand.** 10 bar / 4096 = 2,4 mbar. Si l'aplicació demana distingir 10 mbar hi ha marge; si en demana 1, cal replantejar convertidor i condicionament.
>
> </details>

## 5 Processament digital

Les **dades primàries** —o dades brutes— són els valors que surten del convertidor, en comptes i codis, no en unitats físiques. Operacions habituals:

- **Escalat.** El codi binari de l'ADC no és una temperatura: només adquireix significat físic quan el PC o el microcontrolador hi aplica els paràmetres de la funció de resposta.
- **Linealització** per funció inversa, polinomi d'ajust o taula de consulta amb interpolació.
- **Correcció d'errors coneguts**: error de zero, deriva tèrmica, efecte de càrrega quantificat. Els dos primers es defineixen al document 5.
- **Filtratge digital i estadística** per reduir la component aleatòria.
- **Càlcul de magnituds derivades**, és a dir mesures indirectes.

> [!IMPORTANT]
>
> En cadenes senzilles i lineals la propagació dels errors és previsible i calculable analíticament. Quan el processament és **fortament no lineal** o encadena moltes operacions, un error d'entrada petit pot amplificar-se de manera difícil d'anticipar. L'anàlisi rigorosa és la **unitat 2**.

### 5.1 · Models de processament

La manera de passar de dades primàries a resultat és el **model de processament**, i n'hi ha dues famílies.

- **Model explícit**: Equacions derivades de la física del sensor i de la cadena, amb paràmetres obtinguts per calibratge, operació que es defineix al document 5. Cada terme té significat identificable i es pot revisar quines operacions transformen les dades.
- **Model basat en aprenentatge**: La relació s'infereix de dades d'entrenament sense formular les lleis físiques. Útil quan la relació és complexa o hi ha variables acoblades —estimar la concentració d'un gas amb sensors poc selectius.

Els models apresos funcionen com una **caixa negra**: la relació existeix i pot ser precisa, però no és inspeccionable en termes de causes físiques. D'aquí dues conseqüències:

1. **Dificulten la traçabilitat**, és a dir la possibilitat de lligar el resultat a patrons de referència per una cadena documentada de comparacions. No es pot descompondre el resultat en contribucions atribuïbles a patrons, cosa que complica el càlcul rigorós de la **incertesa**.
2. **Extrapolen malament.** Són fiables dins del domini d'entrenament; fora, poden produir resultats arbitràriament erronis *sense cap indicació*, cosa perillosa en aplicacions de seguretat. El biaix del conjunt d'entrenament es trasllada al resultat.

> [!TIP]
>
> No queden invalidats, però exigeixen una **validació** molt més exhaustiva: caracteritzar el domini de validesa, comprovar els límits i comparar amb un mètode de referència independent. El criteri és que **el model sigui tan explícit com la física permeti i tan après com la complexitat obligui**.

### 5.2 · Sensors virtuals, registre i integració

Un **sensor virtual** o *soft sensor* estima una magnitud a partir d'altres de mesurades i d'un model: la temperatura interna d'un motor a partir del corrent, la velocitat i la temperatura ambient, o l'estat de càrrega d'una bateria. Estalvia maquinari i accedeix a magnituds inaccessibles, però **hereta la incertesa de totes les mesures que hi intervenen i, a més, la del model**.

El **registre de dades** —*data logging*— exigeix decidir quines magnituds es guarden, amb quina cadència i durant quant de temps. Guardar-ho tot no sempre és viable, i una decisió mal presa pot deixar un episodi anòmal fora de les dades quan cal analitzar-lo.

Els **sensors intel·ligents** integren en un encapsulat el transductor, el condicionament, la conversió, el processament i una interfície digital. **No deixen de ser sistemes de mesura**: contenen les mateixes etapes, només que no accessibles per separat. Ofereixen autocalibratge i diagnòstic, però traslladen al fabricant decisions que abans prenia el dissenyador. Un **oscil·loscopi digital** (DSO) és igualment una cadena completa de condicionament, conversió, processament i presentació: no és un sensor sinó un sistema de mesura de senyals elèctrics.

## 6 Presentació

- **Xifres significatives.** Mostrar-ne més de les que la incertesa justifica enganya l'operador.
- **Unitats.** Formen part del resultat i no són opcionals.
- **Estats anòmals.** Cal distingir valor vàlid, valor fora de marge i absència de mesura per avaria.
- **Latència.** En un llaç de control, el retard forma part del comportament dinàmic (document 6).

> [!TIP] **Síntesi**
>
> 1. **Mesurand** = el que es vol conèixer; **quantitat sota mesura** = el que el sistema capta. La diferència és error sistemàtic.
> 2. Cinc etapes, i **cadascuna aporta el seu error**.
> 3. L'**efecte de càrrega** és inevitable: es minimitza i, si cal, es caracteritza per corregir-lo.
> 4. **Wheatstone** mesura desequilibris i compensa derives; **4-20 mA** és immune a la caiguda de tensió i detecta avaries.
> 5. $f_{s}$  > 2 $f_{\max}$;  $f_{N}$  =  $f_{s}$ /2. L'**aliàsing** és irreversible i només s'evita amb filtre analògic previ.
> 6. Error de quantificació acotat per ± $q$ /2. Més bits no serveixen si el soroll supera  $q$.
> 7. Models **explícits** = traçabilitat; **apresos** = flexibilitat a canvi d'opacitat i validació exhaustiva.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC

Unitat 1 · Document 3 de 6 · Materials de treball previ · Curs 2026-T

---
[← Document 2 El Sistema Internacional d'Unitats](#sm-unitat-1-2-el-sistema-internacional-dunitats) • [Document 4 → Sensors: definició i classificació](#sm-unitat-1-4-sensors-definició-i-classificació)

---

<!-- FIN CAPÍTULO: SM_U1_03_Estructura_dels_sistemes_de_mesura -->

---

<!-- INICIO CAPÍTULO: SM_U1_04_Sensors_definicio_i_classificacio -->

# SM · Unitat 1 · 4. Sensors: definició i classificació

[← Índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura)
[1](SM_U1_01_Concepte_de_mesura.md "Concepte de mesura")[2](SM_U1_02_El_Sistema_Internacional_dUnitats.md "El Sistema Internacional d'Unitats")[3](SM_U1_03_Estructura_dels_sistemes_de_mesura.md "Estructura dels sistemes de mesura")4[5](SM_U1_05_Caracteristiques_estatiques.md "Característiques estàtiques")[6](SM_U1_06_Caracteristiques_dinamiques.md "Característiques dinàmiques")

Sistemes de Mesura · Unitat 1 · Document 4 de 6

# Sensors: definició i classificació

Dedicació estimada: 11 minuts

> [!NOTE] **Objectius**
>
> 1. Distingir sensor, transductor i actuador.
> 2. Classificar un sensor pels diferents criteris i saber què aporta cadascun.
> 3. Explicar el principi de transducció de cada família.
> 4. Deduir del model elèctric les exigències sobre el condicionament.
> 5. Identificar la sensibilitat creuada i les seves estratègies de compensació.

> [!TIP]
>
> Aquest document és el **mapa** dels sensors. L'estudi detallat de cada família —models, circuits, limitacions— és el nucli de bona part de l'assignatura, i s'indica en quina unitat es reprèn cada cas.

## 1 Sensor, transductor i actuador

- **Transductor**: Qualsevol dispositiu que converteix una forma d'energia en una altra. És el terme general.
- **Sensor**: Transductor destinat a obtenir informació. Es dissenya per maximitzar la fidelitat de la representació, no l'eficiència energètica.
- **Actuador**: Transductor invers: converteix un senyal, habitualment elèctric, en una acció física. Tanca el llaç de control.

Els criteris de disseny són **oposats**: al sensor interessa extreure energia mínima —per limitar l'efecte de càrrega— i màxima reproductibilitat; a l'actuador, transferir energia amb el màxim rendiment. Alguns dispositius fan les dues funcions: un element **piezoelèctric** genera càrrega quan es deforma i es deforma quan se li aplica tensió, reversibilitat que és la base dels transductors ultrasònics.

## 2 Classificacions

No hi ha una única classificació vàlida; se n'utilitzen diverses en paral·lel i cadascuna aporta una cosa diferent.

- **Per magnitud mesurada**: Temperatura, pressió, posició, cabal. És la dels catàlegs i la més útil per a l'usuari final. No determina el circuit de lectura: dos sensors de temperatura poden exigir electròniques ben diferents.
- **Per principi físic**: Resistiu, capacitiu, inductiu, piezoelèctric, termoelèctric, fotoelèctric. Permet preveure les vulnerabilitats a interferències: un principi magnètic patirà camps externs; un de capacitiu, la humitat i la proximitat d'objectes.
- **Per model elèctric**: Resistència, reactància, font de tensió, de corrent o de càrrega. És la del dissenyador del condicionament i permet reutilitzar topologies per a magnituds diferents.

### 2.1 · Per aportació d'energia

És la de més conseqüències pràctiques, perquè determina el tipus de condicionament.

|  | Moduladors (passius) | Generadors (actius) |
|:--- |:--- |:--- |
| Què fan | Modifiquen una propietat elèctrica —R, C, L— en funció del mesurand | Produeixen tensió, corrent o càrrega a partir de l'energia del mesurand |
| Alimentació | **Necessiten excitació externa** | No en necessiten |
| Risc dominant | La deriva de l'excitació entra directament al resultat | Senyals molt febles i impedàncies altes o reactives |

> [!IMPORTANT]
>
> La terminologia «passiu/actiu» és desafortunada perquè en electrònica de circuits significa una altra cosa. Convé recordar que un sensor **passiu és el que necessita alimentació externa**, cosa que sorprèn per contraintuïtiva.

### 2.2 · Per tipus de sortida i per referència

Els **analògics** lliuren una magnitud contínua; els **digitals**, un codi, sigui perquè el fenomen és discret —un codificador òptic— o perquè integren la conversió. Els de sortida **en freqüència** codifiquen la informació al període i no a l'amplitud, cosa que els dona immunitat a interferències i a atenuacions del cable; els mètodes de conversió són de la **unitat 8**.

Un sensor **absolut** mesura respecte d'una referència fixa i universal —un termistor respecte del zero absolut, un sensor de pressió absoluta respecte del buit. Un **diferencial** mesura la diferència entre dos punts sense determinar cap dels dos, i **cancel·la per construcció les pertorbacions comunes**. Aquest rebuig de mode comú es reprèn a la **unitat 3** i a la **unitat 6**.

## 3 Principis de transducció

### 3.1 · Resistius

- **Galga extensomètrica**: la **deformació** altera longitud i secció del conductor i, en materials piezoresistius, també la resistivitat. Mesura força, parell, pressió o massa. Les variacions són molt petites —de l'ordre del **0,1 %** en una galga metàl·lica—, cosa que obliga al pont del document 3.
- **RTD**: la resistència d'un metall pur, típicament platí, augmenta amb la temperatura amb un **coeficient de temperatura positiu** i gairebé constant, cosa que els fa molt lineals.
- **Termistors**: la resistència d'un semiconductor varia molt més abruptament. Els **NTC** tenen coeficient negatiu. Sensibilitat molt superior a la dels RTD a canvi d'una **no-linealitat pronunciada**.
- **LDR**: la resistència disminueix en augmentar la il·luminació. Mostra que aquestes famílies comparteixen el *model elèctric*, no el fenomen físic.

![Galga extensomètrica: làmina flexible amb un conductor metàl·lic disposat en ziga-zaga sobre un suport aïllant, amb dos terminals.](assets/SM_U1_04_Sensors_definicio_i_classificacio_img_1.png)

*Figura: Figura 1.4 — Galga extensomètrica. El ziga-zaga augmenta la longitud sensible a la deformació.*

Sensors resistius: **unitat 5**. Condicionament en contínua: **unitat 6**.

### 3.2 · Capacitius i inductius

Als **capacitius** el mesurand modifica la capacitat actuant sobre la superfície enfrontada, la distància entre armadures o la permitivitat del **dielèctric**. Aquest darrer mecanisme permet detectar presència de materials o nivell de líquid sense contacte elèctric.

Als **inductius** el mesurand altera la inductància d'una bobina o l'acoblament entre bobines. La proximitat d'un objecte metàl·lic canvia el camp, cosa que permet detectar posició **sense contacte mecànic**. Un cas molt estès és el **LVDT**, transformador amb nucli mòbil en què la posició del nucli fixa l'acoblament entre primari i secundaris; s'usa per a **posició i desplaçament lineal** amb resolució elevada i sense fregament. Els sensors inductius de proximitat comercials solen incorporar a l'encapsulat l'**oscil·lador** que els excita i el detector.

![Secció d'un sensor inductiu de proximitat: bobina amb nucli de ferrita, camp magnètic sortint de la cara activa i un objecte metàl·lic apropant-s'hi.](assets/SM_U1_04_Sensors_definicio_i_classificacio_img_2.png)

*Figura: Figura 1.5 — Sensor inductiu de proximitat.*

> [!TIP]
>
> Tots dos són moduladors i comparteixen una limitació que condiciona el disseny: **la seva impedància només és observable en règim altern**. Cal excitar-los amb un senyal altern i extreure la informació de l'amplitud o de la fase. Sensors: **unitat 7**; condicionament: **unitat 8**.

### 3.3 · Efecte Hall

Quan un **corrent de polarització** circula per una làmina immersa en un camp magnètic perpendicular, la força de Lorentz desvia els portadors i genera una **tensió transversal** proporcional al producte del corrent i del camp. Sense corrent de polarització no hi ha portadors en moviment i **no apareix cap tensió de Hall** per intens que sigui el camp: el sensor Hall és, doncs, modulador tot i que la sortida sigui una tensió.

![Circuit integrat de sensor d'efecte Hall de tres terminals amb la làmina semiconductora, el corrent longitudinal, el camp perpendicular i la tensió transversal.](assets/SM_U1_04_Sensors_definicio_i_classificacio_img_3.png)

*Figura: Figura 1.6 — Sensor d'efecte Hall integrat.*

Permet mesurar camps, però l'aplicació més freqüent és indirecta: com que el camp que envolta un conductor és proporcional al corrent, **mesura corrent sense interrompre el circuit ni contacte galvànic**. També detecta posició angular amb imants solidaris a l'eix. **Unitat 7**.

### 3.4 · Termoparell

L'**efecte Seebeck** estableix que en un circuit de dos metalls diferents apareix una força electromotriu quan les dues unions són a temperatures diferents. És un sensor **generador**: no necessita alimentació, cosa que el fa útil en forns industrials. Ofereix marge de temperatura molt ampli, robustesa mecànica i resposta ràpida per la seva massa tèrmica petita, a canvi d'una sensibilitat molt baixa —**desenes de microvolts per grau**— i una no-linealitat apreciable.

![Termoparell: dos fils metàl·lics de composició diferent units per soldadura en un extrem i connectats a un instrument per l'altre.](assets/SM_U1_04_Sensors_definicio_i_classificacio_img_4.jpg)

*Figura: Figura 1.7 — Termoparell.*

> [!IMPORTANT] **La unió freda**
>
> El termoparell **no mesura una temperatura sinó una diferència** entre la unió de mesura i la de referència, anomenada **unió freda**. Històricament es mantenia en gel a 0 °C; avui es mesura la seva temperatura amb un segon sensor i s'aplica la **compensació de unió freda**. Resulta paradoxal però inevitable: **per fer servir un termoparell cal un altre termòmetre**, i l'exactitud del conjunt queda limitada per la del sensor de compensació.

Termoparells i sensors generadors: **unitat 9**.

### 3.5 · Òptics i electroquímics

El **fotodíode** genera un corrent proporcional al flux lluminós. És generador, però la sortida és un **corrent de l'ordre de nanoamperes**, cosa que obliga a un amplificador de **transimpedància** que el converteix en tensió mantenint el fotodíode a tensió pràcticament nul·la. Mesurar-lo amb un simple **voltímetre** sobre una resistència de càrrega degrada linealitat i ample de banda.

Els **sensors electroquímics** aprofiten que una reacció entre l'espècie a detectar i un elèctrode genera un potencial relacionat amb la seva **concentració**: elèctrode de pH, oxigen dissolt, detectors de gasos. Tenen impedàncies de font molt altes i **selectivitat limitada**, de manera que la sensibilitat creuada sol ser el factor limitant.

Amplificadors de transimpedància, electromètrics i de càrrega: **unitat 10**.

## 4 Model elèctric

| Família | Model equivalent | Exigència sobre el condicionament |
|:--- |:--- |:--- |
| Resistiu (galga, RTD, termistor, LDR) | Resistència variable | Excitació estable; mesura del desequilibri |
| Capacitiu / inductiu | Reactància variable | Excitació alterna; detecció d'amplitud o fase |
| Termoparell | Font de tensió molt petita, resistència sèrie baixa | Guany elevat, deriva baixa, compensació de unió freda |
| Fotodíode | Font de corrent amb capacitat en paral·lel | Amplificador de transimpedància |
| Piezoelèctric | Font de càrrega amb capacitat en paral·lel | Amplificador de càrrega; inservible per a mesures estàtiques |

**Taula 1.4 — Model elèctric per família.**

> [!TIP]
>
> **Sensor i condicionament no es trien per separat.** Un termoparell exigeix deriva molt baixa perquè el senyal és de microvolts; un fotodíode exigeix una topologia completament diferent perquè lliura corrent i no tensió. Per això l'assignatura alterna unitats de sensors amb unitats de condicionament.

## 5 Sensibilitat creuada

Cap sensor real respon exclusivament al mesurand. La **sensibilitat creuada** és la resposta indesitjada a altres magnituds. L'exemple canònic és la galga: la resistència canvia amb la deformació i també amb la temperatura, i les dues variacions són indistingibles a la sortida, de manera que un canvi ambiental produeix una lectura de força inexistent.

1. **Compensació estructural.** Dissenyar el muntatge perquè l'efecte es cancel·li per construcció, com el pont de Wheatstone amb galgues en configuració diferencial.
2. **Mesura i correcció.** Un segon sensor per a la magnitud interferent, com la compensació de unió freda.
3. **Estabilització de l'entorn.** Termostatar el sensor. És l'opció més cara, però en metrologia de precisió resulta inevitable.

> [!IMPORTANT]
>
> La sensibilitat creuada és **un problema de definició del mesurand abans que d'instrument**: si el sensor respon a dues magnituds i només se n'observa una sortida, no hi ha manera d'inferir dues incògnites d'una equació. Les tres estratègies consisteixen, respectivament, a anul·lar la segona incògnita, afegir una segona equació o fixar-ne el valor.

## 6 Selecció

Criteris habituals: marge de mesura i sobrecàrrega admissible, exactitud i resolució (document 5), comportament dinàmic (document 6), condicions ambientals, facilitat de condicionament —que sovint domina el cost total per damunt del preu del sensor— i cost, disponibilitat i periodicitat del calibratge.

El pes relatiu depèn del **domini d'aplicació**:

- **Automoció**: marge de temperatura i resistència a la vibració, sovint per damunt de l'exactitud.
- **Mèdic**: aïllament elèctric del pacient i biocompatibilitat, abans que cap consideració metrològica.
- **Aeroespacial**: traçabilitat documentada i fiabilitat estadística per damunt del cost unitari.
- **IoT**: mida, consum i connectivitat per damunt de la resolució.

El termoparell i el RTD il·lustren el compromís: el primer cobreix més marge i respon més ràpid però té sensibilitat baixa, linealitat pitjor i exigeix compensació; el segon és més exacte i lineal però més lent, més car i, com a modulador, necessita excitació estable i pateix autoescalfament. **Cap dels dos és millor en abstracte.**

> [!TIP] **Síntesi**
>
> 1. **Transductor** és el terme general; sensor i actuador en són dues classes amb criteris de disseny oposats.
> 2. **Moduladors** necessiten excitació i n'hereten l'estabilitat; **generadors** no, però lliuren senyals febles.
> 3. Un sensor **diferencial** cancel·la per construcció les pertorbacions comunes.
> 4. Cada família aprofita un fenomen distint: variació de **R**, de **reactància**, efecte **Hall**, efecte **Seebeck**, generació fotoelèctrica o reacció electroquímica.
> 5. Un termoparell mesura una **diferència** i exigeix **compensació de unió freda**.
> 6. El **model elèctric** determina la topologia del condicionament.
> 7. La **sensibilitat creuada** es combat cancel·lant, mesurant i corregint, o fixant la magnitud interferent.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC

Unitat 1 · Document 4 de 6 · Materials de treball previ · Curs 2026-T

---
[← Document 3 Estructura dels sistemes de mesura](#sm-unitat-1-3-estructura-dels-sistemes-de-mesura) • [Document 5 → Característiques estàtiques](#sm-unitat-1-5-característiques-estàtiques)

<!-- FIN CAPÍTULO: SM_U1_04_Sensors_definicio_i_classificacio -->

---

<!-- INICIO CAPÍTULO: SM_U1_05_Caracteristiques_estatiques -->

# SM · Unitat 1 · 5. Característiques estàtiques

[← Índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura)
[1](SM_U1_01_Concepte_de_mesura.md "Concepte de mesura")[2](SM_U1_02_El_Sistema_Internacional_dUnitats.md "El Sistema Internacional d'Unitats")[3](SM_U1_03_Estructura_dels_sistemes_de_mesura.md "Estructura dels sistemes de mesura")[4](SM_U1_04_Sensors_definicio_i_classificacio.md "Sensors: definició i classificació")5[6](SM_U1_06_Caracteristiques_dinamiques.md "Característiques dinàmiques")

Sistemes de Mesura · Unitat 1 · Document 5 de 6

# Característiques estàtiques

Dedicació estimada: 12 minuts

> [!NOTE] **Objectius**
>
> 1. Definir la funció de resposta i justificar per què la invertibilitat condiciona el disseny.
> 2. Calcular sensibilitat i error de zero, i referir els errors a l'entrada.
> 3. Distingir les tres rectes d'aproximació i per què l'error de linealitat depèn de l'elecció.
> 4. Usar amb rigor exactitud, veracitat i fidelitat.
> 5. Estimar biaix i desviació estàndard identificant prèviament els valors aberrants.
> 6. Definir histèresi, zona morta i resolució.

## 1 Règim permanent i funció de resposta

Les **característiques estàtiques** descriuen el sistema quan el mesurand és constant o varia prou lentament perquè s'assoleixi el **règim permanent**. Sota aquesta hipòtesi el temps no hi intervé. **Deixen de descriure el sistema quan el mesurand varia ràpidament**, cas del document 6: aplicar una especificació estàtica —«exactitud ±0,1 %»— a una mesura dinàmica és l'error més comú en la lectura d'un full de característiques.

La **funció de resposta** lliga mesurand i indicació en règim permanent, i es determina per calibratge:

$$
y = f(x) \qquad (1.5)
$$

A la pràctica s'aproxima per un **model lineal**:

$$
y = S \cdot x + y_{0} \qquad (1.6)
$$

> [!TIP]
>
> La raó de fons per preferir la linealitat no és la comoditat sinó la **inversió**. L'objectiu no és obtenir  $y$  sinó estimar  $x$  a partir de  $y$:
>
>

$$
x = (y - y_{0}) / S \qquad (1.7)
$$

>
> Amb un model lineal la inversió són dues operacions; amb un polinomi de grau elevat o una exponencial caldrien mètodes numèrics iteratius, cosa rellevant en sistemes encastats amb bateria. **Tot disseny d'un sistema de mesura és, en el fons, un problema d'inversió.**

## 2 Sensibilitat i error de zero

La **sensibilitat absoluta** és la **derivada** de la funció de resposta:

$$
S = \frac{\mathrm{d}y}{\mathrm{d}x} \qquad (1.8)
$$

Les seves unitats són les de la sortida dividides per les de l'entrada: mV/°C, Ω/kg, pF/mm. En un sistema **lineal la derivada és constant** i el sensor respon igual a un canvi d'un grau a −20 °C i a +100 °C. En un de no lineal,  $S$  és funció de  $x$: un termistor NTC té sensibilitat molt alta a temperatures baixes i molt baixa a temperatures altes.

La **sensibilitat relativa** normalitza respecte de la sortida:

$$
S_{r} = (\frac{1}{y}) \cdot \frac{\mathrm{d}y}{\mathrm{d}x} \qquad (1.9)
$$

És útil quan l'error és proporcional a la lectura —l'especificació «error de l'1 % de la lectura»— però **no té les mateixes unitats que l'absoluta**. Als catàlegs, «sensibilitat» sense qualificar designa l'absoluta.

L'**error de zero** —també **offset**— és l'ordenada a l'origen  $y_{0}$: la indicació quan el mesurand val zero. És sistemàtic i, per tant, **corregible**: un cop estimat per calibratge, n'hi ha prou de restar-ne el valor com a constant. És el que fa la tara d'una bàscula.

> [!NOTE]
>
> Cal expressar-lo **referit a l'entrada**, dividint per la sensibilitat. Un error de 20 mV no significa res; amb  $S$  = 100 mV/°C equival a 0,2 °C, xifra que ja es pot comparar amb l'exigència de l'aplicació.

## 3 Error de linealitat

$$
e_{L}(x) = f(x) - (S \cdot x + y_{0}) \qquad (1.10)
$$

![Gràfica amb la corba de resposta real d'un sensor i la recta d'aproximació superposada, amb segments verticals que marquen les desviacions i el màxim destacat.](assets/SM_U1_05_Caracteristiques_estatiques_img_1.png)

*Figura: Figura 1.8 — Error de linealitat. El full de característiques en dona el màxim.*

> [!IMPORTANT]
>
> **L'error de linealitat no és un nombre sinó una funció de  $x$.** Per consignar-lo se'n pren el màxim en valor absolut i s'expressa en percentatge del fons d'escala:
>
>

$$
e_{\text{L,\max}} (\% FSO) = 100 \cdot \max|e_{L}(x)| / y_{\text{FE}} \qquad (1.11)
$$

>
> Si interessa la bondat global i no el pitjor cas, s'usa el valor eficaç en lloc del màxim.

**L'error depèn de quina recta s'hagi triat**, i totes tres són legítimes:

- **Recta tangent**: Desenvolupament de Taylor al voltant d'un punt de treball. Minimitza l'error en aquest punt i el fa créixer als extrems. Natural si el sistema treballa sempre en un entorn reduït.
- **Recta de dos punts**: Passa pels extrems del rang —zero i span. Només necessita dos punts de calibratge, però força l'error a zero als extrems i el concentra al centre, on sovint arriba al màxim.
- **Mínims quadrats**: Minimitza la suma dels quadrats de les desviacions sobre tots els punts mesurats. Millor compromís global.

Comparar la linealitat de dos sensors de fabricants diferents exigeix comprovar que tots dos l'han definit sobre el mateix tipus de recta.

> [!EXAMPLE] **Exercici resolt 1 — Caracterització amb dos punts**
>
> Un sistema de temperatura lliura 2,02 V a 20 °C i 10,02 V a 100 °C. Es vol modelar com  $y$  = S x +  $y_{0}$.
>
> <details>
> <summary><b>🔍 Desplegar Resolució</b></summary>
>
> **Sensibilitat.** $S$ = (10,02 − 2,02)/(100 − 20) = 0,100 V/°C = **100 mV/°C**.
>
> **Error de zero.** $y_{0}$ = 2,02 − 0,100 × 20 = **0,020 V**. El model és $y$ = 0,100 $x$ + 0,020. Referit a l'entrada, $x_{0}$ = 20 mV / 100 mV/°C = **0,2 °C**: el termòmetre indica sistemàticament dues dècimes de més.
>
> **Linealitat en un tercer punt.** A 60 °C el sistema lliura 6,03 V i el model prediu 6,020 V, de manera que $e_{L}$ = 10 mV, és a dir **0,1 °C** referit a l'entrada.
>
> Tots els errors s'han expressat **referits a l'entrada**: dir «10 mV d'error» no informa de res fins que no es coneix la sensibilitat.
>
> </details>

## 4 Exactitud, veracitat i fidelitat

Al carrer «precís» i «exacte» són sinònims; en metrologia no, i tenen definicions normalitzades per la ISO 5725 i el vocabulari internacional de metrologia.

- **Exactitud**: Proximitat al valor veritable. Concepte global i qualitatiu. Quan un fabricant en dona xifra, es refereix a l'error total del pitjor cas.
- **Veracitat**: Proximitat entre la tendència central de moltes mesures repetides i el valor veritable. Absència d'errors sistemàtics. La seva manca es quantifica amb el biaix.
- **Fidelitat**: Proximitat entre resultats en les mateixes condicions, és a dir dispersió, amb independència que siguin correctes. Limitada pels errors aleatoris.

![Quatre dianes que il·lustren les combinacions de veracitat i fidelitat: impactes agrupats al centre, agrupats fora del centre, dispersos al voltant del centre i dispersos i desplaçats.](assets/SM_U1_05_Caracteristiques_estatiques_img_2.png)

*Figura: Figura 1.9 — Analogia de la diana. Agrupats = fidelitat; centrats = veracitat. Exactitud = veracitat + fidelitat.*

> [!IMPORTANT]
>
> La combinació més perillosa és **molt fidel i poc veraç**. Repetir una mesura mil vegades i obtenir sempre el mateix transmet una confiança injustificada: un instrument descalibrat pot ser extraordinàriament fidel mentre menteix de manera consistent. És l'expressió quantitativa d'una idea del document 1: **l'objectivitat no garanteix la correcció**.

La fidelitat s'avalua en dues condicions normatives. La **repetibilitat** manté deliberadament constants operador, instrument, procediment, lloc i un interval curt: mesura la dispersió intrínseca. La **reproductibilitat** canvia operador, instrument, laboratori o moment. La reproductibilitat és sempre igual o pitjor, i una diferència gran entre ambdues indica que el resultat depèn de factors no controlats pel procediment.

## 5 Errors sistemàtics i aleatoris

|  | Error sistemàtic | Error aleatori |
|:--- |:--- |:--- |
| Es manifesta com | Biaix de la mitjana | Dispersió al voltant de la mitjana |
| Afecta | La veracitat | La fidelitat |
| En repetir | Es manté | Canvia de signe i de valor |
| Es redueix | Corregint-lo per calibratge | Promitjant lectures |
| Origen típic | Descalibratge, error de zero, efecte de càrrega | Soroll electrònic, turbulència, arrodoniment |

El **biaix** estima l'error sistemàtic comparant la mitjana d'un nombre elevat de lectures amb la sortida que hauria de donar el sistema:

$$
b = \bar{y} - y_{\text{ref}} \qquad (1.12)
$$

- **$\bar{y}$**: Mitjana de les $N$ lectures vàlides obtingudes en aplicar un patró de referència a l'entrada.
- **$y_{\text{ref}}$**: La sortida que produiria, per a aquest mateix patró, un sistema sense biaix. És el valor que es dedueix de la funció de resposta de referència, $y_{\text{ref}}$ = $S$ · $x_{p}$ + $y_{0}$, on $x_{p}$ és el valor convencionalment veritable del patró.

> [!IMPORTANT]
>
> Els dos termes de l'equació (1.12) han de ser **homogenis**: tots dos són sortides. Restar directament el valor del patró a la mitjana de les lectures només és correcte quan la sortida ja ve expressada en unitats del mesurand —el cas d'una bàscula que indica quilograms—, i és una font d'error habitual quan no ho és.
>
> Com amb l'error de zero, el biaix es pot expressar **referit a l'entrada** dividint-lo per la sensibilitat,  $b_{x}$  =  $b$ / $S$, que és la forma que permet comparar-lo amb l'exigència de l'aplicació.

La **dispersió** s'estima amb la desviació estàndard experimental de les lectures vàlides:

$$
s = \sqrt{\sum (y_{i} - \bar{y})^2 / (N - 1)} \qquad (1.13)
$$

El **calibratge** estableix la relació entre les indicacions i els valors de patrons de referència: **no modifica l'instrument, el caracteritza**. L'ajust posterior sí que el modifica. Cal repetir-lo periòdicament per la **deriva**: la variació lenta de les característiques amb el temps, la temperatura o l'ús.

Un **valor aberrant** —*outlier*— és una lectura incompatible amb la resta, atribuïble a una causa singular i no a la variabilitat normal. Descartar-lo és legítim si se'n justifica la causa o si ho avalen criteris fixats **abans** de mirar les dades; eliminar dades perquè no encaixen és manipulació. El que mai és admissible és **incloure'l sense revisar-lo**: distorsiona alhora la mitjana i la desviació estàndard, i per tant falseja el diagnòstic de veracitat i el de fidelitat.

## 6 Histèresi, zona morta i resolució

- **Histèresi**: Diferència entre les indicacions per a un mateix mesurand segons si s'hi arriba des de valors inferiors o superiors: la sortida depèn de la història prèvia. Prové de fregament, folgances, romanència magnètica, deformacions no elàstiques i absorció d'humitat o gasos. No es corregeix amb un simple calibratge, perquè caldria conèixer el sentit de l'aproximació.
- **Zona morta**: Interval del mesurand dins del qual una variació de l'entrada no produeix cap canvi apreciable de sortida. Apareix per fregaments estàtics o llindars de detecció. El sistema esdevé cec a variacions petites, cosa crítica en aplicacions d'alarma.
- **Resolució**: Canvi més petit del mesurand que produeix un canvi perceptible de la indicació. En sistemes digitals ve fixada pel bit menys significatiu.

> [!IMPORTANT]
>
> **Resolució, fidelitat i exactitud són tres coses diferents i cap implica les altres.** La resolució és el pas mínim representable; la fidelitat, com de juntes queden les lectures repetides; l'exactitud, com de prop queden del valor veritable. Afegir dígits a una indicació sorollosa només afegeix xifres sense contingut.

> [!EXAMPLE] **Exercici resolt 2 — Caracterització d'una bàscula**
>
> Amb un pes patró de 10,000 kg es prenen 11 lectures:
>
> 10,58 · 10,63 · 3,00 · 10,52 · 10,65 · 10,48 · 10,70 · 10,51 · 10,55 · 10,61 · 10,57 (kg)
>
> <details>
> <summary><b>🔍 Desplegar Resolució</b></summary>
>
> **Resolució.** Totes tenen dos decimals i el dígit menys significatiu varia d'unitat en unitat: **0,01 kg = 10 g**, deduït de les dades i no del catàleg.
>
> **Valor aberrant.** La tercera lectura, **3,00 kg**, és incompatible amb un objecte de 10 kg. Es descarta i queden $N$ = 10. Sense descartar-la la mitjana cauria a 9,89 kg i s'hauria conclòs, erròniament, que la bàscula és gairebé veraç: **un sol outlier hauria invertit el diagnòstic**.
>
> **Biaix i dispersió.** La bàscula indica directament en quilograms, de manera que la sortida de referència per al patró és $y_{\text{ref}}$ = 10,000 kg. Amb $\bar{y}$ = 10,580 kg resulta $b$ = **+0,58 kg**; $s$ = **0,068 kg**. El **biaix positiu** indica que la bàscula **sobreestima** el mesurand: indica sistemàticament 580 g de més. Veracitat molt baixa, fidelitat raonable.
>
> **Diagnòstic.** El biaix és vuit vegades la dispersió: domina l'error **sistemàtic**, i és bona notícia perquè es corregeix restant 0,58 kg.
>
> **Observació final.** La pantalla mostra dos decimals —resolució 0,01 kg— però la dispersió real és 0,068 kg, set vegades més. **El segon decimal no conté informació fiable**: està dominat pel soroll i no pel pes.
>
> </details>

Un sistema ideal tindria resposta lineal, sensibilitat alta i constant, error de zero nul, biaix nul, soroll nul, histèresi i zona morta nul·les i resolució infinita. Com que no existeix, la feina de l'enginyer és el millor compromís per a cada aplicació: **no hi ha sensors bons en abstracte, hi ha sensors adequats a un problema**.

> [!TIP] **Síntesi**
>
> 1. Descriuen el **règim permanent** i deixen de valer si el mesurand varia ràpid.
> 2. S'aproxima per una recta sobretot perquè la **inversió** sigui trivial.
> 3. **Sensibilitat** = pendent; **error de zero** = ordenada a l'origen. Els errors, referits a l'entrada.
> 4. L'**error de linealitat** és funció de  $x$  i depèn de la recta: tangent, dos punts o **mínims quadrats**.
> 5. **Exactitud = veracitat + fidelitat.** Biaix i dispersió les quantifiquen.
> 6. El **sistemàtic** es corregeix per calibratge; l'**aleatori**, promitjant.
> 7. Un **outlier** no tractat pot invertir el diagnòstic d'un instrument.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC

Unitat 1 · Document 5 de 6 · Materials de treball previ · Curs 2026-T

---
[← Document 4 Sensors: definició i classificació](#sm-unitat-1-4-sensors-definició-i-classificació) • [Document 6 → Característiques dinàmiques](#sm-unitat-1-6-característiques-dinàmiques)

---

<!-- FIN CAPÍTULO: SM_U1_05_Caracteristiques_estatiques -->

---

<!-- INICIO CAPÍTULO: SM_U1_06_Caracteristiques_dinamiques -->

# SM · Unitat 1 · 6. Característiques dinàmiques

[← Índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura)
[1](SM_U1_01_Concepte_de_mesura.md "Concepte de mesura")[2](SM_U1_02_El_Sistema_Internacional_dUnitats.md "El Sistema Internacional d'Unitats")[3](SM_U1_03_Estructura_dels_sistemes_de_mesura.md "Estructura dels sistemes de mesura")[4](SM_U1_04_Sensors_definicio_i_classificacio.md "Sensors: definició i classificació")[5](SM_U1_05_Caracteristiques_estatiques.md "Característiques estàtiques")6

Sistemes de Mesura · Unitat 1 · Document 6 de 6

# Característiques dinàmiques

Dedicació estimada: 9 minuts

> [!NOTE] **Objectius**
>
> 1. Decidir quan el model estàtic continua sent vàlid.
> 2. Distingir ordre zero, primer ordre i segon ordre.
> 3. Relacionar la constant de temps amb la freqüència de tall i amb l'error dinàmic.
> 4. Justificar per què un primer ordre no segueix mai una rampa sense error.
> 5. Estimar la constant de temps d'una resposta a esglaó registrada.

## 1 Quan el mesurand varia

El document 5 pressuposa el mesurand constant. A la pràctica molts són dinàmics: la pressió d'una canonada en obrir una vàlvula, la temperatura d'un component en engegar, l'acceleració en un impacte. Llavors el sistema **no pot seguir el mesurand instantàniament** i la sortida és una versió distorsionada en el temps de l'entrada.

> [!TIP]
>
> **Si la dinàmica del sistema és molt més ràpida que la del mesurand**, el model estàtic val i aquest document és innecessari. **Si no**, cal modelar-lo com un sistema dinàmic lineal i caracteritzar-lo per la resposta freqüencial o per les respostes a esglaó i a rampa. Si no és lineal hi ha mètodes més sofisticats, fora de l'abast del curs.

Aquest error és de naturalesa distinta: un sistema perfectament calibrat, amb error de zero nul i linealitat impecable, pot lliurar una indicació completament incorrecta si el mesurand varia massa ràpid. **Cap característica estàtica no ho detecta**, perquè totes suposen el mesurand quiet.

## 2 Tres models

> [!TIP]
>
> **Tot sistema de mesura real té limitacions de sistema passa-baix.** Cap dispositiu físic no pot respondre instantàniament, perquè qualsevol element que emmagatzemi energia —una massa tèrmica, una inèrcia mecànica, una capacitat paràsita, l'ample de banda finit d'un amplificador— introdueix un retard. Per damunt d'una certa freqüència, doncs, **tot sistema de mesura atenua i desfasa**.
>
> Per això el model d'ordre zero és una **idealització**: descriu bé un sistema real només dins d'una banda de freqüències prou per sota del seu límit.
>
> La pregunta pertinent no és, per tant, si el sistema és passa-baix, sinó *on* té el límit i si el mesurand hi queda prou per sota.

| Model | Caracterització | Comportament |
|:--- |:--- |:--- |
| **Ordre zero** | Només la sensibilitat  $S$ | Ideal: resposta plana, sense retard ni distorsió, error dinàmic nul. Un potenciòmetre de posició s'hi aproxima. |
| **Primer ordre** | Una **constant de temps**  $\tau$ | **Filtre passa-baix**: segueix bé les variacions lentes i atenua les ràpides. És el més freqüent. |
| **Segon ordre** | Freqüència natural  $\omega_{n}$  i amortiment  $\zeta$ | Dos elements d'emmagatzematge d'energia. Pot oscil·lar. Acceleròmetres, micròfons, manòmetres de tub. |

$$
y(t) = S \cdot x(t) \qquad (1.14)
$$

$$
H(s) = S / (1 + \tau s) \qquad (1.15)
$$

$$
H(s) = S \cdot \omega _{n}^2 / (s^2 + 2 \zeta \omega _{n}s + \omega _{n}^2) \qquad (1.16)
$$

Corresponen a primer ordre els termòmetres —on  $\tau$  depèn de la massa tèrmica i del coeficient de transferència de calor— i, en general, qualsevol sistema amb una sola capacitat i una sola resistència. Al segon ordre el comportament depèn de l'amortiment: amb  $\zeta$  petit oscil·la i presenta pic a la resposta freqüencial; amb  $\zeta$  gran no oscil·la però respon lentament. El compromís habitual en instrumentació és  $\zeta$  ≈ 0,7.

## 3 Resposta del sistema de primer ordre

> [!IMPORTANT]
>
> Tot el que segueix en aquesta secció —la constant de temps, la freqüència de tall, el 63,2 % i el retard davant d'una rampa— **val exclusivament per a sistemes de primer ordre**. Un sistema de segon ordre no queda descrit per un únic paràmetre temporal: necessita la freqüència natural i el coeficient d'amortiment, i la seva resposta a un esglaó pot presentar sobreoscil·lació, cosa que cap expressió d'aquesta secció no recull.

La resposta d'un sistema de primer ordre a un esglaó és una exponencial:

$$
y(t) = y_{f} + (y_{i} - y_{f}) \cdot e^{-t/ \tau} \qquad (1.17)
$$

![Dos panells: a l'esquerra, entrada en esglaó i resposta exponencial d'un sistema de primer ordre; a la dreta, entrada en rampa i resposta que la segueix amb un retard constant.](assets/SM_U1_06_Caracteristiques_dinamiques_img_1.png)

*Figura: Figura 1.10 — Resposta d'un primer ordre a un esglaó i a una rampa.*

> [!NOTE]
>
> La **constant de temps** és el temps per recórrer el **63,2 %** de l'excursió total, o equivalentment per reduir al 36,8 % el que quedava. Després de **5 $\tau$**  la resposta ha recorregut més del 99 % i es considera assentada.

$$
f_{c} = \frac{1}{2 \pi \tau } \qquad (1.18)
$$

Aquesta és la **freqüència de tall del primer ordre**, i la relació és inversa: **reduir  $\tau$  eixampla l'ample de banda**. Un termòmetre amb  $\tau$  = 2 s té  $f_{c}$  = 0,08 Hz i no serveix per registrar fluctuacions d'un hertz per exacte que sigui en règim permanent.

> [!IMPORTANT]
>
> Davant d'una **rampa**, passat el transitori la sortida creix amb la mateixa pendent però **desplaçada un retard constant igual a  $\tau$**. L'error de seguiment **no s'anul·la mai**: un primer ordre **no atrapa mai una rampa**, assoleix la seva velocitat però no la seva posició. En un llaç de control amb consigna creixent, el regulador treballa permanentment amb informació desfasada.

L'**error dinàmic** és la diferència entre el valor indicat i el real, atribuïble només a la incapacitat de seguir les variacions. El **concepte és general** i s'aplica a qualsevol ordre; el que és propi del primer ordre és la seva quantificació mitjançant una única constant de temps. Té tres propietats:

1. **No és constant**: depèn de l'instant i de la forma d'ona, i no es pot resumir en una xifra de catàleg.
2. **No es corregeix per calibratge**: no prové d'un desajust sinó d'una limitació d'ample de banda.
3. **És predictible** si es coneixen el model i l'entrada. En això s'assembla a un error sistemàtic i es diferencia del soroll.

Aquesta previsibilitat permet **compensar el retard per processament digital**, tot i que la compensació amplifica el soroll d'alta freqüència i el marge de millora queda limitat per la qualitat del senyal.

## 4 Estimació de la constant de temps d'un primer ordre

Els cinc mètodes següents pressuposen que el sistema és de **primer ordre**; aplicats a un de segon ordre amb amortiment baix donen resultats sense sentit. Aixecar tota la resposta freqüencial exigiria injectar sinusoides una per una; en canvi **una sola resposta a esglaó registrada conté tota la informació**. Cinc mètodes, de més senzill a més robust, sobre un esglaó descendent:

1. **Pendent inicial.** Es traça la tangent en l'instant de l'esglaó i es prolonga fins al valor final; l'abscissa de la intersecció és  $\tau$.
2. **63 % de l'excursió.** Es busca l'instant en què la resposta n'ha recorregut el 63,2 %.
3. **Temps de transició 10 %–90 %.** Per a un primer ordre la relació és fixa. No cal determinar l'instant de l'esglaó, cosa còmoda sobre l'oscil·loscopi.
4. **Dos instants arbitraris.** Mètode general per logaritmes. Serveix amb qualsevol parell de punts, però **exigeix conèixer  $y_{f}$  amb precisió**, i aquesta dependència és el seu punt feble.
5. **Mínims quadrats.** S'ajusta el model exponencial complet sobre totes les dades.

$$
t_{10-90} \approx 2{,}2 \tau \implies \tau \approx t_{10-90} / 2{,}2 \qquad (1.19)
$$

$$
\tau = (t_{2} - t_{1}) / \ln[(y_{1} - y_{f}) / (y_{2} - y_{f})] \qquad (1.20)
$$

![Corba exponencial descendent amb la recta tangent a l'origen prolongada fins a tallar el valor final; una fletxa marca l'instant de la intersecció.](assets/SM_U1_06_Caracteristiques_dinamiques_img_2.png)

*Figura: Figura 1.11 — Mètode del pendent inicial.*

![Corba exponencial descendent amb una línia horitzontal al 63 per cent de l'excursió i una vertical que baixa fins a l'eix de temps.](assets/SM_U1_06_Caracteristiques_dinamiques_img_3.png)

*Figura: Figura 1.12 — Mètode del 63 % de l'excursió.*

![Corba exponencial descendent amb dues línies horitzontals als nivells del 10 i del 90 per cent i la indicació de l'interval entre els encreuaments.](assets/SM_U1_06_Caracteristiques_dinamiques_img_4.png)

*Figura: Figura 1.13 — Mètode del temps de transició 10 %–90 %.*

![Corba exponencial descendent amb dos punts arbitraris marcats i les seves projeccions sobre els eixos.](assets/SM_U1_06_Caracteristiques_dinamiques_img_5.png)

*Figura: Figura 1.14 — Mètode dels dos instants arbitraris.*

> [!TIP]
>
> Amb soroll, els quatre primers donen valors lleugerament diferents perquè cadascun depèn d'uns pocs punts. Els **mètodes 1 a 4 són gràfics i ràpids**, per estimar sobre la marxa amb l'oscil·loscopi; el **cinquè és numèric i robust**, perquè utilitza tota la informació registrada, i és el que correspon quan el resultat ha de sostenir una decisió. Cal situar l'esglaó a l'origen de temps i considerar només les mostres posteriors.

## 5 Una excepció

Tot sistema té un límit superior de banda, però alguns en tenen també un d'inferior. Els sensors **piezoelèctrics** i **piroelèctrics** són **passa-banda**, perquè tenen **resposta nul·la en contínua**. Un piezoelèctric no pot mesurar una magnitud constant: davant d'una força estàtica genera una càrrega inicial que es descarrega per la resistència de fuita fins que la indicació torna a zero, tot i que la força continuï. Són excel·lents per a vibracions, impactes i transitoris, i inservibles per a mesures estàtiques.

> [!TIP] **Síntesi**
>
> 1. Calen quan la dinàmica del mesurand no és molt més lenta que la del sistema. **Tot sistema real és passa-baix** per damunt d'alguna freqüència.
> 2. **Ordre zero** (ideal), **primer ordre** (una constant de temps), **segon ordre** (freqüència natural i amortiment).
> 3. Per al **primer ordre**:  $\tau$  = temps per recórrer el **63,2 %**, i a 5 $\tau$  es considera assentada.
> 4. $f_{c}$  = 1/(2π $\tau$ ): reduir  $\tau$  eixampla l'ample de banda.
> 5. Davant d'una **rampa**, el primer ordre queda endarrerit  $\tau$  permanentment.
> 6. L'**error dinàmic** no és constant ni es corregeix per calibratge, però **és predictible**.
> 7. Els **piezoelèctrics** són passa-banda i no serveixen per a mesures estàtiques.

**Sistemes de Mesura** · Grau en Enginyeria Electrònica de Telecomunicacions · ETSETB — UPC

Unitat 1 · Document 6 de 6 · Materials de treball previ · Curs 2026-T

---
[← Document 5 Característiques estàtiques](#sm-unitat-1-5-característiques-estàtiques) • [Has acabat → Torna a l'índex de la unitat](#sm-unitat-1-introducció-als-sistemes-de-mesura)

---

<!-- FIN CAPÍTULO: SM_U1_06_Caracteristiques_dinamiques -->

---

<!-- INICIO CAPÍTULO: SM_U1_07_Entrenament -->

# SM · Unitat 1 · Entrenament

Sistemes de Mesura · Unitat 1

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
Unitat 1 · Material d'entrenament · Curs 2026-T

---

## 🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)

> [!TIP] **Com utilitzar aquest material d'entrenament**
> Aquest banc conté **50 afirmacions clau** dissenyades per consolidar els conceptes de la unitat i preparar els qüestionaris d'avaluació continuada.
> Intenta respondre mentalment **Vertader (V)** o **Fals (F)** abans de desplegar la solució i la justificació tècnica.

### Qüestió 01
> 📌 **Afirmació:** *La representativitat d'una escala numèrica es defineix respecte d'un atribut concret i no de manera absoluta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La representativitat no és una propietat absoluta d'una escala: es defineix respecte d'un atribut concret. Una escala pot ser representativa per a la duresa i no dir res del color.*

> **📚 Document de referència:** `SM_U1_01_Concepte_de_mesura.md`
> </details>

### Qüestió 02
> 📌 **Afirmació:** *Un valor obtingut exclusivament per simulació, si el model és exacte, constitueix una mesura del sistema real.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'assignació ha de ser empírica. Un valor obtingut només per simulació, per exacte que sigui el model, és una predicció sobre el sistema, no una mesura del sistema.*

> **📚 Document de referència:** `SM_U1_01_Concepte_de_mesura.md`
> </details>

### Qüestió 03
> 📌 **Afirmació:** *Dos enginyers independents que segueixin el mateix protocol amb instruments calibrats han d'obtenir resultats compatibles.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició operativa d'objectivitat: el resultat depèn del procediment i dels instruments, no de qui mesura.*

> **📚 Document de referència:** `SM_U1_01_Concepte_de_mesura.md`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *Que una mesura sigui directa o indirecta és una propietat de la magnitud mesurada i no del procediment emprat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És una propietat del procediment. La mateixa magnitud pot ser directa amb un instrument i indirecta amb un altre.*

> **📚 Document de referència:** `SM_U1_01_Concepte_de_mesura.md`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *Si es disposa d'un wattímetre, la mesura de la potència continua sent indirecta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Amb wattímetre, la potència s'obté per lectura sense càlculs de l'usuari, i per tant passa a ser directa.*

> **📚 Document de referència:** `SM_U1_01_Concepte_de_mesura.md`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *El resultat d'un producte es pot expressar amb més xifres significatives que el factor que menys en té.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El resultat no pot tenir més xifres significatives que el factor que menys en té; altrament s'atribueix a la mesura una precisió que els instruments no tenen.*

> **📚 Document de referència:** `SM_U1_01_Concepte_de_mesura.md`
> </details>

### Qüestió 07
> 📌 **Afirmació:** *Un ohmímetre que injecta un corrent i mesura la tensió és una mesura directa per a l'usuari i indirecta per al dissenyador.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La classificació depèn del punt de vista: l'usuari llegeix un valor, però el dissenyador ha combinat una mesura de tensió amb una font de corrent.*

> **📚 Document de referència:** `SM_U1_01_Concepte_de_mesura.md`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *La coherència del SI elimina la necessitat de factors de conversió dins del mateix sistema.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de coherència: les unitats derivades es formen sense factors numèrics, de manera que les fórmules no en necessiten cap.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 09
> 📌 **Afirmació:** *Com que la unitat base de massa és el quilogram, els prefixos s'apliquen al quilogram i no al gram.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El quilogram és l'excepció: com que ja incorpora un prefix, els prefixos s'apliquen al gram. 10⁻⁶ kg és un mil·ligram.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 10
> 📌 **Afirmació:** *Des que es va fixar la velocitat de la llum com a valor exacte, el metre depèn del segon.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Des de 1983 la velocitat de la llum és un valor fixat, i el metre es defineix com el que recorre la llum en 1/299 792 458 s.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 11
> 📌 **Afirmació:** *La candela és una unitat derivada perquè la seva definició depèn de la percepció visual humana.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És una de les set unitats base. Que depengui de la percepció humana no la converteix en derivada.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 12
> 📌 **Afirmació:** *El símbol del kelvin s'escriu amb majúscula perquè la unitat prové d'un nom propi.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Els símbols van en minúscula excepte si la unitat prové d'un nom propi: K de Kelvin, A d'Ampère, V de Volta, N de Newton.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *La denominació correcta de la unitat de temperatura termodinàmica és «grau Kelvin».*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La denominació correcta és «kelvin», sense «grau». El grau només s'usa amb el Celsius.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 14
> 📌 **Afirmació:** *El radian és adimensional, però conservar-lo permet distingir la freqüència angular de la freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Dimensionalment és la unitat, però escriure'l permet distingir la freqüència angular en rad/s de la freqüència en Hz, i un factor 2π omès té conseqüències greus.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 15
> 📌 **Afirmació:** *En context tècnic el SI recomana emprar preferentment els prefixos hecto, deca, deci i centi.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al revés: en context tècnic es recomanen els prefixos que són potències de mil, i hecto, deca, deci i centi es desaconsellen.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 16
> 📌 **Afirmació:** *A la pèrdua del Mars Climate Orbiter, tots dos programaris eren internament correctes i l'error va aparèixer a la frontera entre subsistemes.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Cap dels dos programaris tenia cap error intern: Lockheed Martin lliurava lliures-força segon i el JPL llegia newton segon. L'error va aparèixer a la interfície.*

> **📚 Document de referència:** `SM_U1_02_El_Sistema_Internacional_dUnitats.md`
> </details>

### Qüestió 17
> 📌 **Afirmació:** *Si el sensor s'adhereix a l'encapsulat i es vol la temperatura del nucli, la resistència tèrmica entre ambdós introdueix un error sistemàtic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El mesurand és la temperatura del nucli i la quantitat sota mesura és la de l'encapsulat. La diferència no és soroll sinó error sistemàtic del muntatge.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 18
> 📌 **Afirmació:** *L'efecte de càrrega es pot eliminar completament amb un disseny prou acurat del sensor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És inevitable: el sensor ha d'extreure energia o informació del sistema. Es pot minimitzar i, si cal, caracteritzar per corregir-lo, però no eliminar.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 19
> 📌 **Afirmació:** *Un error conegut i quantificat és menys perillós que un error petit però ignorat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un error conegut es corregeix; un error petit però ignorat es propaga silenciosament fins a la decisió final.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 20
> 📌 **Afirmació:** *El pont de Wheatstone permet amplificar el valor absolut de la resistència del sensor sense saturar l'amplificador.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El pont fa justament el contrari: el senyal útil és el desequilibri i no el valor absolut, i per això es pot amplificar amb guany elevat sense saturar.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 21
> 📌 **Afirmació:** *Les variacions tèrmiques dels quatre braços d'un pont de Wheatstone s'acumulen i degraden la mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Si totes les resistències són a la mateixa temperatura, les variacions tèrmiques es compensen mútuament. És un mecanisme de rebuig d'interferències.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *En una transmissió de 0-10 V, una lectura de 0 V permet distingir un mesurand nul d'un cable tallat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És l'inconvenient del 0-10 V: 0 V és ambigu entre mesurand nul i cable tallat. El llaç de 4-20 mA sí que els distingeix, perquè el zero són 4 mA.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 23
> 📌 **Afirmació:** *La freqüència de Nyquist designa la meitat de la freqüència de mostreig, mentre que la taxa de Nyquist designa el doble de la freqüència màxima del senyal.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Són les dues convencions que conviuen a la literatura. L'assignatura adopta la primera: f_N = f_s/2.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 24
> 📌 **Afirmació:** *Un filtre digital aplicat després de la conversió pot desfer un plegament que ja s'ha produït.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'aliàsing és irreversible. Un filtre digital elimina banda alta de l'espectre mostrejat, però un component ja plegat no és separable del contingut genuí.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 25
> 📌 **Afirmació:** *L'error de quantificació d'un convertidor ideal està acotat per la meitat del pas de quantificació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El valor s'arrodoneix al nivell disponible més proper, de manera que l'error queda acotat per ±q/2. A diferència de l'aliàsing, és predictible.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *Un model de processament basat en aprenentatge facilita l'establiment de la traçabilitat metrològica.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La dificulta: com que no es pot descompondre el resultat en contribucions atribuïbles a patrons, la cadena de traçabilitat i el càlcul d'incertesa es compliquen.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *Un sensor virtual hereta la incertesa de totes les mesures que hi intervenen i, a més, la del model.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *No és una mesura gratuïta: és una mesura indirecta, amb totes les conseqüències sobre la propagació d'incerteses.*

> **📚 Document de referència:** `SM_U1_03_Estructura_dels_sistemes_de_mesura.md`
> </details>

### Qüestió 28
> 📌 **Afirmació:** *Sensor i actuador són dues classes de transductor definides pel seu propòsit.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Transductor és el terme general; sensor i actuador se'n distingeixen pel propòsit, i tenen criteris de disseny oposats.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 29
> 📌 **Afirmació:** *Un sensor generador necessita una font d'excitació externa per produir el seu senyal.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És al revés: el generador produeix el senyal a partir de l'energia del mesurand. Qui necessita excitació externa és el modulador, també anomenat passiu.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 30
> 📌 **Afirmació:** *Un sensor d'efecte Hall és modulador tot i que la seva magnitud de sortida sigui una tensió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Sense corrent de polarització no hi ha portadors en moviment i no apareix cap tensió de Hall, per intens que sigui el camp. Que la sortida sigui una tensió no el fa generador.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 31
> 📌 **Afirmació:** *Un detector de temperatura resistiu de platí presenta un coeficient de temperatura negatiu.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El coeficient positiu i gairebé constant és el del RTD. El negatiu és el del termistor NTC.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *Un termistor NTC ofereix més sensibilitat que un RTD a canvi d'una no-linealitat més pronunciada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La resistència d'un semiconductor varia molt més abruptament amb la temperatura que la d'un metall pur.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 33
> 📌 **Afirmació:** *La impedància d'un sensor capacitiu o inductiu es pot caracteritzar amb una excitació contínua.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Una capacitat o una inductància no es poden mesurar amb excitació contínua: cal alimentar-los amb un senyal altern i extreure la informació de l'amplitud o de la fase.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *Utilitzar un termoparell exigeix disposar d'un segon sensor de temperatura per compensar la unió freda.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El termoparell mesura una diferència entre la unió de mesura i la unió freda, de manera que cal conèixer la temperatura d'aquesta darrera amb un altre sensor.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 35
> 📌 **Afirmació:** *El corrent d'un fotodíode es mesura habitualment amb un voltímetre sobre una resistència de càrrega sense degradar-ne la linealitat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Un voltímetre sobre una resistència de càrrega degrada la linealitat i l'ample de banda. Cal un amplificador de transimpedància, que manté el fotodíode a tensió pràcticament nul·la.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 36
> 📌 **Afirmació:** *La compensació estructural de la sensibilitat creuada consisteix a dissenyar el muntatge perquè l'efecte parasitari es cancel·li per construcció.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la primera de les tres estratègies, i la preferible: el pont de Wheatstone amb galgues en configuració diferencial.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 37
> 📌 **Afirmació:** *La classificació dels sensors per magnitud mesurada determina de manera única el circuit de lectura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És la dels catàlegs i la més útil per a l'usuari final, però no determina el circuit: dos sensors de temperatura poden exigir electròniques ben diferents.*

> **📚 Document de referència:** `SM_U1_04_Sensors_definicio_i_classificacio.md`
> </details>

### Qüestió 38
> 📌 **Afirmació:** *La preferència per un model de resposta lineal prové sobretot de la facilitat d'inversió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'objectiu no és obtenir y sinó estimar x. Amb un model lineal la inversió són dues operacions; amb un polinomi de grau elevat caldrien mètodes numèrics iteratius.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 39
> 📌 **Afirmació:** *La sensibilitat relativa té les mateixes unitats que la sensibilitat absoluta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Està normalitzada per la sortida i, per tant, no té les mateixes unitats. Als catàlegs, «sensibilitat» sense qualificar designa l'absoluta.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 40
> 📌 **Afirmació:** *L'error de zero s'ha d'expressar referit a l'entrada, dividint-lo per la sensibilitat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un error de 20 mV no significa res per si sol; amb una sensibilitat de 100 mV/°C equival a 0,2 °C, que ja es pot comparar amb l'exigència de l'aplicació.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 41
> 📌 **Afirmació:** *L'error de linealitat és un únic nombre, independent de la recta que s'hagi adoptat com a aproximació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És una funció de x, no un nombre, i el seu valor depèn de si la recta és tangent, de dos punts o de mínims quadrats.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 42
> 📌 **Afirmació:** *La recta que passa pels extrems del rang força un error nul als extrems i el concentra al centre.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per construcció passa pels extrems, de manera que hi força error nul; el màxim se sol desplaçar al centre del rang.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 43
> 📌 **Afirmació:** *Un sistema de mesura molt fidel és necessàriament veraç.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És la combinació més perillosa: un instrument descalibrat pot ser extraordinàriament fidel mentre menteix de manera consistent.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 44
> 📌 **Afirmació:** *La reproductibilitat és sempre igual o pitjor que la repetibilitat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Canviar operador, instrument, laboratori o moment només pot afegir dispersió. Una diferència gran indica factors no controlats pel procediment.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 45
> 📌 **Afirmació:** *L'error aleatori es redueix corregint-lo mitjançant calibratge.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El calibratge corregeix l'error sistemàtic. L'aleatori es redueix promitjant lectures repetides.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 46
> 📌 **Afirmació:** *La histèresi no es corregeix amb un simple calibratge perquè caldria conèixer el sentit de l'aproximació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La sortida depèn de la història prèvia, de manera que corregir-la exigiria conèixer el sentit de l'aproximació i sovint tot l'historial recent del mesurand.*

> **📚 Document de referència:** `SM_U1_05_Caracteristiques_estatiques.md`
> </details>

### Qüestió 47
> 📌 **Afirmació:** *Un sistema dinàmic de primer ordre queda completament caracteritzat per una única constant de temps.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'únic paràmetre que cal per caracteritzar-ne la dinàmica. El segon ordre necessita freqüència natural i coeficient d'amortiment.*

> **📚 Document de referència:** `SM_U1_06_Caracteristiques_dinamiques.md`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *L'error dinàmic es corregeix mitjançant un calibratge estàtic prou acurat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *No prové d'un desajust sinó d'una limitació d'ample de banda. Un calibratge estàtic perfecte no el redueix gens.*

> **📚 Document de referència:** `SM_U1_06_Caracteristiques_dinamiques.md`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *Reduir la constant de temps d'un sistema de primer ordre n'eixampla l'ample de banda.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La freqüència de tall val 1/(2πτ): la relació és inversa.*

> **📚 Document de referència:** `SM_U1_06_Caracteristiques_dinamiques.md`
> </details>

### Qüestió 50
> 📌 **Afirmació:** *Un sensor piezoelèctric és adequat per mesurar una força constant aplicada durant molt de temps.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Té resposta nul·la en contínua. Davant d'una força estàtica genera una càrrega que es descarrega per la resistència de fuita fins que la indicació torna a zero.*

> **📚 Document de referència:** `SM_U1_06_Caracteristiques_dinamiques.md`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | La representativitat no és una propietat absoluta d'una escala: es defineix respecte d'un atribut concret. Una escala... | SM_U1_01_Concepte_de_mesura.md |
| **02** | **F** | L'assignació ha de ser empírica. Un valor obtingut només per simulació, per exacte que sigui el model, és una predicc... | SM_U1_01_Concepte_de_mesura.md |
| **03** | **V** | És la definició operativa d'objectivitat: el resultat depèn del procediment i dels instruments, no de qui mesura. | SM_U1_01_Concepte_de_mesura.md |
| **04** | **F** | És una propietat del procediment. La mateixa magnitud pot ser directa amb un instrument i indirecta amb un altre. | SM_U1_01_Concepte_de_mesura.md |
| **05** | **F** | Amb wattímetre, la potència s'obté per lectura sense càlculs de l'usuari, i per tant passa a ser directa. | SM_U1_01_Concepte_de_mesura.md |
| **06** | **F** | El resultat no pot tenir més xifres significatives que el factor que menys en té; altrament s'atribueix a la mesura u... | SM_U1_01_Concepte_de_mesura.md |
| **07** | **V** | La classificació depèn del punt de vista: l'usuari llegeix un valor, però el dissenyador ha combinat una mesura de te... | SM_U1_01_Concepte_de_mesura.md |
| **08** | **V** | És la definició de coherència: les unitats derivades es formen sense factors numèrics, de manera que les fórmules no ... | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **09** | **F** | El quilogram és l'excepció: com que ja incorpora un prefix, els prefixos s'apliquen al gram. 10⁻⁶ kg és un mil·ligram. | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **10** | **V** | Des de 1983 la velocitat de la llum és un valor fixat, i el metre es defineix com el que recorre la llum en 1/299 792... | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **11** | **F** | És una de les set unitats base. Que depengui de la percepció humana no la converteix en derivada. | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **12** | **V** | Els símbols van en minúscula excepte si la unitat prové d'un nom propi: K de Kelvin, A d'Ampère, V de Volta, N de New... | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **13** | **F** | La denominació correcta és «kelvin», sense «grau». El grau només s'usa amb el Celsius. | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **14** | **V** | Dimensionalment és la unitat, però escriure'l permet distingir la freqüència angular en rad/s de la freqüència en Hz,... | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **15** | **F** | És al revés: en context tècnic es recomanen els prefixos que són potències de mil, i hecto, deca, deci i centi es des... | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **16** | **V** | Cap dels dos programaris tenia cap error intern: Lockheed Martin lliurava lliures-força segon i el JPL llegia newton ... | SM_U1_02_El_Sistema_Internacional_dUnitats.md |
| **17** | **V** | El mesurand és la temperatura del nucli i la quantitat sota mesura és la de l'encapsulat. La diferència no és soroll ... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **18** | **F** | És inevitable: el sensor ha d'extreure energia o informació del sistema. Es pot minimitzar i, si cal, caracteritzar p... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **19** | **V** | Un error conegut es corregeix; un error petit però ignorat es propaga silenciosament fins a la decisió final. | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **20** | **F** | El pont fa justament el contrari: el senyal útil és el desequilibri i no el valor absolut, i per això es pot amplific... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **21** | **F** | Si totes les resistències són a la mateixa temperatura, les variacions tèrmiques es compensen mútuament. És un mecani... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **22** | **F** | És l'inconvenient del 0-10 V: 0 V és ambigu entre mesurand nul i cable tallat. El llaç de 4-20 mA sí que els distinge... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **23** | **V** | Són les dues convencions que conviuen a la literatura. L'assignatura adopta la primera: f_N = f_s/2. | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **24** | **F** | L'aliàsing és irreversible. Un filtre digital elimina banda alta de l'espectre mostrejat, però un component ja plegat... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **25** | **V** | El valor s'arrodoneix al nivell disponible més proper, de manera que l'error queda acotat per ±q/2. A diferència de l... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **26** | **F** | La dificulta: com que no es pot descompondre el resultat en contribucions atribuïbles a patrons, la cadena de traçabi... | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **27** | **V** | No és una mesura gratuïta: és una mesura indirecta, amb totes les conseqüències sobre la propagació d'incerteses. | SM_U1_03_Estructura_dels_sistemes_de_mesura.md |
| **28** | **V** | Transductor és el terme general; sensor i actuador se'n distingeixen pel propòsit, i tenen criteris de disseny oposats. | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **29** | **F** | És al revés: el generador produeix el senyal a partir de l'energia del mesurand. Qui necessita excitació externa és e... | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **30** | **V** | Sense corrent de polarització no hi ha portadors en moviment i no apareix cap tensió de Hall, per intens que sigui el... | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **31** | **F** | El coeficient positiu i gairebé constant és el del RTD. El negatiu és el del termistor NTC. | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **32** | **V** | La resistència d'un semiconductor varia molt més abruptament amb la temperatura que la d'un metall pur. | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **33** | **F** | Una capacitat o una inductància no es poden mesurar amb excitació contínua: cal alimentar-los amb un senyal altern i ... | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **34** | **V** | El termoparell mesura una diferència entre la unió de mesura i la unió freda, de manera que cal conèixer la temperatu... | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **35** | **F** | Un voltímetre sobre una resistència de càrrega degrada la linealitat i l'ample de banda. Cal un amplificador de trans... | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **36** | **V** | És la primera de les tres estratègies, i la preferible: el pont de Wheatstone amb galgues en configuració diferencial. | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **37** | **F** | És la dels catàlegs i la més útil per a l'usuari final, però no determina el circuit: dos sensors de temperatura pode... | SM_U1_04_Sensors_definicio_i_classificacio.md |
| **38** | **V** | L'objectiu no és obtenir y sinó estimar x. Amb un model lineal la inversió són dues operacions; amb un polinomi de gr... | SM_U1_05_Caracteristiques_estatiques.md |
| **39** | **F** | Està normalitzada per la sortida i, per tant, no té les mateixes unitats. Als catàlegs, «sensibilitat» sense qualific... | SM_U1_05_Caracteristiques_estatiques.md |
| **40** | **V** | Un error de 20 mV no significa res per si sol; amb una sensibilitat de 100 mV/°C equival a 0,2 °C, que ja es pot comp... | SM_U1_05_Caracteristiques_estatiques.md |
| **41** | **F** | És una funció de x, no un nombre, i el seu valor depèn de si la recta és tangent, de dos punts o de mínims quadrats. | SM_U1_05_Caracteristiques_estatiques.md |
| **42** | **V** | Per construcció passa pels extrems, de manera que hi força error nul; el màxim se sol desplaçar al centre del rang. | SM_U1_05_Caracteristiques_estatiques.md |
| **43** | **F** | És la combinació més perillosa: un instrument descalibrat pot ser extraordinàriament fidel mentre menteix de manera c... | SM_U1_05_Caracteristiques_estatiques.md |
| **44** | **V** | Canviar operador, instrument, laboratori o moment només pot afegir dispersió. Una diferència gran indica factors no c... | SM_U1_05_Caracteristiques_estatiques.md |
| **45** | **F** | El calibratge corregeix l'error sistemàtic. L'aleatori es redueix promitjant lectures repetides. | SM_U1_05_Caracteristiques_estatiques.md |
| **46** | **V** | La sortida depèn de la història prèvia, de manera que corregir-la exigiria conèixer el sentit de l'aproximació i sovi... | SM_U1_05_Caracteristiques_estatiques.md |
| **47** | **V** | És l'únic paràmetre que cal per caracteritzar-ne la dinàmica. El segon ordre necessita freqüència natural i coeficien... | SM_U1_06_Caracteristiques_dinamiques.md |
| **48** | **F** | No prové d'un desajust sinó d'una limitació d'ample de banda. Un calibratge estàtic perfecte no el redueix gens. | SM_U1_06_Caracteristiques_dinamiques.md |
| **49** | **V** | La freqüència de tall val 1/(2πτ): la relació és inversa. | SM_U1_06_Caracteristiques_dinamiques.md |
| **50** | **F** | Té resposta nul·la en contínua. Davant d'una força estàtica genera una càrrega que es descarrega per la resistència d... | SM_U1_06_Caracteristiques_dinamiques.md |

<!-- FIN CAPÍTULO: SM_U1_07_Entrenament -->

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
| **(1.1)** | $P = V \cdot I$ |
| **(1.2)** | $f_{s} = 1 / T_{s}$ |
| **(1.3)** | $f_{s} > 2f_{\text{\max}}$ |
| **(1.4)** | $q = V_{\text{FE}} / 2^{n}$ |
| **(1.5)** | $y = f(x)$ |
| **(1.6)** | $y = S \cdot x + y_{0}$ |
| **(1.7)** | $x = (y - y_{0}) / S$ |
| **(1.8)** | $S = \frac{\mathrm{d}y}{\mathrm{d}x}$ |
| **(1.9)** | $S_{r} = (\frac{1}{y}) \cdot \frac{\mathrm{d}y}{\mathrm{d}x}$ |
| **(1.10)** | $e_{L}(x) = f(x) - (S \cdot x + y_{0})$ |
| **(1.11)** | $e_{\text{L,\max}} (\% FSO) = 100 \cdot \max\|e_{L}(x)\| / y_{\text{FE}}$ |
| **(1.12)** | $b = \bar{y} - y_{\text{ref}}$ |
| **(1.13)** | $s = \sqrt{\sum (y_{i} - \bar{y})^2 / (N - 1)}$ |
| **(1.14)** | $y(t) = S \cdot x(t)$ |
| **(1.15)** | $H(s) = S / (1 + \tau s)$ |
| **(1.16)** | $H(s) = S \cdot \omega _{n}^2 / (s^2 + 2 \zeta \omega _{n}s + \omega _{n}^2)$ |
| **(1.17)** | $y(t) = y_{f} + (y_{i} - y_{f}) \cdot e^{-t/ \tau}$ |
| **(1.18)** | $f_{c} = \frac{1}{2 \pi \tau }$ |
| **(1.19)** | $t_{10-90} \approx 2{,}2 \tau \implies \tau \approx t_{10-90} / 2{,}2$ |
| **(1.20)** | $\tau = (t_{2} - t_{1}) / \ln[(y_{1} - y_{f}) / (y_{2} - y_{f})]$ |