# -*- coding: utf-8 -*-

from shortcuts import ShortCuts
import wx
import shortcut_menu_wx_skeleton
import os
from Tkinter import *
import tkMessageBox

USER_DATA_FILE_NAME = 'user_data.json'
SPECIAL_CHARACTERS_LIST = ['windows', 'alt', 'control', 'shift', 'space', 'backspace', 'enter']
SHORTCUT_OPTIONS = ['open folder', 'open url', 'open program', 'open cmd', 'open settings']
SHORTCUT_GRID_LABELS = {0: 'Action', 1: 'Argument', 2: 'Sequence'}
SEQUENCE_ERROR = 'Not a legal sequence'
ACTION_ERROR = 'Choose a action'
DELETE_BUTTON_ERROR = 'Row number was not selected'

class Main(shortcut_menu_wx_skeleton.MainFrame):
    #constructor
    def __init__(self, parent):
        shortcut_menu_wx_skeleton.MainFrame.__init__(self, parent)
        self.__shortcuts_user = ShortCuts()
        self.__row_selection_number = 0
        self.__selected_file_name_to_delete = {'file name': '', 'action': ''}
        self.__input_status = {'sequence': False, 'action': False, 'row number to delete': False}
        self.check_if_first_time()

#-------------------------------------------------------------------------------
    def check_if_first_time(self):
        if os.path.isfile(USER_DATA_FILE_NAME):
            self.__shortcuts_user.get_user_previous_activity()
#-------------------------------------------------------------------------------
    def add_new_shortcut_menu(self, event):
        self.show_new_shortcut_panel()
        self.add_special_characters_to_the_add_table()
        self.add_options_to_shortcut_list()

#-------------------------------------------------------------------------------
    def show_new_shortcut_panel(self):
        self.new_shortcut_panel.Show()
        self.main_panel.Hide()
        self.current_shortcuts_panel.Hide()
        self.new_shortcut_panel.GetSizer().Layout()
        self.new_shortcut_panel.GetParent().Layout()

#-------------------------------------------------------------------------------
    def add_new_shortcut_to_the_list(self, event):
        print '+'.join(self.__shortcuts_user.get_shortcut_sequence()), '---sequence---'

        if self.__input_status['sequence'] and self.__input_status['action']:
            self.__shortcuts_user.write_new_shortcut()
            self.__shortcuts_user.save_user_activity()

        elif not self.__input_status['sequence'] and self.__input_status['action']:
            self.open_error_dialog(SEQUENCE_ERROR)

        elif self.__input_status['sequence'] and not self.__input_status['action'] or not self.__input_status['sequence'] and not self.__input_status['action']:
            self.open_error_dialog(ACTION_ERROR)

#-------------------------------------------------------------------------------
    def save_user_choice(self, event):
        print SHORTCUT_OPTIONS[self.shortcuts_choices.GetSelection()], '---action---'
        self.__shortcuts_user.set_users_choice(SHORTCUT_OPTIONS[self.shortcuts_choices.GetSelection()])
        self.__input_status['action'] = True

#-------------------------------------------------------------------------------
    def add_special_characters_to_the_add_table(self):
        if not self.special_keys_list.GetCount():
            self.special_keys_list.InsertItems(SPECIAL_CHARACTERS_LIST, 0)

#-------------------------------------------------------------------------------
    def add_special_key_to_the_sequence(self, event):
        self.add_item_to_the_sequence_box(SPECIAL_CHARACTERS_LIST[self.special_keys_list.GetSelection()])

#-------------------------------------------------------------------------------
    def add_plus_to_sequence(self, event):
        self.add_item_to_the_sequence_box('+')

#-------------------------------------------------------------------------------
    def add_item_to_the_sequence_box(self, item):
        self.sequence_text_control.AppendText(item)

#-------------------------------------------------------------------------------
    def add_options_to_shortcut_list(self):
        if self.shortcuts_choices.IsEmpty():
            for shortcut in SHORTCUT_OPTIONS:
                self.shortcuts_choices.Append(shortcut)

#-------------------------------------------------------------------------------
    def check_sequence_input(self, event):
        self.__shortcuts_user.set_shortcut_sequence(self.sequence_text_control.GetValue())
        self.check_if_sequence_is_in_protocol()

#-------------------------------------------------------------------------------
    def check_if_sequence_is_in_protocol(self):
        self.__input_status['sequence'] = True
        sequence = self.sequence_text_control.GetValue().split('+')
        if not ''.join(sequence):
            self.__input_status['sequence'] = False
        elif len(sequence) > 6:
            self.__input_status['sequence'] = False
        else:
            for sequence_entry in sequence:
                if len(sequence_entry) > 1:
                    self.check_sequence_special_keys(sequence_entry)

