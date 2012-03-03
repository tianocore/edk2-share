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
  Sends a SCSI Request Packet to a SCSI device that is attached to 
  the SCSI channel. This function supports both blocking I/O and 
  non-blocking I/O.  The blocking I/O functionality is required, 
  and the non-blocking I/O functionality is optional.

  @param  This   Protocol instance pointer.
  @param  Target The Target ID of the SCSI device to
                 send the SCSI Request Packet.
  @param  Lun    The LUN of the SCSI device to send the
                 SCSI Request Packet.
  @param  Packet A pointer to the SCSI Request Packet to send
                 to the SCSI device specified by Target and Lun.
  @param  Event  If non-blocking I/O is not supported then Event
                 is ignored, and blocking I/O is performed.
                 If Event is NULL, then blocking I/O is performed.
                 If Event is not NULL and non blocking I/O is
                 supported, then non-blocking I/O is performed,
                 and Event will be signaled when the SCSI Request
                 Packet completes

  @retval EFI_SUCCESS               The SCSI Request Packet was sent by the host, and
                                    TransferLength bytes were transferred to/from
                                    DataBuffer. See HostAdapterStatus, TargetStatus,
                                    SenseDataLength, and SenseData in that order
                                    for additional status information.
  @retval EFI_BAD_BUFFER_SIZE       The SCSI Request Packet was executed, but the
                                    entire DataBuffer could not be transferred.
                                    The actual number of bytes transferred is returned
                                    in TransferLength. See HostAdapterStatus,
                                    TargetStatus, SenseDataLength, and SenseData in
                                    that order for additional status information.
  @retval EFI_NOT_READY             The SCSI Request Packet could not be sent because
                                    there are too many SCSI Request Packets already
                                    queued.  The caller may retry again later.
  @retval EFI_DEVICE_ERROR          A device error occurred while attempting to send
                                    the SCSI Request Packet. See HostAdapterStatus,
                                    TargetStatus, SenseDataLength, and SenseData in
                                    that order for additional status information.
  @retval EFI_INVALID_PARAMETER     Target, Lun, or the contents of ScsiRequestPacket
                                    are invalid. The SCSI Request Packet was not sent,
                                    so no additional status information is available.
  @retval EFI_UNSUPPORTED           The command described by the SCSI Request Packet
                                    is not supported by the host adapter. The SCSI
                                    Request Packet was not sent, so no additional
                                    status information is available.
  @retval EFI_TIMEOUT               A timeout occurred while waiting for the SCSI
                                    Request Packet to execute. See HostAdapterStatus,
                                    TargetStatus, SenseDataLength, and SenseData in
                                    that order for additional status information.
                                    
**/
EFI_STATUS
EFIAPI
<<DriverName>>ScsiPassThruPassThru (
  IN EFI_SCSI_PASS_THRU_PROTOCOL                          *This,
  IN UINT32                                               Target,
  IN UINT64                                               Lun,
  IN OUT EFI_SCSI_PASS_THRU_SCSI_REQUEST_PACKET           *Packet,
  IN EFI_EVENT                                            Event   OPTIONAL
  );

/**
  Used to retrieve the list of legal Target IDs for SCSI devices 
  on a SCSI channel.

  @param  This   Protocol instance pointer.
  @param  Target On input, a pointer to the Target ID of a
                 SCSI device present on the SCSI channel.
                 On output, a pointer to the Target ID of
                 the next SCSI device present on a SCSI channel.
                 An input value of 0xFFFFFFFF retrieves the
                 Target ID of the first SCSI device present on
                 a SCSI channel.
  @param  Lun    On input, a pointer to the LUN of a SCSI device
                 present on the SCSI channel. On output, a pointer
                 to the LUN of the next SCSI device present on a
                 SCSI channel.

  @retval EFI_SUCCESS           The Target ID of the next SCSI device on the SCSI
                                channel was returned in Target and Lun.
  @retval EFI_NOT_FOUND         There are no more SCSI devices on this SCSI channel.
  @retval EFI_INVALID_PARAMETER Target is not 0xFFFFFFFF, and Target and Lun were
                                 not returned on a previous call to GetNextDevice().

**/
EFI_STATUS
EFIAPI
<<DriverName>>ScsiPassThruGetNextDevice (
  IN EFI_SCSI_PASS_THRU_PROTOCOL            *This,
  IN OUT UINT32                             *Target,
  IN OUT UINT64                             *Lun
  );

