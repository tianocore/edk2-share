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
EFI_ABSOLUTE_POINTER_PROTOCOL  g<<DriverName>>AbsolutePointer =  {
  <<DriverName>>AbsolutePointerReset,
  <<DriverName>>AbsolutePointerGetState,
  NULL,
  NULL
};

/**
  This function resets the pointer device hardware. As part of
  initialization process, the firmware/device will make a quick
  but reasonable attempt to verify that the device is
  functioning. If the ExtendedVerification flag is TRUE the
  firmware may take an extended amount of time to verify the
  device is operating on reset. Otherwise the reset operation is
  to occur as quickly as possible. The hardware verification
  process is not defined by this specification and is left up to
  the platform firmware or driver to implement.

  @param This                 A pointer to the EFI_ABSOLUTE_POINTER_PROTOCOL
                              instance.

  @param ExtendedVerification Indicates that the driver may
                              perform a more exhaustive
                              verification operation of the
                              device during reset.

  @retval EFI_SUCCESS       The device was reset.
  
  @retval EFI_DEVICE_ERROR  The device is not functioning
                            correctly and could not be reset.

**/
EFI_STATUS
EFIAPI
<<DriverName>>AbsolutePointerReset (
  IN EFI_ABSOLUTE_POINTER_PROTOCOL *This,
  IN BOOLEAN                       ExtendedVerification
  )
{
  return EFI_DEVICE_ERROR;
}

/**
  The GetState() function retrieves the current state of a pointer
  device. This includes information on the active state associated
  with the pointer device and the current position of the axes
  associated with the pointer device. If the state of the pointer
  device has not changed since the last call to GetState(), then
  EFI_NOT_READY is returned. If the state of the pointer device
  has changed since the last call to GetState(), then the state
  information is placed in State, and EFI_SUCCESS is returned. If
  a device error occurs while attempting to retrieve the state
  information, then EFI_DEVICE_ERROR is returned.


  @param This   A pointer to the EFI_ABSOLUTE_POINTER_PROTOCOL
                instance.

  @param State  A pointer to the state information on the
                pointer device.

  @retval EFI_SUCCESS       The state of the pointer device was
                            returned in State.

  @retval EFI_NOT_READY     The state of the pointer device has not
                            changed since the last call to GetState().

  @retval EFI_DEVICE_ERROR  A device error occurred while
                            attempting to retrieve the pointer
                            device's current state.

**/
EFI_STATUS
EFIAPI
<<DriverName>>AbsolutePointerGetState (
  IN      EFI_ABSOLUTE_POINTER_PROTOCOL  *This,
  IN OUT  EFI_ABSOLUTE_POINTER_STATE     *State
  )
{
  return EFI_NOT_READY;
}
