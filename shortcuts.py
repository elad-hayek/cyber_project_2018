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

HOT_KEYS_TEMPLATE = """~%s & %s::
if GetKeyState("%s", "%s") & GetKeyState("%s", "%s")
{
"""


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


    def write_new_shortcut(self, shortcut_name):
        self.__shortcut_sequence = raw_input('enter your shortcut sequence:')
        self.__shortcut_sequence = '+'.join(self.__shortcut_sequence).split('+')


        if shortcut_name == 'open folder':
            path = raw_input('enter path:')
            ahk_file = open(FOLDER_SCRIPTS_PATH+r'\folder'+str(          # create new ahk file
                self.__files_ending_counter['folders'])+'.ahk', 'w')

            ahk_file.write(self.write_to_file('open folder', path))
            ahk_file.close()


            self.activate_ahk_files(FOLDER_SCRIPTS_PATH+r'\folder'+str(         # activate
                self.__files_ending_counter['folders'])+'.ahk')

            self.add_to_history('open folder', r'folder'+str(self.__files_ending_counter['folders'])+'.ahk',FOLDER_SCRIPTS_PATH+r'\folder'+str(self.__files_ending_counter['folders'])+'.ahk', path)

            self.__files_ending_counter['folders'] += 1

        elif shortcut_name == 'open url':
            url = raw_input('enter url: ')
            ahk_file = open(URL_SCRIPTS_PATH+'\url'+str(                # create new ahk file
                self.__files_ending_counter['urls'])+'.ahk', 'w')

            ahk_file.write(self.write_to_file('open url', url))
            ahk_file.close()

            self.activate_ahk_files(URL_SCRIPTS_PATH+'\url'+str(                # activate
                self.__files_ending_counter['urls'])+'.ahk')

            self.add_to_history('open url', r'url'+str(self.__files_ending_counter['urls'])+'.ahk', URL_SCRIPTS_PATH+'\url'+str(self.__files_ending_counter['urls'])+'.ahk' ,url)

            self.__files_ending_counter['urls'] += 1

        elif shortcut_name == 'open program':
            path = raw_input('enter path:')
            ahk_file = open(PROGRAM_SCRIPTS_PATH+r'\program'+str(          # create new ahk file
                self.__files_ending_counter['programs'])+'.ahk', 'w')

            ahk_file.write(self.write_to_file('open program', path))
            ahk_file.close()


            self.activate_ahk_files(PROGRAM_SCRIPTS_PATH+r'\program'+str(       # activate
                self.__files_ending_counter['programs'])+'.ahk')

            self.add_to_history('open program', r'program'+str(self.__files_ending_counter['programs'])+'.ahk', PROGRAM_SCRIPTS_PATH+r'\program'+str(self.__files_ending_counter['programs'])+'.ahk', path)

            self.__files_ending_counter['programs'] += 1

        elif shortcut_name == 'open cmd':
            ahk_file = open(CMD_SCRIPTS_PATH+r'\cmd.ahk', 'w')

            ahk_file.write(self.write_to_file('open cmd'))
            ahk_file.close()

            self.activate_ahk_files(CMD_SCRIPTS_PATH+r'\cmd.ahk')

            self.add_to_history('open cmd', r'cmd.ahk', CMD_SCRIPTS_PATH+r'\cmd.ahk')

        elif shortcut_name == 'open settings':
            ahk_file = open(SETTINGS_SCRIPTS_PATH+r'\settings.ahk', 'w')

            ahk_file.write(self.write_to_file('open settings'))
            ahk_file.close()

            self.activate_ahk_files(SETTINGS_SCRIPTS_PATH+r'\settings.ahk')

            self.add_to_history('open settings', r'settings.ahk',SETTINGS_SCRIPTS_PATH+r'\settings.ahk')

    def write_to_file(self, shortcut_name, argument=''):
        if len(self.__shortcut_sequence) == 1:
            string_to_write = HOT_KEYS_TEMPLATE[:3] % self.__shortcut_sequence[0] + '::' + self.__shortcuts_templates[shortcut_name] % argument
            return string_to_write

        elif len(self.__shortcut_sequence) == 2:
            string_to_write = HOT_KEYS_TEMPLATE[:10] % (self.__shortcut_sequence[0], self.__shortcut_sequence[1]) + self.__shortcuts_templates[shortcut_name] % argument
            return string_to_write

        elif len(self.__shortcut_sequence) == 3:
            string_to_write = HOT_KEYS_TEMPLATE[:30] % (self.__shortcut_sequence[1], self.__shortcut_sequence[2], self.__shortcut_sequence[0])+')\n{' + self.__shortcuts_templates[shortcut_name] % argument +'\n}'
            return string_to_write

        elif len(self.__shortcut_sequence) == 4:
            string_to_write = HOT_KEYS_TEMPLATE[:37] % (self.__shortcut_sequence[2], self.__shortcut_sequence[3], self.__shortcut_sequence[0], self.__shortcut_sequence[1])+'\n{' + self.__shortcuts_templates[shortcut_name] % argument +'\n}'
            return string_to_write

        elif len(self.__shortcut_sequence) == 5:
            string_to_write = HOT_KEYS_TEMPLATE[:56] % (self.__shortcut_sequence[3], self.__shortcut_sequence[4], self.__shortcut_sequence[0], self.__shortcut_sequence[1], self.__shortcut_sequence[2])+')\n{' + self.__shortcuts_templates[shortcut_name] % argument +'\n}'
            return string_to_write

        elif len(self.__shortcut_sequence) == 6:
            string_to_write = HOT_KEYS_TEMPLATE[:65] % (self.__shortcut_sequence[4], self.__shortcut_sequence[5], self.__shortcut_sequence[0], self.__shortcut_sequence[1], self.__shortcut_sequence[2], self.__shortcut_sequence[3])+ self.__shortcuts_templates[shortcut_name] % argument +'\n}'
            return string_to_write

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