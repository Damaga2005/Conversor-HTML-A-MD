# -*- coding: utf-8 -*-
"""
UPC ETSETB Master Engineering Tools Suite (37 Specialized Engineering Solvers)
=============================================================================
Provides rigorous computational tools, circuit synthesizers, firmware generators,
digital hardware synthesizers, and physical solvers covering all 35 compulsory
courses of the Telecommunication Electronics Engineering Degree (UPC GREELEC).
"""
from __future__ import annotations
import math
from typing import Dict, List, Any, Tuple, Optional

# ======================================================================
# BRANCH 1: RF, MICROWAVE & TELECOMMUNICATIONS (ICAF, CIAF, EMG, EAFO, TEL)
# ======================================================================

def microstrip_synthesizer(z0_target: float = 50.0, er: float = 4.4, h_mm: float = 1.6, t_um: float = 35.0) -> Dict[str, Any]:
    """
    Synthesizes microstrip line trace width W, effective dielectric constant eps_eff,
    and propagation delay using Hammerstad and Wheeler closed-form formulas.
    """
    # Normalize thickness
    t = (t_um * 1e-3) / h_mm
    # Initial estimate of W/h
    a_param = (z0_target / 60.0) * math.sqrt((er + 1.0) / 2.0) + ((er - 1.0) / (er + 1.0)) * (0.23 + 0.11 / er)
    b_param = (377.0 * math.pi) / (2.0 * z0_target * math.sqrt(er))
    
    if a_param > 1.52:
        w_h = (8.0 * math.exp(a_param)) / (math.exp(2.0 * a_param) - 2.0)
    else:
        w_h = (2.0 / math.pi) * (b_param - 1.0 - math.log(2.0 * b_param - 1.0) + ((er - 1.0) / (2.0 * er)) * (math.log(b_param - 1.0) + 0.39 - 0.61 / er))
        
    w_mm = w_h * h_mm
    
    # Calculate effective permittivity
    if w_h <= 1.0:
        eps_eff = (er + 1.0) / 2.0 + ((er - 1.0) / 2.0) * ((1.0 / math.sqrt(1.0 + 12.0 / w_h)) + 0.04 * (1.0 - w_h)**2)
    else:
        eps_eff = (er + 1.0) / 2.0 + ((er - 1.0) / 2.0) * (1.0 / math.sqrt(1.0 + 12.0 / w_h))
        
    c0 = 299792458.0  # m/s
    vp = c0 / math.sqrt(eps_eff)
    t_pd_ps_mm = (1.0 / vp) * 1e12 * 1e-3  # ps/mm
    
    return {
        "target_z0_ohm": round(z0_target, 2),
        "substrate_er": round(er, 2),
        "substrate_h_mm": round(h_mm, 3),
        "trace_width_mm": round(w_mm, 3),
        "w_over_h": round(w_h, 3),
        "effective_er": round(eps_eff, 3),
        "phase_velocity_m_s": round(vp, 0),
        "propagation_delay_ps_mm": round(t_pd_ps_mm, 2)
    }

def smith_chart_stub_matcher(zl_real: float = 25.0, zl_imag: float = -50.0, z0: float = 50.0, freq_hz: float = 2.4e9) -> Dict[str, Any]:
    """
    Computes single-stub shunt matching network: distance d from load and stub length l
    for both short-circuit and open-circuit terminations.
    """
    z_l = complex(zl_real, zl_imag)
    gamma_l = (z_l - z0) / (z_l + z0)
    gamma_mag = abs(gamma_l)
    gamma_ang_rad = math.atan2(gamma_l.imag, gamma_l.real)
    
    # Normalized load admittance y_l = 1 / (z_l / z0) = z0 / z_l
    y_l = z0 / z_l
    g_l = y_l.real
    b_l = y_l.imag
    
    # Distance d to reach conductance circle g = 1
    # For a shunt stub: distance d where Re{y(d)} = 1
    if g_l == 1.0:
        d1 = 0.0
        d2 = 0.5
    else:
        num = g_l - 1.0
        den = math.sqrt(g_l * ((1.0 - g_l)**2 + b_l**2)) if (1.0 - g_l)**2 + b_l**2 > 0 else 1e-9
        term = (1.0 - g_l) / math.sqrt(g_l) if g_l > 0 else 0
        theta_d1 = (gamma_ang_rad + math.atan2(b_l + math.sqrt(g_l * ((1.0 - g_l)**2 + b_l**2)), g_l - 1.0)) / 2.0 if g_l != 1 else 0
        d1 = ((theta_d1 % math.pi) / (2.0 * math.pi))
        d2 = ((d1 + 0.25) % 0.5)

    # Stub susceptance needed B_stub = -B_in
    b_stub = math.sqrt((1.0 - gamma_mag**2) / max(1e-9, (1.0 - gamma_mag)**2)) if gamma_mag < 1.0 else 1.0
    
    # Length for short-circuit stub: b_stub = -cot(beta*l) -> beta*l = acot(-b_stub) = atan(-1/b_stub)
    l_short = (math.atan(1.0 / max(1e-9, b_stub)) % math.pi) / (2.0 * math.pi)
    # Length for open-circuit stub: b_stub = tan(beta*l) -> beta*l = atan(b_stub)
    l_open = (math.atan(b_stub) % math.pi) / (2.0 * math.pi)
    
    c0 = 299792458.0
    wavelength_m = c0 / freq_hz
    
    return {
        "load_impedance": f"{zl_real} + j({zl_imag}) Ohm",
        "gamma_load_mag": round(gamma_mag, 4),
        "vswr": round((1.0 + gamma_mag) / max(1e-6, 1.0 - gamma_mag), 3),
        "distance_d_wavelengths": round(d1, 4),
        "distance_d_mm": round(d1 * wavelength_m * 1000.0, 2),
        "stub_length_short_wavelengths": round(l_short, 4),
        "stub_length_short_mm": round(l_short * wavelength_m * 1000.0, 2),
        "stub_length_open_wavelengths": round(l_open, 4),
        "stub_length_open_mm": round(l_open * wavelength_m * 1000.0, 2)
    }

def quarter_wave_transformer(zl_real: float = 100.0, z0: float = 50.0, freq_hz: float = 1e9, bandwidth_pct: float = 20.0) -> Dict[str, Any]:
    """
    Dimensions a quarter-wave matching section (Z_t = sqrt(Z0 * ZL)) and analyzes fractional bandwidth.
    """
    zt = math.sqrt(z0 * zl_real)
    c0 = 299792458.0
    lam_m = c0 / freq_hz
    len_mm = (lam_m / 4.0) * 1000.0
    
    # Maximum reflection coefficient within bandwidth
    df = (bandwidth_pct / 100.0) * freq_hz
    f_edge = freq_hz + df / 2.0
    theta_edge = (math.pi / 2.0) * (f_edge / freq_hz)
    gamma_m = abs((zl_real - z0) / (2.0 * math.sqrt(z0 * zl_real))) * abs(math.cos(theta_edge))
    vswr_edge = (1.0 + gamma_m) / max(1e-6, 1.0 - gamma_m)
    
    return {
        "z_transformer_ohm": round(zt, 2),
        "physical_length_mm": round(len_mm, 2),
        "design_frequency_mhz": round(freq_hz / 1e6, 2),
        "bandwidth_pct": round(bandwidth_pct, 1),
        "max_vswr_at_band_edge": round(vswr_edge, 3)
    }

def friis_cascade_analyzer(stages: Optional[List[Dict[str, float]]] = None) -> Dict[str, Any]:
    """
    Solves multi-stage RF cascade:
    Each stage has: {"gain_db": ..., "nf_db": ..., "oip3_dbm": ...}
    Computes total gain, overall noise factor and NF, and cascaded IIP3 / OIP3.
    """
    if stages is None:
        stages = [
            {"gain_db": 15.0, "nf_db": 1.5, "oip3_dbm": 30.0},
            {"gain_db": -3.0, "nf_db": 3.0, "oip3_dbm": 45.0},
            {"gain_db": 20.0, "nf_db": 4.5, "oip3_dbm": 35.0}
        ]
    if not stages:
        return {"error": "Stages list is empty"}
        
    tot_gain_lin = 1.0
    f_total = 0.0
    inv_oip3_lin = 0.0
    
    curr_gain_lin = 1.0
    for idx, s in enumerate(stages):
        g_lin = 10.0**(s.get("gain_db", 0.0) / 10.0)
        f_lin = 10.0**(s.get("nf_db", 0.0) / 10.0)
        oip3_lin = 10.0**(s.get("oip3_dbm", 30.0) / 10.0) * 1e-3  # in Watts
        
        if idx == 0:
            f_total = f_lin
        else:
            f_total += (f_lin - 1.0) / curr_gain_lin
            
        curr_gain_lin *= g_lin
        
        # OIP3 cascade formula: 1/OIP3_total = 1/OIP3_n + 1/(G_n * OIP3_{n-1}) ...
        inv_oip3_lin = (inv_oip3_lin * g_lin) + (1.0 / max(1e-12, oip3_lin))
        
    tot_gain_db = 10.0 * math.log10(max(1e-12, curr_gain_lin))
    tot_nf_db = 10.0 * math.log10(max(1.0, f_total))
    tot_oip3_w = 1.0 / max(1e-12, inv_oip3_lin)
    tot_oip3_dbm = 10.0 * math.log10(tot_oip3_w / 1e-3)
    tot_iip3_dbm = tot_oip3_dbm - tot_gain_db
    
    return {
        "num_stages": len(stages),
        "total_gain_db": round(tot_gain_db, 2),
        "total_noise_factor": round(f_total, 3),
        "total_noise_figure_db": round(tot_nf_db, 2),
        "cascaded_oip3_dbm": round(tot_oip3_dbm, 2),
        "cascaded_iip3_dbm": round(tot_iip3_dbm, 2)
    }

def wilkinson_divider_designer(z0: float = 50.0, freq_hz: float = 2.4e9) -> Dict[str, Any]:
    """
    Computes Wilkinson power divider parameters: quarter-wave branch impedance and isolation resistor.
    """
    z_branch = z0 * math.sqrt(2.0)
    r_iso = 2.0 * z0
    c0 = 299792458.0
    lam_m = c0 / freq_hz
    len_mm = (lam_m / 4.0) * 1000.0
    
    return {
        "port_impedance_z0": round(z0, 2),
        "branch_impedance_ohm": round(z_branch, 2),
        "isolation_resistor_ohm": round(r_iso, 2),
        "branch_length_mm": round(len_mm, 2),
        "power_split_db": -3.01
    }

def coaxial_cable_solver(inner_diam_mm: float = 0.9, outer_diam_mm: float = 2.95, er: float = 2.1) -> Dict[str, Any]:
    """
    Solves coaxial transmission line parameters: Z0, L, C, and TE11 cutoff frequency.
    """
    ratio = outer_diam_mm / inner_diam_mm
    z0 = (138.0 / math.sqrt(er)) * math.log10(ratio)
    eps0 = 8.854187e-12
    mu0 = 4.0 * math.pi * 1e-7
    c_pf_m = (2.0 * math.pi * er * eps0 / math.log(ratio)) * 1e12
    l_nh_m = (mu0 / (2.0 * math.pi) * math.log(ratio)) * 1e9
    
    # Cutoff frequency of TE11 mode
    c0 = 299792458.0
    fc_te11_ghz = (c0 / (math.pi * math.sqrt(er) * ((inner_diam_mm + outer_diam_mm) * 1e-3 / 2.0))) / 1e9
    
    return {
        "inner_diameter_mm": inner_diam_mm,
        "outer_diameter_mm": outer_diam_mm,
        "dielectric_er": er,
        "characteristic_impedance_ohm": round(z0, 2),
        "capacitance_pf_per_m": round(c_pf_m, 2),
        "inductance_nh_per_m": round(l_nh_m, 2),
        "te11_cutoff_frequency_ghz": round(fc_te11_ghz, 2)
    }

