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
/// Bus Specific Driver Override Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED 
EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL g<<DriverName>>BusSpecificDriverOverride = {
  <<DriverName>>BusSpecificDriverOverrideGetDriver
};

/**                                                                   
  Uses a bus specific algorithm to retrieve a driver image handle for a controller.
    
  @param  This                  A pointer to the EFI_BUS_SPECIFIC_DRIVER_
                                OVERRIDE_PROTOCOL instance.              
  @param  DriverImageHandle     On input, a pointer to the previous driver image handle returned
                                by GetDriver(). On output, a pointer to the next driver         
                                image handle. Passing in a NULL, will return the first driver   
                                image handle.

  @retval EFI_SUCCESS           A bus specific override driver is returned in DriverImageHandle.
  @retval EFI_NOT_FOUND         The end of the list of override drivers was reached.
                                A bus specific override driver is not returned in DriverImageHandle.
  @retval EFI_INVALID_PARAMETER DriverImageHandle is not a handle that was returned on a
                                previous call to GetDriver().

**/
EFI_STATUS
EFIAPI
<<DriverName>>BusSpecificDriverOverrideGetDriver (
  IN EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL              *This,
  IN OUT EFI_HANDLE                                         *DriverImageHandle
  )
{
  return EFI_NOT_FOUND;
}