#-------------------------------------------------------------------------------
    def check_sequence_special_keys(self, sequence_entry):
        if sequence_entry.lower() not in SPECIAL_CHARACTERS_LIST:
            self.__input_status['sequence'] = False
        else:
            self.__input_status['sequence'] = True

#-------------------------------------------------------------------------------
    def open_error_dialog(self, error):
        root = Tk()
        root.withdraw()
        tkMessageBox.showerror("Error", error)

#===============================================================================
    def show_current_shortcuts_menu(self, event):
        self.show_current_shortcut_panel()
        self.change_shortcut_grid_labels()
        self.add_shortcuts_to_shortcut_grid()
        self.add_options_to_delete_list()

#-------------------------------------------------------------------------------
    def show_current_shortcut_panel(self):
        self.main_panel.Hide()
        self.new_shortcut_panel.Hide()
        self.current_shortcuts_panel.Show()
        self.current_shortcuts_panel.GetSizer().Layout()
        self.current_shortcuts_panel.GetParent().Layout()

#-------------------------------------------------------------------------------
    def change_shortcut_grid_labels(self):
        for key in SHORTCUT_GRID_LABELS:
            self.computer_shortcuts_grid.SetColLabelValue(key, SHORTCUT_GRID_LABELS[key])

#-------------------------------------------------------------------------------
    def add_shortcuts_to_shortcut_grid(self):
        print self.__shortcuts_user.get_current_shortcuts()
        row = 0
        for key in self.__shortcuts_user.get_current_shortcuts():
            col = 0
            if self.__shortcuts_user.get_current_shortcuts()[key]:
                for file_name in self.__shortcuts_user.get_current_shortcuts()[key]:
                    self.computer_shortcuts_grid.SetCellValue(row, col, key)
                    col += 1
                    argument = self.__shortcuts_user.get_current_shortcuts()[key][file_name][0]
                    self.computer_shortcuts_grid.SetCellValue(row, col, argument)
                    col += 1
                    sequence = '+'.join(self.__shortcuts_user.get_current_shortcuts()[key][file_name][1])
                    self.computer_shortcuts_grid.SetCellValue(row, col, sequence)
                    row += 1
                    col = 0
        self.__row_selection_number = row

#-------------------------------------------------------------------------------
    def add_options_to_delete_list(self):
        self.delete_number_choice.Clear()
        if self.__row_selection_number != 0:
            for number in range(self.__row_selection_number):
                self.delete_number_choice.Append(str(number + 1))

#-------------------------------------------------------------------------------
    def select_shortcut_to_delete(self, event):
        print self.__row_selection_number
        action = self.computer_shortcuts_grid.GetCellValue(self.delete_number_choice.GetSelection(), 0)
        sequence = self.computer_shortcuts_grid.GetCellValue(self.delete_number_choice.GetSelection(), 2)
        sequence = sequence.split('+')
        for file_name in self.__shortcuts_user.get_current_shortcuts()[action]:
            if self.__shortcuts_user.get_current_shortcuts()[action][file_name][1] == sequence:
                self.__selected_file_name_to_delete['file name'] = file_name
                self.__selected_file_name_to_delete['action'] = action
                print self.__selected_file_name_to_delete

        print sequence, action

#-------------------------------------------------------------------------------
    def clear_shortcuts_grid(self):
        self.computer_shortcuts_grid.ClearGrid()

#-------------------------------------------------------------------------------
    def delete_a_shortcut_from_the_grid(self, event):
        self.check_if_row_number_to_delete_was_selected()
        print self.__input_status['row number to delete']
        if self.__input_status['row number to delete']:
            self.__shortcuts_user.delete_shortcut(self.__selected_file_name_to_delete['action'], self.__selected_file_name_to_delete['file name'])
            self.clear_shortcuts_grid()
            self.add_shortcuts_to_shortcut_grid()
            self.add_options_to_delete_list()
            self.__shortcuts_user.save_user_activity()
            self.__input_status['row number to delete'] = False
        else:
            self.open_error_dialog(DELETE_BUTTON_ERROR)

#-------------------------------------------------------------------------------
    def check_if_row_number_to_delete_was_selected(self):
        if self.delete_number_choice.GetSelection() != -1:
            self.__input_status['row number to delete'] = True

#===============================================================================
    def go_to_home_panel(self, event):
        self.main_panel.Show()
        self.current_shortcuts_panel.Hide()
        self.new_shortcut_panel.Hide()

    def update_user_data(self, event):
        self.__shortcuts_user.save_user_activity()
        self.Destroy()


def main():
    app = wx.App(False)

    #create an object of CalcFrame
    frame = Main(None)
    #show the frame
    frame.Show(True)
    #start the applications
    app.MainLoop()

if __name__ == '__main__':
    main()