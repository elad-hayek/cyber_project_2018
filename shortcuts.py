# -*- coding: utf-8 -*-
import subprocess
import os

CLOSE_PROCESS_BY_NAME_PATH = 'E:\USER\Documents\school\cyber\project_2018\close_process.ahk'

HOT_KEYS_PROGRAM_PATH = 'E:\Program Files\AutoHotKey\AutoHotkey.exe'

FOLDER_SCRIPTS_PATH = r'C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' \
                      '\user_shortcuts\\folders_shortcuts'

PROGRAM_SCRIPTS_PATH = r'C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' \
                       r'\user_shortcuts\programs_shortcuts'

URL_SCRIPTS_PATH = r'C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' \
                   r'\user_shortcuts\url_shortcuts'

CMD_SCRIPTS_PATH = r'C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' \
                   r'\user_shortcuts\cmd_shortcuts'

SETTINGS_SCRIPTS_PATH = r'C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' \
                        r'\user_shortcuts\settings_shortcuts'

HOT_KEYS_TEMPLATE = """~{5}::
if GetKeyState("{0}") & GetKeyState("{1}") & GetKeyState("{2}") & GetKeyState("{3}")& GetKeyState("{4}")"""


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

        self.__scripts_path = {'folder': FOLDER_SCRIPTS_PATH, 'url': URL_SCRIPTS_PATH, 'program': PROGRAM_SCRIPTS_PATH,
                                    'cmd': CMD_SCRIPTS_PATH, 'settings': SETTINGS_SCRIPTS_PATH}

#-------------------------------------------------------------------------------
    def get_shortcut_sequence(self):
        self.__shortcut_sequence = raw_input('enter your shortcut sequence:')
        self.__shortcut_sequence = '+'.join(self.__shortcut_sequence).split('+')

#-------------------------------------------------------------------------------
    def run_action_sequence_for_shortcut(self, shortcut_type, argument=''):
        self.__shortcut_script_path = self.__scripts_path[shortcut_type]+'\\'+shortcut_type+str(self.__files_ending_counter[shortcut_type])+'.ahk'
        print self.__shortcut_script_path
        ahk_file = open(self.__shortcut_script_path, 'w')

        ahk_file.write(self.write_to_file('open '+shortcut_type, argument))
        ahk_file.close()


        self.activate_ahk_files(self.__shortcut_script_path)

        self.add_to_history('open '+shortcut_type, shortcut_type+str(self.__files_ending_counter[shortcut_type])+'.ahk', argument)

        self.__files_ending_counter[shortcut_type] += 1

#-------------------------------------------------------------------------------

    def write_new_shortcut(self, shortcut_name):
        self.get_shortcut_sequence()

        if shortcut_name == 'open folder':
            path = raw_input('enter path:')
            self.run_action_sequence_for_shortcut('folder', path)

        elif shortcut_name == 'open url':
            url = raw_input('enter url:')
            self.run_action_sequence_for_shortcut('url', url)

        elif shortcut_name == 'open program':
            path = raw_input('enter path:')
            self.run_action_sequence_for_shortcut('program', path)

        elif shortcut_name == 'open cmd':
            self.run_action_sequence_for_shortcut('cmd')

        elif shortcut_name == 'open settings':
            self.run_action_sequence_for_shortcut('settings')

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

    def show_current_shortcuts(self):
        print self.__current_shortcuts
#-------------------------------------------------------------------------------

    def activate_ahk_files(self, file_path, argument=''):
        subprocess.Popen([HOT_KEYS_PROGRAM_PATH, file_path, argument])
#-------------------------------------------------------------------------------

    def add_to_history(self, shortcut_type, file_name, argument=None):
        self.__current_shortcuts[shortcut_type][file_name] = (argument, self.__shortcut_sequence, self.__shortcut_script_path)


def main():
    shortcut = ShortCuts()
    option = raw_input('choos option: open folder, open url, open settings, open cmd, open program: ')
    shortcut.write_new_shortcut(option)
    shortcut.show_current_shortcuts()

    a=raw_input('type:')
    b=raw_input('name:')
    shortcut.delete_shortcut(a, b)




if __name__ == '__main__':
    main()