# -*- coding: utf-8 -*-

from shortcuts import ShortCuts, GetArgument
import wx
import shortcut_menu_wx_skeleton
import os
from Tkinter import *
import tkMessageBox
from new_computer_class import Server, Client
import pickle
import subprocess
#import threading

SHORTCUTS_USER_DATA_FILE_NAME = 'user_data.json'
ADDED_COMPUTERS_DATA_FILE_NAME = 'added_computers_data.json'
SPECIAL_CHARACTERS_LIST = ['windows', 'alt', 'control', 'shift', 'space', 'backspace', 'enter']
SHORTCUT_OPTIONS = ['open folder', 'open url', 'open file', 'open cmd', 'open settings']
SHORTCUT_GRID_LABELS = {0: 'Action', 1: 'Argument', 2: 'Sequence'}
CHOOSE_COMPUTER_ERROR = 'Choose a computer'
REMOTE_SERVER_CONNECTION_ERROR = 'There was a problem with the connection'
SEQUENCE_ERROR = 'Not a legal sequence'
ACTION_ERROR = 'Choose a action'
DELETE_BUTTON_ERROR = 'Row number was not selected'
WINDOWS_KEY_REPRESENTATION = 'LWin'
CURRENT_SHORTCUTS_TEMPLATE = {'open folder': {}, 'open url': {}, 'open file': {}, 'open cmd': {}, 'open settings': {}}
FILES_ENDING_COUNTER_TEMPLATE = {'folder': 0, 'url': 0, 'file': 0, 'cmd': 0, 'settings': 0}
REMOTE_URL_ARGUMENT_REMARK = ' Please enter full url  example: www.google.com'

class Main(shortcut_menu_wx_skeleton.MainFrame):
    #constructor
    def __init__(self, parent):
        shortcut_menu_wx_skeleton.MainFrame.__init__(self, parent)
        self.__shortcuts_user = ShortCuts()
        self.__client = Client()
        self.__row_selection_number = 0
        self.__saved_computer_list = {'My Computer': [[], CURRENT_SHORTCUTS_TEMPLATE, FILES_ENDING_COUNTER_TEMPLATE]}
        self.__computer_list_for_getting_user_selection = []
        self.__computer_name_list = []
        self.__selected_computer_name = ''
        self.__argument_functions = GetArgument()
        self.__remote_computer_argument = ''
        self.__current_shortcuts_selected_computer_name = 'My Computer'
        self.__selected_file_name_to_delete = {'file name': '', 'action': ''}
        self.__input_status = {'sequence': False, 'action': False, 'row number to delete': False, 'new computer': False, 'remote argument': False}
        self.__shortcut_argument_activation = {'open folder': self.open_remote_folder, 'open url': self.open_remote_url, 'open file': self.open_remote_file, 'open cmd': self.no_needed_argument, 'open settings': self.no_needed_argument}
        self.check_if_first_time()

#-------------------------------------------------------------------------------
    def check_if_first_time(self):
        if os.path.isfile(ADDED_COMPUTERS_DATA_FILE_NAME):
            self.get_added_computers_previous_activity()

#-------------------------------------------------------------------------------
    def add_new_shortcut_menu(self, event):
        self.show_new_shortcut_panel()
        self.add_special_characters_to_the_add_table()
        self.add_options_to_shortcut_list()
        self.add_computers_to_choose_computer_list()

#-------------------------------------------------------------------------------
    def show_new_shortcut_panel(self):
        self.new_shortcut_panel.Show()
        self.main_panel.Hide()
        self.current_shortcuts_panel.Hide()
        self.add_new_computer_panel.Hide()
        self.new_shortcut_panel.GetSizer().Layout()
        self.new_shortcut_panel.GetParent().Layout()

