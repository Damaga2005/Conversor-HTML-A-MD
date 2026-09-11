# Unitat 8 — Condicionament de sensors en alterna · Lectura prèvia

## 📑 Índice de Contenidos

  - [[1. Sensors reactius, freqüència de treball i cadena de condicionament](01_Unitat8_Sensors_reactius_i_cadena_de_condicionament.md)](#1-sensors-reactius-freqüència-de-treball-i-cadena-de-condicionament01-unitat8-sensors-reactius-i-cadena-de-condicionamentmd)
  - [[2. Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts](02_Unitat8_Conversio_impedancia_tensio.md)](#2-conversió-impedànciatensió-divisors-inversor-ponts-i-pseudoponts02-unitat8-conversio-impedancia-tensiomd)
  - [[3. Amplificadors d'alterna i limitacions dels operacionals](03_Unitat8_Amplificadors_d_alterna.md)](#3-amplificadors-dalterna-i-limitacions-dels-operacionals03-unitat8-amplificadors-d-alternamd)
  - [[4. Estimació de l'amplitud: mètodes no coherents](04_Unitat8_04_Metodes_no_coherents.md)](#4-estimació-de-lamplitud-mètodes-no-coherents04-unitat8-04-metodes-no-coherentsmd)
  - [[5. Detecció coherent: homodina, rectificació síncrona i mostreig síncron](05_Unitat8_Deteccio_coherent.md)](#5-detecció-coherent-homodina-rectificació-síncrona-i-mostreig-síncron05-unitat8-deteccio-coherentmd)
  - [[6. Mètodes basats en oscil·ladors i mesura de freqüència](06_Unitat8_Oscil_ladors_de_frequencia_variable.md)](#6-mètodes-basats-en-oscilladors-i-mesura-de-freqüència06-unitat8-oscil-ladors-de-frequencia-variablemd)

---

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 8 — Condicionament de sensors en alterna

Materials de lectura prèvia · dedicació total estimada: 61 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents contenen tot el que cal per preparar la unitat.

Llegeix els sis documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor.

### [1. Sensors reactius, freqüència de treball i cadena de condicionament](01_Unitat8_Sensors_reactius_i_cadena_de_condicionament.md)

El model d'impedància complexa Z(f,x)=R+jX i la condició que fa que un sensor es pugui tractar com a reactiu. Com es tria la freqüència de treball: el que hi imposa el sensor —nucli ferromagnètic, corrents de Foucault, capacitiu— i el que hi imposa el sistema, allunyar-se de la xarxa i del soroll 1/f. Les dues aproximacions al condicionament, la lineal i la basada en oscil·ladors. Els quatre blocs de la cadena lineal i la funció de cadascun. Els quatre models canònics de sensor. Dos condicionadors integrats comercials com a il·lustració de les dues aproximacions.

*⏱️ Dedicació estimada: 10 min*

### [2. Conversió impedància–tensió: divisors, inversor, ponts i pseudoponts](02_Unitat8_Conversio_impedancia_tensio.md)

El divisor d'impedàncies i quan la freqüència s'hi cancel·la. La no linealitat del divisor amb un sol sensor i la linealitat exacta del divisor diferencial, amb el seu rebuig de mode comú. El problema de la impedància de sortida del divisor passiu i les seves mitigacions, de l'apantallament a l'amplificador operacional. L'amplificador inversor capacitiu, la resistència de polarització i les seves dues condicions contraposades, i on col·locar el sensor. El pont d'alterna: homogeneïtat de branques, condició d'equilibri, sortida amb sensor diferencial i impedància de sortida. El pseudopont i els seus dos avantatges.

*⏱️ Dedicació estimada: 9 min*

### [3. Amplificadors d'alterna i limitacions dels operacionals](03_Unitat8_Amplificadors_d_alterna.md)

Per què l'amplificació ha de ser passa-banda: supressió dels errors de contínua, reducció del soroll 1/f i rebuig de la xarxa. La banda que ocupa el senyal modulat i la condició de guany pla als seus extrems. Centrat per mitjana geomètrica i el compromís d'amplada de banda entre error de guany i rebuig de soroll. Les dues topologies —no inversora i d'instrumentació— amb l'anàlisi en tres règims i les freqüències de tall. Les quatre limitacions de l'operacional a la freqüència de treball: GBW, slew rate, capacitat d'entrada i de les pistes, i degradació de CMRR i PSRR, amb el desacoblament de l'alimentació.

*⏱️ Dedicació estimada: 12 min*

### [4. Estimació de l'amplitud: mètodes no coherents](04_Unitat8_04_Metodes_no_coherents.md)

Modulació AM clàssica davant de modulació DSB i què determina quines tècniques són admissibles. Els convertidors de valor eficaç: tèrmics, de càlcul explícit i implícit, i per rectificació amb el seu factor de forma, comparats en exactitud, amplada de banda, velocitat i cost. Per què tot mètode no coherent introdueix un biaix positiu davant del soroll i les interferències. Els multiplicadors analògics i els seus quadrants, les implementacions amb amplificadors logarítmics i antilogarítmics i la cèl·lula de Gilbert. Els detectors de pic: arrissat, criteri de la constant de temps i sensibilitat al soroll impulsiu.

*⏱️ Dedicació estimada: 12 min*

### [5. Detecció coherent: homodina, rectificació síncrona i mostreig síncron](05_Unitat8_Deteccio_coherent.md)

Què aporta la referència de fase: recuperació del signe en DSB, rebuig de la quadratura i reducció del soroll. La detecció homodina, el terme a 2f0 que el filtre elimina i la interpretació de la sortida en funció del desfasament. La tria de la freqüència de tall, l'atenuació d'una interferència i la reducció de soroll respecte de l'amplada de banda de l'amplificador. La rectificació síncrona amb referència quadrada i commutador, i el preu dels seus harmònics imparells. El mostreig síncron: què elimina cada combinació de mostres, per què la taxa la fixa el mesurand i no la portadora, i la validesa del sub-mostreig.

*⏱️ Dedicació estimada: 10 min*

### [6. Mètodes basats en oscil·ladors i mesura de freqüència](06_Unitat8_Oscil_ladors_de_frequencia_variable.md)

Codificar el mesurand en la freqüència: senzillesa, sortida digital directa i immunitat a les pertorbacions d'amplitud, davant de la no linealitat, la deriva dels components i el temps d'integració. Els tres oscil·ladors de relaxació —555 astable, amplificador operacional amb histèresi i inversors CMOS de Schmitt— amb les seves expressions i el seu cicle de treball. La conversió freqüència–tensió amb monoestable i la condició sobre la durada del pols. El comptatge digital de flancs, la resolució 1/Tgate i el compromís amb la velocitat de resposta.

*⏱️ Dedicació estimada: 8 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.