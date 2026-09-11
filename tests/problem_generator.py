# -*- coding: utf-8 -*-
"""
Generador Paramétrico de Problemas Numéricos de Examen para Sistemes de Mesura (UPC)
Genera problemas con valores aleatorios dentro de rangos realistas y valida respuestas numéricas.
"""
import math
import random

def generate_wheatstone_problem():
    """Genera un problema de galgas en puente de Wheatstone con valores aleatorios."""
    R0 = random.choice([120.0, 350.0])
    K = round(random.uniform(2.00, 2.15), 2)
    Vs = round(random.uniform(5.0, 12.0), 1)
    eps_ue = random.randint(800, 2000)
    eps = eps_ue * 1e-6
    
    # Cálculos
    dR = R0 * K * eps
    # Montaje A (1/4 puente)
    x = dR / R0
    Vo_quarter = (Vs / 4.0) * (x / (1.0 + 0.5 * x))
    Vo_quarter_approx = (Vs / 4.0) * x
    error_nl_pct = abs(Vo_quarter - Vo_quarter_approx) / (Vo_quarter * 2) * 100
    
    # Montaje B (1/2 puente)
    Vo_half = (Vs / 2.0) * x
    
    return {
        "title": "Puente de Wheatstone con Galgas Extensométricas",
        "params": {
            "R0_ohm": R0,
            "K": K,
            "Vs_V": Vs,
            "eps_ue": eps_ue
        },
        "questions": [
            {
                "q": f"Para una deformación de {eps_ue} µε con galga R0={R0} Ω y K={K}, ¿cuánto vale la variación de resistencia ΔR (en ohmios)?",
                "answer": round(dR, 4),
                "unit": "Ω",
                "tolerance": 0.02
            },
            {
                "q": f"En montaje de cuarto de puente con Vs={Vs} V, ¿cuál es la tensión de salida Vo exacta (en mV)?",
                "answer": round(Vo_quarter * 1000, 3),
                "unit": "mV",
                "tolerance": 0.02
            },
            {
                "q": f"En montaje de medio puente push-pull, ¿cuál es la tensión de salida Vo (en mV)?",
                "answer": round(Vo_half * 1000, 3),
                "unit": "mV",
                "tolerance": 0.02
            }
        ],
        "solution_steps": [
            f"1. ΔR = R0 * K * ε = {R0} * {K} * ({eps_ue}e-6) = {dR:.4f} Ω",
            f"2. x = ΔR / R0 = {x:.6f}",
            f"3. Vo (1/4 puente) = (Vs/4) * [x / (1 + 0.5*x)] = {Vo_quarter*1000:.3f} mV",
            f"4. Vo (1/2 puente) = (Vs/2) * x = {Vo_half*1000:.3f} mV"
        ]
    }

def generate_ina_problem():
    """Genera un problema de Amplificador de Instrumentación (INA)."""
    R1 = random.choice([20.0, 25.0, 50.0]) * 1e3 # Ohm
    Vd_mV = random.choice([10.0, 20.0, 25.0, 40.0])
    Vo_target = 5.0 # V
    Gd = Vo_target / (Vd_mV * 1e-3)
    
    # Rg = 2*R1 / (Gd - 1)
    Rg = (2.0 * R1) / (Gd - 1.0)
    
    # CMRR con tolerancia
    tol = random.choice([0.01, 0.001])
    cmrr_ratio = Gd / (4.0 * tol)
    cmrr_db = 20.0 * math.log10(cmrr_ratio)
    
    Vcm = round(random.uniform(2.0, 5.0), 1)
    Vo_cm_mV = (Gd / cmrr_ratio) * Vcm * 1000 # mV
    
    return {
        "title": "Amplificador de Instrumentación (INA) y CMRR",
        "params": {
            "R1_kohm": R1 / 1e3,
            "Vd_mV": Vd_mV,
            "Vo_target_V": Vo_target,
            "tol_pct": tol * 100,
            "Vcm_V": Vcm
        },
        "questions": [
            {
                "q": f"Para amplificar Vd = {Vd_mV} mV a Vo = {Vo_target} V con R1 = {R1/1e3} kΩ, ¿cuál debe ser el valor de Rg (en ohmios)?",
                "answer": round(Rg, 2),
                "unit": "Ω",
                "tolerance": 0.02
            },
            {
                "q": f"Si las resistencias del segundo bloque tienen tolerancia del {tol*100}%, ¿cuál es el CMRR total (en dB)?",
                "answer": round(cmrr_db, 2),
                "unit": "dB",
                "tolerance": 0.03
            },
            {
                "q": f"Con una tensión de modo común parásita Vcm = {Vcm} V, ¿cuál es la tensión de error Vo,cm en la salida (en mV)?",
                "answer": round(Vo_cm_mV, 2),
                "unit": "mV",
                "tolerance": 0.03
            }
        ],
        "solution_steps": [
            f"1. Ganancia diferencial necesaria: Gd = Vo / Vd = {Vo_target} / {Vd_mV*1e-3} = {Gd:.1f}",
            f"2. Rg = 2*R1 / (Gd - 1) = (2 * {R1:.0f}) / ({Gd:.1f} - 1) = {Rg:.2f} Ω",
            f"3. CMRR = Gd / (4 * δ) = {Gd:.1f} / (4 * {tol}) = {cmrr_ratio:.1f} ({cmrr_db:.2f} dB)",
            f"4. Vo,cm = (Gd / CMRR) * Vcm = {Vo_cm_mV:.2f} mV"
        ]
    }

