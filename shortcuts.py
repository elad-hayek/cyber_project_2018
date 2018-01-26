# -*- coding: utf-8 -*-
import subprocess
import os

CLOSE_PROCESS_BY_NAME_PATH = 'E:\USER\Documents\school\cyber\project_2018\user_shortcuts\close_process.ahk'

HOT_KEYS_PROGRAM_PATH = 'E:\Program Files\AutoHotKey\AutoHotkey.exe'

FOLDER_SCRIPTS_PATH = r'E:\USER\Documents\school\cyber\project_2018' \
                      '\user_shortcuts\\folders_shortcuts'

PROGRAM_SCRIPTS_PATH = r'E:\USER\Documents\school\cyber\project_2018' \
                       r'\user_shortcuts\programs_shortcuts'

URL_SCRIPTS_PATH = r'E:\USER\Documents\school\cyber\project_2018' \
                   r'\user_shortcuts\url_shortcuts'

CMD_SCRIPTS_PATH = r'E:\USER\Documents\school\cyber\project_2018' \
                   r'\user_shortcuts\cmd_shortcuts'

SETTINGS_SCRIPTS_PATH = r'E:\USER\Documents\school\cyber\project_2018' \
                        r'\user_shortcuts\settings_shortcuts'

HOT_KEYS_TEMPLATE = """~{5}::
if GetKeyState("{0}") & GetKeyState("{1}") & GetKeyState("{2}") & GetKeyState("{3}")& GetKeyState("{4}")"""



class ShortCuts:
    def __init__(self):
        self.__shortcut_sequence = ''
        self.__shortcuts_templates = {'open folder': 'Run, %s',
                                      'open url': 'Run, chrome.exe %s',
                                      'open settings': 'Run, control %s',
                                      'open cmd': 'Run, cmd %s',
                                      'open program': 'Run, %s'}

        self.__current_shortcuts = {'open folder': {}, 'open url': {}, 'open program': {},
                                    'open cmd': {}, 'open settings': {}}

        self.__files_ending_counter = {'folders': 0, 'urls': 0, 'programs': 0}


    def get_shortcut_sequence(self):
        self.__shortcut_sequence = raw_input('enter your shortcut sequence:')
        self.__shortcut_sequence = '+'.join(self.__shortcut_sequence).split('+')

    def open_folder(self):
        path = raw_input('enter path:')
        ahk_file = open(FOLDER_SCRIPTS_PATH+r'\folder'+str(          # create new ahk file
            self.__files_ending_counter['folders'])+'.ahk', 'w')

        ahk_file.write(self.write_to_file('open folder', path))
        ahk_file.close()


        self.activate_ahk_files(FOLDER_SCRIPTS_PATH+r'\folder'+str(         # activate
            self.__files_ending_counter['folders'])+'.ahk')

        self.add_to_history('open folder', r'folder'+str(self.__files_ending_counter['folders'])+'.ahk',FOLDER_SCRIPTS_PATH+r'\folder'+str(self.__files_ending_counter['folders'])+'.ahk', path)

        self.__files_ending_counter['folders'] += 1

    def open_url(self):
        url = raw_input('enter url: ')
        ahk_file = open(URL_SCRIPTS_PATH+'\url'+str(                # create new ahk file
            self.__files_ending_counter['urls'])+'.ahk', 'w')

        ahk_file.write(self.write_to_file('open url', url))
        ahk_file.close()

        self.activate_ahk_files(URL_SCRIPTS_PATH+'\url'+str(                # activate
            self.__files_ending_counter['urls'])+'.ahk')

        self.add_to_history('open url', r'url'+str(self.__files_ending_counter['urls'])+'.ahk', URL_SCRIPTS_PATH+'\url'+str(self.__files_ending_counter['urls'])+'.ahk' ,url)

        self.__files_ending_counter['urls'] += 1

    def open_program(self):
        path = raw_input('enter path:')
        ahk_file = open(PROGRAM_SCRIPTS_PATH+r'\program'+str(          # create new ahk file
            self.__files_ending_counter['programs'])+'.ahk', 'w')

        ahk_file.write(self.write_to_file('open program', path))
        ahk_file.close()


        self.activate_ahk_files(PROGRAM_SCRIPTS_PATH+r'\program'+str(       # activate
            self.__files_ending_counter['programs'])+'.ahk')

        self.add_to_history('open program', r'program'+str(self.__files_ending_counter['programs'])+'.ahk', PROGRAM_SCRIPTS_PATH+r'\program'+str(self.__files_ending_counter['programs'])+'.ahk', path)

        self.__files_ending_counter['programs'] += 1

    def open_cmd(self):
        ahk_file = open(CMD_SCRIPTS_PATH+r'\cmd.ahk', 'w')

        ahk_file.write(self.write_to_file('open cmd'))
        ahk_file.close()

        self.activate_ahk_files(CMD_SCRIPTS_PATH+r'\cmd.ahk')

        self.add_to_history('open cmd', r'cmd.ahk', CMD_SCRIPTS_PATH+r'\cmd.ahk')

    def open_settings(self):
        ahk_file = open(SETTINGS_SCRIPTS_PATH+r'\settings.ahk', 'w')

        ahk_file.write(self.write_to_file('open settings'))
        ahk_file.close()

        self.activate_ahk_files(SETTINGS_SCRIPTS_PATH+r'\settings.ahk')

        self.add_to_history('open settings', r'settings.ahk',SETTINGS_SCRIPTS_PATH+r'\settings.ahk')


    def write_new_shortcut(self, shortcut_name):
        self.get_shortcut_sequence()
        if shortcut_name == 'open folder':
            self.open_folder()

        elif shortcut_name == 'open url':
            self.open_url()

        elif shortcut_name == 'open program':
            self.open_program()

        elif shortcut_name == 'open cmd':
            self.open_cmd()

        elif shortcut_name == 'open settings':
            self.open_settings()

    def write_to_file(self, shortcut_name, argument=''):
        sequence_format_list = self.check_sequence_length()
        string_to_write = HOT_KEYS_TEMPLATE.format(*sequence_format_list)+'\n{'+ self.__shortcuts_templates[shortcut_name] % argument +'\n}'
        return string_to_write


    def check_sequence_length(self):
        sequence_format_list = self.__shortcut_sequence
        if len(sequence_format_list) < 6:
            for i in range(6-len(sequence_format_list)):
                sequence_format_list.append(sequence_format_list[-1])
        return sequence_format_list

    def delete_shortcut(self, shortcut_type, file_name):
        file_to_delete = self.__current_shortcuts[shortcut_type][file_name][2]
        self.activate_ahk_files(CLOSE_PROCESS_BY_NAME_PATH, file_name)
        os.remove(file_to_delete)

    def show_current_shortcuts(self):
        print self.__current_shortcuts

    def activate_ahk_files(self, file_path, argument=''):
        subprocess.Popen([HOT_KEYS_PROGRAM_PATH, file_path, argument])

    def add_to_history(self, shortcut_name, file_name, full_path, argument=None):
        self.__current_shortcuts[shortcut_name][file_name] = (argument, self.__shortcut_sequence, full_path)


def main():
    shortcut = ShortCuts()
    option = raw_input('choos option: open folder, open url, open settings, open cmd, open program: ')
    shortcut.write_new_shortcut(option)
    shortcut.show_current_shortcuts()


    option = raw_input('choos option: open folder, open url, open settings, open cmd, open program: ')
    shortcut.write_new_shortcut(option)
    shortcut.show_current_shortcuts()
    shortcut.delete_shortcut('open folder', 'folder0.ahk')




if __name__ == '__main__':
    main()