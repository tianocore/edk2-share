## @file
# Main entry point and code generator for UEFI Driver Wizard
#
# Copyright (c) 2012 - 2014, Intel Corporation. All rights reserved.<BR>
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

##
# Import Modules
#
import Config
import wx
import os
import sys
import uuid
import string
import TemplateString
import UefiDriverWizard
import UefiDriverWizardNewPackage
import UefiDriverWizardNewUefiDriver
import UefiDriverWizardNewProtocol
import UefiDriverWizardNewGuid
import UefiDriverWizardNewLibraryClass
import UefiDriverWizardUefiDriverWizard
import UefiDriverWizardUefiDriverModelOptionalFeatures
import UefiDriverWizardUefiDriverModelConsumedProtocols
import UefiDriverWizardUefiDriverModelProducedProtocols

##
# Extra imports only used by this file
#
import glob
import codecs

##
# Main class for this application
#
class MyApp(wx.App):
  def OnInit(self):
    frame = UefiDriverWizardUefiDriverWizard.UefiDriverWizardUefiDriverWizard (None)
    self.frame = frame
    self.SetTopWindow(frame)
    self.WorkspacePath = ''
    icon = wx.Icon(os.path.join(os.path.abspath(sys.path[0]), 'Logo.ico'), wx.BITMAP_TYPE_ICO)