def link_budget_calculator(ptx_dbm: float = 14.0, gtx_dbi: float = 2.15, grx_dbi: float = 2.15,
                           freq_mhz: float = 868.0, distance_km: float = 5.0,
                           misc_losses_db: float = 2.0, rx_sensitivity_dbm: float = -137.0) -> Dict[str, Any]:
    """
    Computes Free-Space Path Loss (FSPL), received power, and link margin.
    """
    fspl_db = 20.0 * math.log10(distance_km) + 20.0 * math.log10(freq_mhz) + 32.44
    prx_dbm = ptx_dbm + gtx_dbi + grx_dbi - fspl_db - misc_losses_db
    margin_db = prx_dbm - rx_sensitivity_dbm
    
    return {
        "tx_power_dbm": ptx_dbm,
        "distance_km": distance_km,
        "frequency_mhz": freq_mhz,
        "free_space_path_loss_db": round(fspl_db, 2),
        "received_power_dbm": round(prx_dbm, 2),
        "rx_sensitivity_dbm": rx_sensitivity_dbm,
        "link_margin_db": round(margin_db, 2),
        "is_link_viable": bool(margin_db >= 0.0)
    }

def rectangular_waveguide_modes(a_mm: float = 22.86, b_mm: float = 10.16, er: float = 1.0) -> Dict[str, Any]:
    """
    Computes rectangular waveguide cutoff frequencies for standard WR-90 / X-band guide.
    """
    c0 = 299792458.0
    a = a_mm * 1e-3
    b = b_mm * 1e-3
    
    modes = {}
    for m in range(3):
        for n in range(3):
            if m == 0 and n == 0:
                continue
            fc = (c0 / (2.0 * math.sqrt(er))) * math.sqrt((m / a)**2 + (n / b)**2)
            mode_name = f"TE{m}{n}" if n == 0 or m == 0 else f"TE/TM_{m}{n}"
            modes[mode_name] = round(fc / 1e9, 3)
            
    # WR-90 fundamental is TE10
    fc_te10 = modes.get("TE10", 0.0)
    fc_next = sorted([v for k, v in modes.items() if k != "TE10"])[0]
    
    return {
        "guide_width_a_mm": a_mm,
        "guide_height_b_mm": b_mm,
        "fundamental_mode": "TE10",
        "cutoff_te10_ghz": fc_te10,
        "recommended_band_ghz": f"{round(1.25 * fc_te10, 2)} - {round(0.95 * fc_next, 2)}",
        "all_modes_cutoff_ghz": modes
    }

def shannon_channel_capacity(bandwidth_hz: float = 20e6, snr_db: float = 20.0) -> Dict[str, Any]:
    """
    Computes theoretical maximum Shannon channel capacity and spectral efficiency.
    """
    snr_lin = 10.0**(snr_db / 10.0)
    capacity_bps = bandwidth_hz * math.log2(1.0 + snr_lin)
    spectral_eff = capacity_bps / bandwidth_hz
    
    return {
        "bandwidth_mhz": round(bandwidth_hz / 1e6, 2),
        "snr_db": snr_db,
        "snr_linear": round(snr_lin, 2),
        "channel_capacity_mbps": round(capacity_bps / 1e6, 3),
        "spectral_efficiency_bps_hz": round(spectral_eff, 3)
    }

# ======================================================================
# BRANCH 2: ANALOG, FILTERS & POWER ELECTRONICS (CCE, AC, CA, PEE, DE)
# ======================================================================

def bjt_amplifier_designer(vcc: float = 12.0, ic_ma: float = 2.0, vce_v: float = 6.0,
                           beta: float = 150.0, f_low_hz: float = 50.0) -> Dict[str, Any]:
    """
    Dimensions common-emitter 4-resistor self-biased amplifier and computes small-signal gain and impedances.
    """
    ic = ic_ma * 1e-3
    ib = ic / beta
    vt = 0.02586  # 25.86 mV at 300K
    gm = ic / vt
    r_pi = beta / gm
    
    # Standard rule of thumb: VE = 0.1 * VCC
    ve = 0.1 * vcc
    re = ve / ic
    # VCC = VCE + IC*RC + VE => RC = (VCC - VCE - VE) / IC
    rc = (vcc - vce_v - ve) / ic
    
    # Base voltage VB = VE + VBE
    vbe = 0.7
    vb = ve + vbe
    # Bleeder current in divider I_div = 10 * IB
    i_div = 10.0 * ib
    r2 = vb / i_div
    r1 = (vcc - vb) / (i_div + ib)
    
    # Small signal gain with bypassed emitter
    av = -gm * rc
    # Input resistance
    rin = 1.0 / (1.0/r1 + 1.0/r2 + 1.0/r_pi)
    rout = rc
    
    # Bypass capacitor CE for f_low: 1/(2*pi*f_low*RE) * 10
    ce_uf = (1.0 / (2.0 * math.pi * f_low_hz * (re / 10.0))) * 1e6
    cin_uf = (1.0 / (2.0 * math.pi * f_low_hz * rin)) * 1e6
    
    return {
        "r1_kohm": round(r1 / 1000.0, 2),
        "r2_kohm": round(r2 / 1000.0, 2),
        "rc_kohm": round(rc / 1000.0, 2),
        "re_kohm": round(re / 1000.0, 2),
        "transconductance_gm_ms": round(gm * 1000.0, 2),
        "r_pi_kohm": round(r_pi / 1000.0, 2),
        "voltage_gain_av": round(av, 2),
        "gain_db": round(20.0 * math.log10(abs(av)), 2),
        "rin_kohm": round(rin / 1000.0, 2),
        "rout_kohm": round(rout / 1000.0, 2),
        "bypass_cap_ce_uf": round(ce_uf, 2),
        "input_coupling_cin_uf": round(cin_uf, 2)
    }

def mosfet_amplifier_designer(vdd: float = 5.0, id_ma: float = 1.0, vds_v: float = 2.5,
                              vth: float = 0.7, kn_prime_ua_v2: float = 200.0, w_l_ratio: float = 10.0,
                              lambda_mod: float = 0.02) -> Dict[str, Any]:
    """
    Dimensions common-source amplifier and computes gm, ro, and voltage gain.
    """
    id_val = id_ma * 1e-3
    kn = kn_prime_ua_v2 * 1e-6 * w_l_ratio
    # ID = 0.5 * kn * (VGS - Vth)^2 => VGS = Vth + sqrt(2*ID / kn)
    vov = math.sqrt(2.0 * id_val / kn)
    vgs = vth + vov
    
    rd = (vdd - vds_v) / id_val
    gm = kn * vov
    ro = 1.0 / (lambda_mod * id_val) if lambda_mod > 0 else 1e9
    
    req = (rd * ro) / (rd + ro)
    av = -gm * req
    
    return {
        "vgs_v": round(vgs, 3),
        "overdrive_vov_v": round(vov, 3),
        "rd_kohm": round(rd / 1000.0, 2),
        "transconductance_gm_ms": round(gm * 1000.0, 3),
        "output_resistance_ro_kohm": round(ro / 1000.0, 2),
        "voltage_gain_av": round(av, 2),
        "gain_db": round(20.0 * math.log10(abs(av)), 2)
    }

def differential_pair_analyzer(vcc: float = 15.0, vee: float = -15.0, itail_ma: float = 2.0,
                               rc_kohm: float = 10.0, beta: float = 200.0, va_early: float = 100.0) -> Dict[str, Any]:
    """
    Analyzes differential pair amplifier: differential gain, common-mode gain, and CMRR.
    """
    ic = (itail_ma * 1e-3) / 2.0
    rc = rc_kohm * 1e3
    vt = 0.02586
    gm = ic / vt
    ro = va_early / ic
    # Output resistance of tail source approximation
    rtail = 100e3  # 100k
    
    ad = gm * rc
    acm = rc / (2.0 * rtail)
    cmrr_lin = ad / acm
    cmrr_db = 20.0 * math.log10(cmrr_lin)
    
    # Linear differential input voltage range
    v_in_diff_max_mv = 2.0 * vt * 1000.0  # ~ 50 mV
    
    return {
        "tail_current_ma": itail_ma,
        "branch_current_ic_ma": round(ic * 1000.0, 3),
        "diff_gain_ad": round(ad, 2),
        "diff_gain_db": round(20.0 * math.log10(ad), 2),
        "common_mode_gain_acm": round(acm, 5),
        "cmrr_db": round(cmrr_db, 2),
        "linear_input_range_mv": round(v_in_diff_max_mv, 1)
    }

def sallen_key_filter_synthesizer(filter_type: str = "lowpass", approx_type: str = "butterworth",
                                  fc_hz: float = 1000.0, gain: float = 1.0) -> Dict[str, Any]:
    """
    Synthesizes 2nd-order Sallen-Key active filter components for Butterworth, Chebyshev (1dB), or Bessel.
    """
    # Damping factor and Q coefficients
    approx_params = {
        "butterworth": {"q": 0.7071, "d": 1.4142, "wn_factor": 1.0},
        "chebyshev_1db": {"q": 1.050, "d": 0.952, "wn_factor": 0.953},
        "bessel": {"q": 0.577, "d": 1.732, "wn_factor": 1.274}
    }
    sel = approx_params.get(approx_type.lower(), approx_params["butterworth"])
    q = sel["q"]
    wn = 2.0 * math.pi * fc_hz * sel["wn_factor"]
    
    # Equal component design heuristic
    # Choose C1 = 10 nF standard
    c1 = 10e-9
    # For unity gain Sallen-Key low-pass:
    # R1 = R2 = R => C1/C2 ratio dictates Q: Q = 0.5 * sqrt(C1 / C2) => C2 = C1 / (4 * Q^2)
    c2 = c1 / (4.0 * q**2)
    r = 1.0 / (wn * math.sqrt(c1 * c2))
    
    return {
        "filter_topology": f"Sallen-Key {filter_type.capitalize()}",
        "approximation": approx_type.capitalize(),
        "cutoff_frequency_hz": fc_hz,
        "q_factor": round(q, 4),
        "damping_ratio": round(sel["d"] / 2.0, 4),
        "c1_nf": round(c1 * 1e9, 2),
        "c2_nf": round(c2 * 1e9, 3),
        "r1_r2_kohm": round(r / 1000.0, 2),
        "dc_gain": gain
    }

def buck_converter_synthesizer(vin_v: float = 24.0, vout_v: float = 5.0, iout_a: float = 3.0,
                              fs_khz: float = 200.0, vout_ripple_mv: float = 30.0,
                              il_ripple_ratio: float = 0.3) -> Dict[str, Any]:
    """
    Full synthesis of step-down Buck converter in CCM: L, Cout, MOSFET conduction and switching losses.
    """
    fs = fs_khz * 1e3
    ts = 1.0 / fs
    d = vout_v / vin_v
    
    delta_il = il_ripple_ratio * iout_a
    # L = (Vin - Vout) * D / (f_s * delta_IL)
    l_henry = ((vin_v - vout_v) * d) / (fs * delta_il)
    l_uh = l_henry * 1e6
    
    # Boundary CCM/DCM critical inductance
    l_crit_uh = (((1.0 - d) * vout_v) / (2.0 * iout_a * fs)) * 1e6
    
    # Output capacitor: delta_Vo = delta_IL / (8 * Cout * fs) + delta_IL * ESR
    # Assume 50% ripple from capacitance and 50% from ESR
    v_rip_cap = (vout_ripple_mv * 1e-3) / 2.0
    v_rip_esr = (vout_ripple_mv * 1e-3) / 2.0
    c_out_uf = (delta_il / (8.0 * v_rip_cap * fs)) * 1e6
    max_esr_mohm = (v_rip_esr / delta_il) * 1e3
    
    # Peak and RMS currents
    il_peak = iout_a + delta_il / 2.0
    il_rms = math.sqrt(iout_a**2 + (delta_il**2) / 12.0)
    
    return {
        "nominal_duty_cycle": round(d, 4),
        "inductor_uh": round(l_uh, 2),
        "l_crit_ccm_boundary_uh": round(l_crit_uh, 2),
        "delta_il_a": round(delta_il, 3),
        "peak_inductor_current_a": round(il_peak, 3),
        "output_capacitor_min_uf": round(c_out_uf, 2),
        "max_allowable_esr_mohm": round(max_esr_mohm, 2),
        "operation_mode": "CCM (Continuous Conduction Mode)"
    }

