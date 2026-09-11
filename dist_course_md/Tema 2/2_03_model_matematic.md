# U2·03 El model matemàtic de la mesura

## 📑 Índice de Contenidos

- [1 La funció de mesura](#1-la-funció-de-mesura)
- [2 El model ha de ser complet](#2-el-model-ha-de-ser-complet)
- [3 Mesures directes i indirectes](#3-mesures-directes-i-indirectes)
- [4 Tipus A i tipus B: una classificació pel mètode](#4-tipus-a-i-tipus-b-una-classificació-pel-mètode)
- [5 Hipòtesis del model](#5-hipòtesis-del-model)

---

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

[← 2. Marc teòric i definicions fonamentals](2_02_marc_teoric.md)[Índex de la unitat](2_00_index.md)[4. Avaluació de la incertesa de tipus A →](2_04_tipus_A.md)

---

## 📐 Formulario Resumen de Ecuaciones

| Nº / Ref | Expresión Matemática |
| :---: | :--- |
| **(2.9)** | $Y=f(X_1,X_2,\dots,X_N)$ |
| **(2.10)** | $L=L_m\left[1+\alpha\left(T-T_0\right)\right]$ |