#-------------------------------------------------------------------------------
    def add_new_shortcut_to_the_list(self, event):
        print '+'.join(self.__shortcuts_user.get_shortcut_sequence()), '---sequence---'
        print self.__selected_computer_name, '---computer---'

        if self.__input_status['sequence'] and self.__input_status['action'] and self.__selected_computer_name:
            if self.check_what_computer_was_chosen():
                self.__shortcuts_user.write_new_shortcut(self.__selected_computer_name, self.__saved_computer_list[self.__selected_computer_name][1], self.__saved_computer_list[self.__selected_computer_name][2], self.__remote_computer_argument)
                self.__remote_computer_argument = ''
                self.__saved_computer_list[self.__selected_computer_name][1] = self.__shortcuts_user.get_current_shortcuts()
                self.__saved_computer_list[self.__selected_computer_name][2] = self.__shortcuts_user.get_file_ending_counter()
                self.save_added_computers_previous_activity()

        elif not self.__input_status['sequence'] and self.__input_status['action']:
            self.open_error_dialog(SEQUENCE_ERROR)

        elif self.__input_status['sequence'] and not self.__input_status['action'] or not self.__input_status['sequence'] and not self.__input_status['action']:
            self.open_error_dialog(ACTION_ERROR)

        elif not self.__selected_computer_name:
            self.open_error_dialog(CHOOSE_COMPUTER_ERROR)

#-------------------------------------------------------------------------------
    def update_my_computer_data(self):
        self.__saved_computer_list['My Computer'][1] = self.__shortcuts_user.get_current_shortcuts()
        self.save_added_computers_previous_activity()

#-------------------------------------------------------------------------------
    def check_what_computer_was_chosen(self):
        if self.__selected_computer_name == 'My Computer':
            self.__input_status['remote argument'] = False
            return True
        else:
            return self.connect_to_server_and_pass_arguments()


#-------------------------------------------------------------------------------
    def connect_to_server_and_pass_arguments(self):
        if self.__client.check_if_remote_server_is_on(self.__saved_computer_list[self.__selected_computer_name][0][0], 0):
            self.__input_status['remote argument'] = True
            self.get_argument_from_server()
            if self.__argument_functions.get_argument():
                self.__client.send_request_to_the_server(self.__shortcuts_user.get_users_choice(), self.__remote_computer_argument.split('$$')[1], '+'.join(self.__shortcuts_user.get_shortcut_sequence()))
                print self.__client.receive_information_from_the_server()
            self.__client.close_client()
            self.__client = Client()
            return True

        else:
            self.open_error_dialog(REMOTE_SERVER_CONNECTION_ERROR)
            self.__client.close_client()
            self.__client = Client()
            return False

#-------------------------------------------------------------------------------
    def get_argument_from_server(self):
            self.__shortcut_argument_activation[self.__shortcuts_user.get_users_choice()]()

#-------------------------------------------------------------------------------
    def open_remote_folder(self):
        self.__argument_functions.ask_text_from_user(self.__shortcuts_user.get_users_choice(), 'enter path to folder')
        self.set_remote_computer_argument()

    def open_remote_url(self):
        self.__argument_functions.ask_text_from_user(self.__shortcuts_user.get_users_choice(), REMOTE_URL_ARGUMENT_REMARK)
        if self.__argument_functions.get_argument():
            if self.__argument_functions.get_argument().split('.')[0] != 'www':
                self.__argument_functions.set_argument('www.'+self.__argument_functions.get_argument())
        self.set_remote_computer_argument()

    def open_remote_file(self):
        self.__argument_functions.ask_text_from_user(self.__shortcuts_user.get_users_choice(), 'enter path to file')
        self.set_remote_computer_argument()

    def no_needed_argument(self):
        print 'no argument needed'
        self.__argument_functions.set_argument('??')
        self.set_remote_computer_argument()

    def set_remote_computer_argument(self):
        print self.__argument_functions.get_argument()
        self.__remote_computer_argument = self.__shortcuts_user.get_users_choice()+'$$'+self.__argument_functions.get_argument()+'$$'+self.__saved_computer_list[self.__selected_computer_name][0][1]

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
        if SPECIAL_CHARACTERS_LIST[self.special_keys_list.GetSelection()] == 'windows':
            self.add_item_to_the_sequence_box(WINDOWS_KEY_REPRESENTATION)
        else:
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

        elif self.sequence_text_control.GetValue()[-1] == '+':
            self.__input_status['sequence'] = False

        else:
            for sequence_entry in sequence:
                if len(sequence_entry) > 1:
                    self.check_sequence_special_keys(sequence_entry)

