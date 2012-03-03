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
  Sends an ATA command to an ATA device that is attached to the ATA controller. This function
  supports both blocking I/O and non-blocking I/O. The blocking I/O functionality is required,
  and the non-blocking I/O functionality is optional.

  @param[in]     This                A pointer to the EFI_ATA_PASS_THRU_PROTOCOL instance. 
  @param[in]     Port                The port number of the ATA device to send the command. 
  @param[in]     PortMultiplierPort  The port multiplier port number of the ATA device to send the command.
                                     If there is no port multiplier, then specify 0.
  @param[in,out] Packet              A pointer to the ATA command to send to the ATA device specified by Port
                                     and PortMultiplierPort.
  @param[in]     Event               If non-blocking I/O is not supported then Event is ignored, and blocking
                                     I/O is performed. If Event is NULL, then blocking I/O is performed. If
                                     Event is not NULL and non blocking I/O is supported, then non-blocking
                                     I/O is performed, and Event will be signaled when the ATA command completes.

  @retval EFI_SUCCESS                The ATA command was sent by the host. For bi-directional commands, 
                                     InTransferLength bytes were transferred from InDataBuffer. For write and
                                     bi-directional commands, OutTransferLength bytes were transferred by OutDataBuffer.
  @retval EFI_BAD_BUFFER_SIZE        The ATA command was not executed. The number of bytes that could be transferred
                                     is returned in InTransferLength. For write and bi-directional commands, 
                                     OutTransferLength bytes were transferred by OutDataBuffer.
  @retval EFI_NOT_READY              The ATA command could not be sent because there are too many ATA commands
                                     already queued. The caller may retry again later.
  @retval EFI_DEVICE_ERROR           A device error occurred while attempting to send the ATA command.
  @retval EFI_INVALID_PARAMETER      Port, PortMultiplierPort, or the contents of Acb are invalid. The ATA
                                     command was not sent, so no additional status information is available.

**/
EFI_STATUS
EFIAPI
<<DriverName>>AtaPassThruPassThru (
  IN     EFI_ATA_PASS_THRU_PROTOCOL       *This,
  IN     UINT16                           Port,
  IN     UINT16                           PortMultiplierPort,
  IN OUT EFI_ATA_PASS_THRU_COMMAND_PACKET *Packet,
  IN     EFI_EVENT                        Event OPTIONAL
  );

/**
  Used to retrieve the lis t of legal port numbers for ATA devices on an ATA controller.
  These can either be the list of ports where ATA devices are actually present or the
  list of legal port numbers for the ATA controller. Regardless, the caller of this
  function must probe the port number returned to see if an ATA device is actually
  present at that location on the ATA controller.

  The GetNextPort() function retrieves the port number on an ATA controller. If on input
  Port is 0xFFFF, then the port number of the first port on the ATA controller is returned
  in Port and EFI_SUCCESS is returned.

  If Port is a port number that was returned on a previous call to GetNextPort(), then the
  port number of the next port on the ATA controller is returned in Port, and EFI_SUCCESS
  is returned. If Port is not 0xFFFF and Port was not returned on a previous call to
  GetNextPort(), then EFI_INVALID_PARAMETER is returned.

  If Port is the port number of the last port on the ATA controller, then EFI_NOT_FOUND is
  returned.

  @param[in]     This           A pointer to the EFI_ATA_PASS_THRU_PROTOCOL instance. 
  @param[in,out] Port           On input, a pointer to the port number on the ATA controller.
                                On output, a pointer to the next port number on the ATA
                                controller. An input value of 0xFFFF retrieves the first port
                                number on the ATA controller.

  @retval EFI_SUCCESS           The next port number on the ATA controller was returned in Port.
  @retval EFI_NOT_FOUND         There are no more ports on this ATA controller.
  @retval EFI_INVALID_PARAMETER Port is not 0xFFFF and Port was not returned on a previous call
                                to GetNextPort().

**/
EFI_STATUS
EFIAPI
<<DriverName>>AtaPassThruGetNextPort (
  IN EFI_ATA_PASS_THRU_PROTOCOL *This,
  IN OUT UINT16                 *Port
  );

