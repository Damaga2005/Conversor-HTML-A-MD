# Unitat 7 — Sensors reactius i electromagnètics · Lectura prèvia

## 📑 Índice de Contenidos

  - [[1. Fonaments dels sensors reactius](01_Unitat7_Fonaments_dels_sensors_reactius.md)](#1-fonaments-dels-sensors-reactius01-unitat7-fonaments-dels-sensors-reactiusmd)
  - [[2. El sensor capacitiu: model, geometries i linealitat](02_Unitat7_El_sensor_capacitiu_model_i_geometries.md)](#2-el-sensor-capacitiu-model-geometries-i-linealitat02-unitat7-el-sensor-capacitiu-model-i-geometriesmd)
  - [[3. El sensor capacitiu real: vores, guardes, fuita i freqüència de treball](03_Unitat7_El_sensor_capacitiu_real.md)](#3-el-sensor-capacitiu-real-vores-guardes-fuita-i-freqüència-de-treball03-unitat7-el-sensor-capacitiu-realmd)
  - [[4. Aplicacions dels sensors capacitius i el condensador diferencial](04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial.md)](#4-aplicacions-dels-sensors-capacitius-i-el-condensador-diferencial04-unitat7-aplicacions-capacitives-i-condensador-diferencialmd)
  - [[5. Sensors inductius i corrents de Foucault](05_Unitat7_Sensors_inductius_i_corrents_de_Foucault.md)](#5-sensors-inductius-i-corrents-de-foucault05-unitat7-sensors-inductius-i-corrents-de-foucaultmd)
  - [[6. Transformadors variables, efecte Hall i magnetostricció](06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio.md)](#6-transformadors-variables-efecte-hall-i-magnetostricció06-unitat7-transformadors-variables-hall-i-magnetostricciomd)

---

Sistemes de Mesura (230920) · ETSETB-UPC

# Unitat 7 — Sensors reactius i electromagnètics

Materials de lectura prèvia · dedicació total estimada: 68 minuts

Aquesta unitat es treballa amb metodologia d'**aula inversa**: les sessions presencials no exposen aquests continguts, sinó que resolen activitats que els pressuposen. Aquests documents contenen tot el que cal per preparar la unitat.

Llegeix els sis documents en ordre **abans de la primera sessió** i resol el qüestionari corresponent dins del termini indicat pel professor.

### [1. Fonaments dels sensors reactius](01_Unitat7_Fonaments_dels_sensors_reactius.md)

Què és un sensor reactiu i per quines raons físiques es prefereix al resistiu: mesura sense contacte, tolerància a entorns bruts, absència de soroll tèrmic i d'autoescalfament de l'element ideal. Per què cap dels dos tipus no es pot mesurar en contínua i què implica treballar en alterna. La freqüència de treball com a paràmetre de disseny i el que la condiciona. Sensors moduladors davant de generadors. Els quatre mecanismes de transducció de la unitat i on es troben aquests sensors.

*⏱️ Dedicació estimada: 8 min*

### [2. El sensor capacitiu: model, geometries i linealitat](02_Unitat7_El_sensor_capacitiu_model_i_geometries.md)

La capacitat com a variable de mesura i la funció de mesura C=g(x). El condensador pla C=epsilon·A/d, la condició d<<l i els ordres de magnitud. Impedància del condensador i l'asimetria de linealitat: si varia l'àrea o la permitivitat respon linealment C, i si varia la separació respon linealment el mòdul de la impedància. Les tres variants del condensador pla —àrea, separació i dielèctric variables— i les geometries esfèrica, coaxial, de cables paral·lels i de cable sobre pla. Criteris de tria del dielèctric.

*⏱️ Dedicació estimada: 8 min*

### [3. El sensor capacitiu real: vores, guardes, fuita i freqüència de treball](03_Unitat7_El_sensor_capacitiu_real.md)

Avantatges i limitacions respecte del sensor resistiu, incloses les capacitats paràsites i la seva deriva. L'efecte de vores: origen, error de Bromwich, dependència amb d/l i la no linealitat que introdueix. Modelat per elements finits i guardes de Kelvin, en una cara i en totes dues. La resistència de fuita del dielèctric, el model C en paral·lel amb Rp, el producte Rp·C=epsilon/sigma i la freqüència de tall. Tria de f0: per damunt de f-3dB i amb el mòdul d'impedància dins d'un rang manejable. Soroll i autoescalfament residuals.

*⏱️ Dedicació estimada: 12 min*

### [4. Aplicacions dels sensors capacitius i el condensador diferencial](04_Unitat7_Aplicacions_capacitives_i_condensador_diferencial.md)

Distància i desplaçament amb resolució nanomètrica, detecció de presència per pertorbació del camp, força i pressió a través d'un element elàstic, angle per solapament, nivell per permitivitat, inclinació i acceleració. Acceleròmetres MEMS de dents interdigitades i sensibilitat de l'ordre de pF/g. El condensador diferencial: model C0±deltaC, el quocient diferencial normalitzat, i els tres avantatges —sensibilitat doble, rebuig de mode comú i linealitat millorada.

*⏱️ Dedicació estimada: 8 min*

### [5. Sensors inductius i corrents de Foucault](05_Unitat7_Sensors_inductius_i_corrents_de_Foucault.md)

Autoinductància, model del solenoide i el significat de cada factor. Reluctància, entreferro i la relació L=N²/R. Què fa variar la inductància i com hi actuen els materials ferromagnètics i els conductors no ferromagnètics. Inductància mútua i la necessitat d'excitació alterna. L'objectiu metàl·lic com a limitació i com a fortalesa. Bobina d'aire davant de nucli ferromagnètic, ferrites i tria del conductor. Aplicacions de distància, força, gir, gruix i pressió. Corrents de Foucault, efecte pell, profunditat de penetració, mesura de distància a conductors no ferromagnètics i inspecció no destructiva.

*⏱️ Dedicació estimada: 15 min*

### [6. Transformadors variables, efecte Hall i magnetostricció](06_Unitat7_Transformadors_variables_Hall_i_magnetostriccio.md)

La LVDT: construcció en sèrie i oposició, sortida proporcional al desplaçament, posició de nul i tensió residual, fase de 0 o 180 graus per al signe, efectes no ideals i freqüència d'excitació òptima. El resolver: dependència en cosinus, dos secundaris en quadratura, atan2 i RDC, errors angulars; synchro i inductosyn. Efecte Hall: força de Lorentz, tensió Hall, per què semiconductors, compromís del gruix, comparació amb la magnetoresistència i aplicacions de presència, velocitat de rotació i mesura de corrent. Magnetostricció: efectes Joule, Villari, Wiedemann i Mateucci, Terfenol-D, sensors de temps de vol, de força i de torsió.

*⏱️ Dedicació estimada: 17 min*

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.