def generate_rtd_problem():
    """Genera un problema de Pt100 y efecto de cables."""
    RL = round(random.uniform(1.5, 4.0), 1)
    T = random.choice([40.0, 50.0, 75.0, 100.0])
    R0 = 100.0
    alpha = 0.00385
    
    R_real = R0 * (1.0 + alpha * T)
    # Error en 2 hilos
    R_aparente = R_real + 2.0 * RL
    T_aparente = (R_aparente - R0) / (R0 * alpha)
    T_error = (2.0 * RL) / (R0 * alpha)
    
    return {
        "title": "Termorresistencia Pt100 y Efecto de Cables",
        "params": {
            "RL_ohm": RL,
            "T_celsius": T
        },
        "questions": [
            {
                "q": f"A T = {T} °C, ¿cuál es la resistencia real de la Pt100 (en ohmios)?",
                "answer": round(R_real, 3),
                "unit": "Ω",
                "tolerance": 0.01
            },
            {
                "q": f"En conexión a 2 hilos con RL = {RL} Ω por hilo, ¿cuál es el error de temperatura inducido en grados Celsius?",
                "answer": round(T_error, 2),
                "unit": "°C",
                "tolerance": 0.02
            }
        ],
        "solution_steps": [
            f"1. R(T) = R0 * (1 + α*T) = 100 * (1 + 0.00385 * {T}) = {R_real:.3f} Ω",
            f"2. Sensibilidad Pt100: S = R0 * α = 0.385 Ω/°C",
            f"3. R_aparente (2 hilos) = R(T) + 2*RL = {R_real:.3f} + {2*RL} = {R_aparente:.3f} Ω",
            f"4. Error de temperatura: ΔT = 2*RL / (R0*α) = {2*RL} / 0.385 = {T_error:.2f} °C"
        ]
    }

def generate_adc_problem():
    """Genera un problema de ADC y cuantificación."""
    N = random.choice([10, 12, 14, 16])
    FSR = random.choice([3.3, 4.096, 5.0, 10.0])
    q_uV = (FSR / (2**N)) * 1e6
    vq_rms_uV = q_uV / math.sqrt(12)
    snr_ideal = 6.02 * N + 1.76
    
    return {
        "title": "Conversor Analógico-Digital (ADC) y Ruido de Cuantificación",
        "params": {
            "N_bits": N,
            "FSR_V": FSR
        },
        "questions": [
            {
                "q": f"Para un ADC de {N} bits con FSR = {FSR} V, ¿cuánto vale el escalón de cuantificación q (LSB) en µV?",
                "answer": round(q_uV, 2),
                "unit": "µV",
                "tolerance": 0.02
            },
            {
                "q": f"¿Cuál es el valor eficaz del ruido de cuantificación ideal vq,rms (en µV)?",
                "answer": round(vq_rms_uV, 2),
                "unit": "µV",
                "tolerance": 0.02
            },
            {
                "q": f"¿Cuál es la relación señal-ruido ideal (SNR_ideal) en dB?",
                "answer": round(snr_ideal, 2),
                "unit": "dB",
                "tolerance": 0.02
            }
        ],
        "solution_steps": [
            f"1. q = FSR / 2^N = {FSR} / {2**N} = {q_uV:.2f} µV",
            f"2. vq,rms = q / sqrt(12) = {q_uV:.2f} / 3.4641 = {vq_rms_uV:.2f} µV",
            f"3. SNR_ideal = 6.02 * N + 1.76 = 6.02 * {N} + 1.76 = {snr_ideal:.2f} dB"
        ]
    }

def check_answer(user_val: float, expected_val: float, tolerance: float = 0.02) -> bool:
    """Verifica si la respuesta del usuario está dentro del margen de tolerancia."""
    if expected_val == 0:
        return abs(user_val) < 1e-4
    rel_diff = abs(user_val - expected_val) / abs(expected_val)
    return rel_diff <= tolerance

if __name__ == "__main__":
    print("--- Probando generador de problemas parametricos ---")
    p1 = generate_wheatstone_problem()
    print(f"[OK] {p1['title']}: {len(p1['questions'])} preguntas generadas")
    p2 = generate_ina_problem()
    print(f"[OK] {p2['title']}: {len(p2['questions'])} preguntas generadas")
    p3 = generate_rtd_problem()
    print(f"[OK] {p3['title']}: {len(p3['questions'])} preguntas generadas")
    p4 = generate_adc_problem()
    print(f"[OK] {p4['title']}: {len(p4['questions'])} preguntas generadas")
    print("Generador parametrico funcionando correctamente.")
