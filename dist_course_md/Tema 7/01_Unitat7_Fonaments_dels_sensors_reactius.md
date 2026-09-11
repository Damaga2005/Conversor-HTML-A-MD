# Fonaments dels sensors reactius

## 📑 Índice de Contenidos

- [1 Què és un sensor reactiu](#1-què-és-un-sensor-reactiu)
- [2 Per què reactius i no resistius](#2-per-què-reactius-i-no-resistius)
- [3 El cost: cal treballar en alterna](#3-el-cost-cal-treballar-en-alterna)
- [4 La freqüència de treball com a paràmetre de disseny](#4-la-freqüència-de-treball-com-a-paràmetre-de-disseny)
- [5 Els quatre mecanismes de transducció de la unitat](#5-els-quatre-mecanismes-de-transducció-de-la-unitat)
- [6 On es troben aquests sensors](#6-on-es-troben-aquests-sensors)

---

Sistemes de Mesura · **Unitat 7 — Sensors reactius i electromagnètics** · Document 1 de 6

# Fonaments dels sensors reactius

Dedicació estimada: 8 minuts

> [!NOTE] **Objectius d'aprenentatge**
>
> - Delimitar què és un sensor reactiu i per quines raons físiques es prefereix a un sensor resistiu.
> - Justificar per què un sensor reactiu no pot mesurar-se en contínua.
> - Situar la freqüència de treball  $f_0$
> com a paràmetre de disseny i enumerar què la condiciona.
> - Classificar els sensors del tema com a moduladors i distingir-los dels generadors.
> - Identificar els quatre mecanismes de transducció que es tracten en aquesta unitat.

A la unitat 5 s'han estudiat els sensors resistius, la família més coneguda històricament. Aquesta unitat tracta les altres dues del mateix grup —els **sensors capacitius** i els **sensors inductius**, que en conjunt reben el nom de **sensors reactius**— i, a més, dos grups basats en efectes electromagnètics que no encaixen en cap de les dues: els sensors d'**efecte Hall**, que donen una tensió transversal proporcional al camp magnètic que travessa una làmina conductora, i els sensors **magnetostrictius**, que exploten l'acoblament entre magnetització i deformació mecànica d'alguns materials ferromagnètics.

## 1 Què és un sensor reactiu

Un sensor és **reactiu** quan el seu element sensor és un condensador o una bobina, és a dir, un element de naturalesa **reactiva i no dissipativa**: emmagatzema energia en un camp —elèctric en el condensador, magnètic en la bobina— en lloc de convertir-la en calor. El mesurand actua modificant la capacitat, l'autoinductància o la inductància mútua de l'element, i el sistema de mesura llegeix aquesta variació d'impedància.

Tots els sensors d'aquesta unitat, inclosos els d'efecte Hall i els magnetostrictius, són **sensors moduladors**: el mesurand modifica alguna propietat del sensor però no aporta l'energia del senyal de sortida, que prové d'una **excitació externa**.

La distinció importa perquè alguns d'aquests sensors lliuren una tensió al terminal de sortida i podrien confondre's amb generadors. És el cas de la **LVDT**, un transformador de nucli mòbil que dona una tensió proporcional al desplaçament: sense excitació al seu bobinatge primari, però, no hi ha cap senyal. Els sensors que generen l'energia del senyal a partir del mesurand es tracten a la unitat 9.

## 2 Per què reactius i no resistius

La decisió de fer servir un condensador o una bobina com a element transductor, en lloc d'una resistència, respon a quatre avantatges físics concrets.

| Avantatge | Origen físic |
|:--- |:--- |
| **Mesura sense contacte** | Un condensador no necessita contacte físic: n'hi ha prou amb variar la separació entre plaques o la superfície de solapament. Una bobina detecta la proximitat d'un metall a través del camp magnètic. S'eliminen el desgast, la fricció i el soroll elèctric del contacte lliscant d'un potenciòmetre. |
| **Tolerància a la brutícia** | La pols, l'oli i altres substàncies sense resposta davant de camps magnètics no pertorben la mesura inductiva, cosa que fa aquests sensors especialment apreciats en entorns industrials agressius. |
| **Absència de soroll tèrmic** | Un element reactiu ideal no dissipa energia i per tant no genera soroll de Johnson-Nyquist. Qualsevol resistència a temperatura superior al zero absolut sí que en genera. D'aquí una resolució potencial superior, rellevant en metrologia i instrumentació científica. |
| **Absència d'autoescalfament** | Sense dissipació no hi ha escalfament propi, que és un dels errors sistemàtics principals dels sensors resistius. |

Aquests avantatges valen per a l'element **ideal**. El sensor real incorpora resistències, capacitats i inductàncies paràsites que reintrodueixen, atenuats, tant el soroll com la dissipació.

## 3 El cost: cal treballar en alterna

El preu d'utilitzar elements reactius és que la seva impedància **depèn de la freqüència del senyal d'excitació**. En contínua, la impedància d'un condensador ideal és infinita i la d'una inductància ideal és nul·la: en tots dos casos, el valor de la impedància no conté cap informació sobre el mesurand. Cal, doncs, **excitar el sensor amb un senyal sinusoïdal** a una freqüència determinada, que s'anomena **freqüència de treball**  $f_0$
.

En els elements reals el límit és el mateix per una altra via. Una bobina real presenta en contínua la resistència òhmica del seu bobinatge, i és aquesta —no la inductància— la que domina la impedància a freqüència molt baixa; cal pujar en freqüència perquè la reactància inductiva  $\omega L$
 sigui rellevant davant d'aquesta resistència. Un condensador real presenta en contínua la resistència de fuita del seu dielèctric, que tampoc no depèn del mesurand.

> [!WARNING] **Convenció**
>
> Al llarg de la unitat,  $f$
> designa una freqüència genèrica i  $f_0$
> la freqüència de treball escollida per al sistema de mesura. La freqüència angular és  $\omega = 2\pi f$
>.

## 4 La freqüència de treball com a paràmetre de disseny

L'elecció de  $f_0$
 és un dels paràmetres de disseny més rellevants del sistema de mesura, i no es pot decidir mirant només el sensor:

- Si es tria **massa baixa**, la impedància del condensador és molt elevada i el sistema esdevé vulnerable a interferències captades per acoblament capacitiu.
- Si es tria **massa alta**, apareixen pèrdues en el nucli ferromagnètic d'una bobina, pèrdues dielèctriques i efectes de capacitats paràsites que degraden la mesura.

El valor òptim depèn simultàniament del tipus de sensor, del material del nucli o del dielèctric, del mesurand, de les condicions de l'entorn i del **circuit de condicionament**, perquè la freqüència determina alhora la impedància que aquest circuit veu i el pes dels efectes paràsits. El dimensionament complet del condicionador en alterna es tracta a la unitat 8.

## 5 Els quatre mecanismes de transducció de la unitat

| Família | Mecanisme |
|:--- |:--- |
| **Capacitius** | Entre dos conductors separats per un dielèctric s'emmagatzema energia en el camp elèctric. La capacitat depèn de la geometria dels conductors i de la permitivitat del dielèctric; qualsevol magnitud que modifiqui la forma del sensor o la naturalesa del dielèctric és detectable. |
| **Inductius** | Inducció electromagnètica. La inductància d'una bobina es veu modificada per la presència o el moviment de materials conductors o ferromagnètics propers que interaccionen amb el camp que ella mateixa genera. Cas particular: els **corrents de Foucault**, induïts en un conductor massís per un camp magnètic variable. |
| **Efecte Hall** | Portadors de càrrega en moviment que travessen un material prim en presència d'un camp magnètic perpendicular experimenten una força de Lorentz que els desvia i genera una diferència de tensió transversal, proporcional al camp i al corrent. |
| **Magnetostrictius** | Acoblament bidireccional entre l'estat magnètic i la deformació mecànica d'alguns materials ferromagnètics: el material es deforma en presència d'un camp, i una deformació mecànica en modifica la magnetització. |

Els sensors reactius es divideixen, a més, segons quantes bobines o elèctrodes hi intervenen. Els **sensors d'un sol element** mesuren la variació de la pròpia autoinductància o capacitat; els **sensors basats en transformadors variables** —LVDT, resolver, synchro, inductosyn— mesuren la variació de la **inductància mútua** entre bobines separades.

## 6 On es troben aquests sensors

Els acceleròmetres dels telèfons mòbils són majoritàriament dispositius MEMS de principi **capacitiu**, i la pantalla tàctil del mateix telèfon és una matriu de sensors capacitius que detecten la pertorbació del camp elèctric produïda per la proximitat del dit, que és conductor. En l'àmbit industrial, els sensors **inductius** de proximitat, presents a gairebé qualsevol línia d'automatització robòtica, detecten sense contacte si una peça metàl·lica ha arribat a una posició determinada, i les LVDT mesuren en aeronàutica el desplaçament de les superfícies de control amb precisió de micròmetres. Els sensors d'**efecte Hall** són a cada motor elèctric de commutació electrònica, als comptadors d'energia i a les portes dels frigorífics, i els **magnetostrictius** mesuren el nivell de líquids en dipòsits industrials amb resolució de dècimes de mil·límetre, fins i tot a temperatura i pressió extremes.

> [!TIP] **Síntesi**
>
> Un sensor reactiu té com a element sensor un condensador o una bobina, que emmagatzemen energia en un camp elèctric o magnètic en lloc de dissipar-la. D'aquí surten la mesura sense contacte, la tolerància a entorns bruts i l'absència de soroll tèrmic i d'autoescalfament de l'element ideal. El preu és que la impedància depèn de la freqüència: en contínua, la d'un condensador ideal és infinita i la d'una bobina ideal nul·la, de manera que cal excitar el sensor en alterna a una freqüència de treball  $f_0$
> que depèn del sensor, del material, de l'entorn i del condicionador. Tots els sensors de la unitat són moduladors: el mesurand modula un senyal d'excitació extern i no n'aporta l'energia. Els mecanismes són quatre: variació de capacitat, variació d'autoinductància o d'inductància mútua, efecte Hall i magnetostricció.

[2. El sensor capacitiu: model, geometries i linealitat →](02_Unitat7_El_sensor_capacitiu_model_i_geometries.md)