#-------------------------------------------------------------------------------
    def check_sequence_special_keys(self, sequence_entry):
        if sequence_entry == WINDOWS_KEY_REPRESENTATION:
            self.__input_status['sequence'] = True
        elif sequence_entry.lower() not in SPECIAL_CHARACTERS_LIST:
            self.__input_status['sequence'] = False
        else:
            self.__input_status['sequence'] = True

#-------------------------------------------------------------------------------
    def open_error_dialog(self, error):
        root = Tk()
        root.withdraw()
        tkMessageBox.showerror("Error", error)

#-------------------------------------------------------------------------------
    def add_computers_to_choose_computer_list(self):
        self.__computer_name_list = [key for key in self.__saved_computer_list.keys()]

        if self.choose_computer_for_action.IsEmpty() or self.__input_status['new computer']:
            self.choose_computer_for_action.Clear()
            for computer in self.__computer_name_list:
                self.choose_computer_for_action.Append(computer)
            self.__input_status['new computer'] = False

#-------------------------------------------------------------------------------
    def choose_a_computer_for_action(self, event):
        self.__selected_computer_name = self.__computer_name_list[self.choose_computer_for_action.GetSelection()]

#===============================================================================
    def show_current_shortcuts_menu(self, event):
        self.show_current_shortcut_panel()
        self.change_shortcut_grid_labels()
        self.add_shortcuts_to_shortcut_grid()
        self.add_options_to_delete_list()
        self.add_computers_to_computer_choice()

#-------------------------------------------------------------------------------
    def show_current_shortcut_panel(self):
        self.main_panel.Hide()
        self.new_shortcut_panel.Hide()
        self.add_new_computer_panel.Hide()
        self.current_shortcuts_panel.Show()
        self.current_shortcuts_panel.GetSizer().Layout()
        self.current_shortcuts_panel.GetParent().Layout()

#-------------------------------------------------------------------------------
    def change_shortcut_grid_labels(self):
        for key in SHORTCUT_GRID_LABELS:
            self.computer_shortcuts_grid.SetColLabelValue(key, SHORTCUT_GRID_LABELS[key])

#-------------------------------------------------------------------------------
    def add_shortcuts_to_shortcut_grid(self):
        print self.__saved_computer_list
        row = 0
        for action in self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1]:
            col = 0
            if self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1][action]:
                for file_name in self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1][action]:
                    self.computer_shortcuts_grid.SetCellValue(row, col, action)
                    col += 1
                    argument = self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1][action][file_name][0]
                    if action == 'open file':
                        argument = argument.split('/')[-1]
                    self.computer_shortcuts_grid.SetCellValue(row, col, argument)
                    col += 1
                    sequence = '+'.join(self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1][action][file_name][1])
                    self.computer_shortcuts_grid.SetCellValue(row, col, sequence)
                    row += 1
                    col = 0
        self.__row_selection_number = row

        self.add_options_to_delete_list()

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
        for file_name in self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1][action]:
            if self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1][action][file_name][1] == sequence:
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
            self.__shortcuts_user.delete_shortcut(self.__selected_file_name_to_delete['action'], self.__selected_file_name_to_delete['file name'], self.__saved_computer_list[self.__current_shortcuts_selected_computer_name][1])
            self.save_added_computers_previous_activity()
            self.clear_shortcuts_grid()
            self.add_shortcuts_to_shortcut_grid()
            self.add_options_to_delete_list()
            self.__input_status['row number to delete'] = False
        else:
            self.open_error_dialog(DELETE_BUTTON_ERROR)

