# -*- coding: utf-8 -*-
"""
Generate subject modules for Q3 and Q4 (10 subjects total, 12 questions each = 120 questions).
"""
import json

q3_q4_data = {
    # 230910: DE (Dispositivos Electrónicos)
    "230910": {
        "code": "230910", "acronym": "DE", "title": "Dispositivos Electrónicos", "semester": 3, "ects": 6.0,
        "department": "710 - EEL - Departamento de Ingeniería Electrónica",
        "description": "Física de semiconductores (bandas de energía, dopaje, portadores, recombinación y transporte por arrastre y difusión), unión p-n en equilibrio y polarización, diodos Zener y Schottky, transistores bipolares BJT (Gummel-Poon y Ebers-Moll), transistores MOSFET (acumulación, desierto, inversión, canal largo y corto, efecto cuerpo y modulación de longitud de canal).",
        "formulas": [
            {"name": "Densidad Intrínseca de Portadores", "latex": r"n_i = \sqrt{N_c N_v} e^{-\frac{E_g}{2 k T}} \approx 1.5 \times 10^{10}\,\text{cm}^{-3} \text{ en Si a } 300\,\text{K}"},
            {"name": "Relación de Einstein para Portadores", "latex": r"\frac{D_n}{\mu_n} = \frac{D_p}{\mu_p} = \frac{k T}{q} = V_T \approx 25.86\,\text{mV}"},
            {"name": "Potencial de Contacto Unión p-n", "latex": r"V_{bi} = V_T \ln\left( \frac{N_A N_D}{n_i^2} \right)"},
            {"name": "Corriente de Drenador MOSFET en Saturación", "latex": r"I_D = \frac{1}{2} \mu_n C_{ox} \frac{W}{L} (V_{GS} - V_{th})^2 (1 + \lambda V_{DS})"},
            {"name": "Anchura de la Zona de Carga Espacial (ZCE)", "latex": r"W = \sqrt{\frac{2 \varepsilon_s}{q} \left( \frac{1}{N_A} + \frac{1}{N_D} \right) (V_{bi} - V_A)}"}
        ],
        "calc_params": {"vgs": 3.0, "vth": 0.7, "kn_prime": 100e-6, "w_l_ratio": 10.0, "lambda_mod": 0.02, "vds": 4.0},
        "calc_outputs": ["id_sat_ma", "vds_sat_v", "gm_ms", "ro_kohm"],
        "calc_fn": "def calc(p):\n    vgs = p.get('vgs', 3.0)\n    vth = p.get('vth', 0.7)\n    vov = max(0.0, vgs - vth)\n    kn = p.get('kn_prime', 100e-6) * p.get('w_l_ratio', 10.0)\n    lam = p.get('lambda_mod', 0.02)\n    vds = p.get('vds', 4.0)\n    id_sat = 0.5 * kn * (vov**2) * (1.0 + lam * vds)\n    gm = kn * vov * (1.0 + lam * vds)\n    ro = (1.0 / (lam * max(1e-9, id_sat))) if lam > 0 else 1e9\n    return {'id_sat_ma': round(id_sat * 1000, 3), 'vds_sat_v': round(vov, 3), 'gm_ms': round(gm * 1000, 3), 'ro_kohm': round(ro / 1000, 2)}",
        "spice_template": "* DE - Curva Caracteristica Id vs Vds del MOSFET nMOS\nM1 d g 0 0 NMOS_UPC W=10u L=1u\nVds d 0 DC 0\nVgs g 0 DC 2.5\n.model NMOS_UPC NMOS(LEVEL=1 VTO=0.7 KP=100u LAMBDA=0.02)\n.dc Vds 0 5 0.05 Vgs 1 3 0.5\n.print dc I(M1)\n.end\n",
        "questions": [
            {"q": "¿En un semiconductor intrínseco, la concentración de electrones en la banda de conducción es igual a la de huecos en la de valencia (n = p = ni)?", "a": "V", "j": "Verdadero. Cada salto térmico a conducción crea simultáneamente un hueco en valencia."},
            {"q": "¿La relación de Einstein vincula el coeficiente de difusión y la movilidad de portadores con la tensión térmica VT = kT/q?", "a": "V", "j": "Verdadero. D / mu = VT."},
            {"q": "¿Al polarizar una unión p-n en inversa, la anchura de la zona de carga espacial (ZCE) aumenta?", "a": "V", "j": "Verdadero. La tensión inversa externa se suma al potencial de contacto interno ampliando la barrera."},
            {"q": "En un transistor MOSFET de canal n en saturación, la corriente de drenador es inversamente proporcional a (Vgs - Vth).", "a": "F", "j": "Falso. Es cuadrática: Id propto (Vgs - Vth)^2."},
            {"q": "¿El fenómeno de estricción o estrangulamiento de canal ('pinch-off') se alcanza cuando Vds >= Vgs - Vth?", "a": "V", "j": "Verdadero. El canal se estrangula cerca del drenador entrando en régimen de saturación."},
            {"q": "¿El dopaje con átomos del grupo V (como fósforo o arsénico) convierte al silicio en un semiconductor tipo n?", "a": "V", "j": "Verdadero. Aportan electrones libres en niveles donores."},
            {"q": "La corriente inversa de saturación Is de un diodo de silicio es insensible a las variaciones de temperatura.", "a": "F", "j": "Falso. Is se duplica aproximadamente cada 5 a 10 grados Celsius debido a la generación térmica exponencial ni^2(T)."},
            {"q": "¿El efecto Early en un transistor BJT representa la modulación de la anchura efectiva de la base con la tensión Vce?", "a": "V", "j": "Verdadero. Modifica ligeramente la pendiente de Ic en la zona activa."},
            {"q": "¿La capacidad de la zona de carga espacial en una unión polarizada en inversa depende del voltaje aplicado?", "a": "V", "j": "Verdadero. Cj = Cj0 / (1 - VA/Vbi)^m; actúa como condensador variable por tensión (varicap)."},
            {"q": "En un MOSFET en corte (subumbral ideal), la corriente de drenador es infinita.", "a": "F", "j": "Falso. Es prácticamente nula (del orden de pA a nA)."},
            {"q": "¿El parámetro de modulación de longitud de canal lambda introduce una conductancia de salida finita ro en el MOSFET en saturación?", "a": "V", "j": "Verdadero. ro = 1 / (lambda * Id)."},
            {"q": "¿En un diodo Zener el mecanismo de ruptura a tensiones bajas (< 5V) está dominado por el efecto túnel cuántico?", "a": "V", "j": "Verdadero. A tensiones mayores predomina la ruptura por ionización por avalancha."}
        ]
    },

    # 230911: DD (Diseño Digital)
    "230911": {
        "code": "230911", "acronym": "DD", "title": "Diseño Digital", "semester": 3, "ects": 6.0,
        "department": "710 - EEL - Departamento de Ingeniería Electrónica",
        "description": "Álgebra de Boole, funciones y puertas lógicas, minimización mediante mapas de Karnaugh, sistemas combinacionales clásicos (multiplexores, decodificadores, sumadores aritméticos, comparadores, ALU), biestables síncronos (D, JK, T), máquinas de estados finitos (FSM Mealy y Moore), temporización y descripción de hardware en VHDL.",
        "formulas": [
            {"name": "Teoremas de De Morgan", "latex": r"\overline{A \cdot B} = \overline{A} + \overline{B}, \quad \overline{A + B} = \overline{A} \cdot \overline{B}"},
            {"name": "Ecuación de Tiempo de Reloj Mínimo", "latex": r"T_{clk} \ge t_{cq} + t_{comb,\max} + t_{setup} - t_{skew}"},
            {"name": "Condición de Evitación de Fallo por Hold", "latex": r"t_{cq,\min} + t_{comb,\min} \ge t_{hold} + t_{skew}"},
            {"name": "Número de Salidas en Decodificador N a 2^N", "latex": r"M = 2^N"},
            {"name": "Ecuación Característica Biestable D", "latex": r"Q_{next} = D"}
        ],
        "calc_params": {"t_cq_ns": 1.2, "t_comb_ns": 4.5, "t_setup_ns": 0.8, "t_skew_ns": 0.2},
        "calc_outputs": ["t_clk_min_ns", "f_max_mhz", "hold_slack_ns"],
        "calc_fn": "def calc(p):\n    tcq = p.get('t_cq_ns', 1.2)\n    tcomb = p.get('t_comb_ns', 4.5)\n    tsetup = p.get('t_setup_ns', 0.8)\n    tskew = p.get('t_skew_ns', 0.2)\n    tclk = tcq + tcomb + tsetup - tskew\n    fmax = (1000.0 / tclk) if tclk > 0 else 0.0\n    slack_hold = (tcq * 0.7) - (0.4 + tskew)\n    return {'t_clk_min_ns': round(tclk, 3), 'f_max_mhz': round(fmax, 2), 'hold_slack_ns': round(slack_hold, 3)}",
        "spice_template": "-- DD - Registro de Desplazamiento Sincrono con Reset en VHDL\nlibrary ieee;\nuse ieee.std_logic_1164.all;\nentity shift_reg is\n    port (clk, rst, din : in std_logic; qout : out std_logic_vector(3 downto 0));\nend entity;\narchitecture rtl of shift_reg is\n    signal r_reg : std_logic_vector(3 downto 0) := (others => '0');\nbegin\n    process(clk, rst) begin\n        if rst = '1' then r_reg <= (others => '0');\n        elsif rising_edge(clk) then r_reg <= r_reg(2 downto 0) & din;\n        end if;\n    end process;\n    qout <= r_reg;\nend architecture;\n",
        "questions": [
            {"q": "¿El mapa de Karnaugh de 4 variables agrupa minterms adyacentes que difieren en exactamente 1 solo bit (código Gray)?", "a": "V", "j": "Verdadero. La adyacencia espacial refleja la adyacencia lógica para simplificar A + not(A) = 1."},
            {"q": "¿En una máquina de estados finitos (FSM) tipo Moore, las salidas dependen exclusivamente del estado actual?", "a": "V", "j": "Verdadero. A diferencia del modelo Mealy donde las salidas dependen del estado y de las entradas presentes."},
            {"q": "El tiempo de setup (t_setup) es el tiempo que debe mantenerse estable la entrada de datos después del flanco activo de reloj.", "a": "F", "j": "Falso. Ese es el tiempo de hold (t_hold); el tiempo de setup es antes del flanco activo de reloj."},
            {"q": "¿Un multiplexor de 2^N entradas de datos requiere exactamente N líneas de selección?", "a": "V", "j": "Verdadero. Las N líneas direccionan unívocamente una de las 2^N entradas."},
            {"q": "¿Los riesgos lógicos estáticos (hazards) pueden eliminarse añadiendo términos producto redundantes en la suma de productos?", "a": "V", "j": "Verdadero. Cubren las transiciones entre lazos adyacentes en el mapa de Karnaugh."},
            {"q": "Un latch tipo D con entrada de habilitación transparente es disparado exclusivamente por flanco de reloj.", "a": "F", "j": "Falso. Los latches son sensibles por nivel (transparentes mientras enable = 1); los biestables flip-flops son disparados por flanco."},
            {"q": "¿La metaestabilidad en sistemas síncronos puede ocurrir si se violan los tiempos de setup o hold en un biestable?", "a": "V", "j": "Verdadero. La salida puede oscilar o quedar en un valor intermedio indeterminado durante un tiempo no acotado."},
            {"q": "¿En VHDL, la sentencia 'process(clk)' con 'rising_edge(clk)' infiere almacenamiento síncrono en registros?", "a": "V", "j": "Verdadero. Estructura estándar de síntesis de biestables flip-flop."},
            {"q": "Una puerta XOR con entradas A y B devuelve '1' si y solo si ambas entradas valen '1'.", "a": "F", "j": "Falso. Esa es una puerta AND; la XOR devuelve '1' si las entradas son distintas (uno exclusivamente)."},
            {"q": "¿El sumador Ripple-Carry tiene un retardo proporcional al número de bits N debido a la propagación del acarreo?", "a": "V", "j": "Verdadero. t_delay = N * t_carry; para reducirlo se utilizan sumadores Carry-Lookahead."},
            {"q": "¿El complemento a dos permite representar números enteros con signo facilitando sumas y restas con el mismo hardware?", "a": "V", "j": "Verdadero. La resta A - B se computa directamente como A + (~B + 1)."},
            {"q": "¿La simplificación booleana A + A*B = A se conoce como la ley de absorción?", "a": "V", "j": "Verdadero. A*(1 + B) = A*1 = A."}
        ]
    },

    # 230912: EAFO (Electromagnetismo Aplicado y Fotónica)
    "230912": {
        "code": "230912", "acronym": "EAFO", "title": "Electromagnetismo Aplicado y Fotónica", "semester": 3, "ects": 6.0,
        "department": "739 - TSC - Departamento de Teoría de la Señal y Comunicaciones",
        "description": "Líneas de transmisión guiadas (ecuaciones del telegrafista, impedancia característica Z0, coeficiente de reflexión, carta de Smith, adaptación de impedancias), guías de ondas rectangulares (modos TE y TM, frecuencias de corte), óptica electromagnética y fotónica básica (ley de Snell, reflexión interna total, fibras ópticas monomodo y multimodo, atenuación y dispersión cromática).",
        "formulas": [
            {"name": "Coeficiente de Reflexión en Línea de Transmisión", "latex": r"\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}"},
            {"name": "Relación de Onda Estacionaria (ROE / VSWR)", "latex": r"\text{ROE} = \frac{1 + |\Gamma|}{1 - |\Gamma|}"},
            {"name": "Apertura Numérica de Fibra Óptica", "latex": r"\text{NA} = \sqrt{n_{\text{core}}^2 - n_{\text{clad}}^2} = \sin \theta_{\max}"},
            {"name": "Frecuencia de Corte en Guía de Onda Rectangular", "latex": r"f_{c,mn} = \frac{c}{2 \sqrt{\varepsilon_r}} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}"},
            {"name": "Parámetro V de Fibra Óptica (Frecuencia Normalizada)", "latex": r"V = \frac{2\pi a}{\lambda_0} \text{NA} \quad (V < 2.405 \implies \text{Monomodo})"}
        ],
        "calc_params": {"zl_real": 100.0, "zl_imag": 0.0, "z0": 50.0, "n_core": 1.48, "n_clad": 1.46, "core_diam_um": 8.2, "lambda_nm": 1550.0},
        "calc_outputs": ["gamma_mag", "vswr", "na_fiber", "v_param", "is_single_mode"],
        "calc_fn": "def calc(p):\n    import math\n    z0 = p.get('z0', 50.0)\n    zr = p.get('zl_real', 100.0)\n    zi = p.get('zl_imag', 0.0)\n    num_r, num_i = zr - z0, zi\n    den_r, den_i = zr + z0, zi\n    mag_num = math.sqrt(num_r**2 + num_i**2)\n    mag_den = math.sqrt(den_r**2 + den_i**2)\n    gamma = mag_num / max(1e-6, mag_den)\n    vswr = (1.0 + gamma) / max(1e-6, 1.0 - gamma)\n    n1 = p.get('n_core', 1.48)\n    n2 = p.get('n_clad', 1.46)\n    na = math.sqrt(max(0.0, n1**2 - n2**2))\n    a = (p.get('core_diam_um', 8.2) * 1e-6) / 2.0\n    lam = p.get('lambda_nm', 1550.0) * 1e-9\n    v_param = (2.0 * math.pi * a / lam) * na\n    single_mode = bool(v_param < 2.4048)\n    return {'gamma_mag': round(gamma, 4), 'vswr': round(vswr, 3), 'na_fiber': round(na, 4), 'v_param': round(v_param, 3), 'is_single_mode': single_mode}",
        "spice_template": "* EAFO - Desadaptacion en Linea de Transmision RF (50 a 100 Ohms)\nT1 in 0 out 0 Z0=50 TD=2ns\nVin in 0 PULSE(0 2 0 100p 100p 20n 50n)\nRs in 1 50\nRL out 0 100\n.tran 50p 15n\n.print tran V(in) V(out)\n.end\n",
        "questions": [
            {"q": "¿Cuando una carga está perfectamente adaptada a una línea (ZL = Z0), el coeficiente de reflexión Gamma es exactamente cero?", "a": "V", "j": "Verdadero. No hay onda reflejada; toda la potencia incidente se transmite a la carga."},
            {"q": "¿En una línea en cortocircuito (ZL = 0), el módulo del coeficiente de reflexión es |Gamma| = 1 con fase de 180 grados?", "a": "V", "j": "Verdadero. Gamma = -1 = 1 /_ 180."},
            {"q": "La Relación de Onda Estacionaria (VSWR) de una carga adaptada es 0.", "a": "F", "j": "Falso. La ROE ideal es 1 (VSWR = 1). Puede oscilar entre 1 e infinito."},
            {"q": "¿La reflexión interna total en la interfaz núcleo-cubierta de una fibra óptica exige que n_core > n_clad?", "a": "V", "j": "Verdadero. La luz debe viajar desde el medio más denso hacia el menos denso con ángulo superior al crítico."},
            {"q": "¿Una fibra óptica opera en régimen monomodo estricto si su parámetro de frecuencia normalizada satisface V < 2.405?", "a": "V", "j": "Verdadero. 2.4048 es el primer cero de la función de Bessel J0."},
            {"q": "En el modo fundamental TE10 de una guía de onda rectangular, la longitud de onda de corte es lambda_c = 2*a.", "a": "V", "j": "Verdadero. 'a' es la anchura mayor de la guía rectangular."},
            {"q": "Las guías de ondas metálicas cerradas huecas pueden propagar modos TEM a frecuencias intermedias.", "a": "F", "j": "Falso. Un modo TEM requiere al menos dos conductores aislados (como el cable coaxial o bifilar)."},
            {"q": "¿La Carta de Smith es un diagrama polar del coeficiente de reflexión Gamma mapeado sobre el plano de impedancias normalizadas?", "a": "V", "j": "Verdadero. Transforma circunferencias de resistencia y reactancia constantes en el círculo unitario |Gamma| <= 1."},
            {"q": "¿La apertura numérica (NA) cuantifica la capacidad angular de captación de luz de una fibra óptica?", "a": "V", "j": "Verdadero. NA = sin(theta_max) = sqrt(n1^2 - n2^2)."},
            {"q": "La atenuación mínima en fibras ópticas estándar de sílice monomodo ocurre a una longitud de onda cercana a 850 nm.", "a": "F", "j": "Falso. La tercera ventana óptica a 1550 nm ofrece la atenuación mínima (approx 0.2 dB/km)."},
            {"q": "¿Un transformador de cuarto de onda con impedancia Z_t = sqrt(Z0 * ZL) adapta una carga puramente resistiva ZL a una línea Z0?", "a": "V", "j": "Verdadero. Zin = Z_t^2 / ZL = Z0."},
            {"q": "¿La dispersión cromática en fibras ópticas provoca el ensanchamiento temporal de los pulsos luminosos reduciendo la tasa binaria máxima?", "a": "V", "j": "Verdadero. Debido a la dependencia del índice de refracción con la longitud de onda (dispersión del material y de guía)."}
        ]
    },

    # 230913: SST (Señales y Sistemas)
    "230913": {
        "code": "230913", "acronym": "SST", "title": "Señales y Sistemas", "semester": 3, "ects": 6.0,
        "department": "739 - TSC - Departamento de Teoría de la Señal y Comunicaciones",
        "description": "Señales continuas y discretas, sistemas lineales e invariantes en el tiempo (LTI), convolución temporal, series y transformada de Fourier continua y discreta (CTFT, DTFT, DFT/FFT), teorema de muestreo de Nyquist-Shannon, aliasing, y función de transferencia en transformada Z con análisis de estabilidad BIBO.",
        "formulas": [
            {"name": "Integral de Convolución Continua", "latex": r"y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau"},
            {"name": "Teorema de Muestreo de Nyquist-Shannon", "latex": r"f_s > 2 f_{\max} = f_{\text{Nyquist}}"},
            {"name": "Transformada Z Bilateral", "latex": r"X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}"},
            {"name": "Condición de Estabilidad BIBO en Tiempo Discreto", "latex": r"\sum_{n=-\infty}^{\infty} |h[n]| < \infty \iff \text{Polos de } H(z) \text{ dentro de } |z| < 1"},
            {"name": "Transformada Discreta de Fourier (DFT de N Puntos)", "latex": r"X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n}"}
        ],
        "calc_params": {"f_sig_hz": 1000.0, "fs_hz": 5000.0, "pole_mag": 0.8},
        "calc_outputs": ["nyquist_limit_hz", "is_nyquist_met", "dtft_omega_rad", "is_bibo_stable"],
        "calc_fn": "def calc(p):\n    import math\n    fsig = p.get('f_sig_hz', 1000.0)\n    fs = max(1.0, p.get('fs_hz', 5000.0))\n    nyq = 2.0 * fsig\n    met = bool(fs > nyq)\n    omega = 2.0 * math.pi * (fsig / fs)\n    r_pole = abs(p.get('pole_mag', 0.8))\n    stable = bool(r_pole < 1.0)\n    return {'nyquist_limit_hz': round(nyq, 1), 'is_nyquist_met': met, 'dtft_omega_rad': round(omega, 4), 'is_bibo_stable': stable}",
        "spice_template": "* SST - Respuesta al Impulso y Filtrado Pasobajo RC\nVin in 0 PULSE(0 1000 0 1n 1n 1u 10m)\nR1 in out 1k\nC1 out 0 100nF\n.tran 1u 2m\n.print tran V(out)\n.end\n",
        "questions": [
            {"q": "¿Un sistema LTI continuo es causal y estable BIBO si y solo si todos los polos de su función de transferencia H(s) se ubican estrictamente en el semiplano izquierdo Re(s) < 0?", "a": "V", "j": "Verdadero. Garantiza que la respuesta impulsional decaiga exponencialmente a cero."},
            {"q": "¿El teorema de Nyquist exige muestrear a una frecuencia estrictamente mayor que el doble del ancho de banda máximo para evitar aliasing?", "a": "V", "j": "Verdadero. fs > 2*fmax."},
            {"q": "La convolución en el dominio temporal equivale a la convolución en el dominio frecuencial de Fourier.", "a": "F", "j": "Falso. Equivale a la multiplicación punto a punto Y(w) = X(w) * H(w)."},
            {"q": "¿En un sistema LTI discreto causal, los polos de H(z) deben situarse dentro del círculo unidad (|z| < 1) para garantizar estabilidad?", "a": "V", "j": "Verdadero. La región de convergencia (ROC) debe abarcar la circunferencia unidad |z| = 1."},
            {"q": "¿La transformada discreta de Fourier de N puntos (DFT) computada mediante el algoritmo FFT tiene una complejidad O(N log2 N)?", "a": "V", "j": "Verdadero. Gran mejora frente al cálculo directo O(N^2)."},
            {"q": "La respuesta impulsional h(t) de un sistema estático sin memoria es proporcional a la función escalón unitario u(t).", "a": "F", "j": "Falso. Es proporcional a un impulso delta de Dirac K*delta(t)."},
            {"q": "¿Un sistema es invariante en el tiempo si un retardo en la entrada x(t - T) produce idéntico retardo en la salida y(t - T)?", "a": "V", "j": "Verdadero. Propiedad fundamental de invariancia temporal."},
            {"q": "¿La respuesta al escalón de un sistema LTI es la integral en el tiempo de su respuesta impulsional h(t)?", "a": "V", "j": "Verdadero. Dado que el escalón es la integral del impulso de Dirac."},
            {"q": "El aliasing espectral se puede corregir digitalmente después del convertidor ADC sin pérdida de información.", "a": "F", "j": "Falso. El aliasing solapa espectros irreversiblemente; debe eliminarse antes del muestreo con un filtro antialiasing analógico."},
            {"q": "¿La autocorrelación de una señal continua en el origen R_xx(0) equivale a la energía total de la señal?", "a": "V", "j": "Verdadero. R_xx(0) = integral(|x(t)|^2 dt) = E_total."},
            {"q": "¿Un filtro de fase lineal pura introduce un retardo de grupo constante en todas las frecuencias de la banda de paso evitando la distorsión de fase?", "a": "V", "j": "Verdadero. Mantiene intacta la forma de onda de la señal compuesta."},
            {"q": "El producto de dos funciones periódicas siempre da como resultado una función periódica para cualquier relación de periodos.", "a": "F", "j": "Falso. Solo es periódica si el cociente de sus periodos o frecuencias es un número racional."}
        ]
    },

    # 230914: PPE (Probabilidad y Procesos Estocásticos)
    "230914": {
        "code": "230914", "acronym": "PPE", "title": "Probabilidad y Procesos Estocásticos", "semester": 3, "ects": 6.0,
        "department": "749 - MAT / 739 - TSC",
        "description": "Espacios de probabilidad, probabilidad total y regla de Bayes, variables aleatorias discretas y continuas (Gaussianas, uniformes, Poisson, exponenciales), vectores aleatorios, momentos, covarianza y correlación, Teorema Central del Límite, procesos estocásticos estacionarios en sentido amplio (WSS), autocorrelación y densidad espectral de potencia (Wiener-Khinchin), y filtrado LTI de procesos aleatorios.",
        "formulas": [
            {"name": "Teorema de Bayes", "latex": r"P(A|B) = \frac{P(B|A) P(A)}{P(B)} = \frac{P(B|A) P(A)}{\sum_k P(B|A_k) P(A_k)}"},
            {"name": "Distribución Gaussiana Normal", "latex": r"f_X(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}"},
            {"name": "Teorema de Wiener-Khinchin", "latex": r"S_{xx}(f) = \mathcal{F}\{R_{xx}(\tau)\} = \int_{-\infty}^{\infty} R_{xx}(\tau) e^{-j 2\pi f \tau} d\tau"},
            {"name": "Filtrado LTI de Procesos WSS", "latex": r"S_{yy}(f) = |H(f)|^2 S_{xx}(f)"},
            {"name": "Coeficiente de Correlación de Pearson", "latex": r"\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \in [-1, 1]"}
        ],
        "calc_params": {"p_a": 0.01, "p_b_given_a": 0.95, "p_b_given_not_a": 0.05, "mu": 0.0, "sigma": 1.0, "x_val": 1.96},
        "calc_outputs": ["bayes_posterior", "gaussian_pdf_val", "q_func_approx"],
        "calc_fn": "def calc(p):\n    import math\n    pa = p.get('p_a', 0.01)\n    p_b_a = p.get('p_b_given_a', 0.95)\n    p_b_nota = p.get('p_b_given_not_a', 0.05)\n    pb = p_b_a * pa + p_b_nota * (1.0 - pa)\n    post = (p_b_a * pa) / max(1e-9, pb)\n    mu = p.get('mu', 0.0)\n    sig = max(1e-6, p.get('sigma', 1.0))\n    x = p.get('x_val', 1.96)\n    pdf = (1.0 / (sig * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu)/sig)**2)\n    z = (x - mu) / sig\n    q_approx = 0.5 * math.erfc(z / math.sqrt(2))\n    return {'bayes_posterior': round(post, 4), 'gaussian_pdf_val': round(pdf, 5), 'q_func_approx': round(q_approx, 5)}",
        "spice_template": "* PPE - Simulacion de Ruido Blanco Termico de Resistencia\nR1 in out 10k\nC1 out 0 10nF\n.noise V(out) R1 dec 20 100 100k\n.print noise onoise inoise\n.end\n",
        "questions": [
            {"q": "¿El Teorema de Wiener-Khinchin establece que la densidad espectral de potencia (PSD) de un proceso WSS es la transformada de Fourier de su autocorrelación?", "a": "V", "j": "Verdadero. Sxx(f) = F{Rxx(tau)}."},
            {"q": "¿Si dos variables aleatorias son independientes, su covarianza y su correlación son estrictamente cero?", "a": "V", "j": "Verdadero. La independencia implica incorrelación."},
            {"q": "La función de autocorrelación R_xx(tau) de un proceso WSS alcanza su máximo valor en el infinito.", "a": "F", "j": "Falso. Su valor máximo absoluto se encuentra siempre en el origen: |R_xx(tau)| <= R_xx(0)."},
            {"q": "¿El Teorema Central del Límite establece que la suma de un gran número de variables independientes e idénticamente distribuidas tiende asintóticamente a una distribución Gaussiana?", "a": "V", "j": "Verdadero. Pilar fundamental de la teoría de la probabilidad y del análisis de ruido."},
            {"q": "La varianza de una variable aleatoria puede tomar valores negativos si la media es negativa.", "a": "F", "j": "Falso. Por definición Var(X) = E[(X - mu)^2] >= 0; es siempre no negativa."},
            {"q": "¿Cuando un proceso WSS con densidad Sxx(f) pasa por un filtro LTI con respuesta H(f), la densidad espectral de salida es Syy(f) = |H(f)|^2 * Sxx(f)?", "a": "V", "j": "Verdadero. Relación espectral fundamental para sistemas lineales."},
            {"q": "¿La densidad espectral de un ruido blanco ideal es constante e idéntica en todas las frecuencias (S_w(f) = N0 / 2)?", "a": "V", "j": "Verdadero. De ahí el nombre 'blanco', por analogía con la luz blanca que contiene todas las frecuencias con igual energía."},
            {"q": "La función de distribución acumulada F_X(x) = P(X <= x) es siempre una función monótona no decreciente que varía entre 0 y 1.", "a": "V", "j": "Verdadero. Propiedad axiomática de toda variable aleatoria."},
            {"q": "¿Para dos eventos independientes A y B, la probabilidad de su intersección es P(A y B) = P(A) * P(B)?", "a": "V", "j": "Verdadero. Definición formal de independencia probabilística."},
            {"q": "Un proceso estocástico ergódico en la media tiene un promedio temporal diferente a su esperanza estadística de conjunto.", "a": "F", "j": "Falso. En un proceso ergódico, el promedio temporal sobre una realización coincide con el promedio estadístico de conjunto."},
            {"q": "¿La integral de menos infinito a más infinito de una función de densidad de probabilidad (PDF) es siempre exactamente 1?", "a": "V", "j": "Verdadero. Condición de normalización del espacio de probabilidad."},
            {"q": "¿El coeficiente de correlación de Pearson rho_XY está rigurosamente acotado en el intervalo [-1, +1]?", "a": "V", "j": "Verdadero. Desigualdad de Cauchy-Schwarz."}
        ]
    },

    # 230915: CA (Circuitos Analógicos)
    "230915": {
        "code": "230915", "acronym": "CA", "title": "Circuitos Analógicos", "semester": 4, "ects": 6.0,
        "department": "710 - EEL - Departamento de Ingeniería Electrónica",
        "description": "Etapas amplificadoras con BJT y MOSFET (emisor/fuente común, base/puerta común, colector/drenador común o seguidores), pares diferenciales con cargas activas (espejos de corriente Wilson y cascode), etapas de salida en potencia (Clase A, B, AB), respuesta en frecuencia (método de Miller, frecuencias de corte inferior y superior), realimentación negativa (topologías, estabilidad, margen de fase y compensación de Miller en amplificadores operacionales).",
        "formulas": [
            {"name": "Ganancia Etapa Fuente Común con Carga Activa", "latex": r"A_v = -g_m (r_o \parallel R_L)"},
            {"name": "Efecto Miller en Capacidad Parásita", "latex": r"C_{in,M} = C_{gd} (1 - A_v) \approx C_{gd} (1 + |A_v|)"},
            {"name": "Relación de Rechazo al Modo Común (CMRR)", "latex": r"\text{CMRR} = 20 \log_{10}\left( \frac{|A_d|}{|A_{cm}|} \right)"},
            {"name": "Margen de Fase (PM)", "latex": r"\text{PM} = 180^\circ + \angle T(j \omega_{0\text{dB}})"},
            {"name": "Producto Ganancia-Ancho de Banda (GBW)", "latex": r"\text{GBW} = A_0 \cdot f_{3\text{dB}} = \frac{g_m}{2\pi C_c}"}
        ],
        "calc_params": {"gm_ms": 5.0, "ro_kohm": 40.0, "rl_kohm": 10.0, "cgd_pf": 2.0, "cc_pf": 10.0},
        "calc_outputs": ["av_diff", "c_in_miller_pf", "gbw_mhz"],
        "calc_fn": "def calc(p):\n    import math\n    gm = p.get('gm_ms', 5.0) * 1e-3\n    ro = p.get('ro_kohm', 40.0) * 1e3\n    rl = p.get('rl_kohm', 10.0) * 1e3\n    req = (ro * rl) / (ro + rl)\n    av = gm * req\n    cgd = p.get('cgd_pf', 2.0)\n    cmiller = cgd * (1.0 + av)\n    cc = max(1e-13, p.get('cc_pf', 10.0) * 1e-12)\n    gbw = (gm / (2 * math.pi * cc)) * 1e-6\n    return {'av_diff': round(av, 2), 'c_in_miller_pf': round(cmiller, 2), 'gbw_mhz': round(gbw, 2)}",
        "spice_template": "* CA - Amplificador Fuente Comun NMOS con Respuesta en Frecuencia\nM1 out in 0 0 NMOS_CA W=20u L=0.5u\nRD vdd out 5k\nVdd vdd 0 DC 5V\nVin in 0 DC 1.2 AC 1m\n.model NMOS_CA NMOS(LEVEL=1 VTO=0.7 KP=150u CGDO=0.5n CGSO=0.5n)\n.ac dec 20 1k 1G\n.print ac V(out) VP(out)\n.end\n",
        "questions": [
            {"q": "¿El efecto Miller multiplica la capacidad parásita entre entrada y salida por un factor aproximadamente igual a 1 + |Av|?", "a": "V", "j": "Verdadero. Reduce significativamente la frecuencia de corte superior en etapas inversoras de alta ganancia."},
            {"q": "¿Una etapa seguidora de emisor (o fuente) presenta una ganancia de tensión cercana a la unidad (Av approx 1) y una baja impedancia de salida?", "a": "V", "j": "Verdadero. Se emplea comúnmente como etapa de acoplo (buffer)."},
            {"q": "La distorsión por cruce por cero (crossover distortion) es típica de los amplificadores de salida en Clase A.", "a": "F", "j": "Falso. Es característica de la Clase B pura; se corrige mediante una pequeña polarización en Clase AB."},
            {"q": "¿El par diferencial amplifica la diferencia entre sus dos entradas mientras rechaza las variaciones en modo común?", "a": "V", "j": "Verdadero. Caracterizado por una alta CMRR."},
            {"q": "¿Un margen de fase de al menos 45 a 60 grados garantiza un comportamiento estable con sobreoscilación moderada en bucle cerrado?", "a": "V", "j": "Verdadero. Criterio de estabilidad y amortiguamiento estándar en diseño analógico."},
            {"q": "¿La técnica de compensación por polo dominante de Miller en un op-amp consiste en intercalar un condensador Cc entre la entrada y salida de la segunda etapa?", "a": "V", "j": "Verdadero. Separa los polos (pole splitting) asegurando que la ganancia caiga por debajo de 0 dB antes del segundo polo."},
            {"q": "La impedancia de salida de una etapa en fuente común con carga de espejo de corriente cascode es extremadamente baja.", "a": "F", "j": "Falso. El cascode incrementa drásticamente la resistencia de salida por un factor de gm*ro, logrando altísimas ganancias."},
            {"q": "¿La realimentación negativa reduce la sensibilidad a las variaciones térmicas y tecnológicas de los componentes?", "a": "V", "j": "Verdadero. La ganancia en bucle cerrado queda fijada por la red pasiva de realimentación: Af = 1 / beta."},
            {"q": "¿El Slew Rate (SR) de un amplificador operacional define la máxima velocidad de variación temporal de la tensión de salida (dV/dt)?", "a": "V", "j": "Verdadero. Limitado por la corriente máxima de la etapa diferencial para cargar el condensador de compensación Cc."},
            {"q": "El rendimiento energético teórico máximo de una etapa amplificadora en Clase A con acoplo resistivo es del 78.5%.", "a": "F", "j": "Falso. El máximo en Clase A resistiva es solo del 25% (o 50% con transformador); el 78.5% corresponde a Clase B ideal."},
            {"q": "¿La resistencia de entrada de un amplificador MOSFET ideal en continua es prácticamente infinita debido al óxido de puerta?", "a": "V", "j": "Verdadero. Rin > 10^12 ohms gracias al dieléctrico aislante de SiO2/high-k."},
            {"q": "¿Un espejo de corriente proporciona una fuente de corriente de polarización constante con muy alta impedancia equivalente?", "a": "V", "j": "Verdadero. Copia la corriente de referencia en ramas secundarias de amplificación."}
        ]
    },

    # 230916: EMB (Sistemas Embebidos)
    "230916": {
        "code": "230916", "acronym": "EMB", "title": "Sistemas Embebidos", "semester": 4, "ects": 6.0,
        "department": "710 - EEL - Departamento de Ingeniería Electrónica",
        "description": "Arquitecturas de microcontroladores modernos (ARM Cortex-M), registros, periféricos hardware integrados (GPIO, Timers, PWM, ADC/DAC), sistemas de interrupciones vectorizadas y anidadas (NVIC), buses serie de comunicación síncronos y asíncronos (UART, SPI, I2C, CAN), control de acceso directo a memoria (DMA), gestión de bajo consumo y desarrollo de firmware bare-metal en C embebido.",
        "formulas": [
            {"name": "Periodo de Interrupción de Temporizador (Timer)", "latex": r"T_{\text{int}} = \frac{(\text{PSC} + 1) \cdot (\text{ARR} + 1)}{f_{\text{clk}}}"},
            {"name": "Baud Rate en Transmisión UART", "latex": r"\text{Baud} = \frac{f_{\text{clk}}}{16 \cdot \text{USARTDIV}}"},
            {"name": "Resolución de Convertidor ADC de N Bits", "latex": r"\Delta V = \frac{V_{\text{ref}}}{2^N}, \quad V_{\text{medido}} = \text{ADC\_VAL} \cdot \frac{V_{\text{ref}}}{2^N - 1}"},
            {"name": "Frecuencia de Bus SPI Síncrono", "latex": r"f_{\text{SCK}} = \frac{f_{\text{bus}}}{2^{\text{BR}[2:0] + 1}}"},
            {"name": "Ciclo de Trabajo (Duty Cycle) PWM", "latex": r"D = \frac{\text{CCR}}{\text{ARR}} \times 100\%"}
        ],
        "calc_params": {"f_clk_mhz": 80.0, "prescaler": 79, "arr_period": 999, "ccr_val": 250, "adc_bits": 12, "vref": 3.3, "raw_adc": 2048},
        "calc_outputs": ["timer_freq_hz", "pwm_duty_pct", "adc_voltage_v"],
        "calc_fn": "def calc(p):\n    fclk = p.get('f_clk_mhz', 80.0) * 1e6\n    psc = p.get('prescaler', 79)\n    arr = p.get('arr_period', 999)\n    f_timer = fclk / ((psc + 1.0) * (arr + 1.0))\n    ccr = p.get('ccr_val', 250)\n    duty = (ccr / float(arr)) * 100.0\n    nbits = p.get('adc_bits', 12)\n    vref = p.get('vref', 3.3)\n    raw = p.get('raw_adc', 2048)\n    vadc = raw * (vref / (2**nbits - 1.0))\n    return {'timer_freq_hz': round(f_timer, 2), 'pwm_duty_pct': round(duty, 2), 'adc_voltage_v': round(vadc, 4)}",
        "spice_template": "// EMB - Firmware de Interrupcion por Timer y Generacion PWM en C Embebido (ARM Cortex-M)\n#include <stdint.h>\n#define TIM2_ARR  (*(volatile uint32_t*)0x4000002C)\n#define TIM2_CCR1 (*(volatile uint32_t*)0x40000034)\nvoid TIM2_IRQHandler(void) {\n    // Rutina de Servicio de Interrupcion (ISR)\n    TIM2_CCR1 = (TIM2_CCR1 + 10) % TIM2_ARR;\n}\n",
        "questions": [
            {"q": "¿El controlador de interrupciones NVIC en arquitecturas ARM Cortex-M soporta anidamiento de interrupciones por niveles de prioridad?", "a": "V", "j": "Verdadero. Una interrupción de mayor prioridad desaloja a una de menor prioridad en ejecución."},
            {"q": "¿El protocolo de comunicación I2C requiere resistencias de pull-up externas en las líneas SDA y SCL porque sus salidas son de colector/drenador abierto?", "a": "V", "j": "Verdadero. Permite la conexión cableada en 'wired-AND' y evita colisiones por contención."},
            {"q": "El protocolo SPI requiere direccionamiento explícito por software de 7 bits para seleccionar cada esclavo.", "a": "F", "j": "Falso. SPI utiliza líneas físicas dedicadas de selección de chip (Chip Select / SS). El direccionamiento por 7 bits es de I2C."},
            {"q": "¿El controlador DMA permite transferir bloques de datos entre periféricos y la memoria RAM sin intervención de la CPU?", "a": "V", "j": "Verdadero. Libera a la CPU de bucles continuos de copia reduciendo consumo y latencia."},
            {"q": "¿Una variable compartida entre la rutina de interrupción (ISR) y el bucle principal de control debe declararse con el cualificador 'volatile'?", "a": "V", "j": "Verdadero. Evita que el compilador optimice o cachee su lectura en un registro interno de la CPU."},
            {"q": "La comunicación UART es un protocolo serie síncrono que transmite una línea de reloj compartida entre transmisor y receptor.", "a": "F", "j": "Falso. Es asíncrono (Universal Asynchronous Receiver-Transmitter); se sincroniza mediante bits de start y stop y un baud rate acordado."},
            {"q": "¿Un temporizador configurado con prescaler PSC divide la frecuencia del reloj maestro por el factor PSC + 1?", "a": "V", "j": "Verdadero. El contador de prescaler cuenta de 0 a PSC."},
            {"q": "¿El convertidor analógico-digital (ADC) de aproximaciones sucesivas (SAR) requiere N ciclos de reloj para una conversión de N bits?", "a": "V", "j": "Verdadero. Resuelve un bit por ciclo mediante un comparador y un DAC interno."},
            {"q": "En el protocolo I2C, la condición de parada (STOP) se genera con una transición de nivel alto a bajo en SDA mientras SCL está en alto.", "a": "F", "j": "Falso. La condición STOP es una transición de bajo a alto en SDA con SCL en alto (la de alto a bajo es la condición de START)."},
            {"q": "¿El temporizador Watchdog (WDT) restablece el microcontrolador si el software queda bloqueado y no refresca el contador periódicamente?", "a": "V", "j": "Verdadero. Mecanismo de seguridad crítico contra bloqueos de software."},
            {"q": "¿En los modos de suspensión de muy bajo consumo (Deep Sleep/Standby), se desactivan osciladores y reguladores no esenciales?", "a": "V", "j": "Verdadero. Permite operar dispositivos IoT a batería durante años."},
            {"q": "¿El bit de paridad en una trama UART permite detectar errores de bit único en la recepción de un carácter?", "a": "V", "j": "Verdadero. Verifica si el número total de unos coincide con la paridad par o impar configurada."}
        ]
    },

    # 230917: ICAF (Introducción a los Circuitos de Alta Frecuencia)
    "230917": {
        "code": "230917", "acronym": "ICAF", "title": "Introducción a los Circuitos de Alta Frecuencia", "semester": 4, "ects": 6.0,
        "department": "710 - EEL / 739 - TSC",
        "description": "Comportamiento de componentes pasivos en alta frecuencia (efectos parásitos en R, L, C y resonancia propia), matriz de parámetros de dispersión (Parámetros S de 2 puertos), adaptación de impedancias en RF mediante stubs simples y dobles y redes LC en L/Pi/T, líneas microstrip en sustratos dieléctricos (FR4, Rogers), y diseño preliminar de amplificadores de RF (ganancia del transductor, estabilidad con factor K de Rollett y círculos de ruido).",
        "formulas": [
            {"name": "Matriz de Parámetros S de 2 Puertos", "latex": r"\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}"},
            {"name": "Pérdidas de Retorno (Return Loss)", "latex": r"\text{RL} = -20 \log_{10}|S_{11}| \quad [\text{dB}]"},
            {"name": "Pérdidas de Inserción (Insertion Loss)", "latex": r"\text{IL} = -20 \log_{10}|S_{21}| \quad [\text{dB}]"},
            {"name": "Factor de Estabilidad de Rollett (K)", "latex": r"K = \frac{1 - |S_{11}|^2 - |S_{22}|^2 + |\Delta|^2}{2 |S_{12} S_{21}|}, \quad \Delta = S_{11} S_{22} - S_{12} S_{21}"},
            {"name": "Condición de Adaptación Conjugada Simultánea", "latex": r"\Gamma_{in}^* = \Gamma_S, \quad \Gamma_{out}^* = \Gamma_L \quad (\text{si } K > 1 \land |\Delta| < 1)"}
        ],
        "calc_params": {"s11_mag": 0.2, "s11_deg": 120.0, "s21_mag": 4.0, "s21_deg": 45.0, "s12_mag": 0.05, "s12_deg": 30.0, "s22_mag": 0.3, "s22_deg": -60.0},
        "calc_outputs": ["delta_mag", "rollett_k", "is_unconditionally_stable", "return_loss_db", "gain_s21_db"],
        "calc_fn": "def calc(p):\n    import math\n    s11 = p.get('s11_mag', 0.2)\n    s21 = p.get('s21_mag', 4.0)\n    s12 = p.get('s12_mag', 0.05)\n    s22 = p.get('s22_mag', 0.3)\n    delta = abs(s11 * s22 - s12 * s21)\n    k = (1.0 - s11**2 - s22**2 + delta**2) / max(1e-9, 2.0 * s12 * s21)\n    stable = bool(k > 1.0 and delta < 1.0)\n    rl = -20.0 * math.log10(max(1e-6, s11))\n    gain = 20.0 * math.log10(max(1e-6, s21))\n    return {'delta_mag': round(delta, 3), 'rollett_k': round(k, 3), 'is_unconditionally_stable': stable, 'return_loss_db': round(rl, 2), 'gain_s21_db': round(gain, 2)}",
        "spice_template": "* ICAF - Red de Adaptacion en L Pasobajo a 2.4 GHz\nVin in 0 AC 1.0 0\nRs in 1 50\nL1 1 out 4.5nH\nC1 out 0 1.8pF\nRL out 0 100\n.ac lin 100 2.0G 3.0G\n.print ac V(out) VP(out)\n.end\n",
        "questions": [
            {"q": "¿El parámetro S11 representa el coeficiente de reflexión visto desde el puerto 1 cuando el puerto 2 está terminado en una carga adaptada a Z0?", "a": "V", "j": "Verdadero. S11 = b1 / a1 con a2 = 0."},
            {"q": "¿El parámetro S21 cuantifica la ganancia o transmisión directa del puerto 1 al puerto 2?", "a": "V", "j": "Verdadero. |S21|^2 es la ganancia de potencia del transductor con puertos adaptados."},
            {"q": "¿Un transistor de RF es incondicionalmente estable si el factor de Rollett cumple K > 1 y |Delta| < 1 simultáneamente?", "a": "V", "j": "Verdadero. No oscilará para cualquier impedancia pasiva conectada a la entrada y salida."},
            {"q": "Una bobina real de RF se comporta como un inductor ideal a cualquier frecuencia por elevada que sea.", "a": "F", "j": "Falso. Por encima de su frecuencia de autorresonancia (SRF) la capacidad parásita entre espiras domina y se vuelve capacitiva."},
            {"q": "¿Un stub en cortocircuito de longitud eléctrica menor a un cuarto de onda (l < lambda/4) presenta una reactancia puramente inductiva?", "a": "V", "j": "Verdadero. Zin = j * Z0 * tan(beta * l) > 0."},
            {"q": "Un stub en circuito abierto de longitud lambda/4 se comporta como un circuito abierto en sus bornes.", "a": "F", "j": "Falso. Actúa como un cortocircuito perfecto (Zin = -j*Z0*cot(pi/2) = 0)."},
            {"q": "¿Las pérdidas de retorno (Return Loss) se definen como -20*log10(|S11|) y un valor alto indica una excelente adaptación?", "a": "V", "j": "Verdadero. Por ejemplo, RL > 20 dB significa que se refleja menos del 1% de la potencia incidente."},
            {"q": "¿En una línea microstrip sobre PCB, la velocidad de propagación depende de la permitividad dieléctrica efectiva del sustrato?", "a": "V", "j": "Verdadero. El campo viaja parcialmente en el dieléctrico y parcialmente en el aire exterior (modo cuasi-TEM)."},
            {"q": "¿La Carta de Smith permite diseñar redes de adaptación en L agregando reactancias serie o susceptancias paralelo como desplazamientos por círculos?", "a": "V", "j": "Verdadero. Método gráfico canónico de diseño de microondas."},
            {"q": "El parámetro S12 representa la reflexión interna del puerto 2 hacia sí mismo.", "a": "F", "j": "Falso. S12 es el aislamiento o transmisión inversa del puerto 2 hacia el puerto 1."},
            {"q": "¿Las pérdidas por inserción (Insertion Loss) representan la atenuación que sufre la señal al atravesar un cuadripolo?", "a": "V", "j": "Verdadero. IL = -20*log10(|S21|) dB."},
            {"q": "¿En RF se prefieren los parámetros S frente a parámetros Z o Y porque son fáciles de medir sin necesidad de cortocircuitos o circuitos abiertos ideales en alta frecuencia?", "a": "V", "j": "Verdadero. Se miden con terminaciones de referencia estándar (50 ohms) sin provocar oscilaciones no deseadas."}
        ]
    },

    # 230918: TRS (Tratamiento de la Señal)
    "230918": {
        "code": "230918", "acronym": "TRS", "title": "Tratamiento de la Señal", "semester": 4, "ects": 6.0,
        "department": "739 - TSC - Departamento de Teoría de la Señal y Comunicaciones",
        "description": "Filtrado digital (filtros FIR de fase lineal por enventanado y Remez-Parks-McClellan, filtros IIR por transformación bilineal Butterworth, Chebyshev y elípticos), procesamiento multirate (diezmado, interpolación, filtros polifase), cuantización y ruido de redondeo, estimación espectral paramétrica y no paramétrica (periodograma de Welch), y algoritmos adaptativos (LMS y RLS).",
        "formulas": [
            {"name": "Transformación Bilineal (Analógico a Digital)", "latex": r"s = \frac{2}{T_s} \frac{1 - z^{-1}}{1 + z^{-1}}, \quad \Omega = \frac{2}{T_s} \tan\left( \frac{\omega}{2} \right)"},
            {"name": "Relación de Fase Lineal en Filtro FIR Simétrico", "latex": r"\theta(\omega) = -\alpha \omega, \quad \tau_g = -\frac{d\theta}{d\omega} = \frac{N-1}{2}"},
            {"name": "Potencia de Ruido de Cuantización Uniforme", "latex": r"\sigma_q^2 = \frac{\Delta^2}{12}, \quad \Delta = \frac{V_{\text{FS}}}{2^B}"},
            {"name": "Relación Señal a Ruido de Cuantización (SQNR)", "latex": r"\text{SQNR} \approx 6.02 B + 1.76\,\text{dB}"},
            {"name": "Algoritmo LMS Adaptativo", "latex": r"\vec{w}[n+1] = \vec{w}[n] + 2 \mu e[n] \vec{x}[n], \quad e[n] = d[n] - \vec{w}^T[n] \vec{x}[n]"}
        ],
        "calc_params": {"bits": 16, "fs_hz": 48000.0, "order_fir": 64, "fc_hz": 4000.0},
        "calc_outputs": ["sqnr_db", "fir_group_delay_samples", "fir_delay_ms"],
        "calc_fn": "def calc(p):\n    b = p.get('bits', 16)\n    sqnr = 6.02 * b + 1.76\n    n = p.get('order_fir', 64)\n    gd = (n - 1) / 2.0\n    fs = max(1.0, p.get('fs_hz', 48000.0))\n    delay_ms = (gd / fs) * 1000.0\n    return {'sqnr_db': round(sqnr, 2), 'fir_group_delay_samples': round(gd, 1), 'fir_delay_ms': round(delay_ms, 3)}",
        "spice_template": "// TRS - Implementación en C de Filtro FIR Direct Form de Fase Lineal\n#define N_TAPS 5\nfloat fir_filter(float input, const float *coeffs, float *buffer) {\n    float acc = 0.0f;\n    for (int i = N_TAPS - 1; i > 0; i--) buffer[i] = buffer[i - 1];\n    buffer[0] = input;\n    for (int i = 0; i < N_TAPS; i++) acc += coeffs[i] * buffer[i];\n    return acc;\n}\n",
        "questions": [
            {"q": "¿Los filtros FIR son intrínsecamente estables porque todas sus funciones de transferencia presentan únicamente polos en el origen z = 0?", "a": "V", "j": "Verdadero. Tienen un número finito de coeficientes en su respuesta impulsional."},
            {"q": "¿Los filtros FIR con simetría par o impar garantizan una fase rigurosamente lineal y retardo de grupo constante?", "a": "V", "j": "Verdadero. Preservan la forma de onda de las señales complejas sin dispersión de fase."},
            {"q": "La transformación bilineal introduce una deformación o compresión de la escala de frecuencias (frequency warping) que exige un predistorsionado previo.", "a": "V", "j": "Verdadero. Omega = (2/Ts)*tan(omega/2); mapea todo el eje jOmega en la circunferencia unidad |z|=1."},
            {"q": "¿Cada bit adicional de resolución en un convertidor ADC cuantizado uniformemente incrementa la relación SQNR en aproximadamente 6.02 dB?", "a": "V", "j": "Verdadero. SQNR approx 6.02*B + 1.76 dB."},
            {"q": "Un filtro IIR requiere siempre mayor número de coeficientes y operaciones que un filtro FIR para satisfacer las mismas especificaciones de atenuación.", "a": "F", "j": "Falso. Los filtros IIR aprovechan polos y ceros, requiriendo un orden mucho menor que los FIR equivalentes."},
            {"q": "¿El diezmado por un factor M consiste en un filtrado antialiasing pasobajo previo seguido de la eliminación de M-1 de cada M muestras?", "a": "V", "j": "Verdadero. El prefiltrado evita el solapamiento espectral."},
            {"q": "¿La interpolación por un factor L inserta L-1 ceros entre muestras consecutivas seguida de un filtro pasobajo de anti-imagen?", "a": "V", "j": "Verdadero. Elimina las réplicas espectrales intermedias restaurando la señal en la nueva frecuencia de muestreo L*fs."},
            {"q": "El algoritmo LMS adaptativo minimiza el error cuadrático medio actualizando los pesos en la dirección del gradiente instantáneo.", "a": "V", "j": "Verdadero. w[n+1] = w[n] + 2*mu*e[n]*x[n]."},
            {"q": "¿El método del periodograma de Welch divide la señal en segmentos solapados enventanados y promedia sus periodogramas para reducir la varianza de la estimación espectral?", "a": "V", "j": "Verdadero. Reduce el ruido y la varianza espectral a costa de una pequeña merma en resolución frecuencial."},
            {"q": "Los filtros Butterworth se caracterizan por presentar un rizado equiripple en la banda de paso y de corte.", "a": "F", "j": "Falso. Los Butterworth son de máxima planicidad (maximally flat) sin ningún rizado. El rizado equiripple es característico de Chebyshev y Cauer/Elípticos."},
            {"q": "¿La estructura de filtrado polifase permite trasladar los filtros digitales a la frecuencia de muestreo más baja optimizando el número de operaciones por segundo?", "a": "V", "j": "Verdadero. Fundamento de los bancos de filtros eficientes en telecomunicaciones."},
            {"q": "¿El desbordamiento en aritmética de punto fijo en complementario a dos sin saturación puede originar ciclos límite de gran amplitud?", "a": "V", "j": "Verdadero. Las oscilaciones por wrap-around provocan inestabilidad si no se incluye lógica de saturación."}
        ]
    },

    # 230919: EP (Empresa y Proyectos)
    "230919": {
        "code": "230919", "acronym": "EP", "title": "Empresa y Proyectos", "semester": 4, "ects": 6.0,
        "department": "732 - OE - Organización de Empresas",
        "description": "Economía y organización de la empresa tecnológica, contabilidad analítica y financiera, análisis de inversiones (VAN, TIR, periodo de recuperación amortizado), gestión de proyectos de ingeniería (WBS, camino crítico CPM/PERT, diagramas de Gantt, gestión del valor ganado EVM), propiedad industrial e intelectual (patentes, licencias y marcas), y ciclo de vida de producto.",
        "formulas": [
            {"name": "Valor Actual Neto (VAN / NPV)", "latex": r"\text{VAN} = -I_0 + \sum_{t=1}^{n} \frac{CF_t}{(1 + k)^t}"},
            {"name": "Tasa Interna de Retorno (TIR / IRR)", "latex": r"\text{VAN}(\text{TIR}) = -I_0 + \sum_{t=1}^{n} \frac{CF_t}{(1 + \text{TIR})^t} = 0"},
            {"name": "Índice de Rendimiento del Coste (CPI en EVM)", "latex": r"\text{CPI} = \frac{\text{EV}}{\text{AC}} \quad (\text{CPI} > 1 \implies \text{Bajo presupuesto})"},
            {"name": "Índice de Rendimiento del Plazo (SPI en EVM)", "latex": r"\text{SPI} = \frac{\text{EV}}{\text{PV}} \quad (\text{SPI} > 1 \implies \text{Adelantado en plazo})"},
            {"name": "Umbral de Rentabilidad (Punto Muerto)", "latex": r"Q^* = \frac{\text{Costes Fijos}}{P - \text{Coste Variable Unitario}}"}
        ],
        "calc_params": {"inv_inicial": 100000.0, "flujo_anual": 35000.0, "anios": 4, "tasa_descuento": 0.08, "costes_fijos": 50000.0, "precio_unit": 120.0, "coste_var_unit": 70.0},
        "calc_outputs": ["van", "punto_muerto_unidades", "payback_anios", "is_viable"],
        "calc_fn": "def calc(p):\n    i0 = p.get('inv_inicial', 100000.0)\n    cf = p.get('flujo_anual', 35000.0)\n    n = int(p.get('anios', 4))\n    k = p.get('tasa_descuento', 0.08)\n    van = -i0 + sum(cf / ((1.0 + k)**t) for t in range(1, n + 1))\n    cfijos = p.get('costes_fijos', 50000.0)\n    margin = max(1.0, p.get('precio_unit', 120.0) - p.get('coste_var_unit', 70.0))\n    be = cfijos / margin\n    payback = i0 / max(1.0, cf)\n    return {'van': round(van, 2), 'punto_muerto_unidades': int(be), 'payback_anios': round(payback, 2), 'is_viable': bool(van > 0)}",
        "spice_template": "# EP - Modelo de Evaluación Financiera de Proyecto Tecnológico en Python\ndef evaluar_inversion(i0, flujos, k):\n    van = -i0 + sum(cf / ((1 + k)**(t+1)) for t, cf in enumerate(flujos))\n    return {'VAN': van, 'Aceptable': van > 0}\n",
        "questions": [
            {"q": "¿Un proyecto de ingeniería de inversión se considera económicamente viable según el criterio del VAN si su VAN > 0 a la tasa de descuento fijada?", "a": "V", "j": "Verdadero. Genera valor añadido neto por encima del coste de oportunidad del capital."},
            {"q": "¿La Tasa Interna de Retorno (TIR) es la tasa de actualización que hace exactamente cero el Valor Actual Neto (VAN = 0)?", "a": "V", "j": "Verdadero. Rentabilidad intrínseca del flujo de caja del proyecto."},
            {"q": "En la gestión de proyectos por el camino crítico (CPM), las actividades que forman parte del camino crítico tienen holgura total positiva y holgada.", "a": "F", "j": "Falso. Tienen holgura total nula (holgura = 0); cualquier retraso en ellas demora la fecha final de entrega del proyecto."},
            {"q": "¿En el método del Valor Ganado (EVM), un CPI > 1 indica que el proyecto está gastando menos presupuesto de lo previsto para el trabajo realizado?", "a": "V", "j": "Verdadero. CPI = EV / AC > 1 representa eficiencia de costes."},
            {"q": "¿El umbral de rentabilidad o punto muerto representa el volumen de ventas en el que los ingresos totales igualan a los costes totales (beneficio cero)?", "a": "V", "j": "Verdadero. A partir de esa cantidad la empresa empieza a obtener beneficios netos."},
            {"q": "Una patente de invención concede un derecho exclusivo de explotación industrial y comercial por tiempo ilimitado para siempre.", "a": "F", "j": "Falso. Concede un monopolio temporal limitado generalmente a 20 años desde la fecha de solicitud."},
            {"q": "¿La estructura de desglose del trabajo (WBS/EDT) organiza y descompone jerárquicamente el alcance completo del proyecto en paquetes de trabajo?", "a": "V", "j": "Verdadero. Base fundamental para planificar costes, recursos y plazos."},
            {"q": "¿El balance de situación refleja el patrimonio de la empresa en un instante temporal dividido en Activo, Pasivo y Patrimonio Neto?", "a": "V", "j": "Verdadero. Activo = Pasivo + Patrimonio Neto."},
            {"q": "¿En la gestión ágil Scrum, el Product Backlog priorizado es responsabilidad principal del Product Owner?", "a": "V", "j": "Verdadero. Define qué funcionalidades aportan mayor valor de negocio al cliente."},
            {"q": "El periodo de recuperación o payback simple tiene en cuenta el valor temporal del dinero a lo largo de los años futuros.", "a": "F", "j": "Falso. El payback simple no descuenta los flujos futuros; para tenerlo en cuenta debe emplearse el payback descontado."},
            {"q": "¿La matriz DAFO (SWOT) evalúa los factores internos (Debilidades, Fortalezas) y los factores externos (Amenazas, Oportunidades) de una organización?", "a": "V", "j": "Verdadero. Herramienta clásica de diagnóstico estratégico empresarial."},
            {"q": "¿El ciclo de vida de un producto tecnológico suele describirse en cuatro fases: introducción, crecimiento, madurez y declive?", "a": "V", "j": "Verdadero. Modelo clásico del ciclo de vida industrial."}
        ]
    }
}

with open("data/subjects_q3_q4.json", "w", encoding="utf-8") as f:
    json.dump(q3_q4_data, f, indent=2, ensure_ascii=False)

print(f"Generated Q3-Q4 catalog with {len(q3_q4_data)} subjects and {sum(len(s['questions']) for s in q3_q4_data.values())} questions.")
