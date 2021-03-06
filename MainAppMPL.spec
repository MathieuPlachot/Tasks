# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None


a = Analysis(['Pomo.py'],
             pathex=['C:\\Users\\253751\\OneDrive - Alstom\\GITRepo\\PomodoroApp'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['conf'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
		  *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          [],
          name='PomoApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)

coll = COLLECT(exe,
          a.binaries,
          a.zipfiles,
          a.datas,
          strip=False,
          upx=True,
          name='PomoApp')