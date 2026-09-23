# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['conversor_html_notebooklm.py'],
    pathex=[],
    datas=[
        ('dist_course_md/_Problemas_Examen_Resueltos.md', '.'),
        ('dist_course_md/_Examenes_Finales_Oficiales_UPC.md', '.'),
        ('dist_course_md/Laboratorio_Virtual_Sensores.html', '.'),
        ('Laboratorio_Virtual_Sensores.html', '.'),
        ('dist_course_md/_Formulario_Oficial_Examen.md', '.'),
        ('dist_course_md/_Glosario_Conceptos_Clave.md', '.'),
        ('dist_course_md/_Gran_Indice_Sistemes_de_Mesura.md', '.'),
        ('data/upc_curriculum_master.json', 'data'),
        ('data/all_upc_compulsory_guides.json', 'data'),
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='conversor_html_notebooklm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='conversor_html_notebooklm',
)
