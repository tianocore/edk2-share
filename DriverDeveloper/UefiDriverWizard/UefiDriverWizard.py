# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

ID_OPEN_WORKSPACE = 1000
ID_NEW_UEFI_DRIVER = 1001
ID_NEW_PACKAGE = 1002
ID_NEW_PROTOCOL = 1003
ID_NEW_GUID = 1004
ID_NEW_LIBRARY_CLASS = 1005
ID_EXIT = 1006
ID_ABOUT = 1007
ID_LICENSE = 1008

###########################################################################
## Class UefiDriverWizard
###########################################################################

class UefiDriverWizard ( wx.Frame ):

  def __init__( self, parent ):
    wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"UEFI 2.3.1 Driver Wizard", pos = wx.DefaultPosition, size = wx.Size( 700,760 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer3 = wx.BoxSizer( wx.VERTICAL )

    self.LogMessageWindow = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_READONLY )
    bSizer3.Add( self.LogMessageWindow, 1, wx.ALL|wx.EXPAND, 5 )

    self.SetSizer( bSizer3 )
    self.Layout()
    self.MainStatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
    self.MainMenuBar = wx.MenuBar( 0 )
    self.file = wx.Menu()
    self.openWorkspace = wx.MenuItem( self.file, ID_OPEN_WORKSPACE, u"&Open WORKSPACE"+ u"\t" + u"CTRL+O", u"Open EDK II Workspace", wx.ITEM_NORMAL )
    self.file.AppendItem( self.openWorkspace )

    self.newUefiDriver = wx.MenuItem( self.file, ID_NEW_UEFI_DRIVER, u"&New UEFI Driver"+ u"\t" + u"CTRL+N", u"Create a new UEFI Driver", wx.ITEM_NORMAL )
    self.file.AppendItem( self.newUefiDriver )

    self.newPackage = wx.MenuItem( self.file, ID_NEW_PACKAGE, u"New Pac&kage"+ u"\t" + u"CTRL+K", u"Create a new EDK II Package", wx.ITEM_NORMAL )
    self.file.AppendItem( self.newPackage )

    self.newProtocol = wx.MenuItem( self.file, ID_NEW_PROTOCOL, u"New &Protocol"+ u"\t" + u"CTRL+P", u"Create a new Protocol in an EDK II Package", wx.ITEM_NORMAL )
    self.file.AppendItem( self.newProtocol )

    self.newGuid = wx.MenuItem( self.file, ID_NEW_GUID, u"New &GUID"+ u"\t" + u"CTRL+G", u"Create a new GUID in an EDK II Package", wx.ITEM_NORMAL )
    self.file.AppendItem( self.newGuid )

    self.newLibraryClass = wx.MenuItem( self.file, ID_NEW_LIBRARY_CLASS, u"New &Library Class"+ u"\t" + u"CTRL+L", u"Create a new Library Class in an EDK II Package", wx.ITEM_NORMAL )
    self.file.AppendItem( self.newLibraryClass )

    self.exit = wx.MenuItem( self.file, ID_EXIT, u"E&xit", u"Exit UEFI Driver Wizard", wx.ITEM_NORMAL )
    self.file.AppendItem( self.exit )

    self.MainMenuBar.Append( self.file, u"&File" )

    self.help = wx.Menu()
    self.about = wx.MenuItem( self.help, ID_ABOUT, u"&About", u"About UEFI Driver Wizard", wx.ITEM_NORMAL )
    self.help.AppendItem( self.about )

    self.license = wx.MenuItem( self.help, ID_LICENSE, u"&License", u"License for UEFI Driver Wizard", wx.ITEM_NORMAL )
    self.help.AppendItem( self.license )

    self.MainMenuBar.Append( self.help, u"&Help" )

    self.SetMenuBar( self.MainMenuBar )


    self.Centre( wx.BOTH )

    # Connect Events
    self.Bind( wx.EVT_MENU, self.openWorkspaceOnMenuSelection, id = self.openWorkspace.GetId() )
    self.Bind( wx.EVT_MENU, self.newUefiDriverOnMenuSelection, id = self.newUefiDriver.GetId() )
    self.Bind( wx.EVT_MENU, self.newPackageOnMenuSelection, id = self.newPackage.GetId() )
    self.Bind( wx.EVT_MENU, self.newProtocolOnMenuSelection, id = self.newProtocol.GetId() )
    self.Bind( wx.EVT_MENU, self.newGuidOnMenuSelection, id = self.newGuid.GetId() )
    self.Bind( wx.EVT_MENU, self.newLibraryClassOnMenuSelection, id = self.newLibraryClass.GetId() )
    self.Bind( wx.EVT_MENU, self.exitOnMenuSelection, id = self.exit.GetId() )
    self.Bind( wx.EVT_MENU, self.aboutOnMenuSelection, id = self.about.GetId() )
    self.Bind( wx.EVT_MENU, self.licenseOnMenuSelection, id = self.license.GetId() )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def openWorkspaceOnMenuSelection( self, event ):
    event.Skip()

  def newUefiDriverOnMenuSelection( self, event ):
    event.Skip()

  def newPackageOnMenuSelection( self, event ):
    event.Skip()

  def newProtocolOnMenuSelection( self, event ):
    event.Skip()

  def newGuidOnMenuSelection( self, event ):
    event.Skip()

  def newLibraryClassOnMenuSelection( self, event ):
    event.Skip()

  def exitOnMenuSelection( self, event ):
    event.Skip()

  def aboutOnMenuSelection( self, event ):
    event.Skip()

  def licenseOnMenuSelection( self, event ):
    event.Skip()


