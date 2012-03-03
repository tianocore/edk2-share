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

<<BEGIN>><<UefiRuntimeDriverEnabled>>
///
/// Global variable for Exit Boot Services event.
///
EFI_EVENT  mExitBootServicesEvent = NULL;

///
/// Global variable for Set Virtual Address Map event.
///
EFI_EVENT  mSetVirtualAddressMapEvent = NULL;

<<END>>
<<BEGIN>><<DriverSupportedEfiVersionEnabled>>
///
/// Driver Support EFI Version Protocol instance
///
GLOBAL_REMOVE_IF_UNREFERENCED 
EFI_DRIVER_SUPPORTED_EFI_VERSION_PROTOCOL g<<DriverName>>DriverSupportedEfiVersion = {
  sizeof (EFI_DRIVER_SUPPORTED_EFI_VERSION_PROTOCOL),
  <<UEFI_SYSTEM_TABLE_REVISON>>
};

<<END>>
<<BEGIN>><<UefiDriverModelEnabled>>
///
/// Driver Binding Protocol instance
///
EFI_DRIVER_BINDING_PROTOCOL g<<DriverName>>DriverBinding = {
  <<DriverName>>DriverBindingSupported,
  <<DriverName>>DriverBindingStart,
  <<DriverName>>DriverBindingStop,
  <<DRIVER_NAME>>_VERSION,
  NULL,
  NULL
};

<<END>>
<<BEGIN>><<UefiRuntimeDriverEnabled>>
/**
  Notification function that is invoked when ExitBootServices() is called.

  @param  Event    Event whose notification function is being invoked.
  @param  Context  The pointer to the notification function's context,
                   which is implementation-dependent.

**/
VOID
EFIAPI
<<DriverName>>NotifyExitBootServices (
  IN EFI_EVENT  Event,
  IN VOID       *Context
  )
{
}

/**
  Notification function that is invoked when SetVirtualAddressMap() is called.

  @param  Event    Event whose notification function is being invoked.
  @param  Context  The pointer to the notification function's context,
                   which is implementation-dependent.

**/
VOID
EFIAPI
<<DriverName>>NotifySetVirtualAddressMap (
  IN EFI_EVENT  Event,
  IN VOID       *Context
  )
{
}

