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
  Retrieves the health status of a controller in the platform.  This function can also 
  optionally return warning messages, error messages, and a set of HII Forms that may 
  be repair a controller that is not proper configured. 
  
  @param[in] This             A pointer to the EFI_DRIVER_HEALTH_PROTOCOL instance.

  @param[in] ControllerHandle The handle of the controller to retrieve the health status 
                              on.  This is an optional parameter that may be NULL.  If 
                              this parameter is NULL, then the value of ChildHandle is 
                              ignored, and the combined health status of all the devices 
                              that the driver is managing is returned.

  @param[in] ChildHandle      The handle of the child controller to retrieve the health 
                              status on.  This is an optional parameter that may be NULL.  
                              This parameter is ignored of ControllerHandle is NULL.  It 
                              will be NULL for device drivers.  It will also be NULL for 
                              bus drivers when an attempt is made to collect the health 
                              status of the bus controller.  If will not be NULL when an 
                              attempt is made to collect the health status for a child 
                              controller produced by the driver.

  @param[out] HealthStatus    A pointer to the health status that is returned by this 
                              function.  This is an optional parameter that may be NULL.  
                              This parameter is ignored of ControllerHandle is NULL.  
                              The health status for the controller specified by 
                              ControllerHandle and ChildHandle is returned. 

  @param[out] MessageList     A pointer to an array of warning or error messages associated 
                              with the controller specified by ControllerHandle and 
                              ChildHandle.  This is an optional parameter that may be NULL.  
                              MessageList is allocated by this function with the EFI Boot 
                              Service AllocatePool(), and it is the caller's responsibility 
                              to free MessageList with the EFI Boot Service FreePool().  
                              Each message is specified by tuple of an EFI_HII_HANDLE and 
                              an EFI_STRING_ID.  The array of messages is terminated by tuple 
                              containing a EFI_HII_HANDLE with a value of NULL.  The 
                              EFI_HII_STRING_PROTOCOL.GetString() function can be used to 
                              retrieve the warning or error message as a Null-terminated 
                              string in a specific language.  Messages may be 
                              returned for any of the HealthStatus values except 
                              EfiDriverHealthStatusReconnectRequired and 
                              EfiDriverHealthStatusRebootRequired.

  @param[out] FormHiiHandle   A pointer to the HII handle containing the HII form used when 
                              configuration is required. The HII handle is associated with 
                              the controller specified by ControllerHandle and ChildHandle.
                              If this is NULL, then no HII form is available. An HII handle
                              will only be returned with a HealthStatus value of 
                              EfiDriverHealthStatusConfigurationRequired.

  @retval EFI_SUCCESS           ControllerHandle is NULL, and all the controllers 
                                managed by this driver specified by This have a health 
                                status of EfiDriverHealthStatusHealthy with no warning 
                                messages to be returned.  The ChildHandle, HealthStatus, 
                                MessageList, and FormList parameters are ignored.

  @retval EFI_DEVICE_ERROR      ControllerHandle is NULL, and one or more of the 
                                controllers managed by this driver specified by This 
                                do not have a health status of EfiDriverHealthStatusHealthy.  
                                The ChildHandle, HealthStatus, MessageList, and 
                                FormList parameters are ignored.

  @retval EFI_DEVICE_ERROR      ControllerHandle is NULL, and one or more of the 
                                controllers managed by this driver specified by This 
                                have one or more warning and/or error messages.  
                                The ChildHandle, HealthStatus, MessageList, and 
                                FormList parameters are ignored.

  @retval EFI_SUCCESS           ControllerHandle is not NULL and the health status 
                                of the controller specified by ControllerHandle and 
                                ChildHandle was returned in HealthStatus.  A list 
                                of warning and error messages may be optionally 
                                returned in MessageList, and a list of HII Forms 
                                may be optionally returned in FormList.

  @retval EFI_UNSUPPORTED       ControllerHandle is not NULL, and the controller 
                                specified by ControllerHandle and ChildHandle is not 
                                currently being managed by the driver specified by This.

  @retval EFI_INVALID_PARAMETER HealthStatus is NULL.

  @retval EFI_OUT_OF_RESOURCES  MessageList is not NULL, and there are not enough 
                                resource available to allocate memory for MessageList.

**/
EFI_STATUS
EFIAPI
<<DriverName>>DriverHealthGetHealthStatus (
  IN  EFI_DRIVER_HEALTH_PROTOCOL       *This,
  IN  EFI_HANDLE                       ControllerHandle OPTIONAL,
  IN  EFI_HANDLE                       ChildHandle      OPTIONAL,
  OUT EFI_DRIVER_HEALTH_STATUS         *HealthStatus,
  OUT EFI_DRIVER_HEALTH_HII_MESSAGE    **MessageList    OPTIONAL,
  OUT EFI_HII_HANDLE                   *FormHiiHandle   OPTIONAL
  );

/**
  Performs a repair operation on a controller in the platform.  This function can 
  optionally report repair progress information back to the platform. 
  
  @param[in] This                  A pointer to the EFI_DRIVER_HEALTH_PROTOCOL instance.
  @param[in] ControllerHandle      The handle of the controller to repair.
  @param[in] ChildHandle           The handle of the child controller to repair.  This is 
                                   an optional parameter that may be NULL.  It will be NULL 
                                   for device drivers.  It will also be NULL for bus 
                                   drivers when an attempt is made to repair a bus controller.
                                   If will not be NULL when an attempt is made to repair a 
                                   child controller produced by the driver.
  @param[in] ProgressNotification  A notification function that may be used by a driver to 
                                   report the progress of the repair operation.  This is 
                                   an optional parameter that may be NULL.  


  @retval EFI_SUCCESS           An attempt to repair the controller specified by 
                                ControllerHandle and ChildHandle was performed.  
                                The result of the repair operation can bet 
                                determined by calling GetHealthStatus().
  @retval EFI_UNSUPPORTED       The driver specified by This is not currently 
                                managing the controller specified by ControllerHandle 
                                and ChildHandle.
  @retval EFI_OUT_OF_RESOURCES  There are not enough resources to perform the 
                                repair operation.

*/
EFI_STATUS
EFIAPI
<<DriverName>>DriverHealthRepair (
  IN  EFI_DRIVER_HEALTH_PROTOCOL                *This,
  IN  EFI_HANDLE                                ControllerHandle,
  IN  EFI_HANDLE                                ChildHandle          OPTIONAL,
  IN  EFI_DRIVER_HEALTH_REPAIR_PROGRESS_NOTIFY  ProgressNotification OPTIONAL
  );
