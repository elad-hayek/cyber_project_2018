# -*- coding: utf-8 -*-
"""
Description:    activates the wx program and controls every action the user
                does. from creating shortcuts to deleting shortcuts and adding
                shortcuts remotely.

name:           Elad Hayek
date:           2.2.18
file name:      user_menu.py
"""

from shortcuts import ShortCuts, GetArgument
import wx
import shortcut_menu_wx_skeleton
import os
from Tkinter import *
import tkMessageBox
from new_computer_class import Client
import pickle
from subprocess import *
from create_server_bat_and_vbs_files import *
# import threading


ADDED_COMPUTERS_DATA_FILE_NAME = 'added_computers_data.json'
SPECIAL_CHARACTERS_LIST = ['windows', 'alt', 'control', 'shift', 'space',
                           'backspace', 'enter']
SHORTCUT_OPTIONS = ['open folder', 'open url', 'open file', 'open cmd',
                    'open settings', 'shutdown', 'restart']
SHORTCUT_GRID_LABELS = {0: 'Action', 1: 'Argument', 2: 'Sequence'}
CHOOSE_COMPUTER_ERROR = 'Choose a computer'
REMOTE_SERVER_CONNECTION_ERROR = 'There was a problem with the connection'
SEQUENCE_ERROR = 'Not a legal sequence'
ACTION_ERROR = 'Choose a action'
DELETE_BUTTON_ERROR = 'Row number was not selected'
COMPUTER_ALREADY_ADDED_ERROR = 'the computer was already added'
NAME_IS_ALREADY_TAKEN_ERROR = 'The Name Is Already Used'
WINDOWS_KEY_REPRESENTATION = 'LWin'
CURRENT_SHORTCUTS_TEMPLATE = {'open folder': {}, 'open url': {},
                              'open file': {}, 'open cmd': {},
                              'open settings': {}, 'shutdown': {},
                              'restart': {}}
FILES_ENDING_COUNTER_TEMPLATE = {'folder': 0, 'url': 0, 'file': 0, 'cmd': 0,
                                 'settings': 0, 'shutdown': 0, 'restart': 0}
REMOTE_URL_ARGUMENT_REMARK = ' Please enter full url  example: www.google.com'
REMOTE_FOLDER_ARGUMENT_REMARK = 'Enter path to folder'
REMOTE_FILE_ARGUMENT_REMARK = 'Enter path to file'
DELETE_ALL_SHORTCUTS_CONFORMATION_MESSAGE =\
    'Are You Sure You Want To Delete All'
DELETE_COMPUTER_INFORMATION_CONFORMATION_MESSAGE =\
    'Are You Sure You Want To Remove The Computer\nAll Of Its Data Will Be' \
    ' Erased'
COMPUTER_NAME_CONFORMATION_FROM_USER_MESSAGE =\
    'Are You Sure\nThe Current Name Will Be Saved'


class Main(shortcut_menu_wx_skeleton.MainFrame):
    def __init__(self, parent):
        """
        constructs the wx gui from the wx skeleton

        :arg parent = the shortcut_menu_wx_skeleton.MainFrame class to inherit
        :type parent = class
        """
        shortcut_menu_wx_skeleton.MainFrame.__init__(self, parent)
        self.__open_servers = Create_bat_and_vbs_files()
        self.__shortcuts_user = ShortCuts()
        self.__client = Client()
        self.__row_selection_number = 0
        self.__saved_computer_list = {
            'My Computer': [
                [], CURRENT_SHORTCUTS_TEMPLATE, FILES_ENDING_COUNTER_TEMPLATE]}
        self.__add_computer_list_for_getting_user_selection = []
        self.__remove_computer_list_for_getting_user_selection = []
        self.__computer_name_list = []
        self.__computer_mac_list = []
        self.__selected_computer_name = ''
        self.__selected_computer_name_to_add = ''
        self.__selected_computer_name_to_remove = ''
        self.__argument_functions = GetArgument()
        self.__remote_computer_argument = ''
        self.__current_shortcuts_selected_computer_name = 'My Computer'
        self.__selected_file_name_to_delete = {'file name': '', 'action': ''}
        self.__input_status = {
            'sequence': False, 'action': False, 'row number to delete': False,
            'computers status for current shortcuts': False,
            'computer status for write shortcuts': False,
            'remote argument': False, 'delete all': False,
            'remove_computer': False}
        self.__shortcut_argument_activation = {
            'open folder': self.open_remote_folder,
            'open url': self.open_remote_url,
            'open file': self.open_remote_file,
            'open cmd': self.no_needed_argument,
            'open settings': self.no_needed_argument,
            'shutdown': self.no_needed_argument,
            'restart': self.no_needed_argument}
        self.check_if_first_time()

