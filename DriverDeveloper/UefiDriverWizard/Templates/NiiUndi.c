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

#include "<<DriverName>>.h"

///
/// Network Interface Identifier Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED 
EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL  g<<DriverName>>Nii = {
  EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL_REVISION,  // Revision
  0,                                                   // Id
  0,                                                   // ImageAddr
  0,                                                   // ImageSize
  { 'U', 'N', 'D', 'I' },                              // StringId
  EfiNetworkInterfaceUndi,                             // Type
  PXE_ROMID_MAJORVER,                                  // MajorVer
  PXE_ROMID_MINORVER,                                  // MinorVer
  FALSE,                                               // Ipv6Supported
  0                                                    // IfNum
};  
