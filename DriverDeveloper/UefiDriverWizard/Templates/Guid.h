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

#ifndef __<<GUID_NAME>>_H__
#define __<<GUID_NAME>>_H__

#define EFI_<<GUID_NAME>>_GUID \
  <<GUID_STRUCT>>

///
/// GUID specific defines
///
  
///
/// GUID specific structures
///
typedef struct {
  //
  // Place GUID specific data fields here
  //
} EFI_<<GUID_NAME>>_GUID;

extern EFI_GUID gEfi<<GuidName>>Guid;

#endif
