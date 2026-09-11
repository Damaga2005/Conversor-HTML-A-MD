# Unitat 6 — Condicionament de sensors en contínua · Lectura prèvia

## 📑 Índice de Contenidos

  - [[1. La cadena de condicionament en contínua](01_Unitat6_Cadena_de_condicionament_en_continua.md)](#1-la-cadena-de-condicionament-en-contínua01-unitat6-cadena-de-condicionament-en-continuamd)
  - [[2. Conversió resistència–tensió: cables, fonts de corrent, divisor i pont](02_Unitat6_Conversio_resistencia_tensio.md)](#2-conversió-resistènciatensió-cables-fonts-de-corrent-divisor-i-pont02-unitat6-conversio-resistencia-tensiomd)
  - [[3. Conversió corrent–tensió i amplificadors diferencials](03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials.md)](#3-conversió-correnttensió-i-amplificadors-diferencials03-unitat6-conversio-corrent-tensio-i-amplificadors-diferencialsmd)
  - [[4. Amplificadors d'instrumentació](04_Unitat6_Amplificadors_dinstrumentacio.md)](#4-amplificadors-dinstrumentació04-unitat6-amplificadors-dinstrumentaciomd)
  - [[5. Interruptors, multiplexors analògics i PGA](05_Unitat6_Interruptors_multiplexors_i_PGA.md)](#5-interruptors-multiplexors-analògics-i-pga05-unitat6-interruptors-multiplexors-i-pgamd)
  - [[6. Referències de tensió i de corrent i mesures ratiomètriques](06_Unitat6_Referencies_i_mesures_ratiometriques.md)](#6-referències-de-tensió-i-de-corrent-i-mesures-ratiomètriques06-unitat6-referencies-i-mesures-ratiometriquesmd)
  - [[✓. Entrenament V/F](07_Unitat6_Entrenament.md)](#entrenament-vf07-unitat6-entrenamentmd)

---

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 6 — Condicionament de sensors en contínua

Materials de lectura prèvia · dedicació total estimada: 61 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents **substitueixen els apunts** i contenen tot el que cal per preparar la unitat.

Llegeix els sis documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor.

### [1. La cadena de condicionament en contínua](01_Unitat6_Cadena_de_condicionament_en_continua.md)

Què vol dir sortida en contínua i quins criteris de disseny en deriven: precisió DC, deriva, soroll de baixa freqüència i autoescalfament. L'objectiu del condicionador en termes del marge dinàmic de l'ADC. Blocs de la cadena: excitació, conversió, front end analògic, multiplexatge, filtratge i conversió A/D. AFE monolítics comercials. Model R=R0(1+alfa·x) i per què interessa la variació i no el valor absolut. Contribucions a la incertesa global i interaccions entre blocs.

*⏱️ Dedicació estimada: 9 min*

### [2. Conversió resistència–tensió: cables, fonts de corrent, divisor i pont](02_Unitat6_Conversio_resistencia_tensio.md)

Biaix de la resistència dels cables i mesura a 2, 3 i 4 fils, amb els criteris de tria. Conversió amb font de corrent: sensibilitat I·R0·alfa i la limitació de la component contínua gran; dues fonts aparellades per anul·lar-la. Divisor de tensió: no-linealitat, sensibilitat màxima Vref·alfa/4 amb R=R0 i el compromís amb l'autoescalfament. Pont de Wheatstone: equilibri, paràmetre k i el seu efecte simultani sobre sensibilitat, linealitat, consum i mode comú; mig pont i pont complet.

*⏱️ Dedicació estimada: 11 min*

### [3. Conversió corrent–tensió i amplificadors diferencials](03_Unitat6_Conversio_corrent_tensio_i_amplificadors_diferencials.md)

Models de sensor de corrent amb offset i proporcional. Resistència de càrrega: quan serveix i per què el soroll tèrmic creix amb l'arrel de R. Amplificador de transimpedància, massa virtual i Vout=Ip·Rf, amb els corrents de polarització com a limitació. Amplificador diferencial de quatre resistències: guany diferencial i en mode comú, la condició R1/R2=R3/R4 i un exemple resolt de combinació de CMRR. Impedàncies d'entrada i efecte de càrrega sobre el pont.

*⏱️ Dedicació estimada: 12 min*

### [4. Amplificadors d'instrumentació](04_Unitat6_Amplificadors_dinstrumentacio.md)

Què resol respecte de l'amplificador diferencial simple. Estructura de tres amplificadors operacionals, guany G1=1+2Rf/Rg ajustable amb una sola resistència, i la impedància d'entrada elevada de la primera etapa no inversora. Especificacions DC: exactitud i no-linealitat de guany, offset referit a l'entrada, corrents de polarització, CMRR, PSRR, derives tèrmiques, soroll i producte guany–amplada de banda. L'INA317 com a cas concret i els criteris de selecció.

*⏱️ Dedicació estimada: 8 min*

### [5. Interruptors, multiplexors analògics i PGA](05_Unitat6_Interruptors_multiplexors_i_PGA.md)

Interruptor ideal enfront del real: Ron, fuites i capacitats paràsites. Per què el CMOS combina canal N i canal P. Errors en contínua amb l'interruptor tancat i obert, i la resistència de càrrega de compromís. Limitacions en commutació: pol i zero, injecció de càrrega, crosstalk i temps d'establiment. Especificacions dels multiplexors i calibratge per canal. PGA i VGA: error de guany introduït per Ron amb exemple resolt i l'arquitectura que l'elimina.

*⏱️ Dedicació estimada: 13 min*

### [6. Referències de tensió i de corrent i mesures ratiomètriques](06_Unitat6_Referencies_i_mesures_ratiometriques.md)

Per què l'estabilitat de l'excitació limita l'exactitud global. Díodes, Zener i referències bandgap: la combinació de coeficients tèrmics oposats. Referències sèrie i shunt. Especificacions: exactitud inicial, deriva tèrmica, soroll, estabilitat a llarg termini i la distinció entre regulació de línia i de càrrega. Referències de corrent amb resistència de sensat i el rang de tensió de càrrega. Mesura ratiomètrica: la cancel·lació de l'excitació, les seves condicions i què no cancel·la.

*⏱️ Dedicació estimada: 8 min*

### [✓. Entrenament V/F](07_Unitat6_Entrenament.md)

50 afirmacions repartides entre els sis documents, en dues modalitats: simulacre en ordre aleatori amb cronòmetre i correcció al final, i entrenament lliure en l'ordre dels documents amb resposta immediata. Cada afirmació porta justificació i enllaç al document que la sustenta.

*⏱️ Simulacre cronometrat al ritme del qüestionari real*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.