#    image = wx.Image(os.path.join(os.path.abspath(sys.path[0]), 'Logo.png'), wx.BITMAP_TYPE_PNG)
#    image = image.Scale(40,40)
#    icon = wx.IconFromBitmap (image.ConvertToBitmap())
    frame.SetIcon(icon)
    frame.Show(True)
    if Config.WorkspacePath <> '':
      frame.LogMessageWindow.AppendText('\nWORKSPACE %s selected\n' % (Config.WorkspacePath))
    return True

  def VerifyWorkspacePackage(self, WorkspacePath, PackageFile, NewDirectory=None, NewFileName=None):
    if not os.path.isdir(WorkspacePath):
      return False, "WORKSPACE path %s is not a valid path." % (WorkspacePath)
    os.chdir (WorkspacePath)
    if os.path.normcase(os.path.abspath(os.curdir)) not in os.path.normcase(os.path.abspath(PackageFile)):
      return False, "Package DEC file %s is not in WORKSPACE path %s." % (PackageFile, WorkspacePath)
    if not os.path.isfile (PackageFile):
      return False, "Package DEC file %s not found." % (PackageFile)
    PackagePath = os.path.split(os.path.abspath(PackageFile))[0]
    os.chdir (PackagePath)
    if NewDirectory == None:
      return True, PackagePath
    if not os.path.exists (NewDirectory):
      os.makedirs (NewDirectory)
    if not os.path.isdir (NewDirectory):
      return False, "%s is not a directory." % (os.path.join(PackagePath, NewDirectory))
    if NewFileName == None:
      return True, os.path.normpath(os.path.join(PackagePath, NewDirectory))
    FileName = os.path.normpath(os.path.join(PackagePath, NewDirectory, NewFileName))
    if os.path.isfile (FileName):
      return False, "File %s already exists." % (FileName)
    return True, FileName

  def MixedCaseNameToDefineName(self, MixedCaseName):
    if MixedCaseName == '':
      return ''
    DefineName = ''
    Index = 0
    for Index in range(1,len(MixedCaseName)):
      DefineName += MixedCaseName[Index - 1]
      if MixedCaseName[Index - 1].islower() and MixedCaseName[Index].isupper():
        DefineName += '_'
    DefineName += MixedCaseName[Index]
    return DefineName.upper()

  def RegisteryGuidValueToStructure(self, GuidValue):
    ByteList = list(uuid.UUID(GuidValue).bytes)
    Bytes = []
    for Byte in ByteList:
      Bytes += [ord(Byte)]
    return '{0x%02x%02x%02x%02x, 0x%02x%02x, 0x%02x%02x, {0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x, 0x%02x}}' % tuple(Bytes)

  def ProcessTemplate(self, TemplateFileName, Dictionary, OutputFileName=None, Encoding=None):
    Contents = TemplateString.TemplateString()
    if Encoding == None:
      TemplateFile = open (os.path.join(sys.path[0], TemplateFileName))
    else:
      TemplateFile = codecs.open (os.path.join(sys.path[0], TemplateFileName), encoding=Encoding)
    Contents.Append(TemplateFile.read().replace('<<','${').replace('>>','}'), Dictionary)
    TemplateFile.close()
    if OutputFileName <> None:
      self.frame.LogMessageWindow.AppendText('  Create file %s\n' % (os.path.abspath(OutputFileName)))
      if Encoding == None:
        File = open (OutputFileName, 'w')
      else:
        File = codecs.open (OutputFileName, 'w', encoding=Encoding)
      File.write(Contents.String)
      File.close()
    return Contents.String

  def InsertLines(self, FileName, Pattern, NewLines):
    File = open (FileName, 'r')
    FileLines = File.readlines()
    File.close()

    NewFileLines = []
    Found = False
    Start = False
    for Line in FileLines:
      Content = Line.split('#')[0].strip()
      if Start and len(Content) > 0:
        if Content[0] == '[':
          NewFileLines = [''.join(NewFileLines).rstrip() + '\n']
          NewFileLines += NewLines + ['\n']
          Start = False
      if Pattern.strip().upper() in Content.upper():
        Found = True
        Start = True
      NewFileLines += [Line]
    if not Found:
      NewFileLines += [Pattern] + NewLines + ['\n']
    elif Start:
      NewFileLines = [''.join(NewFileLines).rstrip() + '\n']
      NewFileLines += NewLines + ['\n']

    self.frame.LogMessageWindow.AppendText('  Update file %s\n' % (os.path.abspath(FileName)))
    File = open (FileName, 'w')
    File.writelines (NewFileLines)
    File.close()

  def TextFieldNameValid(self, TextField, event):
    Name = str(event.GetString())
    ValidName = Name.translate(None, string.punctuation.translate (None,'._-') + ' ')
    if Name == ValidName:
      return Name
    Position = TextField.GetInsertionPoint()
    TextField.SetValue(ValidName)
    TextField.SetInsertionPoint(Position-1)
    return ValidName

  def TextFieldVersionValid(self, TextField, event):
    Version = str(event.GetString())
    if Version.count('.') > 1:
      Position = TextField.GetInsertionPoint()
      ValidVersion = Version[:Position-1] + Version[Position:]
      TextField.SetValue(ValidVersion)
      TextField.SetInsertionPoint(Position-1)
      return ValidVersion
    ValidVersion = Version.translate(None, string.letters + string.punctuation.translate (None,'.') + ' ')
    if Version == ValidVersion:
      return Version
    Position = TextField.GetInsertionPoint()
    TextField.SetValue(ValidVersion)
    TextField.SetInsertionPoint(Position-1)
    return ValidVersion

  def CreatePackage(self):
    try:
      if Config.PackageName == '':
        return False, "Package Name is not valid."
      try:
        Guid = uuid.UUID(Config.PackageGuidValue)
      except:
        return False, "Package GUID is not valid."
      if Config.PackageVersion == '':
        return False, "Package Version is not valid."
      try:
        Guid = uuid.UUID(Config.PlatformGuidValue)
      except:
        return False, "Platform GUID is not valid."

      SavedCurDir = os.curdir

      if not os.path.isdir(Config.WorkspacePath):
        return False, "WORKSPACE path %s is not a valid path." % (Config.WorkspacePath)
      os.chdir (Config.WorkspacePath)
      if os.path.normcase(os.path.abspath(os.curdir)) not in os.path.normcase(os.path.abspath(Config.PackagePath)):
        return False, "PackagePath %s is not in WORKSPACE path %s." % (Config.PackagePath, Config.WorkspacePath)
      if os.path.normcase(os.path.abspath(os.curdir)) == os.path.normcase(os.path.abspath(Config.PackagePath)):
        return False, "PackagePath %s is identical to WORKSPACE path %s." % (Config.PackagePath, Config.WorkspacePath)
      if not os.path.exists (Config.PackagePath):
        os.makedirs (Config.PackagePath)
      if not os.path.isdir (Config.PackagePath):
        return False, "PackagePath %s is not a directory in WORKSPACE %s." % (Config.PackagePath, Config.WorkspacePath)
      os.chdir (Config.PackagePath)
      for File in [Config.PackageName + '.dec', Config.PackageName + '.dsc']:
        if os.path.isfile (File):
          return False, "Package %s already exists." % (File)
      for Directory in ['Include', 'Include/Protocol', 'Include/Guid', 'Include/Library']:
        if not os.path.exists (Directory):
          os.makedirs (Directory)
        if not os.path.isdir (Directory):
          return False, "%s is not a directory." % (Directory)

      self.frame.LogMessageWindow.AppendText('\nCreate Package %s\n' % (Config.PackageName))

      Dictionary = {}
      Dictionary['SKIP']                 = []
      Dictionary['BriefDescription']     = 'TODO: Brief Description of Package %s' % (Config.PackageName)
      Dictionary['DetailedDescription']  = 'TODO: Detailed Description of Package %s' % (Config.PackageName)
      Dictionary['Copyright']            = 'TODO: Copyright for Pacvkage %s' % (Config.PackageName)
      Dictionary['License']              = 'TODO: License for Package %s' % (Config.PackageName)
      Dictionary['PackageName']          = Config.PackageName
      Dictionary['GUID_REGISTRY_FORMAT'] = Config.PackageGuidValue
      Dictionary['PackageVersionString'] = Config.PackageVersion

      self.ProcessTemplate('Templates/Package.dec', Dictionary, Config.PackageName + '.dec')

      Dictionary['GUID_REGISTRY_FORMAT'] = Config.PlatformGuidValue

      self.ProcessTemplate('Templates/Package.dsc', Dictionary, Config.PackageName + '.dsc')

      Config.PackageFile = os.path.join (Config.PackagePath, Config.PackageName + '.dec')

      os.chdir (SavedCurDir)

      return True, "Package %s created at %s" % (Config.PackageName, Config.PackageFile)
    except:
      return False, "Package creation failed"

  def CreatePackageByParams(self, PackagePath, PackageName, PackageGuidValue, PackageVersion, PlatformGuidValue):
    Config.PackagePath       = PackagePath
    Config.PackageName       = PackageName
    Config.PackageGuidValue  = PackageGuidValue
    Config.PackageVersion    = PackageVersion
    Config.PlatformGuidValue = PlatformGuidValue
    return self.CreatePackage()

  def CreateGuid(self):
    try:
      if Config.GuidIncludeName == '':
        return False, "GUID Include Name is not valid"
      try:
        Guid = uuid.UUID(Config.GuidValue)
      except:
        return False, "GUID is not valid."

      SavedCurDir = os.curdir
      Result, GuidFileName = self.VerifyWorkspacePackage (
                                    Config.WorkspacePath,
                                    Config.PackageFile,
                                    'Include/Guid',
                                    Config.GuidIncludeName + '.h'
                                    )
      if not Result:
        os.chdir (SavedCurDir)
        return Result, GuidFileName

      self.frame.LogMessageWindow.AppendText('\nCreate GUID %s\n' % (Config.GuidIncludeName))

      Dictionary = {}
      Dictionary['SKIP']                 = []
      Dictionary['BriefDescription']     = 'TODO: Brief Description of GUID %s' % (Config.GuidIncludeName)
      Dictionary['DetailedDescription']  = 'TODO: Detailed Description of GUID %s' % (Config.GuidIncludeName)
      Dictionary['Copyright']            = 'TODO: Copyright for GUID %s' % (Config.GuidIncludeName)
      Dictionary['License']              = 'TODO: License for GUID %s' % (Config.GuidIncludeName)
      Dictionary['GuidName']             = Config.GuidIncludeName
      Dictionary['GUID_NAME']            = self.MixedCaseNameToDefineName(Config.GuidIncludeName)
      Dictionary['GUID_STRUCT']          = self.RegisteryGuidValueToStructure(Config.GuidValue)

      self.ProcessTemplate('Templates/Guid.h', Dictionary, GuidFileName)

      NewLines = self.ProcessTemplate('Templates/Guid.dec', Dictionary).lstrip().splitlines(True)
      self.InsertLines(Config.PackageFile, NewLines[0], NewLines[1:])

      os.chdir (SavedCurDir)

      return True, "GUID %s created at %s" % (Config.GuidIncludeName, GuidFileName)
    except:
      return False, "GUID creation failed"

  def CreateLibraryClass(self):
    try:
      if Config.LibraryClassIncludeName == '':
        return False, "Library Class Include Name is not valid"

      SavedCurDir = os.curdir
      Result, LibraryClassFileName = self.VerifyWorkspacePackage (
                                            Config.WorkspacePath,
                                            Config.PackageFile,
                                            'Include/Library',
                                            Config.LibraryClassIncludeName + '.h'
                                            )
      if not Result:
        os.chdir (SavedCurDir)
        return Result, LibraryClassFileName

      self.frame.LogMessageWindow.AppendText('\nCreate Library Class %s\n' % (Config.LibraryClassIncludeName))

      Dictionary = {}
      Dictionary['SKIP']                 = []
      Dictionary['BriefDescription']     = 'TODO: Brief Description of Library Class %s' % (Config.LibraryClassIncludeName)
      Dictionary['DetailedDescription']  = 'TODO: Detailed Description of Library Class %s' % (Config.LibraryClassIncludeName)
      Dictionary['Copyright']            = 'TODO: Copyright for Library Class %s' % (Config.LibraryClassIncludeName)
      Dictionary['License']              = 'TODO: License for Library Class %s' % (Config.LibraryClassIncludeName)
      Dictionary['LibraryClassName']     = Config.LibraryClassIncludeName
      Dictionary['LIBRARY_CLASS_NAME']   = self.MixedCaseNameToDefineName(Config.LibraryClassIncludeName)

      self.ProcessTemplate('Templates/LibraryClass.h', Dictionary, LibraryClassFileName)

      NewLines = self.ProcessTemplate('Templates/LibraryClass.dec', Dictionary).lstrip().splitlines(True)
      self.InsertLines(Config.PackageFile, NewLines[0], NewLines[1:])

      os.chdir (SavedCurDir)

      return True, "Library Class %s created at %s" % (Config.LibraryClassIncludeName, LibraryClassFileName)
    except:
      return False, "Library Class creation failed"

  def CreateProtocol(self):
    try:
      if Config.ProtocolIncludeName == '':
        return False, "Protocol Include Name is not valid"
      try:
        Guid = uuid.UUID(Config.ProtocolGuidValue)
      except:
        return False, "Protocol GUID is not valid."

      SavedCurDir = os.curdir
      Result, ProtocolFileName = self.VerifyWorkspacePackage (
                                        Config.WorkspacePath,
                                        Config.PackageFile,
                                        'Include/Protocol',
                                        Config.ProtocolIncludeName + '.h'
                                )
      if not Result:
        os.chdir (SavedCurDir)
        return Result, ProtocolFileName

      self.frame.LogMessageWindow.AppendText('\nCreate Protocol %s\n' % (Config.ProtocolIncludeName))

      Dictionary = {}
      Dictionary['SKIP']                = []
      Dictionary['BriefDescription']    = 'TODO: Brief Description of Protocol %s' % (Config.ProtocolIncludeName)
      Dictionary['DetailedDescription'] = 'TODO: Detailed Description of Protocol %s' % (Config.ProtocolIncludeName)
      Dictionary['Copyright']           = 'TODO: Copyright for Protocol %s' % (Config.ProtocolIncludeName)
      Dictionary['License']             = 'TODO: License for Protocol %s' % (Config.ProtocolIncludeName)
      Dictionary['ProtocolName']        = Config.ProtocolIncludeName
      Dictionary['PROTOCOL_NAME']       = self.MixedCaseNameToDefineName(Config.ProtocolIncludeName)
      Dictionary['GUID_STRUCT']         = self.RegisteryGuidValueToStructure(Config.ProtocolGuidValue)
      Dictionary['FUNCTION_NAME_1']     = 'FUNCTION_NAME_1'
      Dictionary['FUNCTION_NAME_2']     = 'FUNCTION_NAME_2'
      Dictionary['FUNCTION_NAME_N']     = 'FUNCTION_NAME_N'
      Dictionary['FunctionName1']       = 'Function1'
      Dictionary['FunctionName2']       = 'Function2'
      Dictionary['FunctionNameN']       = 'FunctionN'

      self.ProcessTemplate('Templates/Protocol.h', Dictionary, ProtocolFileName)

      NewLines = self.ProcessTemplate('Templates/Protocol.dec', Dictionary).lstrip().splitlines(True)
      self.InsertLines(Config.PackageFile, NewLines[0], NewLines[1:])

      os.chdir (SavedCurDir)

      return True, "Protocol %s created at %s" % (Config.ProtocolIncludeName, ProtocolFileName)
    except:
      return False, "Protocol creation failed"

  def CreateUefiDriver(self):
    try:
      if Config.UefiDriverName == '':
        return False, "UEFI Driver Name is not valid."
      try:
        Guid = uuid.UUID(Config.UefiDriverGuid)
      except:
        return False, "UEFI Driver GUID is not valid."
      if Config.UefiDriverVersion == '':
        return False, "UEFI Driver Version is not valid."

      SavedCurDir = os.curdir

      if not os.path.isdir(Config.WorkspacePath):
        return False, "WORKSPACE path %s is not a valid path." % (Config.WorkspacePath)
      os.chdir (Config.WorkspacePath)
      if os.path.normcase(os.path.abspath(os.curdir)) not in os.path.normcase(os.path.abspath(Config.UefiDriverPath)):
        return False, "UEFI Driver Path %s is not in WORKSPACE path %s." % (Config.UefiDriverPath, Config.WorkspacePath)
      if not os.path.exists (Config.UefiDriverPath):
        os.makedirs (Config.UefiDriverPath)
      if not os.path.isdir (Config.UefiDriverPath):
        return False, "UEFI Driver Path %s is not a directory." % (Config.UefiDriverPath)
      if os.path.exists(os.path.join(Config.UefiDriverPath, Config.UefiDriverName + '.inf')):
        return False, "UEFI Driver INF %s already exists." % (os.path.join(Config.UefiDriverPath, Config.UefiDriverName + '.inf'))

      self.frame.LogMessageWindow.AppendText('\nCreate UEFI Driver %s\n' % (Config.UefiDriverName))

      Path = os.path.normcase(os.path.abspath(Config.UefiDriverPath)).replace(os.path.normcase(os.path.abspath(os.curdir)), '')
      UefiDriverPath = Config.UefiDriverPath[-len(Path):].replace('\\','/').strip('/')
      Path = os.path.abspath(Config.UefiDriverPath)
      while Path <> '':
        DscFileList = glob.glob(os.path.join(Path, '*.dsc'))
        if DscFileList == []:
          if Path == os.path.dirname(Path):
            break
          Path = os.path.dirname(Path)
          continue
        if len(DscFileList) > 1:
          break
        if 'All CPU Architectures' in Config.UefiDriverCpuArchitecture:
          self.InsertLines(DscFileList[0], '[Components]\n', ['  ' + UefiDriverPath + '/' + Config.UefiDriverName + '.inf\n'])
        else:
          for Arch in ['IA32', 'X64', 'IPF', 'EBC', 'ARM']:
            if Arch in Config.UefiDriverCpuArchitecture:
              self.InsertLines(DscFileList[0], '[Components.' + Arch + ']\n', ['  ' + UefiDriverPath + '/' + Config.UefiDriverName + '.inf\n'])
        break

      os.chdir (Config.UefiDriverPath)

      Dictionary = {}
      Dictionary['SKIP']                 = []
      Dictionary['BriefDescription']     = 'TODO: Brief Description of UEFI Driver %s' % (Config.UefiDriverName)
      Dictionary['DetailedDescription']  = 'TODO: Detailed Description of UEFI Driver %s' % (Config.UefiDriverName)
      Dictionary['Copyright']            = 'TODO: Copyright for UEFI Driver %s' % (Config.UefiDriverName)
      Dictionary['License']              = 'TODO: License for UEFI Driver %s' % (Config.UefiDriverName)
      Dictionary['DriverName']           = Config.UefiDriverName
      Dictionary['DRIVER_NAME']          = self.MixedCaseNameToDefineName(Config.UefiDriverName)
      Dictionary['GUID_REGISTRY_FORMAT'] = Config.UefiDriverGuid
      Dictionary['GUID_STRUCT']          = self.RegisteryGuidValueToStructure(Config.UefiDriverGuid)
      Dictionary['DriverVersionString']  = Config.UefiDriverVersion

      Dictionary['UefiBootServiceDriverEnabled'] = ['']
      Dictionary['UefiRuntimeDriverEnabled']     = []
      if u"Network Interface Card producing NII/UNDI" in Config.UefiDriverProducedProtocols:
        Dictionary['UefiBootServiceDriverEnabled'] = []
        Dictionary['UefiRuntimeDriverEnabled']     = ['']

      Dictionary['UnloadEnabled'] = []
      if u"Unloadable" in Config.UefiDriverCommonFeatures:
        Dictionary['UnloadEnabled'] = ['']

      Dictionary['UefiDriverModelEnabled'] = []
      Dictionary['UefiDriverModelDeviceDriverEnabled'] = []
      Dictionary['UefiDriverModelBusDriverEnabled'] = []
      if u"UEFI Driver Model Device Driver" in Config.UefiDriverType:
        Dictionary['UefiDriverModelEnabled'] = ['']
        Dictionary['UefiDriverModelDeviceDriverEnabled'] = ['']
      if u"UEFI Driver Model Bus Driver" in Config.UefiDriverType:
        Dictionary['UefiDriverModelEnabled'] = ['']
        Dictionary['UefiDriverModelBusDriverEnabled'] = ['']
      if u"UEFI Driver Model Hybrid Driver" in Config.UefiDriverType:
        Dictionary['UefiDriverModelEnabled'] = ['']
        Dictionary['UefiDriverModelBusDriverEnabled'] = ['']
      if Dictionary['UefiDriverModelEnabled'] <> []:
        Dictionary['DriverBindingVersion'] = Config.DriverBindingVersion

      Dictionary['DriverSupportedEfiVersionEnabled']        = []
      Dictionary['UEFI_SYSTEM_TABLE_REVISON']               = ''
      if u"Driver Supported EFI Version Protocol" in Config.UefiDriverCommonFeatures:
        Dictionary['UEFI_SYSTEM_TABLE_REVISON'] = Config.UefiSpecificationVersion
        Dictionary['DriverSupportedEfiVersionEnabled'] = ['']

      Dictionary['HiiEnabled']             = []
      Dictionary['HiiConfigAccessEnabled'] = []
      if u"HII Packages for Strings, Fonts, or Images" in Config.UefiDriverCommonFeatures:
        Dictionary['HiiEnabled'] = ['']
      if u"HII Packages for forms and HII based configuration " in Config.UefiDriverDriverModelFeatures:
        Dictionary['HiiEnabled'] = ['']
        Dictionary['HiiConfigAccessEnabled'] = ['']

      Dictionary['ComponentNameEnabled'] = []
      if u"Component Name 2 Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['ComponentNameEnabled'] = ['']
      if u"Component Name Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['ComponentNameEnabled'] = ['']
      if Dictionary['ComponentNameEnabled'] <> []:
        Dictionary['Iso639SupportedLanguages'] = [Config.Iso639LanguageCodes]
        Dictionary['Rfc4646SupportedLanguages'] = [Config.Rfc4646LanguageCodes]

      Dictionary['DriverDiagnosticsEnabled'] = []
      if u"Driver Diagnostics 2 Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['DriverDiagnosticsEnabled'] = ['']
      if u"Driver Diagnostics Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['DriverDiagnosticsEnabled'] = ['']
      if Dictionary['DriverDiagnosticsEnabled'] <> []:
        Dictionary['Iso639SupportedLanguages'] = [Config.Iso639LanguageCodes]
        Dictionary['Rfc4646SupportedLanguages'] = [Config.Rfc4646LanguageCodes]

      Dictionary['DriverConfigurationEnabled'] = []
      if u"Driver Configuration 2 Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['DriverConfigurationEnabled'] = ['']
      if u"Driver Configuration Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['DriverConfigurationEnabled'] = ['']
      if Dictionary['DriverConfigurationEnabled'] <> []:
        Dictionary['Iso639SupportedLanguages'] = [Config.Iso639LanguageCodes]
        Dictionary['Rfc4646SupportedLanguages'] = [Config.Rfc4646LanguageCodes]

      Dictionary['EfiLibInstallDriverBinding'] = []
      Dictionary['EfiLibInstallDriverBindingComponentName2'] = []
      Dictionary['EfiLibInstallAllDriverProtocols2_111'] = []
      Dictionary['EfiLibInstallAllDriverProtocols2_110'] = []
      Dictionary['EfiLibInstallAllDriverProtocols2_101'] = []
      Dictionary['EfiLibInstallAllDriverProtocols2_001'] = []
      Dictionary['EfiLibInstallAllDriverProtocols2_010'] = []
      Dictionary['EfiLibInstallAllDriverProtocols2_011'] = []
      if Dictionary['UefiDriverModelEnabled'] <> []:
        if Dictionary['DriverDiagnosticsEnabled'] <> [] or Dictionary['DriverConfigurationEnabled'] <> []:
          if Dictionary['ComponentNameEnabled'] <> [] and Dictionary['DriverConfigurationEnabled'] <> [] and Dictionary['DriverDiagnosticsEnabled'] <> []:
            Dictionary['EfiLibInstallAllDriverProtocols2_111'] = ['']
          if Dictionary['ComponentNameEnabled'] <> [] and Dictionary['DriverConfigurationEnabled'] <> [] and Dictionary['DriverDiagnosticsEnabled'] == []:
            Dictionary['EfiLibInstallAllDriverProtocols2_110'] = ['']
          if Dictionary['ComponentNameEnabled'] <> [] and Dictionary['DriverConfigurationEnabled'] == [] and Dictionary['DriverDiagnosticsEnabled'] <> []:
            Dictionary['EfiLibInstallAllDriverProtocols2_101'] = ['']
          if Dictionary['ComponentNameEnabled'] == [] and Dictionary['DriverConfigurationEnabled'] == [] and Dictionary['DriverDiagnosticsEnabled'] <> []:
            Dictionary['EfiLibInstallAllDriverProtocols2_001'] = ['']
          if Dictionary['ComponentNameEnabled'] == [] and Dictionary['DriverConfigurationEnabled'] <> [] and Dictionary['DriverDiagnosticsEnabled'] == []:
            Dictionary['EfiLibInstallAllDriverProtocols2_010'] = ['']
          if Dictionary['ComponentNameEnabled'] == [] and Dictionary['DriverConfigurationEnabled'] <> [] and Dictionary['DriverDiagnosticsEnabled'] <> []:
            Dictionary['EfiLibInstallAllDriverProtocols2_011'] = ['']
        elif Dictionary['ComponentNameEnabled'] <> []:
          Dictionary['EfiLibInstallDriverBindingComponentName2'] = ['']
        else:
          Dictionary['EfiLibInstallDriverBinding'] = ['']

      Dictionary['DriverFamilyOverrideEnabled'] = []
      if u"Driver Family Override Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['DriverFamilyOverrideEnabled'] = ['']

      Dictionary['DriverHealthEnabled'] = []
      if u"Driver Health Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['DriverHealthEnabled'] = ['']

      Dictionary['BusSpecificDriverOverrideEnabled'] = []
      if u"Bus Specific Driver Override Protocol" in Config.UefiDriverDriverModelFeatures:
        Dictionary['BusSpecificDriverOverrideEnabled'] = ['']

      Dictionary['ConsumedProtocol'] = ''
      Dictionary['ConsumedProtocolIncludeFile'] = ''
      if u"PCI Driver that consumes the PCI I/O Protocol" in Config.UefiDriverConsumedProtocols:
        Dictionary['ConsumedProtocol'] = 'gEfiPciIoProtocolGuid                         ## TO_START'
        Dictionary['ConsumedProtocolIncludeFile'] = 'PciIo.h'
      if u"USB Driver that consumes the USB I/O Protocol" in Config.UefiDriverConsumedProtocols:
        Dictionary['ConsumedProtocol'] = 'gEfiUsbIoProtocolGuid                         ## TO_START'
        Dictionary['ConsumedProtocolIncludeFile'] = 'UsbIo.h'
      if u"SCSI Driver that consumes the SCSI I/O Protocol" in Config.UefiDriverConsumedProtocols:
        Dictionary['ConsumedProtocol'] = 'gEfiScsiIoProtocolGuid                        ## TO_START'
        Dictionary['ConsumedProtocolIncludeFile'] = 'ScsiIo.h'
      if u"ATA Driver that consumes the ATA Pass Thru Protocol" in Config.UefiDriverConsumedProtocols:
        Dictionary['ConsumedProtocol'] = 'gEfiAtaPassThruProtocolGuid                   ## TO_START'
        Dictionary['ConsumedProtocolIncludeFile'] = 'AtaPassThru.h'

      Dictionary['SimpleTextInputEnabled']        = []
      Dictionary['SimplePointerEnabled']          = []
      Dictionary['AbsolutePointerEnabled']        = []
      Dictionary['SimpleTextOutputEnabled']       = []
      Dictionary['SerialIoEnabled']               = []
      Dictionary['GraphicsOutputEnabled']         = []
      Dictionary['BlockIoEnabled']                = []
      Dictionary['StorageSecurityCommandEnabled'] = []
      Dictionary['NiiUndiEnabled']                = []
      Dictionary['SimpleNetworkEnabled']          = []
      Dictionary['Usb2HostControllerEnabled']     = []
      Dictionary['ScsiPassThruEnabled']           = []
      Dictionary['ExtScsiPassThruEnabled']        = []
      Dictionary['AtaPassThruEnabled']            = []
      Dictionary['UserCredentialEnabled']         = []
      Dictionary['LoadFileEnabled']               = []
      Dictionary['EdidOverrideEnabled']           = []
      if u"Keyboard producing Simple Text In Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['SimpleTextInputEnabled'] = ['']
      if u"Keyboard producing Simple Text In Ex Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['SimpleTextInputEnabled'] = ['']
      if u"Mouse producing Simple Pointer Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['SimplePointerEnabled'] = ['']
      if u"Tablet producing Absolute Pointer Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['AbsolutePointerEnabled'] = ['']
      if u"Text Console producing the Simple Text Output Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['SimpleTextOutputEnabled'] = ['']
      if u"Byte stream device (i.e. UART) producing Serial I/O Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['SerialIoEnabled'] = ['']
      if u"Graphics Console producing the Graphics Output Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['GraphicsOutputEnabled'] = ['']
      if u"Mass Storage Device producing Block I/O Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['BlockIoEnabled'] = ['']
      if u"Mass Storage Device producing Block I/O 2 Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['BlockIoEnabled'] = ['']
      if u"Mass Storage Device producing Storage Security Command Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['StorageSecurityCommand'] = ['']
      if u"Network Interface Card producing NII/UNDI" in Config.UefiDriverProducedProtocols:
        Dictionary['NiiUndiEnabled'] = ['']
      if u"Network Interface Card producing Simple Network Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['SimpleNetworkEnabled'] = ['']
      if u"USB Host Controller producing the USB Host Controller 2 Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['Usb2HostControllerEnabled'] = ['']
        Dictionary['UsbSpecificationMajorRevision'] = Config.UsbMajorVersion
        Dictionary['UsbSpecificationMinorRevision'] = Config.UsbMinorVersion
      if u"ATA Host Controller producing the ATA Pass Thru Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['AtaPassThruEnabled'] = ['']
      if u"SCSI Host Controller producing the SCSI Pass Thru Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['ScsiPassThruEnabled'] = ['']
      if u"SCSI Host Controller or ATA Host Controller producing the Extended SCSI Pass Thru Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['ExtScsiPassThruEnabled'] = ['']
      if u"User identification device producing the User Credential Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['UserCredentialEnabled'] = ['']
      if u"Non standard boot device producing Load File Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['LoadFileEnabled'] = ['']
      if u"Platform driver producing the EDID Override Protocol" in Config.UefiDriverProducedProtocols:
        Dictionary['EdidOverrideEnabled'] = ['']

      self.ProcessTemplate('Templates/UefiDriver.inf',          Dictionary, Config.UefiDriverName + '.inf')
      self.ProcessTemplate('Templates/UefiDriver.c',            Dictionary, Config.UefiDriverName + '.c')
      self.ProcessTemplate('Templates/UefiDriver.h',            Dictionary, Config.UefiDriverName + '.h')
      self.ProcessTemplate('Templates/UefiDriverExtra.uni',     Dictionary, Config.UefiDriverName + 'Extra.uni',   Encoding='utf-16')
      self.ProcessTemplate('Templates/UefiDriverModStrs.uni',   Dictionary, Config.UefiDriverName + 'ModStrs.uni', Encoding='utf-16')
      if Dictionary['UefiDriverModelEnabled'] <> []:
        self.ProcessTemplate('Templates/DriverBinding.h', Dictionary, 'DriverBinding.h')
      if Dictionary['ComponentNameEnabled'] <> []:
        self.ProcessTemplate('Templates/ComponentName.c', Dictionary, 'ComponentName.c')
        self.ProcessTemplate('Templates/ComponentName.h', Dictionary, 'ComponentName.h')
      if Dictionary['DriverDiagnosticsEnabled'] <> []:
        self.ProcessTemplate('Templates/DriverDiagnostics.c', Dictionary, 'DriverDiagnostics.c')
        self.ProcessTemplate('Templates/DriverDiagnostics.h', Dictionary, 'DriverDiagnostics.h')
      if Dictionary['DriverConfigurationEnabled'] <> []:
        self.ProcessTemplate('Templates/DriverConfiguration.c', Dictionary, 'DriverConfiguration.c')
        self.ProcessTemplate('Templates/DriverConfiguration.h', Dictionary, 'DriverConfiguration.h')
      if Dictionary['DriverFamilyOverrideEnabled'] <> []:
        self.ProcessTemplate('Templates/DriverFamilyOverride.c', Dictionary, 'DriverFamilyOverride.c')
        self.ProcessTemplate('Templates/DriverFamilyOverride.h', Dictionary, 'DriverFamilyOverride.h')
      if Dictionary['DriverHealthEnabled'] <> []:
        self.ProcessTemplate('Templates/DriverHealth.c', Dictionary, 'DriverHealth.c')
        self.ProcessTemplate('Templates/DriverHealth.h', Dictionary, 'DriverHealth.h')
      if Dictionary['BusSpecificDriverOverrideEnabled'] <> []:
        self.ProcessTemplate('Templates/BusSpecificDriverOverride.c', Dictionary, 'BusSpecificDriverOverride.c')
        self.ProcessTemplate('Templates/BusSpecificDriverOverride.h', Dictionary, 'BusSpecificDriverOverride.h')
      if Dictionary['HiiEnabled'] <> []:
        self.ProcessTemplate('Templates/UefiDriver.uni',   Dictionary, Config.UefiDriverName + '.uni', Encoding='utf-16')
      if Dictionary['HiiConfigAccessEnabled'] <> []:
        self.ProcessTemplate('Templates/UefiDriver.vfr',    Dictionary, Config.UefiDriverName + '.vfr')
        self.ProcessTemplate('Templates/HiiConfigAccess.c', Dictionary, 'HiiConfigAccess.c')
        self.ProcessTemplate('Templates/HiiConfigAccess.h', Dictionary, 'HiiConfigAccess.h')
      if Dictionary['SimpleTextInputEnabled']    <> []:
        self.ProcessTemplate('Templates/SimpleTextInput.c', Dictionary, 'SimpleTextInput.c')
        self.ProcessTemplate('Templates/SimpleTextInput.h', Dictionary, 'SimpleTextInput.h')
      if Dictionary['SimplePointerEnabled']      <> []:
        self.ProcessTemplate('Templates/SimplePointer.c', Dictionary, 'SimplePointer.c')
        self.ProcessTemplate('Templates/SimplePointer.h', Dictionary, 'SimplePointer.h')
      if Dictionary['AbsolutePointerEnabled']    <> []:
        self.ProcessTemplate('Templates/AbsolutePointer.c', Dictionary, 'AbsolutePointer.c')
        self.ProcessTemplate('Templates/AbsolutePointer.h', Dictionary, 'AbsolutePointer.h')
      if Dictionary['SimpleTextOutputEnabled']   <> []:
        self.ProcessTemplate('Templates/SimpleTextOutput.c', Dictionary, 'SimpleTextOutput.c')
        self.ProcessTemplate('Templates/SimpleTextOutput.h', Dictionary, 'SimpleTextOutput.h')
      if Dictionary['SerialIoEnabled']   <> []:
        self.ProcessTemplate('Templates/SerialIo.c', Dictionary, 'SerialIo.c')
        self.ProcessTemplate('Templates/SerialIo.h', Dictionary, 'SerialIo.h')
      if Dictionary['GraphicsOutputEnabled']     <> []:
        self.ProcessTemplate('Templates/GraphicsOutput.c', Dictionary, 'GraphicsOutput.c')
        self.ProcessTemplate('Templates/GraphicsOutput.h', Dictionary, 'GraphicsOutput.h')
      if Dictionary['BlockIoEnabled']            <> []:
        self.ProcessTemplate('Templates/BlockIo.c', Dictionary, 'BlockIo.c')
        self.ProcessTemplate('Templates/BlockIo.h', Dictionary, 'BlockIo.h')
      if Dictionary['StorageSecurityCommandEnabled']            <> []:
        self.ProcessTemplate('Templates/StorageSecurityCommand.c', Dictionary, 'StorageSecurityCommand.c')
        self.ProcessTemplate('Templates/StorageSecurityCommand.h', Dictionary, 'StorageSecurityCommand.h')
      if Dictionary['NiiUndiEnabled']            <> []:
        self.ProcessTemplate('Templates/NiiUndi.c', Dictionary, 'NiiUndi.c')
      if Dictionary['SimpleNetworkEnabled']      <> []:
        self.ProcessTemplate('Templates/SimpleNetwork.c', Dictionary, 'SimpleNetwork.c')
        self.ProcessTemplate('Templates/SimpleNetwork.h', Dictionary, 'SimpleNetwork.h')
      if Dictionary['Usb2HostControllerEnabled'] <> []:
        self.ProcessTemplate('Templates/Usb2HostController.c', Dictionary, 'Usb2HostController.c')
        self.ProcessTemplate('Templates/Usb2HostController.h', Dictionary, 'Usb2HostController.h')
      if Dictionary['ScsiPassThruEnabled']    <> []:
        self.ProcessTemplate('Templates/ScsiPassThru.c', Dictionary, 'ScsiPassThru.c')
        self.ProcessTemplate('Templates/ScsiPassThru.h', Dictionary, 'ScsiPassThru.h')
      if Dictionary['ExtScsiPassThruEnabled']    <> []:
        self.ProcessTemplate('Templates/ExtScsiPassThru.c', Dictionary, 'ExtScsiPassThru.c')
        self.ProcessTemplate('Templates/ExtScsiPassThru.h', Dictionary, 'ExtScsiPassThru.h')
      if Dictionary['AtaPassThruEnabled']        <> []:
        self.ProcessTemplate('Templates/AtaPassThru.c', Dictionary, 'AtaPassThru.c')
        self.ProcessTemplate('Templates/AtaPassThru.h', Dictionary, 'AtaPassThru.h')
      if Dictionary['UserCredentialEnabled']     <> []:
        self.ProcessTemplate('Templates/UserCredential.c', Dictionary, 'UserCredential.c')
        self.ProcessTemplate('Templates/UserCredential.h', Dictionary, 'UserCredential.h')
      if Dictionary['LoadFileEnabled']           <> []:
        self.ProcessTemplate('Templates/LoadFile.c', Dictionary, 'LoadFile.c')
        self.ProcessTemplate('Templates/LoadFile.h', Dictionary, 'LoadFile.h')
      if Dictionary['EdidOverrideEnabled']     <> []:
        self.ProcessTemplate('Templates/EdidOverride.c', Dictionary, 'EdidOverride.c')
        self.ProcessTemplate('Templates/EdidOverride.h', Dictionary, 'EdidOverride.h')

      os.chdir (SavedCurDir)

      return True, "UEFI Driver %s created at %s" % (Config.UefiDriverName, os.path.join(Config.UefiDriverPath, Config.UefiDriverName + '.inf'))
    except:
      return False, "UEFI Driver creation failed"

  def CreateUefiDriverByParams (
        self,
        UefiDriverPath,
        UefiDriverName,
        UefiDriverGuid,
        UefiDriverVersion,
        UefiDriverType,
        UefiDriverCommonFeatures,
        UefiDriverCpuArchitecture,
        UefiDriverDriverModelFeatures,
        UefiDriverConsumedProtocols,
        UefiDriverProducedProtocols,
        DriverBindingVersion,
        UefiSpecificationVersion,
        Rfc4646LanguageCodes,
        Iso639LanguageCodes,
        UsbMajorVersion,
        UsbMinorVersion):

    Config.UefiDriverPath                = UefiDriverPath
    Config.UefiDriverName                = UefiDriverName
    Config.UefiDriverGuid                = UefiDriverGuid
    Config.UefiDriverVersion             = UefiDriverVersion
    Config.UefiDriverType                = UefiDriverType
    Config.UefiDriverCommonFeatures      = UefiDriverCommonFeatures
    Config.UefiDriverCpuArchitecture     = UefiDriverCpuArchitecture
    Config.UefiDriverDriverModelFeatures = UefiDriverDriverModelFeatures
    Config.UefiDriverConsumedProtocols   = UefiDriverConsumedProtocols
    Config.UefiDriverProducedProtocols   = UefiDriverProducedProtocols
    Config.DriverBindingVersion          = DriverBindingVersion
    Config.UefiSpecificationVersion      = UefiSpecificationVersion
    Config.Rfc4646LanguageCodes          = Rfc4646LanguageCodes
    Config.Iso639LanguageCodes           = Iso639LanguageCodes
    Config.UsbMajorVersion               = UsbMajorVersion
    Config.UsbMinorVersion               = UsbMinorVersion

    return self.CreateUefiDriver()

