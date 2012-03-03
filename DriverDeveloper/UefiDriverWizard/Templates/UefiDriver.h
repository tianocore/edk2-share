<<BEGIN>><<SKIP>>
/** @file
  UEFI Driver Wizard template file

Copyright (c) 2012, Intel Corporation. All rights reserved.<BR>

This program and the accompanying materials are licensed and made 
available under the terms and conditions of the BSD License which 
accompanies this distribution.  The full text of the license may 
be found at http://opensource.org/licenses/bsd-license.php.

THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" 
BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER 
EXPRESS OR IMPLIED.

**/
<<END>>
/** @file
  <<BriefDescription>>
  
  <<DetailedDescription>>

  <<Copyright>>
  
  <<License>>

**/

#ifndef __EFI_<<DRIVER_NAME>>_H__
#define __EFI_<<DRIVER_NAME>>_H__

#include <Uefi.h>

//
// Libraries
//
#include <Library/UefiBootServicesTableLib.h>
#include <Library/MemoryAllocationLib.h>
#include <Library/BaseMemoryLib.h>
#include <Library/BaseLib.h>
#include <Library/UefiLib.h>
#include <Library/DevicePathLib.h>
#include <Library/DebugLib.h>
<<BEGIN>><<UefiRuntimeDriverEnabled>>#include <Library/UefiRuntimeServicesTableLib.h>
<<END>>
<<BEGIN>><<UefiRuntimeDriverEnabled>>#include <Library/UefiRuntimeLib.h>
<<END>>

//
// UEFI Driver Model Protocols
//
<<BEGIN>><<UefiDriverModelEnabled>>#include <Protocol/DriverBinding.h>
<<END>>
<<BEGIN>><<HiiEnabled>>#include <Protocol/HiiDatabase.h>
<<END>>
<<BEGIN>><<HiiEnabled>>#include <Protocol/HiiPackageList.h>
<<END>>
<<BEGIN>><<DriverSupportedEfiVersionEnabled>>#include <Protocol/DriverSupportedEfiVersion.h>
<<END>>
<<BEGIN>><<ComponentNameEnabled>>#include <Protocol/ComponentName2.h>
<<END>>
<<BEGIN>><<ComponentNameEnabled>>#include <Protocol/ComponentName.h>
<<END>>
<<BEGIN>><<DriverDiagnosticsEnabled>>#include <Protocol/DriverDiagnostics2.h>
<<END>>
<<BEGIN>><<DriverDiagnosticsEnabled>>#include <Protocol/DriverDiagnostics.h>
<<END>>
<<BEGIN>><<DriverConfigurationEnabled>>#include <Protocol/DriverConfiguration2.h>
<<END>>
<<BEGIN>><<DriverConfigurationEnabled>>#include <Protocol/DriverConfiguration.h>
<<END>>
<<BEGIN>><<DriverFamilyOverrideEnabled>>#include <Protocol/DriverFamilyOverride.h>
<<END>>
<<BEGIN>><<DriverHealthEnabled>>#include <Protocol/DriverHealth.h>
<<END>>
<<BEGIN>><<BusSpecificDriverOverrideEnabled>>#include <Protocol/BusSpecificDriverOverride.h>
<<END>>
<<BEGIN>><<HiiConfigAccessEnabled>>#include <Protocol/HiiConfigAccess.h>
<<END>>

//
// Consumed Protocols
//
<<BEGIN>><<UefiDriverModelEnabled>>#include <Protocol/<<ConsumedProtocolIncludeFile>>>
<<END>>

//
// Produced Protocols
//
<<BEGIN>><<SimpleTextInputEnabled>>#include <Protocol/SimpleTextIn.h>
<<END>>
<<BEGIN>><<SimpleTextInputEnabled>>#include <Protocol/SimpleTextInEx.h>
<<END>>
<<BEGIN>><<SimplePointerEnabled>>#include <Protocol/SimplePointer.h>
<<END>>
<<BEGIN>><<AbsolutePointerEnabled>>#include <Protocol/AbsolutePointer.h>
<<END>>
<<BEGIN>><<SimpleTextOutputEnabled>>#include <Protocol/SimpleTextOut.h>
<<END>>
<<BEGIN>><<SerialIoEnabled>>#include <Protocol/SerialIo.h>
<<END>>
<<BEGIN>><<GraphicsOutputEnabled>>#include <Protocol/GraphicsOutput.h>
<<END>>
<<BEGIN>><<GraphicsOutputEnabled>>#include <Protocol/EdidDiscovered.h>
<<END>>
<<BEGIN>><<GraphicsOutputEnabled>>#include <Protocol/EdidActive.h>
<<END>>
<<BEGIN>><<BlockIoEnabled>>#include <Protocol/BlockIo.h>
<<END>>
<<BEGIN>><<BlockIoEnabled>>#include <Protocol/BlockIo2.h>
<<END>>
<<BEGIN>><<StorageSecurityCommandEnabled>>#include <Protocol/StorageSecurityCommand.h>
<<END>>
<<BEGIN>><<NiiUndiEnabled>>#include <Protocol/NetworkInterfaceIdentifier.h>
<<END>>
<<BEGIN>><<SimpleNetworkEnabled>>#include <Protocol/SimpleNetwork.h>
<<END>>
<<BEGIN>><<Usb2HostControllerEnabled>>#include <Protocol/Usb2HostController.h>
<<END>>
<<BEGIN>><<ScsiPassThruEnabled>>#include <Protocol/ScsiPassThru.h>
<<END>>
<<BEGIN>><<ExtScsiPassThruEnabled>>#include <Protocol/ScsiPassThruExt.h>
<<END>>
<<BEGIN>><<AtaPassThruEnabled>>#include <Protocol/AtaPassThru.h>
<<END>>
<<BEGIN>><<UserCredentialEnabled>>#include <Protocol/UserCredential2.h>
<<END>>
<<BEGIN>><<LoadFileEnabled>>#include <Protocol/LoadFile.h>
<<END>>
<<BEGIN>><<EdidOverrideEnabled>>#include <Protocol/EdidOverride.h>
<<END>>

