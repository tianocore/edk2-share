@REM
@REM CX_Freeze 4.0.1 has been integrated into python as a script.
@REM After Cx_Freeze 4.0.1 installed, cxfreeze.bat is put into <Python2.5 PATH>\scripts\ 
@REM

@echo off
pushd .
cd %~dp0

if not defined PYTHONFREEZE_PATH (
  echo !!!ERROR!!! Please set PYTHONFREEZE_PATH macro for path of cxfreeze.bat. For example: set PYTHONFREEZE_PATH=c:\Python25\scripts\
  @goto end
)

%PYTHONFREEZE_PATH%\cxfreeze.bat --include-modules=encodings.utf_16 --base=Win32GUI --install-dir ..\bin_win32\ packagedocapp.pyw 

:end