# -----------------------------------------------------------------------------
    def check_if_first_time(self):
        """
        checks if the user activates the program fro the first time and if so
        creates a file to save the data.
        """
        if os.path.isfile(ADDED_COMPUTERS_DATA_FILE_NAME):
            self.get_added_computers_previous_activity()
        else:
            with open(ADDED_COMPUTERS_DATA_FILE_NAME, 'w') as f:
                pass

# -----------------------------------------------------------------------------
    def add_new_shortcut_menu(self, event):
        """
        shows the add new shortcuts panel in the wx frame and adds all
        important information.

        :arg event = the event from clicking the add new shortcuts panel button
        :type event = wx._core.CommandEvent
        """
        self.show_new_shortcut_panel()
        self.add_special_characters_to_the_add_table()
        self.add_options_to_shortcut_list()
        self.add_computers_to_choose_computer_list()

# -----------------------------------------------------------------------------
    def show_new_shortcut_panel(self):
        """
        shows the add new shortcut panel and makes it fit the the frame size.
        """
        self.new_shortcut_panel.Show()
        self.main_panel.Hide()
        self.current_shortcuts_panel.Hide()
        self.manage_computers_panel.Hide()
        self.new_shortcut_panel.GetSizer().Layout()
        self.new_shortcut_panel.GetParent().Layout()

# -----------------------------------------------------------------------------
    def add_new_shortcut_to_the_list(self, event):
        """
        creates new shortcuts and checks for errors.

        :arg event = the event from clicking the add new shortcut button
        :type event = wx._core.CommandEvent
        """
        print '+'.join(self.__shortcuts_user.get_shortcut_sequence()),\
            '---sequence---'
        print self.__selected_computer_name, '---computer---'

        if self.__input_status['sequence'] and self.__input_status['action'] \
                and self.__selected_computer_name:
            if self.check_what_computer_was_chosen():
                self.__shortcuts_user.write_new_shortcut(
                    self.__selected_computer_name, self.__saved_computer_list[
                        self.__selected_computer_name][1],
                    self.__saved_computer_list[
                        self.__selected_computer_name][2],
                    self.__remote_computer_argument)
                self.__remote_computer_argument = ''
                self.__saved_computer_list[self.__selected_computer_name][1] =\
                    self.__shortcuts_user.get_current_shortcuts()
                self.__saved_computer_list[self.__selected_computer_name][2] =\
                    self.__shortcuts_user.get_file_ending_counter()
                self.save_added_computers_previous_activity()

        elif not self.__input_status['sequence'] \
                and self.__input_status['action']:
            self.open_error_dialog(SEQUENCE_ERROR)

        elif self.__input_status['sequence'] \
                and not self.__input_status['action'] \
                or not self.__input_status['sequence'] \
                and not self.__input_status['action']:
            self.open_error_dialog(ACTION_ERROR)

        elif not self.__selected_computer_name:
            self.open_error_dialog(CHOOSE_COMPUTER_ERROR)

# -----------------------------------------------------------------------------
    def update_my_computer_data(self):
        """
        updates my computer saved data after adding or removing data and saves
        it to the data file.
        """
        self.__saved_computer_list['My Computer'][1] =\
            self.__shortcuts_user.get_current_shortcuts()
        self.save_added_computers_previous_activity()

# -----------------------------------------------------------------------------
    def check_what_computer_was_chosen(self):
        """
        checks what computer was chosen by the user and if it wasn't my
        computer its returns a remote shortcut configuration.
        """
        if self.__selected_computer_name == 'My Computer':
            self.__input_status['remote argument'] = False
            return True
        else:
            return self.connect_to_server_and_pass_arguments()

