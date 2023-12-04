# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/compile.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/venv/Lib/site-packages/fast_fs/__init__.py', '.'), ('C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/venv/Lib/site-packages/fast_fs/fast_fs.cp312-win_amd64.pyd', '.'), ('C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/venv/Lib/site-packages/fast_fs/__pycache__', '__pycache__/')],
    hiddenimports=['fast fs'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Raisfeld encrypter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\raisf\\Desktop\\projects\\Raisfeld_Encrypter\\raisfeld-encrypter-website\\static\\icon.ico'],
)