<<END>>
/**
  Unloads an image.

  @param  ImageHandle           Handle that identifies the image to be unloaded.

  @retval EFI_SUCCESS           The image has been unloaded.
  @retval EFI_INVALID_PARAMETER ImageHandle is not a valid image handle.

**/
EFI_STATUS 
EFIAPI
<<DriverName>>Unload (
  IN EFI_HANDLE  ImageHandle
  )
{
  EFI_STATUS  Status;
<<BEGIN>><<UefiDriverModelEnabled>>
  EFI_HANDLE  *HandleBuffer;
  UINTN       HandleCount;
  UINTN       Index;
<<END>>

  Status = EFI_SUCCESS;
<<BEGIN>><<UefiDriverModelEnabled>>
  //
  // Retrieve array of all handles in the handle database
  //
  Status = gBS->LocateHandleBuffer (
                  AllHandles,
                  NULL,
                  NULL,
                  &HandleCount,
                  &HandleBuffer
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

  //
  // Disconnect the current driver from handles in the handle database 
  //
  for (Index = 0; Index < HandleCount; Index++) {
    Status = gBS->DisconnectController (HandleBuffer[Index], gImageHandle, NULL);
  }

  //
  // Free the array of handles
  //
  FreePool (HandleBuffer);

<<END>>
<<BEGIN>><<UefiRuntimeDriverEnabled>>
  //
  // Close Exit Boot Services event.
  // 
  Status = gBS->CloseEvent (mExitBootServicesEvent);
  if (EFI_ERROR (Status)) {
    return Status;
  }

  //
  // Close Set Virtual Address Map event.
  // 
  Status = gBS->CloseEvent (mSetVirtualAddressMapEvent);
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallDriverBinding>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid, &g<<DriverName>>DriverBinding,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallDriverBindingComponentName2>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid,  &g<<DriverName>>DriverBinding,
                  &gEfiComponentNameProtocolGuid,  &g<<DriverName>>ComponentName,
                  &gEfiComponentName2ProtocolGuid, &g<<DriverName>>ComponentName2,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_011>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid,        &g<<DriverName>>DriverBinding,
                  &gEfiDriverConfigurationProtocolGuid,  &g<<DriverName>>DriverConfiguration,
                  &gEfiDriverConfiguration2ProtocolGuid, &g<<DriverName>>DriverConfiguration2,
                  &gEfiDriverDiagnosticsProtocolGuid,    &g<<DriverName>>DriverDiagnostics,
                  &gEfiDriverDiagnostics2ProtocolGuid,   &g<<DriverName>>DriverDiagnostics2,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_010>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid,        &g<<DriverName>>DriverBinding,
                  &gEfiDriverConfigurationProtocolGuid,  &g<<DriverName>>DriverConfiguration,
                  &gEfiDriverConfiguration2ProtocolGuid, &g<<DriverName>>DriverConfiguration2,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_001>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid,      &g<<DriverName>>DriverBinding,
                  &gEfiDriverDiagnosticsProtocolGuid,  &g<<DriverName>>DriverDiagnostics,
                  &gEfiDriverDiagnostics2ProtocolGuid, &g<<DriverName>>DriverDiagnostics2,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_101>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid,      &g<<DriverName>>DriverBinding,
                  &gEfiComponentNameProtocolGuid,      &g<<DriverName>>ComponentName,
                  &gEfiComponentName2ProtocolGuid,     &g<<DriverName>>ComponentName2,
                  &gEfiDriverDiagnosticsProtocolGuid,  &g<<DriverName>>DriverDiagnostics,
                  &gEfiDriverDiagnostics2ProtocolGuid, &g<<DriverName>>DriverDiagnostics2,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_110>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid,        &g<<DriverName>>DriverBinding,
                  &gEfiComponentNameProtocolGuid,        &g<<DriverName>>ComponentName,
                  &gEfiComponentName2ProtocolGuid,       &g<<DriverName>>ComponentName2,
                  &gEfiDriverConfigurationProtocolGuid,  &g<<DriverName>>DriverConfiguration,
                  &gEfiDriverConfiguration2ProtocolGuid, &g<<DriverName>>DriverConfiguration2,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_111>>
  //
  // Uninstall protocols installed in the driver entry point
  // 
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverBindingProtocolGuid,        &g<<DriverName>>DriverBinding,
                  &gEfiComponentNameProtocolGuid,        &g<<DriverName>>ComponentName,
                  &gEfiComponentName2ProtocolGuid,       &g<<DriverName>>ComponentName2,
                  &gEfiDriverConfigurationProtocolGuid,  &g<<DriverName>>DriverConfiguration,
                  &gEfiDriverConfiguration2ProtocolGuid, &g<<DriverName>>DriverConfiguration2,
                  &gEfiDriverDiagnosticsProtocolGuid,    &g<<DriverName>>DriverDiagnostics,
                  &gEfiDriverDiagnostics2ProtocolGuid,   &g<<DriverName>>DriverDiagnostics2,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<DriverSupportedEfiVersionEnabled>>
  //
  // Uninstall Driver Supported EFI Version Protocol onto ImageHandle
  //
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverSupportedEfiVersionProtocolGuid, &g<<DriverName>>DriverSupportedEfiVersion,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<DriverHealthEnabled>>
  //
  // Uninstall Driver Health Protocol onto ImageHandle
  //
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverHealthProtocolGuid, &g<<DriverName>>DriverHealth,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
<<BEGIN>><<DriverFamilyOverrideEnabled>>
  //
  // Uninstall Driver Family Override Protocol onto ImageHandle
  //
  Status = gBS->UninstallMultipleProtocolInterfaces (
                  ImageHandle,
                  &gEfiDriverFamilyOverrideProtocolGuid, &g<<DriverName>>DriverFamilyOverride,
                  NULL
                  );
  if (EFI_ERROR (Status)) {
    return Status;
  }

<<END>>
  //
  // Do any additional cleanup that is required for this driver
  //

  return EFI_SUCCESS;
}

/**
  This is the declaration of an EFI image entry point. This entry point is
  the same for UEFI Applications, UEFI OS Loaders, and UEFI Drivers including
  both device drivers and bus drivers.

  @param  ImageHandle           The firmware allocated handle for the UEFI image.
  @param  SystemTable           A pointer to the EFI System Table.

  @retval EFI_SUCCESS           The operation completed successfully.
  @retval Others                An unexpected error occurred.
**/
EFI_STATUS
EFIAPI
<<DriverName>>DriverEntryPoint (
  IN EFI_HANDLE        ImageHandle,
  IN EFI_SYSTEM_TABLE  *SystemTable
  )
{
  EFI_STATUS  Status;
<<BEGIN>><<HiiEnabled>>
  EFI_HII_PACKAGE_LIST_HEADER  *PackageListHeader;
  EFI_HII_DATABASE_PROTOCOL    *HiiDatabase;
  EFI_HII_HANDLE               HiiHandle;
<<END>>

  Status = EFI_SUCCESS;

<<BEGIN>><<UefiRuntimeDriverEnabled>>
  //
  // Create an Exit Boot Services event.
  // 
  Status = gBS->CreateEvent (
                  EVT_SIGNAL_EXIT_BOOT_SERVICES,         // Type
                  TPL_NOTIFY,                            // NotifyTpl
                  <<DriverName>>NotifyExitBootServices,  // NotifyFunction
                  NULL,                                  // NotifyContext
                  &mExitBootServicesEvent                // Event
                  );
  ASSERT_EFI_ERROR (Status);

  //
  // Create a Set Virtual Address Map event.
  // 
  Status = gBS->CreateEvent (
                  EVT_SIGNAL_VIRTUAL_ADDRESS_CHANGE,         // Type
                  TPL_NOTIFY,                                // NotifyTpl
                  <<DriverName>>NotifySetVirtualAddressMap,  // NotifyFunction
                  NULL,                                      // NotifyContext
                  &mSetVirtualAddressMapEvent                // Event
                  );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallDriverBinding>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallDriverBinding (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallDriverBindingComponentName2>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallDriverBindingComponentName2 (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle,
             &g<<DriverName>>ComponentName,
             &g<<DriverName>>ComponentName2
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_011>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallAllDriverProtocols2 (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle,
             NULL,
             NULL,
             &g<<DriverName>>DriverConfiguration,
             &g<<DriverName>>DriverConfiguration2,
             &g<<DriverName>>DriverDiagnostics,
             &g<<DriverName>>DriverDiagnostics2
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_010>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallAllDriverProtocols2 (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle,
             NULL,
             NULL,
             &g<<DriverName>>DriverConfiguration,
             &g<<DriverName>>DriverConfiguration2,
             NULL,
             NULL
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_001>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallAllDriverProtocols2 (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle,
             NULL,
             NULL,
             NULL,
             NULL,
             &g<<DriverName>>DriverDiagnostics,
             &g<<DriverName>>DriverDiagnostics2
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_101>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallAllDriverProtocols2 (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle,
             &g<<DriverName>>ComponentName,
             &g<<DriverName>>ComponentName2,
             NULL,
             NULL,
             &g<<DriverName>>DriverDiagnostics,
             &g<<DriverName>>DriverDiagnostics2
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_110>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallAllDriverProtocols2 (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle,
             &g<<DriverName>>ComponentName,
             &g<<DriverName>>ComponentName2,
             &g<<DriverName>>DriverConfiguration,
             &g<<DriverName>>DriverConfiguration2,
             NULL,
             NULL
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<EfiLibInstallAllDriverProtocols2_111>>
  //
  // Install UEFI Driver Model protocol(s).
  //
  Status = EfiLibInstallAllDriverProtocols2 (
             ImageHandle,
             SystemTable,
             &g<<DriverName>>DriverBinding,
             ImageHandle,
             &g<<DriverName>>ComponentName,
             &g<<DriverName>>ComponentName2,
             &g<<DriverName>>DriverConfiguration,
             &g<<DriverName>>DriverConfiguration2,
             &g<<DriverName>>DriverDiagnostics,
             &g<<DriverName>>DriverDiagnostics2
             );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<HiiEnabled>>
  //
  // Retrieve HII Package List Header on ImageHandle
  //
  Status = gBS->OpenProtocol (
                  ImageHandle,
                  &gEfiHiiPackageListProtocolGuid,
                  (VOID **)&PackageListHeader,
                  ImageHandle,
                  NULL,
                  EFI_OPEN_PROTOCOL_GET_PROTOCOL
                  );
  if (!EFI_ERROR (Status)) {
    //
    // Retrieve the pointer to the UEFI HII Database Protocol 
    //
    Status = gBS->LocateProtocol (
                    &gEfiHiiDatabaseProtocolGuid, 
                    NULL, 
                    (VOID **)&HiiDatabase
                    );
    if (!EFI_ERROR (Status)) {
      //
      // Register list of HII packages in the HII Database
      //
      Status = HiiDatabase->NewPackageList (
                              HiiDatabase, 
                              PackageListHeader,
                              NULL, 
                              &HiiHandle
                              );
      ASSERT_EFI_ERROR (Status);
    }
  }
  Status = EFI_SUCCESS;

<<END>>
<<BEGIN>><<DriverSupportedEfiVersionEnabled>>
  //
  // Install Driver Supported EFI Version Protocol onto ImageHandle
  //
  Status = gBS->InstallMultipleProtocolInterfaces (
                  &ImageHandle,
                  &gEfiDriverSupportedEfiVersionProtocolGuid, &g<<DriverName>>DriverSupportedEfiVersion,
                  NULL
                  );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<DriverHealthEnabled>>
  //
  // Install Driver Health Protocol onto ImageHandle
  //
  Status = gBS->InstallMultipleProtocolInterfaces (
                  &ImageHandle,
                  &gEfiDriverHealthProtocolGuid, &g<<DriverName>>DriverHealth,
                  NULL
                  );
  ASSERT_EFI_ERROR (Status);

<<END>>
<<BEGIN>><<DriverFamilyOverrideEnabled>>
  //
  // Install Driver Family Override Protocol onto ImageHandle
  //
  Status = gBS->InstallMultipleProtocolInterfaces (
                  &ImageHandle,
                  &gEfiDriverFamilyOverrideProtocolGuid, &g<<DriverName>>DriverFamilyOverride,
                  NULL
                  );
  ASSERT_EFI_ERROR (Status);

<<END>>
  return Status;
}

<<BEGIN>><<UefiDriverModelEnabled>>
/**
  Tests to see if this driver supports a given controller. If a child device is provided, 
  it further tests to see if this driver supports creating a handle for the specified child device.

  This function checks to see if the driver specified by This supports the device specified by 
  ControllerHandle. Drivers will typically use the device path attached to 
  ControllerHandle and/or the services from the bus I/O abstraction attached to 
  ControllerHandle to determine if the driver supports ControllerHandle. This function 
  may be called many times during platform initialization. In order to reduce boot times, the tests 
  performed by this function must be very small, and take as little time as possible to execute. This 
  function must not change the state of any hardware devices, and this function must be aware that the 
  device specified by ControllerHandle may already be managed by the same driver or a 
  different driver. This function must match its calls to AllocatePages() with FreePages(), 
  AllocatePool() with FreePool(), and OpenProtocol() with CloseProtocol().  
  Because ControllerHandle may have been previously started by the same driver, if a protocol is 
  already in the opened state, then it must not be closed with CloseProtocol(). This is required 
  to guarantee the state of ControllerHandle is not modified by this function.

  @param[in]  This                 A pointer to the EFI_DRIVER_BINDING_PROTOCOL instance.
  @param[in]  ControllerHandle     The handle of the controller to test. This handle 
                                   must support a protocol interface that supplies 
                                   an I/O abstraction to the driver.
  @param[in]  RemainingDevicePath  A pointer to the remaining portion of a device path.  This 
                                   parameter is ignored by device drivers, and is optional for bus 
                                   drivers. For bus drivers, if this parameter is not NULL, then 
                                   the bus driver must determine if the bus controller specified 
                                   by ControllerHandle and the child controller specified 
                                   by RemainingDevicePath are both supported by this 
                                   bus driver.

  @retval EFI_SUCCESS              The device specified by ControllerHandle and
                                   RemainingDevicePath is supported by the driver specified by This.
  @retval EFI_ALREADY_STARTED      The device specified by ControllerHandle and
                                   RemainingDevicePath is already being managed by the driver
                                   specified by This.
  @retval EFI_ACCESS_DENIED        The device specified by ControllerHandle and
                                   RemainingDevicePath is already being managed by a different
                                   driver or an application that requires exclusive access.
                                   Currently not implemented.
  @retval EFI_UNSUPPORTED          The device specified by ControllerHandle and
                                   RemainingDevicePath is not supported by the driver specified by This.
**/
EFI_STATUS
EFIAPI
<<DriverName>>DriverBindingSupported (
  IN EFI_DRIVER_BINDING_PROTOCOL  *This,
  IN EFI_HANDLE                   ControllerHandle,
  IN EFI_DEVICE_PATH_PROTOCOL     *RemainingDevicePath OPTIONAL
  )
{
  return EFI_UNSUPPORTED;
}

/**
  Starts a device controller or a bus controller.

  The Start() function is designed to be invoked from the EFI boot service ConnectController().
  As a result, much of the error checking on the parameters to Start() has been moved into this 
  common boot service. It is legal to call Start() from other locations, 
  but the following calling restrictions must be followed, or the system behavior will not be deterministic.
  1. ControllerHandle must be a valid EFI_HANDLE.
  2. If RemainingDevicePath is not NULL, then it must be a pointer to a naturally aligned
     EFI_DEVICE_PATH_PROTOCOL.
  3. Prior to calling Start(), the Supported() function for the driver specified by This must
     have been called with the same calling parameters, and Supported() must have returned EFI_SUCCESS.  

  @param[in]  This                 A pointer to the EFI_DRIVER_BINDING_PROTOCOL instance.
  @param[in]  ControllerHandle     The handle of the controller to start. This handle 
                                   must support a protocol interface that supplies 
                                   an I/O abstraction to the driver.
  @param[in]  RemainingDevicePath  A pointer to the remaining portion of a device path.  This 
                                   parameter is ignored by device drivers, and is optional for bus 
                                   drivers. For a bus driver, if this parameter is NULL, then handles 
                                   for all the children of Controller are created by this driver.  
                                   If this parameter is not NULL and the first Device Path Node is 
                                   not the End of Device Path Node, then only the handle for the 
                                   child device specified by the first Device Path Node of 
                                   RemainingDevicePath is created by this driver.
                                   If the first Device Path Node of RemainingDevicePath is 
                                   the End of Device Path Node, no child handle is created by this
                                   driver.

  @retval EFI_SUCCESS              The device was started.
  @retval EFI_DEVICE_ERROR         The device could not be started due to a device error.Currently not implemented.
  @retval EFI_OUT_OF_RESOURCES     The request could not be completed due to a lack of resources.
  @retval Others                   The driver failded to start the device.

**/
EFI_STATUS
EFIAPI
<<DriverName>>DriverBindingStart (
  IN EFI_DRIVER_BINDING_PROTOCOL  *This,
  IN EFI_HANDLE                   ControllerHandle,
  IN EFI_DEVICE_PATH_PROTOCOL     *RemainingDevicePath OPTIONAL
  )
{
  return EFI_UNSUPPORTED;
}

/**
  Stops a device controller or a bus controller.
  
  The Stop() function is designed to be invoked from the EFI boot service DisconnectController(). 
  As a result, much of the error checking on the parameters to Stop() has been moved 
  into this common boot service. It is legal to call Stop() from other locations, 
  but the following calling restrictions must be followed, or the system behavior will not be deterministic.
  1. ControllerHandle must be a valid EFI_HANDLE that was used on a previous call to this
     same driver's Start() function.
  2. The first NumberOfChildren handles of ChildHandleBuffer must all be a valid
     EFI_HANDLE. In addition, all of these handles must have been created in this driver's
     Start() function, and the Start() function must have called OpenProtocol() on
     ControllerHandle with an Attribute of EFI_OPEN_PROTOCOL_BY_CHILD_CONTROLLER.
  
  @param[in]  This              A pointer to the EFI_DRIVER_BINDING_PROTOCOL instance.
  @param[in]  ControllerHandle  A handle to the device being stopped. The handle must 
                                support a bus specific I/O protocol for the driver 
                                to use to stop the device.
  @param[in]  NumberOfChildren  The number of child device handles in ChildHandleBuffer.
  @param[in]  ChildHandleBuffer An array of child handles to be freed. May be NULL 
                                if NumberOfChildren is 0.

  @retval EFI_SUCCESS           The device was stopped.
  @retval EFI_DEVICE_ERROR      The device could not be stopped due to a device error.

**/
EFI_STATUS
EFIAPI
<<DriverName>>DriverBindingStop (
  IN EFI_DRIVER_BINDING_PROTOCOL  *This,
  IN EFI_HANDLE                   ControllerHandle,
  IN UINTN                        NumberOfChildren,
  IN EFI_HANDLE                   *ChildHandleBuffer OPTIONAL
  )
{
  return EFI_UNSUPPORTED;
}
<<END>>