# -----------------------------------------------------------------------------
    def connect_to_server_and_pass_arguments(self):
        """
        connects the remote server and passes the shortcut information for the
        creation of a remote shortcut.
        """
        arp_question = Popen(['python', 'get_ip_and_mac.py',
                              self.__saved_computer_list[
                                  self.__selected_computer_name][0][1]],
                             stdout=PIPE)
        result = arp_question.communicate()[0]
        ip = result.strip()
        print ip
        if self.__client.check_if_remote_server_is_on(ip, 0):
            self.__input_status['remote argument'] = True
            self.get_argument_from_server()
            if self.__argument_functions.get_argument():
                self.__client.send_request_to_the_server(
                    self.__shortcuts_user.get_users_choice(),
                    self.__remote_computer_argument.split('$$')[1], '+'.join(
                        self.__shortcuts_user.get_shortcut_sequence()))
                if self.__client.receive_information_from_the_server() \
                        == 'not found':
                    self.open_error_dialog('Path not found')
                    self.__client.close_client()
                    self.__client = Client()
                    return False
            self.__client.close_client()
            self.__client = Client()
            return True

        else:
            self.open_error_dialog(REMOTE_SERVER_CONNECTION_ERROR)
            self.__client.close_client()
            self.__client = Client()
            return False

# -----------------------------------------------------------------------------
    def get_argument_from_server(self):
        """
        gets the argument for the remote shortcut according the the action the
        user chose.
        """
        self.__shortcut_argument_activation[
            self.__shortcuts_user.get_users_choice()]()

# -----------------------------------------------------------------------------
    def open_remote_folder(self):
        """
        opens a text box with a remote folder query for the user
        """
        self.__argument_functions.ask_text_from_user(
            self.__shortcuts_user.get_users_choice(),
            REMOTE_FOLDER_ARGUMENT_REMARK)
        self.set_remote_computer_argument()

# -----------------------------------------------------------------------------
    def open_remote_url(self):
        """
        opens a text box with a remote url query for the user
        """
        self.__argument_functions.ask_text_from_user(
            self.__shortcuts_user.get_users_choice(),
            REMOTE_URL_ARGUMENT_REMARK)
        if self.__argument_functions.get_argument():
            # the url must start with www
            if self.__argument_functions.get_argument().split('.')[0] != 'www':
                    self.__argument_functions.set_argument(
                        'www.'+self.__argument_functions.get_argument())
        self.set_remote_computer_argument()

# -----------------------------------------------------------------------------
    def open_remote_file(self):
        """
        opens a text box with a remote file query for the user
        """
        self.__argument_functions.ask_text_from_user(
            self.__shortcuts_user.get_users_choice(),
            REMOTE_FILE_ARGUMENT_REMARK)
        self.set_remote_computer_argument()

# -----------------------------------------------------------------------------
    def no_needed_argument(self):
        """
        sends a ;; when no argument needed for the action
        """
        print 'no argument needed'
# sets the argument to ;; because the hot key script will think its a remark
        self.__argument_functions.set_argument(';;')
        self.set_remote_computer_argument()

# -----------------------------------------------------------------------------
    def set_remote_computer_argument(self):
        """
        creates the remote shortcut information to be sent to the remote server
        """
        print self.__argument_functions.get_argument()
        self.__remote_computer_argument =\
            self.__shortcuts_user.get_users_choice(
            )+'$$'+self.__argument_functions.get_argument(
            )+'$$'+self.__saved_computer_list[
                self.__selected_computer_name][0][1]

# -----------------------------------------------------------------------------
    def save_user_choice(self, event):
        """
        saves the user action choice from the list of actions

        :arg event = the event from clicking the actions list in add new
        shortcut panel
        :type event = wx._core.CommandEvent
        """
        print SHORTCUT_OPTIONS[self.shortcuts_choices.GetSelection()],\
            '---action---'
        self.__shortcuts_user.set_users_choice(SHORTCUT_OPTIONS[
            self.shortcuts_choices.GetSelection()])
        self.__input_status['action'] = True

# -----------------------------------------------------------------------------
    def add_special_characters_to_the_add_table(self):
        """
        adds the special characters (enter, space etc) to the list.
        """
        if not self.special_keys_list.GetCount():
            self.special_keys_list.InsertItems(SPECIAL_CHARACTERS_LIST, 0)

