# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Shortcuts Generator Pro", pos = wx.DefaultPosition, size = wx.Size( 886,448 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.main_menubar = wx.MenuBar( 0 )
		self.main_menu = wx.Menu()
		self.home_menu_bar = wx.MenuItem( self.main_menu, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menu.AppendItem( self.home_menu_bar )
		
		self.new_shortcut = wx.MenuItem( self.main_menu, wx.ID_ANY, u"Add New Shortcut", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menu.AppendItem( self.new_shortcut )
		
		self.show_current_shortcuts = wx.MenuItem( self.main_menu, wx.ID_ANY, u"Show Current Shortcuts", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menu.AppendItem( self.show_current_shortcuts )
		
		self.main_menubar.Append( self.main_menu, u"Menu" ) 
		
		self.SetMenuBar( self.main_menubar )
		
		main_box_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.main_panel.SetBackgroundColour( wx.Colour( 18, 153, 218 ) )
		
		main_panel_box_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.project_name = wx.StaticText( self.main_panel, wx.ID_ANY, u"Shortcut Generator Pro", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.project_name.Wrap( -1 )
		self.project_name.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		main_panel_box_sizer.Add( self.project_name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.new_shortcut_button = wx.Button( self.main_panel, wx.ID_ANY, u"New Shortcut", wx.Point( -1,-1 ), wx.Size( 300,60 ), 0 )
		self.new_shortcut_button.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		main_panel_box_sizer.Add( self.new_shortcut_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 25 )
		
		self.current_shortcuts_button = wx.Button( self.main_panel, wx.ID_ANY, u"Current Shortcuts", wx.DefaultPosition, wx.Size( 300,60 ), 0 )
		self.current_shortcuts_button.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		main_panel_box_sizer.Add( self.current_shortcuts_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 25 )
		
		
		self.main_panel.SetSizer( main_panel_box_sizer )
		self.main_panel.Layout()
		main_panel_box_sizer.Fit( self.main_panel )
		main_box_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.new_shortcut_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.new_shortcut_panel.SetBackgroundColour( wx.Colour( 128, 128, 0 ) )
		self.new_shortcut_panel.Hide()
		
		new_shortcut_grid_sizer = wx.GridSizer( 0, 2, 0, 0 )
		
		special_keys_and_computer_selection_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		special_keys_and_computer_selection_sizer.SetFlexibleDirection( wx.BOTH )
		special_keys_and_computer_selection_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		special_buttons_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.special_keys = wx.StaticText( self.new_shortcut_panel, wx.ID_ANY, u"Click to add a key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.special_keys.Wrap( -1 )
		self.special_keys.SetFont( wx.Font( 16, 74, 90, 90, False, "Arial" ) )
		
		special_buttons_sizer.Add( self.special_keys, 0, wx.ALL, 10 )
		
		special_keys_listChoices = []
		self.special_keys_list = wx.ListBox( self.new_shortcut_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,300 ), special_keys_listChoices, 0 )
		self.special_keys_list.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		special_buttons_sizer.Add( self.special_keys_list, 0, wx.ALL, 10 )
		
		
		special_keys_and_computer_selection_sizer.Add( special_buttons_sizer, 1, wx.EXPAND, 5 )
		
		computer_selection_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.choose_computer_for_action_label = wx.StaticText( self.new_shortcut_panel, wx.ID_ANY, u"Choose a computer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.choose_computer_for_action_label.Wrap( -1 )
		self.choose_computer_for_action_label.SetFont( wx.Font( 16, 74, 90, 90, False, "Arial" ) )
		
		computer_selection_sizer.Add( self.choose_computer_for_action_label, 0, wx.ALL, 10 )
		
		choose_computer_for_actionChoices = []
		self.choose_computer_for_action = wx.Choice( self.new_shortcut_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), choose_computer_for_actionChoices, 0 )
		self.choose_computer_for_action.SetSelection( 0 )
		computer_selection_sizer.Add( self.choose_computer_for_action, 0, wx.ALL, 5 )
		
		
		computer_selection_sizer.AddSpacer( ( 0, 160), 0, wx.EXPAND, 5 )
		
		self.add_plus_to_sequence_button = wx.Button( self.new_shortcut_panel, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.add_plus_to_sequence_button.SetFont( wx.Font( 16, 74, 90, 90, False, "Arial" ) )
		
		computer_selection_sizer.Add( self.add_plus_to_sequence_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		special_keys_and_computer_selection_sizer.Add( computer_selection_sizer, 1, wx.EXPAND, 5 )
		
		
		new_shortcut_grid_sizer.Add( special_keys_and_computer_selection_sizer, 1, wx.EXPAND, 5 )
		
		choose_action_sizer = wx.GridSizer( 0, 1, 0, 0 )
		
		self.choices_text = wx.StaticText( self.new_shortcut_panel, wx.ID_ANY, u"Choose An Action", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.choices_text.Wrap( -1 )
		self.choices_text.SetFont( wx.Font( 20, 74, 90, 90, False, "Arial" ) )
		
		choose_action_sizer.Add( self.choices_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 10 )
		
		shortcuts_choicesChoices = []
		self.shortcuts_choices = wx.Choice( self.new_shortcut_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,150 ), shortcuts_choicesChoices, 0 )
		self.shortcuts_choices.SetSelection( 0 )
		self.shortcuts_choices.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		choose_action_sizer.Add( self.shortcuts_choices, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.enter_sequence_text = wx.StaticText( self.new_shortcut_panel, wx.ID_ANY, u"Enter Your Sequence Here", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.enter_sequence_text.Wrap( -1 )
		self.enter_sequence_text.SetFont( wx.Font( 20, 74, 90, 90, False, "Arial" ) )
		
		choose_action_sizer.Add( self.enter_sequence_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.sequence_text_control = wx.TextCtrl( self.new_shortcut_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,30 ), 0 )
		self.sequence_text_control.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		choose_action_sizer.Add( self.sequence_text_control, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.add_new_shortcut_button = wx.Button( self.new_shortcut_panel, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 150,50 ), 0 )
		self.add_new_shortcut_button.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		choose_action_sizer.Add( self.add_new_shortcut_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		new_shortcut_grid_sizer.Add( choose_action_sizer, 1, wx.EXPAND, 5 )
		
		
		self.new_shortcut_panel.SetSizer( new_shortcut_grid_sizer )
		self.new_shortcut_panel.Layout()
		new_shortcut_grid_sizer.Fit( self.new_shortcut_panel )
		main_box_sizer.Add( self.new_shortcut_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.current_shortcuts_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.current_shortcuts_panel.SetBackgroundColour( wx.Colour( 255, 128, 64 ) )
		self.current_shortcuts_panel.Hide()
		
		current_shortcuts_sizer = wx.GridSizer( 0, 2, 0, 100 )
		
		choose_and_delete_sizer = wx.GridSizer( 0, 1, 0, 0 )
		
		self.choose_computer_text = wx.StaticText( self.current_shortcuts_panel, wx.ID_ANY, u"Choose Computer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.choose_computer_text.Wrap( -1 )
		self.choose_computer_text.SetFont( wx.Font( 18, 74, 90, 90, False, "Arial" ) )
		
		choose_and_delete_sizer.Add( self.choose_computer_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		computer_choiceChoices = []
		self.computer_choice = wx.Choice( self.current_shortcuts_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,-1 ), computer_choiceChoices, 0 )
		self.computer_choice.SetSelection( 0 )
		choose_and_delete_sizer.Add( self.computer_choice, 0, wx.ALL, 5 )
		
		self.select_row_num_text = wx.StaticText( self.current_shortcuts_panel, wx.ID_ANY, u"Select row number to delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.select_row_num_text.Wrap( -1 )
		self.select_row_num_text.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		choose_and_delete_sizer.Add( self.select_row_num_text, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		delete_number_choiceChoices = []
		self.delete_number_choice = wx.Choice( self.current_shortcuts_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), delete_number_choiceChoices, 0 )
		self.delete_number_choice.SetSelection( 0 )
		self.delete_number_choice.SetFont( wx.Font( 11, 74, 90, 90, False, "Arial" ) )
		
		choose_and_delete_sizer.Add( self.delete_number_choice, 0, wx.ALL, 5 )
		
		self.delete_button = wx.Button( self.current_shortcuts_panel, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.Size( 150,50 ), 0 )
		self.delete_button.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		choose_and_delete_sizer.Add( self.delete_button, 0, wx.ALL, 10 )
		
		
		current_shortcuts_sizer.Add( choose_and_delete_sizer, 1, wx.EXPAND, 5 )
		
		shortcuts_grid_sizer = wx.GridSizer( 0, 1, 0, 0 )
		
		self.computer_shortcuts_grid = wx.grid.Grid( self.current_shortcuts_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		# Grid
		self.computer_shortcuts_grid.CreateGrid( 20, 3 )
		self.computer_shortcuts_grid.EnableEditing( False )
		self.computer_shortcuts_grid.EnableGridLines( True )
		self.computer_shortcuts_grid.EnableDragGridSize( False )
		self.computer_shortcuts_grid.SetMargins( 0, 0 )
		
		# Columns
		self.computer_shortcuts_grid.EnableDragColMove( False )
		self.computer_shortcuts_grid.EnableDragColSize( True )
		self.computer_shortcuts_grid.SetColLabelSize( 30 )
		self.computer_shortcuts_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.computer_shortcuts_grid.SetRowSize( 0, 19 )
		self.computer_shortcuts_grid.SetRowSize( 1, 19 )
		self.computer_shortcuts_grid.SetRowSize( 2, 19 )
		self.computer_shortcuts_grid.SetRowSize( 3, 19 )
		self.computer_shortcuts_grid.SetRowSize( 4, 19 )
		self.computer_shortcuts_grid.SetRowSize( 5, 19 )
		self.computer_shortcuts_grid.SetRowSize( 6, 19 )
		self.computer_shortcuts_grid.SetRowSize( 7, 19 )
		self.computer_shortcuts_grid.SetRowSize( 8, 19 )
		self.computer_shortcuts_grid.SetRowSize( 9, 19 )
		self.computer_shortcuts_grid.SetRowSize( 10, 19 )
		self.computer_shortcuts_grid.SetRowSize( 11, 19 )
		self.computer_shortcuts_grid.SetRowSize( 12, 19 )
		self.computer_shortcuts_grid.SetRowSize( 13, 19 )
		self.computer_shortcuts_grid.SetRowSize( 14, 19 )
		self.computer_shortcuts_grid.SetRowSize( 15, 19 )
		self.computer_shortcuts_grid.SetRowSize( 16, 19 )
		self.computer_shortcuts_grid.SetRowSize( 17, 19 )
		self.computer_shortcuts_grid.AutoSizeRows()
		self.computer_shortcuts_grid.EnableDragRowSize( True )
		self.computer_shortcuts_grid.SetRowLabelSize( 20 )
		self.computer_shortcuts_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.computer_shortcuts_grid.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_BOTTOM )
		shortcuts_grid_sizer.Add( self.computer_shortcuts_grid, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		current_shortcuts_sizer.Add( shortcuts_grid_sizer, 1, wx.EXPAND, 5 )
		
		
		self.current_shortcuts_panel.SetSizer( current_shortcuts_sizer )
		self.current_shortcuts_panel.Layout()
		current_shortcuts_sizer.Fit( self.current_shortcuts_panel )
		main_box_sizer.Add( self.current_shortcuts_panel, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		
		self.SetSizer( main_box_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.update_user_data )
		self.Bind( wx.EVT_MENU, self.go_to_home_panel, id = self.home_menu_bar.GetId() )
		self.Bind( wx.EVT_MENU, self.add_new_shortcut_menu, id = self.new_shortcut.GetId() )
		self.Bind( wx.EVT_MENU, self.show_current_shortcuts_menu, id = self.show_current_shortcuts.GetId() )
		self.new_shortcut_button.Bind( wx.EVT_BUTTON, self.add_new_shortcut_menu )
		self.current_shortcuts_button.Bind( wx.EVT_BUTTON, self.show_current_shortcuts_menu )
		self.special_keys_list.Bind( wx.EVT_LISTBOX_DCLICK, self.add_special_key_to_the_sequence )
		self.choose_computer_for_action.Bind( wx.EVT_CHOICE, self.choose_a_computer_for_action )
		self.add_plus_to_sequence_button.Bind( wx.EVT_BUTTON, self.add_plus_to_sequence )
		self.shortcuts_choices.Bind( wx.EVT_CHOICE, self.save_user_choice )
		self.sequence_text_control.Bind( wx.EVT_TEXT, self.check_sequence_input )
		self.add_new_shortcut_button.Bind( wx.EVT_BUTTON, self.add_new_shortcut_to_the_list )
		self.delete_number_choice.Bind( wx.EVT_CHOICE, self.select_shortcut_to_delete )
		self.delete_button.Bind( wx.EVT_BUTTON, self.delete_a_shortcut_from_the_grid )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def update_user_data( self, event ):
		event.Skip()
	
	def go_to_home_panel( self, event ):
		event.Skip()
	
	def add_new_shortcut_menu( self, event ):
		event.Skip()
	
	def show_current_shortcuts_menu( self, event ):
		event.Skip()
	
	
	
	def add_special_key_to_the_sequence( self, event ):
		event.Skip()
	
	def choose_a_computer_for_action( self, event ):
		event.Skip()
	
	def add_plus_to_sequence( self, event ):
		event.Skip()
	
	def save_user_choice( self, event ):
		event.Skip()
	
	def check_sequence_input( self, event ):
		event.Skip()
	
	def add_new_shortcut_to_the_list( self, event ):
		event.Skip()
	
	def select_shortcut_to_delete( self, event ):
		event.Skip()
	
	def delete_a_shortcut_from_the_grid( self, event ):
		event.Skip()
	

