# -*- coding: utf-8 -*-
"""
Description:    activates the shortcuts that are send remotely

name:           Elad Hayek
date:           22.3.18
file name:      activate_shortcuts.py
"""

import sys
import os


class ActivateShortcuts():
    def __init__(self):
        """
        creates the active shortcut instance
        """
        self.__action = ''
        self.__argument = ''
        self.__remote_shortcut_activation = {
            'open folder': self.open_folder, 'open url': self.open_url,
            'open file': self.open_file, 'open cmd': self.open_cmd,
            'open settings': self.open_settings}

    def open_folder(self):
        """
        opens a folder
        """
        os.system(self.__argument[:2]+' && cd '+self.__argument+' && start.')

    def open_url(self):
        """
        opens a url
        """
        os.system('start "" '+self.__argument)

    def open_file(self):
        """
        opens a file
        """
        os.system('start "" '+self.__argument)

    def open_cmd(self):
        """
        opens cmd
        """
        os.system('start cmd')

    def open_settings(self):
        """
        opens the control panel
        """
        os.system('start "" "control"')

    def set_action(self, action):
        """
        sets the action for the right function activation
        """
        self.__action = action

    def set_argument(self, argument):
        """
        stets the argument for the function activation
        """
        self.__argument = argument

    def activate_action(self):
        """
        activates the right function according to the action
        """
        self.__remote_shortcut_activation[self.__action]()


def main():
    """
    receives the needed information and activates the action
    """
    activate_shortcut = ActivateShortcuts()
    activate_shortcut.set_action(sys.argv[1])
    print sys.argv[:]
    if sys.argv[2]:
        activate_shortcut.set_argument(sys.argv[2])
    activate_shortcut.activate_action()


if __name__ == '__main__':
    main()
