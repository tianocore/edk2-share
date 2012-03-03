## @file
# Template string processing required by UEFI Driver Wizard code generation
#
# Copyright (c) 2012, Intel Corporation. All rights reserved.<BR>
#
# This program and the accompanying materials are licensed and made available
# under the terms and conditions of the BSD License which accompanies this
# distribution. The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#
##

##
# Import Modules
#
import re

gPlaceholderPattern = re.compile("\$\{([^$()\s]+)\}", re.MULTILINE|re.UNICODE)

## A string template class
#
#  This class implements a template for string replacement. A string template
#  looks like following
#
#       ${BEGIN} other_string ${placeholder_name} other_string ${END}
#
#  The string between ${BEGIN} and ${END} will be repeated as many times as the
#  length of "placeholder_name", which is a list passed through a dict. The
#  "placeholder_name" is the key name of the dict. The ${BEGIN} and ${END} can
#  be not used and, in this case, the "placeholder_name" must not a list and it
#  will just be replaced once.
#
class TemplateString(object):
    _REPEAT_START_FLAG = "BEGIN"
    _REPEAT_END_FLAG = "END"

    class Section(object):
        _LIST_TYPES = [type([]), type(set()), type((0,))]

        def __init__(self, TemplateSection, PlaceHolderList):
            self._Template = TemplateSection
            self._PlaceHolderList = []

            # Split the section into sub-sections according to the position of placeholders
            if PlaceHolderList:
                self._SubSectionList = []
                SubSectionStart = 0
                #
                # The placeholders passed in must be in the format of
                #
                #   PlaceHolderName, PlaceHolderStartPoint, PlaceHolderEndPoint
                #
                for PlaceHolder,Start,End in PlaceHolderList:
                    self._SubSectionList.append(TemplateSection[SubSectionStart:Start])
                    self._SubSectionList.append(TemplateSection[Start:End])
                    self._PlaceHolderList.append(PlaceHolder)
                    SubSectionStart = End
                if SubSectionStart < len(TemplateSection):
                    self._SubSectionList.append(TemplateSection[SubSectionStart:])
            else:
                self._SubSectionList = [TemplateSection]

        def __str__(self):
            return self._Template + " : " + str(self._PlaceHolderList)

        def Instantiate(self, PlaceHolderValues):
            RepeatTime = -1
            RepeatPlaceHolders = {}
            NonRepeatPlaceHolders = {}

            for PlaceHolder in self._PlaceHolderList:
                if PlaceHolder not in PlaceHolderValues:
                    continue
                Value = PlaceHolderValues[PlaceHolder]
                if type(Value) in self._LIST_TYPES:
                    if RepeatTime < 0:
                        RepeatTime = len(Value)
                    elif RepeatTime != len(Value):
                        EdkLogger.error(
                                    "TemplateString",
                                    PARAMETER_INVALID,
                                    "${%s} has different repeat time from others!" % PlaceHolder,
                                    ExtraData=str(self._Template)
                                    )
                    RepeatPlaceHolders["${%s}" % PlaceHolder] = Value
                else:
                    NonRepeatPlaceHolders["${%s}" % PlaceHolder] = Value

            if NonRepeatPlaceHolders:
                StringList = []
                for S in self._SubSectionList:
                    if S not in NonRepeatPlaceHolders:
                        StringList.append(S)
                    else:
                        StringList.append(str(NonRepeatPlaceHolders[S]))
            else:
                StringList = self._SubSectionList

            if RepeatPlaceHolders:
                TempStringList = []
                for Index in range(RepeatTime):
                    for S in StringList:
                        if S not in RepeatPlaceHolders:
                            TempStringList.append(S)
                        else:
                            TempStringList.append(str(RepeatPlaceHolders[S][Index]))
                StringList = TempStringList
            ReturnString = "".join(StringList)
            if ReturnString.strip() == '':
              return ''
            if len(ReturnString) > 0 and ReturnString[0] == '\n':
              return ReturnString[1:]
            return ReturnString

    ## Constructor
    def __init__(self, Template=None):
        self.String = ''
        self.IsBinary = False
        self._Template = Template
        self._TemplateSectionList = self._Parse(Template)

    ## str() operator
    #
    #   @retval     string  The string replaced
    #
    def __str__(self):
        return self.String

    ## Split the template string into fragments per the ${BEGIN} and ${END} flags
    #
    #   @retval     list    A list of TemplateString.Section objects
    #
    def _Parse(self, Template):
        SectionStart = 0
        SearchFrom = 0
        MatchEnd = 0
        PlaceHolderList = []
        TemplateSectionList = []
        while Template:
            MatchObj = gPlaceholderPattern.search(Template, SearchFrom)
            if not MatchObj:
                if MatchEnd <= len(Template):
                    TemplateSection = TemplateString.Section(Template[SectionStart:], PlaceHolderList)
                    TemplateSectionList.append(TemplateSection)
                break

            MatchString = MatchObj.group(1)
            MatchStart = MatchObj.start()
            MatchEnd = MatchObj.end()

            if MatchString == self._REPEAT_START_FLAG:
                if MatchStart > SectionStart:
                    TemplateSection = TemplateString.Section(Template[SectionStart:MatchStart], PlaceHolderList)
                    TemplateSectionList.append(TemplateSection)
                SectionStart = MatchEnd
                PlaceHolderList = []
            elif MatchString == self._REPEAT_END_FLAG:
                TemplateSection = TemplateString.Section(Template[SectionStart:MatchStart], PlaceHolderList)
                TemplateSectionList.append(TemplateSection)
                SectionStart = MatchEnd
                PlaceHolderList = []
            else:
                PlaceHolderList.append((MatchString, MatchStart - SectionStart, MatchEnd - SectionStart))
            SearchFrom = MatchEnd
        return TemplateSectionList

    ## Replace the string template with dictionary of placeholders and append it to previous one
    #
    #   @param      AppendString    The string template to append
    #   @param      Dictionary      The placeholder dictionaries
    #
    def Append(self, AppendString, Dictionary=None):
        if Dictionary:
            SectionList = self._Parse(AppendString)
            self.String += "".join([S.Instantiate(Dictionary) for S in SectionList])
        else:
            self.String += AppendString

    ## Replace the string template with dictionary of placeholders
    #
    #   @param      Dictionary      The placeholder dictionaries
    #
    #   @retval     str             The string replaced with placeholder values
    #
    def Replace(self, Dictionary=None):
        return "".join([S.Instantiate(Dictionary) for S in self._TemplateSectionList])