#-------------------------------------------------------------------------------
    def get_computer_to_show_shortcuts(self, event):
        self.__current_shortcuts_selected_computer_name = self.__computer_name_list[self.computer_choice.GetSelection()]
        print self.__current_shortcuts_selected_computer_name
        self.clear_shortcuts_grid()
        self.add_shortcuts_to_shortcut_grid()

#-------------------------------------------------------------------------------
    def add_computers_to_computer_choice(self):
        self.__computer_name_list = [key for key in self.__saved_computer_list.keys()]

        if self.computer_choice.IsEmpty() or self.__input_status['new computer']:
            self.computer_choice.Clear()
            for computer in self.__computer_name_list:
                self.computer_choice.Append(computer)
            self.__input_status['new computer'] = False

#-------------------------------------------------------------------------------
    def check_if_row_number_to_delete_was_selected(self):
        if self.delete_number_choice.GetSelection() != -1:
            self.__input_status['row number to delete'] = True

#===============================================================================
    def show_add_new_computer_menu(self, event):
        self.show_add_new_computer_panel()
        self.show_loading_screen()
#-------------------------------------------------------------------------------

    def show_loading_screen(self):
        loading_screen = subprocess.Popen(['python', 'loading_screen.py'])
        self.__client.find_computers_in_the_network()
        self.add_computer_information_to_the_add_table()
        loading_screen.terminate()

    def show_add_new_computer_panel(self):
        self.new_shortcut_panel.Hide()
        self.main_panel.Hide()
        self.current_shortcuts_panel.Hide()
        self.add_new_computer_panel.Show()
        self.add_new_computer_panel.GetSizer().Layout()
        self.add_new_computer_panel.GetParent().Layout()

#-------------------------------------------------------------------------------
    def add_computer_information_to_the_add_table(self):
        self.__computer_list_for_getting_user_selection = []
        for computer_name in self.__client.get_computer_information():
            self.__computer_list_for_getting_user_selection.append([computer_name, self.__client.get_computer_information()[computer_name][0]])

        self.add_new_computer_list_control.DeleteAllItems()
        for computer in self.__computer_list_for_getting_user_selection:
            self.add_new_computer_list_control.AppendItem(computer)

#-------------------------------------------------------------------------------
    def add_new_computer_to_the_list(self, event):
        self.__saved_computer_list[self.__selected_computer_name] = [self.__client.get_computer_information()[self.__selected_computer_name], CURRENT_SHORTCUTS_TEMPLATE, FILES_ENDING_COUNTER_TEMPLATE]
        self.save_added_computers_previous_activity()
        self.__input_status['new computer'] = True  # update the new computer status so the choice list will update
        print self.__saved_computer_list

#-------------------------------------------------------------------------------
    def choose_computer_name_and_ip(self, event):
        if self.__computer_list_for_getting_user_selection[self.add_new_computer_list_control.GetSelectedRow()][0]:
            self.__selected_computer_name = self.__computer_list_for_getting_user_selection[self.add_new_computer_list_control.GetSelectedRow()][0].title()

        print self.__selected_computer_name

#-------------------------------------------------------------------------------
    def save_added_computers_previous_activity(self):
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'w')
        pickle.dump(self.__saved_computer_list, json_save_file)
        json_save_file.close()

#-------------------------------------------------------------------------------
    def get_added_computers_previous_activity(self):
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'r')
        self.__saved_computer_list = pickle.load(json_save_file)

#===============================================================================
    def go_to_home_panel(self, event):
        self.main_panel.Show()
        self.current_shortcuts_panel.Hide()
        self.new_shortcut_panel.Hide()
        self.add_new_computer_panel.Hide()

    def update_user_data(self, event):
        # self.__shortcuts_user.save_user_activity()
        self.save_added_computers_previous_activity()
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