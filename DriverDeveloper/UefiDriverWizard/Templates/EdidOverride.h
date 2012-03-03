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

/**
  Returns policy information and potentially a replacement EDID for the specified video output device.

  @param  This              The EFI_EDID_OVERRIDE_PROTOCOL instance.
  @param  ChildHandle       A child handle produced by the Graphics Output EFI
                            driver that represents a video output device.
  @param  Attributes        The attributes associated with ChildHandle video output device.
  @param  EdidSize          A pointer to the size, in bytes, of the Edid buffer.
  @param  Edid              A pointer to callee allocated buffer that contains the EDID that
                            should be used for ChildHandle. A value of NULL
                            represents no EDID override for ChildHandle.

  @retval EFI_SUCCESS       Valid overrides returned for ChildHandle.
  @retval EFI_UNSUPPORTED   ChildHandle has no overrides.

**/
EFI_STATUS
EFIAPI
<<DriverName>>EdidOverrideGetEdid (
  IN  EFI_EDID_OVERRIDE_PROTOCOL          *This,
  IN  EFI_HANDLE                          *ChildHandle,
  OUT UINT32                              *Attributes,
  IN OUT UINTN                            *EdidSize,
  IN OUT UINT8                            **Edid
  );
