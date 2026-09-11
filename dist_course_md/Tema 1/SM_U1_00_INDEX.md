# SM · Unitat 1 · Introducció als sistemes de mesura

## 📑 Índice de Contenidos

- [Presentació de la unitat](#presentació-de-la-unitat)
- [Metodologia de treball](#metodologia-de-treball)
- [Documents de la unitat](#documents-de-la-unitat)
  - [Concepte de mesura](#concepte-de-mesura)
  - [El Sistema Internacional d'Unitats](#el-sistema-internacional-dunitats)
  - [Estructura dels sistemes de mesura](#estructura-dels-sistemes-de-mesura)
  - [Sensors: definició i classificació](#sensors-definició-i-classificació)
  - [Característiques estàtiques](#característiques-estàtiques)
  - [Característiques dinàmiques](#característiques-dinàmiques)

---

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

8 min](SM_U1_01_Concepte_de_mesura.md)
[2

### El Sistema Internacional d'Unitats

Presenta el marc de referència sobre el qual es construeix tota comparació metrològica: les set unitats base, el mecanisme de derivació d'unitats i la redefinició de 2019 a partir de constants fonamentals.

- Motivació i evolució històrica del SI
- Magnituds base i magnituds derivades. Coherència
- Les set constants fonamentals com a base de les definicions
- Prefixos decimals i convencions de notació

11 min](SM_U1_02_El_Sistema_Internacional_dUnitats.md)
[3

### Estructura dels sistemes de mesura

Descriu l'arquitectura funcional comuna a qualsevol instrument, bloc a bloc, i identifica on s'origina cada contribució d'error. Inclou el tractament dels models de processament com a part integrant del procés de mesura.

- Quantitat sota mesura, mesurand i soroll d'entrada
- Condicionament de senyal i transmissió
- Conversió A/D: mostreig, quantificació i aliàsing
- Processament digital i models de processament

13 min](SM_U1_03_Estructura_dels_sistemes_de_mesura.md)
[4

### Sensors: definició i classificació

Analitza el component que efectua la transducció primària. Estudia quatre principis físics representatius, les limitacions que cap sensor no pot evitar, i els criteris de classificació que condicionen el disseny del circuit de lectura.

- Sensor, actuador i transductor
- Galga extensomètrica, sensor inductiu, efecte Hall i termoparell
- Sensibilitat creuada i efecte de càrrega
- Criteris de classificació i model elèctric

11 min](SM_U1_04_Sensors_definicio_i_classificacio.md)
[5

### Característiques estàtiques

Defineix els paràmetres amb què s'especifica el comportament d'un sistema de mesura en règim permanent. Constitueix el vocabulari amb què la indústria descriu els seus productes als fulls de característiques.

- Funció de resposta i aproximació lineal
- Sensibilitat, error de zero i error de linealitat
- Exactitud, veracitat i fidelitat. Errors sistemàtics i aleatoris
- Histèresi, zona morta i resolució

12 min](SM_U1_05_Caracteristiques_estatiques.md)
[6

### Característiques dinàmiques

Estudia el comportament del sistema quan el mesurand varia amb el temps. Introdueix els models d'ordre zero, primer i segon, l'error dinàmic i els mètodes experimentals d'estimació de la constant de temps.

- Models dinàmics bàsics i resposta freqüencial
- Error dinàmic davant esglaó i rampa
- Estimació experimental de la constant de temps

9 min](SM_U1_06_Caracteristiques_dinamiques.md)

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
> A la mateixa carpeta hi ha la pàgina [**Entrenament**](SM_U1_07_Entrenament.md),
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