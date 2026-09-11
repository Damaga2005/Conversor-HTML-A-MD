# Entrenament V/F · Unitat 6: Condicionament de sensors en contínua

Sistemes de Mesura (230920) · ETSETB-UPC · **Unitat 6 — Condicionament de sensors en contínua**

# Entrenament V/F

50 afirmacions repartides entre els sis documents de la unitat. Tot el càlcul es fa al vostre navegador: les respostes no s'envien enlloc.

**Simulacre cronometrat**
Les 50 afirmacions en ordre aleatori, amb cronòmetre i correcció al final. El temps es calcula a 30 s per afirmació, el ritme del qüestionari real.

**Entrenament lliure**
Les 50 afirmacions en l'ordre dels documents, sense rellotge i amb resposta immediata després de cada tria.

Les dues modalitats tenen tres respostes possibles: **Vertader**, **Fals** i **No ho sé**. Feu servir «No ho sé» quan realment no ho sabeu: al qüestionari real, endevinar penalitza.

Respostes: **0** / 50
Encerts: **0**
Corregir
Sortir

Corregir

Sistemes de Mesura · Grau en Enginyeria Electrònica de Telecomunicació · ETSETB-UPC. Prof. Miguel Ángel García González.

---

## 🧠 Banc d'Afirmacions d'Autoavaluació (Entrenament d'Examen)

> [!TIP] **Com utilitzar aquest material d'entrenament**
> Aquest banc conté **50 afirmacions clau** dissenyades per consolidar els conceptes de la unitat i preparar els qüestionaris d'avaluació continuada.
> Intenta respondre mentalment **Vertader (V)** o **Fals (F)** abans de desplegar la solució i la justificació tècnica.

### Qüestió 02
> 📌 **Afirmació:** *En sensors de sortida en continua, el criteri dominant de disseny és sempre l'amplada de banda per sobre de MHz.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En contínua el criteri dominant és la precisió DC, la deriva, el soroll de baixa freqüència i l'autoescalfament, no l'amplada de banda.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 06
> 📌 **Afirmació:** *L'objectiu pràctic del condicionador és aprofitar el marge dinàmic de l'ADC sense saturar-lo.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'objectiu enunciat: ocupar una fracció elevada del rang de l'ADC evitant saturacions.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 08
> 📌 **Afirmació:** *Les derives de temperatura dels components del condicionador poden contribuir a la incertesa de mesura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Tots els components de l'etapa de precondicionament poden derivar amb la temperatura, i per això se sol monitorar-la.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 13
> 📌 **Afirmació:** *En molts sensors resistius interessa mesurar sobretot variacions de resistència al voltant d'un valor de referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'objectiu no és R0 en valor absolut sinó ΔR, sovint de l'ordre de 10⁻³·R0 o menys.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 22
> 📌 **Afirmació:** *L'autoescalfament incrementa la sensibilitat del sensor sense introduir error sistemàtic.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *L'autoescalfament és un error sistemàtic, crític quan el sensor mesura precisament la temperatura del medi.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 26
> 📌 **Afirmació:** *La sensibilitat efectiva depèn del sensor, del condicionador i del rang utilitzable de l'ADC.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La sensibilitat efectiva depèn del sensor, del guany del condicionador i del rang de l'ADC.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 32
> 📌 **Afirmació:** *En una mesura a 2 fils, la resistència mesurada coincideix amb la del sensor encara que els cables tinguin resistència apreciable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La resistència mesurada val R + 2Rw.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 34
> 📌 **Afirmació:** *La mesura a 4 fils separa el camí de corrent del camí de mesura de tensió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un parell de cables injecta el corrent i un altre, independent, mesura la tensió.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 40
> 📌 **Afirmació:** *Els sensors de valor resistiu baix són menys sensibles als errors de resistència de cable.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Al revés: com més baixa és la resistència nominal, més crític és l'error de cable.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 42
> 📌 **Afirmació:** *Amb una font de corrent simple, la sortida queda automàticament centrada a zero per al valor R0.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La sortida arrossega una component contínua V0 = I·R0.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 48
> 📌 **Afirmació:** *En un divisor senzill, triar R propera a R0 sol maximitzar la sensibilitat local al voltant del punt de referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Per a x petit el màxim és a R = R0, amb Smax = Vref·α/4.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 53
> 📌 **Afirmació:** *La condició d'equilibri del pont correspon a la igualtat de les relacions de divisió de les dues branques.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *L'equilibri és la igualtat de les relacions de divisió de les dues branques.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 63
> 📌 **Afirmació:** *Augmentar k tendeix a reduir la sensibilitat intrínseca del pont.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La sensibilitat decau aproximadament com 1/k.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 66
> 📌 **Afirmació:** *L'error de no-linealitat del pont augmenta aproximadament amb el quadrat de k.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Decau aproximadament com 1/k²; no creix com k².*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 73
> 📌 **Afirmació:** *Les galgues de compensació es poden utilitzar per reduir l'efecte d'una pertorbació comuna com la temperatura.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La galga compensadora, a la mateixa temperatura però no sotmesa a la força, cancel·la la deriva tèrmica.*

