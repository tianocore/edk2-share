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

#ifndef __<<PROTOCOL_NAME>>_H__
#define __<<PROTOCOL_NAME>>_H__

#define EFI_<<PROTOCOL_NAME>>_PROTOCOL_GUID \
  <<GUID_STRUCT>>

///
/// Forward declaration
///  
typedef struct _EFI_<<PROTOCOL_NAME>>_PROTOCOL EFI_<<PROTOCOL_NAME>>_PROTOCOL;

///
/// Function prototypes
///
typedef
EFI_STATUS
(EFIAPI *EFI_<<PROTOCOL_NAME>>_<<FUNCTION_NAME_1>>)(
  IN EFI_<<PROTOCOL_NAME>>_PROTOCOL  *This
  //
  // Place additional function arguments here
  //
  );

typedef
EFI_STATUS
(EFIAPI *EFI_<<PROTOCOL_NAME>>_<<FUNCTION_NAME_2>>)(
  IN EFI_<<PROTOCOL_NAME>>_PROTOCOL  *This
  //
  // Place additional function arguments here
  //
  );

typedef
EFI_STATUS
(EFIAPI *EFI_<<PROTOCOL_NAME>>_<<FUNCTION_NAME_N>>)(
  IN EFI_<<PROTOCOL_NAME>>_PROTOCOL  *This
  //
  // Place additional function arguments here
  //
  );

///
/// Protocol structure
///
typedef struct _EFI_<<PROTOCOL_NAME>>_PROTOCOL {
  EFI_<<PROTOCOL_NAME>>_<<FUNCTION_NAME_1>>  <<FunctionName1>>;
  EFI_<<PROTOCOL_NAME>>_<<FUNCTION_NAME_2>>  <<FunctionName2>>;
  // . . .
  EFI_<<PROTOCOL_NAME>>_<<FUNCTION_NAME_N>>  <<FunctionNameN>>;
  //
  // Place protocol data fields here
  //
}

extern EFI_GUID gEfi<<ProtocolName>>ProtocolGuid;

#endif
