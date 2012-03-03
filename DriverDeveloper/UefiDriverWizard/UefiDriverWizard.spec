## @file
# PyInstaller SPEC file used to generate Windows EXE for UEFI Driver Wizard
#
# Copyright (c) 2012, Intel Corporation. All rights reserved.<BR>
#
# This program and the accompanying materials are licensed and made available 
# under the terms and conditions of the BSD License which accompanies this 
# distribution. The full text of the license may be found at 
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#
##

# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'launch.py'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries + [('Logo.png', 'Logo.png', 'DATA')] + Tree('Templates', 'Templates'),
          a.zipfiles,
          a.datas,
          name='UefiDriverWizard.exe',
          debug=False,
          strip=False,
          upx=True,
          console=False , 
          icon='Logo.ico'
          )
app = BUNDLE(exe, name='UefiDriverWizard.exe.app')