/**
  Used to retrieve the list of legal port multiplier port numbers for ATA devices on a port of an ATA 
  controller. These can either be the list of port multiplier ports where ATA devices are actually 
  present on port or the list of legal port multiplier ports on that port. Regardless, the caller of this 
  function must probe the port number and port multiplier port number returned to see if an ATA 
  device is actually present.

  The GetNextDevice() function retrieves the port multiplier port number of an ATA device 
  present on a port of an ATA controller.
  
  If PortMultiplierPort points to a port multiplier port number value that was returned on a 
  previous call to GetNextDevice(), then the port multiplier port number of the next ATA device
  on the port of the ATA controller is returned in PortMultiplierPort, and EFI_SUCCESS is
  returned.
  
  If PortMultiplierPort points to 0xFFFF, then the port multiplier port number of the first 
  ATA device on port of the ATA controller is returned in PortMultiplierPort and 
  EFI_SUCCESS is returned.
  
  If PortMultiplierPort is not 0xFFFF and the value pointed to by PortMultiplierPort
  was not returned on a previous call to GetNextDevice(), then EFI_INVALID_PARAMETER
  is returned.
  
  If PortMultiplierPort is the port multiplier port number of the last ATA device on the port of 
  the ATA controller, then EFI_NOT_FOUND is returned.

  @param[in]     This                A pointer to the EFI_ATA_PASS_THRU_PROTOCOL instance.
  @param[in]     Port                The port number present on the ATA controller.
  @param[in,out] PortMultiplierPort  On input, a pointer to the port multiplier port number of an
                                     ATA device present on the ATA controller. 
                                     If on input a PortMultiplierPort of 0xFFFF is specified, 
                                     then the port multiplier port number of the first ATA device
                                     is returned. On output, a pointer to the port multiplier port
                                     number of the next ATA device present on an ATA controller.

  @retval EFI_SUCCESS                The port multiplier port number of the next ATA device on the port
                                     of the ATA controller was returned in PortMultiplierPort.
  @retval EFI_NOT_FOUND              There are no more ATA devices on this port of the ATA controller.
  @retval EFI_INVALID_PARAMETER      PortMultiplierPort is not 0xFFFF, and PortMultiplierPort was not
                                     returned on a previous call to GetNextDevice().

**/
EFI_STATUS
EFIAPI
<<DriverName>>AtaPassThruGetNextDevice (
  IN EFI_ATA_PASS_THRU_PROTOCOL *This,
  IN UINT16                     Port,
  IN OUT UINT16                 *PortMultiplierPort
  );

/**
  Used to allocate and build a device path node for an ATA device on an ATA controller.

  The BuildDevicePath() function allocates and builds a single device node for the ATA
  device specified by Port and PortMultiplierPort. If the ATA device specified by Port and
  PortMultiplierPort is not present on the ATA controller, then EFI_NOT_FOUND is returned.
  If DevicePath is NULL, then EFI_INVALID_PARAMETER is returned. If there are not enough
  resources to allocate the device path node, then EFI_OUT_OF_RESOURCES is returned.

  Otherwise, DevicePath is allocated with the boot service AllocatePool(), the contents of
  DevicePath are initialized to describe the ATA device specified by Port and PortMultiplierPort,
  and EFI_SUCCESS is returned.

  @param[in]     This                A pointer to the EFI_ATA_PASS_THRU_PROTOCOL instance.
  @param[in]     Port                Port specifies the port number of the ATA device for which a
                                     device path node is to be allocated and built.
  @param[in]     PortMultiplierPort  The port multiplier port number of the ATA device for which a
                                     device path node is to be allocated and built. If there is no
                                     port multiplier, then specify 0.
  @param[in,out] DevicePath          A pointer to a single device path node that describes the ATA
                                     device specified by Port and PortMultiplierPort. This function
                                     is responsible for allocating the buffer DevicePath with the
                                     boot service AllocatePool(). It is the caller's responsibility
                                     to free DevicePath when the caller is finished with DevicePath.
  @retval EFI_SUCCESS                The device path node that describes the ATA device specified by
                                     Port and PortMultiplierPort was allocated and returned in DevicePath.
  @retval EFI_NOT_FOUND              The ATA device specified by Port and PortMultiplierPort does not
                                     exist on the ATA controller.
  @retval EFI_INVALID_PARAMETER      DevicePath is NULL.
  @retval EFI_OUT_OF_RESOURCES       There are not enough resources to allocate DevicePath.

**/
EFI_STATUS
EFIAPI
<<DriverName>>AtaPassThruBuildDevicePath (
  IN     EFI_ATA_PASS_THRU_PROTOCOL *This,
  IN     UINT16                     Port,
  IN     UINT16                     PortMultiplierPort,
  IN OUT EFI_DEVICE_PATH_PROTOCOL   **DevicePath
  );