> **📚 Document de referència:** `Document 02`
> </details>

### Qüestió 83
> 📌 **Afirmació:** *Per corrents molt petits, la resistència de càrrega necessària pot ser molt elevada.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Un fotodíode de 10 pA que hagi de donar 1 mV demana una resistència de l'ordre de 100 MΩ.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 84
> 📌 **Afirmació:** *Una resistència de càrrega molt gran redueix simultàniament el soroll tèrmic generat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El soroll tèrmic creix amb l'arrel quadrada del valor de la resistència.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 86
> 📌 **Afirmació:** *L'amplificador de transimpedància manté el node d'entrada inversora prop d'una massa virtual.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El curtcircuit virtual manté l'entrada inversora a massa virtual.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 87
> 📌 **Afirmació:** *En un amplificador de transimpedància ideal, la sortida depèn principalment de Ip/Rf.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La sortida val Ip·Rf, no Ip/Rf.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 88
> 📌 **Afirmació:** *Els corrents de polarització de l'operacional poden generar offsets a través de la resistència de realimentació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Circulen per Rf i generen una tensió d'offset a la sortida que es confon amb el senyal.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 92
> 📌 **Afirmació:** *La tensió diferencial es defineix com la suma algebraica de les dues entrades respecte a massa.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La diferencial és la diferència de les entrades; el mode comú n'és el valor mitjà.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 94
> 📌 **Afirmació:** *En l'amplificador diferencial de quatre resistències, el CMRR ideal depèn de la igualtat exacta de relacions de resistències.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El guany en mode comú s'anul·la quan R1/R2 = R3/R4.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 99
> 📌 **Afirmació:** *Els CMRR s'han de combinar directament en dB mitjançant una suma algebraica simple.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal convertir-los a unitats lineals, combinar-los i tornar a dB al final.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 101
> 📌 **Afirmació:** *La impedància d'entrada d'un amplificador diferencial pot carregar la sortida d'un pont.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Zd = 2R és finita i pot carregar el pont.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 102
> 📌 **Afirmació:** *L'efecte de càrrega incrementa sempre el guany diferencial efectiu del conjunt pont-amplificador.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La càrrega redueix el guany efectiu per sota del valor nominal.*

> **📚 Document de referència:** `Document 03`
> </details>

