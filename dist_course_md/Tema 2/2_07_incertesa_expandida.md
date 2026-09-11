# U2·07 Incertesa expandida, factor de cobertura i graus de llibertat

## 📑 Índice de Contenidos

- [1 Definició i expressió del resultat](#1-definició-i-expressió-del-resultat)
- [2 El factor de cobertura en el cas normal](#2-el-factor-de-cobertura-en-el-cas-normal)
- [3 Poques dades: la distribució t de Student](#3-poques-dades-la-distribució-t-de-student)
- [4 Graus de llibertat efectius: Welch-Satterthwaite](#4-graus-de-llibertat-efectius-welch-satterthwaite)

---

> [!NOTE] **Objectius d'aprenentatge**
>
> - Calcular la incertesa expandida  $U=k\,u_c$  i triar el factor de cobertura segons la distribució i el nivell de confiança.
> - Associar els factors  $k=2$  i  $k=3$  als nivells del 95 % i del 99,7 % en el cas normal.
> - Reconèixer quan cal la distribució t de Student (poques mesures de tipus A).
> - Aplicar la fórmula de Welch-Satterthwaite per estimar els graus de llibertat efectius.

La incertesa típica combinada  $u_c$  és perfecta per als càlculs intermedis, però sovint insuficient per comunicar el resultat final: una desviació estàndard només cobreix aproximadament el 68 % de probabilitat (en el cas normal). Si diem «el valor és  $y\pm u_c$ », hi ha un 32 % de possibilitats que el valor real quedi fora, un risc d'1 de cada 3 inacceptable en la majoria d'aplicacions. Per això el pas final sol ser calcular la **incertesa expandida**  $U$, que amplia l'interval fins a un nivell de confiança superior.

## 1 Definició i expressió del resultat

La incertesa expandida és el producte de la incertesa típica combinada per un **factor de cobertura**  $k$:

$$
U=k\,u_c(y) \qquad (2.31)
$$

i el resultat final s'expressa aleshores com:

$$
Y=y\pm U \qquad (2.32)
$$

El nivell de confiança és la probabilitat que l'interval  $y\pm U$  contingui el valor veritable. No n'hi ha cap de «correcte» universal; depèn de l'aplicació: el **95 %** (o 95,45 %) és l'estàndard de facto en indústria i calibratge, i sovint es llegeix « $k=2$ »; el **99 %** (o 99,73 %) s'usa en aplicacions crítiques (seguretat, aeroespacial, salut), habitualment amb  $k=3$; en física de partícules es busquen certeses de «5 sigma». Un nivell de confiança més alt implica, en general, un interval més ample.

## 2 El factor de cobertura en el cas normal

El valor de  $k$  depèn de la distribució del resultat final i del nivell de confiança. Per avaluacions de tipus A la mitjana tendeix a una normal; per mesures indirectes, si cap font domina, pel teorema del límit central la sortida tendeix a una normal independentment de si les entrades eren uniformes o triangulars. Assumint normalitat, els factors són:

| Nivell de confiança | Factor  $k$ |
|:--- |:--- |
| 68,27 % | 1 |
| 90 % | 1,645 |
| 95 % | 1,96 |
| 95,45 % | 2 |
| 99 % | 2,576 |
| 99,73 % | 3 |

La regla pràctica més comuna és, doncs: «multiplica la incertesa combinada per 2 per obtenir aproximadament el 95 % de confiança». Per a nivells arbitraris, si s'assumeix normalitat el factor s'obté, en Python amb SciPy (`from scipy.stats import norm`), com `k = -norm.ppf((1-Conf/100)/2)` (per exemple, per al 99,9 % dona  $k=3{,}29$ ).

## 3 Poques dades: la distribució t de Student

La regla del  $k=2$  assumeix que la nostra estimació de la incertesa és sòlida i que la distribució és normal. Això és cert si les avaluacions de tipus A s'han fet amb moltes mostres i les de tipus B es coneixen amb precisió. Però si la incertesa dominant prové d'una repetibilitat de tipus A amb només 3 o 4 mesures, l'estimació de la dispersió és poc fiable: la distribució real no és normal, sinó una **t de Student** amb pocs graus de llibertat, que té *cues més amples*. Aleshores  $k$  ha de ser més gran que 2 per garantir el mateix 95 %. Per exemple, al 95 %: per  $\nu\to\infty$,  $k=1{,}96$; per  $\nu=9$,  $k\approx 2{,}26$; per  $\nu=3$,  $k\approx 3{,}18$. Usar  $k=2$  amb només 4 mesures donaria un nivell de confiança real molt inferior al 95 %. En Python amb SciPy (`from scipy.stats import t`) s'obté amb `k = -t.ppf((1-Conf/100)/2, N-1)`, on  $N$  és el nombre de mesures i  $\nu=N-1$  els graus de llibertat.

## 4 Graus de llibertat efectius: Welch-Satterthwaite

Quan combinem fonts, algunes poden ser molt sòlides (tipus B de full de dades, o tipus A amb  $N$  gran) i d'altres molt febles (tipus A amb poques mesures). Quin  $k$  fem servir per a la  $u_c$  global? La GUM ho resol calculant els **graus de llibertat efectius**  $\nu_{\text{ef}}$, una mena de mitjana ponderada que representa quanta informació equivalent tenim sobre la incertesa combinada:

$$
\nu_{\text{ef}}=\frac{u_c^{\,4}(y)}{ \sum_{i=1}^{N}\frac{u_i^{\,4}}{\nu_i}} \qquad (2.33)
$$

on  $u_i=c_i\,u(x_i)$  és la contribució de la font  $i$ -èsima i  $\nu_i$  els seus graus de llibertat. Per a les fonts de **tipus A**,  $\nu_i=N_i-1$. Per a les de **tipus B** basades en límits ben establerts, s'assumeix  $\nu_i\to\infty$, de manera que el seu terme al denominador s'anul·la. Si la font dominant té molts graus de llibertat,  $\nu_{\text{ef}}$  és gran i podem usar el  $k$  de la normal; si en té pocs,  $\nu_{\text{ef}}$  baixa i ens força a usar un  $k$  més gran (t de Student).

El procediment per a la incertesa expandida en mesures indirectes és, doncs: (1) calcular totes les contribucions  $u_i$  i la  $u_c$; (2) calcular  $\nu_{\text{ef}}$  amb Welch-Satterthwaite; (3) buscar el  $k$  corresponent a  $\nu_{\text{ef}}$  i al nivell de confiança desitjat (taula t de Student o funció de càlcul); i (4) calcular  $U=k\,u_c$.

> [!TIP] **Síntesi**
>
> La incertesa expandida  $U=k\,u_c$  amplia l'interval fins al nivell de confiança desitjat. En el cas normal,  $k=2$  correspon a ≈95 % i  $k=3$  a ≈99,73 %. Quan la incertesa dominant prové de poques mesures de tipus A, la distribució és una t de Student amb cues més amples. Els graus de llibertat efectius es calculen amb Welch-Satterthwaite (2.33), amb  $\nu_i=N_i-1$  per al tipus A i  $\nu_i\to\infty$  per al tipus B; el seu valor determina el  $k$  adequat per a la incertesa combinada.

[← 6. Combinació d'incerteses en mesures indirectes](2_06_combinacio.md)[Índex de la unitat](2_00_index.md)[8. Expressió final del resultat i balanç d'incertesa →](2_08_expressio_final.md)

---

## 📐 Formulario Resumen de Ecuaciones

| Nº / Ref | Expresión Matemática |
| :---: | :--- |
| **(2.31)** | $U=k\,u_c(y)$ |
| **(2.32)** | $Y=y\pm U$ |
| **(2.33)** | $\nu_{\text{ef}}=\frac{u_c^{\,4}(y)}{ \sum_{i=1}^{N}\frac{u_i^{\,4}}{\nu_i}}$ |