//
// Guids
//

//
// Driver Version
//
<<BEGIN>><<UefiDriverModelEnabled>>#define <<DRIVER_NAME>>_VERSION  <<DriverBindingVersion>>
<<END>>

//
// Protocol instances
//
<<BEGIN>><<UefiDriverModelEnabled>>extern EFI_DRIVER_BINDING_PROTOCOL  g<<DriverName>>DriverBinding;
<<END>>
<<BEGIN>><<ComponentNameEnabled>>extern EFI_COMPONENT_NAME2_PROTOCOL  g<<DriverName>>ComponentName2;
<<END>>
<<BEGIN>><<ComponentNameEnabled>>extern EFI_COMPONENT_NAME_PROTOCOL  g<<DriverName>>ComponentName;
<<END>>
<<BEGIN>><<DriverDiagnosticsEnabled>>extern EFI_DRIVER_DIAGNOSTICS2_PROTOCOL  g<<DriverName>>DriverDiagnostics2;
<<END>>
<<BEGIN>><<DriverDiagnosticsEnabled>>extern EFI_DRIVER_DIAGNOSTICS_PROTOCOL  g<<DriverName>>DriverDiagnostics;
<<END>>
<<BEGIN>><<DriverConfigurationEnabled>>extern EFI_DRIVER_CONFIGURATION2_PROTOCOL  g<<DriverName>>DriverConfiguration2;
<<END>>
<<BEGIN>><<DriverConfigurationEnabled>>extern EFI_DRIVER_CONFIGURATION_PROTOCOL  g<<DriverName>>DriverConfiguration;
<<END>>
<<BEGIN>><<DriverFamilyOverrideEnabled>>extern EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL  g<<DriverName>>DriverFamilyOverride;
<<END>>
<<BEGIN>><<DriverHealthEnabled>>extern EFI_DRIVER_HEALTH_PROTOCOL  g<<DriverName>>DriverHealth;
<<END>>
<<BEGIN>><<BusSpecificDriverOverrideEnabled>>extern EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL  g<<DriverName>>BusSpecificDriverOverride;
<<END>>
<<BEGIN>><<HiiConfigAccessEnabled>>extern EFI_HII_CONFIG_ACCESS_PROTOCOL  g<<DriverName>>HiiConfigAccess;
<<END>>

//
// Include files with function prototypes
//
<<BEGIN>><<UefiDriverModelEnabled>>#include "DriverBinding.h"
<<END>>
<<BEGIN>><<ComponentNameEnabled>>#include "ComponentName.h"
<<END>>
<<BEGIN>><<DriverDiagnosticsEnabled>>#include "DriverDiagnostics.h"
<<END>>
<<BEGIN>><<DriverConfigurationEnabled>>#include "DriverConfiguration.h"
<<END>>
<<BEGIN>><<DriverFamilyOverrideEnabled>>#include "DriverFamilyOverride.h"
<<END>>
<<BEGIN>><<DriverHealthEnabled>>#include "DriverHealth.h"
<<END>>
<<BEGIN>><<BusSpecificDriverOverrideEnabled>>#include "BusSpecificDriverOverride.h"
<<END>>
<<BEGIN>><<HiiConfigAccessEnabled>>#include "HiiConfigAccess.h"
<<END>>
<<BEGIN>><<SimpleTextInputEnabled>>#include "SimpleTextInput.h"
<<END>>
<<BEGIN>><<SimplePointerEnabled>>#include "SimplePointer.h"
<<END>>
<<BEGIN>><<AbsolutePointerEnabled>>#include "AbsolutePointer.h"
<<END>>
<<BEGIN>><<SimpleTextOutputEnabled>>#include "SimpleTextOutput.h"
<<END>>
<<BEGIN>><<SerialIoEnabled>>#include "SerialIo.h"
<<END>>
<<BEGIN>><<GraphicsOutputEnabled>>#include "GraphicsOutput.h"
<<END>>
<<BEGIN>><<BlockIoEnabled>>#include "BlockIo.h"
<<END>>
<<BEGIN>><<StorageSecurityCommandEnabled>>#include "StorageSecurityCommand.h"
<<END>>
<<BEGIN>><<SimpleNetworkEnabled>>#include "SimpleNetwork.h"
<<END>>
<<BEGIN>><<Usb2HostControllerEnabled>>#include "Usb2HostController.h"
<<END>>
<<BEGIN>><<ScsiPassThruEnabled>>#include "ScsiPassThru.h"
<<END>>
<<BEGIN>><<ExtScsiPassThruEnabled>>#include "ExtScsiPassThru.h"
<<END>>
<<BEGIN>><<AtaPassThruEnabled>>#include "AtaPassThru.h"
<<END>>
<<BEGIN>><<UserCredentialEnabled>>#include "UserCredential.h"
<<END>>
<<BEGIN>><<LoadFileEnabled>>#include "LoadFile.h"
<<END>>
<<BEGIN>><<EdidOverrideEnabled>>#include "EdidOverride.h"
<<END>>

#endif
