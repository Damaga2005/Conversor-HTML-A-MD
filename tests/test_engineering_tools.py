# -*- coding: utf-8 -*-
"""
Automated unit tests for the 37 GREELEC Specialized Engineering Solvers:
- Tests all 37 tools across 5 engineering branches.
- Verifies input validation, default execution, and parameter parsing.
- Verifies physical / numerical bounds and correctness of engineering models.
- Tests UPCDegreeEngine integration and CLI bridge.
"""
import pytest
import math
from typing import Dict, Any

import engineering_tools_suite as ets
from upc_degree_engine import UPCDegreeEngine

@pytest.fixture(scope="module")
def engine():
    return UPCDegreeEngine()

def test_tool_count_and_metadata_integrity():
    tools = ets.get_all_engineering_tools()
    metadata = ets.ENGINEERING_TOOLS_METADATA
    assert len(tools) == 37, f"Expected 37 tools, got {len(tools)}"
    assert len(metadata) == 37, f"Expected 37 metadata entries, got {len(metadata)}"
    
    for tool_name, func in tools.items():
        assert callable(func), f"{tool_name} is not callable"
        assert tool_name in metadata, f"Metadata missing for {tool_name}"
        meta = metadata[tool_name]
        assert "title" in meta and len(meta["title"]) > 3
        assert "branch" in meta and len(meta["branch"]) > 3
        assert "courses" in meta and len(meta["courses"]) > 0
        assert "description" in meta and len(meta["description"]) > 10
        assert "params" in meta and isinstance(meta["params"], dict)

def test_all_37_tools_default_execution():
    """Verify that every single tool runs with its default arguments without throwing an exception."""
    for tool_name in ets.ALL_ENGINEERING_TOOLS:
        res = ets.run_engineering_tool(tool_name)
        assert isinstance(res, dict), f"{tool_name} must return a dictionary"
        assert len(res) > 0, f"{tool_name} returned an empty dictionary"
        assert "error" not in res, f"{tool_name} returned error: {res.get('error')}"

def test_rf_microwave_tools():
    # 1. Microstrip
    ms = ets.microstrip_synthesizer(z0_target=50.0, er=4.4, h_mm=1.6)
    assert 2.5 <= ms["trace_width_mm"] <= 3.5
    assert 3.0 <= ms["effective_er"] <= 4.0
    
    # 2. Smith Chart Stub Matcher
    sm = ets.smith_chart_stub_matcher(zl_real=25.0, zl_imag=-50.0, z0=50.0)
    assert sm["vswr"] > 1.0
    assert 0.0 <= sm["distance_d_wavelengths"] <= 0.5
    
    # 3. Quarter Wave
    qw = ets.quarter_wave_transformer(zl_real=100.0, z0=50.0, freq_hz=1e9)
    assert math.isclose(qw["z_transformer_ohm"], math.sqrt(50.0 * 100.0), rel_tol=1e-2)
    
    # 4. Friis Cascade
    fc = ets.friis_cascade_analyzer()
    assert fc["total_gain_db"] > 25.0
    assert fc["total_noise_figure_db"] < 2.5
    
    # 5. Wilkinson
    wd = ets.wilkinson_divider_designer(z0=50.0, freq_hz=2.4e9)
    assert math.isclose(wd["branch_impedance_ohm"], 50.0 * math.sqrt(2.0), rel_tol=1e-2)
    assert wd["isolation_resistor_ohm"] == 100.0
    
    # 6. Coaxial
    cx = ets.coaxial_cable_solver(inner_diam_mm=0.9, outer_diam_mm=2.95, er=2.1)
    assert 45.0 <= cx["characteristic_impedance_ohm"] <= 55.0
    
    # 7. Link Budget
    lb = ets.link_budget_calculator(ptx_dbm=14.0, distance_km=5.0, freq_mhz=868.0)
    assert "received_power_dbm" in lb
    assert lb["link_margin_db"] > 0
    
    # 8. Rectangular Waveguide
    wg = ets.rectangular_waveguide_modes(a_mm=22.86, b_mm=10.16)
    assert 6.0 <= wg["cutoff_te10_ghz"] <= 7.0
    assert "recommended_band_ghz" in wg
    
    # 9. Shannon Capacity
    sh = ets.shannon_channel_capacity(bandwidth_hz=20e6, snr_db=30.0)
    assert sh["channel_capacity_mbps"] > 150.0
    
    # 10. PLL Loop Filter
    pll = ets.pll_loop_filter_synthesizer(f_ref_hz=10e6, f_out_hz=2.4e9, loop_bw_hz=100e3)
    assert pll["divider_ratio_n"] == 240
    assert pll["c1_pf"] > 0
    assert pll["c2_pf"] > 0
    assert pll["r2_ohm"] > 0