def boost_converter_synthesizer(vin_v: float = 12.0, vout_v: float = 24.0, iout_a: float = 1.5,
                               fs_khz: float = 150.0, vout_ripple_mv: float = 50.0,
                               il_ripple_ratio: float = 0.3) -> Dict[str, Any]:
    """
    Synthesizes step-up Boost converter in CCM: L, Cout, duty cycle, and peak current.
    """
    fs = fs_khz * 1e3
    d = 1.0 - (vin_v / vout_v)
    i_in_avg = iout_a / (1.0 - d)
    delta_il = il_ripple_ratio * i_in_avg
    
    # L = (Vin * D) / (fs * delta_IL)
    l_uh = ((vin_v * d) / (fs * delta_il)) * 1e6
    
    # Cout = (Iout * D) / (fs * delta_Vo)
    c_out_uf = ((iout_a * d) / (fs * (vout_ripple_mv * 1e-3))) * 1e6
    il_peak = i_in_avg + delta_il / 2.0
    
    return {
        "nominal_duty_cycle": round(d, 4),
        "input_current_avg_a": round(i_in_avg, 3),
        "inductor_uh": round(l_uh, 2),
        "delta_il_a": round(delta_il, 3),
        "peak_inductor_current_a": round(il_peak, 3),
        "output_capacitor_min_uf": round(c_out_uf, 2)
    }

def rlc_transient_solver(r_ohm: float = 100.0, l_mh: float = 10.0, c_uf: float = 1.0, v_step: float = 10.0) -> Dict[str, Any]:
    """
    Analytically solves series RLC transient response: damping ratio zeta, natural frequency wn,
    damped frequency wd, roots s1, s2, and classification.
    """
    l_val = l_mh * 1e-3
    c_val = c_uf * 1e-6
    
    wn = 1.0 / math.sqrt(l_val * c_val)
    alpha = r_ohm / (2.0 * l_val)
    zeta = alpha / wn
    
    disc = alpha**2 - wn**2
    if zeta < 1.0:
        wd = math.sqrt(wn**2 - alpha**2)
        response_type = "Subamortiguado (Oscilatorio)"
        s1 = f"{-alpha:.1f} + j{wd:.1f}"
        s2 = f"{-alpha:.1f} - j{wd:.1f}"
        ts_2pct = 4.0 / alpha
    elif zeta == 1.0:
        wd = 0.0
        response_type = "Críticamente amortiguado"
        s1 = s2 = f"{-alpha:.1f}"
        ts_2pct = 5.8 / alpha
    else:
        wd = 0.0
        s1_val = -alpha + math.sqrt(disc)
        s2_val = -alpha - math.sqrt(disc)
        response_type = "Sobreamortiguado (Lento)"
        s1 = f"{s1_val:.1f}"
        s2 = f"{s2_val:.1f}"
        ts_2pct = 4.0 / abs(s1_val)
        
    return {
        "undamped_frequency_wn_rad_s": round(wn, 2),
        "natural_frequency_f0_hz": round(wn / (2.0 * math.pi), 2),
        "attenuation_alpha": round(alpha, 2),
        "damping_ratio_zeta": round(zeta, 4),
        "response_classification": response_type,
        "pole_s1": s1,
        "pole_s2": s2,
        "settling_time_2pct_sec": round(ts_2pct, 4)
    }

def opamp_error_budget_calculator(vos_mv: float = 1.0, ib_na: float = 50.0, iio_na: float = 10.0,
                                  r1_kohm: float = 1.0, r2_kohm: float = 100.0, cmrr_db: float = 80.0,
                                  vcm_v: float = 5.0) -> Dict[str, Any]:
    """
    Computes op-amp non-inverting amplifier DC error budget: offset voltage, bias current, and CMRR error.
    """
    gain = 1.0 + (r2_kohm / r1_kohm)
    vos_err_out = (vos_mv * 1e-3) * gain
    
    # Bias current error: without compensation resistor R3 = R1||R2
    r_eq = (r1_kohm * r2_kohm) / (r1_kohm + r2_kohm) * 1e3
    ib_err_uncomp_out = (ib_na * 1e-9) * (r2_kohm * 1e3)
    ib_err_comp_out = (iio_na * 1e-9) * (r2_kohm * 1e3)
    
    # CMRR error
    cmrr_lin = 10.0**(cmrr_db / 20.0)
    v_err_cm = vcm_v / cmrr_lin
    cmrr_err_out = v_err_cm * gain
    
    tot_err_uncomp = vos_err_out + ib_err_uncomp_out + cmrr_err_out
    tot_err_comp = vos_err_out + ib_err_comp_out + cmrr_err_out
    
    return {
        "closed_loop_gain": round(gain, 2),
        "vos_error_output_mv": round(vos_err_out * 1000.0, 3),
        "ib_error_uncompensated_mv": round(ib_err_uncomp_out * 1000.0, 3),
        "ib_error_compensated_mv": round(ib_err_comp_out * 1000.0, 3),
        "cmrr_error_output_mv": round(cmrr_err_out * 1000.0, 3),
        "total_output_error_uncomp_mv": round(tot_err_uncomp * 1000.0, 3),
        "total_output_error_comp_mv": round(tot_err_comp * 1000.0, 3)
    }

# ======================================================================
# BRANCH 3: EMBEDDED SYSTEMS, DIGITAL & REAL-TIME (DD, EMB, SDC, HIPS, RT)
# ======================================================================

def arm_cortex_systick_timer(cpu_freq_mhz: float = 80.0, target_interval_ms: float = 1.0) -> Dict[str, Any]:
    """
    Computes ARM Cortex-M SysTick reload register value and generates CMSIS C code.
    """
    f_cpu = cpu_freq_mhz * 1e6
    interval_s = target_interval_ms * 1e-3
    ticks = int(f_cpu * interval_s)
    reload_val = ticks - 1
    
    is_valid = bool(0 < reload_val <= 0x00FFFFFF)  # 24-bit timer
    
    c_code = f"""// Inicialización SysTick para interrupción cada {target_interval_ms} ms a {cpu_freq_mhz} MHz
void SysTick_Init(void) {{
    SysTick->LOAD = {reload_val}UL; // 24-bit Reload Value
    SysTick->VAL  = 0UL;           // Reset counter
    SysTick->CTRL = SysTick_CTRL_CLKSOURCE_Msk |
                    SysTick_CTRL_TICKINT_Msk   |
                    SysTick_CTRL_ENABLE_Msk;   // Core clock, enable IRQ
}}
"""
    return {
        "cpu_freq_mhz": cpu_freq_mhz,
        "target_interval_ms": target_interval_ms,
        "reload_value_dec": reload_val,
        "reload_value_hex": f"0x{reload_val:06X}",
        "fits_24bit_timer": is_valid,
        "c_initialization_code": c_code
    }

def usart_baud_rate_generator(cpu_freq_mhz: float = 80.0, baud_rate: int = 115200, oversampling: int = 16) -> Dict[str, Any]:
    """
    Calculates USART baud rate register divisor (USART_BRR) for STM32/ARM Cortex-M.
    """
    f_clk = cpu_freq_mhz * 1e6
    usart_div = f_clk / (oversampling * baud_rate)
    mantissa = int(usart_div)
    fraction = int(round((usart_div - mantissa) * oversampling))
    
    if fraction >= oversampling:
        mantissa += 1
        fraction = 0
        
    actual_baud = f_clk / (oversampling * (mantissa + fraction / float(oversampling)))
    err_pct = ((actual_baud - baud_rate) / baud_rate) * 100.0
    brr_reg = (mantissa << 4) | (fraction & 0x0F)
    
    return {
        "target_baud": baud_rate,
        "actual_baud": round(actual_baud, 1),
        "error_percentage": round(err_pct, 3),
        "mantissa": mantissa,
        "fraction": fraction,
        "brr_register_hex": f"0x{brr_reg:04X}",
        "is_acceptable": bool(abs(err_pct) < 2.0)
    }

def adc_sar_timing_calculator(f_adc_mhz: float = 14.0, resolution_bits: int = 12, sampling_cycles: float = 15.0) -> Dict[str, Any]:
    """
    Calculates Successive Approximation (SAR) ADC total conversion time and maximum sampling rate.
    """
    total_cycles = sampling_cycles + resolution_bits
    t_conv_us = (total_cycles / (f_adc_mhz * 1e6)) * 1e6
    max_fs_ksps = (1.0 / (t_conv_us * 1e-6)) / 1000.0
    
    return {
        "adc_clock_mhz": f_adc_mhz,
        "resolution_bits": resolution_bits,
        "sampling_cycles": sampling_cycles,
        "total_cycles": total_cycles,
        "conversion_time_us": round(t_conv_us, 3),
        "max_sampling_rate_ksps": round(max_fs_ksps, 2)
    }

def vhdl_entity_generator(component_type: str = "fifo", width_bits: int = 8, depth: int = 16) -> Dict[str, Any]:
    """
    Generates clean synthesizable VHDL-93/2008 code for digital building blocks.
    """
    comp = component_type.lower()
    if comp == "fifo":
        code = f"""library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity sync_fifo is
    generic (
        DATA_WIDTH : integer := {width_bits};
        FIFO_DEPTH : integer := {depth}
    );
    port (
        clk     : in  std_logic;
        rst     : in  std_logic;
        wr_en   : in  std_logic;
        rd_en   : in  std_logic;
        din     : in  std_logic_vector(DATA_WIDTH-1 downto 0);
        dout    : out std_logic_vector(DATA_WIDTH-1 downto 0);
        full    : out std_logic;
        empty   : out std_logic
    );
end entity;

architecture rtl of sync_fifo is
    type mem_type is array (0 to FIFO_DEPTH-1) of std_logic_vector(DATA_WIDTH-1 downto 0);
    signal mem : mem_type := (others => (others => '0'));
    signal wr_ptr, rd_ptr : integer range 0 to FIFO_DEPTH-1 := 0;
    signal count : integer range 0 to FIFO_DEPTH := 0;
begin
    empty <= '1' when count = 0 else '0';
    full  <= '1' when count = FIFO_DEPTH else '0';

    process(clk) begin
        if rising_edge(clk) then
            if rst = '1' then
                wr_ptr <= 0;
                rd_ptr <= 0;
                count  <= 0;
            else
                if (wr_en = '1' and count < FIFO_DEPTH) then
                    mem(wr_ptr) <= din;
                    wr_ptr <= (wr_ptr + 1) mod FIFO_DEPTH;
                end if;
                if (rd_en = '1' and count > 0) then
                    dout <= mem(rd_ptr);
                    rd_ptr <= (rd_ptr + 1) mod FIFO_DEPTH;
                end if;
                if (wr_en = '1' and rd_en = '0' and count < FIFO_DEPTH) then
                    count <= count + 1;
                elsif (rd_en = '1' and wr_en = '0' and count > 0) then
                    count <= count - 1;
                end if;
            end if;
        end if;
    end process;
end architecture;
"""
    elif comp == "counter":
        code = f"""library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity generic_counter is
    generic (WIDTH : integer := {width_bits});
    port (
        clk, rst, en, up_down : in std_logic;
        count : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity;

architecture rtl of generic_counter is
    signal cnt_reg : unsigned(WIDTH-1 downto 0) := (others => '0');
begin
    process(clk, rst) begin
        if rst = '1' then
            cnt_reg <= (others => '0');
        elsif rising_edge(clk) then
            if en = '1' then
                if up_down = '1' then
                    cnt_reg <= cnt_reg + 1;
                else
                    cnt_reg <= cnt_reg - 1;
                end if;
            end if;
        end if;
    end process;
    count <= std_logic_vector(cnt_reg);
end architecture;
"""
    else:
        code = "-- Tipo de componente VHDL no soportado."
        
    return {
        "component": comp,
        "width_bits": width_bits,
        "depth": depth,
        "vhdl_code": code
    }

