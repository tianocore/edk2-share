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
/// Simple Text Input Ex Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED 
EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL  g<<DriverName>>SimpleTextInputEx = {
  <<DriverName>>SimpleTextInputReset,
  <<DriverName>>SimpleTextInputReadKeyStrokeEx,
  NULL,
  <<DriverName>>SimpleTextInputSetState,
  <<DriverName>>SimpleTextInputRegisterKeyNotify,
  <<DriverName>>SimpleTextInputUnregisterKeyNotify
};

///
/// Simple Text Input Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED 
EFI_SIMPLE_TEXT_INPUT_PROTOCOL  g<<DriverName>>SimpleTextInput = {
  (EFI_INPUT_RESET)<<DriverName>>SimpleTextInputReset,
  <<DriverName>>SimpleTextInputReadKeyStroke,
  NULL
};

/**
  The Reset() function resets the input device hardware. As part
  of initialization process, the firmware/device will make a quick
  but reasonable attempt to verify that the device is functioning.
  If the ExtendedVerification flag is TRUE the firmware may take
  an extended amount of time to verify the device is operating on
  reset. Otherwise the reset operation is to occur as quickly as
  possible. The hardware verification process is not defined by
  this specification and is left up to the platform firmware or
  driver to implement.

  @param This                 A pointer to the EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL instance.

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
<<DriverName>>SimpleTextInputReset (
  IN EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL *This,
  IN BOOLEAN                           ExtendedVerification
  )
{
  return EFI_DEVICE_ERROR;
}

/**
  The function reads the next keystroke from the input device. If
  there is no pending keystroke the function returns
  EFI_NOT_READY. If there is a pending keystroke, then
  KeyData.Key.ScanCode is the EFI scan code defined in Error!
  Reference source not found. The KeyData.Key.UnicodeChar is the
  actual printable character or is zero if the key does not
  represent a printable character (control key, function key,
  etc.). The KeyData.KeyState is shift state for the character
  reflected in KeyData.Key.UnicodeChar or KeyData.Key.ScanCode .
  When interpreting the data from this function, it should be
  noted that if a class of printable characters that are
  normally adjusted by shift modifiers (e.g. Shift Key + "f"
  key) would be presented solely as a KeyData.Key.UnicodeChar
  without the associated shift state. So in the previous example
  of a Shift Key + "f" key being pressed, the only pertinent
  data returned would be KeyData.Key.UnicodeChar with the value
  of "F". This of course would not typically be the case for
  non-printable characters such as the pressing of the Right
  Shift Key + F10 key since the corresponding returned data
  would be reflected both in the KeyData.KeyState.KeyShiftState
  and KeyData.Key.ScanCode values. UEFI drivers which implement
  the EFI_SIMPLE_TEXT_INPUT_EX protocol are required to return
  KeyData.Key and KeyData.KeyState values. These drivers must
  always return the most current state of
  KeyData.KeyState.KeyShiftState and
  KeyData.KeyState.KeyToggleState. It should also be noted that
  certain input devices may not be able to produce shift or toggle
  state information, and in those cases the high order bit in the
  respective Toggle and Shift state fields should not be active.


  @param This     A pointer to the EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL instance.

  @param KeyData  A pointer to a buffer that is filled in with
                  the keystroke state data for the key that was
                  pressed.


  @retval EFI_SUCCESS     The keystroke information was
                          returned.

  @retval EFI_NOT_READY   There was no keystroke data available.
                          EFI_DEVICE_ERROR The keystroke
                          information was not returned due to
                          hardware errors.


**/
EFI_STATUS
EFIAPI
<<DriverName>>SimpleTextInputReadKeyStrokeEx (
  IN  EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL *This,
  OUT EFI_KEY_DATA                      *KeyData
  )
{
  return EFI_NOT_READY;
}

/**
  The SetState() function allows the input device hardware to
  have state settings adjusted.

  @param This           A pointer to the EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL instance.

  @param KeyToggleState Pointer to the EFI_KEY_TOGGLE_STATE to
                        set the state for the input device.


  @retval EFI_SUCCESS       The device state was set appropriately.

  @retval EFI_DEVICE_ERROR  The device is not functioning
                            correctly and could not have the
                            setting adjusted.

  @retval EFI_UNSUPPORTED   The device does not support the
                            ability to have its state set.

**/
EFI_STATUS
EFIAPI
<<DriverName>>SimpleTextInputSetState (
  IN EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL *This,
  IN EFI_KEY_TOGGLE_STATE              *KeyToggleState
  )
{
  return EFI_UNSUPPORTED;
}

/**
  The RegisterKeystrokeNotify() function registers a function
  which will be called when a specified keystroke will occur.

  @param This                     A pointer to the EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL instance.

  @param KeyData                  A pointer to a buffer that is filled in with
                                  the keystroke information for the key that was
                                  pressed.

  @param KeyNotificationFunction  Points to the function to be
                                  called when the key sequence
                                  is typed specified by KeyData.


  @param NotifyHandle             Points to the unique handle assigned to
                                  the registered notification.

  @retval EFI_SUCCESS           The device state was set
                                appropriately.

  @retval EFI_OUT_OF_RESOURCES  Unable to allocate necessary
                                data structures.

**/
EFI_STATUS
EFIAPI
<<DriverName>>SimpleTextInputRegisterKeyNotify (
  IN  EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL *This,
  IN  EFI_KEY_DATA                      *KeyData,
  IN  EFI_KEY_NOTIFY_FUNCTION           KeyNotificationFunction,
  OUT EFI_HANDLE                        *NotifyHandle
  )
{
  return EFI_OUT_OF_RESOURCES;
}

/**
  The UnregisterKeystrokeNotify() function removes the
  notification which was previously registered.

  @param This               A pointer to the EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL instance.

  @param NotificationHandle The handle of the notification
                            function being unregistered.

  @retval EFI_SUCCESS The device state was set appropriately.

  @retval EFI_INVALID_PARAMETER The NotificationHandle is
                                invalid.

**/
EFI_STATUS
EFIAPI
<<DriverName>>SimpleTextInputUnregisterKeyNotify (
  IN EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL  *This,
  IN EFI_HANDLE                         NotificationHandle
  )
{
  return EFI_INVALID_PARAMETER;
}

/**
  Reads the next keystroke from the input device. The WaitForKey Event can
  be used to test for existence of a keystroke via WaitForEvent () call.

  @param  This  Protocol instance pointer.
  @param  Key   A pointer to a buffer that is filled in with the keystroke
                information for the key that was pressed.

  @retval EFI_SUCCESS      The keystroke information was returned.
  @retval EFI_NOT_READY    There was no keystroke data available.
  @retval EFI_DEVICE_ERROR The keystroke information was not returned due to
                           hardware errors.

**/
EFI_STATUS
EFIAPI
<<DriverName>>SimpleTextInputReadKeyStroke (
  IN EFI_SIMPLE_TEXT_INPUT_PROTOCOL       *This,
  OUT EFI_INPUT_KEY                       *Key
  )
{
  return EFI_NOT_READY;
}