def test_analog_and_power_tools():
    # 1. BJT Designer
    bjt = ets.bjt_amplifier_designer(vcc=12.0, ic_ma=2.0, vce_v=6.0, beta=150.0)
    assert bjt["rc_kohm"] > 0
    assert bjt["re_kohm"] > 0
    assert bjt["voltage_gain_av"] < 0
    
    # 2. MOSFET Designer
    mos = ets.mosfet_amplifier_designer(vdd=5.0, id_ma=1.0, vds_v=2.5)
    assert mos["vgs_v"] > 0
    assert mos["voltage_gain_av"] < 0
    
    # 3. Differential Pair
    diff = ets.differential_pair_analyzer(vcc=15.0, vee=-15.0, itail_ma=2.0, rc_kohm=10.0)
    assert diff["diff_gain_db"] > 0
    assert diff["cmrr_db"] > 40.0
    
    # 4. Sallen-Key
    sk = ets.sallen_key_filter_synthesizer(filter_type="lowpass", approx_type="butterworth", fc_hz=1000.0)
    assert sk["r1_r2_kohm"] > 0
    
    # 5. Buck Converter
    buck = ets.buck_converter_synthesizer(vin_v=24.0, vout_v=5.0, iout_a=3.0, fs_khz=200.0)
    assert 0.15 <= buck["nominal_duty_cycle"] <= 0.25
    assert buck["inductor_uh"] > 0
    
    # 6. Boost Converter
    boost = ets.boost_converter_synthesizer(vin_v=12.0, vout_v=24.0, iout_a=1.5, fs_khz=150.0)
    assert 0.45 <= boost["nominal_duty_cycle"] <= 0.55
    assert boost["inductor_uh"] > 0
    
    # 7. RLC Transient
    rlc = ets.rlc_transient_solver(r_ohm=100.0, l_mh=10.0, c_uf=1.0)
    assert rlc["damping_ratio_zeta"] > 0
    assert rlc["undamped_frequency_wn_rad_s"] > 0
    
    # 8. OpAmp Error Budget
    op = ets.opamp_error_budget_calculator(vos_mv=1.0, ib_na=50.0, r1_kohm=1.0, r2_kohm=100.0)
    assert op["closed_loop_gain"] > 0
    assert op["total_output_error_uncomp_mv"] > 0

def test_digital_and_embedded_tools():
    # 1. ARM SysTick
    st = ets.arm_cortex_systick_timer(cpu_freq_mhz=80.0, target_interval_ms=1.0)
    assert st["reload_value_dec"] > 0
    assert st["fits_24bit_timer"] is True
    
    # 2. USART Baud Rate
    uart = ets.usart_baud_rate_generator(cpu_freq_mhz=80.0, baud_rate=115200)
    assert abs(uart["error_percentage"]) < 1.0
    assert "brr_register_hex" in uart
    
    # 3. ADC SAR Timing
    adc = ets.adc_sar_timing_calculator(f_adc_mhz=14.0, resolution_bits=12)
    assert adc["conversion_time_us"] > 0
    assert adc["max_sampling_rate_ksps"] > 0
    
    # 4. VHDL Generator
    vhdl = ets.vhdl_entity_generator(component_type="fifo", width_bits=8, depth=16)
    assert "vhdl_code" in vhdl
    assert "entity sync_fifo is" in vhdl["vhdl_code"]
    
    # 5. STA Timing Slack
    sta = ets.sta_timing_slack_analyzer(t_clk_ns=5.0, t_cq_ns=0.35, t_logic_ns=2.1, t_setup_ns=0.5)
    assert sta["setup_slack_ns"] > 0
    assert sta["setup_timing_met"] is True
    
    # 6. RTOS Schedulability
    rtos = ets.rtos_schedulability_solver()
    assert rtos["total_utilization"] > 0
    assert rtos["is_edf_schedulable"] is True
    
    # 7. Transmission Line Bounce
    tl = ets.transmission_line_bounce_diagram(vg_step_v=3.3, zg_ohm=20.0, z0_ohm=50.0, zl_ohm=1000.0)
    assert len(tl["bounce_timeline"]) >= 10
    assert math.isclose(tl["steady_state_v"], 3.3 * (1000.0 / 1020.0), rel_tol=1e-2)