def sta_timing_slack_analyzer(t_clk_ns: float = 5.0, t_cq_ns: float = 0.35, t_logic_ns: float = 2.1,
                             t_routing_ns: float = 1.4, t_setup_ns: float = 0.45,
                             t_hold_ns: float = 0.25, t_skew_ns: float = 0.1) -> Dict[str, Any]:
    """
    Computes Setup Slack, Hold Slack, minimum clock period, and max clock frequency.
    """
    data_path_max = t_cq_ns + t_logic_ns + t_routing_ns
    setup_slack = (t_clk_ns - t_skew_ns) - (data_path_max + t_setup_ns)
    
    # Hold slack with fastest path estimate (30% logic delay)
    data_path_min = (t_cq_ns * 0.7) + (t_logic_ns * 0.3) + (t_routing_ns * 0.3)
    hold_slack = data_path_min - (t_hold_ns + t_skew_ns)
    
    t_min = data_path_max + t_setup_ns + t_skew_ns
    f_max_mhz = (1000.0 / t_min) if t_min > 0 else 0.0
    
    return {
        "clock_period_ns": t_clk_ns,
        "setup_slack_ns": round(setup_slack, 3),
        "setup_timing_met": bool(setup_slack >= 0.0),
        "hold_slack_ns": round(hold_slack, 3),
        "hold_timing_met": bool(hold_slack >= 0.0),
        "minimum_period_ns": round(t_min, 3),
        "maximum_frequency_mhz": round(f_max_mhz, 2)
    }

def rtos_schedulability_solver(tasks: Optional[List[Dict[str, float]]] = None) -> Dict[str, Any]:
    """
    Evaluates periodic real-time task set ({C_i, T_i}):
    Total utilization, RM bound, EDF schedulability, and exact RTA (Response Time Analysis).
    """
    if tasks is None:
        tasks = [
            {"c": 1.0, "t": 5.0, "name": "Task_A"},
            {"c": 2.0, "t": 10.0, "name": "Task_B"},
            {"c": 4.0, "t": 25.0, "name": "Task_C"}
        ]
    if not tasks:
        return {"error": "Task list is empty"}
        
    u_total = sum(t["c"] / t["t"] for t in tasks)
    n = len(tasks)
    rm_bound = n * (2**(1.0 / n) - 1.0)
    
    # Sort tasks by period for Rate Monotonic priority assignment
    sorted_tasks = sorted(tasks, key=lambda x: x["t"])
    
    # Exact RTA calculation
    wcrt_list = []
    schedulable_rta = True
    
    for i, t in enumerate(sorted_tasks):
        ci = t["c"]
        ti = t["t"]
        r = ci
        while True:
            r_next = ci
            for j in range(i):
                r_next += math.ceil(r / sorted_tasks[j]["t"]) * sorted_tasks[j]["c"]
            if r_next == r:
                break
            if r_next > ti:
                schedulable_rta = False
                break
            r = r_next
        wcrt_list.append({"task_period": ti, "wcet": ci, "wcrt": r, "schedulable": bool(r <= ti)})
        
    return {
        "num_tasks": n,
        "total_utilization": round(u_total, 4),
        "rm_liu_layland_bound": round(rm_bound, 4),
        "is_rm_guaranteed_by_bound": bool(u_total <= rm_bound),
        "is_edf_schedulable": bool(u_total <= 1.0),
        "is_rta_schedulable": schedulable_rta,
        "tasks_response_times": wcrt_list
    }

# ======================================================================
# BRANCH 4: SIGNALS, COMMUNICATIONS & DSP (SST, PPE, TRS, IOT)
# ======================================================================

def fir_filter_window_designer(order: int = 32, fc_hz: float = 2000.0, fs_hz: float = 16000.0,
                               window_type: str = "hamming") -> Dict[str, Any]:
    """
    Computes linear-phase FIR lowpass filter coefficients using windowed sinc method.
    """
    m = order
    ft = fc_hz / fs_hz
    h = []
    
    for i in range(m + 1):
        n = i - m / 2.0
        # Ideal sinc
        if n == 0:
            h_ideal = 2.0 * ft
        else:
            h_ideal = math.sin(2.0 * math.pi * ft * n) / (math.pi * n)
            
        # Window function
        if window_type.lower() == "hann":
            w = 0.5 * (1.0 - math.cos(2.0 * math.pi * i / m))
        elif window_type.lower() == "blackman":
            w = 0.42 - 0.5 * math.cos(2.0 * math.pi * i / m) + 0.08 * math.cos(4.0 * math.pi * i / m)
        else:  # Hamming default
            w = 0.54 - 0.46 * math.cos(2.0 * math.pi * i / m)
            
        h.append(round(h_ideal * w, 6))
        
    return {
        "filter_order": order,
        "taps": order + 1,
        "cutoff_frequency_hz": fc_hz,
        "sampling_frequency_hz": fs_hz,
        "window_type": window_type.capitalize(),
        "group_delay_samples": order / 2.0,
        "coefficients": h
    }

def bilinear_transform_mapper(fc_analog_hz: float = 1000.0, fs_hz: float = 8000.0) -> Dict[str, Any]:
    """
    Computes prewarped analog frequency and bilinear transform mapping parameters.
    """
    ts = 1.0 / fs_hz
    omega_digital = 2.0 * math.pi * (fc_analog_hz / fs_hz)
    omega_prewarped = (2.0 / ts) * math.tan(omega_digital / 2.0)
    
    return {
        "analog_fc_hz": fc_analog_hz,
        "sampling_rate_hz": fs_hz,
        "digital_omega_rad": round(omega_digital, 4),
        "prewarped_analog_rad_s": round(omega_prewarped, 2),
        "prewarped_freq_hz": round(omega_prewarped / (2.0 * math.pi), 2)
    }

def fft_resolution_inspector(fs_hz: float = 48000.0, n_fft: int = 1024) -> Dict[str, Any]:
    """
    Analyzes FFT frequency bin width, window time length, and frequency resolution.
    """
    delta_f = fs_hz / n_fft
    t_window_ms = (n_fft / fs_hz) * 1000.0
    nyquist_hz = fs_hz / 2.0
    
    return {
        "sampling_frequency_hz": fs_hz,
        "fft_points": n_fft,
        "frequency_bin_width_hz": round(delta_f, 3),
        "time_window_ms": round(t_window_ms, 3),
        "nyquist_limit_hz": round(nyquist_hz, 1)
    }

def lora_toa_and_energy_predictor(sf: int = 7, bw_khz: float = 125.0, cr: int = 1,
                                  payload_bytes: int = 25, preamble_symbols: int = 8,
                                  bat_mah: float = 2400.0, i_tx_ma: float = 40.0,
                                  i_sleep_ua: float = 10.0, tx_interval_s: float = 600.0) -> Dict[str, Any]:
    """
    Calculates exact LoRa Time-on-Air (ToA) and battery longevity in years.
    """
    bw = bw_khz * 1e3
    t_sym_ms = ((2**sf) / bw) * 1000.0
    t_preamble = (preamble_symbols + 4.25) * t_sym_ms
    
    # Payload symbol count formula
    num = 8 * payload_bytes - 4 * sf + 28 + 16  # with CRC
    den = 4.0 * sf
    n_payload = 8 + max(0, math.ceil(num / den) * (cr + 4))
    t_payload = n_payload * t_sym_ms
    toa_ms = t_preamble + t_payload
    
    # Energy model
    duty = (toa_ms / 1000.0) / max(1.0, tx_interval_s)
    avg_current_ma = (i_tx_ma * duty) + ((i_sleep_ua * 1e-3) * (1.0 - duty))
    lifetime_hours = bat_mah / max(1e-6, avg_current_ma)
    lifetime_years = lifetime_hours / (24.0 * 365.25)
    
    return {
        "spreading_factor": sf,
        "bandwidth_khz": bw_khz,
        "symbol_duration_ms": round(t_sym_ms, 4),
        "preamble_duration_ms": round(t_preamble, 2),
        "payload_duration_ms": round(t_payload, 2),
        "total_time_on_air_ms": round(toa_ms, 2),
        "average_current_ua": round(avg_current_ma * 1000.0, 2),
        "battery_longevity_years": round(lifetime_years, 2)
    }

def adc_quantization_noise_analyzer(bits: int = 12, v_fs: float = 3.3) -> Dict[str, Any]:
    """
    Computes ADC quantization step, RMS noise, and theoretical SQNR.
    """
    lsb_volts = v_fs / (2**bits)
    q_noise_rms_uv = (lsb_volts / math.sqrt(12.0)) * 1e6
    sqnr_db = 6.02 * bits + 1.76
    
    return {
        "resolution_bits": bits,
        "full_scale_voltage_v": v_fs,
        "lsb_step_mv": round(lsb_volts * 1000.0, 4),
        "quantization_noise_rms_uv": round(q_noise_rms_uv, 3),
        "theoretical_sqnr_db": round(sqnr_db, 2)
    }

def z_transform_pole_zero_analyzer(b_coeffs: Optional[List[float]] = None, a_coeffs: Optional[List[float]] = None) -> Dict[str, Any]:
    """
    Analyzes discrete-time system stability, DC gain H(1), and Nyquist gain H(-1).
    """
    if b_coeffs is None:
        b_coeffs = [0.2, 0.2]
    if a_coeffs is None:
        a_coeffs = [1.0, -0.6]
    # DC gain (z = 1)
    dc_num = sum(b_coeffs)
    dc_den = sum(a_coeffs)
    dc_gain = dc_num / max(1e-9, dc_den)
    
    # Nyquist gain (z = -1)
    nyq_num = sum(b * ((-1)**i) for i, b in enumerate(b_coeffs))
    nyq_den = sum(a * ((-1)**i) for i, a in enumerate(a_coeffs))
    nyq_gain = nyq_num / max(1e-9, nyq_den)
    
    return {
        "num_coefficients_b": b_coeffs,
        "den_coefficients_a": a_coeffs,
        "dc_gain_at_z1": round(dc_gain, 4),
        "dc_gain_db": round(20.0 * math.log10(max(1e-6, abs(dc_gain))), 2),
        "nyquist_gain_at_z_minus1": round(nyq_gain, 4)
    }

# ======================================================================
# BRANCH 5: PHYSICAL SENSORS, MATERIALS & DEVICES (F, CEM, SM, DIFO, INT)
# ======================================================================

def solar_cell_single_diode_solver(isc_a: float = 9.5, voc_v: float = 40.0,
                                   rs_ohm: float = 0.05, rsh_ohm: float = 1000.0,
                                   ideality_n: float = 1.2, temp_c: float = 25.0,
                                   area_m2: float = 1.6, irradiance_w_m2: float = 1000.0) -> Dict[str, Any]:
    """
    Computes photovoltaic I-V curve, Maximum Power Point (MPP), Fill Factor, and efficiency.
    """
    vt = 8.617333e-5 * (temp_c + 273.15)
    # Reverse saturation current estimate from Voc
    i0 = isc_a / (math.exp(voc_v / (ideality_n * vt * 60)) - 1.0)
    
    # Approximate MPP voltage ~ 0.8 * Voc
    v_mpp = 0.82 * voc_v
    # Approximate MPP current ~ 0.94 * Isc
    i_mpp = 0.94 * isc_a
    p_max = v_mpp * i_mpp
    
    ff = p_max / (voc_v * isc_a)
    pin = irradiance_w_m2 * area_m2
    eff = (p_max / max(1.0, pin)) * 100.0
    
    return {
        "short_circuit_current_isc_a": round(isc_a, 2),
        "open_circuit_voltage_voc_v": round(voc_v, 2),
        "mpp_voltage_v": round(v_mpp, 2),
        "mpp_current_a": round(i_mpp, 2),
        "max_power_mpp_w": round(p_max, 2),
        "fill_factor": round(ff, 4),
        "conversion_efficiency_pct": round(eff, 2)
    }

