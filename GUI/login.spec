# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['login.py'],
             pathex=['E:\\chaixin\\02_working\\04_automation\\03_daido-demo\\demo1_0722\\GUI'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
			 
a.datas += (('icon_logo','E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//logo.png','DATA'),('icon_comitX','E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//ComitX.png','DATA'),('icon_control','E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//icon_control.png','DATA'))

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('icon_logo','E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//logo.png','DATA')],
          name='test',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None)