### Qüestió 113
> 📌 **Afirmació:** *El guany de la primera etapa es pot ajustar mitjançant una única resistència externa en moltes arquitectures.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *G1 = 1 + 2Rf/Rg, ajustable amb una sola resistència externa.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 114
> 📌 **Afirmació:** *La primera etapa d'un AI de tres operacionals carrega fortament el pont perquè és inversora.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És no inversora i presenta una impedància d'entrada molt elevada.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 117
> 📌 **Afirmació:** *El CMRR d'un AI és independent del guany i de la freqüència en qualsevol dispositiu real.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El CMRR depèn del guany i de la freqüència: cal llegir-lo al rang d'ús.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 123
> 📌 **Afirmació:** *La tensió d'offset referida a l'entrada pot aparèixer com un error de zero després de l'amplificació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *Amb entrada diferencial zero la sortida val l'offset multiplicat pel guany.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 125
> 📌 **Afirmació:** *El PSRR quantifica la sensibilitat de la sortida a variacions de l'alimentació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la definició de PSRR.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 129
> 📌 **Afirmació:** *Una especificació en ppm/°C indica sempre un offset absolut expressat en volts.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *És una deriva relativa per grau, no un offset absolut en volts.*

> **📚 Document de referència:** `Document 04`
> </details>

### Qüestió 131
> 📌 **Afirmació:** *Un multiplexor analògic suma simultàniament tots els canals d'entrada abans de l'amplificació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Un multiplexor selecciona un camí de senyal, no suma els canals.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 134
> 📌 **Afirmació:** *La resistència de conducció d'un interruptor real equival a un curtcircuit ideal per a qualsevol càrrega.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *La sortida queda per sota de l'entrada segons la relació entre Ron i la impedància de càrrega.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 135
> 📌 **Afirmació:** *Els interruptors CMOS combinen dispositius de canal N i de canal P per obtenir una resistència de conducció més petita.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La resistència resultant és el paral·lel de les dues i, a més, molt més plana amb la tensió.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 136
> 📌 **Afirmació:** *El corrent de fuites pot produir una tensió residual a la sortida quan l'interruptor està obert.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *La tensió residual val ILKG·RLOAD.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 140
> 📌 **Afirmació:** *Els interruptors rail-to-rail transfereixen qualsevol tensió del sistema encara que superi tots els límits d'alimentació.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Admeten tensions dins del marge VSS–VDD, fins i tot molt a prop dels límits, però no fora de tots ells.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 142
> 📌 **Afirmació:** *La injecció de càrrega pot alterar temporalment la tensió de sortida després d'un canvi d'estat.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És la injecció de càrrega dels transistors del driver.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 144
> 📌 **Afirmació:** *En sistemes multiplexats ràpids, el temps d'establiment després de commutar és compatible automàticament amb qualsevol ADC.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Cal verificar-ho: no és automàticament compatible amb el temps de conversió de l'ADC.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 148
> 📌 **Afirmació:** *Les especificacions ON leakage i OFF leakage poden tenir valors diferents.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El fabricant especifica ON leakage i OFF leakage per separat.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 150
> 📌 **Afirmació:** *La commutació analògica elimina la necessitat de calibratge individual de canal en sistemes multicanal exigents.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *En sistemes multicanal exigents continua essent habitual el calibratge individual per canal.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 152
> 📌 **Afirmació:** *En un PGA, el guany se selecciona habitualment amb una entrada digital discreta.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *El PGA fixa el guany amb una entrada digital, entre un conjunt finit de valors.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 157
> 📌 **Afirmació:** *Col·locar l'interruptor en un node sense corrent apreciable pot reduir l'efecte de Ron sobre el guany.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *És l'arquitectura més emprada en PGA comercials, precisament per això.*

> **📚 Document de referència:** `Document 05`
> </details>

