# 📚 Cuaderno Maestro: Tema 3

> ℹ️ **Documento Unificado y Consolidado para NotebookLM, Claude, Gemini & Obsidian**  
> 📂 **Carpeta de origen:** `Tema 3` | 📄 **Capítulos incluidos:** 6  
> 📅 **Generado:** 2026-09-11 19:09

---

## 📑 Índice General del Cuaderno Maestro

1. [Unitat 3 · Interferències en Sistemes de Mesura](#unitat-3-interferències-en-sistemes-de-mesura)
   - [Distribució del temps](#distribució-del-temps)
2. [U3 · 1. Fonaments i classificació de les interferències](#u3-1-fonaments-i-classificació-de-les-interferències)
   - [1 Soroll i interferència en la mesura](#1-soroll-i-interferència-en-la-mesura)
   - [2 Compatibilitat electromagnètica](#2-compatibilitat-electromagnètica)
   - [3 Classificació per origen de la font](#3-classificació-per-origen-de-la-font)
   - [4 Classificació per canal de transmissió](#4-classificació-per-canal-de-transmissió)
3. [U3 · 2. Mode diferencial i comú. Interferències conduïdes](#u3-2-mode-diferencial-i-comú-interferències-conduïdes)
   - [1 Mode diferencial i mode comú](#1-mode-diferencial-i-mode-comú)
   - [2 Interferències conduïdes externes](#2-interferències-conduïdes-externes)
   - [3 Interferències conduïdes internes](#3-interferències-conduïdes-internes)
   - [4 Tècniques de mitigació de les interferències conduïdes](#4-tècniques-de-mitigació-de-les-interferències-conduïdes)
4. [U3 · 3. Interferències capacitives i blindatge](#u3-3-interferències-capacitives-i-blindatge)
   - [1 Mecanisme de l'acoblament capacitiu](#1-mecanisme-de-lacoblament-capacitiu)
   - [2 Blindatge](#2-blindatge)
   - [3 Cable coaxial i limitació d'amplada de banda](#3-cable-coaxial-i-limitació-damplada-de-banda)
   - [4 Sondes atenuadores compensades](#4-sondes-atenuadores-compensades)
5. [U3 · 4. Interferències inductives i efecte sobre la mesura](#u3-4-interferències-inductives-i-efecte-sobre-la-mesura)
   - [1 Acoblament inductiu](#1-acoblament-inductiu)
   - [2 Mitigació de les interferències inductives](#2-mitigació-de-les-interferències-inductives)
   - [3 Efecte de les interferències sobre el resultat de mesura](#3-efecte-de-les-interferències-sobre-el-resultat-de-mesura)
   - [4 Diagnosi i selecció de la mitigació](#4-diagnosi-i-selecció-de-la-mitigació)
6. [Entrenament V/F · Unitat 3: Interferències](#entrenament-vf-unitat-3-interferències)
   - [🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)](#banc-dafirmacions-dautoavaluació-entrenament-dexamen)
   - [📋 Solucionari Ràpid (Taula de Respostes i Justificacions)](#solucionari-ràpid-taula-de-respostes-i-justificacions)

---

<!-- INICIO CAPÍTULO: 00_index -->

# Unitat 3 · Interferències en Sistemes de Mesura

La unitat es divideix en quatre documents. Cadascun inclou els objectius d'aprenentatge, exercicis resolts on escau i una síntesi final dels conceptes clau.

[1

### Fonaments i classificació de les interferències

Soroll enfront d'interferència, representació temporal i espectral, estructura font–canal–receptor, marc EMC (Directiva 2014/30/UE i IEC 61000) i classificació per origen i per canal.

Dedicació estimada: 16 minuts](#u3-1-fonaments-i-classificació-de-les-interferències)
[2

### Mode diferencial i comú. Interferències conduïdes

Mode diferencial i comú, rebuig de mode comú (CMRR), els quatre casos de connexió a terra, interferències conduïdes internes pel transformador d'alimentació i tècniques de mitigació.

Dedicació estimada: 18 minuts](#u3-2-mode-diferencial-i-comú-interferències-conduïdes)
[3

### Interferències capacitives i blindatge

Acoblament capacitiu i corrent de desplaçament, geometries de la capacitat paràsita, blindatge com a gàbia de Faraday, cable coaxial i sondes atenuadores compensades.

Dedicació estimada: 13 minuts](#u3-3-interferències-capacitives-i-blindatge)
[4

### Interferències inductives i efecte sobre la mesura

Acoblament inductiu i inductància mútua, blindatge magnètic i trenat, efecte de la interferència sobre el resultat (valor mitjà nul, distribució en U, promitjat i biaix) i diagnosi.

Dedicació estimada: 11 minuts](#u3-4-interferències-inductives-i-efecte-sobre-la-mesura)

## Distribució del temps

| Doc. | Títol | Dedicació |
|:--- |:--- | ---: |
| 1 | Fonaments i classificació de les interferències | 16 min |
| 2 | Mode diferencial i comú. Interferències conduïdes | 18 min |
| 3 | Interferències capacitives i blindatge | 13 min |
| 4 | Interferències inductives i efecte sobre la mesura | 11 min |
| Total de lectura |  | 58 min |

> [!NOTE]
>
> #### Abans de la primera sessió
>
> Un cop llegits els quatre documents, cal resoldre el qüestionari d'avaluació corresponent al tema. Les condicions concretes s'explicaran a la primera sessió de classe.

<!-- FIN CAPÍTULO: 00_index -->

---

<!-- INICIO CAPÍTULO: 01_doc -->

# U3 · 1. Fonaments i classificació de les interferències

> [!NOTE] **Objectius d'aprenentatge**
>
> - Distingir el **soroll** de la **interferència** per la seva naturalesa, origen, espectre i estratègia de reducció.
> - Descriure l'estructura **font–canal–receptor** de tot problema electromagnètic i el marc normatiu de compatibilitat electromagnètica (EMC).
> - Classificar una interferència pel seu **origen** (natural o artificial; intencionada o involuntària) i pel seu **canal de transmissió** (conduïda o radiada).
> - Situar el problema en **camp proper** o **llunyà** a partir de la freqüència i la distància, i anticipar la separació entre acoblament capacitiu i inductiu.

En tot sistema electrònic de mesura, el senyal desitjat es superposa sempre amb efectes no desitjats que en deterioren la qualitat. Aquests efectes es classifiquen en dues grans categories — el **soroll** i les **interferències** — que, tot i tractar-se sovint conjuntament, tenen orígens, característiques i metodologies de reducció fonamentalment diferents. Aquesta unitat s'ocupa de les interferències; el soroll es tracta en la unitat 4.

## 1 Soroll i interferència en la mesura

El **soroll** es defineix com la presència de variacions aleatòries i impredictibles en els senyals del sistema de mesura. Sorgeix de fenòmens físics de naturalesa estocàstica, tant en els components electrònics com en els transductors i els cables. Es pot modelar com una superposició de tensions i corrents de valor mitjà nul. Les seves característiques principals són:

- **Espectre ample:** ocupa una amplada de banda molt més gran que la de les interferències periòdiques. En el cas particular del **soroll blanc**, la seva densitat espectral de potència és pràcticament constant amb la freqüència i està present a tota la banda de mesura.
- **Naturalesa contínua:** a diferència dels esdeveniments impulsius, afecta el sistema de manera constant.

Les estratègies de reducció del soroll són complementàries: seleccionar components de baix soroll (encara que siguin més cars), integrar el senyal per reduir l'efecte estadístic de les fluctuacions, i limitar l'amplada de banda del sistema al mínim necessari mitjançant filtratge, atès que un sistema de banda més estreta capta menys soroll. Com a exemple, si es mesura una tensió contínua d'1 V en presència de soroll blanc de desviació estàndard 10 mV, cada lectura individual pot variar aproximadament entre 0,97 V i 1,03 V; en canvi, la mitjana de 100 mesures redueix la incertesa típica a l'entorn d'1 mV, ja que en promitjar *N* lectures independents la desviació típica del promig es divideix per l'arrel de *N*.

Una **interferència electromagnètica** (EMI, *Electromagnetic Interference*) es defineix com qualsevol senyal periòdic — no necessàriament sinusoïdal, sinó compost genèricament per una freqüència fonamental i una sèrie d'harmònics — que no és emprat pel sistema per fer la mesura, però que en pot pertorbar el resultat. Tradicionalment també s'hi inclouen els esdeveniments impulsius externs que, tot i ser rars, per la seva gran amplitud poden afectar esporàdicament la mesura; com que les seves estratègies de mitigació són radicalment diferents, les interferències impulsives s'estudien en cursos superiors i aquesta unitat es limita a les **interferències periòdiques**. Les seves característiques distintives són:

- **Origen habitualment humà i extern:** exemples típics són la xarxa de distribució a 50 Hz (60 Hz en altres països), les emissions de telefonia mòbil de l'ordre dels gigahertz, l'encesa elèctrica de motors o l'electrònica industrial.
- **Espectre estret:** concentrat en una freqüència fonamental i alguns harmònics (múltiples enters de la fonamental), a diferència de la banda ampla del soroll blanc.
- **Periodicitat:** presenten una estructura periòdica ben definida, expressable com una sèrie de Fourier amb un nombre limitat de components significatius.

La interferència no prové sempre de fonts externes. En una placa de circuit imprès, una pista que transporta un rellotge digital pot acoblar-se a una pista de la cadena de mesura: encara que aquest senyal és necessari per al funcionament del sistema, se suma de manera no desitjada al senyal d'interès i, per tant, actua com a interferència interna.

Perquè soroll i interferència determinen estratègies de reducció completament divergents. La reducció de soroll se centra a minimitzar les fonts internes i condicionar el senyal; la reducció d'interferència se centra, típicament, a **bloquejar el canal de transmissió** entre la font i el receptor. La taula 3.1 en resumeix les diferències.

| Aspecte | Soroll | Interferència periòdica |
|:--- |:--- |:--- |
| Naturalesa | Aleatòria, impredictible | Periòdica, determinista |
| Origen típic | Intern del sistema de mesura | Generalment extern, d'origen humà |
| Espectre | Amplada de banda gran (blanc: constant en freqüència) | Estret (fonamental i harmònics) |
| Reducció | Components de baix soroll, filtres passa-baix, mitjana | Modificació del canal de transmissió, filtres de banda eliminada |

La presència simultània de soroll i interferència degrada la **repetibilitat** del sistema: mentre un sistema ideal donaria sempre el mateix valor, un de real proporciona lectures que varien al voltant del valor veritable. Millorar la repetibilitat exigeix reduir alhora soroll i interferència, cosa que sol comportar solucions més costoses o complexes; el disseny és, doncs, una negociació constant entre cost i qualitat. Si es vol mesurar un senyal de 100 µV en presència d'1 mV de soroll i interferència combinats, l'efecte pertorbador és deu vegades més gran que el senyal i el sistema no el pot detectar de manera fiable sense reduir-lo abans.

### Representació temporal i espectral

Un senyal observat es pot descompondre com la suma del senyal útil, la interferència i el soroll:

$$
x(t) = s(t) + i(t) + n(t) \qquad (3.1)
$$

on

$$
s(t)
$$

  és el senyal d'interès,

$$
i(t)
$$

  la interferència superposada i

$$
n(t)
$$

  el soroll additiu. En el **domini temporal**, el senyal d'interès varia lentament o amb una freqüència ben definida; la interferència apareix com una oscil·lació periòdica clara (per exemple, els 50 Hz de la xarxa); i el soroll es manifesta com una fluctuació aleatòria contínua sense patró reconeixible. La figura 3.1 mostra un senyal continu d'unes 87 unitats contaminat per una interferència d'amplitud ±15 unitats a prop de 100 Hz i per soroll blanc de ±2–3 unitats; el resultat oscil·la entre 65 i 109 unitats.

![Senyal continu amb interferència periòdica i soroll en el temps](assets/01_doc_img_1.png)

*Figura: Figura 3.1. Superposició d'un senyal continu amb interferència periòdica i soroll, en el domini temporal.*

En el **domini de la freqüència** (mitjançant la transformada de Fourier o qualsevol estimador d'espectre de potència) les distincions es fan encara més evidents: el senyal d'interès ocupa una banda baixa i concentrada; la interferència apareix com a **pics espectrals discrets** a la freqüència fonamental i als seus harmònics; i el soroll es distribueix com un **nivell de base continu** (*spectral floor*) per tota la banda. La figura 3.2 mostra la densitat espectral de potència (PSD) del senyal de la figura 3.1: un nivell molt elevat en contínua, pics a 100, 200, 300 Hz… (fonamental i harmònics) i un terra de soroll a l'entorn de les $10^{3}$ unitats de densitat espectral.

![Densitat espectral de potència del senyal contaminat](assets/01_doc_img_2.png)

*Figura: Figura 3.2. Densitat espectral de potència de la superposició de la figura 3.1: pics discrets de la interferència sobre el terra de soroll.*

## 2 Compatibilitat electromagnètica

Per gestionar de manera efectiva els problemes d'interferència cal entendre l'estructura bàsica de qualsevol problema electromagnètic, que implica tres elements inseparables (figura 3.3).

![Estructura font, canal, receptor](assets/01_doc_img_3.png)

*Figura: Figura 3.3. Estructura bàsica per a l'anàlisi d'interferències electromagnètiques: font, canal i receptor.*

La **font** o generador d'interferència és qualsevol equip o procés que genera energia electromagnètica que no és el senyal útil (xarxa elèctrica, motors, telèfons, commutadors electrònics). Es caracteritza per una freqüència fonamental i harmònics amb amplituds determinades i es pot descriure per la seva PSD. El **canal** és la via física per la qual l'energia viatja de la font al receptor: cables de mesura, un medi dielèctric com l'aire, o una combinació d'ambdós; el canal típicament atenua la interferència. El **receptor** és el sistema electrònic que intenta mesurar el senyal útil però que també és sensible a la interferència; l'impacte dependrà de la seva impedància d'entrada, amplada de banda i aïllament.

En teoria es pot actuar sobre qualsevol dels tres elements, però l'estratègia més eficaç consisteix generalment a actuar sobre el **canal**, modificant la manera com la interferència s'introdueix en el sistema: blindatges, cables coaxials, filtratge o millora de les connexions.

### El marc normatiu

A escala comercial i legal, els problemes d'interferència s'aborden mitjançant les normatives de **compatibilitat electromagnètica (EMC)**, que asseguren que els dispositius no causin interferències excessives i que en tolerin adequadament les presents en el seu entorn operatiu. A la Unió Europea, la **Directiva 2014/30/UE** (anteriorment 89/336/CEE) exigeix que tots els aparells elèctrics i electrònics comercialitzats compleixin els estàndards de la sèrie **IEC 61000**, subdividida en parts: generalitats i guies (61000-1), entorn electromagnètic (61000-2), límits d'emissió (61000-3), tècniques de prova d'immunitat (61000-4), protecció i instal·lacions (61000-5) i normes genèriques (61000-6). Altres regions segueixen normatives anàlogues: la FCC als Estats Units o l'ISED al Canadà.

Per comercialitzar un equip a la Unió Europea cal superar dues bateries de proves complementàries. Les **proves d'emissió** mesuren el nivell d'interferència que l'equip genera en funcionament normal — emissió conduïda pels cables d'alimentació i de dades i emissió radiada —, i s'han de mantenir per sota dels límits segons la classe (residencial, comercial o industrial). Les **proves d'immunitat** mesuren la capacitat de l'equip de tolerar les interferències del seu entorn (impulsos ràpids, transitoris, variacions de tensió de xarxa, camps radiats) sense deixar de funcionar correctament.

Els límits són fruit de negociacions internacionals que equilibren la viabilitat tècnica, la coexistència de múltiples equips i el risc sobre equips crítics (comunicacions, salut). Cal remarcar que **complir la normativa no garanteix l'absència de problemes** a la pràctica: les proves no cobreixen totes les configuracions possibles, diversos equips conformes poden sumar interferències que superin els nivells tolerables, l'usuari pot fer-ne un ús no previst i l'envelliment o les avaries poden augmentar-ne l'emissió.

## 3 Classificació per origen de la font

L'origen determina les característiques dinàmiques de la interferència: si és periòdica o impulsiva, l'espectre que ocupa, l'amplitud i l'estabilitat temporal. És el primer pas de l'anàlisi. Les interferències poden tenir origen **natural** o **artificial**.

### Interferències naturals

Es manifesten típicament com a senyals **impulsius** més que periòdics. Tot i ser menys freqüents en laboratoris urbans moderns que les artificials, la seva magnitud i potencial destructiu són considerables, i poden tenir origen terrestre o extraterrestre.

Entre les **terrestres** destaquen les descàrregues de llamps — un dels fenòmens electromagnètics més energètics de la natura — i les **descàrregues electrostàtiques (ESD)**, més comunes en entorns de treball. Les ESD es generen en contactes amb materials no conductors i, malgrat durar microsegons, contenen prou energia per danyar irreversiblement components semiconductors, especialment en tecnologies de canal estret: ruptura de dielèctrics en portes CMOS, danys d'unió PN en díodes i degradació latent que es manifesta setmanes o mesos després.

Entre les **extraterrestres** destaquen les **tempestes solars**, que constitueixen un risc d'EMC a escala global: una erupció solar pot alterar la magnetosfera i induir transitoris en línies de transmissió separades per centenars de quilòmetres. La **radiació còsmica** primària és una font contínua per als sistemes en altes altituds: protons i partícules alfa produeixen ionització secundària als semiconductors i poden invertir bits en memòries, un problema crític en satèl·lits i, creixentment, en circuits nanomètrics a nivell de terra.

### Interferències artificials

La immensa majoria de les interferències pràctiques procedeix de fonts creades per l'home. Es categoritzen segons si la radiació és una funció **desitjada** de l'equip (interferència intencionada) o una manifestació **no desitjada** del seu funcionament (interferència involuntària).

Les **intencionades** provenen de transmissors de comunicació — ràdio, televisió, telefonia mòbil, radar —, que emeten deliberadament energia amb potències significatives (de quilowatts a megawatts). Tot i operar dins de bandes designades, la radiació sempre es propaga més enllà de l'antena i pot contaminar sistemes propers que operin a freqüències pròximes o amb marges de separació insuficients; s'acoblen als receptors per mecanismes capacitius i inductius.

Les **involuntàries** sorgeixen com a productes secundaris d'altres sistemes. La **interferència de xarxa** n'és l'exemple més omnipresent: la distribució elèctrica de l'edifici és una font ubiqua que no es limita als 50 Hz, ja que els components no lineals de les fonts commutades, els rectificadors i els inductors saturats generen harmònics a múltiples de la fonamental. Els **motors elèctrics**, sobretot amb variadors de freqüència (VFD), combinen components de baixa freqüència (modulació de la velocitat) i d'alta freqüència i banda ampla (commutació de l'electrònica de potència). Les **eines elèctriques** produeixen interferència per arcs elèctrics, amb espectres de banda ampla de centenars de Hz a centenars de MHz; el seu caràcter impulsiu les fa especialment perilloses perquè, malgrat durar poc, distribueixen energia en una banda molt gran. Finalment, els **sistemes d'ignició** d'automòbils generen impulsos de tensió a les bobines primàries que s'acoblen als sistemes propers.

## 4 Classificació per canal de transmissió

El canal de transmissió és el camí físic pel qual l'energia viatja de la font al receptor, i és el criteri més útil per al disseny i la mitigació, ja que identifica **on** actuar. Es distingeix entre interferències **conduïdes** i **radiades**; a baixes freqüències, les radiades es poden separar en **capacitives** (de camp elèctric) i **inductives** (de camp magnètic).

### Interferències conduïdes

Les interferències **conduïdes** (o resistives) sorgeixen quan corrents elèctrics no desitjats circulen pels mateixos conductors que transporten el senyal útil, o pels conductors de terra i retorn comuns. L'energia es propaga de forma guiada, no lliure per l'espai. El mecanisme fonamental és el següent: quan un corrent interferent

$$
I_f
$$

  circula per un conductor de terra o retorn amb impedància

$$
Z_\mathrm{terra}
$$

, hi apareix una caiguda de tensió

$$
V_\mathrm{interferent} = I_f \cdot Z_\mathrm{terra} \qquad (3.2)
$$

Si el senyal útil està referit al mateix conductor de terra en un **punt diferent**, la diferència de potencial entre els dos punts de terra contamina la mesura. Aquesta impedància compartida entre els circuits de la font d'interferència i del receptor sol ser el conductor de protecció de terra de la instal·lació. El seu caràcter varia amb la freqüència: a 50 o 100 Hz és predominantment **resistiu** (un conductor d'1 m i 1 mm² té una resistència d'alguns mil·liohms), però a partir dels quilohertz domina la **inductància**. Un conductor d'1 m presenta una inductància de l'ordre d'1 µH, que a 100 kHz equival a una impedància

$$
Z = j\,\omega L = j\,2\pi \cdot 10^{5}\,\mathrm{Hz} \cdot 10^{-6}\,\mathrm{H} \approx j\,0{,}63\ \Omega
$$

Per això els transitoris de commutació ràpida (amb

$$
\frac{\mathrm{d}i}{\mathrm{d}t}
$$

  elevat) s'acoblen molt més fàcilment que la freqüència fonamental lenta de la xarxa. L'anàlisi detallada del model circuital d'una interferència conduïda, amb les impedàncies dels cables i el bucle de massa, es desenvolupa al document 2.

### Interferències radiades: camp proper i camp llunyà

Les interferències **radiades** són fruit dels camps electromagnètics de la font, i la seva anàlisi depèn de la freqüència i de la separació entre font i receptor. La longitud d'ona d'un senyal de freqüència

$$
f
$$

  és

$$
\lambda = \frac{c}{f} \qquad (3.3)
$$

on

$$
c
$$

  és la velocitat de la llum. Així, a 50 Hz

$$
\lambda \approx 6\,000
$$

  km; a 1 MHz,

$$
\lambda \approx 300
$$

  m; i a 1 GHz,

$$
\lambda \approx 0{,}3
$$

  m. La frontera entre camp proper i llunyà se situa aproximadament a

$$
r \approx \lambda/2\pi \approx 0{,}16\,\lambda
$$

. Els sistemes de mesura típics (de centímetres a metres) estan gairebé sempre en **camp proper** respecte a interferències de freqüència baixa (per sota d'uns 100 MHz).

La distinció és fonamental. En **camp proper**, els camps elèctric

$$
E
$$

  i magnètic

$$
H
$$

  són independents: pot existir energia de camp elèctric sense camp magnètic apreciable (acoblament capacitiu pur) o a l'inrevés (acoblament inductiu pur). En **camp llunyà**, en canvi,

$$
E
$$

  i

$$
H
$$

  estan lligats per la impedància característica de l'espai, que al buit val

$$
E/H = 377\ \Omega
$$

. Com que en els sistemes de mesura els problemes solen correspondre a camp proper, és lícit separar l'anàlisi en interferències capacitives i inductives, que es tracten als documents 3 i 4 respectivament.

> [!TIP] **Síntesi**
>
> Soroll i interferència degraden tots dos la mesura, però el soroll és aleatori, de banda ampla i intern, mentre que la interferència és periòdica, d'espectre estret i generalment externa i humana; per això es redueixen amb estratègies oposades i la interferència s'ataca, sobretot, tallant el canal. Tot problema electromagnètic s'estructura en font, canal i receptor, i el marc EMC (Directiva 2014/30/UE, sèrie IEC 61000) en fixa límits d'emissió i immunitat sense garantir l'absència de problemes reals. Les interferències es classifiquen per origen — naturals (llamps, ESD, tempestes solars, radiació còsmica) o artificials, intencionades o involuntàries — i per canal — conduïdes o radiades —; en camp proper, on operen gairebé sempre els sistemes de mesura, el camp elèctric i el magnètic són independents i permeten separar l'anàlisi capacitiva de la inductiva.

[← Índex](#unitat-3-interferències-en-sistemes-de-mesura)[2. Mode diferencial i comú. Interferències conduïdes →](#u3-2-mode-diferencial-i-comú-interferències-conduïdes)

Sistemes de Mesura (230920) · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB – UPC
Material de lectura prèvia · Unitat 3: Interferències en Sistemes de Mesura

---

<!-- FIN CAPÍTULO: 01_doc -->

---

<!-- INICIO CAPÍTULO: 02_doc -->

# U3 · 2. Mode diferencial i comú. Interferències conduïdes

> [!NOTE] **Objectius d'aprenentatge**
>
> - Definir la tensió en **mode diferencial** i en **mode comú** i relacionar-les amb el senyal útil i amb la interferència.
> - Interpretar el **rebuig de mode comú (CMRR)**, convertir-lo entre decibels i factor lineal, i explicar-ne la dependència amb la freqüència.
> - Analitzar els **quatre casos** de connexió a terra de font i sistema de mesura, i calcular la tensió interferent i el CMRR de cada configuració.
> - Distingir les interferències conduïdes **externes** (corrent de fuita per terra) de les **internes** (transformador d'alimentació) i enumerar-ne les tècniques de mitigació.

Al document anterior s'ha vist que una interferència es pot classificar pel canal de transmissió i que les **conduïdes** es propaguen de manera guiada pels conductors. Abans d'analitzar-les en detall cal introduir com apareix una tensió interferent als terminals d'entrada del receptor, és a dir, el **mode d'acoblament**.

## 1 Mode diferencial i mode comú

El receptor d'interferència — el sistema de mesura — es modela com una impedància d'entrada

$$
Z_d
$$

  i un node de **referència** de tensió respecte al qual es mesuren totes les tensions. El mode d'acoblament determina quina tensió provoca la interferència en bornes de

$$
Z_d
$$

, i és decisiu perquè cada mode exigeix estratègies de mitigació diferents.

Una interferència en **mode diferencial** (o mode sèrie, o normal) es manifesta directament com una tensió entre els dos terminals de mesura (figura 3.4):

$$
V_d = V_A - V_B \qquad (3.4)
$$

![Acoblament en mode diferencial](assets/02_doc_img_1.png)

*Figura: Figura 3.4. Acoblament d'interferència en mode diferencial: el generador modela la interferència, en sèrie amb el senyal, entre els terminals A i B.*

És el mode d'acoblament més directe, perquè la interferència actua exactament com la magnitud que el circuit està dissenyat per mesurar: una diferència de potencial entre dos punts. Quan s'introdueix, se suma al senyal útil i un amplificador no la pot discriminar basant-se només en la tensió diferencial; només se'n pot rebutjar si té característiques temporals o espectrals que la diferenciïn del senyal. Per exemple, un convertidor analògic–digital **integrador** ofereix rebuig de mode sèrie (SMRR) a freqüències concretes: si integra durant un temps

$$
T
$$

, el seu guany per a una interferència sinusoïdal de freqüència

$$
f
$$

  és proporcional a

$$
g(f) \propto \frac{\sin(\pi f T)}{\pi f T} \qquad (3.5)
$$

que s'anul·la quan

$$
fT
$$

  és un nombre enter. Per això els multímetres digitals que integren durant 20 ms (un període complet de xarxa a 50 Hz) rebutgen tan bé la interferència de xarxa: el temps d'integració conté un nombre enter de períodes de la interferència.

La **tensió de mode comú** es defineix, respecte al node de referència, com la mitjana de les tensions dels dos terminals:

$$
V_c = \frac{V_A + V_B}{2} \qquad (3.6)
$$

Tota interferència diferencial porta associat, en general, un cert mode comú, excepte en el cas particular

$$
V_A = -V_B
$$

. Una interferència en **mode comú** (o transversal) afecta ambdós terminals amb aproximadament la mateixa tensió i fase (figura 3.5) i, idealment, no s'hauria de manifestar en el senyal detectat, perquè la diferència de tensió a l'entrada seria nul·la.

![Acoblament en mode comú](assets/02_doc_img_2.png)

*Figura: Figura 3.5. Acoblament d'interferència en mode comú: ambdós terminals es desplacen alhora (

$$
V_B = V_A
$$

 ) respecte a la referència.*

A la pràctica, però, cap circuit real rebutja perfectament el mode comú: les impedàncies dels cables són baixes però no nul·les ni idèntiques per als dos terminals, de manera que part del mode comú es converteix en mode diferencial. A més, la impedància entre cada node i la referència no és infinita.

### Rebuig de mode comú (CMRR)

El **rebuig de mode comú** es defineix com la relació entre el guany del sistema per al mode diferencial i el guany, no volgut, per al mode comú:

$$
\mathrm{CMRR} = \frac{A_d}{A_c}, \qquad \mathrm{CMRR}_{\mathrm{dB}} = 20\log_{10}\frac{A_d}{A_c} \qquad (3.7)
$$

de manera que el factor lineal es recupera com

$$
\mathrm{CMRR} = 10^{\,\mathrm{CMRR}_{\mathrm{dB}}/20}
$$

. Així, una interferència de mode comú d'1 V en un sistema amb un CMRR de 80 dB es manifesta com una pertorbació diferencial equivalent de només 0,1 mV.

El CMRR **no és constant en freqüència**: típicament disminueix en pujar la freqüència, sobretot per als acoblaments capacitius. Un amplificador amb 100 dB en contínua pot quedar-se en 60 dB a 1 kHz i 40 dB a 10 kHz. La causa és la capacitat paràsita de mode comú, que crea una via de fuita per als senyals ràpids; per això, en sistemes diferencials ben dissenyats, les impedàncies de mode comú dels dos camins es mantenen **simètriques**, ja que qualsevol desequilibri converteix mode comú en mode diferencial irrebutjable.

## 2 Interferències conduïdes externes

Les interferències conduïdes es transmeten a través dels conductors (de senyal, d'alimentació o de terra) i tenen el seu mecanisme en una **impedància comuna** entre la font d'interferència i el receptor. En un edifici, la xarxa de distribució interconnecta molts equips; quan diversos es posen a terra en punts diferents, la impedància del conductor de protecció fa que el potencial de terra no sigui idèntic a tot arreu, i els corrents de fuita que hi circulen generen tensions interferents. La figura 3.6 mostra el model d'anàlisi.

![Model elèctric d'interferència conduïda](assets/02_doc_img_3.png)

*Figura: Figura 3.6. Model elèctric per a l'anàlisi d'interferències conduïdes. Es vol mesurar

$$
V_s
$$

 (amb impedància

$$
Z_s
$$

 ) amb un sistema

$$
Z_d
$$

; els cables tenen impedàncies

$$
Z_a
$$

 i

$$
Z_b
$$

, i entre les dues referències de terra M i M' hi ha la impedància del conductor de protecció

$$
Z_{\text{cp}}
$$

. El corrent de fuita

$$
I_f
$$

 tanca el circuit per terra.*

Els ordres de magnitud de les impedàncies condicionen tota l'anàlisi. La impedància de sortida de la font

$$
Z_s
$$

  sol ser baixa en instruments (50 Ω o menys), però pot arribar a MΩ o GΩ en alguns sensors. Els cables de mesura d'1 m i 1 mm² presenten

$$
Z_a, Z_b
$$

  de l'ordre de 0,01–0,1 Ω a baixa freqüència. La impedància d'entrada

$$
Z_d
$$

  és molt alta (MΩ), cosa que fa que els corrents de fuita retornin gairebé tots pel conductor baix i no per

$$
Z_d
$$

. Finalment, el conductor de protecció

$$
Z_{\text{cp}}
$$

  (coure, resistivitat ≈ 0,017 Ω·mm²/m a 25 °C) pot valer de 0,1 a 1 Ω o més en instal·lacions grans, i el seu caràcter passa de resistiu a inductiu en pujar la freqüència.

Aquestes interferències s'originen en els **corrents de fuita a terra**: corrents que van, de manera no intencionada, del circuit d'alimentació d'un equip al conductor de protecció, per capacitats paràsites de les fonts, filtres de xarxa amb condensadors a terra, aïllament degradat o contactes accidentals. En una oficina o laboratori amb 5–10 equips solen acumular 50–200 mA eficaços a 50 Hz, i en instal·lacions industrials, diversos amperes. El conductor de protecció és imprescindible per **seguretat** — manté les parts metàl·liques accessibles a potencial de terra i força la desconnexió en cas de defecte —, però la seva impedància distribuïda és, precisament, l'origen del problema de mesura.

L'impacte depèn de la classe de seguretat dels equips interconnectats (figura 3.7 i 3.8). Els equips de **classe I** connecten les parts metàl·liques accessibles al conductor de protecció (cable de tres conductors); les seves fonts commutades injecten corrents de fuita de 0,5 a 2 mA eficaços i, per tant, són la causa de les interferències conduïdes externes: són equips *posats a terra* (oscil·loscopis, generadors de funcions; qualsevol equip amb connectors BNC). Els equips de **classe II** es protegeixen amb **doble aïllament**, són *flotants* (la seva massa és independent de la terra de la instal·lació) i tenen connectors de banana amb aïllament reforçat (multímetres i fonts de laboratori); aquest reforç n'encareix el preu. Els de **classe III** s'alimenten a tensió de seguretat molt baixa (≤ 50 V en alterna) i no generen corrents de fuita significatius.

![Equips connectats a la instal·lació elèctrica](assets/02_doc_img_4.png)

*Figura: Figura 3.7. Conjunt d'equips connectats a la xarxa (fase, neutre i terra): part del corrent de fase es desvia cap al conductor de protecció com a corrent de fuita.*

![Símbols de les classes d'equips I, II i III](assets/02_doc_img_5.png)

*Figura: Figura 3.8. Símbols identificadors de les classes de seguretat elèctrica: classe I (posada a terra), classe II (doble aïllament) i classe III (tensió de seguretat molt baixa).*

L'efecte de la interferència depèn de com es connectin font i sistema de mesura respecte a terra. S'analitzen els quatre casos rellevants.

### Cas 1: font a terra + mesura a terra

És el cas més simple i sovint el més problemàtic, ja que representa la majoria d'equips de classe I (per exemple, un generador de funcions connectat a un oscil·loscopi). El corrent de fuita

$$
I_f
$$

  arriba al node M' i es reparteix entre tres camins en paral·lel: per

$$
Z_{\text{cp}}
$$

, per

$$
Z_b
$$

  i, de manera negligible, per

$$
Z_d
$$

  (perquè

$$
Z_d+Z_a+Z_s \gg Z_{\text{cp}}, Z_b
$$

 ). Prescindint de signes (senyals d'alterna), la tensió entre masses és

$$
V_{MM'} = I_f \,(Z_b \parallel Z_{\text{cp}}) = I_f\,\frac{Z_b\,Z_{\text{cp}}}{Z_b + Z_{\text{cp}}} \qquad (3.8)
$$

i, com que

$$
Z_d \gg Z_a + Z_s
$$

, gairebé tota aquesta tensió apareix a l'entrada:

$$
V_d|_{I_f} = V_{MM'}\,\frac{Z_d}{Z_d + Z_a + Z_s} \approx V_{MM'} \qquad (3.9)
$$

![Model del cas 1](assets/02_doc_img_6.png)

*Figura: Figura 3.9. Cas 1: font i sistema de mesura posats a terra en punts diferents (M i M').*

**Exemple.** Amb

$$
Z_s = 50\ \Omega
$$

,

$$
Z_a = 1\ \Omega
$$

,

$$
Z_d = 1\ \mathrm{M\Omega}
$$

,

$$
Z_b = 1\ \Omega
$$

,

$$
Z_{\text{cp}} = 0{,}1\ \Omega
$$

  i

$$
I_f = 20\ \mathrm{mA}
$$

  eficaços, el paral·lel val

$$
Z_b \parallel Z_{\text{cp}} = (1)(0{,}1)/(1{,}1) \approx 0{,}091\ \Omega
$$

  i la tensió interferent a l'entrada és

$$
V_d \approx 20\ \mathrm{mA} \times 0{,}091\ \Omega \approx 1{,}82\ \mathrm{mV}
$$

  eficaços. Una interferència prou gran per contaminar mesures de baix nivell.

### Cas 2: font flotant + mesura a terra

Quan la font s'aïlla de terra (bateries o transformador d'aïllament), entre la seva massa i terra apareix una impedància paràsita

$$
Z_A
$$

  deguda a capacitats paràsites (10–100 pF), aïllament imperfecte o contactes accidentals. Es comporta com a resistiva a molt baixa freqüència (10–100 MΩ a 50 Hz, fins a GΩ en contínua) i cau a l'ordre de kΩ per sobre d'1 MHz. Com que

$$
Z_A \gg Z_{\text{cp}}
$$

, el corrent de fuita circula pràcticament sencer per

$$
Z_{\text{cp}}
$$

, i la tensió de mode comú és

$$
V_c = V_{MM'} = I_f Z_{\text{cp}}
$$

. Aquesta tensió es reparteix pel divisor

$$
Z_b
$$

 –

$$
Z_A
$$

:

$$
V_d|_{I_f} = V_c\,\frac{Z_b}{Z_b + Z_A} \approx V_c\,\frac{Z_b}{Z_A} = \frac{V_c}{\mathrm{CMRR}}, \qquad \mathrm{CMRR} = \frac{Z_A}{Z_b} \qquad (3.10)
$$

![Model del cas 2](assets/02_doc_img_7.png)

*Figura: Figura 3.10. Cas 2: font flotant (impedància d'aïllament

$$
Z_A
$$

 ) i sistema de mesura posat a terra.*

Aquesta configuració converteix la interferència en una tensió de **mode comú** que el CMRR del circuit atenua. La millora respecte al cas 1 és enorme: si al cas 1 s'identifica

$$
V_c = I_f Z_{\text{cp}}
$$

, el seu CMRR efectiu és només

$$
\mathrm{CMRR}_{\mathrm{cas 1}} = 1 + Z_{\text{cp}}/Z_b
$$

, amb

$$
Z_{\text{cp}}
$$

  i

$$
Z_b
$$

  comparables (factor proper a 2). En canvi, amb

$$
Z_b = 0{,}1\ \Omega
$$

  i

$$
Z_A = 10\ \mathrm{M\Omega}
$$

  a 50 Hz, el cas 2 dóna

$$
\mathrm{CMRR} = 10^{8}
$$

, és a dir **160 dB**: el mode comú s'atenua en vuit ordres de magnitud.

### Cas 3: font a terra + mesura flotant

Ara és el sistema de mesura el que està aïllat de terra (per exemple, un generador connectat a un multímetre); l'aïllament del mesurador es modela amb una impedància

$$
Z_{\text{bt}}
$$

, anàloga a

$$
Z_A
$$

. El corrent de fuita torna a circular per

$$
Z_{\text{cp}}
$$

  creant

$$
V_c = I_f Z_{\text{cp}}
$$

, que ara es reparteix entre

$$
Z_b
$$

  i

$$
Z_{\text{bt}}
$$

:

$$
V_d|_{I_f} = V_c\,\frac{Z_b}{Z_{\text{bt}}} = \frac{V_c}{\mathrm{CMRR}}, \qquad \mathrm{CMRR} = \frac{Z_{\text{bt}}}{Z_b} \qquad (3.11)
$$

![Model del cas 3](assets/02_doc_img_8.png)

*Figura: Figura 3.11. Cas 3: font posada a terra i sistema de mesura flotant (impedància d'aïllament

$$
Z_{\text{bt}}
$$

 ).*

Els fabricants de multímetres solen informar de

$$
Z_{\text{bt}}
$$

  de manera indirecta, donant el CMRR a diverses freqüències per a una impedància de desequilibri

$$
Z_b
$$

  elevada (típicament 1 kΩ).

**Exemple.** Si un fabricant declara un CMRR de 100 dB en contínua i de 70 dB a 50 Hz per a

$$
Z_b = 1\ \mathrm{k\Omega}
$$

, la resistència d'aïllament és

$$
Z_{\text{bt}} = 1\ \mathrm{k\Omega} \times 10^{100/20} = 1\ \mathrm{k\Omega} \times 10^{5} = 100\ \mathrm{M\Omega}
$$

. A 50 Hz, el mòdul ja ha baixat a

$$
1\ \mathrm{k\Omega} \times 10^{70/20} \approx 3{,}16\ \mathrm{M\Omega}
$$

, dominat per la component capacitiva; aquesta reactància de 3,16 MΩ a 50 Hz correspon a una capacitat d'aïllament

$$
C = \frac{1}{2\pi \cdot 50 \cdot 3{,}16\times10^{6}} \approx 1\ \mathrm{nF}
$$

.

### Cas 4: font flotant + mesura flotant

És la configuració més favorable per a mesures de baix nivell i baixa freqüència, tot i que la millora respecte als casos 2 i 3 no és gran, perquè el CMRR el dicta la més gran de les dues impedàncies d'aïllament. El corrent torna a circular per

$$
Z_{\text{cp}}
$$

  i la tensió a l'entrada és

$$
V_d|_{I_f} = I_f\,Z_{\text{cp}}\,\frac{Z_b}{Z_A + Z_{\text{bt}}} \qquad (3.12)
$$

![Model del cas 4](assets/02_doc_img_9.png)

*Figura: Figura 3.12. Cas 4: font i sistema de mesura tots dos flotants. El CMRR ve donat pel quocient entre la suma de les impedàncies d'aïllament i la impedància del cable baix.*

## 3 Interferències conduïdes internes

Les interferències conduïdes **internes** no travessen el conductor de protecció, sinó que penetren pel propi cable d'alimentació de l'equip. La xarxa, nominalment a 230 V i 50 Hz, transporta també harmònics d'equips no lineals, interferències acoblades i transitoris de commutació, amb freqüències que arriben a centenars de kHz o MHz. Aquestes pertorbacions entren a l'equip per acoblament **capacitiu** a través del transformador de la font d'alimentació.

![Model del transformador de la font d'alimentació](assets/02_doc_img_10.png)

*Figura: Figura 3.13. Transformador de la font d'alimentació. Les capacitats paràsites

$$
C_{\text{fm}}
$$

 (fase–massa) i

$$
C_{\text{nm}}
$$

 (neutre–massa) entre primari i secundari permeten el pas de corrents d'alta freqüència de la xarxa cap als circuits de baix nivell.*

Idealment el transformador aïllaria completament primari i secundari, però la proximitat dels debanats crea capacitats paràsites

$$
C_{\text{fm}}
$$

  (fase–massa del secundari) i

$$
C_{\text{nm}}
$$

  (neutre–massa). En transformadors amb nucli de ferrita valen de 100 pF a 10 nF; els **transformadors d'aïllament amb pantalla de blindatge** les redueixen a només 5–10 pF. La pertorbació predomina per

$$
C_{\text{fm}}
$$

  (representada per

$$
Z_{\text{fm}}
$$

 ), perquè la fase transporta la tensió principal, mentre que el neutre, referenciat a terra, aporta menys. El model de Norton equivalent considera la font

$$
V_f
$$

  amb impedància

$$
Z_{\text{fm}} \parallel Z_{\text{nm}}
$$

  (figura 3.14 representa el cas típic on s'interconnecta una font posada a terra amb un sistema de mesura flotant).

![Equivalent Norton de la interferència interna](assets/02_doc_img_11.png)

*Figura: Figura 3.14. Equivalent Norton per a l'anàlisi de l'efecte de les interferències del conductor de fase, amb

$$
I_f = V_f/Z_{\text{fm}}
$$

.*

Com que

$$
Z_b \ll Z_d+Z_a+Z_s
$$

,

$$
Z_b \ll Z_{\text{bt}}+Z_{\text{cp}}
$$

  i

$$
Z_b \ll Z_{\text{fm}}\parallel Z_{\text{nm}}
$$

, el corrent circula majoritàriament per

$$
Z_b
$$

  i la tensió a l'entrada és

$$
V_d|_{V_f} = \frac{V_f}{Z_{\text{fm}}}\,Z_b \qquad (3.13)
$$

Com més alta és la freqüència, més petita és

$$
Z_{\text{fm}}
$$

  i, per tant, més gran l'efecte de la interferència interna.

## 4 Tècniques de mitigació de les interferències conduïdes

L'objectiu és reduir la tensió que apareix en bornes de

$$
Z_d
$$

. Per a les interferències **externes**, l'estratègia més bàsica és **minimitzar les impedàncies dels camins de retorn**: augmentar la secció del cable baix (passar d'1 a 4 mm² en divideix la resistència per quatre, amb més cost i pes) o — sovint més efectiu econòmicament — escurçar-lo (reduir-ne la longitud a la meitat en divideix la impedància a la meitat sense cost de material).

Una segona via és **reduir el corrent de fuita total**

$$
I_f
$$

, desconnectant de la xarxa els equips no essencials: els de classe I injecten corrent de fuita fins i tot en *standby*, perquè la font commutada segueix activa. Té límits, però: en sales amb 20–30 instruments els corrents acumulats són inevitables, i afegir interruptors individuals encareix el sistema i introdueix punts de fallida.

La tàctica **més efectiva** és emprar sistemes de mesura **flotants** (classe II) en lloc de connectats a terra (classe I). En un sistema flotant, la tensió

$$
I_f Z_{\text{cp}}
$$

  apareix com a mode comú a l'entrada, i el CMRR del sistema determina quina fracció es converteix en tensió diferencial: un CMRR elevat atenua dràsticament l'efecte, tal com quantifiquen els casos 2 i 4. Les interferències **internes** es combaten, sobretot, amb transformadors d'aïllament amb pantalla, que redueixen les capacitats paràsites

$$
C_{\text{fm}}
$$

  i

$$
C_{\text{nm}}
$$

  i, per tant, augmenten

$$
Z_{\text{fm}}
$$

.

A l'entrada d'alimentació dels equips també s'hi afegeixen elements dedicats. Els **filtres de xarxa** (filtres EMI) combinen bobines en sèrie amb la fase i condensadors entre fase, neutre i terra: aquests condensadors ofereixen un camí de baixa impedància que deriva a terra els corrents interferents d'alta freqüència, mentre deixen passar el senyal de 50 Hz gairebé sense atenuar. La seva banda de rebuig s'estén d'uns pocs kHz a centenars de MHz, amb atenuacions de 30–60 dB per sobre de 100 kHz. Contra els **transitoris** de la xarxa (llamps, connexió i desconnexió de motors), que poden assolir centenars o milers de volts durant microsegons, s'empren **supressors de transitoris**: varistors d'òxid de metall (**MOV**) i díodes supressors (**TVS**), que desvien ràpidament la sobretensió a terra i limiten la tensió que arriba als circuits a un valor segur. Aquests supressors no filtren la interferència periòdica — ni tenen res a veure amb el guany de l'amplificador —, sinó que protegeixen l'equip de l'energia impulsiva. Finalment, quan la interferència no s'ha pogut eliminar del tot, encara es pot **filtrar el senyal mesurat** (analògicament o digitalment) i promitjar diverses mesures, sempre que la interferència no hagi saturat abans cap etapa de la cadena.

> [!TIP] **Síntesi**
>
> Una interferència s'acobla en mode diferencial (entre terminals, se suma al senyal i només es rebutja per criteris temporals o espectrals, com l'ADC integrador a 20 ms) o en mode comú (desplaça els dos terminals alhora i el rebutja el CMRR, que es mesura en dB i cau amb la freqüència). Les interferències conduïdes externes neixen del corrent de fuita a terra que circula per la impedància del conductor de protecció; la seva magnitud depèn de com es connectin font i sistema de mesura, i els quatre casos mostren que flotar qualsevol dels dos equips converteix la interferència en mode comú i n'eleva enormement el CMRR (fins a 160 dB en el cas 2). Les interferències internes entren pel transformador d'alimentació a través de les capacitats paràsites

$$
C_{\text{fm}}
$$

  i

$$
C_{\text{nm}}
$$

. La mitigació passa per minimitzar les impedàncies de retorn, reduir el corrent de fuita, emprar sistemes flotants d'alt CMRR i transformadors d'aïllament amb pantalla.

[← 1. Fonaments i classificació de les interferències](#u3-1-fonaments-i-classificació-de-les-interferències)[3. Interferències capacitives i blindatge →](#u3-3-interferències-capacitives-i-blindatge)

Sistemes de Mesura (230920) · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB – UPC
Material de lectura prèvia · Unitat 3: Interferències en Sistemes de Mesura

---

<!-- FIN CAPÍTULO: 02_doc -->

---

<!-- INICIO CAPÍTULO: 03_doc -->

# U3 · 3. Interferències capacitives i blindatge

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar el mecanisme de l'**acoblament capacitiu** com un corrent de desplaçament proporcional a

$$
\frac{\mathrm{d}V}{\mathrm{d}t}
$$

  a través d'una capacitat paràsita.
> - Estimar la tensió interferent amb el model de capacitats i relacionar-la amb la impedància d'entrada i la freqüència (

$$
Z_C = \frac{1}{j2\pi fC}
$$

 ).
> - Justificar el **blindatge** com a gàbia de Faraday i la importància de connectar-lo a la referència correcta.
> - Analitzar la limitació d'amplada de banda del **cable coaxial** i com la **sonda atenuadora compensada** l'estén a canvi d'atenuar el senyal.

Al camp proper, el camp elèctric i el magnètic són independents (document 1), de manera que l'acoblament radiat es pot separar en capacitiu i inductiu. Aquest document tracta l'**acoblament capacitiu** — de camp elèctric — i la tècnica principal per combatre'l, el blindatge.

## 1 Mecanisme de l'acoblament capacitiu

Entre dos conductors qualssevol separats per un dielèctric sempre hi ha una capacitat. Si un dels conductors està a un potencial **variable**

$$
V(t)
$$

  respecte a terra i l'altre forma part del circuit de mesura, per la capacitat hi circula un **corrent de desplaçament**

$$
i_C = C\,\frac{dV}{dt} \qquad (3.14)
$$

La dependència de

$$
\frac{\mathrm{d}V}{\mathrm{d}t}
$$

  és essencial: l'acoblament el provoca la *variació* de tensió de la font interferent, no un corrent elevat; una tensió constant, per gran que sigui, no acobla res. Per la mateixa raó, com més alta és la freqüència, més gran és el corrent injectat.

**Exemple.** Una capacitat de 50 pF — valor típic entre un cable de xarxa i un conductor de senyal separats 10 cm al llarg d'1 m — sotmesa a la tensió de xarxa de 230 V eficaços a 50 Hz injecta

$$
i_C = 50\ \mathrm{pF}\times 2\pi\times 50\ \mathrm{Hz}\times 230\ \mathrm{V} \approx 3{,}6\ \mathrm{\mu A}
$$

. Si aquest corrent entra en un circuit d'alta impedància (1 MΩ), hi desenvolupa

$$
V = 3{,}6\ \mathrm{\mu A}\times 1\ \mathrm{M\Omega} = 3{,}6\ \mathrm{V}
$$

. Amb una capacitat minúscula, la tensió interferent és de volts: per això els circuits d'alta impedància són tan susceptibles a l'acoblament capacitiu — a igualtat de corrent, com més alta és la impedància d'entrada, més gran és la tensió interferent, no pas menor.

Per analitzar-ho quantitativament es modelen dos conductors (1 i 2) amb una massa comuna M (figura 3.15). La capacitat

$$
C_{1M}
$$

  queda en paral·lel amb la font d'interferència

$$
V_1
$$

  i no afecta la tensió a

$$
Z_d
$$

; la capacitat

$$
C_{2M}
$$

  modifica la impedància equivalent del receptor; i el **canal** que acobla la interferència és la capacitat paràsita

$$
C_{12}
$$

  entre els dos conductors, el valor de la qual depèn de la geometria.

![Model d'acoblament capacitiu](assets/03_doc_img_1.png)

*Figura: Figura 3.15. Model d'acoblament capacitiu entre la font d'interferència

$$
V_1
$$

 (conductor 1) i el circuit receptor (conductor 2, amb

$$
Z_s
$$

 i

$$
Z_d
$$

 ). El canal és la capacitat paràsita

$$
C_{12}
$$

.*

La impedància de la capacitat d'acoblament és

$$
Z_{C_{12}} = \frac{1}{j\,2\pi f\,C_{12}} \qquad (3.15)
$$

— que disminueix en pujar la freqüència — i, resolent el divisor, la tensió interferent a l'entrada resulta

$$
V_i|_{V_1} = V_1\,\frac{j\,2\pi f\,C_{12}}{\,j\,2\pi f\,(C_{12}+C_{2M}) + \frac{Z_d+Z_s}{Z_d\,Z_s}\,} \qquad (3.16)
$$

Aquestes capacitats paràsites apareixen a tot arreu — entre els cables de xarxa i els de mesura, entre la carcassa i les entrades, dins dels transformadors, entre pistes d'una placa — amb valors que van de picofarads (circuits ben dissenyats) a nanofarads (transformadors mal blindats).

### Geometries habituals

El valor de

$$
C_{12}
$$

  depèn de la geometria i de la permitivitat del dielèctric (figura 3.16). Per a dos conductors cilíndrics paral·lels de radis

$$
r_1, r_2
$$

  separats una distància

$$
d \gg r
$$

  al llarg d'una longitud

$$
\ell
$$

,

$$
C_{12} \approx \frac{\pi\,\varepsilon_r\,\varepsilon_0\,\ell}{\ln\!(d/\sqrt{r_1 r_2})} \qquad (3.17)
$$

amb

$$
\varepsilon_0 = 8{,}854\times10^{-12}
$$

  F/m i

$$
\varepsilon_r
$$

  la constant dielèctrica relativa. Per a dos conductors sobre un pla de massa a distància

$$
h
$$

  l'expressió inclou un factor addicional que depèn de

$$
h
$$

  i

$$
d
$$

, i per a un **cable coaxial** de radi intern

$$
a
$$

  i malla de radi

$$
b
$$

,

$$
C_{12} \approx \frac{2\pi\,\varepsilon_r\,\varepsilon_0\,\ell}{\ln(b/a)} \qquad (3.18)
$$

![Geometries: conductors paral·lels, sobre pla de massa, coaxial](assets/03_doc_img_2.png)

*Figura: Figura 3.16. Geometries habituals: (a) dos conductors paral·lels; (b) dos conductors sobre un pla de massa; (c) cable coaxial.*

## 2 Blindatge

Quan les tensions interferents estimades són inacceptables, cal actuar sobre el canal reduint

$$
C_{12}
$$

. El **blindatge** és la tècnica més efectiva: consisteix a envoltar completament la zona que es vol protegir amb un conductor connectat a una referència de potencial adequada. El blindatge es comporta com una **gàbia de Faraday** — les càrregues es distribueixen a la superfície de manera que el camp interior és nul — i les càrregues induïdes per la font es deriven directament a la referència del blindatge sense circular pel circuit de senyal.

![Blindatge d'un circuit sensible](assets/03_doc_img_3.png)

*Figura: Figura 3.17. Blindatge d'un circuit sensible enfront de la interferència de xarxa. La capacitat blindatge–xarxa

$$
C_{\text{rc}}
$$

 queda en paral·lel amb

$$
V_r
$$

 i no afecta; en canvi, la capacitat residual blindatge–entrada

$$
C_{\text{ca}}
$$

 forma un passa-baixes amb la resistència de la font.*

La connexió a la referència correcta és **determinant**: per a interferències de la instal·lació, el blindatge s'ha de connectar a la terra de la instal·lació, de manera que les càrregues induïdes es derivin a terra; per a interferències internes (per exemple, un rellotge que s'acobla a una pista de baix nivell), s'ha de connectar a la massa de la font d'interferència. Un blindatge mal referenciat no protegeix. El blindatge té, però, un límit visible a la figura 3.17: entre el blindatge i el node d'entrada A queda una capacitat residual

$$
C_{\text{ca}}
$$

  que, amb la resistència de sortida de la font

$$
R_s
$$

, forma un filtre passa-baixes de freqüència de tall

$$
f_{-3\,\mathrm{dB}} = \frac{1}{2\pi R_s C_{\text{ca}}} \qquad (3.19)
$$

El blindatge adopta moltes formes: la carcassa metàl·lica exterior (efectiva només si els segments es contacten amb baixa impedància), gàbies internes de malla en plaques, làmines separadores i, sobretot, els **plans de massa** de les plaques multicapa, que actuen alhora com a referència única, com a gàbia de Faraday entre capes i com a retorn de baixa impedància. Un blindatge ben fet atenua 40–80 dB a baixa i mitjana freqüència, però cal preservar-ne la **continuïtat elèctrica**: les obertures — per exemple, per a ventilació — i els conductors que han de sortir *redueixen* la seva efectivitat.

## 3 Cable coaxial i limitació d'amplada de banda

Per interconnectar font i sistema de mesura enfront d'interferències capacitives s'empra cable **coaxial**: el conductor central porta el senyal i la malla actua de blindatge, connectada — en un únic punt, per evitar bucles de massa — a la referència de la font d'interferència (figura 3.18). Si la connexió de la malla és bona, la capacitat malla–xarxa

$$
C_{\text{rb}}
$$

  queda en paral·lel amb

$$
V_r
$$

  i la interferència residual és molt petita.

![Ús de cable coaxial apantallat](assets/03_doc_img_4.png)

*Figura: Figura 3.18. Cable coaxial apantallat: (a) connexió; (b) circuit equivalent. La malla (B'–B) connecta les referències i el conductor central (A'–A) porta el senyal;

$$
C_{\text{bA}}
$$

 és la capacitat entre malla i conductor central.*

**Exemple (interferència residual).** Amb un generador (

$$
Z_s = 50\ \Omega
$$

 ) connectat per coaxial a un oscil·loscopi (1 MΩ ∥ 13 pF), capacitat malla–central

$$
C_{\text{bA}} = 150\ \mathrm{pF}
$$

, resistència de malla i contacte

$$
Z_b = 0{,}07\ \Omega
$$

  i capacitat malla–xarxa

$$
C_{\text{rb}} = 15\ \mathrm{pF}
$$

: a 50 Hz,

$$
|Z_{C_{\text{rb}}}| = \frac{1}{2\pi\cdot 50\cdot 15\,\mathrm{pF}} \approx 212\ \mathrm{M\Omega} \gg Z_b
$$

, de manera que la interferència a l'entrada és

$$
V_{\text{AB}}|_{V_r} \approx 230\ \mathrm{V}\times \dfrac{0{,}07\ \Omega}{212\ \mathrm{M\Omega}} \approx 76\ \mathrm{nV}
$$

: l'apantallament la fa negligible.

Ara bé, el coaxial introdueix un problema propi. La seva capacitat (100–150 pF/m) se suma a la d'entrada de l'oscil·loscopi i, amb la resistència de la font, forma un passa-baixes que **retalla l'amplada de banda**.

**Exemple (amplada de banda).** Amb

$$
R_s \approx 50\ \Omega
$$

  (

$$
Z_s \parallel Z_d
$$

 ) i

$$
C_{\text{osc}}+C_{\text{bA}} = 13 + 150 = 163\ \mathrm{pF}
$$

, la freqüència de tall és

$$
f_{-3\,\mathrm{dB}} = \frac{1}{2\pi\cdot 50\ \Omega\cdot 163\ \mathrm{pF}} \approx 19{,}5\ \mathrm{MHz}
$$

. Encara que l'oscil·loscopi tingui 100 MHz d'amplada de banda, el cable ja la limita a uns 20 MHz.

## 4 Sondes atenuadores compensades

Per recuperar amplada de banda s'empren **sondes atenuadores** (la típica sonda x10). La punta afegeix una impedància en sèrie — el paral·lel d'una resistència

$$
R_p
$$

  (MΩ) i un condensador ajustable

$$
C_p
$$

  (pocs pF) — abans del cable i l'entrada de l'oscil·loscopi (figura 3.19). La funció de transferència

$$
V_{\text{in}}/V_s = Z_1/(Z_1+Z_2)
$$

, amb

$$
Z_1
$$

  el paral·lel de l'entrada de l'oscil·loscopi i el cable i

$$
Z_2
$$

  la impedància de la punta, esdevé **d'ordre zero** (independent de la freqüència) si es compleix la **condició de compensació**

$$
R_p\,C_p = R_{\text{osc}}\,(C_{\text{cable}}+C_{\text{osc}}) \qquad (3.20)
$$

![Model elèctric d'una sonda atenuadora](assets/03_doc_img_5.png)

*Figura: Figura 3.19. Model d'una sonda atenuadora: la punta (

$$
R_p \parallel C_p
$$

 ) en sèrie amb el cable (

$$
C_{\text{cable}}
$$

 ) i l'entrada de l'oscil·loscopi (

$$
R_{\text{osc}} \parallel C_{\text{osc}}
$$

 ).*

Amb

$$
R_p = (A-1)R_{\text{osc}}
$$

, la compensació exigeix

$$
C_p = (C_{\text{cable}}+C_{\text{osc}})/(A-1)
$$

, i aleshores la transferència és constant a totes les freqüències:

$$
H_{\text{comp}} = \frac{1}{A} \qquad (3.21)
$$

És a dir, el senyal s'**atenua** per un factor

$$
A
$$

  (10 en una sonda x10, de vegades 100). Cal subratllar que una sonda ben compensada *no* és un passa-baixes fortament dependent de la freqüència: precisament la compensació elimina aquesta dependència i deixa un guany pla. Incloent la resistència de sortida de la font

$$
R_g
$$

  (i amb

$$
R_g \ll R_p
$$

 ), el conjunt és un passa-baixes de primer ordre amb guany en contínua

$$
\approx \frac{1}{A}
$$

  i freqüència de tall

$$
f_{-3\,\mathrm{dB}} = \frac{A}{2\pi\,(C_{\text{osc}}+C_{\text{cable}})\,R_g} \qquad (3.22)
$$

**Exemple.** Amb

$$
R_{\text{osc}} = 1\ \mathrm{M\Omega}
$$

,

$$
C_{\text{osc}} = 13\ \mathrm{pF}
$$

,

$$
C_{\text{cable}} = 150\ \mathrm{pF}
$$

,

$$
R_g = 50\ \Omega
$$

  i una sonda x10 (

$$
A=10
$$

 ): la punta ha de tenir

$$
R_p = 9\ \mathrm{M\Omega}
$$

  i

$$
C_p = 163/9 \approx 18{,}1\ \mathrm{pF}
$$

. La freqüència de tall passa a

$$
f_{-3\,\mathrm{dB}} = 10/(2\pi\cdot 163\ \mathrm{pF}\cdot 50\ \Omega) \approx 195\ \mathrm{MHz}
$$

: l'amplada de banda s'estén per un factor igual a l'atenuació (deu vegades) respecte al cable coaxial sol, a canvi de dividir l'amplitud per deu.

> [!TIP] **Síntesi**
>
> L'acoblament capacitiu injecta un corrent de desplaçament

$$
i_C = C\,\frac{\mathrm{d}V}{\mathrm{d}t}
$$

  a través d'una capacitat paràsita: depèn de la *variació* de tensió i de la freqüència, i és més perjudicial com més alta és la impedància d'entrada del receptor. La impedància d'acoblament

$$
Z_C = \frac{1}{j2\pi fC}
$$

  disminueix amb la freqüència, i el valor de la capacitat depèn de la geometria (conductors paral·lels, sobre pla de massa, coaxial). La defensa principal és el blindatge, una gàbia de Faraday que ha d'anar connectada a la referència correcta i mantenir la continuïtat elèctrica, ja que obertures i sortides de cable en redueixen l'eficàcia. El cable coaxial protegeix però afegeix capacitat que, amb la resistència de la font, limita l'amplada de banda; la sonda atenuadora compensada (

$$
R_pC_p = R_{\text{osc}}(C_{\text{cable}}+C_{\text{osc}})
$$

 ) recupera una resposta plana i estén la banda per un factor igual a l'atenuació

$$
A
$$

, a costa de reduir el senyal a

$$
\frac{1}{A}
$$

.

[← 2. Mode diferencial i comú. Interferències conduïdes](#u3-2-mode-diferencial-i-comú-interferències-conduïdes)[4. Interferències inductives i efecte sobre la mesura →](#u3-4-interferències-inductives-i-efecte-sobre-la-mesura)

Sistemes de Mesura (230920) · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB – UPC
Material de lectura prèvia · Unitat 3: Interferències en Sistemes de Mesura

---

<!-- FIN CAPÍTULO: 03_doc -->

---

<!-- INICIO CAPÍTULO: 04_doc -->

# U3 · 4. Interferències inductives i efecte sobre la mesura

> [!NOTE] **Objectius d'aprenentatge**
>
> - Explicar l'**acoblament inductiu** per la llei de Faraday i la inductància mútua, i la seva dependència de

$$
\frac{\mathrm{d}I}{\mathrm{d}t}
$$

  i de la geometria.
> - Distingir la mitigació magnètica (blindatge d'alta permeabilitat, **trenat**, minimització de l'àrea de bucle) de l'elèctrica, i entendre per què la interferència magnètica és independent de la impedància del receptor.
> - Modelar l'efecte d'una interferència sobre el resultat: **valor mitjà nul**, relació

$$
\sigma = V_{\text{rms}}
$$

, distribució en U del mostreig i incertesa associada.
> - Quantificar el rebuig per **promitjat** i el **biaix** en mesures de valor eficaç, i sistematitzar la **diagnosi** font–canal–receptor.

Al camp proper, l'acoblament magnètic es pot analitzar separadament de l'elèctric (document 3). Aquest darrer document tracta les interferències **inductives**, la seva mitigació i, finalment, com afecta qualsevol interferència el resultat numèric d'una mesura.

## 1 Acoblament inductiu

Les interferències inductives es produeixen quan un corrent **variable** en un circuit indueix una tensió en un altre de proper. A diferència de l'acoblament capacitiu, el mecanisme és el camp magnètic: cal que circuli un corrent variable per la font — *no* n'hi ha prou amb una tensió elevada sense corrent associat. Tot corrent genera un camp magnètic; si aquest camp, variable, travessa l'àrea d'una malla del circuit de mesura, hi indueix una tensió en sèrie proporcional a la derivada del flux (llei de Faraday):

$$
V_i = -\frac{\partial \Phi}{\partial t} = -\frac{\partial}{\partial t}(B\,S\cos\theta) \qquad (3.23)
$$

on

$$
\theta
$$

  és l'angle entre el camp

$$
B
$$

  i l'àrea

$$
S
$$

  de la malla. L'acoblament entre els dos circuits es quantifica amb la **inductància mútua**

$$
L_m
$$

, de manera que

$$
V_i = -L_m\,\frac{dI_1}{dt} \qquad (3.24)
$$

essent

$$
I_1
$$

  el corrent de la font d'interferència. La inductància mútua depèn de la longitud en què els circuits discorren paral·lels, de la separació entre ells, de les dimensions dels conductors i de la permeabilitat del medi (aire,

$$
\mu_r \approx 1
$$

 ). La figura 3.20 mostra el model circuital, amb les autoinductàncies dels conductors

$$
L_1
$$

  i

$$
L_2
$$

  i la mútua

$$
L_m
$$

.

![Model d'acoblament inductiu](assets/04_doc_img_1.png)

*Figura: Figura 3.20. Model d'acoblament inductiu: el corrent

$$
I_1
$$

 de la font (

$$
V_1
$$

,

$$
Z_1
$$

 ) indueix, per la mútua

$$
L_m
$$

, una tensió al circuit receptor (

$$
V_s
$$

,

$$
Z_s
$$

,

$$
Z_d
$$

 ).*

La tensió induïda

$$
V_i
$$

  queda en sèrie dins la malla de mesura, i la que arriba a l'entrada es reparteix amb la impedància de la font i l'autoinductància dels cables:

$$
V_d = V_i\,\frac{Z_d}{Z_d + Z_s + j\,2\pi f\,L_2} \qquad (3.25)
$$

Com que la derivada d'un corrent sinusoïdal introdueix un factor

$$
2\pi f
$$

, **doblar la freqüència del corrent interferent duplica la tensió induïda** a igualtat d'amplitud. Per això els transitoris de commutació i els harmònics d'alta freqüència de la xarxa s'acoblen inductivament amb molta més facilitat que els 50 Hz, i els **motors** i **transformadors de potència**, amb corrents elevats, en són fonts rellevants.

### Geometria de la inductància mútua

Per a geometries típiques existeixen aproximacions de

$$
L_m
$$

  (figura 3.21). Per a dos conductors paral·lels a alçada

$$
h
$$

  sobre un pla de massa comú i separats

$$
d
$$

  al llarg d'una longitud

$$
\ell
$$

,

$$
L_m \approx \ell\,\frac{\mu_r \mu_0}{4\pi}\,\ln\!(1+\frac{4h^2}{d^2}) \qquad (3.26)
$$

amb

$$
\mu_0 = 4\pi\times10^{-7}
$$

  H/m. La mútua creix amb la longitud de paral·lelisme

$$
\ell
$$

  i amb l'alçada

$$
h
$$

, i decreix en separar els conductors (

$$
d
$$

 ). Per a dues malles — conductors 1–2 (font) i 3–4 (receptor) —,

$$
L_m \approx \ell\,\frac{\mu_r \mu_0}{4\pi}\,\ln\!(\frac{d_{14}\,d_{23}}{d_{13}\,d_{24}}) \qquad (3.27)
$$

![Geometries d'acoblament inductiu](assets/04_doc_img_2.png)

*Figura: Figura 3.21. Geometries d'acoblament inductiu: (a) dos conductors sobre un pla de massa; (b) dues malles (font 1–2, receptor 3–4).*

Aquesta expressió suggereix com **minimitzar** la interferència: fer que

$$
d_{14}
$$

  s'aproximi a

$$
d_{24}
$$

  i

$$
d_{23}
$$

  a

$$
d_{13}
$$

, cosa que s'aconsegueix acostant molt els conductors 1–2 entre si i els 3–4 entre si, és a dir, **minimitzant l'àrea de les malles**. Convé recordar que qualsevol malla tancada travessada per un camp magnètic variable pateix tensió induïda: fins i tot el bucle de massa entre dos punts de terra, sense corrent de fuita, capta un camp extern que apareix com a mode comú.

Una diferència fonamental amb l'acoblament capacitiu: la tensió inductiva en mode sèrie **no depèn de la impedància del receptor**. Per això augmentar la impedància d'entrada *no* elimina una tensió induïda magnèticament. Se sol dir que les interferències magnètiques afecten circuits de baixa impedància, però realment poden afectar-ne de qualsevol; el que passa és que, en circuits d'alta impedància, hi predomina l'acoblament capacitiu, perquè la caiguda deguda als corrents capacitius s'hi fa més gran.

## 2 Mitigació de les interferències inductives

El **blindatge magnètic** funciona per un principi diferent de l'elèctric: no n'hi ha prou amb un conductor connectat a una referència, sinó que cal un material que reculli el flux. La seva eficàcia depèn de la permeabilitat relativa: materials amb

$$
\mu_r \gg 1
$$

  (ferro, acer i, sobretot, **mu-metal** i permalloy, amb

$$
\mu_r
$$

  de fins a desenes de milers) redirigeixen les línies de camp a través seu i les aparten de la zona protegida. El mu-metal s'usa precisament perquè té una permeabilitat *molt alta*. La freqüència és decisiva: a alta freqüència (

$$
\geq 1
$$

  MHz) qualsevol metall serveix, perquè els corrents de Foucault induïts creen camps que s'oposen a l'incident; però a baixa freqüència calen materials d'alta permeabilitat, ja que a 50 Hz el coure o l'alumini (

$$
\mu_r \approx 1
$$

 ) gairebé no proporcionen blindatge magnètic.

La tècnica més característica per als cables és el **trenat** del parell de conductors. En cada volta els dos conductors intercanvien la seva posició relativa respecte a la font, de manera que la tensió induïda en una meitat de volta es cancel·la, aproximadament, amb la de signe oposat de l'altra meitat; el resultat és una inductància mútua neta pràcticament nul·la. Complementàriament, **minimitzar l'àrea dels bucles** de corrent (mantenir junts anada i retorn) redueix directament el flux captat. En plaques de circuit imprès, on el blindatge magnètic complet és difícil, s'apliquen plans de massa, disposició acurada dels components i reducció de l'àrea de les malles.

## 3 Efecte de les interferències sobre el resultat de mesura

La interferència se superposa al senyal útil de manera additiva. Si

$$
V_s(t)
$$

  és la tensió útil i

$$
V_i(t)
$$

  la interferent, la tensió observada és

$$
V_d(t) = V_s(t) + V_i(t) \qquad (3.28)
$$

vàlida mentre el sistema sigui lineal; si una etapa **satura** per l'amplitud de la interferència, la descomposició deixa de ser aplicable. Una propietat clau de les interferències periòdiques és que el seu **valor mitjà sobre un nombre sencer de períodes és nul**: no introdueixen cap desplaçament de contínua permanent, però sí que augmenten la variabilitat del senyal, cosa que degrada la repetibilitat.

Per a un senyal de mitjana nul·la, la desviació estàndard i el valor eficaç **coincideixen**. Per a una interferència sinusoïdal d'amplitud de pic

$$
A_p
$$

,

$$
\sigma = V_{\text{rms}} = \frac{A_p}{\sqrt{2}} \qquad (3.29)
$$

Aquesta

$$
\sigma
$$

  és, precisament, la magnitud que determina la incertesa típica quan la interferència es tracta com a font d'incertesa aleatòria.

### Distribució del mostreig d'una sinusoide

Quan una interferència sinusoïdal es mesura en instants **no sincronitzats** amb la seva freqüència, els valors obtinguts no segueixen una distribució normal, sinó una distribució en **forma de U** tal com es va veure al tema 2: com que la sinusoide passa més temps a prop de les crestes (on la derivada és petita) que prop del zero (derivada màxima), és més probable observar valors extrems que valors propers a zero. La seva funció de densitat de probabilitat és

$$
\mathrm{fdp}(x) = \frac{1}{\pi\sqrt{A^2 - x^2}}, \qquad |x| < A \qquad (3.30)
$$

![Distribució en U](assets/04_doc_img_3.png)

*Figura: Figura 3.22. Densitat de probabilitat en forma de U del mostreig aleatori d'una sinusoide d'amplitud

$$
A
$$

: mínima al centre i divergent als extrems

$$
\pm A
$$

.*

La incertesa típica associada a la interferència, tractada com a magnitud aleatòria, és igual al seu valor eficaç:

$$
u_{\mathrm{interf}}(y) = \sigma_{\mathrm{interf}} \qquad (3.31)
$$

### Mesura d'una magnitud constant: promitjat

Si es mesura una tensió contínua

$$
V_{\text{dc}}
$$

  en un instant arbitrari, la interferència present en aquell moment afecta el resultat; mesures repetides en instants aleatoris es dispersen dins del rang

$$
[V_{\text{dc}}-A,\ V_{\text{dc}}+A]
$$

. Per reduir-ho es pot **promitjar** durant un temps d'integració

$$
T
$$

. Amb

$$
V_d(t) = V_{\text{dc}} + A\cos(2\pi f t)
$$

,

$$
\overline{V_d} = V_{\text{dc}} + A\,\frac{\sin(2\pi f T)}{2\pi f T} \qquad (3.32)
$$

Si s'escull

$$
T = N/f
$$

  amb

$$
N
$$

  enter, el terme de la interferència s'anul·la exactament i el promig és igual a

$$
V_{\text{dc}}
$$

: la interferència queda completament rebutjada. Aquest rebuig només és exacte per a un nombre **sencer** de períodes; promitjar durant una durada arbitrària — o durant mitja volta, independentment de la fase — *no* elimina la interferència. A la pràctica

$$
N
$$

  no és mai exactament enter, però com més gran és

$$
T
$$

, menor és l'efecte residual. És el fonament del rebuig de xarxa dels multímetres integradors (document 2).

### Mesura d'un valor eficaç: biaix

Quan es mesura el valor eficaç d'un senyal altern, una interferència sinusoïdal de freqüència diferent introdueix un **error sistemàtic**. Si el senyal útil té valor eficaç

$$
\sigma_s
$$

  i la interferència

$$
\sigma_i
$$

, el valor eficaç mesurat és

$$
\sigma_d = \sqrt{\sigma_s^2 + \sigma_i^2} \qquad (3.33)
$$

Ara la interferència no degrada la repetibilitat, sinó que provoca un **biaix** sempre positiu (mai alterna de signe), que pot ser important si la interferència és comparable al senyal. En resum: sobre una magnitud constant la interferència es percep com a **falta de repetibilitat** proporcional a la seva magnitud; sobre un valor eficaç, com un **error sistemàtic** sempre positiu.

## 4 Diagnosi i selecció de la mitigació

Una diagnosi racional d'un problema d'interferència comença identificant els tres elements del problema (document 1): la **font**, el **canal d'acoblament** i el **receptor** afectat. Un cop identificat el canal, la mitigació més eficaç sol ser la que hi actua:

- **Conduïda:** minimitzar les impedàncies de retorn, reduir el corrent de fuita i, sobretot, emprar sistemes flotants d'alt CMRR (document 2).
- **Capacitiva:** blindar amb un conductor ben referenciat i, quan escaigui, cable coaxial; augmentar la impedància d'entrada *empitjora* aquest cas (document 3).
- **Inductiva:** trenar els conductors, minimitzar l'àrea de bucle i, a baixa freqüència, blindar amb material d'alta permeabilitat; aquí augmentar la impedància d'entrada no ajuda, perquè la tensió induïda n'és independent.

Com a orientació, en circuits d'alta impedància acostuma a dominar l'acoblament capacitiu i en circuits de baixa impedància, l'inductiu. Quan la interferència no es pot eliminar del tot, encara es pot atacar en el processament: filtratge (analògic o digital) i promitjat, sempre que cap etapa prèvia no hagi saturat.

> [!TIP] **Síntesi**
>
> L'acoblament inductiu indueix, per la llei de Faraday, una tensió en sèrie

$$
V_i = -L_m\,dI_1/dt
$$

  que exigeix un corrent variable a la font, creix amb la freqüència i depèn de la geometria (longitud de paral·lelisme, separació, àrea de bucle), però **no** de la impedància del receptor. Es mitiga trenant els conductors, minimitzant l'àrea de les malles i, a baixa freqüència, amb blindatge d'alta permeabilitat (mu-metal), ja que a 50 Hz els metalls de

$$
\mu_r \approx 1
$$

  no blinden magnèticament. Sobre el resultat, una interferència periòdica té valor mitjà nul, la seva

$$
\sigma = V_{\text{rms}} = A_p/\sqrt{2}
$$

  fixa la incertesa típica, i el mostreig aleatori d'una sinusoide segueix una distribució en U. En mesures de contínua, el promitjat sobre un nombre sencer de períodes la rebutja completament (i mai una durada arbitrària); en mesures de valor eficaç, hi afegeix un biaix positiu

$$
\sigma_d = \sqrt{\sigma_s^2+\sigma_i^2}
$$

. Tota intervenció comença per identificar font, canal i receptor, i actua preferentment sobre el canal.

[← 3. Interferències capacitives i blindatge](#u3-3-interferències-capacitives-i-blindatge)[Índex →](#unitat-3-interferències-en-sistemes-de-mesura)

Sistemes de Mesura (230920) · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB – UPC
Material de lectura prèvia · Unitat 3: Interferències en Sistemes de Mesura

---

<!-- FIN CAPÍTULO: 04_doc -->

---

<!-- INICIO CAPÍTULO: 05_entrenament_tema3 -->

# Entrenament V/F · Unitat 3: Interferències

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
> 📌 **Afirmació:** *El soroll blanc presenta, idealment, una densitat espectral de potència pràcticament constant amb la freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El soroll blanc ocupa tota l'amplada de banda de mesura amb densitat espectral pràcticament constant (document 1, secció 1).*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 02
> 📌 **Afirmació:** *Una interferència periòdica ocupa una amplada de banda més gran que la del soroll blanc.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És a l'inrevés: la interferència té espectre estret (fonamental i harmònics) i el soroll blanc ocupa tota la banda.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 03
> 📌 **Afirmació:** *Una interferència periòdica es pot descriure per una freqüència fonamental i els seus harmònics.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És una de les característiques distintives de la interferència periòdica: espectre concentrat en múltiples enters de la fonamental.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 04
> 📌 **Afirmació:** *L'objectiu de la mitigació d'interferències consisteix habitualment a augmentar l'acoblament entre la font interferent i el receptor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'objectiu és el contrari: bloquejar o atenuar el canal de transmissió entre font i receptor.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 05
> 📌 **Afirmació:** *Promitjar 100 lectures independents redueix la desviació típica del promig en un factor 10.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *En promitjar N lectures independents, la desviació típica del promig es divideix per l'arrel de N; amb N = 100, el factor és 10.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *El soroll d'un sistema de mesura té origen típicament extern i d'origen humà.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Això descriu la interferència. El soroll s'origina generalment dins del sistema de mesura o ja ve superposat al transductor.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 07
> 📌 **Afirmació:** *Una descàrrega electrostàtica pot provocar una degradació latent que es manifesti setmanes o mesos després.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Malgrat durar microsegons, les ESD poden causar ruptura de dielèctrics, danys d'unió PN i degradació latent diferida.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *Les tempestes solars constitueixen una font artificial intencionada d'interferència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Són una interferència natural d'origen extraterrestre; les intencionades són artificials (transmissors de comunicació).*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 09
> 📌 **Afirmació:** *Les eines elèctriques amb arcs generen espectres de banda ampla que s'estenen de centenars de Hz a centenars de MHz.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El seu caràcter impulsiu distribueix l'energia en una banda molt gran, cosa que les fa especialment perilloses.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 10
> 📌 **Afirmació:** *Les interferències només es poden classificar segons l'origen de la font.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Es classifiquen per origen de la font, per mode d'acoblament i per canal de transmissió.*

> **📚 Document de referència:** `1. Soroll, interferència i classificació`
> </details>

### Qüestió 11
> 📌 **Afirmació:** *Tot problema d'interferència electromagnètica es pot estructurar en font, canal i receptor.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Són els tres elements inseparables de l'anàlisi; la mitigació més eficaç sol actuar sobre el canal.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 12
> 📌 **Afirmació:** *La Directiva 2014/30/UE exigeix que els equips comercialitzats compleixin els estàndards de la sèrie IEC 61000.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És el marc normatiu d'EMC a la Unió Europea (anteriorment 89/336/CEE).*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *Complir la normativa EMC garanteix que no hi haurà problemes d'interferència a la pràctica.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Les proves no cobreixen totes les configuracions; diversos equips conformes poden sumar interferències, i l'envelliment n'augmenta l'emissió.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 14
> 📌 **Afirmació:** *Les proves d'emissió mesuren la capacitat de l'equip per tolerar les interferències presents en el seu entorn.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Això són les proves d'immunitat. Les d'emissió mesuren la interferència que l'equip genera en funcionament normal.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 15
> 📌 **Afirmació:** *La sèrie IEC 61000 tracta únicament la resistència mecànica de les carcasses dels equips.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Es subdivideix en parts sobre generalitats, entorn electromagnètic, límits d'emissió, immunitat, instal·lacions i normes genèriques.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 16
> 📌 **Afirmació:** *L'estratègia de mitigació generalment més eficaç consisteix a actuar sobre el canal de transmissió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Es pot actuar sobre qualsevol dels tres elements, però modificar el canal (blindatge, coaxial, filtratge, connexions) sol ser el més efectiu.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 17
> 📌 **Afirmació:** *A 1 MHz, la longitud d'ona electromagnètica és aproximadament de 300 m.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb λ = c/f: 3·10⁸ / 10⁶ = 300 m.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 18
> 📌 **Afirmació:** *A 50 Hz, la longitud d'ona electromagnètica és inferior a un metre.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *A 50 Hz la longitud d'ona és d'uns 6.000 km.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 19
> 📌 **Afirmació:** *La frontera entre camp proper i camp llunyà se situa aproximadament a una distància λ/2π.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Equival a uns 0,16·λ; els sistemes de mesura típics estan gairebé sempre en camp proper a baixa freqüència.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 20
> 📌 **Afirmació:** *En camp proper, els camps elèctric i magnètic estan lligats per la impedància característica de 377 Ω.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Aquesta relació és pròpia del camp llunyà. En camp proper E i H són independents, cosa que permet separar l'anàlisi capacitiva de la inductiva.*

> **📚 Document de referència:** `2. Compatibilitat electromagnètica, canal i camp`
> </details>

### Qüestió 21
> 📌 **Afirmació:** *La tensió de mode comú es pot expressar com Vc = (VA + VB)/2.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de mode comú respecte al node de referència del sistema de mesura.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *Un CMRR de 80 dB equival a un factor de rebuig lineal igual a 80.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El factor lineal és 10^(80/20) = 10⁴, no 80.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 23
> 📌 **Afirmació:** *Amb una tensió de mode comú d'1 V i un CMRR de 80 dB, la pertorbació diferencial equivalent és de 0,1 mV.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *1 V dividit pel factor lineal 10⁴ dóna 0,1 mV.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 24
> 📌 **Afirmació:** *Un convertidor analògic-digital integrador pot rebutjar una interferència periòdica si el temps d'integració conté un nombre enter de períodes.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El guany és proporcional a sin(πfT)/(πfT), que s'anul·la quan fT és enter; per això integrar 20 ms rebutja els 50 Hz.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 25
> 📌 **Afirmació:** *El CMRR d'un amplificador real es manté constant a totes les freqüències.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Disminueix típicament amb la freqüència: 100 dB en contínua poden quedar en 60 dB a 1 kHz i 40 dB a 10 kHz.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *Un desequilibri entre les impedàncies de mode comú dels dos camins d'entrada converteix part del mode comú en mode diferencial.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per això la simetria de les impedàncies determina en gran mesura el CMRR efectiu a freqüències altes.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 27
> 📌 **Afirmació:** *Els equips de classe I tenen les parts metàl·liques accessibles connectades al conductor de protecció de terra.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Requereixen cable de tres conductors i les seves fonts commutades injecten corrents de fuita de 0,5 a 2 mA eficaços.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 28
> 📌 **Afirmació:** *Els equips de classe II garanteixen la protecció connectant la carcassa al conductor de terra en lloc d'emprar doble aïllament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La classe II es basa precisament en el doble aïllament; són equips flotants amb massa independent de la terra de la instal·lació.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 29
> 📌 **Afirmació:** *Els equips de classe III s'alimenten amb tensió de seguretat molt baixa i no generen corrents de fuita significatius.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Típicament ≤ 50 V en alterna, sovint amb bateries.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 30
> 📌 **Afirmació:** *Quan la font i el sistema de mesura estan tots dos posats a terra, el CMRR resultant del circuit és molt elevat, superior a 100 dB.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En aquest cas el CMRR val 1 + Zcp/Zb, amb Zcp i Zb comparables: un factor proper a 2, molt lluny dels 100 dB.*

> **📚 Document de referència:** `3. Mode diferencial, mode comú i CMRR`
> </details>

### Qüestió 31
> 📌 **Afirmació:** *Quan la font és flotant i el mesurador està posat a terra, el CMRR val ZA/Zb i pot assolir valors molt elevats.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb Zb = 0,1 Ω i ZA = 10 MΩ a 50 Hz s'obtenen 160 dB, és a dir, vuit ordres de magnitud d'atenuació.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *Desconnectar de la instal·lació els equips que no s'utilitzen incrementa el corrent de fuita acumulat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El redueix. Els equips de classe I injecten fuita fins i tot en standby, perquè la font commutada continua activa.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 33
> 📌 **Afirmació:** *Augmentar la impedància del conductor de retorn Zb és una forma directa de reduir la interferència conduïda externa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal minimitzar les impedàncies dels camins de retorn: engruixir o escurçar el cable, no augmentar-ne la impedància.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *Un varistor MOV s'utilitza principalment per augmentar el guany diferencial de l'amplificador d'entrada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És un supressor de transitoris: desvia ràpidament les sobretensions a terra i limita la tensió que arriba als circuits.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 35
> 📌 **Afirmació:** *Un transformador d'aïllament amb pantalla redueix la capacitat paràsita d'acoblament entre primari i secundari.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Passa dels 100 pF – 10 nF d'un transformador convencional a valors de 5–10 pF amb blindatge doble.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 36
> 📌 **Afirmació:** *El corrent acoblat capacitivament compleix iC = C · dV/dt.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És el corrent de desplaçament a través de la capacitat paràsita.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 37
> 📌 **Afirmació:** *L'acoblament capacitiu requereix un corrent elevat a la font interferent, encara que la seva tensió sigui constant.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Depèn de la variació de tensió (dV/dt); una tensió constant, per gran que sigui, no acobla res.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 38
> 📌 **Afirmació:** *La impedància d'una capacitat es pot expressar com ZC = j·2·π·f·C.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És la inversa: ZC = 1/(j·2·π·f·C), de manera que disminueix en pujar la freqüència.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 39
> 📌 **Afirmació:** *A freqüències altes, la impedància de l'acoblament capacitiu tendeix a disminuir.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Com que ZC = 1/(j2πfC), l'acoblament s'agreuja amb la freqüència.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 40
> 📌 **Afirmació:** *Un receptor d'alta impedància desenvolupa una tensió interferent menor per a un mateix corrent acoblat capacitivament.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En desenvolupa una de més gran (V = i·Z); per això els circuits d'alta impedància són especialment susceptibles.*

> **📚 Document de referència:** `4. Interferències conduïdes i acoblament capacitiu`
> </details>

### Qüestió 41
> 📌 **Afirmació:** *L'eficàcia d'un blindatge depèn de manera determinant de la seva connexió a una referència de potencial adequada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per a interferències de la instal·lació cal connectar-lo a terra; per a interferències internes, a la massa de la font interferent.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 42
> 📌 **Afirmació:** *Les obertures practicades en una carcassa metàl·lica augmenten l'efectivitat del blindatge.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La redueixen: trenquen la continuïtat elèctrica de la gàbia de Faraday, igual que els conductors que n'han de sortir.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 43
> 📌 **Afirmació:** *La condició de compensació d'una sonda atenuadora és Rp · Cp = Rosc · (Ccable + Cosc).*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Si es compleix, la funció de transferència esdevé d'ordre zero, constant amb la freqüència.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 44
> 📌 **Afirmació:** *Quan una sonda està correctament compensada, la transferència entre la punta i l'entrada de l'oscil·loscopi esdevé un passa-baixes de primer ordre fortament dependent de la freqüència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És justament el contrari: la compensació elimina la dependència freqüencial i deixa un guany pla igual a 1/A.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 45
> 📌 **Afirmació:** *La tensió induïda per acoblament inductiu es pot modelar com Vi = −Lm · dI1/dt.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Deriva de la llei de Faraday, amb Lm la inductància mútua entre els dos circuits.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 46
> 📌 **Afirmació:** *Perquè es produeixi una interferència inductiva n'hi ha prou amb una tensió elevada a la font, encara que no hi circuli corrent.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal un corrent variable: el mecanisme és el camp magnètic, que depèn de dI/dt, no de la tensió.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 47
> 📌 **Afirmació:** *El mu-metal s'utilitza en blindatge magnètic perquè presenta una permeabilitat relativa especialment baixa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *S'utilitza precisament perquè la té molt alta (fins a desenes de milers), cosa que redirigeix les línies de camp.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *Mostrejar una sinusoide en instants de fase aleatòria produeix una distribució de probabilitat en forma de U.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La densitat és mínima al centre i divergeix als extrems ±A, perquè la sinusoide és més lenta prop de les crestes.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 49
> 📌 **Afirmació:** *Per a un senyal de valor mitjà nul, la desviació estàndard coincideix amb el valor eficaç.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per això la incertesa típica associada a una interferència s'estima amb el seu valor rms.*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

### Qüestió 50
> 📌 **Afirmació:** *Promitjar una lectura durant qualsevol durada elimina exactament les interferències periòdiques presents.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Només s'anul·len si el temps d'integració conté un nombre enter de períodes (T = N/f).*

> **📚 Document de referència:** `5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **01** | **V** | El soroll blanc ocupa tota l'amplada de banda de mesura amb densitat espectral pràcticament constant (document 1, sec... | 1. Soroll, interferència i classificació |
| **02** | **F** | És a l'inrevés: la interferència té espectre estret (fonamental i harmònics) i el soroll blanc ocupa tota la banda. | 1. Soroll, interferència i classificació |
| **03** | **V** | És una de les característiques distintives de la interferència periòdica: espectre concentrat en múltiples enters de ... | 1. Soroll, interferència i classificació |
| **04** | **F** | L'objectiu és el contrari: bloquejar o atenuar el canal de transmissió entre font i receptor. | 1. Soroll, interferència i classificació |
| **05** | **V** | En promitjar N lectures independents, la desviació típica del promig es divideix per l'arrel de N; amb N = 100, el fa... | 1. Soroll, interferència i classificació |
| **06** | **F** | Això descriu la interferència. El soroll s'origina generalment dins del sistema de mesura o ja ve superposat al trans... | 1. Soroll, interferència i classificació |
| **07** | **V** | Malgrat durar microsegons, les ESD poden causar ruptura de dielèctrics, danys d'unió PN i degradació latent diferida. | 1. Soroll, interferència i classificació |
| **08** | **F** | Són una interferència natural d'origen extraterrestre; les intencionades són artificials (transmissors de comunicació). | 1. Soroll, interferència i classificació |
| **09** | **V** | El seu caràcter impulsiu distribueix l'energia en una banda molt gran, cosa que les fa especialment perilloses. | 1. Soroll, interferència i classificació |
| **10** | **F** | Es classifiquen per origen de la font, per mode d'acoblament i per canal de transmissió. | 1. Soroll, interferència i classificació |
| **11** | **V** | Són els tres elements inseparables de l'anàlisi; la mitigació més eficaç sol actuar sobre el canal. | 2. Compatibilitat electromagnètica, canal i camp |
| **12** | **V** | És el marc normatiu d'EMC a la Unió Europea (anteriorment 89/336/CEE). | 2. Compatibilitat electromagnètica, canal i camp |
| **13** | **F** | Les proves no cobreixen totes les configuracions; diversos equips conformes poden sumar interferències, i l'envellime... | 2. Compatibilitat electromagnètica, canal i camp |
| **14** | **F** | Això són les proves d'immunitat. Les d'emissió mesuren la interferència que l'equip genera en funcionament normal. | 2. Compatibilitat electromagnètica, canal i camp |
| **15** | **F** | Es subdivideix en parts sobre generalitats, entorn electromagnètic, límits d'emissió, immunitat, instal·lacions i nor... | 2. Compatibilitat electromagnètica, canal i camp |
| **16** | **V** | Es pot actuar sobre qualsevol dels tres elements, però modificar el canal (blindatge, coaxial, filtratge, connexions)... | 2. Compatibilitat electromagnètica, canal i camp |
| **17** | **V** | Amb λ = c/f: 3·10⁸ / 10⁶ = 300 m. | 2. Compatibilitat electromagnètica, canal i camp |
| **18** | **F** | A 50 Hz la longitud d'ona és d'uns 6.000 km. | 2. Compatibilitat electromagnètica, canal i camp |
| **19** | **V** | Equival a uns 0,16·λ; els sistemes de mesura típics estan gairebé sempre en camp proper a baixa freqüència. | 2. Compatibilitat electromagnètica, canal i camp |
| **20** | **F** | Aquesta relació és pròpia del camp llunyà. En camp proper E i H són independents, cosa que permet separar l'anàlisi c... | 2. Compatibilitat electromagnètica, canal i camp |
| **21** | **V** | És la definició de mode comú respecte al node de referència del sistema de mesura. | 3. Mode diferencial, mode comú i CMRR |
| **22** | **F** | El factor lineal és 10^(80/20) = 10⁴, no 80. | 3. Mode diferencial, mode comú i CMRR |
| **23** | **V** | 1 V dividit pel factor lineal 10⁴ dóna 0,1 mV. | 3. Mode diferencial, mode comú i CMRR |
| **24** | **V** | El guany és proporcional a sin(πfT)/(πfT), que s'anul·la quan fT és enter; per això integrar 20 ms rebutja els 50 Hz. | 3. Mode diferencial, mode comú i CMRR |
| **25** | **F** | Disminueix típicament amb la freqüència: 100 dB en contínua poden quedar en 60 dB a 1 kHz i 40 dB a 10 kHz. | 3. Mode diferencial, mode comú i CMRR |
| **26** | **V** | Per això la simetria de les impedàncies determina en gran mesura el CMRR efectiu a freqüències altes. | 3. Mode diferencial, mode comú i CMRR |
| **27** | **V** | Requereixen cable de tres conductors i les seves fonts commutades injecten corrents de fuita de 0,5 a 2 mA eficaços. | 3. Mode diferencial, mode comú i CMRR |
| **28** | **F** | La classe II es basa precisament en el doble aïllament; són equips flotants amb massa independent de la terra de la i... | 3. Mode diferencial, mode comú i CMRR |
| **29** | **V** | Típicament ≤ 50 V en alterna, sovint amb bateries. | 3. Mode diferencial, mode comú i CMRR |
| **30** | **F** | En aquest cas el CMRR val 1 + Zcp/Zb, amb Zcp i Zb comparables: un factor proper a 2, molt lluny dels 100 dB. | 3. Mode diferencial, mode comú i CMRR |
| **31** | **V** | Amb Zb = 0,1 Ω i ZA = 10 MΩ a 50 Hz s'obtenen 160 dB, és a dir, vuit ordres de magnitud d'atenuació. | 4. Interferències conduïdes i acoblament capacitiu |
| **32** | **F** | El redueix. Els equips de classe I injecten fuita fins i tot en standby, perquè la font commutada continua activa. | 4. Interferències conduïdes i acoblament capacitiu |
| **33** | **F** | Cal minimitzar les impedàncies dels camins de retorn: engruixir o escurçar el cable, no augmentar-ne la impedància. | 4. Interferències conduïdes i acoblament capacitiu |
| **34** | **F** | És un supressor de transitoris: desvia ràpidament les sobretensions a terra i limita la tensió que arriba als circuits. | 4. Interferències conduïdes i acoblament capacitiu |
| **35** | **V** | Passa dels 100 pF – 10 nF d'un transformador convencional a valors de 5–10 pF amb blindatge doble. | 4. Interferències conduïdes i acoblament capacitiu |
| **36** | **V** | És el corrent de desplaçament a través de la capacitat paràsita. | 4. Interferències conduïdes i acoblament capacitiu |
| **37** | **F** | Depèn de la variació de tensió (dV/dt); una tensió constant, per gran que sigui, no acobla res. | 4. Interferències conduïdes i acoblament capacitiu |
| **38** | **F** | És la inversa: ZC = 1/(j·2·π·f·C), de manera que disminueix en pujar la freqüència. | 4. Interferències conduïdes i acoblament capacitiu |
| **39** | **V** | Com que ZC = 1/(j2πfC), l'acoblament s'agreuja amb la freqüència. | 4. Interferències conduïdes i acoblament capacitiu |
| **40** | **F** | En desenvolupa una de més gran (V = i·Z); per això els circuits d'alta impedància són especialment susceptibles. | 4. Interferències conduïdes i acoblament capacitiu |
| **41** | **V** | Per a interferències de la instal·lació cal connectar-lo a terra; per a interferències internes, a la massa de la fon... | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **42** | **F** | La redueixen: trenquen la continuïtat elèctrica de la gàbia de Faraday, igual que els conductors que n'han de sortir. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **43** | **V** | Si es compleix, la funció de transferència esdevé d'ordre zero, constant amb la freqüència. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **44** | **F** | És justament el contrari: la compensació elimina la dependència freqüencial i deixa un guany pla igual a 1/A. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **45** | **V** | Deriva de la llei de Faraday, amb Lm la inductància mútua entre els dos circuits. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **46** | **F** | Cal un corrent variable: el mecanisme és el camp magnètic, que depèn de dI/dt, no de la tensió. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **47** | **F** | S'utilitza precisament perquè la té molt alta (fins a desenes de milers), cosa que redirigeix les línies de camp. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **48** | **V** | La densitat és mínima al centre i divergeix als extrems ±A, perquè la sinusoide és més lenta prop de les crestes. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **49** | **V** | Per això la incertesa típica associada a una interferència s'estima amb el seu valor rms. | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |
| **50** | **F** | Només s'anul·len si el temps d'integració conté un nombre enter de períodes (T = N/f). | 5. Blindatge, sondes, acoblament inductiu i efecte sobre la mesura |

<!-- FIN CAPÍTULO: 05_entrenament_tema3 -->

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
| **(3.1)** | $x(t) = s(t) + i(t) + n(t)$ |
| **(3.2)** | $V_\mathrm{interferent} = I_f \cdot Z_\mathrm{terra}$ |
| **(3.3)** | $\lambda = \frac{c}{f}$ |
| **(3.4)** | $V_d = V_A - V_B$ |
| **(3.5)** | $g(f) \propto \frac{\sin(\pi f T)}{\pi f T}$ |
| **(3.6)** | $V_c = \frac{V_A + V_B}{2}$ |
| **(3.7)** | $\mathrm{CMRR} = \frac{A_d}{A_c}, \qquad \mathrm{CMRR}_{\mathrm{dB}} = 20\log_{10}\frac{A_d}{A_c}$ |
| **(3.8)** | $V_{MM'} = I_f \,(Z_b \parallel Z_{\text{cp}}) = I_f\,\frac{Z_b\,Z_{\text{cp}}}{Z_b + Z_{\text{cp}}}$ |
| **(3.9)** | $V_d\|_{I_f} = V_{MM'}\,\frac{Z_d}{Z_d + Z_a + Z_s} \approx V_{MM'}$ |
| **(3.10)** | $V_d\|_{I_f} = V_c\,\frac{Z_b}{Z_b + Z_A} \approx V_c\,\frac{Z_b}{Z_A} = \frac{V_c}{\mathrm{CMRR}}, \qquad \mathrm{CMRR} = \frac{Z_A}{Z_b}$ |
| **(3.11)** | $V_d\|_{I_f} = V_c\,\frac{Z_b}{Z_{\text{bt}}} = \frac{V_c}{\mathrm{CMRR}}, \qquad \mathrm{CMRR} = \frac{Z_{\text{bt}}}{Z_b}$ |
| **(3.12)** | $V_d\|_{I_f} = I_f\,Z_{\text{cp}}\,\frac{Z_b}{Z_A + Z_{\text{bt}}}$ |
| **(3.13)** | $V_d\|_{V_f} = \frac{V_f}{Z_{\text{fm}}}\,Z_b$ |
| **(3.14)** | $i_C = C\,\frac{dV}{dt}$ |
| **(3.15)** | $Z_{C_{12}} = \frac{1}{j\,2\pi f\,C_{12}}$ |
| **(3.16)** | $V_i\|_{V_1} = V_1\,\frac{j\,2\pi f\,C_{12}}{\,j\,2\pi f\,(C_{12}+C_{2M}) + \frac{Z_d+Z_s}{Z_d\,Z_s}\,}$ |
| **(3.17)** | $C_{12} \approx \frac{\pi\,\varepsilon_r\,\varepsilon_0\,\ell}{\ln\!(d/\sqrt{r_1 r_2})}$ |
| **(3.18)** | $C_{12} \approx \frac{2\pi\,\varepsilon_r\,\varepsilon_0\,\ell}{\ln(b/a)}$ |
| **(3.19)** | $f_{-3\,\mathrm{dB}} = \frac{1}{2\pi R_s C_{\text{ca}}}$ |
| **(3.20)** | $R_p\,C_p = R_{\text{osc}}\,(C_{\text{cable}}+C_{\text{osc}})$ |
| **(3.21)** | $H_{\text{comp}} = \frac{1}{A}$ |
| **(3.22)** | $f_{-3\,\mathrm{dB}} = \frac{A}{2\pi\,(C_{\text{osc}}+C_{\text{cable}})\,R_g}$ |
| **(3.23)** | $V_i = -\frac{\partial \Phi}{\partial t} = -\frac{\partial}{\partial t}(B\,S\cos\theta)$ |
| **(3.24)** | $V_i = -L_m\,\frac{dI_1}{dt}$ |
| **(3.25)** | $V_d = V_i\,\frac{Z_d}{Z_d + Z_s + j\,2\pi f\,L_2}$ |
| **(3.26)** | $L_m \approx \ell\,\frac{\mu_r \mu_0}{4\pi}\,\ln\!(1+\frac{4h^2}{d^2})$ |
| **(3.27)** | $L_m \approx \ell\,\frac{\mu_r \mu_0}{4\pi}\,\ln\!(\frac{d_{14}\,d_{23}}{d_{13}\,d_{24}})$ |
| **(3.28)** | $V_d(t) = V_s(t) + V_i(t)$ |
| **(3.29)** | $\sigma = V_{\text{rms}} = \frac{A_p}{\sqrt{2}}$ |
| **(3.30)** | $\mathrm{fdp}(x) = \frac{1}{\pi\sqrt{A^2 - x^2}}, \qquad \|x\| < A$ |
| **(3.31)** | $u_{\mathrm{interf}}(y) = \sigma_{\mathrm{interf}}$ |
| **(3.32)** | $\overline{V_d} = V_{\text{dc}} + A\,\frac{\sin(2\pi f T)}{2\pi f T}$ |
| **(3.33)** | $\sigma_d = \sqrt{\sigma_s^2 + \sigma_i^2}$ |