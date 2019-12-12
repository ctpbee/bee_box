# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['bee_box.py'],
             pathex=['C:\\GIT\\bee_box',
             "C:\\GIT\\bee_box\\venv\\Lib\\site-packages\\shiboken2"],
             binaries=[],
             datas=[],
             hiddenimports=['PySide2.QtPrintSupport'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='bee_box',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='C:\\GIT\\bee_box\\beebox.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='bee_box')