### Qüestió 163
> 📌 **Afirmació:** *Un díode en conducció directa proporciona una referència d'alta estabilitat tèrmica per a mesures de precisió.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Té un coeficient de −2 mV/°C, cosa que dona uns 100 mV de deriva en un rang de 50 °C.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 165
> 📌 **Afirmació:** *En una referència shunt, el corrent de polarització es reparteix entre la càrrega i el dispositiu de referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *IBIAS = ISHUNT + ILOAD.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 166
> 📌 **Afirmació:** *Les referències bandgap combinen termes amb coeficients tèrmics oposats per reduir la deriva.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ✅ **Vertader (V)**
> 
> **Justificació Tècnica:** *VBE decreix amb la temperatura i ΔVBE hi creix: sumats amb els factors adequats, la deriva es cancel·la.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 168
> 📌 **Afirmació:** *La regulació de línia descriu la variació de Vref amb el corrent de càrrega.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Això és la regulació de càrrega; la de línia descriu la variació amb la tensió d'alimentació.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 174
> 📌 **Afirmació:** *Els offsets de l'amplificador d'instrumentació es cancel·len completament perquè formen part de la mateixa referència.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Els offsets no són proporcionals a V i cal compensar-los per calibratge.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 177
> 📌 **Afirmació:** *El resultat digital d'una mesura ratiomètrica ideal depèn de l'excitació absoluta V.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El codi digital resulta independent de V.*

> **📚 Document de referència:** `Document 06`
> </details>

### Qüestió 183
> 📌 **Afirmació:** *El calibratge elimina permanentment les derives tèrmiques posteriors de tots els blocs del sistema.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *El calibratge corregeix el que és estable, no les derives tèrmiques posteriors.*

> **📚 Document de referència:** `Document 01`
> </details>

### Qüestió 189
> 📌 **Afirmació:** *Un guany més gran millora sempre la incertesa final del sistema.*
> 
> - [ ] **V** (Vertader)
> - [ ] **F** (Fals)
> 
> <details>
> <summary>💡 <b>Veure Resposta i Justificació Detallada</b></summary>
> 
> **Resposta Correcta:** ❌ **Fals (F)**
> 
> **Justificació Tècnica:** *Un guany més gran també amplifica offset, soroll i deriva, i pot excedir el rang admissible de l'ADC.*

> **📚 Document de referència:** `Document 01`
> </details>

---

## 📋 Solucionari Ràpid (Taula de Respostes i Justificacions)