###########################################################################
## Class NewUefiDriver
###########################################################################

class NewUefiDriver ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New UEFI Driver", pos = wx.DefaultPosition, size = wx.Size( 600,680 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer11 = wx.BoxSizer( wx.VERTICAL )

    bSizer4 = wx.BoxSizer( wx.VERTICAL )

    bSizer4.SetMinSize( wx.Size( -1,600 ) )
    self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

    fgSizer92 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer92.SetFlexibleDirection( wx.BOTH )
    fgSizer92.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"    UEFI Driver Path", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText82.Wrap( -1 )
    self.m_staticText82.SetToolTipString( u"The path to a folder where the UEFI Driver Wizard \ncreates a new UEFI Driver.  The path must be in the\ncurrently selected WORKSPACE.  The UEFI Driver \nWizard creates a new folder for the UEFI Driver if \nthe folder does not exist.\n" )

    fgSizer92.Add( self.m_staticText82, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )

    self.UefiDriverPath = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select New UEFI Driver Folder", wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRP_USE_TEXTCTRL )
    self.UefiDriverPath.SetMinSize( wx.Size( 400,25 ) )

    fgSizer92.Add( self.UefiDriverPath, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    bSizer4.Add( fgSizer92, 0, wx.EXPAND, 5 )

    fgSizer9 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer9.SetFlexibleDirection( wx.BOTH )
    fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"  UEFI Driver Name", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText8.Wrap( -1 )
    self.m_staticText8.SetToolTipString( u"The name of the UEFI Driver.  Is not allowed to \ncontain spaces or special characters.  This name \nis used to generate the file names for the UEFI \nDriver source files as well as generated names \nfor C functions and variables.\n" )

    fgSizer9.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.UefiDriverName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 308,-1 ), 0 )
    fgSizer9.Add( self.UefiDriverName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    bSizer4.Add( fgSizer9, 0, wx.EXPAND, 5 )

    fgSizer93 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer93.SetFlexibleDirection( wx.BOTH )
    fgSizer93.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u"UEFI Driver Version", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText83.Wrap( -1 )
    self.m_staticText83.SetToolTipString( u"The version of the UEFI Driver that is declared \nin the [Defines] section of the INF file.  Must be\na floating point value (i.e. 1.27)\n" )

    fgSizer93.Add( self.m_staticText83, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.UefiDriverVersion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 308,-1 ), 0 )
    fgSizer93.Add( self.UefiDriverVersion, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    bSizer4.Add( fgSizer93, 0, wx.EXPAND, 5 )

    fgSizer91 = wx.FlexGridSizer( 1, 3, 0, 0 )
    fgSizer91.SetFlexibleDirection( wx.BOTH )
    fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"   UEFI Driver GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText81.Wrap( -1 )
    self.m_staticText81.SetToolTipString( u"The globally unique identifier for this UEFI Driver \nin registry format\n\n    (i.e. 8ed7d500-4582-11e1-a3a9-8c02263c353d).  \n\nIf a UEFI Driver is backwards compatible with a \nprevious version of a UEFI Driver, then the same \nGUID may be used with a higher Version value.  \nIf a UEFI Driver is new or not backwards compatible \nwith a previous version, then a new GUID must be generated." )

    fgSizer91.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.UefiDriverGuid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 310,-1 ), 0 )
    fgSizer91.Add( self.UefiDriverGuid, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.GenerateGuid = wx.Button( self, wx.ID_ANY, u"Generate GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer91.Add( self.GenerateGuid, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    bSizer4.Add( fgSizer91, 0, wx.EXPAND, 5 )

    self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

    UefiDriverTypeChoices = [ u"UEFI Driver Model Device Driver", u"UEFI Driver Model Bus Driver", u"UEFI Driver Model Hybrid Driver", u"Root Bridge Driver", u"Service Driver", u"Initializing Driver" ]
    self.UefiDriverType = wx.RadioBox( self, wx.ID_ANY, u"UEFI Driver Type", wx.DefaultPosition, wx.Size( -1,-1 ), UefiDriverTypeChoices, 3, wx.RA_SPECIFY_ROWS )
    self.UefiDriverType.SetSelection( 0 )
    self.UefiDriverType.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
    self.UefiDriverType.SetToolTipString( u"Device driver - A driver that follows the UEFI driver model. This type of driver produces one or more \ndriver handles or driver image handles by installing one or more instances of the Driver Binding Protocol \ninto the handle database. This type of driver does not create any child handles when the Start() service of \nhe Driver Binding Protocol is called. Instead, it only adds additional I/O protocols to existing controller \nhandles.\n\nBus driver - A driver that follows the UEFI driver model. This type of driver produces one or more \ndriver handles or driver image handles by installing one or more instances of the Driver Binding Protocol \nin the handle database. This type of driver creates new child handles when the Start() service of the \nDriver Binding Protocol is called. It also adds I/O protocols to these newly created child handles.\n\nHybrid driver - A driver that follows the UEFI driver model and shares characteristics with both device \ndrivers and bus drivers. This distinction means that the Start() service of the Driver Binding Protocol adds \nI/O protocols to existing handles and creates child handles.\n\nRoot bridge driver - A driver that creates one or physical controller handles that contain a Device \nPath Protocol and a protocol that is a software abstraction for the I/O services provided by a root \nbus produced by a core chipset. The most common root bridge driver is one that creates handles for \nthe PCI root bridges in the platform that support the Device Path Protocol and the PCI Root Bridge I/O Protocol.\n\nService driver - A driver that produces one or more protocols on one or more new service handles and \nreturns EFI_SUCCESS from its entry point.\n\nInitializing driver - A driver that does not create any handles and does not add any protocols to the handle \ndatabase. Instead, this type of driver performs some initialization operations and returns an error code so \nthe driver is unloaded from system memory." )

    bSizer20.Add( self.UefiDriverType, 0, wx.ALL, 5 )

    bSizer21 = wx.BoxSizer( wx.VERTICAL )

    self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Driver Binding Version", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText26.Wrap( -1 )
    bSizer21.Add( self.m_staticText26, 0, wx.ALL, 5 )

    self.DriverBindingVersion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
    bSizer21.Add( self.DriverBindingVersion, 0, wx.ALL, 5 )

    bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )

    bSizer4.Add( bSizer20, 0, 0, 5 )

    self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

    self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Optional Features Common to all UEFI Driver Types", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText6.Wrap( -1 )
    bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

    bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

    UefiDriverCommonFeaturesChoices = [ u"Unloadable", u"Driver Supported EFI Version Protocol", u"HII Packages for Strings, Fonts, or Images", u"Service Binding Protocol" ];
    self.UefiDriverCommonFeatures = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,80 ), UefiDriverCommonFeaturesChoices, 0 )
    bSizer24.Add( self.UefiDriverCommonFeatures, 0, wx.ALL, 5 )

    bSizer25 = wx.BoxSizer( wx.VERTICAL )

    self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"UEFI Specification Version", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText29.Wrap( -1 )
    bSizer25.Add( self.m_staticText29, 0, wx.ALL, 5 )

    self.UefiSpecificationVersion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
    bSizer25.Add( self.UefiSpecificationVersion, 0, wx.ALL, 5 )

    bSizer24.Add( bSizer25, 1, wx.EXPAND, 5 )

    bSizer4.Add( bSizer24, 1, wx.EXPAND, 5 )

    self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

    self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"CPU Architectures", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText7.Wrap( -1 )
    bSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )

    UefiDriverCpuArchitectureChoices = [ u"All CPU Architectures", u"IA32", u"X64", u"IPF", u"EBC", u"ARM" ];
    self.UefiDriverCpuArchitecture = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,120 ), UefiDriverCpuArchitectureChoices, 0 )
    bSizer4.Add( self.UefiDriverCpuArchitecture, 0, wx.ALL, 5 )

    self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer11.Add( bSizer4, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Prev = wx.Button( self, wx.ID_ANY, u"<< Prev", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Prev.Enable( False )

    fgSizer1.Add( self.Prev, 0, wx.ALL, 5 )

    self.Next = wx.Button( self, wx.ID_ANY, u"Next >>", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Next.SetDefault()
    fgSizer1.Add( self.Next, 0, wx.ALL, 5 )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.ALL, 5 )

    bSizer11.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer11 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.UefiDriverPath.Bind( wx.EVT_DIRPICKER_CHANGED, self.UefiDriverPathOnDirChanged )
    self.UefiDriverName.Bind( wx.EVT_TEXT, self.UefiDriverNameOnText )
    self.UefiDriverVersion.Bind( wx.EVT_TEXT, self.UefiDriverVersionOnText )
    self.UefiDriverGuid.Bind( wx.EVT_TEXT, self.UefiDriverGuidOnText )
    self.GenerateGuid.Bind( wx.EVT_BUTTON, self.GenerateGuidOnButtonClick )
    self.UefiDriverType.Bind( wx.EVT_RADIOBOX, self.UefiDriverTypeOnRadioBox )
    self.DriverBindingVersion.Bind( wx.EVT_TEXT, self.DriverBindingVersionOnText )
    self.UefiDriverCommonFeatures.Bind( wx.EVT_CHECKLISTBOX, self.UefiDriverCommonFeaturesOnCheckListBoxToggled )
    self.UefiSpecificationVersion.Bind( wx.EVT_TEXT, self.UefiSpecificationVersionOnText )
    self.UefiDriverCpuArchitecture.Bind( wx.EVT_CHECKLISTBOX, self.UefiDriverCpuArchitectureOnCheckListBoxToggled )
    self.Next.Bind( wx.EVT_BUTTON, self.NextOnButtonClick )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def UefiDriverPathOnDirChanged( self, event ):
    event.Skip()

  def UefiDriverNameOnText( self, event ):
    event.Skip()

  def UefiDriverVersionOnText( self, event ):
    event.Skip()

  def UefiDriverGuidOnText( self, event ):
    event.Skip()

  def GenerateGuidOnButtonClick( self, event ):
    event.Skip()

  def UefiDriverTypeOnRadioBox( self, event ):
    event.Skip()

  def DriverBindingVersionOnText( self, event ):
    event.Skip()

  def UefiDriverCommonFeaturesOnCheckListBoxToggled( self, event ):
    event.Skip()

  def UefiSpecificationVersionOnText( self, event ):
    event.Skip()

  def UefiDriverCpuArchitectureOnCheckListBoxToggled( self, event ):
    event.Skip()

  def NextOnButtonClick( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

###########################################################################
## Class UefiDriverModelOptionalFeatures
###########################################################################

class UefiDriverModelOptionalFeatures ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"UEFI Driver Model Optional Features", pos = wx.DefaultPosition, size = wx.Size( 600,680 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer13 = wx.BoxSizer( wx.VERTICAL )

    bSizer9 = wx.BoxSizer( wx.VERTICAL )

    bSizer9.SetMinSize( wx.Size( -1,600 ) )
    self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

    UefiDriverDriverModelFeaturesChoices = [ u"Component Name 2 Protocol", u"Component Name Protocol", u"Driver Family Override Protocol", u"Driver Diagnostics 2 Protocol", u"Driver Diagnostics Protocol", u"HII Packages for forms and HII based configuration ", u"Driver Configuration 2 Protocol", u"Driver Configuration Protocol", u"Driver Health Protocol", u"Bus Specific Driver Override Protocol" ];
    self.UefiDriverDriverModelFeatures = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,190 ), UefiDriverDriverModelFeaturesChoices, 0 )
    bSizer9.Add( self.UefiDriverDriverModelFeatures, 0, wx.ALL, 5 )

    self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

    self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"RFC 4646 Language Codes", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText30.Wrap( -1 )
    bSizer9.Add( self.m_staticText30, 0, wx.ALL, 5 )

    self.Rfc4646LanguageCodes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
    bSizer9.Add( self.Rfc4646LanguageCodes, 0, wx.ALL, 5 )

    self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

    self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"ISO 639-2 Language Codes", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText31.Wrap( -1 )
    bSizer9.Add( self.m_staticText31, 0, wx.ALL, 5 )

    self.Iso639LanguageCodes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
    bSizer9.Add( self.Iso639LanguageCodes, 0, wx.ALL, 5 )

    self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer13.Add( bSizer9, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Prev = wx.Button( self, wx.ID_ANY, u"<< Prev", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Prev, 0, wx.ALL, 5 )

    self.Next = wx.Button( self, wx.ID_ANY, u"Next >>", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Next.SetDefault()
    fgSizer1.Add( self.Next, 0, wx.ALL, 5 )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.ALL, 5 )

    bSizer13.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer13 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.UefiDriverDriverModelFeatures.Bind( wx.EVT_CHECKLISTBOX, self.UefiDriverDriverModelFeaturesOnCheckListBoxToggled )
    self.Rfc4646LanguageCodes.Bind( wx.EVT_TEXT, self.Rfc4646LanguageCodesOnText )
    self.Iso639LanguageCodes.Bind( wx.EVT_TEXT, self.Iso639LanguageCodesOnText )
    self.Prev.Bind( wx.EVT_BUTTON, self.PrevOnButtonClick )
    self.Next.Bind( wx.EVT_BUTTON, self.NextOnButtonClick )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def UefiDriverDriverModelFeaturesOnCheckListBoxToggled( self, event ):
    event.Skip()

  def Rfc4646LanguageCodesOnText( self, event ):
    event.Skip()

  def Iso639LanguageCodesOnText( self, event ):
    event.Skip()

  def PrevOnButtonClick( self, event ):
    event.Skip()

  def NextOnButtonClick( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

###########################################################################
## Class UefiDriverModelConsumedProtocols
###########################################################################

class UefiDriverModelConsumedProtocols ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"UEFI Driver Consumed Protocol", pos = wx.DefaultPosition, size = wx.Size( 600,680 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer15 = wx.BoxSizer( wx.VERTICAL )

    bSizer9 = wx.BoxSizer( wx.VERTICAL )

    bSizer9.SetMinSize( wx.Size( -1,600 ) )
    self.m_staticline111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline111, 0, wx.EXPAND |wx.ALL, 5 )

    UefiDriverConsumedProtocolsChoices = [ u"PCI Driver that consumes the PCI I/O Protocol", u"USB Driver that consumes the USB I/O Protocol", u"SCSI Driver that consumes the SCSI I/O Protocol", u"ATA Driver that consumes the ATA Pass Thru Protocol" ];
    self.UefiDriverConsumedProtocols = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,80 ), UefiDriverConsumedProtocolsChoices, 0 )
    bSizer9.Add( self.UefiDriverConsumedProtocols, 0, wx.ALL, 5 )

    self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer15.Add( bSizer9, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Prev = wx.Button( self, wx.ID_ANY, u"<< Prev", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Prev, 0, wx.ALL, 5 )

    self.Next = wx.Button( self, wx.ID_ANY, u"Next >>", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Next.SetDefault()
    fgSizer1.Add( self.Next, 0, wx.ALL, 5 )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.ALL, 5 )

    bSizer15.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer15 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.UefiDriverConsumedProtocols.Bind( wx.EVT_CHECKLISTBOX, self.UefiDriverConsumedProtocolsOnCheckListBoxToggled )
    self.Prev.Bind( wx.EVT_BUTTON, self.PrevOnButtonClick )
    self.Next.Bind( wx.EVT_BUTTON, self.NextOnButtonClick )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def UefiDriverConsumedProtocolsOnCheckListBoxToggled( self, event ):
    event.Skip()

  def PrevOnButtonClick( self, event ):
    event.Skip()

  def NextOnButtonClick( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

###########################################################################
## Class UefiDriverModelProducedProtocols
###########################################################################

class UefiDriverModelProducedProtocols ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"UEFI Driver Produced Protocols", pos = wx.DefaultPosition, size = wx.Size( 600,680 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer17 = wx.BoxSizer( wx.VERTICAL )

    bSizer9 = wx.BoxSizer( wx.VERTICAL )

    bSizer9.SetMinSize( wx.Size( -1,600 ) )
    self.m_staticline111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline111, 0, wx.EXPAND |wx.ALL, 5 )

    UefiDriverProducedProtocolsChoices = [ u"Keyboard producing Simple Text In Protocol", u"Keyboard producing Simple Text In Ex Protocol", u"Mouse producing Simple Pointer Protocol", u"Tablet producing Absolute Pointer Protocol", u"Text Console producing the Simple Text Output Protocol", u"Byte stream device (i.e. UART) producing Serial I/O Protocol", u"Graphics Console producing the Graphics Output Protocol", u"Mass Storage Device producing Block I/O Protocol", u"Mass Storage Device producing Block I/O 2 Protocol", u"Mass Storage Device producing Storage Security Command Protocol", u"Network Interface Card producing NII/UNDI", u"Network Interface Card producing Simple Network Protocol", u"USB Host Controller producing the USB Host Controller 2 Protocol", u"ATA Host Controller producing the ATA Pass Thru Protocol", u"SCSI Host Controller producing the SCSI Pass Thru Protocol", u"SCSI Host Controller or ATA Host Controller producing the Extended SCSI Pass Thru Protocol", u"User identification device producing the User Credential Protocol", u"Non standard boot device producing Load File Protocol", u"Platform driver producing the EDID Override Protocol" ];
    self.UefiDriverProducedProtocols = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,350 ), UefiDriverProducedProtocolsChoices, 0 )
    bSizer9.Add( self.UefiDriverProducedProtocols, 0, wx.ALL, 5 )

    self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer9.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

    self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"USB Major Version", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText32.Wrap( -1 )
    bSizer9.Add( self.m_staticText32, 0, wx.ALL, 5 )

    self.UsbMajorVersion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
    bSizer9.Add( self.UsbMajorVersion, 0, wx.ALL, 5 )

    self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"USB Minor Version", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText33.Wrap( -1 )
    bSizer9.Add( self.m_staticText33, 0, wx.ALL, 5 )

    self.UsbMinorVersion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
    bSizer9.Add( self.UsbMinorVersion, 0, wx.ALL, 5 )

    bSizer17.Add( bSizer9, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Prev = wx.Button( self, wx.ID_ANY, u"<< Prev", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Prev, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.Next = wx.Button( self, wx.ID_ANY, u"Next >>", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Next.SetDefault()
    self.Next.Enable( False )

    fgSizer1.Add( self.Next, 0, wx.ALL, 5 )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Finish.SetDefault()
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.EXPAND|wx.ALL, 5 )

    bSizer17.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer17 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.UefiDriverProducedProtocols.Bind( wx.EVT_CHECKLISTBOX, self.UefiDriverProducedProtocolsOnCheckListBoxToggled )
    self.UsbMajorVersion.Bind( wx.EVT_TEXT, self.UsbMajorVersionOnText )
    self.UsbMinorVersion.Bind( wx.EVT_TEXT, self.UsbMinorVersionOnText )
    self.Prev.Bind( wx.EVT_BUTTON, self.PrevOnButtonClick )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def UefiDriverProducedProtocolsOnCheckListBoxToggled( self, event ):
    event.Skip()

  def UsbMajorVersionOnText( self, event ):
    event.Skip()

  def UsbMinorVersionOnText( self, event ):
    event.Skip()

  def PrevOnButtonClick( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

###########################################################################
## Class NewPackage
###########################################################################

class NewPackage ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Package", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer19 = wx.BoxSizer( wx.VERTICAL )

    bSizer4 = wx.BoxSizer( wx.VERTICAL )

    bSizer4.SetMinSize( wx.Size( -1,220 ) )
    self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

    fgSizer92 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer92.SetFlexibleDirection( wx.BOTH )
    fgSizer92.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"    Package Path", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText82.Wrap( -1 )
    fgSizer92.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.PackagePath = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select EDK II Package Folder", wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRP_USE_TEXTCTRL )
    self.PackagePath.SetMinSize( wx.Size( 400,25 ) )

    fgSizer92.Add( self.PackagePath, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    bSizer4.Add( fgSizer92, 1, wx.EXPAND, 5 )

    fgSizer9 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer9.SetFlexibleDirection( wx.BOTH )
    fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"  Package Name", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText8.Wrap( -1 )
    fgSizer9.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.PackageName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 310,-1 ), 0 )
    fgSizer9.Add( self.PackageName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    bSizer4.Add( fgSizer9, 1, wx.EXPAND, 5 )

    fgSizer91 = wx.FlexGridSizer( 1, 3, 0, 0 )
    fgSizer91.SetFlexibleDirection( wx.BOTH )
    fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"   Package GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText81.Wrap( -1 )
    fgSizer91.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.PackageGuidValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 310,-1 ), 0 )
    fgSizer91.Add( self.PackageGuidValue, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.GenerateGuid = wx.Button( self, wx.ID_ANY, u"Generate GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer91.Add( self.GenerateGuid, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

    bSizer4.Add( fgSizer91, 1, wx.EXPAND, 5 )

    fgSizer93 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer93.SetFlexibleDirection( wx.BOTH )
    fgSizer93.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u"Package Version", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText83.Wrap( -1 )
    fgSizer93.Add( self.m_staticText83, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.PackageVersion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 308,-1 ), 0 )
    fgSizer93.Add( self.PackageVersion, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    bSizer4.Add( fgSizer93, 1, wx.EXPAND, 5 )

    fgSizer911 = wx.FlexGridSizer( 1, 3, 0, 0 )
    fgSizer911.SetFlexibleDirection( wx.BOTH )
    fgSizer911.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText811 = wx.StaticText( self, wx.ID_ANY, u"   Platform GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText811.Wrap( -1 )
    fgSizer911.Add( self.m_staticText811, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.PlatformGuidValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 310,-1 ), 0 )
    fgSizer911.Add( self.PlatformGuidValue, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.GeneratePlatformGuid = wx.Button( self, wx.ID_ANY, u"Generate GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer911.Add( self.GeneratePlatformGuid, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

    bSizer4.Add( fgSizer911, 1, wx.EXPAND, 5 )

    self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer19.Add( bSizer4, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 1, 3, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Finish.SetDefault()
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.ALL, 5 )

    bSizer19.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer19 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.PackagePath.Bind( wx.EVT_DIRPICKER_CHANGED, self.PackagePathOnDirChanged )
    self.PackageName.Bind( wx.EVT_TEXT, self.PackageNameOnText )
    self.PackageGuidValue.Bind( wx.EVT_TEXT, self.PackageGuidValueOnText )
    self.GenerateGuid.Bind( wx.EVT_BUTTON, self.GenerateGuidOnButtonClick )
    self.PackageVersion.Bind( wx.EVT_TEXT, self.PackageVersionOnText )
    self.PlatformGuidValue.Bind( wx.EVT_TEXT, self.PlatformGuidValueOnText )
    self.GeneratePlatformGuid.Bind( wx.EVT_BUTTON, self.GeneratePlatformGuidOnButtonClick )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def PackagePathOnDirChanged( self, event ):
    event.Skip()

  def PackageNameOnText( self, event ):
    event.Skip()

  def PackageGuidValueOnText( self, event ):
    event.Skip()

  def GenerateGuidOnButtonClick( self, event ):
    event.Skip()

  def PackageVersionOnText( self, event ):
    event.Skip()

  def PlatformGuidValueOnText( self, event ):
    event.Skip()

  def GeneratePlatformGuidOnButtonClick( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

###########################################################################
## Class NewProtocol
###########################################################################

class NewProtocol ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Protocol", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer21 = wx.BoxSizer( wx.VERTICAL )

    bSizer4 = wx.BoxSizer( wx.VERTICAL )

    bSizer4.SetMinSize( wx.Size( -1,220 ) )
    self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

    fgSizer922 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer922.SetFlexibleDirection( wx.BOTH )
    fgSizer922.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText822 = wx.StaticText( self, wx.ID_ANY, u"              Package File", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText822.Wrap( -1 )
    fgSizer922.Add( self.m_staticText822, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.PackageFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select EDK II Package File", u"*.dec", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
    self.PackageFile.SetMinSize( wx.Size( 400,25 ) )

    fgSizer922.Add( self.PackageFile, 0, wx.ALL, 5 )

    bSizer4.Add( fgSizer922, 1, wx.EXPAND, 5 )

    fgSizer91 = wx.FlexGridSizer( 0, 3, 0, 0 )
    fgSizer91.SetFlexibleDirection( wx.BOTH )
    fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"             Protocol GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText81.Wrap( -1 )
    fgSizer91.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.ProtocolGuidValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 305,-1 ), 0 )
    fgSizer91.Add( self.ProtocolGuidValue, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.GenerateGuid = wx.Button( self, wx.ID_ANY, u"Generate GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer91.Add( self.GenerateGuid, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

    bSizer4.Add( fgSizer91, 1, wx.EXPAND, 5 )

    fgSizer923 = wx.FlexGridSizer( 2, 2, 0, 0 )
    fgSizer923.SetFlexibleDirection( wx.BOTH )
    fgSizer923.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText823 = wx.StaticText( self, wx.ID_ANY, u"Protocol Include Name", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText823.Wrap( -1 )
    fgSizer923.Add( self.m_staticText823, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.ProtocolIncludeName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 310,-1 ), 0 )
    fgSizer923.Add( self.ProtocolIncludeName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    bSizer4.Add( fgSizer923, 1, wx.EXPAND, 5 )

    self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer21.Add( bSizer4, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Finish.SetDefault()
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.ALL, 5 )

    bSizer21.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer21 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.PackageFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.PackageFileOnFileChanged )
    self.ProtocolGuidValue.Bind( wx.EVT_TEXT, self.ProtocolGuidValueOnText )
    self.GenerateGuid.Bind( wx.EVT_BUTTON, self.GenerateGuidOnButtonClick )
    self.ProtocolIncludeName.Bind( wx.EVT_TEXT, self.ProtocolIncludeNameOnText )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def PackageFileOnFileChanged( self, event ):
    event.Skip()

  def ProtocolGuidValueOnText( self, event ):
    event.Skip()

  def GenerateGuidOnButtonClick( self, event ):
    event.Skip()

  def ProtocolIncludeNameOnText( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

###########################################################################
## Class NewGuid
###########################################################################

class NewGuid ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New GUID", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer23 = wx.BoxSizer( wx.VERTICAL )

    bSizer4 = wx.BoxSizer( wx.VERTICAL )

    bSizer4.SetMinSize( wx.Size( -1,220 ) )
    self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

    fgSizer922 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer922.SetFlexibleDirection( wx.BOTH )
    fgSizer922.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText822 = wx.StaticText( self, wx.ID_ANY, u"         Package File", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText822.Wrap( -1 )
    fgSizer922.Add( self.m_staticText822, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.PackageFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select EDK II Package File", u"*.dec", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
    self.PackageFile.SetMinSize( wx.Size( 400,25 ) )

    fgSizer922.Add( self.PackageFile, 0, wx.ALL, 5 )

    bSizer4.Add( fgSizer922, 1, wx.EXPAND, 5 )

    fgSizer91 = wx.FlexGridSizer( 0, 3, 0, 0 )
    fgSizer91.SetFlexibleDirection( wx.BOTH )
    fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"                    GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText81.Wrap( -1 )
    fgSizer91.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.GuidValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 306,-1 ), 0 )
    fgSizer91.Add( self.GuidValue, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.GenerateGuid = wx.Button( self, wx.ID_ANY, u"Generate GUID", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer91.Add( self.GenerateGuid, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

    bSizer4.Add( fgSizer91, 1, wx.EXPAND, 5 )

    fgSizer923 = wx.FlexGridSizer( 2, 2, 0, 0 )
    fgSizer923.SetFlexibleDirection( wx.BOTH )
    fgSizer923.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText823 = wx.StaticText( self, wx.ID_ANY, u"GUID Include Name", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText823.Wrap( -1 )
    fgSizer923.Add( self.m_staticText823, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.GuidIncludeName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 305,-1 ), 0 )
    fgSizer923.Add( self.GuidIncludeName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    bSizer4.Add( fgSizer923, 1, wx.EXPAND, 5 )

    self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer23.Add( bSizer4, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Finish.SetDefault()
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.ALL, 5 )

    bSizer23.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer23 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.PackageFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.PackageFileOnFileChanged )
    self.GuidValue.Bind( wx.EVT_TEXT, self.GuidValueOnText )
    self.GenerateGuid.Bind( wx.EVT_BUTTON, self.GenerateGuidOnButtonClick )
    self.GuidIncludeName.Bind( wx.EVT_TEXT, self.GuidIncludeNameOnText )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def PackageFileOnFileChanged( self, event ):
    event.Skip()

  def GuidValueOnText( self, event ):
    event.Skip()

  def GenerateGuidOnButtonClick( self, event ):
    event.Skip()

  def GuidIncludeNameOnText( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

###########################################################################
## Class NewLibraryClass
###########################################################################

class NewLibraryClass ( wx.Dialog ):

  def __init__( self, parent ):
    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Library Class", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_DIALOG_STYLE )

    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

    bSizer25 = wx.BoxSizer( wx.VERTICAL )

    bSizer4 = wx.BoxSizer( wx.VERTICAL )

    bSizer4.SetMinSize( wx.Size( -1,220 ) )
    self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

    fgSizer922 = wx.FlexGridSizer( 1, 2, 0, 0 )
    fgSizer922.SetFlexibleDirection( wx.BOTH )
    fgSizer922.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText822 = wx.StaticText( self, wx.ID_ANY, u"                     Package File", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText822.Wrap( -1 )
    fgSizer922.Add( self.m_staticText822, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    self.PackageFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select EDK II Package File", u"*.dec", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
    self.PackageFile.SetMinSize( wx.Size( 400,25 ) )

    fgSizer922.Add( self.PackageFile, 0, wx.ALL, 5 )

    bSizer4.Add( fgSizer922, 1, wx.EXPAND, 5 )

    fgSizer923 = wx.FlexGridSizer( 2, 2, 0, 0 )
    fgSizer923.SetFlexibleDirection( wx.BOTH )
    fgSizer923.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.m_staticText823 = wx.StaticText( self, wx.ID_ANY, u"Library Class Include Name", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.m_staticText823.Wrap( -1 )
    fgSizer923.Add( self.m_staticText823, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

    self.LibraryClassIncludeName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 310,-1 ), 0 )
    fgSizer923.Add( self.LibraryClassIncludeName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

    bSizer4.Add( fgSizer923, 1, wx.EXPAND, 5 )

    self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer4.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

    bSizer25.Add( bSizer4, 0, wx.EXPAND, 5 )

    fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
    fgSizer1.SetFlexibleDirection( wx.BOTH )
    fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

    self.Finish = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.Finish.SetDefault()
    fgSizer1.Add( self.Finish, 0, wx.ALL, 5 )

    self.Cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    fgSizer1.Add( self.Cancel, 0, wx.ALL, 5 )

    bSizer25.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )

    self.SetSizer( bSizer25 )
    self.Layout()

    self.Centre( wx.BOTH )

    # Connect Events
    self.PackageFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.PackageFileOnFileChanged )
    self.LibraryClassIncludeName.Bind( wx.EVT_TEXT, self.LibraryClassIncludeNameOnText )
    self.Finish.Bind( wx.EVT_BUTTON, self.FinishOnButtonClick )
    self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

  def __del__( self ):
    pass


  # Virtual event handlers, overide them in your derived class
  def PackageFileOnFileChanged( self, event ):
    event.Skip()

  def LibraryClassIncludeNameOnText( self, event ):
    event.Skip()

  def FinishOnButtonClick( self, event ):
    event.Skip()

  def CancelOnButtonClick( self, event ):
    event.Skip()
  