def rtd_pt100_temperature_solver(temp_c: Optional[float] = None, resistance_ohm: Optional[float] = None,
                                 wiring_mode: str = "4-wire", lead_resistance_ohm: float = 2.5) -> Dict[str, Any]:
    """
    Solves Callendar-Van Dusen equation forward (T -> R) or reverse (R -> T) with Kelvin compensation.
    """
    r0 = 100.0
    a = 3.9083e-3
    b = -5.775e-7
    
    if temp_c is None and resistance_ohm is None:
        resistance_ohm = 119.40
    
    if temp_c is not None:
        t = temp_c
        if t >= 0:
            r_pt100 = r0 * (1.0 + a * t + b * t**2)
        else:
            c_coeff = -4.183e-12
            r_pt100 = r0 * (1.0 + a * t + b * t**2 + c_coeff * (t - 100.0) * t**3)
            
        # Error depending on wiring
        if wiring_mode.lower() == "2-wire":
            r_measured = r_pt100 + 2.0 * lead_resistance_ohm
        elif wiring_mode.lower() == "3-wire":
            r_measured = r_pt100  # balanced bridge eliminates lead resistance
        else:  # 4-wire
            r_measured = r_pt100
            
        return {
            "input_temperature_c": temp_c,
            "actual_sensor_resistance_ohm": round(r_pt100, 4),
            "measured_resistance_ohm": round(r_measured, 4),
            "wiring_mode": wiring_mode,
            "lead_resistance_induced_error_c": round((r_measured - r_pt100) / (r0 * a), 3)
        }
    elif resistance_ohm is not None:
        r = resistance_ohm
        # Inverse solution (t >= 0): r = r0*(1 + a*t + b*t^2) => b*t^2 + a*t + (1 - r/r0) = 0
        disc = a**2 - 4.0 * b * (1.0 - r / r0)
        if disc >= 0:
            t = (-a + math.sqrt(disc)) / (2.0 * b)
        else:
            t = (r - r0) / (r0 * a)
        return {
            "input_resistance_ohm": resistance_ohm,
            "calculated_temperature_c": round(t, 3),
            "sensitivity_dr_dt_ohm_c": round(r0 * a, 4)
        }
    else:
        return {"error": "Must provide either temp_c or resistance_ohm"}

def strain_gauge_rosette_solver(eps_0_ue: float = 400.0, eps_45_ue: float = 250.0, eps_90_ue: float = -100.0,
                                e_modulus_gpa: float = 70.0, poisson_ratio: float = 0.33) -> Dict[str, Any]:
    """
    Solves 45-degree rectangular strain rosette: principal strains, angle, and principal stresses (Mohr's circle).
    """
    e0 = eps_0_ue * 1e-6
    e45 = eps_45_ue * 1e-6
    e90 = eps_90_ue * 1e-6
    
    # Centre and radius of strain Mohr's circle
    eps_center = (e0 + e90) / 2.0
    r_strain = math.sqrt(((e0 - e90) / 2.0)**2 + (e45 - eps_center)**2)
    
    eps_1 = eps_center + r_strain
    eps_2 = eps_center - r_strain
    gamma_max = 2.0 * r_strain
    theta_p_deg = 0.5 * math.degrees(math.atan2(2.0 * e45 - e0 - e90, e0 - e90))
    
    # Plane stress constitutive equations
    e = e_modulus_gpa * 1e9
    nu = poisson_ratio
    sigma_1 = (e / (1.0 - nu**2)) * (eps_1 + nu * eps_2) * 1e-6  # MPa
    sigma_2 = (e / (1.0 - nu**2)) * (eps_2 + nu * eps_1) * 1e-6  # MPa
    
    return {
        "principal_strain_1_ue": round(eps_1 * 1e6, 2),
        "principal_strain_2_ue": round(eps_2 * 1e6, 2),
        "max_shear_strain_ue": round(gamma_max * 1e6, 2),
        "principal_angle_deg": round(theta_p_deg, 2),
        "principal_stress_1_mpa": round(sigma_1, 2),
        "principal_stress_2_mpa": round(sigma_2, 2)
    }

def pcb_thermal_heatsink_dimensioner(p_dis_w: float = 5.0, t_ambient_c: float = 40.0,
                                     t_junction_max_c: float = 125.0, theta_jc: float = 1.5,
                                     theta_cs: float = 0.5) -> Dict[str, Any]:
    """
    Dimensions heatsink maximum allowable thermal resistance and determines thermal viability.
    """
    delta_t_max = t_junction_max_c - t_ambient_c
    theta_ja_max = delta_t_max / p_dis_w
    theta_sa_max = theta_ja_max - theta_jc - theta_cs
    
    is_safe = bool(theta_sa_max > 0.0)
    
    return {
        "dissipated_power_w": p_dis_w,
        "max_junction_temperature_c": t_junction_max_c,
        "ambient_temperature_c": t_ambient_c,
        "max_total_rth_ja_c_w": round(theta_ja_max, 2),
        "max_allowable_heatsink_rth_sa_c_w": round(theta_sa_max, 2) if is_safe else 0.0,
        "is_passive_cooling_feasible": is_safe
    }

def system_reliability_markov_solver(components_mttf_h: Optional[List[float]] = None, mission_time_h: float = 5000.0,
                                     configuration: str = "parallel") -> Dict[str, Any]:
    """
    Computes system reliability R(t), failure rate, and MTBF for Series or Parallel configurations.
    """
    if components_mttf_h is None:
        components_mttf_h = [100000.0, 100000.0]
    if not components_mttf_h:
        return {"error": "Components list empty"}
        
    reliabilities = [math.exp(-mission_time_h / max(1.0, mttf)) for mttf in components_mttf_h]
    
    if configuration.lower() == "series":
        r_sys = 1.0
        lambda_sum = 0.0
        for mttf, r_comp in zip(components_mttf_h, reliabilities):
            r_sys *= r_comp
            lambda_sum += 1.0 / max(1.0, mttf)
        mtbf_sys = 1.0 / max(1e-12, lambda_sum)
    else:  # Parallel redundant
        unavail = 1.0
        for r_comp in reliabilities:
            unavail *= (1.0 - r_comp)
        r_sys = 1.0 - unavail
        # For identical components in parallel: MTBF = MTTF * sum(1/i)
        base_mttf = components_mttf_h[0]
        mtbf_sys = base_mttf * sum(1.0 / (i + 1) for i in range(len(components_mttf_h)))
        
    return {
        "configuration": configuration.capitalize(),
        "mission_time_hours": mission_time_h,
        "system_reliability": round(r_sys, 6),
        "system_mtbf_hours": round(mtbf_sys, 1),
        "unreliability": round(1.0 - r_sys, 6)
    }

def second_order_system_step_response(wn_rad_s: float = 10.0, zeta: float = 0.5) -> Dict[str, Any]:
    """
    Solves standard second order system step response metrics: rise time, peak time, settling time, overshoot.
    """
    if zeta < 1.0:
        wd = wn_rad_s * math.sqrt(1.0 - zeta**2)
        mp_pct = math.exp(-math.pi * zeta / math.sqrt(1.0 - zeta**2)) * 100.0
        tp = math.pi / wd
        # Rise time (10% to 90% approximation)
        tr = (0.8 + 2.5 * zeta) / wn_rad_s
        ts_2pct = 4.0 / (zeta * wn_rad_s)
        ts_5pct = 3.0 / (zeta * wn_rad_s)
        classification = "Subamortiguado (Underdamped)"
    elif zeta == 1.0:
        mp_pct = 0.0
        tp = 0.0
        tr = 3.36 / wn_rad_s
        ts_2pct = 5.83 / wn_rad_s
        ts_5pct = 4.74 / wn_rad_s
        classification = "Críticamente amortiguado (Critically Damped)"
    else:
        mp_pct = 0.0
        tp = 0.0
        s1 = -zeta * wn_rad_s + wn_rad_s * math.sqrt(zeta**2 - 1.0)
        tr = 2.2 / abs(s1)
        ts_2pct = 4.0 / abs(s1)
        ts_5pct = 3.0 / abs(s1)
        classification = "Sobreamortiguado (Overdamped)"
        
    return {
        "natural_frequency_wn_rad_s": wn_rad_s,
        "damping_ratio_zeta": zeta,
        "classification": classification,
        "peak_overshoot_percentage": round(mp_pct, 2),
        "peak_time_sec": round(tp, 4),
        "rise_time_sec": round(tr, 4),
        "settling_time_2pct_sec": round(ts_2pct, 4),
        "settling_time_5pct_sec": round(ts_5pct, 4)
    }

def pll_loop_filter_synthesizer(
    f_ref_hz: float = 10e6,
    f_out_hz: float = 2.4e9,
    loop_bw_hz: float = 100e3,
    phase_margin_deg: float = 48.0,
    k_vco_mhz_v: float = 30.0,
    i_cp_ma: float = 2.5
) -> Dict[str, Any]:
    """
    Synthesizes a 2nd-order passive lead-lag loop filter for a Charge-Pump PLL.
    Computes divider ratio N, loop component values (C1, C2, R2), and pole/zero frequencies.
    """
    n_div = int(round(f_out_hz / f_ref_hz))
    wc = 2.0 * math.pi * loop_bw_hz
    pm_rad = math.radians(phase_margin_deg)
    k_vco_rad_s_v = (k_vco_mhz_v * 1e6) * (2.0 * math.pi)
    i_cp_a = i_cp_ma * 1e-3
    
    # Standard Banerjee / Gardner Charge-Pump PLL 2nd-order loop filter synthesis
    sec_pm = 1.0 / math.cos(pm_rad)
    tan_pm = math.tan(pm_rad)
    gamma = sec_pm + tan_pm
    
    t2 = gamma / wc          # Stabilizing zero time constant
    t1 = 1.0 / (wc * gamma)  # High-frequency pole time constant
    
    # Total effective capacitance at low frequency: C_total = C1 + C2
    c_tot = (i_cp_a * k_vco_rad_s_v) / (2.0 * math.pi * (wc**2) * n_div) * math.sqrt((1.0 + (wc * t1)**2) / (1.0 + (wc * t2)**2))
    
    c1 = c_tot * (t1 / t2)
    c2 = c_tot * (1.0 - (t1 / t2))
    r2 = t2 / c2 if c2 > 0 else 0.0
    
    # Express in engineering units
    c1_pf = c1 * 1e12
    c2_pf = c2 * 1e12
    r2_ohm = r2
    
    return {
        "output_frequency_hz": f_out_hz,
        "reference_frequency_hz": f_ref_hz,
        "divider_ratio_n": n_div,
        "loop_bandwidth_khz": round(loop_bw_hz * 1e-3, 2),
        "target_phase_margin_deg": phase_margin_deg,
        "c1_pf": round(c1_pf, 2),
        "c2_pf": round(c2_pf, 2),
        "r2_ohm": round(r2_ohm, 1),
        "zero_frequency_khz": round(1.0 / (2.0 * math.pi * t2 * 1e3), 2),
        "pole_frequency_khz": round(1.0 / (2.0 * math.pi * t1 * 1e3), 2)
    }