def test_dsp_and_signal_tools():
    # 1. FIR Filter
    fir = ets.fir_filter_window_designer(order=32, fc_hz=2000.0, fs_hz=16000.0, window_type="hamming")
    assert len(fir["coefficients"]) == 33
    assert math.isclose(sum(fir["coefficients"]), 1.0, rel_tol=1e-1)
    
    # 2. Bilinear Transform
    bl = ets.bilinear_transform_mapper(fc_analog_hz=1000.0, fs_hz=8000.0)
    assert bl["digital_omega_rad"] > 0
    assert bl["prewarped_freq_hz"] > 0
    
    # 3. FFT Resolution
    fft = ets.fft_resolution_inspector(fs_hz=48000.0, n_fft=1024)
    assert math.isclose(fft["frequency_bin_width_hz"], 48000.0 / 1024, rel_tol=1e-3)
    assert fft["nyquist_limit_hz"] == 24000.0
    
    # 4. LoRa ToA
    lora = ets.lora_toa_and_energy_predictor(sf=7, bw_khz=125.0, payload_bytes=20)
    assert lora["total_time_on_air_ms"] > 0
    assert lora["battery_longevity_years"] > 0
    
    # 5. ADC Quantization Noise
    q_noise = ets.adc_quantization_noise_analyzer(bits=12, v_fs=3.3)
    assert math.isclose(q_noise["theoretical_sqnr_db"], 1.76 + 6.02 * 12, rel_tol=1e-2)
    assert q_noise["lsb_step_mv"] > 0
    
    # 6. Z-Transform Analyzer
    zt = ets.z_transform_pole_zero_analyzer()
    assert "dc_gain_at_z1" in zt
    assert "nyquist_gain_at_z_minus1" in zt

def test_physics_sensors_control_tools():
    # 1. Solar Cell
    sc = ets.solar_cell_single_diode_solver(isc_a=9.5, voc_v=40.0)
    assert sc["max_power_mpp_w"] > 0
    assert 0.7 <= sc["fill_factor"] <= 0.85
    
    # 2. RTD PT100
    rtd = ets.rtd_pt100_temperature_solver(resistance_ohm=119.4)
    assert math.isclose(rtd["calculated_temperature_c"], 50.0, abs_tol=0.1)
    
    # 3. Strain Gauge
    sg = ets.strain_gauge_rosette_solver(eps_0_ue=400.0, eps_45_ue=250.0, eps_90_ue=-100.0)
    assert sg["principal_stress_1_mpa"] > 0
    assert sg["principal_strain_1_ue"] > sg["principal_strain_2_ue"]
    
    # 4. Thermal Dimensioner
    th = ets.pcb_thermal_heatsink_dimensioner(p_dis_w=5.0, t_ambient_c=40.0, t_junction_max_c=125.0)
    assert th["max_allowable_heatsink_rth_sa_c_w"] > 0
    assert th["is_passive_cooling_feasible"] is True
    
    # 5. Markov Reliability
    rel = ets.system_reliability_markov_solver(components_mttf_h=[100000.0, 100000.0], mission_time_h=5000.0)
    assert rel["system_reliability"] > 0.95
    assert rel["system_mtbf_hours"] > 100000.0
    
    # 6. Second Order Response
    sec = ets.second_order_system_step_response(wn_rad_s=10.0, zeta=0.5)
    assert sec["peak_overshoot_percentage"] > 15.0
    assert sec["classification"] == "Subamortiguado (Underdamped)"

def test_engine_integration_bridge(engine):
    tools = engine.get_engineering_tools()
    assert len(tools) == 37
    
    meta = engine.get_engineering_tool_metadata("microstrip_synthesizer")
    assert meta is not None
    assert meta["title"] == "Sintetizador de Líneas Microstrip"
    
    # Run tool via engine
    res = engine.run_engineering_tool("shannon_channel_capacity", {"bandwidth_hz": 10e6, "snr_db": 20.0})
    assert "channel_capacity_mbps" in res
    assert res["channel_capacity_mbps"] > 60.0
