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
/// Driver Diagnostics Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED
EFI_DRIVER_DIAGNOSTICS_PROTOCOL g<<DriverName>>DriverDiagnostics = {
  (EFI_DRIVER_DIAGNOSTICS_RUN_DIAGNOSTICS)<<DriverName>>DriverDiagnosticsRunDiagnostics,
  "<<Iso639SupportedLanguages>>"
};

///
/// Driver Diagnostics 2 Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED
EFI_DRIVER_DIAGNOSTICS2_PROTOCOL g<<DriverName>>DriverDiagnostics2 = {
  <<DriverName>>DriverDiagnosticsRunDiagnostics,
  "<<Rfc4646SupportedLanguages>>"
};

/**
  Runs diagnostics on a controller.

  @param  This             A pointer to the EFI_DRIVER_DIAGNOSTICS2_PROTOCOL instance.
  @param  ControllerHandle The handle of the controller to run diagnostics on.
  @param  ChildHandle      The handle of the child controller to run diagnostics on
                           This is an optional parameter that may be NULL.  It will
                           be NULL for device drivers.  It will also be NULL for
                           bus drivers that wish to run diagnostics on the bus
                           controller.  It will not be NULL for a bus driver that
                           wishes to run diagnostics on one of its child controllers.
  @param  DiagnosticType   Indicates the type of diagnostics to perform on the controller
                           specified by ControllerHandle and ChildHandle.   See
                           "Related Definitions" for the list of supported types.
  @param  Language         A pointer to a Null-terminated ASCII string
                           array indicating the language. This is the
                           language of the driver name that the caller
                           is requesting, and it must match one of the
                           languages specified in SupportedLanguages.
                           The number of languages supported by a
                           driver is up to the driver writer. Language
                           is specified in RFC 4646 language code format.
  @param  ErrorType        A GUID that defines the format of the data returned in Buffer.
  @param  BufferSize       The size, in bytes, of the data returned in Buffer.
  @param  Buffer           A buffer that contains a Null-terminated Unicode string
                           plus some additional data whose format is defined by
                           ErrorType.  Buffer is allocated by this function with
                           AllocatePool(), and it is the caller's responsibility
                           to free it with a call to FreePool().

  @retval EFI_SUCCESS           The controller specified by ControllerHandle and
                                ChildHandle passed the diagnostic.
  @retval EFI_ACCESS_DENIED     The request for initiating diagnostics was unable
                                to be complete due to some underlying hardware or
                                software state.
  @retval EFI_INVALID_PARAMETER ControllerHandle is NULL.
  @retval EFI_INVALID_PARAMETER ChildHandle is not NULL and it is not a valid EFI_HANDLE.
  @retval EFI_INVALID_PARAMETER Language is NULL.
  @retval EFI_INVALID_PARAMETER ErrorType is NULL.
  @retval EFI_INVALID_PARAMETER BufferType is NULL.
  @retval EFI_INVALID_PARAMETER Buffer is NULL.
  @retval EFI_UNSUPPORTED       The driver specified by This does not support
                                running diagnostics for the controller specified
                                by ControllerHandle and ChildHandle.
  @retval EFI_UNSUPPORTED       The driver specified by This does not support the
                                type of diagnostic specified by DiagnosticType.
  @retval EFI_UNSUPPORTED       The driver specified by This does not support the
                                language specified by Language.
  @retval EFI_OUT_OF_RESOURCES  There are not enough resources available to complete
                                the diagnostics.
  @retval EFI_OUT_OF_RESOURCES  There are not enough resources available to return
                                the status information in ErrorType, BufferSize,
                                and Buffer.
  @retval EFI_DEVICE_ERROR      The controller specified by ControllerHandle and
                                ChildHandle did not pass the diagnostic.

**/
EFI_STATUS
EFIAPI
<<DriverName>>DriverDiagnosticsRunDiagnostics (
  IN EFI_DRIVER_DIAGNOSTICS2_PROTOCOL  *This,
  IN  EFI_HANDLE                       ControllerHandle,
  IN  EFI_HANDLE                       ChildHandle  OPTIONAL,
  IN  EFI_DRIVER_DIAGNOSTIC_TYPE       DiagnosticType,
  IN  CHAR8                            *Language,
  OUT EFI_GUID                         **ErrorType,
  OUT UINTN                            *BufferSize,
  OUT CHAR16                           **Buffer
  )
{
  EFI_STATUS  Status;
  CHAR8       *SupportedLanguages;
  BOOLEAN     Rfc4646Language;
  BOOLEAN     Found;
  UINTN       Index;
<<BEGIN>><<UefiDriverModelDeviceDriverEnabled>>
  //
  // ChildHandle must be NULL for a Device Driver
  //
  if (ChildHandle != NULL) {
    return EFI_UNSUPPORTED;
  }

  //
  // Make sure this driver is currently managing ControllerHandle
  //
  Status = EfiTestManagedDevice (
             ControllerHandle,
             g<<DriverName>>DriverBinding.DriverBindingHandle,
             &<<ConsumedProtocol>>
             );
  if (EFI_ERROR (Status)) {
    return Status;
  }

  //
  // Check input parameters
  //
  if (Language         == NULL ||
      ErrorType        == NULL ||
      BufferSize       == NULL ||
      Buffer           == NULL    ) {
    return EFI_INVALID_PARAMETER;
  }

  //
  // Make sure Language is in the set of Supported Languages
  //
  SupportedLanguages = This->SupportedLanguages;
  Rfc4646Language = (BOOLEAN)(This == &g<<DriverName>>DriverDiagnostics2);
  Found = FALSE;
  while (*SupportedLanguages != 0) {
    if (Rfc4646Language) {
      for (Index = 0;
           SupportedLanguages[Index] != 0 && SupportedLanguages[Index] != ';';
           Index++);
      if ((AsciiStrnCmp(SupportedLanguages, Language, Index) == 0) &&
          (Language[Index] == 0)) {
        Found = TRUE;
        break;
      }
      SupportedLanguages += Index;
      for (; *SupportedLanguages != 0 && *SupportedLanguages == ';';
           SupportedLanguages++);
    } else {
      if (CompareMem (Language, SupportedLanguages, 3) == 0) {
        Found = TRUE;
        break;
      }
      SupportedLanguages += 3;
    }
  }
  //
  // If Language is not a member of SupportedLanguages, then return EFI_UNSUPPORTED
  //
  if (!Found) {
    return EFI_UNSUPPORTED;
  }

  //
  // Perform Diagnostics Algorithm on ControllerHandle for the
  // type of diagnostics requested in DiagnosticsType
  //
  // Return results in ErrorType, Buffer, and BufferSize
  //
  // If Diagnostics Algorithm fails, then return EFI_DEVICE_ERROR
  //
  Status = EFI_DEVICE_ERROR;
<<END>>
<<BEGIN>><<UefiDriverModelBusDriverEnabled>>
  //
  // Make sure this driver is currently managing ControllerHandle
  //
  Status = EfiTestManagedDevice (
             ControllerHandle,
             g<<DriverName>>DriverBinding.DriverBindingHandle,
             &<<ConsumedProtocol>>
             );
  if (EFI_ERROR (Status)) {
    return Status;
  }

  //
  // If ChildHandle is not NULL, then make sure this driver produced ChildHandle
  //
  if (ChildHandle != NULL) {
    Status = EfiTestChildHandle (
               ControllerHandle,
               ChildHandle,
               &<<ConsumedProtocol>>
               );
    if (EFI_ERROR (Status)) {
      return Status;
    }
  }

  //
  // Check input parameters
  //
  if (Language         == NULL ||
      ErrorType        == NULL ||
      BufferSize       == NULL ||
      Buffer           == NULL    ) {
    return EFI_INVALID_PARAMETER;
  }

  //
  // Make sure Language is in the set of Supported Languages
  //
  SupportedLanguages = This->SupportedLanguages;
  Rfc4646Language = (BOOLEAN)(This == &g<<DriverName>>DriverDiagnostics2);
  Found = FALSE;
  while (*SupportedLanguages != 0) {
    if (Rfc4646Language) {
      for (Index = 0;
           SupportedLanguages[Index] != 0 && SupportedLanguages[Index] != ';';
           Index++);
      if ((AsciiStrnCmp(SupportedLanguages, Language, Index) == 0) &&
          (Language[Index] == 0)) {
        Found = TRUE;
        break;
      }
      SupportedLanguages += Index;
      for (; *SupportedLanguages != 0 && *SupportedLanguages == ';';
           SupportedLanguages++);
    } else {
      if (CompareMem (Language, SupportedLanguages, 3) == 0) {
        Found = TRUE;
        break;
      }
      SupportedLanguages += 3;
    }
  }
  //
  // If Language is not a member of SupportedLanguages, then return EFI_UNSUPPORTED
  //
  if (!Found) {
    return EFI_UNSUPPORTED;
  }

  if (ChildHandle == NULL) {
    //
    // Perform Diagnostics Algorithm on the bus controller specified
    // by ControllerHandle for the type of diagnostics requested in
    // DiagnosticsType
    //
    // Return results in ErrorType, Buffer, and BufferSize
    //
    // If Diagnostics Algorithm fails, then return EFI_DEVICE_ERROR
    //
    Status = EFI_DEVICE_ERROR;
  } else {
    //
    // Perform Diagnostics Algorithm on child controller specified
    // by ChildHandle for the type of diagnostics requested in
    // DiagnosticsType
    //
    // Return results in ErrorType, Buffer, and BufferSize
    //
    // If Diagnostics Algorithm fails, then return EFI_DEVICE_ERROR
    //
    Status = EFI_DEVICE_ERROR;
  }

<<END>>
  return Status;
}