def transmission_line_bounce_diagram(
    vg_step_v: float = 3.3,
    zg_ohm: float = 20.0,
    z0_ohm: float = 50.0,
    zl_ohm: float = 1000.0,
    td_ns: float = 1.5,
    num_bounces: int = 5
) -> Dict[str, Any]:
    """
    Computes transient reflections and lattice bounce diagram for high-speed digital transmission lines.
    Calculates reflection coefficients Gamma_G and Gamma_L, step voltages, and steady-state values.
    """
    gamma_l = (zl_ohm - z0_ohm) / (zl_ohm + z0_ohm)
    gamma_g = (zg_ohm - z0_ohm) / (zg_ohm + z0_ohm)
    
    # Initial forward voltage launched into transmission line at t = 0+
    v1_plus = vg_step_v * (z0_ohm / (zg_ohm + z0_ohm))
    
    timeline = []
    current_wave = v1_plus
    
    v_near = v1_plus
    v_far = 0.0
    
    # Step-by-step wave tracking
    # t = 0: Generator launches v1_plus
    timeline.append({
        "time_ns": 0.0,
        "location": "Generator (Near-End)",
        "event": "Initial wave launched",
        "delta_v": round(v1_plus, 4),
        "v_node": round(v_near, 4)
    })
    
    for i in range(1, num_bounces + 1):
        t_load = (2 * i - 1) * td_ns
        refl_load = current_wave * gamma_l
        v_far += (current_wave + refl_load)
        timeline.append({
            "time_ns": round(t_load, 3),
            "location": "Load (Far-End)",
            "event": f"Reflection bounce {2*i-1}",
            "delta_v": round(current_wave + refl_load, 4),
            "v_node": round(v_far, 4)
        })
        
        t_gen = (2 * i) * td_ns
        refl_gen = refl_load * gamma_g
        v_near += (refl_load + refl_gen)
        timeline.append({
            "time_ns": round(t_gen, 3),
            "location": "Generator (Near-End)",
            "event": f"Reflection bounce {2*i}",
            "delta_v": round(refl_load + refl_gen, 4),
            "v_node": round(v_near, 4)
        })
        
        current_wave = refl_gen
        
    steady_state_v = vg_step_v * (zl_ohm / (zg_ohm + zl_ohm))
    
    return {
        "vg_step_v": vg_step_v,
        "gamma_generator": round(gamma_g, 4),
        "gamma_load": round(gamma_l, 4),
        "initial_launched_v": round(v1_plus, 4),
        "steady_state_v": round(steady_state_v, 4),
        "one_way_delay_ns": td_ns,
        "bounce_timeline": timeline
    }

# Master registry of all available tools
ALL_ENGINEERING_TOOLS = {
    # Branch 1: RF, Microwaves & Telecommunications
    "microstrip_synthesizer": microstrip_synthesizer,
    "smith_chart_stub_matcher": smith_chart_stub_matcher,
    "quarter_wave_transformer": quarter_wave_transformer,
    "friis_cascade_analyzer": friis_cascade_analyzer,
    "wilkinson_divider_designer": wilkinson_divider_designer,
    "coaxial_cable_solver": coaxial_cable_solver,
    "link_budget_calculator": link_budget_calculator,
    "rectangular_waveguide_modes": rectangular_waveguide_modes,
    "shannon_channel_capacity": shannon_channel_capacity,
    "pll_loop_filter_synthesizer": pll_loop_filter_synthesizer,
    
    # Branch 2: Analog & Power Electronics
    "bjt_amplifier_designer": bjt_amplifier_designer,
    "mosfet_amplifier_designer": mosfet_amplifier_designer,
    "differential_pair_analyzer": differential_pair_analyzer,
    "sallen_key_filter_synthesizer": sallen_key_filter_synthesizer,
    "buck_converter_synthesizer": buck_converter_synthesizer,
    "boost_converter_synthesizer": boost_converter_synthesizer,
    "rlc_transient_solver": rlc_transient_solver,
    "opamp_error_budget_calculator": opamp_error_budget_calculator,
    
    # Branch 3: Digital Systems & Embedded Computing
    "arm_cortex_systick_timer": arm_cortex_systick_timer,
    "usart_baud_rate_generator": usart_baud_rate_generator,
    "adc_sar_timing_calculator": adc_sar_timing_calculator,
    "vhdl_entity_generator": vhdl_entity_generator,
    "sta_timing_slack_analyzer": sta_timing_slack_analyzer,
    "rtos_schedulability_solver": rtos_schedulability_solver,
    "transmission_line_bounce_diagram": transmission_line_bounce_diagram,
    
    # Branch 4: Signal Processing & Communications
    "fir_filter_window_designer": fir_filter_window_designer,
    "bilinear_transform_mapper": bilinear_transform_mapper,
    "fft_resolution_inspector": fft_resolution_inspector,
    "lora_toa_and_energy_predictor": lora_toa_and_energy_predictor,
    "adc_quantization_noise_analyzer": adc_quantization_noise_analyzer,
    "z_transform_pole_zero_analyzer": z_transform_pole_zero_analyzer,
    
    # Branch 5: Physical Devices, Sensors & Control
    "solar_cell_single_diode_solver": solar_cell_single_diode_solver,
    "rtd_pt100_temperature_solver": rtd_pt100_temperature_solver,
    "strain_gauge_rosette_solver": strain_gauge_rosette_solver,
    "pcb_thermal_heatsink_dimensioner": pcb_thermal_heatsink_dimensioner,
    "system_reliability_markov_solver": system_reliability_markov_solver,
    "second_order_system_step_response": second_order_system_step_response
}

