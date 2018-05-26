# -*- coding: utf-8 -*-
###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
#
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.dataview

###########################################################################
# Class MainFrame
###########################################################################


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=u"Shortcuts Generator Pro",
                          pos=wx.DefaultPosition, size=wx.Size(886, 448),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX |
                                wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.main_menubar = wx.MenuBar(0)
        self.main_menu = wx.Menu()
        self.home_menu_bar = wx.MenuItem(self.main_menu, wx.ID_ANY, u"Home",
                                         wx.EmptyString, wx.ITEM_NORMAL)
        self.main_menu.AppendItem(self.home_menu_bar)

        self.new_shortcut = wx.MenuItem(self.main_menu, wx.ID_ANY,
                                        u"Add New Shortcut", wx.EmptyString,
                                        wx.ITEM_NORMAL)
        self.main_menu.AppendItem(self.new_shortcut)

        self.show_current_shortcuts = wx.MenuItem(self.main_menu, wx.ID_ANY,
                                                  u"Show Current Shortcuts",
                                                  wx.EmptyString,
                                                  wx.ITEM_NORMAL)
        self.main_menu.AppendItem(self.show_current_shortcuts)

        self.add_new_computer_menu_bar = wx.MenuItem(self.main_menu, wx.ID_ANY,
                                                     u"Manage Computers",
                                                     wx.EmptyString,
                                                     wx.ITEM_NORMAL)
        self.main_menu.AppendItem(self.add_new_computer_menu_bar)

        self.main_menubar.Append(self.main_menu, u"Menu")

        self.SetMenuBar(self.main_menubar)

        main_box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                   wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.main_panel.SetBackgroundColour(wx.Colour(18, 153, 218))

        main_panel_box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.project_name = wx.StaticText(self.main_panel, wx.ID_ANY,
                                          u"Shortcut Generator Pro",
                                          wx.Point(-1, -1), wx.DefaultSize, 0)
        self.project_name.Wrap(-1)
        self.project_name.SetFont(
            wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        main_panel_box_sizer.Add(self.project_name, 0,
                                 wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.new_shortcut_button = wx.Button(self.main_panel, wx.ID_ANY,
                                             u"New Shortcut", wx.Point(-1, -1),
                                             wx.Size(300, 60), 0)
        self.new_shortcut_button.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        main_panel_box_sizer.Add(self.new_shortcut_button, 0,
                                 wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 25)

        self.current_shortcuts_button = wx.Button(self.main_panel, wx.ID_ANY,
                                                  u"Shortcuts -  History",
                                                  wx.DefaultPosition,
                                                  wx.Size(300, 60), 0)
        self.current_shortcuts_button.SetFont(
            wx.Font(18, 70, 90, 90, False, wx.EmptyString))

        main_panel_box_sizer.Add(self.current_shortcuts_button, 0,
                                 wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 25)

        self.main_add_new_computer_button = wx.Button(self.main_panel,
                                                      wx.ID_ANY,
                                                      u"Add /"
                                                      u" Remove Computers",
                                                      wx.DefaultPosition,
                                                      wx.Size(300, 60), 0)
        self.main_add_new_computer_button.SetFont(
            wx.Font(18, 74, 90, 90, False, "Arial"))

        main_panel_box_sizer.Add(self.main_add_new_computer_button, 0,
                                 wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 25)

        self.main_panel.SetSizer(main_panel_box_sizer)
        self.main_panel.Layout()
        main_panel_box_sizer.Fit(self.main_panel)
        main_box_sizer.Add(self.main_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.new_shortcut_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.new_shortcut_panel.SetBackgroundColour(wx.Colour(5, 122, 84))
        self.new_shortcut_panel.Hide()

        new_shortcut_grid_sizer = wx.FlexGridSizer(0, 4, 0, 0)
        new_shortcut_grid_sizer.SetFlexibleDirection(wx.BOTH)
        new_shortcut_grid_sizer.SetNonFlexibleGrowMode(
            wx.FLEX_GROWMODE_SPECIFIED)

        special_buttons_sizer = wx.BoxSizer(wx.VERTICAL)

        self.special_keys_header_text = wx.StaticText(self.new_shortcut_panel,
                                                      wx.ID_ANY,
                                                      u"Special Keys",
                                                      wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.special_keys_header_text.Wrap(-1)
        self.special_keys_header_text.SetFont(
            wx.Font(16, 74, 90, 90, False, "Arial"))

        special_buttons_sizer.Add(self.special_keys_header_text, 0, wx.ALL, 5)

        self.special_keys = wx.StaticText(self.new_shortcut_panel, wx.ID_ANY,
                                          u"Click to add a key",
                                          wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.special_keys.Wrap(-1)
        self.special_keys.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))

        special_buttons_sizer.Add(self.special_keys, 0,
                                  wx.BOTTOM | wx.RIGHT | wx.LEFT, 10)

        special_keys_listChoices = []
        self.special_keys_list = wx.ListBox(self.new_shortcut_panel, wx.ID_ANY,
                                            wx.DefaultPosition,
                                            wx.Size(-1, 300),
                                            special_keys_listChoices, 0)
        self.special_keys_list.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))

        special_buttons_sizer.Add(self.special_keys_list, 0, wx.ALL, 10)

        new_shortcut_grid_sizer.Add(special_buttons_sizer, 1, wx.EXPAND, 5)

        spacer_sizer = wx.BoxSizer(wx.VERTICAL)

        spacer_sizer.AddSpacer((100, 0), 0, wx.EXPAND, 5)

        new_shortcut_grid_sizer.Add(spacer_sizer, 1, wx.EXPAND, 5)

        computer_selection_sizer = wx.BoxSizer(wx.VERTICAL)

        self.choose_computer_for_action_label = wx.StaticText(
            self.new_shortcut_panel, wx.ID_ANY, u"Choose a computer",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.choose_computer_for_action_label.Wrap(-1)
        self.choose_computer_for_action_label.SetFont(
            wx.Font(16, 74, 90, 90, False, "Arial"))

        computer_selection_sizer.Add(self.choose_computer_for_action_label, 0,
                                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)

        choose_computer_for_actionChoices = []
        self.choose_computer_for_action = wx.Choice(
            self.new_shortcut_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.Size(300, -1),
            choose_computer_for_actionChoices,
            0)
        self.choose_computer_for_action.SetSelection(0)
        self.choose_computer_for_action.SetFont(
            wx.Font(14, 74, 90, 90, False, "Arial"))

        computer_selection_sizer.Add(self.choose_computer_for_action, 0,
                                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.choices_text = wx.StaticText(self.new_shortcut_panel, wx.ID_ANY,
                                          u"Choose An Action",
                                          wx.Point(-1, -1), wx.DefaultSize, 0)
        self.choices_text.Wrap(-1)
        self.choices_text.SetFont(wx.Font(16, 74, 90, 90, False, "Arial"))

        computer_selection_sizer.Add(self.choices_text, 0,
                                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |
                                     wx.ALIGN_BOTTOM,
                                     10)

        shortcuts_choicesChoices = []
        self.shortcuts_choices = wx.Choice(self.new_shortcut_panel, wx.ID_ANY,
                                           wx.DefaultPosition,
                                           wx.Size(300, 80),
                                           shortcuts_choicesChoices, 0)
        self.shortcuts_choices.SetSelection(0)
        self.shortcuts_choices.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))

        computer_selection_sizer.Add(self.shortcuts_choices, 0,
                                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.enter_sequence_text = wx.StaticText(self.new_shortcut_panel,
                                                 wx.ID_ANY,
                                                 u"Enter Your Sequence Here",
                                                 wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.enter_sequence_text.Wrap(-1)
        self.enter_sequence_text.SetFont(
            wx.Font(18, 74, 90, 90, False, "Arial"))

        computer_selection_sizer.Add(self.enter_sequence_text, 0,
                                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |
                                     wx.ALIGN_BOTTOM,
                                     5)

        self.sequence_useg_text = wx.StaticText(self.new_shortcut_panel,
                                                wx.ID_ANY,
                                                u"Use special keys, +"
                                                u", keyboard",
                                                wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.sequence_useg_text.Wrap(-1)
        self.sequence_useg_text.SetFont(
            wx.Font(14, 74, 90, 90, False, "Arial"))

        computer_selection_sizer.Add(self.sequence_useg_text, 0,
                                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.sequence_text_control = wx.TextCtrl(self.new_shortcut_panel,
                                                 wx.ID_ANY, wx.EmptyString,
                                                 wx.DefaultPosition,
                                                 wx.Size(300, 30), 0)
        self.sequence_text_control.SetFont(
            wx.Font(12, 74, 90, 90, False, "Arial"))

        computer_selection_sizer.Add(self.sequence_text_control, 0,
                                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        new_shortcut_grid_sizer.Add(computer_selection_sizer, 1, wx.EXPAND, 5)

        buttons_sizer = wx.BoxSizer(wx.VERTICAL)

        buttons_sizer.AddSpacer((300, 0), 0, wx.EXPAND, 5)

        self.add_new_shortcut_button = wx.Button(self.new_shortcut_panel,
                                                 wx.ID_ANY, u"Create",
                                                 wx.DefaultPosition,
                                                 wx.Size(150, 50), 0)
        self.add_new_shortcut_button.SetFont(
            wx.Font(14, 74, 90, 90, False, "Arial"))

        buttons_sizer.Add(self.add_new_shortcut_button, 0,
                          wx.ALL | wx.ALIGN_RIGHT, 5)

        buttons_sizer.AddSpacer((0, 190), 0, wx.EXPAND, 5)

        self.add_plus_to_sequence_button = wx.Button(self.new_shortcut_panel,
                                                     wx.ID_ANY, u"+",
                                                     wx.DefaultPosition,
                                                     wx.Size(80, 50), 0)
        self.add_plus_to_sequence_button.SetFont(
            wx.Font(16, 74, 90, 90, False, "Arial"))

        buttons_sizer.Add(self.add_plus_to_sequence_button, 0, wx.ALL, 5)

        new_shortcut_grid_sizer.Add(buttons_sizer, 1, wx.EXPAND, 5)

        self.new_shortcut_panel.SetSizer(new_shortcut_grid_sizer)
        self.new_shortcut_panel.Layout()
        new_shortcut_grid_sizer.Fit(self.new_shortcut_panel)
        main_box_sizer.Add(self.new_shortcut_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.current_shortcuts_panel = wx.Panel(self, wx.ID_ANY,
                                                wx.DefaultPosition,
                                                wx.Size(-1, -1),
                                                wx.TAB_TRAVERSAL)
        self.current_shortcuts_panel.SetBackgroundColour(
            wx.Colour(255, 128, 64))
        self.current_shortcuts_panel.Hide()

        current_shortcuts_sizer = wx.GridSizer(0, 2, 0, 100)

        choose_and_delete_sizer = wx.GridSizer(0, 1, 0, 0)

        self.choose_computer_text = wx.StaticText(self.current_shortcuts_panel,
                                                  wx.ID_ANY,
                                                  u"Choose Computer",
                                                  wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.choose_computer_text.Wrap(-1)
        self.choose_computer_text.SetFont(
            wx.Font(18, 74, 90, 90, False, "Arial"))

        choose_and_delete_sizer.Add(self.choose_computer_text, 0,
                                    wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        computer_choiceChoices = []
        self.computer_choice = wx.Choice(self.current_shortcuts_panel,
                                         wx.ID_ANY, wx.DefaultPosition,
                                         wx.Size(270, -1),
                                         computer_choiceChoices, 0)
        self.computer_choice.SetSelection(0)
        self.computer_choice.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))

        choose_and_delete_sizer.Add(self.computer_choice, 0, wx.ALL, 5)

        self.select_row_num_text = wx.StaticText(
            self.current_shortcuts_panel,
            wx.ID_ANY,
            u"Select row number to delete",
            wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.select_row_num_text.Wrap(-1)
        self.select_row_num_text.SetFont(
            wx.Font(14, 74, 90, 90, False, "Arial"))

        choose_and_delete_sizer.Add(self.select_row_num_text, 0,
                                    wx.ALL | wx.ALIGN_BOTTOM, 5)

        delete_number_choiceChoices = []
        self.delete_number_choice = wx.Choice(self.current_shortcuts_panel,
                                              wx.ID_ANY, wx.DefaultPosition,
                                              wx.Size(40, -1),
                                              delete_number_choiceChoices, 0)
        self.delete_number_choice.SetSelection(0)
        self.delete_number_choice.SetFont(
            wx.Font(11, 74, 90, 90, False, "Arial"))

        choose_and_delete_sizer.Add(self.delete_number_choice, 0, wx.ALL, 5)

        delete_buttons_sizer = wx.GridSizer(0, 2, 0, 0)

        self.delete_button = wx.Button(self.current_shortcuts_panel, wx.ID_ANY,
                                       u"Delete", wx.DefaultPosition,
                                       wx.Size(150, 50), 0)
        self.delete_button.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))

        delete_buttons_sizer.Add(self.delete_button, 0, wx.ALL, 10)

        self.delete_all_button = wx.Button(self.current_shortcuts_panel,
                                           wx.ID_ANY, u"Delete All",
                                           wx.DefaultPosition,
                                           wx.Size(150, 50), 0)
        self.delete_all_button.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))

        delete_buttons_sizer.Add(self.delete_all_button, 0, wx.ALL, 10)

        choose_and_delete_sizer.Add(delete_buttons_sizer, 1, wx.EXPAND, 5)

        current_shortcuts_sizer.Add(choose_and_delete_sizer, 1, wx.EXPAND, 5)

        shortcuts_grid_sizer = wx.GridSizer(0, 1, 0, 0)

        self.computer_shortcuts_grid = wx.grid.Grid(
            self.current_shortcuts_panel, wx.ID_ANY, wx.DefaultPosition,
            wx.Size(-1, -1), 0)

        # Grid
        self.computer_shortcuts_grid.CreateGrid(20, 3)
        self.computer_shortcuts_grid.EnableEditing(False)
        self.computer_shortcuts_grid.EnableGridLines(True)
        self.computer_shortcuts_grid.EnableDragGridSize(False)
        self.computer_shortcuts_grid.SetMargins(0, 0)

        # Columns
        self.computer_shortcuts_grid.EnableDragColMove(False)
        self.computer_shortcuts_grid.EnableDragColSize(True)
        self.computer_shortcuts_grid.SetColLabelSize(30)
        self.computer_shortcuts_grid.SetColLabelAlignment(wx.ALIGN_CENTRE,
                                                          wx.ALIGN_CENTRE)

        # Rows
        self.computer_shortcuts_grid.SetRowSize(0, 19)
        self.computer_shortcuts_grid.SetRowSize(1, 19)
        self.computer_shortcuts_grid.SetRowSize(2, 19)
        self.computer_shortcuts_grid.SetRowSize(3, 19)
        self.computer_shortcuts_grid.SetRowSize(4, 19)
        self.computer_shortcuts_grid.SetRowSize(5, 19)
        self.computer_shortcuts_grid.SetRowSize(6, 19)
        self.computer_shortcuts_grid.SetRowSize(7, 19)
        self.computer_shortcuts_grid.SetRowSize(8, 19)
        self.computer_shortcuts_grid.SetRowSize(9, 19)
        self.computer_shortcuts_grid.SetRowSize(10, 19)
        self.computer_shortcuts_grid.SetRowSize(11, 19)
        self.computer_shortcuts_grid.SetRowSize(12, 19)
        self.computer_shortcuts_grid.SetRowSize(13, 19)
        self.computer_shortcuts_grid.SetRowSize(14, 19)
        self.computer_shortcuts_grid.SetRowSize(15, 19)
        self.computer_shortcuts_grid.SetRowSize(16, 19)
        self.computer_shortcuts_grid.SetRowSize(17, 19)
        self.computer_shortcuts_grid.AutoSizeRows()
        self.computer_shortcuts_grid.EnableDragRowSize(True)
        self.computer_shortcuts_grid.SetRowLabelSize(20)
        self.computer_shortcuts_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE,
                                                          wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.computer_shortcuts_grid.SetDefaultCellAlignment(wx.ALIGN_CENTRE,
                                                             wx.ALIGN_BOTTOM)
        shortcuts_grid_sizer.Add(self.computer_shortcuts_grid, 0,
                                 wx.ALL | wx.EXPAND, 5)

        current_shortcuts_sizer.Add(shortcuts_grid_sizer, 1, wx.EXPAND, 5)

        self.current_shortcuts_panel.SetSizer(current_shortcuts_sizer)
        self.current_shortcuts_panel.Layout()
        current_shortcuts_sizer.Fit(self.current_shortcuts_panel)
        main_box_sizer.Add(self.current_shortcuts_panel, 0,
                           wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.manage_computers_panel = wx.Panel(self, wx.ID_ANY,
                                               wx.DefaultPosition,
                                               wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        self.manage_computers_panel.SetFont(
            wx.Font(18, 74, 90, 90, False, "Arial"))
        self.manage_computers_panel.SetBackgroundColour(wx.Colour(113, 70, 95))
        self.manage_computers_panel.Hide()

        manage_computers_sizer = wx.GridSizer(0, 2, 0, 0)

        add_new_computer_sizer = wx.BoxSizer(wx.VERTICAL)

        self.add_new_computer_label = wx.StaticText(
            self.manage_computers_panel, wx.ID_ANY,
            u"Select A Computer To Add", wx.DefaultPosition, wx.DefaultSize, 0)
        self.add_new_computer_label.Wrap(-1)
        self.add_new_computer_label.SetFont(
            wx.Font(18, 74, 90, 90, False, "Arial"))

        add_new_computer_sizer.Add(self.add_new_computer_label, 0,
                                   wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.add_new_computer_list_control = wx.dataview.DataViewListCtrl(
            self.manage_computers_panel, wx.ID_ANY, wx.DefaultPosition,
            wx.Size(300, 250),
            wx.dataview.DV_HORIZ_RULES | wx.dataview.DV_ROW_LINES |
            wx.dataview.DV_VERT_RULES)
        self.add_new_computer_list_control.SetFont(
            wx.Font(12, 74, 90, 90, False, "Arial"))

        self.new_computer_name_label =\
            self.add_new_computer_list_control.AppendTextColumn(u"Name")
        self.new_computer_ip_label =\
            self.add_new_computer_list_control.AppendTextColumn(u"IP")
        add_new_computer_sizer.Add(self.add_new_computer_list_control, 0,
                                   wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        add_computers_buttons_sizer = wx.GridSizer(0, 2, 0, 0)

        self.search_computers_button = wx.Button(self.manage_computers_panel,
                                                 wx.ID_ANY,
                                                 u"Search Computers",
                                                 wx.DefaultPosition,
                                                 wx.Size(180, 50), 0)
        self.search_computers_button.SetFont(
            wx.Font(14, 74, 90, 90, False, "Arial"))

        add_computers_buttons_sizer.Add(self.search_computers_button, 0,
                                        wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
                                        20)

        self.add_new_computer_button = wx.Button(self.manage_computers_panel,
                                                 wx.ID_ANY, u"Add",
                                                 wx.DefaultPosition,
                                                 wx.Size(100, 50), 0)
        self.add_new_computer_button.SetFont(
            wx.Font(14, 74, 90, 90, False, "Arial"))

        add_computers_buttons_sizer.Add(self.add_new_computer_button, 0,
                                        wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
                                        20)

        add_new_computer_sizer.Add(add_computers_buttons_sizer, 1, wx.EXPAND,
                                   5)

        manage_computers_sizer.Add(add_new_computer_sizer, 1, wx.EXPAND, 5)

        delete_computer_sizer = wx.BoxSizer(wx.VERTICAL)

        self.remove_computer_text = wx.StaticText(
            self.manage_computers_panel,
            wx.ID_ANY,
            u"Select A Computer To Delete",
            wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.remove_computer_text.Wrap(-1)
        delete_computer_sizer.Add(self.remove_computer_text, 0,
                                  wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        remove_computer_listboxChoices = []
        self.remove_computer_listbox = wx.ListBox(
            self.manage_computers_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.Size(300, 250),
            remove_computer_listboxChoices,
            0)
        self.remove_computer_listbox.SetFont(
            wx.Font(12, 74, 90, 90, False, "Arial"))

        delete_computer_sizer.Add(self.remove_computer_listbox, 0,
                                  wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.delete_computer_button = wx.Button(self.manage_computers_panel,
                                                wx.ID_ANY, u"Delete",
                                                wx.DefaultPosition,
                                                wx.Size(100, 50), 0)
        self.delete_computer_button.SetFont(
            wx.Font(14, 74, 90, 90, False, "Arial"))

        delete_computer_sizer.Add(self.delete_computer_button, 0,
                                  wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

        manage_computers_sizer.Add(delete_computer_sizer, 1, wx.EXPAND, 5)

        self.manage_computers_panel.SetSizer(manage_computers_sizer)
        self.manage_computers_panel.Layout()
        manage_computers_sizer.Fit(self.manage_computers_panel)
        main_box_sizer.Add(self.manage_computers_panel, 1,
                           wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.SetSizer(main_box_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.update_user_data)
        self.Bind(wx.EVT_MENU, self.go_to_home_panel,
                  id=self.home_menu_bar.GetId())
        self.Bind(wx.EVT_MENU, self.add_new_shortcut_menu,
                  id=self.new_shortcut.GetId())
        self.Bind(wx.EVT_MENU, self.show_current_shortcuts_menu,
                  id=self.show_current_shortcuts.GetId())
        self.Bind(wx.EVT_MENU, self.show_add_new_computer_menu,
                  id=self.add_new_computer_menu_bar.GetId())
        self.new_shortcut_button.Bind(wx.EVT_BUTTON,
                                      self.add_new_shortcut_menu)
        self.current_shortcuts_button.Bind(wx.EVT_BUTTON,
                                           self.show_current_shortcuts_menu)
        self.main_add_new_computer_button.Bind(wx.EVT_BUTTON,
                                               self.show_add_new_computer_menu)
        self.special_keys_list.Bind(wx.EVT_LISTBOX,
                                    self.add_special_key_to_the_sequence)
        self.choose_computer_for_action.Bind(wx.EVT_CHOICE,
                                             self.choose_a_computer_for_action)
        self.shortcuts_choices.Bind(wx.EVT_CHOICE, self.save_user_choice)
        self.sequence_text_control.Bind(wx.EVT_TEXT, self.check_sequence_input)
        self.add_new_shortcut_button.Bind(wx.EVT_BUTTON,
                                          self.add_new_shortcut_to_the_list)
        self.add_plus_to_sequence_button.Bind(wx.EVT_BUTTON,
                                              self.add_plus_to_sequence)
        self.computer_choice.Bind(wx.EVT_CHOICE,
                                  self.get_computer_to_show_shortcuts)
        self.delete_number_choice.Bind(wx.EVT_CHOICE,
                                       self.select_shortcut_to_delete)
        self.delete_button.Bind(wx.EVT_BUTTON,
                                self.delete_a_shortcut_from_the_grid)
        self.delete_all_button.Bind(wx.EVT_BUTTON,
                                    self.delete_all_of_the_computer_shortcuts)
        self.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED,
                  self.choose_computer_name_and_ip_to_add_to_list,
                  id=wx.ID_ANY)
        self.search_computers_button.Bind(wx.EVT_BUTTON,
                                          self.search_computers_in_network)
        self.add_new_computer_button.Bind(wx.EVT_BUTTON,
                                          self.add_new_computer_to_the_list)
        self.remove_computer_listbox.Bind(
            wx.EVT_LISTBOX,
            self.choose_computer_name_and_ip_to_remove_from_list)
        self.delete_computer_button.Bind(wx.EVT_BUTTON,
                                         self.delete_computer_from_saved_list)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def update_user_data(self, event):
        event.Skip()

    def go_to_home_panel(self, event):
        event.Skip()

    def add_new_shortcut_menu(self, event):
        event.Skip()

    def show_current_shortcuts_menu(self, event):
        event.Skip()

    def show_add_new_computer_menu(self, event):
        event.Skip()

    def add_special_key_to_the_sequence(self, event):
        event.Skip()

    def choose_a_computer_for_action(self, event):
        event.Skip()

    def save_user_choice(self, event):
        event.Skip()

    def check_sequence_input(self, event):
        event.Skip()

    def add_new_shortcut_to_the_list(self, event):
        event.Skip()

    def add_plus_to_sequence(self, event):
        event.Skip()

    def get_computer_to_show_shortcuts(self, event):
        event.Skip()

    def select_shortcut_to_delete(self, event):
        event.Skip()

    def delete_a_shortcut_from_the_grid(self, event):
        event.Skip()

    def delete_all_of_the_computer_shortcuts(self, event):
        event.Skip()

    def choose_computer_name_and_ip_to_add_to_list(self, event):
        event.Skip()

    def search_computers_in_network(self, event):
        event.Skip()

    def add_new_computer_to_the_list(self, event):
        event.Skip()

    def choose_computer_name_and_ip_to_remove_from_list(self, event):
        event.Skip()

    def delete_computer_from_saved_list(self, event):
        event.Skip()
