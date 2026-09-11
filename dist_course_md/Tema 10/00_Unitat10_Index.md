# Unitat 10 — Condicionament singular de senyals · Lectura prèvia

## 📑 Índice de Contenidos

  - [[1. Condicionament singular: sensors, l'operacional real i les seves derives](01_Unitat10_Condicionament_singular_i_limits_de_loperacional.md)](#1-condicionament-singular-sensors-loperacional-real-i-les-seves-derives01-unitat10-condicionament-singular-i-limits-de-loperacionalmd)
  - [[2. Amplificadors de baixes derives: compensació de la polarització i ajust d'offset](02_Unitat10_Amplificadors_de_baixes_derives.md)](#2-amplificadors-de-baixes-derives-compensació-de-la-polarització-i-ajust-doffset02-unitat10-amplificadors-de-baixes-derivesmd)
  - [[3. Amplificadors chopper i amplificadors amb autozero](03_Unitat10_Chopper_i_autozero.md)](#3-amplificadors-chopper-i-amplificadors-amb-autozero03-unitat10-chopper-i-autozeromd)
  - [[4. Amplificadors electromètrics i de transimpedància](04_Unitat10_Electrometrics_i_transimpedancia.md)](#4-amplificadors-electromètrics-i-de-transimpedància04-unitat10-electrometrics-i-transimpedanciamd)
  - [[5. Amplificadors de càrrega](05_Unitat10_Amplificadors_de_carrega.md)](#5-amplificadors-de-càrrega05-unitat10-amplificadors-de-carregamd)

---

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 10 — Condicionament singular de senyals

Materials de lectura prèvia · dedicació total estimada: 54 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen.

Llegeix els cinc documents en ordre **abans de la primera sessió**.

### [1. Condicionament singular: sensors, l'operacional real i les seves derives](01_Unitat10_Condicionament_singular_i_limits_de_loperacional.md)

Què fa singular un sensor: la classificació electrònica, complementària de la física, en dos blocs segons si el problema dominant és el nivell de senyal o la impedància de sortida, i les tres famílies de circuits que se'n deriven. Tres mesures on l'operacional de propòsit general queda curt. El model de l'operacional real: tensió d'offset, corrents de polarització i d'offset, i l'error que produeixen en circular per les resistències del circuit. Deriva tèrmica i envelliment, i la diferència pràctica entre un error constant i un que deriva. Soroll blanc i soroll 1/f, la freqüència de cantonada i la integral sobre la banda útil. Ordres de magnitud per tecnologia d'entrada.

*⏱️ Dedicació estimada: 12 min*

### [2. Amplificadors de baixes derives: compensació de la polarització i ajust d'offset](02_Unitat10_Amplificadors_de_baixes_derives.md)

L'especificació del problema del termoparell: sensibilitats, resolució exigida i contingut freqüencial fins a la contínua, amb les cinc condicions simultànies que ha de satisfer l'amplificador i el criteri d'error referit a l'entrada. La resistència auxiliar que canvia un error proporcional al corrent de polarització per un de proporcional al corrent d'offset, i en quines tecnologies compensa. El guany de soroll com a factor que multiplica l'offset. L'ajust intern amb pins d'offset null i la seva degradació tèrmica. La compensació externa en les topologies inversora i no inversora, la doble compensació simultània i el dimensionament de la tensió de referència.

*⏱️ Dedicació estimada: 10 min*

### [3. Amplificadors chopper i amplificadors amb autozero](03_Unitat10_Chopper_i_autozero.md)

La modulació a la freqüència de commutació, l'amplificació lluny de la zona de soroll 1/f i la desmodulació síncrona, seguides en el temps als cinc punts interns i en el domini freqüencial. El guany en llaç tancat i la seva equivalència amb el d'un amplificador convencional. Les tres limitacions intrínseques: banda útil, plegament de soroll de bandes laterals i residus de commutació. Els amplificadors amb autozero: les dues fases, l'emmagatzematge capacitiu de les correccions i la tensió d'offset efectiva reduïda pel factor de correcció. Arquitectures híbrides i els sis criteris de selecció d'un amplificador.

*⏱️ Dedicació estimada: 10 min*

### [4. Amplificadors electromètrics i de transimpedància](04_Unitat10_Electrometrics_i_transimpedancia.md)

El model de Thevenin i el de Norton com a descripcions equivalents d'un mateix sensor, i la topologia que cadascun suggereix. L'amplificador electromètric: condicions de funcionament, divisor amb la impedància d'entrada finita i aplicació a l'elèctrode de vidre. L'amplificador de transimpedància: curtcircuit virtual, transimpedància en ohms o volts per ampere, estabilitat i la capacitat de realimentació. Errors de contínua i soroll de totes dues topologies, amb el guany de soroll que creix amb la freqüència. La xarxa en T per sintetitzar transimpedàncies de gigaohms i el seu preu en offset i soroll. Guardes, apantallament, aïllants, neteja i control d'humitat.

*⏱️ Dedicació estimada: 14 min*

### [5. Amplificadors de càrrega](05_Unitat10_Amplificadors_de_carrega.md)

El model del sensor amb sortida en càrrega i les capacitats paràsites del cable i de l'entrada, comparables o superiors a la del sensor. La relació entre corrent i càrrega, l'integrador amb condensador de realimentació i la sortida proporcional a la càrrega, independent de les capacitats paràsites mentre el guany en llaç obert ho permeti. La resistència en paral·lel que evita la saturació, la condició que ha de complir a la freqüència mínima d'interès i la freqüència de tall inferior que en resulta. Errors de contínua en el model amb els condensadors oberts, i la tecnologia d'entrada que se'n dedueix. L'efecte triboelèctric i les mesures que el mitiguen.

*⏱️ Dedicació estimada: 8 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.