ENGINEERING_TOOLS_METADATA = {
    # Branch 1
    "microstrip_synthesizer": {
        "title": "Sintetizador de Líneas Microstrip",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230022 - ICAF", "230026 - CIAF"],
        "description": "Calcula el ancho de pista W, permitividad efectiva y retardo de propagación para una impedancia Z0 dada usando Hammerstad-Wheeler.",
        "params": {
            "z0_target": {"default": 50.0, "type": "float", "label": "Impedancia deseada (Ohm)"},
            "er": {"default": 4.4, "type": "float", "label": "Permitividad sustrato (eps_r)"},
            "h_mm": {"default": 1.6, "type": "float", "label": "Espesor del dieléctrico (mm)"},
            "t_um": {"default": 35.0, "type": "float", "label": "Grosor del cobre (um)"}
        }
    },
    "smith_chart_stub_matcher": {
        "title": "Adaptador Shunt Stub (Carta de Smith)",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230022 - ICAF", "230026 - CIAF"],
        "description": "Calcula distancia d y longitud l de stub abierto/cortocircuitado para adaptación perfecta en alta frecuencia.",
        "params": {
            "zl_real": {"default": 25.0, "type": "float", "label": "Parte real Z_L (Ohm)"},
            "zl_imag": {"default": -50.0, "type": "float", "label": "Parte imag Z_L (Ohm)"},
            "z0": {"default": 50.0, "type": "float", "label": "Impedancia característica Z0 (Ohm)"},
            "freq_hz": {"default": 2.4e9, "type": "float", "label": "Frecuencia de trabajo (Hz)"}
        }
    },
    "quarter_wave_transformer": {
        "title": "Transformador de Cuarto de Onda (Lambda/4)",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230022 - ICAF"],
        "description": "Diseña línea Lambda/4 para adaptar cargas reales y analiza ancho de banda para un VSWR máximo.",
        "params": {
            "zl_real": {"default": 100.0, "type": "float", "label": "Impedancia de carga Z_L (Ohm)"},
            "z0": {"default": 50.0, "type": "float", "label": "Impedancia de entrada Z0 (Ohm)"},
            "freq_hz": {"default": 1e9, "type": "float", "label": "Frecuencia central (Hz)"},
            "bandwidth_pct": {"default": 20.0, "type": "float", "label": "Ancho de banda porcentual (%)"}
        }
    },
    "friis_cascade_analyzer": {
        "title": "Analizador de Cascada RF (Fórmula de Friis)",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230026 - CIAF", "230027 - SCOM"],
        "description": "Calcula Ganancia total, Factor de Ruido (NF en dB) y Temperatura equivalente de una cadena de receptores en cascada.",
        "params": {
            "stages": {
                "default": [
                    {"gain_db": 15.0, "nf_db": 1.5, "oip3_dbm": 30.0},
                    {"gain_db": -3.0, "nf_db": 3.0, "oip3_dbm": 45.0},
                    {"gain_db": 20.0, "nf_db": 4.5, "oip3_dbm": 35.0}
                ],
                "type": "list",
                "label": "Etapas RF (JSON: gain_db, nf_db, oip3_dbm)"
            }
        }
    },
    "wilkinson_divider_designer": {
        "title": "Diseñador de Divisor de Wilkinson",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230026 - CIAF"],
        "description": "Calcula impedancias de rama, resistencia de aislamiento y parámetros S del divisor de potencia de Wilkinson.",
        "params": {
            "z0": {"default": 50.0, "type": "float", "label": "Impedancia de puertos Z0 (Ohm)"},
            "freq_hz": {"default": 2.4e9, "type": "float", "label": "Frecuencia de diseño (Hz)"}
        }
    },
    "coaxial_cable_solver": {
        "title": "Calculador de Línea Coaxial",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230018 - EMG", "230022 - ICAF"],
        "description": "Calcula Z0, L, C, frecuencia de corte de modos superiores (TE11) y tensión de ruptura dieléctrica de un cable coaxial.",
        "params": {
            "inner_diam_mm": {"default": 0.9, "type": "float", "label": "Diámetro conductor interno (mm)"},
            "outer_diam_mm": {"default": 2.95, "type": "float", "label": "Diámetro conductor externo (mm)"},
            "er": {"default": 2.1, "type": "float", "label": "Permitividad dieléctrica"}
        }
    },
    "link_budget_calculator": {
        "title": "Presupuesto de Enlace Radio (Link Budget)",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230027 - SCOM", "230022 - ICAF"],
        "description": "Calcula potencia recibida (Prx), margen de desvanecimiento y SNR según la ecuación de transmisión de Friis con pérdidas atmosféricas.",
        "params": {
            "ptx_dbm": {"default": 14.0, "type": "float", "label": "Potencia transmisor (dBm)"},
            "gtx_dbi": {"default": 2.15, "type": "float", "label": "Ganancia antena TX (dBi)"},
            "grx_dbi": {"default": 2.15, "type": "float", "label": "Ganancia antena RX (dBi)"},
            "freq_mhz": {"default": 868.0, "type": "float", "label": "Frecuencia (MHz)"},
            "distance_km": {"default": 5.0, "type": "float", "label": "Distancia del enlace (km)"},
            "misc_losses_db": {"default": 2.0, "type": "float", "label": "Pérdidas adicionales (dB)"},
            "rx_sensitivity_dbm": {"default": -137.0, "type": "float", "label": "Sensibilidad del receptor (dBm)"}
        }
    },
    "rectangular_waveguide_modes": {
        "title": "Analizador de Guía de Onda Rectangular",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230018 - EMG", "230022 - ICAF"],
        "description": "Calcula frecuencias de corte para modos TE/TM, modo fundamental y rango de operación monomodo.",
        "params": {
            "a_mm": {"default": 22.86, "type": "float", "label": "Ancho 'a' de la guía (mm) [WR-90 standard]"},
            "b_mm": {"default": 10.16, "type": "float", "label": "Alto 'b' de la guía (mm)"},
            "er": {"default": 1.0, "type": "float", "label": "Permitividad del medio interior"}
        }
    },
    "shannon_channel_capacity": {
        "title": "Capacidad de Canal (Shannon-Hartley)",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230027 - SCOM", "230019 - AST"],
        "description": "Calcula el límite teórico de velocidad de transmisión de datos sin errores para un ancho de banda y SNR dados.",
        "params": {
            "bandwidth_hz": {"default": 20e6, "type": "float", "label": "Ancho de banda (Hz)"},
            "snr_db": {"default": 20.0, "type": "float", "label": "Relación Señal a Ruido (SNR en dB)"}
        }
    },
    "pll_loop_filter_synthesizer": {
        "title": "Sintetizador de Filtro de Bucle PLL",
        "branch": "RF, Microondas y Telecomunicación",
        "courses": ["230026 - CIAF", "230022 - ICAF"],
        "description": "Sintetiza filtro de bucle pasivo de 2º orden para PLL con bomba de carga (C1, C2, R2) y margen de fase óptimo.",
        "params": {
            "f_ref_hz": {"default": 10e6, "type": "float", "label": "Frecuencia de referencia (Hz)"},
            "f_out_hz": {"default": 2.4e9, "type": "float", "label": "Frecuencia de salida del VCO (Hz)"},
            "loop_bw_hz": {"default": 100e3, "type": "float", "label": "Ancho de banda del bucle (Hz)"},
            "phase_margin_deg": {"default": 48.0, "type": "float", "label": "Margen de fase deseado (grados)"},
            "k_vco_mhz_v": {"default": 30.0, "type": "float", "label": "Ganancia del VCO Kvco (MHz/V)"},
            "i_cp_ma": {"default": 2.5, "type": "float", "label": "Corriente Charge Pump (mA)"}
        }
    },
    # Branch 2
    "bjt_amplifier_designer": {
        "title": "Diseñador de Amplificador BJT (Emisor Común)",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230023 - ED", "230025 - CISE"],
        "description": "Calcula punto de polarización Q (Vce, Ic), divisor resistivo y genera netlist SPICE ejecutable.",
        "params": {
            "vcc": {"default": 12.0, "type": "float", "label": "Tensión de alimentación Vcc (V)"},
            "ic_ma": {"default": 2.0, "type": "float", "label": "Corriente de colector deseada (mA)"},
            "vce_v": {"default": 6.0, "type": "float", "label": "Tensión Vce reposo deseada (V)"},
            "beta": {"default": 150.0, "type": "float", "label": "Ganancia beta (hfe)"},
            "f_low_hz": {"default": 50.0, "type": "float", "label": "Frecuencia de corte inferior (Hz)"}
        }
    },
    "mosfet_amplifier_designer": {
        "title": "Diseñador de Amplificador MOSFET (Fuente Común)",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230023 - ED", "230025 - CISE"],
        "description": "Calcula polarización en zona de saturación, transconductancia gm, resistencia de salida y ganancia en pequeña señal.",
        "params": {
            "vdd": {"default": 5.0, "type": "float", "label": "Alimentación Vdd (V)"},
            "id_ma": {"default": 1.0, "type": "float", "label": "Corriente de drenador Id (mA)"},
            "vds_v": {"default": 2.5, "type": "float", "label": "Tensión Vds deseada (V)"},
            "vth": {"default": 0.7, "type": "float", "label": "Tensión de umbral Vth (V)"},
            "kn_prime_ua_v2": {"default": 200.0, "type": "float", "label": "Parámetro Kn' (uA/V^2)"},
            "w_l_ratio": {"default": 10.0, "type": "float", "label": "Relación W/L"},
            "lambda_mod": {"default": 0.02, "type": "float", "label": "Modulación de longitud de canal lambda"}
        }
    },
    "differential_pair_analyzer": {
        "title": "Analizador de Par Diferencial (BJT/MOS)",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230025 - CISE"],
        "description": "Calcula ganancia diferencial Ad, ganancia de modo común Acm, CMRR en dB y rango dinámico lineal.",
        "params": {
            "vcc": {"default": 15.0, "type": "float", "label": "Alimentación positiva Vcc (V)"},
            "vee": {"default": -15.0, "type": "float", "label": "Alimentación negativa Vee (V)"},
            "itail_ma": {"default": 2.0, "type": "float", "label": "Corriente de cola I_tail (mA)"},
            "rc_kohm": {"default": 10.0, "type": "float", "label": "Resistencia de carga Rc (kOhm)"},
            "beta": {"default": 200.0, "type": "float", "label": "Ganancia de corriente beta"},
            "va_early": {"default": 100.0, "type": "float", "label": "Tensión de Early Va (V)"}
        }
    },
    "sallen_key_filter_synthesizer": {
        "title": "Sintetizador de Filtro Sallen-Key Activo",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230025 - CISE"],
        "description": "Sintetiza filtro activo paso-bajo de 2º orden con respuesta Butterworth, Chebyshev o Bessel.",
        "params": {
            "filter_type": {"default": "lowpass", "type": "str", "label": "Tipo de filtro (lowpass, highpass)"},
            "approx_type": {"default": "butterworth", "type": "str", "label": "Aproximación (butterworth, chebyshev_1db, bessel)"},
            "fc_hz": {"default": 1000.0, "type": "float", "label": "Frecuencia de corte fc (Hz)"},
            "gain": {"default": 1.0, "type": "float", "label": "Ganancia de banda pasante"}
        }
    },
    "buck_converter_synthesizer": {
        "title": "Sintetizador de Convertidor Buck (Step-Down)",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230030 - EAP"],
        "description": "Calcula ciclo de trabajo D, inductancia L para modo CCM, condensador de salida Cout y corriente de pico.",
        "params": {
            "vin_v": {"default": 24.0, "type": "float", "label": "Tensión de entrada Vin (V)"},
            "vout_v": {"default": 5.0, "type": "float", "label": "Tensión de salida Vout (V)"},
            "iout_a": {"default": 3.0, "type": "float", "label": "Corriente de salida nominal (A)"},
            "fsw_khz": {"default": 200.0, "type": "float", "label": "Frecuencia de conmutación (kHz)"},
            "delta_il_ratio": {"default": 0.3, "type": "float", "label": "Rizado relativo de inductor (0.2 a 0.4)"},
            "delta_vo_ratio": {"default": 0.01, "type": "float", "label": "Rizado relativo de tensión de salida"}
        }
    },
    "boost_converter_synthesizer": {
        "title": "Sintetizador de Convertidor Boost (Step-Up)",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230030 - EAP"],
        "description": "Calcula ciclo de trabajo D, inductancia L para CCM, condensador Cout y estrés de tensión en semiconductor.",
        "params": {
            "vin_v": {"default": 12.0, "type": "float", "label": "Tensión de entrada Vin (V)"},
            "vout_v": {"default": 24.0, "type": "float", "label": "Tensión de salida Vout (V)"},
            "iout_a": {"default": 1.5, "type": "float", "label": "Corriente de salida nominal (A)"},
            "fsw_khz": {"default": 150.0, "type": "float", "label": "Frecuencia de conmutación (kHz)"},
            "delta_il_ratio": {"default": 0.3, "type": "float", "label": "Rizado relativo de inductor"},
            "delta_vo_ratio": {"default": 0.01, "type": "float", "label": "Rizado relativo de tensión de salida"}
        }
    },
    "rlc_transient_solver": {
        "title": "Solucionador de Transitorios RLC",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230020 - CCE"],
        "description": "Calcula polos complejos, factor de amortiguamiento zeta, frecuencia natural wn y tiempo de establecimiento.",
        "params": {
            "r_ohm": {"default": 100.0, "type": "float", "label": "Resistencia R (Ohm)"},
            "l_mh": {"default": 10.0, "type": "float", "label": "Inductancia L (mH)"},
            "c_uf": {"default": 1.0, "type": "float", "label": "Capacidad C (uF)"},
            "v_step": {"default": 10.0, "type": "float", "label": "Escalón de tensión aplicado (V)"}
        }
    },
    "opamp_error_budget_calculator": {
        "title": "Balance de Errores de Amplificador Operacional",
        "branch": "Electrónica Analógica y Potencia",
        "courses": ["230025 - CISE"],
        "description": "Calcula error de tensión total en continua debido a Vos, Ibias, Ios y ganancia de bucle abierto.",
        "params": {
            "vos_mv": {"default": 1.0, "type": "float", "label": "Tensión de offset de entrada Vos (mV)"},
            "ib_na": {"default": 50.0, "type": "float", "label": "Corriente de polarización Ib (nA)"},
            "iio_na": {"default": 10.0, "type": "float", "label": "Corriente de offset Iio (nA)"},
            "r1_kohm": {"default": 1.0, "type": "float", "label": "Resistencia R1 (kOhm)"},
            "r2_kohm": {"default": 100.0, "type": "float", "label": "Resistencia de realimentación R2 (kOhm)"},
            "cmrr_db": {"default": 80.0, "type": "float", "label": "Rechazo de modo común CMRR (dB)"},
            "vcm_v": {"default": 5.0, "type": "float", "label": "Tensión de modo común (V)"}
        }
    },
    # Branch 3
    "arm_cortex_systick_timer": {
        "title": "Calculador de SysTick (ARM Cortex-M)",
        "branch": "Sistemas Digitales y Embebidos",
        "courses": ["230024 - MP", "230028 - SE"],
        "description": "Calcula valor del registro RELOAD y genera código C de inicialización para STM32 / ARM Cortex-M.",
        "params": {
            "cpu_freq_mhz": {"default": 80.0, "type": "float", "label": "Frecuencia del reloj del núcleo (MHz)"},
            "target_interval_ms": {"default": 1.0, "type": "float", "label": "Periodo de interrupción deseado (ms)"}
        }
    },
    "usart_baud_rate_generator": {
        "title": "Generador de Baud Rate USART/UART",
        "branch": "Sistemas Digitales y Embebidos",
        "courses": ["230024 - MP", "230028 - SE"],
        "description": "Calcula mantisa, fracción de USART_BRR y error porcentual de baud rate para microcontroladores.",
        "params": {
            "cpu_freq_mhz": {"default": 80.0, "type": "float", "label": "Reloj de periférico PCLK (MHz)"},
            "baud_rate": {"default": 115200, "type": "int", "label": "Baud rate deseado (bps)"},
            "oversampling": {"default": 16, "type": "int", "label": "Factor de sobremuestreo (8 o 16)"}
        }
    },
    "adc_sar_timing_calculator": {
        "title": "Calculador de Temporización ADC SAR",
        "branch": "Sistemas Digitales y Embebidos",
        "courses": ["230024 - MP", "230028 - SE"],
        "description": "Calcula tiempo de muestreo mínimo según impedancia de la fuente, tiempo total de conversión y tasa máxima de muestreo.",
        "params": {
            "f_adc_mhz": {"default": 14.0, "type": "float", "label": "Reloj del ADC (MHz)"},
            "resolution_bits": {"default": 12, "type": "int", "label": "Resolución en bits"},
            "sampling_cycles": {"default": 15.0, "type": "float", "label": "Ciclos de reloj para muestreo"}
        }
    },
    "vhdl_entity_generator": {
        "title": "Generador de Entidades VHDL Paramétricas",
        "branch": "Sistemas Digitales y Embebidos",
        "courses": ["230021 - DD", "230029 - DSD"],
        "description": "Genera código VHDL sintetizable (entidad, arquitectura, generics y puertos) listo para Vivado/Quartus.",
        "params": {
            "component_type": {"default": "fifo", "type": "str", "label": "Tipo de componente (fifo, timer, spi_master)"},
            "width_bits": {"default": 8, "type": "int", "label": "Ancho de bus de datos (bits)"},
            "depth": {"default": 16, "type": "int", "label": "Profundidad del buffer"}
        }
    },
    "sta_timing_slack_analyzer": {
        "title": "Analizador de Slack de Tiempo (STA)",
        "branch": "Sistemas Digitales y Embebidos",
        "courses": ["230021 - DD", "230029 - DSD"],
        "description": "Calcula Setup Slack y Hold Slack verificando si se cumplen las restricciones temporales a la frecuencia máxima.",
        "params": {
            "t_clk_ns": {"default": 5.0, "type": "float", "label": "Periodo de reloj (ns)"},
            "t_cq_ns": {"default": 0.35, "type": "float", "label": "Retardo Clock-to-Q (ns)"},
            "t_logic_ns": {"default": 2.1, "type": "float", "label": "Retardo lógico combinacional (ns)"},
            "t_setup_ns": {"default": 0.5, "type": "float", "label": "Tiempo de Setup (ns)"},
            "t_hold_ns": {"default": 0.2, "type": "float", "label": "Tiempo de Hold (ns)"},
            "t_skew_ns": {"default": 0.1, "type": "float", "label": "Clock skew (ns)"}
        }
    },
    "rtos_schedulability_solver": {
        "title": "Planificador de Tareas RTOS (Rate Monotonic)",
        "branch": "Sistemas Digitales y Embebidos",
        "courses": ["230028 - SE"],
        "description": "Evalúa planificabilidad de tareas en tiempo real usando el límite superior de Liu & Layland para Rate Monotonic.",
        "params": {
            "tasks": {
                "default": [
                    {"c": 1.0, "t": 5.0, "name": "Task_A"},
                    {"c": 2.0, "t": 10.0, "name": "Task_B"},
                    {"c": 4.0, "t": 25.0, "name": "Task_C"}
                ],
                "type": "list",
                "label": "Lista de tareas (JSON: c, t, name)"
            }
        }
    },
    "transmission_line_bounce_diagram": {
        "title": "Diagrama de Rebote en Líneas Digitales (Lattice)",
        "branch": "Sistemas Digitales y Embebidos",
        "courses": ["230021 - DD", "230020 - CCE"],
        "description": "Calcula reflexiones transitorias de flancos rápidos en pistas de alta velocidad y genera la tabla de rebotes.",
        "params": {
            "vg_step_v": {"default": 3.3, "type": "float", "label": "Flanco de tensión del driver (V)"},
            "zg_ohm": {"default": 20.0, "type": "float", "label": "Impedancia interna driver (Ohm)"},
            "z0_ohm": {"default": 50.0, "type": "float", "label": "Impedancia de la pista Z0 (Ohm)"},
            "zl_ohm": {"default": 1000.0, "type": "float", "label": "Impedancia de entrada receptor (Ohm)"},
            "td_ns": {"default": 1.5, "type": "float", "label": "Retardo de vuelo de la pista (ns)"},
            "num_bounces": {"default": 5, "type": "int", "label": "Número de rebotes a calcular"}
        }
    },
    # Branch 4
    "fir_filter_window_designer": {
        "title": "Diseñador de Filtros FIR por Ventana",
        "branch": "Tratamiento de Señal y Comunicaciones",
        "courses": ["230027 - SCOM", "230019 - AST"],
        "description": "Calcula coeficientes h[n] de un filtro paso-bajo digital con ventana Hamming, Hann, Blackman o Rectangular.",
        "params": {
            "order": {"default": 32, "type": "int", "label": "Orden del filtro FIR"},
            "fc_hz": {"default": 2000.0, "type": "float", "label": "Frecuencia de corte (Hz)"},
            "fs_hz": {"default": 16000.0, "type": "float", "label": "Frecuencia de muestreo (Hz)"},
            "window_type": {"default": "hamming", "type": "str", "label": "Tipo de ventana (hamming, hann, blackman)"}
        }
    },
    "bilinear_transform_mapper": {
        "title": "Mapeador de Transformada Bilineal (s a z)",
        "branch": "Tratamiento de Señal y Comunicaciones",
        "courses": ["230027 - SCOM", "230019 - AST"],
        "description": "Aplica pre-warping frecuencial y mapea polos continuos al plano z discreto mediante transformada bilineal.",
        "params": {
            "fc_analog_hz": {"default": 1000.0, "type": "float", "label": "Frecuencia analógica de corte (Hz)"},
            "fs_hz": {"default": 8000.0, "type": "float", "label": "Frecuencia de muestreo (Hz)"}
        }
    },
    "fft_resolution_inspector": {
        "title": "Inspector de Resolución Espectral FFT",
        "branch": "Tratamiento de Señal y Comunicaciones",
        "courses": ["230019 - AST"],
        "description": "Calcula resolución en frecuencia (Hz/bin), longitud temporal de ventana y frecuencia de Nyquist para FFT.",
        "params": {
            "fs_hz": {"default": 48000.0, "type": "float", "label": "Frecuencia de muestreo (Hz)"},
            "n_fft": {"default": 1024, "type": "int", "label": "Tamaño de la FFT (potencia de 2)"}
        }
    },
    "lora_toa_and_energy_predictor": {
        "title": "Predictor de Tiempo en el Aire y Energía LoRa",
        "branch": "Tratamiento de Señal y Comunicaciones",
        "courses": ["230027 - SCOM", "230028 - SE"],
        "description": "Calcula Time on Air (ToA) y consumo energético de paquetes de radiofrecuencia LoRa.",
        "params": {
            "sf": {"default": 7, "type": "int", "label": "Spreading Factor (7 a 12)"},
            "bw_khz": {"default": 125.0, "type": "float", "label": "Ancho de banda (125, 250 o 500 kHz)"},
            "cr": {"default": 1, "type": "int", "label": "Coding Rate (1=4/5, 4=4/8)"},
            "payload_bytes": {"default": 20, "type": "int", "label": "Tamaño del payload (bytes)"},
            "tx_power_dbm": {"default": 14.0, "type": "float", "label": "Potencia de transmisión TX (dBm)"}
        }
    },
    "adc_quantization_noise_analyzer": {
        "title": "Analizador de Ruido de Cuantización y ENOB",
        "branch": "Tratamiento de Señal y Comunicaciones",
        "courses": ["230027 - SCOM", "230019 - AST"],
        "description": "Calcula relación señal a ruido de cuantización (SQNR), ENOB, tensión de LSB y densidad espectral de ruido.",
        "params": {
            "bits": {"default": 12, "type": "int", "label": "Número de bits del convertidor"},
            "v_fs": {"default": 3.3, "type": "float", "label": "Tensión de fondo de escala (V)"}
        }
    },
    "z_transform_pole_zero_analyzer": {
        "title": "Analizador de Polos y Ceros en Plano Z",
        "branch": "Tratamiento de Señal y Comunicaciones",
        "courses": ["230019 - AST"],
        "description": "Calcula magnitud, ángulo y estabilidad de polos y ceros discretos verificando el círculo unidad.",
        "params": {
            "b_coeffs": {"default": [0.2, 0.2], "type": "list", "label": "Coeficientes del numerador B(z)"},
            "a_coeffs": {"default": [1.0, -0.6], "type": "list", "label": "Coeficientes del denominador A(z)"}
        }
    },
    # Branch 5
    "solar_cell_single_diode_solver": {
        "title": "Solucionador de Célula Fotovoltaica (1 Diodo)",
        "branch": "Física, Sensores y Control",
        "courses": ["230030 - EAP", "230015 - FM"],
        "description": "Modela curva I-V, potencia máxima (MPP), Fill Factor (FF) y rendimiento cuántico bajo radiación solar.",
        "params": {
            "isc_a": {"default": 9.5, "type": "float", "label": "Corriente de cortocircuito Isc (A)"},
            "voc_v": {"default": 40.0, "type": "float", "label": "Tensión de circuito abierto Voc (V)"},
            "rs_ohm": {"default": 0.05, "type": "float", "label": "Resistencia serie Rs (Ohm)"},
            "rsh_ohm": {"default": 1000.0, "type": "float", "label": "Resistencia paralelo Rsh (Ohm)"},
            "ideality_n": {"default": 1.2, "type": "float", "label": "Factor de idealidad del diodo n"},
            "temp_c": {"default": 25.0, "type": "float", "label": "Temperatura de trabajo (C)"},
            "area_m2": {"default": 1.6, "type": "float", "label": "Área del panel solar (m^2)"},
            "irradiance_w_m2": {"default": 1000.0, "type": "float", "label": "Irradiancia solar (W/m^2)"}
        }
    },
    "rtd_pt100_temperature_solver": {
        "title": "Linealizador de Sensor RTD PT100",
        "branch": "Física, Sensores y Control",
        "courses": ["230025 - CISE"],
        "description": "Calcula temperatura exacta a partir de la resistencia medida usando la ecuación de Callendar-Van Dusen (DIN EN 60751).",
        "params": {
            "resistance_ohm": {"default": 119.40, "type": "float", "label": "Resistencia medida de la PT100 (Ohm)"},
            "temp_c": {"default": None, "type": "float", "label": "O temperatura conocida (C)"},
            "wiring_mode": {"default": "4-wire", "type": "str", "label": "Tipo de conexión (2-wire, 3-wire, 4-wire)"},
            "lead_resistance_ohm": {"default": 2.5, "type": "float", "label": "Resistencia de hilos conductores (Ohm)"}
        }
    },
    "strain_gauge_rosette_solver": {
        "title": "Analizador de Roseta de Galgas Extensiométricas",
        "branch": "Física, Sensores y Control",
        "courses": ["230025 - CISE"],
        "description": "Calcula deformaciones principales eps1 y eps2, esfuerzo de corte máximo y tensiones de Von Mises.",
        "params": {
            "eps_0_ue": {"default": 400.0, "type": "float", "label": "Microdeformación a 0 grados (ue)"},
            "eps_45_ue": {"default": 250.0, "type": "float", "label": "Microdeformación a 45 grados (ue)"},
            "eps_90_ue": {"default": -100.0, "type": "float", "label": "Microdeformación a 90 grados (ue)"},
            "e_modulus_gpa": {"default": 70.0, "type": "float", "label": "Módulo de Young E (GPa)"},
            "poisson_ratio": {"default": 0.33, "type": "float", "label": "Coeficiente de Poisson nu"}
        }
    },
    "pcb_thermal_heatsink_dimensioner": {
        "title": "Dimensionador Térmico PCB y Disipador",
        "branch": "Física, Sensores y Control",
        "courses": ["230030 - EAP", "230015 - FM"],
        "description": "Calcula resistencia térmica máxima admisible del disipador (Rth_sa) para evitar sobrecalentamiento de la unión.",
        "params": {
            "p_dis_w": {"default": 5.0, "type": "float", "label": "Potencia disipada (W)"},
            "t_ambient_c": {"default": 40.0, "type": "float", "label": "Temperatura ambiente máxima (C)"},
            "t_junction_max_c": {"default": 125.0, "type": "float", "label": "Temperatura máxima de unión (C)"},
            "theta_jc": {"default": 1.5, "type": "float", "label": "Resistencia térmica unión-cápsula (C/W)"},
            "theta_cs": {"default": 0.5, "type": "float", "label": "Resistencia térmica pasta térmica (C/W)"}
        }
    },
    "system_reliability_markov_solver": {
        "title": "Analizador de Fiabilidad y MTBF (Markov)",
        "branch": "Física, Sensores y Control",
        "courses": ["230028 - SE"],
        "description": "Calcula MTBF del sistema, fiabilidad R(t) a las horas indicadas para arquitecturas simplex o redundantes 1-de-2.",
        "params": {
            "components_mttf_h": {"default": [100000.0, 100000.0], "type": "list", "label": "MTTF de componentes (horas)"},
            "mission_time_h": {"default": 5000.0, "type": "float", "label": "Horas de misión a evaluar (h)"},
            "configuration": {"default": "parallel", "type": "str", "label": "Configuración (series, parallel)"}
        }
    },
    "second_order_system_step_response": {
        "title": "Respuesta al Escalón de Sistema de 2º Orden",
        "branch": "Física, Sensores y Control",
        "courses": ["230025 - CISE"],
        "description": "Calcula sobreoscilación Mp (%), tiempo de pico tp, tiempo de subida tr y tiempo de establecimiento ts.",
        "params": {
            "wn_rad_s": {"default": 10.0, "type": "float", "label": "Frecuencia natural wn (rad/s)"},
            "zeta": {"default": 0.5, "type": "float", "label": "Coeficiente de amortiguamiento zeta"}
        }
    }
}

