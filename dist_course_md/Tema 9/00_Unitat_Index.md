# Unitat 9 — Sensors generadors i unions semiconductores · Lectura prèvia

## 📑 Índice de Contenidos

  - [[1. Sensors generadors i efectes termoelèctrics](01_Unitat9_Sensors_generadors_i_efectes_termoelectrics.md)](#1-sensors-generadors-i-efectes-termoelèctrics01-unitat9-sensors-generadors-i-efectes-termoelectricsmd)
  - [[2. El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura](02_Unitat_El_termoparell_tipus_i_conversio.md)](#2-el-termoparell-resposta-tipus-normalitzats-i-conversió-tensiótemperatura02-unitat-el-termoparell-tipus-i-conversiomd)
  - [[3. Lleis termoelèctriques, compensació de la unió freda i prestacions](03_Unitat9_Lleis_unio_freda_i_prestacions.md)](#3-lleis-termoelèctriques-compensació-de-la-unió-freda-i-prestacions03-unitat9-lleis-unio-freda-i-prestacionsmd)
  - [[4. Sensors piezoelèctrics: efecte, materials, model elèctric i resposta](04_Unitat9_Sensors_piezoelectrics.md)](#4-sensors-piezoelèctrics-efecte-materials-model-elèctric-i-resposta04-unitat9-sensors-piezoelectricsmd)
  - [[5. Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig](05_Unitat9_Sensors_piroelectrics.md)](#5-sensors-piroelèctrics-polarització-espontània-dinàmica-i-detecció-dinfraroig05-unitat9-sensors-piroelectricsmd)
  - [[6. Sensors de temperatura basats en unions semiconductores](06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora.md)](#6-sensors-de-temperatura-basats-en-unions-semiconductores06-unitat9-sensors-de-temperatura-d-unio-semiconductoramd)

---

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 9 — Sensors generadors i unions semiconductores

Materials de lectura prèvia · dedicació total estimada: 63 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen.

Llegeix els sis documents en ordre **abans de la primera sessió**.

### [1. Sensors generadors i efectes termoelèctrics](01_Unitat9_Sensors_generadors_i_efectes_termoelectrics.md)

Què distingeix un sensor generador d'un sensor modulador: d'on prové l'energia del senyal de sortida i què implica per al condicionament —nivell de senyal, impedància de font, càrrega i banda de treball. Les tres famílies generadores i el fenomen físic de cadascuna. L'efecte Seebeck: el coeficient de Seebeck absolut com a propietat d'un conductor homogeni, la formulació en circuit obert, la unió calenta i la unió freda, i el coeficient de Seebeck diferencial. Els efectes Peltier i Thomson com a fonts d'error que s'eliminen llegint el sensor en obert.

*⏱️ Dedicació estimada: 9 min*

### [2. El termoparell: resposta, tipus normalitzats i conversió tensió–temperatura](02_Unitat_El_termoparell_tipus_i_conversio.md)

La tensió com a integral del coeficient de Seebeck diferencial i la seva aproximació lineal: el termoparell mesura diferència de temperatura. El model circuital i les tres conseqüències que se'n deriven. La normalització IEC 584-3 i ANSI, la intercanviabilitat i el seu preu en puresa dels materials. Els vuit tipus normalitzats amb materials, marge i sensibilitat, i els quatre criteris de tria. Taules i polinomis referits a una unió freda a 0 °C, i la interpolació.

*⏱️ Dedicació estimada: 7 min*

### [3. Lleis termoelèctriques, compensació de la unió freda i prestacions](03_Unitat9_Lleis_unio_freda_i_prestacions.md)

Les dues lleis dels metalls intermedis i la llei de les temperatures intermèdies, i què justifica cadascuna: intercalar cables i instruments, referir tots els materials al platí i tabular sempre amb la unió freda a 0 °C. Els cables d'extensió i de compensació. El muntatge pràctic sobre bloc isoterm. La compensació de la unió freda, la tensió corregida i la propagació de l'error de la mesura de la temperatura de referència. Avantatges i limitacions dels termoparells i el que exigeixen a l'amplificador.

*⏱️ Dedicació estimada: 8 min*

### [4. Sensors piezoelèctrics: efecte, materials, model elèctric i resposta](04_Unitat9_Sensors_piezoelectrics.md)

La piezoelectricitat i la simetria cristal·lina: 32 classes, 20 piezoelèctriques, 10 piroelèctriques. Efecte directe i efecte invers. Els coeficients de càrrega, els seus índexs i les seves unitats, i per què importa l'orientació del tall. El poling, la temperatura de Curie i la compensació tèrmica amb estructures multicapa. Les tres famílies de materials i el criteri de tria segons si interessa la sensibilitat en càrrega o en tensió. El model de condensador amb resistència de fuita, la resposta passa-alt i l'efecte de la impedància d'entrada, la ressonància mecànica i les aplicacions.

*⏱️ Dedicació estimada: 14 min*

### [5. Sensors piroelèctrics: polarització espontània, dinàmica i detecció d'infraroig](05_Unitat9_Sensors_piroelectrics.md)

La polarització espontània dependent de la temperatura i per què el sensor no dona senyal en règim estacionari. L'estructura de condensador amb capa absorbent, el desacoblament mecànic i la configuració diferencial de dues cel·les. Els coeficients piroelèctrics de càrrega i de tensió, la relació entre tots dos i l'estimació de la càrrega i la tensió generades. Les constants de temps tèrmica i elèctrica i la resposta de dues exponencials a un pols de radiació. La detecció d'infraroig, el chopping, la lent de Fresnel i les limitacions dels detectors PIR.

*⏱️ Dedicació estimada: 13 min*

### [6. Sensors de temperatura basats en unions semiconductores](06_Unitat9_Sensors_de_temperatura_d_unio_semiconductora.md)

Per què desplacen les RTD i els termistors en el marge de l'electrònica integrada: cost, integrabilitat i intercanviabilitat. La unió polaritzada a corrent constant —díode o transistor NPN amb col·lector i base curtcircuitats—, l'equació de Shockley i per què la tensió directa baixa uns 2 mV/°C en pujar la temperatura, amb l'aproximació lineal i la seva inversa. Les quatre limitacions: repetibilitat del corrent de saturació, la seva variació amb la temperatura, autoescalfament i necessitat de corrent constant. La dispersió entre dispositius, el calibratge a dos punts i el pressupost d'error. Els sensors PTAT i la diferència de tensions base-emissor independent del corrent de saturació. Sortides digitals i prestacions.

*⏱️ Dedicació estimada: 12 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.