def GenerateTestCases():
  UefiDriverTypeChoices                = [ u"UEFI Driver Model Device Driver", u"UEFI Driver Model Bus Driver", u"UEFI Driver Model Hybrid Driver", u"Root Bridge Driver", u"Service Driver", u"Initializing Driver" ]
  UefiDriverCommonFeaturesChoices      = [ u"Unloadable", u"Driver Supported EFI Version Protocol", u"HII Packages for Strings, Fonts, or Images", u"Service Binding Protocol" ];
  UefiDriverCpuArchitectureChoices     = [ u"All CPU Architectures", u"IA32", u"X64", u"IPF", u"EBC", u"ARM" ];
  UefiDriverDriverModelFeaturesChoices = [ u"Component Name 2 Protocol", u"Component Name Protocol", u"Driver Family Override Protocol", u"Driver Diagnostics 2 Protocol", u"Driver Diagnostics Protocol", u"HII Packages for forms and HII based configuration ", u"Driver Configuration 2 Protocol", u"Driver Configuration Protocol", u"Driver Health Protocol", u"Bus Specific Driver Override Protocol" ];
  UefiDriverConsumedProtocolsChoices   = [ u"PCI Driver that consumes the PCI I/O Protocol", u"USB Driver that consumes the USB I/O Protocol", u"SCSI Driver that consumes the SCSI I/O Protocol", u"ATA Driver that consumes the ATA Pass Thru Protocol"];
  UefiDriverProducedProtocolsChoices   = [ u"Keyboard producing Simple Text In Protocol", u"Keyboard producing Simple Text In Ex Protocol", u"Mouse producing Simple Pointer Protocol", u"Tablet producing Absolute Pointer Protocol", u"Text Console producing the Simple Text Output Protocol", u"Byte stream device (i.e. UART) producing Serial I/O Protocol", u"Graphics Console producing the Graphics Output Protocol", u"Mass Storage Device producing Block I/O Protocol", u"Mass Storage Device producing Block I/O 2 Protocol", u"Mass Storage Device producing Storage Security Command Protocol", u"Network Interface Card producing NII/UNDI", u"Network Interface Card producing Simple Network Protocol", u"USB Host Controller producing the USB Host Controller 2 Protocol", u"ATA Host Controller producing the ATA Pass Thru Protocol", u"SCSI Host Controller producing the SCSI Pass Thru Protocol", u"SCSI Host Controller or ATA Host Controller producing the Extended SCSI Pass Thru Protocol", u"User identification device producing the User Credential Protocol", u"Non standard boot device producing Load File Protocol", u"Platform driver producing the EDID Override Protocol"];

  for UefiDriverType in UefiDriverTypeChoices:
    for UefiDriverCommonFeatures in UefiDriverCommonFeaturesChoices:

      for Index in range (0,9999):
        PackageName = 'TestPkg%04d' % (Index)
        PackagePath = os.path.join (Config.WorkspacePath, PackageName)
        if not os.path.exists(PackagePath):
          break
      if Index <= 9999:
        Config.App.CreatePackageByParams(PackagePath, PackageName, uuid.uuid1().get_urn().split(':')[2], '0.10', uuid.uuid1().get_urn().split(':')[2])
        DriverIndex = 0

      for UefiDriverProducedProtocols in UefiDriverProducedProtocolsChoices:
        if UefiDriverType in [ u"UEFI Driver Model Device Driver", u"UEFI Driver Model Bus Driver", u"UEFI Driver Model Hybrid Driver"]:
          for UefiDriverDriverModelFeatures in UefiDriverDriverModelFeaturesChoices:
            for UefiDriverConsumedProtocols in UefiDriverConsumedProtocolsChoices:
              UefiDriverName = 'TestDriver%04d' % (DriverIndex)
              UefiDriverPath = os.path.join (PackagePath, UefiDriverName)
              UefiDriverCpuArchitecture = u"All CPU Architectures"
              DriverIndex = DriverIndex + 1
              Config.App.CreateUefiDriverByParams(
                UefiDriverPath,
                UefiDriverName,
                uuid.uuid1().get_urn().split(':')[2],
                '0.10',
                UefiDriverType,
                UefiDriverCommonFeatures,
                UefiDriverCpuArchitecture,
                UefiDriverDriverModelFeatures,
                UefiDriverConsumedProtocols,
                UefiDriverProducedProtocols,
                '0x00000010',
                '0x0002001E',
                'en',
                'eng',
                '3',
                '0'
                )
        else:
          UefiDriverName = 'TestDriver%04d' % (DriverIndex)
          UefiDriverPath = os.path.join (PackagePath, UefiDriverName)
          UefiDriverCpuArchitecture = u"All CPU Architectures"
          DriverIndex = DriverIndex + 1
          Config.App.CreateUefiDriverByParams(
            UefiDriverPath,
            UefiDriverName,
            uuid.uuid1().get_urn().split(':')[2],
            '0.10',
            UefiDriverType,
            UefiDriverCommonFeatures,
            UefiDriverCpuArchitecture,
            [],
            [],
            UefiDriverProducedProtocols,
            '0x00000010',
            '0x0002001E',
            'en',
            'eng',
            '3',
            '0'
            )

def main(TestMode = False):
  Config.WorkspacePath     = os.getenv('WORKSPACE')
  if Config.WorkspacePath == None:
    if os.path.exists (os.path.join(os.getcwd (), 'Conf', 'target.txt')):
      Config.WorkspacePath = os.getcwd ()
    else:
      Config.WorkspacePath = ''
  else:
    if not os.path.exists (os.path.join(Config.WorkspacePath, 'Conf', 'target.txt')):
      Config.WorkspacePath = ''
  Config.App = MyApp(False)
  Config.App.TopWindow.SetTitle ("%s - UEFI Driver Wizard" % (Config.WorkspacePath))
  if TestMode == True:
    GenerateTestCases()
  Config.App.MainLoop()

if __name__ == '__main__':
  try:
    #
    # Run in normal mode
    #
    main (False)
  except:
    print "Unexpected error in UEFI Driver Wizard"