# -----------------------------------------------------------------------------
    def add_special_key_to_the_sequence(self, event):
        """
        adds a special key to the user sequence from the list

        :arg event = the event from clicking a special character from the list
        :type event = wx._core.CommandEvent
        """
        if SPECIAL_CHARACTERS_LIST[
                self.special_keys_list.GetSelection()] == 'windows':
            self.add_item_to_the_sequence_box(WINDOWS_KEY_REPRESENTATION)
        else:
            self.add_item_to_the_sequence_box(
                SPECIAL_CHARACTERS_LIST[self.special_keys_list.GetSelection()])

# -----------------------------------------------------------------------------
    def add_plus_to_sequence(self, event):
        """
        adds a + to the sequence

        :arg event = the event from clicking the + button
        :type event = wx._core.CommandEvent
        """
        self.add_item_to_the_sequence_box('+')

# -----------------------------------------------------------------------------
    def add_item_to_the_sequence_box(self, item):
        """
        adds a key to the sequence box

        :arg item = the wanted key
        :type item = string
        """
        self.sequence_text_control.AppendText(item)

# -----------------------------------------------------------------------------
    def add_options_to_shortcut_list(self):
        """
        adds the actions for the actions list in the add new shortcut panel
        """
        if self.shortcuts_choices.IsEmpty():
            for shortcut in SHORTCUT_OPTIONS:
                self.shortcuts_choices.Append(shortcut)

# -----------------------------------------------------------------------------
    def check_sequence_input(self, event):
        """
        activates the check sequence protocol when a new kry is added to the
        sequence box.

        :arg event = the event from adding a key to the sequence box
        :type event = wx._core.CommandEvent
        """
        self.__shortcuts_user.set_shortcut_sequence(
            self.sequence_text_control.GetValue())
        self.check_if_sequence_is_in_protocol()

