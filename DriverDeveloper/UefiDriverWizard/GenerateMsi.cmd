@REM @file
@REM   Batch file to convert UEFI Driver Wizard to EXE and MSI
@REM
@REM Copyright (c) 2012, Intel Corporation. All rights reserved.<BR>
@REM This program and the accompanying materials
@REM are licensed and made available under the terms and conditions of the BSD License
@REM which accompanies this distribution.  The full text of the license may be found at
@REM http://opensource.org/licenses/bsd-license.php
@REM
@REM THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
@REM WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
@REM

@echo off

SETLOCAL

@REM
@REM Set locals for paths to PyInstaller and Windows Installer XML
@REM
SET PYINSTALLER_PATH=c:/pyinstaller-1.5.1
SET WIX_PATH="c:\Program Files (x86)\Windows Installer XML v3.5\bin"

@REM
@REM Verify path PyInstaller
@REM
if exist %PYINSTALLER_PATH%/Configure.py goto continue1
echo ERROR: PyInstaller path is not valid.  Set PYINSTALLER_PATH in this script
goto errorexit
:continue1

@REM
@REM Verify path to Windows Installer XML
@REM
if exist %WIX_PATH%\candle.exe if exist %WIX_PATH%\light.exe goto continue2
echo ERROR: Windows Installer XML path is not valid.  Set WIX_PATH in this script
goto errorexit
:continue2

@REM
@REM Use PyInstaller to Convert UEFI Driver Wizard Python application to an EXE
@REM
python %PYINSTALLER_PATH%/Configure.py
if not errorlevel 1 goto continue3
echo ERROR: Python is not in PATH
goto errorexit
:continue3
python %PYINSTALLER_PATH%/Makespec.py --onefile --icon Logo.ico --windowed -n UefiDriverWizard.Generated launch.py
python %PYINSTALLER_PATH%/Build.py UefiDriverWizard.spec

@REM
@REM Use Windows Installer XML 3.5 to Convert UEFI Driver Wizard Python application to an EXE
@REM
%WIX_PATH%\candle UefiDriverWizard.wxs
%WIX_PATH%\light  UefiDriverWizard.wixobj -cultures:en-US -ext WixUIExtension.dll

:errorexit

ENDLOCAL

@echo on