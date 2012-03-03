<<BEGIN>><<SKIP>>
## @file
#
# UEFI Driver Wizard template file
#
# Copyright (c) 2012, Intel Corporation. All rights reserved.<BR>
#
# This program and the accompanying materials are licensed and made 
# available under the terms and conditions of the BSD License which 
# accompanies this distribution.  The full text of the license may 
# be found at http://opensource.org/licenses/bsd-license.php.
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" 
# BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER 
# EXPRESS OR IMPLIED.
#
##
<<END>>
## @file
#  <<BriefDescription>>
#  
#  <<DetailedDescription>>
#
#  <<Copyright>>
#  
#  <<License>>
#  
##

[Defines]
  PLATFORM_NAME                  = <<PackageName>>
  PLATFORM_GUID                  = <<GUID_REGISTRY_FORMAT>>
  PLATFORM_VERSION               = <<PackageVersionString>>
  DSC_SPECIFICATION              = 0x00010005
  OUTPUT_DIRECTORY               = Build/<<PackageName>>
  SUPPORTED_ARCHITECTURES        = IA32|IPF|X64|EBC|ARM
  BUILD_TARGETS                  = DEBUG|RELEASE
  SKUID_IDENTIFIER               = DEFAULT

[LibraryClasses]
  UefiDriverEntryPoint|MdePkg/Library/UefiDriverEntryPoint/UefiDriverEntryPoint.inf
  UefiApplicationEntryPoint|MdePkg/Library/UefiApplicationEntryPoint/UefiApplicationEntryPoint.inf
  UefiBootServicesTableLib|MdePkg/Library/UefiBootServicesTableLib/UefiBootServicesTableLib.inf
  UefiLib|MdePkg/Library/UefiLib/UefiLib.inf
  UefiRuntimeServicesTableLib|MdePkg/Library/UefiRuntimeServicesTableLib/UefiRuntimeServicesTableLib.inf
  UefiRuntimeLib|MdePkg/Library/UefiRuntimeLib/UefiRuntimeLib.inf
  MemoryAllocationLib|MdePkg/Library/UefiMemoryAllocationLib/UefiMemoryAllocationLib.inf
  DevicePathLib|MdePkg/Library/UefiDevicePathLib/UefiDevicePathLib.inf
  UefiUsbLib|MdePkg/Library/UefiUsbLib/UefiUsbLib.inf
  UefiScsiLib|MdePkg/Library/UefiScsiLib/UefiScsiLib.inf
  BaseLib|MdePkg/Library/BaseLib/BaseLib.inf
  BaseMemoryLib|MdePkg/Library/BaseMemoryLib/BaseMemoryLib.inf
  SynchronizationLib|MdePkg/Library/BaseSynchronizationLib/BaseSynchronizationLib.inf
  PrintLib|MdePkg/Library/BasePrintLib/BasePrintLib.inf
  DebugLib|MdePkg/Library/UefiDebugLibStdErr/UefiDebugLibStdErr.inf
  DebugPrintErrorLevelLib|MdePkg/Library/BaseDebugPrintErrorLevelLib/BaseDebugPrintErrorLevelLib.inf  
  PostCodeLib|MdePkg/Library/BasePostCodeLibPort80/BasePostCodeLibPort80.inf
  PcdLib|MdePkg/Library/BasePcdLibNull/BasePcdLibNull.inf

[Components]

[Components.IA32]

[Components.X64]

[Components.IPF]

[Components.EBC]

[Components.ARM]