| Nº | Resposta | Justificació Tècnica Resumida | Referència |
| :---: | :---: | :--- | :--- |
| **02** | **F** | En contínua el criteri dominant és la precisió DC, la deriva, el soroll de baixa freqüència i l'autoescalfament, no l... | Document 01 |
| **06** | **V** | És l'objectiu enunciat: ocupar una fracció elevada del rang de l'ADC evitant saturacions. | Document 01 |
| **08** | **V** | Tots els components de l'etapa de precondicionament poden derivar amb la temperatura, i per això se sol monitorar-la. | Document 01 |
| **13** | **V** | L'objectiu no és R0 en valor absolut sinó ΔR, sovint de l'ordre de 10⁻³·R0 o menys. | Document 01 |
| **22** | **F** | L'autoescalfament és un error sistemàtic, crític quan el sensor mesura precisament la temperatura del medi. | Document 01 |
| **26** | **V** | La sensibilitat efectiva depèn del sensor, del guany del condicionador i del rang de l'ADC. | Document 01 |
| **32** | **F** | La resistència mesurada val R + 2Rw. | Document 02 |
| **34** | **V** | Un parell de cables injecta el corrent i un altre, independent, mesura la tensió. | Document 02 |
| **40** | **F** | Al revés: com més baixa és la resistència nominal, més crític és l'error de cable. | Document 02 |
| **42** | **F** | La sortida arrossega una component contínua V0 = I·R0. | Document 02 |
| **48** | **V** | Per a x petit el màxim és a R = R0, amb Smax = Vref·α/4. | Document 02 |
| **53** | **V** | L'equilibri és la igualtat de les relacions de divisió de les dues branques. | Document 02 |
| **63** | **V** | La sensibilitat decau aproximadament com 1/k. | Document 02 |
| **66** | **F** | Decau aproximadament com 1/k²; no creix com k². | Document 02 |
| **73** | **V** | La galga compensadora, a la mateixa temperatura però no sotmesa a la força, cancel·la la deriva tèrmica. | Document 02 |
| **83** | **V** | Un fotodíode de 10 pA que hagi de donar 1 mV demana una resistència de l'ordre de 100 MΩ. | Document 03 |
| **84** | **F** | El soroll tèrmic creix amb l'arrel quadrada del valor de la resistència. | Document 03 |
| **86** | **V** | El curtcircuit virtual manté l'entrada inversora a massa virtual. | Document 03 |
| **87** | **F** | La sortida val Ip·Rf, no Ip/Rf. | Document 03 |
| **88** | **V** | Circulen per Rf i generen una tensió d'offset a la sortida que es confon amb el senyal. | Document 03 |
| **92** | **F** | La diferencial és la diferència de les entrades; el mode comú n'és el valor mitjà. | Document 03 |
| **94** | **V** | El guany en mode comú s'anul·la quan R1/R2 = R3/R4. | Document 03 |
| **99** | **F** | Cal convertir-los a unitats lineals, combinar-los i tornar a dB al final. | Document 03 |
| **101** | **V** | Zd = 2R és finita i pot carregar el pont. | Document 03 |
| **102** | **F** | La càrrega redueix el guany efectiu per sota del valor nominal. | Document 03 |
| **113** | **V** | G1 = 1 + 2Rf/Rg, ajustable amb una sola resistència externa. | Document 04 |
| **114** | **F** | És no inversora i presenta una impedància d'entrada molt elevada. | Document 04 |
| **117** | **F** | El CMRR depèn del guany i de la freqüència: cal llegir-lo al rang d'ús. | Document 04 |
| **123** | **V** | Amb entrada diferencial zero la sortida val l'offset multiplicat pel guany. | Document 04 |
| **125** | **V** | És la definició de PSRR. | Document 04 |
| **129** | **F** | És una deriva relativa per grau, no un offset absolut en volts. | Document 04 |
| **131** | **F** | Un multiplexor selecciona un camí de senyal, no suma els canals. | Document 05 |
| **134** | **F** | La sortida queda per sota de l'entrada segons la relació entre Ron i la impedància de càrrega. | Document 05 |
| **135** | **V** | La resistència resultant és el paral·lel de les dues i, a més, molt més plana amb la tensió. | Document 05 |
| **136** | **V** | La tensió residual val ILKG·RLOAD. | Document 05 |
| **140** | **F** | Admeten tensions dins del marge VSS–VDD, fins i tot molt a prop dels límits, però no fora de tots ells. | Document 05 |
| **142** | **V** | És la injecció de càrrega dels transistors del driver. | Document 05 |
| **144** | **F** | Cal verificar-ho: no és automàticament compatible amb el temps de conversió de l'ADC. | Document 05 |
| **148** | **V** | El fabricant especifica ON leakage i OFF leakage per separat. | Document 05 |
| **150** | **F** | En sistemes multicanal exigents continua essent habitual el calibratge individual per canal. | Document 05 |
| **152** | **V** | El PGA fixa el guany amb una entrada digital, entre un conjunt finit de valors. | Document 05 |
| **157** | **V** | És l'arquitectura més emprada en PGA comercials, precisament per això. | Document 05 |
| **163** | **F** | Té un coeficient de −2 mV/°C, cosa que dona uns 100 mV de deriva en un rang de 50 °C. | Document 06 |
| **165** | **V** | IBIAS = ISHUNT + ILOAD. | Document 06 |
| **166** | **V** | VBE decreix amb la temperatura i ΔVBE hi creix: sumats amb els factors adequats, la deriva es cancel·la. | Document 06 |
| **168** | **F** | Això és la regulació de càrrega; la de línia descriu la variació amb la tensió d'alimentació. | Document 06 |
| **174** | **F** | Els offsets no són proporcionals a V i cal compensar-los per calibratge. | Document 06 |
| **177** | **F** | El codi digital resulta independent de V. | Document 06 |
| **183** | **F** | El calibratge corregeix el que és estable, no les derives tèrmiques posteriors. | Document 01 |
| **189** | **F** | Un guany més gran també amplifica offset, soroll i deriva, i pot excedir el rang admissible de l'ADC. | Document 01 |