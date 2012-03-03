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

GLOBAL_REMOVE_IF_UNREFERENCED
EFI_SIMPLE_POINTER_PROTOCOL  g<<DriverName>>SimplePointer =  {
  <<DriverName>>SimplePointerReset,
  <<DriverName>>SimplePointerGetState,
  NULL,
  NULL
};

/**                                                                 
  Resets the pointer device hardware.
    
  @param  This                  A pointer to the EFI_SIMPLE_POINTER_PROTOCOL
                                instance.                                   
  @param  ExtendedVerification  Indicates that the driver may perform a more exhaustive
                                verification operation of the device during reset.                                       
                                
  @retval EFI_SUCCESS           The device was reset.
  @retval EFI_DEVICE_ERROR      The device is not functioning correctly and could not be reset.  
                                   
**/
EFI_STATUS
EFIAPI
<<DriverName>>SimplePointerReset (
  IN EFI_SIMPLE_POINTER_PROTOCOL            *This,
  IN BOOLEAN                                ExtendedVerification
  )
{
  return EFI_DEVICE_ERROR;
}

/**                                                                 
  Retrieves the current state of a pointer device.
    
  @param  This                  A pointer to the EFI_SIMPLE_POINTER_PROTOCOL
                                instance.                                   
  @param  State                 A pointer to the state information on the pointer device.
                                
  @retval EFI_SUCCESS           The state of the pointer device was returned in State.
  @retval EFI_NOT_READY         The state of the pointer device has not changed since the last call to
                                GetState().                                                           
  @retval EFI_DEVICE_ERROR      A device error occurred while attempting to retrieve the pointer device's
                                current state.                                                           
                                   
**/
EFI_STATUS
EFIAPI
<<DriverName>>SimplePointerGetState (
  IN EFI_SIMPLE_POINTER_PROTOCOL          *This,
  IN OUT EFI_SIMPLE_POINTER_STATE         *State
  )
{
  return EFI_NOT_READY;
}