/**
  Used to allocate and build a device path node for a SCSI device 
  on a SCSI channel.

  @param  This       Protocol instance pointer.
  @param  Target     The Target ID of the SCSI device for which
                     a device path node is to be allocated and built.
  @param  Lun        The LUN of the SCSI device for which a device
                     path node is to be allocated and built.
  @param  DevicePath A pointer to a single device path node that
                     describes the SCSI device specified by
                     Target and Lun. This function is responsible
                     for allocating the buffer DevicePath with the boot
                     service AllocatePool().  It is the caller's
                     responsibility to free DevicePath when the caller
                     is finished with DevicePath.

  @retval EFI_SUCCESS           The device path node that describes the SCSI device
                                specified by Target and Lun was allocated and
                                returned in DevicePath.
  @retval EFI_NOT_FOUND         The SCSI devices specified by Target and Lun does
                                not exist on the SCSI channel.
  @retval EFI_INVALID_PARAMETER DevicePath is NULL.
  @retval EFI_OUT_OF_RESOURCES  There are not enough resources to allocate
                                DevicePath.

**/
EFI_STATUS
EFIAPI
<<DriverName>>ScsiPassThruBuildDevicePath (
  IN EFI_SCSI_PASS_THRU_PROTOCOL            *This,
  IN     UINT32                             Target,
  IN     UINT64                             Lun,
  IN OUT EFI_DEVICE_PATH_PROTOCOL           **DevicePath
  );

/**
  Used to translate a device path node to a Target ID and LUN.

  @param  This       Protocol instance pointer.
  @param  DevicePath A pointer to the device path node that
                     describes a SCSI device on the SCSI channel.
  @param  Target     A pointer to the Target ID of a SCSI device
                     on the SCSI channel.
  @param  Lun        A pointer to the LUN of a SCSI device on
                     the SCSI channel.

  @retval EFI_SUCCESS           DevicePath was successfully translated to a
                                Target ID and LUN, and they were returned
                                in Target and Lun.
  @retval EFI_INVALID_PARAMETER DevicePath is NULL.
  @retval EFI_INVALID_PARAMETER Target is NULL.
  @retval EFI_INVALID_PARAMETER Lun is NULL.
  @retval EFI_UNSUPPORTED       This driver does not support the device path
                                node type in DevicePath.
  @retval EFI_NOT_FOUND         A valid translation from DevicePath to a
                                Target ID and LUN does not exist.

**/
EFI_STATUS
EFIAPI
<<DriverName>>ScsiPassThruGetTargetLun (
  IN EFI_SCSI_PASS_THRU_PROTOCOL            *This,
  IN  EFI_DEVICE_PATH_PROTOCOL              *DevicePath,
  OUT UINT32                                *Target,
  OUT UINT64                                *Lun
  );

/**
  Resets a SCSI channel.This operation resets all the 
  SCSI devices connected to the SCSI channel.

  @param  This Protocol instance pointer.

  @retval EFI_SUCCESS      The SCSI channel was reset.
  @retval EFI_UNSUPPORTED  The SCSI channel does not support
                           a channel reset operation.
  @retval EFI_DEVICE_ERROR A device error occurred while
                           attempting to reset the SCSI channel.
  @retval EFI_TIMEOUT      A timeout occurred while attempting
                           to reset the SCSI channel.

**/
EFI_STATUS
EFIAPI
<<DriverName>>ScsiPassThruResetChannel (
  IN EFI_SCSI_PASS_THRU_PROTOCOL             *This
  );

/**
  Resets a SCSI device that is connected to a SCSI channel.

  @param  This   Protocol instance pointer.
  @param  Target The Target ID of the SCSI device to reset.
  @param  Lun    The LUN of the SCSI device to reset.

  @retval EFI_SUCCESS           The SCSI device specified by Target and
                                Lun was reset.
  @retval EFI_UNSUPPORTED       The SCSI channel does not support a target
                                reset operation.
  @retval EFI_INVALID_PARAMETER Target or Lun are invalid.
  @retval EFI_DEVICE_ERROR      A device error occurred while attempting
                                to reset the SCSI device specified by Target
                                and Lun.
  @retval EFI_TIMEOUT           A timeout occurred while attempting to reset
                                the SCSI device specified by Target and Lun.

**/
EFI_STATUS
EFIAPI
<<DriverName>>ScsiPassThruResetTarget (
  IN EFI_SCSI_PASS_THRU_PROTOCOL             *This,
  IN UINT32                                  Target,
  IN UINT64                                  Lun
  );