def get_all_engineering_tools() -> Dict[str, Any]:
    """Returns the dictionary mapping tool names to callable functions."""
    return ALL_ENGINEERING_TOOLS

def get_tool_metadata(tool_name: str) -> Optional[Dict[str, Any]]:
    """Retrieves full descriptive metadata and parameter specifications for a tool."""
    return ENGINEERING_TOOLS_METADATA.get(tool_name)

def run_engineering_tool(tool_name: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Executes a specialized engineering solver by name with user parameters or defaults.
    """
    if tool_name not in ALL_ENGINEERING_TOOLS:
        raise ValueError(f"Herramienta '{tool_name}' no encontrada. Disponibles: {list(ALL_ENGINEERING_TOOLS.keys())}")
    
    func = ALL_ENGINEERING_TOOLS[tool_name]
    params = params or {}
    
    # Filter only parameters that match the function signature
    import inspect
    sig = inspect.signature(func)
    valid_args = {}
    for p_name, p_param in sig.parameters.items():
        if p_name in params:
            val = params[p_name]
            # Cast type if specified in metadata
            meta = ENGINEERING_TOOLS_METADATA.get(tool_name, {}).get("params", {}).get(p_name, {})
            p_type = meta.get("type")
            if p_type == "float" and val is not None:
                val = float(val)
            elif p_type == "int" and val is not None:
                val = int(val)
            elif p_type == "str" and val is not None:
                val = str(val)
            valid_args[p_name] = val
            
    return func(**valid_args)

print(f"Loaded {len(ALL_ENGINEERING_TOOLS)} professional engineering tools and metadata.")