/**
  Used to translate a device path node to a port number and port multiplier port number.

  The GetDevice() function determines the port and port multiplier port number associated with
  the ATA device described by DevicePath. If DevicePath is a device path node type that the
  ATA Pass Thru driver supports, then the ATA Pass Thru driver will attempt to translate the contents 
  DevicePath into a port number and port multiplier port number.

  If this translation is successful, then that port number and port multiplier port number are returned
  in Port and PortMultiplierPort, and EFI_SUCCESS is returned.

  If DevicePath, Port, or PortMultiplierPort are NULL, then EFI_INVALID_PARAMETER is returned.

  If DevicePath is not a device path node type that the ATA Pass Thru driver supports, then 
  EFI_UNSUPPORTED is returned.

  If DevicePath is a device path node type that the ATA Pass Thru driver supports, but there is not 
  a valid translation from DevicePath to a port number and port multiplier port number, then 
  EFI_NOT_FOUND is returned.

  @param[in]  This                A pointer to the EFI_ATA_PASS_THRU_PROTOCOL instance.
  @param[in]  DevicePath          A pointer to the device path node that describes an ATA device on the
                                  ATA controller.
  @param[out] Port                On return, points to the port number of an ATA device on the ATA controller.
  @param[out] PortMultiplierPort  On return, points to the port multiplier port number of an ATA device
                                  on the ATA controller.

  @retval EFI_SUCCESS             DevicePath was successfully translated to a port number and port multiplier
                                  port number, and they were returned in Port and PortMultiplierPort.
  @retval EFI_INVALID_PARAMETER   DevicePath is NULL.
  @retval EFI_INVALID_PARAMETER   Port is NULL.
  @retval EFI_INVALID_PARAMETER   PortMultiplierPort is NULL.
  @retval EFI_UNSUPPORTED         This driver does not support the device path node type in DevicePath.
  @retval EFI_NOT_FOUND           A valid translation from DevicePath to a port number and port multiplier
                                  port number does not exist.
**/
EFI_STATUS
EFIAPI
<<DriverName>>AtaPassThruGetDevice (
  IN  EFI_ATA_PASS_THRU_PROTOCOL *This,
  IN  EFI_DEVICE_PATH_PROTOCOL   *DevicePath,
  OUT UINT16                     *Port,
  OUT UINT16                     *PortMultiplierPort
  );

/**
  Resets a specific port on the ATA controller. This operation also resets all the ATA devices
  connected to the port.

  The ResetChannel() function resets an a specific port on an ATA controller. This operation
  resets all the ATA devices connected to that port. If this ATA controller does not support
  a reset port operation, then EFI_UNSUPPORTED is returned.

  If a device error occurs while executing that port reset operation, then EFI_DEVICE_ERROR is
  returned.

  If a timeout occurs during the execution of the port reset operation, then EFI_TIMEOUT is returned.

  If the port reset operation is completed, then EFI_SUCCESS is returned.

  @param[in]  This          A pointer to the EFI_ATA_PASS_THRU_PROTOCOL instance.
  @param[in]  Port          The port number on the ATA controller.

  @retval EFI_SUCCESS       The ATA controller port was reset.
  @retval EFI_UNSUPPORTED   The ATA controller does not support a port reset operation.
  @retval EFI_DEVICE_ERROR  A device error occurred while attempting to reset the ATA port.
  @retval EFI_TIMEOUT       A timeout occurred while attempting to reset the ATA port.

**/
EFI_STATUS
EFIAPI
<<DriverName>>AtaPassThruResetPort (
  IN EFI_ATA_PASS_THRU_PROTOCOL *This,
  IN UINT16                     Port
  );

/**
  Resets an ATA device that is connected to an ATA controller.

  The ResetDevice() function resets the ATA device specified by Port and PortMultiplierPort.
  If this ATA controller does not support a device reset operation, then EFI_UNSUPPORTED is
  returned.

  If Port or PortMultiplierPort are not in a valid range for this ATA controller, then 
  EFI_INVALID_PARAMETER is returned.

  If a device error occurs while executing that device reset operation, then EFI_DEVICE_ERROR
  is returned.

  If a timeout occurs during the execution of the device reset operation, then EFI_TIMEOUT is
  returned.

  If the device reset operation is completed, then EFI_SUCCESS is returned.

  @param[in] This                A pointer to the EFI_ATA_PASS_THRU_PROTOCOL instance.
  @param[in] Port                Port represents the port number of the ATA device to be reset.
  @param[in] PortMultiplierPort  The port multiplier port number of the ATA device to reset.
                                 If there is no port multiplier, then specify 0.
  @retval EFI_SUCCESS            The ATA device specified by Port and PortMultiplierPort was reset.
  @retval EFI_UNSUPPORTED        The ATA controller does not support a device reset operation.
  @retval EFI_INVALID_PARAMETER  Port or PortMultiplierPort are invalid.
  @retval EFI_DEVICE_ERROR       A device error occurred while attempting to reset the ATA device
                                 specified by Port and PortMultiplierPort.
  @retval EFI_TIMEOUT            A timeout occurred while attempting to reset the ATA device
                                 specified by Port and PortMultiplierPort.

**/
EFI_STATUS
EFIAPI
<<DriverName>>AtaPassThruResetDevice (
  IN EFI_ATA_PASS_THRU_PROTOCOL *This,
  IN UINT16                     Port,
  IN UINT16                     PortMultiplierPort
  );