# -----------------------------------------------------------------------------
    def check_if_sequence_is_in_protocol(self):
        """
        checks if the sequence is up to protocol and change the sequence flag
        accordingly
        """
        self.__input_status['sequence'] = True
        sequence = self.sequence_text_control.GetValue().split('+')
        if not ''.join(sequence):
            self.__input_status['sequence'] = False
        elif len(sequence) > 6:
            self.__input_status['sequence'] = False

        elif self.sequence_text_control.GetValue()[-1] == '+':
            self.__input_status['sequence'] = False

        elif '' in sequence:
            self.__input_status['sequence'] = False

        else:
            for sequence_entry in sequence:
                if len(sequence_entry) > 1:
                    self.check_sequence_special_keys(sequence_entry)
        try:
            self.sequence_text_control.GetValue().encode(
                encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            self.__input_status['sequence'] = False

# -----------------------------------------------------------------------------
    def check_sequence_special_keys(self, sequence_entry):
        """
        checks for special characters in the sequence box
        """
        if sequence_entry == WINDOWS_KEY_REPRESENTATION:
            self.__input_status['sequence'] = True
        elif sequence_entry.lower() not in SPECIAL_CHARACTERS_LIST:
            self.__input_status['sequence'] = False
        else:
            self.__input_status['sequence'] = True

# -----------------------------------------------------------------------------
    def open_error_dialog(self, error):
        """
        opens an error message box

        :arg error = the error message the user gets
        :type error = string
        """
        root = Tk()
        root.withdraw()
        tkMessageBox.showerror("Error", error)

    def get_saved_computers_name_list(self):
        self.__computer_name_list = [
            key for key in self.__saved_computer_list.keys()]

# -----------------------------------------------------------------------------
    def add_computers_to_choose_computer_list(self):
        """
        adds computer names to the computer name list in add new shortcut panel
        """
        self.get_saved_computers_name_list()

        if self.choose_computer_for_action.IsEmpty() \
                or self.__input_status['computer status for write shortcuts']:
            self.choose_computer_for_action.Clear()
            for computer in self.__computer_name_list:
                self.choose_computer_for_action.Append(computer)
            self.__input_status['computer status for write shortcuts'] = False

# -----------------------------------------------------------------------------
    def choose_a_computer_for_action(self, event):
        """
        sets the chosen computer by the user

        :arg event = the event from clicking a computer name fom the list
        :type event = wx._core.CommandEvent
        """
        self.__selected_computer_name = self.__computer_name_list[
            self.choose_computer_for_action.GetSelection()]

# =============================================================================
    def show_current_shortcuts_menu(self, event):
        """
        shows the current shortcuts panel and adds all important
        information.

        :arg event = the event from clicking the current shortcuts panel button
        :type event = wx._core.CommandEvent
        """
        self.show_current_shortcut_panel()
        self.change_shortcut_grid_labels()
        self.add_shortcuts_to_shortcut_grid()
        self.add_options_to_delete_list()
        self.add_computers_to_computer_choice()

# -----------------------------------------------------------------------------
    def show_current_shortcut_panel(self):
        """
        shows the current shortcuts panel and makes it fit the frame size
        """
        self.main_panel.Hide()
        self.new_shortcut_panel.Hide()
        self.manage_computers_panel.Hide()
        self.current_shortcuts_panel.Show()
        self.current_shortcuts_panel.GetSizer().Layout()
        self.current_shortcuts_panel.GetParent().Layout()

# -----------------------------------------------------------------------------
    def change_shortcut_grid_labels(self):
        """
        sets the shortcut grid labels
        """
        for key in SHORTCUT_GRID_LABELS:
            self.computer_shortcuts_grid.SetColLabelValue(
                key, SHORTCUT_GRID_LABELS[key])

# -----------------------------------------------------------------------------
    def add_shortcuts_to_shortcut_grid(self):
        """
        adds shortcuts to the shortcut grid from the saved data
        """
        self.get_added_computers_previous_activity()
        print self.__saved_computer_list
        row = 0
        for action in self.__saved_computer_list[
                self.__current_shortcuts_selected_computer_name][1]:
            col = 0
            if self.__saved_computer_list[
                    self.__current_shortcuts_selected_computer_name][1][
                        action]:
                for file_name in self.__saved_computer_list[
                    self.__current_shortcuts_selected_computer_name][1][
                        action]:
                    self.computer_shortcuts_grid.SetCellValue(row, col, action)
                    col += 1
                    argument = self.__saved_computer_list[
                        self.__current_shortcuts_selected_computer_name][1][
                            action][file_name][0]
                    if action == 'open file':
                        argument = argument.split('/')[-1]
                    self.computer_shortcuts_grid.SetCellValue(
                        row, col, argument)
                    col += 1
                    sequence = '+'.join(self.__saved_computer_list[
                        self.__current_shortcuts_selected_computer_name][1][
                            action][file_name][1])
                    self.computer_shortcuts_grid.SetCellValue(
                        row, col, sequence)
                    row += 1
                    col = 0
        self.__row_selection_number = row

        self.add_options_to_delete_list()

# -----------------------------------------------------------------------------
    def add_options_to_delete_list(self):
        """
        adds the numbers the the delete shortcut by number according to the
        shortcuts grid
        """
        self.delete_number_choice.Clear()
        if self.__row_selection_number != 0:
            for number in range(self.__row_selection_number):
                self.delete_number_choice.Append(str(number + 1))

# -----------------------------------------------------------------------------
    def select_shortcut_to_delete(self, event, delete_all_row_number=0):
        """
        selects a shortcut to delete according to the user selected number of
        shortcut or selects all shortcuts fo deletion

        :arg event = the event from clicking the row number selection list
        :type event = wx._core.CommandEvent

        :arg delete_all_row_number = the row number for deletion if the delete
        all button was pressed
        :type = int
        """
        print self.__row_selection_number
        if self.__input_status['delete all']:
            row_number_selected = delete_all_row_number
        else:
            row_number_selected = self.delete_number_choice.GetSelection()
            print row_number_selected

        action = self.computer_shortcuts_grid.GetCellValue(
            row_number_selected, 0)
        argument = self.computer_shortcuts_grid.GetCellValue(
            row_number_selected, 1)
        sequence = self.computer_shortcuts_grid.GetCellValue(
            row_number_selected, 2)

        sequence = sequence.split('+')
        for file_name in self.__saved_computer_list[
                self.__current_shortcuts_selected_computer_name][1][action]:
            if self.__saved_computer_list[
                self.__current_shortcuts_selected_computer_name][1][
                    action][file_name][1] == sequence and \
                    self.__saved_computer_list[
                        self.__current_shortcuts_selected_computer_name][1][
                    action][file_name][0] == argument:
                self.__selected_file_name_to_delete['file name'] = file_name
                self.__selected_file_name_to_delete['action'] = action
                print self.__selected_file_name_to_delete

        print sequence, action

# -----------------------------------------------------------------------------
    def clear_shortcuts_grid(self):
        """
        clears the shortcuts grid
        """
        self.computer_shortcuts_grid.ClearGrid()

# -----------------------------------------------------------------------------
    def delete_a_shortcut_from_the_grid(self, event):
        """
        deletes a shortcut from the grid

        :arg event = the event from clicking the add new shortcuts panel button
        :type event = wx._core.CommandEvent
        """
        self.check_if_row_number_to_delete_was_selected()
        print self.__input_status['row number to delete']
        if self.__input_status['delete all']:
            self.__input_status['row number to delete'] = True
        if self.__input_status['row number to delete']:
            self.__shortcuts_user.delete_shortcut(
                self.__selected_file_name_to_delete['action'],
                self.__selected_file_name_to_delete['file name'],
                self.__saved_computer_list[
                    self.__current_shortcuts_selected_computer_name][1])
            self.save_added_computers_previous_activity()
            self.clear_shortcuts_grid()
            self.add_shortcuts_to_shortcut_grid()
            self.add_options_to_delete_list()
        else:
            self.open_error_dialog(DELETE_BUTTON_ERROR)
        self.__input_status['row number to delete'] = False

# -----------------------------------------------------------------------------
    def confirmation_from_user(self, conformation_title, conformation_message):
        """
        shows a confirm message for the user

        :arg conformation_title = the message's title
        :type conformation_title = string

        :arg conformation_message = the message for the user
        :type conformation_message = string
        """
        root = Tk()
        root.withdraw()
        result = tkMessageBox.askquestion(conformation_title,
                                          conformation_message, icon='warning')
        if result == 'yes':
            return True
        else:
            return False

# -----------------------------------------------------------------------------
    def delete_all_of_the_computer_shortcuts(self, event):
        """
        deletes all of the selected computer shortcuts

        :arg event = the event from clicking the delete all button
        :type event = wx._core.CommandEvent
        """
        if self.__input_status['remove_computer']:
            conformation_result = self.confirmation_from_user(
                'Delete', DELETE_COMPUTER_INFORMATION_CONFORMATION_MESSAGE)
        else:
            conformation_result = self.confirmation_from_user(
                'Delete', DELETE_ALL_SHORTCUTS_CONFORMATION_MESSAGE)
        if conformation_result:
            self.__input_status['delete all'] = True
            for shortcuts_number in range(self.__row_selection_number):
                self.select_shortcut_to_delete('')
                self.delete_a_shortcut_from_the_grid('')

            self.__input_status['delete all'] = False
        return conformation_result

# -----------------------------------------------------------------------------
    def get_computer_to_show_shortcuts(self, event):
        """
        adds shortcuts to the grid according to the user selected computer

        :arg event = the event from clicking the choose computer list
        :type event = wx._core.CommandEvent
        """
        self.__current_shortcuts_selected_computer_name =\
            self.__computer_name_list[self.computer_choice.GetSelection()]
        print self.__current_shortcuts_selected_computer_name
        self.clear_shortcuts_grid()
        self.add_shortcuts_to_shortcut_grid()

# -----------------------------------------------------------------------------
    def add_computers_to_computer_choice(self):
        """
        adds the computer names to the choose computer list in the show
        shortcuts panel
        """
        self.get_saved_computers_name_list()

        if self.computer_choice.IsEmpty() \
                or self.__input_status[
                    'computers status for current shortcuts']:
            self.computer_choice.Clear()
            for computer in self.__computer_name_list:
                self.computer_choice.Append(computer)
            self.__input_status['computers status for current shortcuts'] =\
                False

# -----------------------------------------------------------------------------
    def check_if_row_number_to_delete_was_selected(self):
        """
        checks if a row number of deletion was selected
        """
        if self.delete_number_choice.GetSelection() != -1:
            self.__input_status['row number to delete'] = True

# =============================================================================
    def show_add_new_computer_menu(self, event):
        """
        shows the add or delete computers panel in the wx frame and adds all
        important information.

        :arg event = the event from clicking the new computer panel button
        :type event = wx._core.CommandEvent
        """
        self.show_add_new_computer_panel()
        self.add_new_computer_list_control.DeleteAllItems()
        self.add_computer_information_to_the_remove_table()

# -----------------------------------------------------------------------------
    def show_loading_screen(self):
        """
        loads a waiting gif for the user and calls the find computers in
        network function
        """
        loading_screen = subprocess.Popen(['python', 'loading_screen.py'])
        self.__client.find_computers_in_the_network()
        self.add_computer_information_to_the_add_table()
        loading_screen.terminate()

# -----------------------------------------------------------------------------
    def show_add_new_computer_panel(self):
        """
        shows the new computer panel and makes it fit the frame size
        """
        self.new_shortcut_panel.Hide()
        self.main_panel.Hide()
        self.current_shortcuts_panel.Hide()
        self.manage_computers_panel.Show()
        self.manage_computers_panel.GetSizer().Layout()
        self.manage_computers_panel.GetParent().Layout()

# -----------------------------------------------------------------------------
    def search_computers_in_network(self, event):
        """
        activates the show loading screen function

        :arg event = the event from clicking the find computers button
        :type event = wx._core.CommandEvent
        """
        self.show_loading_screen()

# -----------------------------------------------------------------------------
    def add_computer_information_to_the_remove_table(self):
        """
        adds the current saved computer names to the list
        """
        self.remove_computer_listbox.Set([])
        self.__remove_computer_list_for_getting_user_selection = []
        for computer_name in self.__saved_computer_list:
            if computer_name != 'My Computer':
                self.__remove_computer_list_for_getting_user_selection.append(
                    computer_name)

        self.remove_computer_listbox.Set(
            self.__remove_computer_list_for_getting_user_selection)

# -----------------------------------------------------------------------------
    def delete_computer_from_saved_list(self, event):
        """
        deletes a computer from the saved data. that includes all it's
        shortcuts

        :arg event = the event from clicking the delete button in the add new
        computer panel
        :type event = wx._core.CommandEvent
        """
        self.__input_status['remove_computer'] = True
        self.__current_shortcuts_selected_computer_name =\
            self.__selected_computer_name_to_remove
        conformation_result = self.delete_all_of_the_computer_shortcuts('')
        if conformation_result:
            # update the new computer status so the choice list will update
            self.__input_status['computers status for current shortcuts'] =\
                True
        # update the new computer status so the write new shortcuts
        #  computer list will update
            self.__input_status['computer status for write shortcuts'] = True
            self.__saved_computer_list.__delitem__(
                self.__selected_computer_name_to_remove)
            self.save_added_computers_previous_activity()
            self.__current_shortcuts_selected_computer_name = 'My Computer'
        self.__input_status['remove_computer'] = False
        self.add_computer_information_to_the_remove_table()
        print self.__selected_computer_name_to_add

# -----------------------------------------------------------------------------
    def choose_computer_name_and_ip_to_remove_from_list(self, event):
        """
        sets the computer to be deleted by the user

        :arg event = the event from clicking a computers name in the remove
        computers list in the add new computer panel
        :type event = wx._core.CommandEvent
        """
        print '#############################################'
        if self.__remove_computer_list_for_getting_user_selection[
                self.remove_computer_listbox.GetSelection()]:
            self.__selected_computer_name_to_remove =\
                self.__remove_computer_list_for_getting_user_selection[
                    self.remove_computer_listbox.GetSelection()].title()

        print self.__selected_computer_name_to_remove

# -----------------------------------------------------------------------------
    def get_saved_computers_mac_list(self):
        """
        gets all the saved computers mac addresses
        """
        self.__computer_mac_list = []
        for key in self.__saved_computer_list:
            if key != 'My Computer':
                self.__computer_mac_list.append(
                    self.__saved_computer_list[key][0][1])

# -----------------------------------------------------------------------------
    def add_computer_information_to_the_add_table(self):
        """
        adds the computers names and ips to the add new computer list
        """
        self.__add_computer_list_for_getting_user_selection = []
        for computer_name in self.__client.get_computer_information():
            self.__add_computer_list_for_getting_user_selection.append(
                [[computer_name, self.__client.get_computer_information()[
                    computer_name][0]],
                 self.__client.get_computer_information()[computer_name][1]])

        self.get_saved_computers_mac_list()

        self.add_new_computer_list_control.DeleteAllItems()

        list_of_computers_to_remove = []

        for computer in self.__add_computer_list_for_getting_user_selection:
            # add computers that aren't saved already
            if computer[1] not in self.__computer_mac_list:
                self.add_new_computer_list_control.AppendItem(computer[0])
            else:
                list_of_computers_to_remove.append(computer)

# remove already saved computers from the name and ip from the arp questions
        for computer in list_of_computers_to_remove:
            self.__add_computer_list_for_getting_user_selection.remove(
                computer)

# -----------------------------------------------------------------------------
    def change_computer_name(self):
        """
        opens a dialog box so the user can change the computer name
        """
        # ask user to give name to computer
        self.__argument_functions.ask_text_from_user('open Name')
        # check if user gave name
        if self.__argument_functions.get_argument():
            self.get_saved_computers_name_list()
            name = self.__argument_functions.get_argument().title()
            # checks if the name is already taken
            if name not in self.__computer_name_list:
                self.__argument_functions.set_argument('')
                return name
            else:
                # warns if the name is already used
                self.open_error_dialog(NAME_IS_ALREADY_TAKEN_ERROR)
                self.__argument_functions.set_argument('')
                return self.change_computer_name()
        else:
            # if not warn him and and use recursive function.
            if not self.confirmation_from_user(
                    'warning', COMPUTER_NAME_CONFORMATION_FROM_USER_MESSAGE):
                return self.change_computer_name()
            else:
                return self.__selected_computer_name_to_add

# -----------------------------------------------------------------------------
    def add_new_computer_to_the_list(self, event):
        """
        adds a new computer to the saved data

        :arg event = the event from clicking the add button in the add new
        computer panel
        :type event = wx._core.CommandEvent
        """
        self.get_saved_computers_mac_list()
        if self.__client.get_computer_information()[
            self.__selected_computer_name_to_add][1] \
                not in self.__computer_mac_list:
            self.__saved_computer_list[self.change_computer_name()] = [
                self.__client.get_computer_information()[
                    self.__selected_computer_name_to_add],
                CURRENT_SHORTCUTS_TEMPLATE, FILES_ENDING_COUNTER_TEMPLATE]
            self.save_added_computers_previous_activity()
            # update the new computer status so the choice list will update
            self.__input_status['computers status for current shortcuts'] =\
                True
            # update the new computer status so the write new shortcuts
            #  computer list will update
            self.__input_status['computer status for write shortcuts'] = True
            self.add_computer_information_to_the_remove_table()
            print self.__selected_computer_name_to_add
        else:
            self.open_error_dialog(COMPUTER_ALREADY_ADDED_ERROR)

# -----------------------------------------------------------------------------
    def choose_computer_name_and_ip_to_add_to_list(self, event):
        """
        sets the computer name and ip to be added to the saved data

        :arg event = the event from clicking the computer' name from the list
        :type event = wx._core.CommandEvent
        """
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        if self.__add_computer_list_for_getting_user_selection[
                self.add_new_computer_list_control.GetSelectedRow()][0]:
            self.__selected_computer_name_to_add = \
                self.__add_computer_list_for_getting_user_selection[
                    self.add_new_computer_list_control.GetSelectedRow()][
                        0][0].title()

        print self.__selected_computer_name_to_add

# -----------------------------------------------------------------------------
    def save_added_computers_previous_activity(self):
        """
        saves data to the data file
        """
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'w')
        pickle.dump(self.__saved_computer_list, json_save_file)
        json_save_file.close()

# -----------------------------------------------------------------------------
    def get_added_computers_previous_activity(self):
        """
        extracts data from the data file
        """
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'r')
        self.__saved_computer_list = pickle.load(json_save_file)

# =============================================================================
    def go_to_home_panel(self, event):
        """
        shows the main panel
        """
        self.main_panel.Show()
        self.current_shortcuts_panel.Hide()
        self.new_shortcut_panel.Hide()
        self.manage_computers_panel.Hide()

    def update_user_data(self, event):
        """
        updates the data file before closing the program

        :arg event = the event from clicking the close button of thw wx frame
        :type event = wx._core.CommandEvent
        """
        # self.__shortcuts_user.save_user_activity()
        self.save_added_computers_previous_activity()
        self.Destroy()


def main():
    """
    opens the wx frame and runs the program
    """
    app = wx.App(False)

    # create an object of CalcFrame
    frame = Main(None)
    # show the frame
    frame.Show(True)
    # start the applications
    app.MainLoop()

if __name__ == '__main__':
    main()
