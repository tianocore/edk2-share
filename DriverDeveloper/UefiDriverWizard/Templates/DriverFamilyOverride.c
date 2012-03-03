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
/// Driver Family Override Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED 
EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL g<<DriverName>>DriverFamilyOverride = {
  <<DriverName>>DriverFamilyOverrideGetVersion
};

/**                                                                 
  This function returns the version value associated with the driver specified by This.

  Retrieves the version of the driver that is used by the EFI Boot Service ConnectController()
  to sort the set of Driver Binding Protocols in order from highest priority to lowest priority.
  For drivers that support the Driver Family Override Protocol, those drivers are sorted so that
  the drivers with higher values returned by GetVersion() are higher priority than drivers that
  return lower values from GetVersion().

  @param  This                  A pointer to the EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL instance.                            
                                
  @return The version value associated with the driver specified by This.                                  
                                   
**/
UINT32
EFIAPI
<<DriverName>>DriverFamilyOverrideGetVersion (
  IN EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL  *This
  )
{
  return 0;
}
