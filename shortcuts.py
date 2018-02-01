# -*- coding: utf-8 -*-
import subprocess
import os
from Tkinter import *
import tkFileDialog
import wx

CLOSE_PROCESS_BY_NAME_PATH = 'E:\USER\Documents\school\cyber\project_2018\close_process.ahk'

HOT_KEYS_PROGRAM_PATH = 'E:\Program Files\AutoHotKey\AutoHotkey.exe'

SCRIPTS_PATH = r'C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'


HOT_KEYS_TEMPLATE = """~{5}::
if GetKeyState("{0}") & GetKeyState("{1}") & GetKeyState("{2}")
 & GetKeyState("{3}")& GetKeyState("{4}")"""


class ShortCuts:
    def __init__(self):
        self.__shortcut_sequence = ''
        self.__shortcut_script_path = ''
        self.__shortcuts_templates = {'open folder': 'Run, %s',
                                      'open url': 'Run, chrome.exe %s',
                                      'open settings': 'Run, control %s',
                                      'open cmd': 'Run, cmd %s',
                                      'open program': 'Run, %s'}

        self.__current_shortcuts = {'open folder': {}, 'open url': {}, 'open program': {},
                                    'open cmd': {}, 'open settings': {}}

        self.__files_ending_counter = {'folder': 0, 'url': 0, 'program': 0, 'cmd': 0, 'settings': 0}

        self.__user_choice = ''

        self.__shortcut_function_activation = {'open folder': self.open_folder, 'open url': self.open_url, 'open settings': self.open_settings, 'open cmd': self.open_cmd, 'open program': self.open_program}


    def ask_text_from_user(self, action):
        frame = wx.Frame(None, -1, action)
        frame.SetDimensions(0, 0, 200, 50)

        # Create text input
        dlg = wx.TextEntryDialog(frame, 'Enter '+action.split()[1], 'Text Entry')
        if dlg.ShowModal() == wx.ID_OK:
            return dlg.GetValue()
        dlg.Destroy()
#-------------------------------------------------------------------------------
    def choose_folder_manager(self):
        root = Tk()
        root.withdraw()
        root.filename = tkFileDialog.askdirectory(mustexist=True, parent=root, initialdir='/', title='Select your pictures folder')
        return root.filename
#-------------------------------------------------------------------------------
    def choose_program_manager(self):
        root = Tk()
        root.withdraw()
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select program", filetypes=(("exe files", "*.exe"), ("all files", "*.*")))
        return root.filename
#-------------------------------------------------------------------------------
    def open_folder(self):
        path = self.choose_folder_manager()
        self.run_action_sequence_for_shortcut('folder', path)

#-------------------------------------------------------------------------------
    def open_url(self):
        url = self.ask_text_from_user('open url')
        self.run_action_sequence_for_shortcut('url', url)

#-------------------------------------------------------------------------------
    def open_settings(self):
        self.run_action_sequence_for_shortcut('settings')

#-------------------------------------------------------------------------------
    def open_cmd(self):
        self.run_action_sequence_for_shortcut('cmd')

#-------------------------------------------------------------------------------
    def open_program(self):
        path = self.choose_program_manager()
        self.run_action_sequence_for_shortcut('program', path)

#-------------------------------------------------------------------------------
    def get_shortcut_sequence(self):
        return self.__shortcut_sequence

#-------------------------------------------------------------------------------
    def set_users_choice(self, choice):
        self.__user_choice = choice

#-------------------------------------------------------------------------------
    def set_shortcut_sequence(self, user_sequence):
        self.__shortcut_sequence = user_sequence
        self.__shortcut_sequence = self.__shortcut_sequence.split('+')

#-------------------------------------------------------------------------------
    def run_action_sequence_for_shortcut(self, shortcut_type, argument=''):
        self.__shortcut_script_path = SCRIPTS_PATH+'\\'+shortcut_type+str(self.__files_ending_counter[shortcut_type])+'.ahk'
        print self.__shortcut_script_path
        ahk_file = open(self.__shortcut_script_path, 'w')

        ahk_file.write(self.write_to_file('open '+shortcut_type, argument))
        ahk_file.close()


        self.activate_ahk_files(self.__shortcut_script_path)

        self.add_to_history('open '+shortcut_type, shortcut_type+str(self.__files_ending_counter[shortcut_type])+'.ahk', argument)

        self.__files_ending_counter[shortcut_type] += 1

#-------------------------------------------------------------------------------

    def write_new_shortcut(self):
        self.__shortcut_function_activation[self.__user_choice]()

#-------------------------------------------------------------------------------

    def write_to_file(self, shortcut_name, argument=''):
        sequence_format_list = self.check_sequence_length()
        string_to_write = HOT_KEYS_TEMPLATE.format(*sequence_format_list)+'\n{'+ self.__shortcuts_templates[shortcut_name] % argument + '\n}'
        return string_to_write

#-------------------------------------------------------------------------------

    def check_sequence_length(self):
        sequence_format_list = self.__shortcut_sequence[:]
        if len(sequence_format_list) < 6:
            for i in range(6-len(sequence_format_list)):
                sequence_format_list.append(sequence_format_list[-1])
        return sequence_format_list
#-------------------------------------------------------------------------------

    def delete_shortcut(self, shortcut_type, file_name):
        file_to_delete = self.__current_shortcuts[shortcut_type][file_name][2]
        self.activate_ahk_files(CLOSE_PROCESS_BY_NAME_PATH, file_name)
        os.remove(file_to_delete)
#-------------------------------------------------------------------------------

    def get_current_shortcuts(self):
        return self.__current_shortcuts

#-------------------------------------------------------------------------------

    def activate_ahk_files(self, file_path, argument=''):
        subprocess.Popen([HOT_KEYS_PROGRAM_PATH, file_path, argument])
#-------------------------------------------------------------------------------

    def add_to_history(self, shortcut_type, file_name, argument=None):
        self.__current_shortcuts[shortcut_type][file_name] = (argument, self.__shortcut_sequence, self.__shortcut_script_path)


def main():
    pass



if __name__ == '__main__':
    main()