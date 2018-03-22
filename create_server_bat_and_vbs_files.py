# -*- coding: utf-8 -*-
"""
Description:    creates the bat and vbs files that will activate the servers
                every time the computer starts and does so hidden from the user.

name:           Elad Hayek
date:           22.3.18
file name:      create_server_bat_and_vbs_files.py
"""

import os
import getpass
import subprocess

CREATING_SCRIPTS_PATH = 'C:\\Users\\'+getpass.getuser()+'\\AppData\\Roaming\Microsoft\\Windows\\Start Menu\Programs\\Startup'

LISTENING_SERVER_BAT_SCRIPT = """
@echo off
set SERVER_TYPE=0
python "open_server.py" %SERVER_TYPE%
echo %ERRORLEVEL%
pause
"""
LISTENING_SERVER_BAT_SCRIPT_NAME = 'open_listening_server.bat'

ACTING_SERVER_BAT_SCRIPT = """
@echo off
set SERVER_TYPE=1
python "open_server.py" %SERVER_TYPE%
echo %ERRORLEVEL%
pause
"""
ACTING_SERVER_BAT_SCRIPT_NAME = 'open_acting_server.bat'

LISTENING_SERVER_VBS_SCRIPT = """
Set shell = CreateObject("WScript.Shell")
shell.CurrentDirectory = "%s"
shell.Run "open_listening_server.bat", 0, True
"""

LISTENING_SERVER_VBS_SCRIPT_NAME = '\\run_listening_server_bat.vbs'

ACTING_SERVER_VBS_SCRIPT = """
Set shell = CreateObject("WScript.Shell")
shell.CurrentDirectory = "%s"
shell.Run "open_acting_server.bat", 0, True
"""

ACTING_SERVER_VBS_SCRIPT_NAME = '\\run_acting_server_bat.vbs'


class Create_bat_and_vbs_files:
    def __init__(self):
        """
        creates the files in order and activates the servers
        """
        if not self.check_if_first_time():
            self.crate_listening_server_bat()
            self.create_listening_server_vbs()
            self.create_acting_server_bat()
            self.create_acting_server_vbs()
            self.activate_servers()

    def crate_listening_server_bat(self):
        """
        creates the listening server bat file
        """
        with open(LISTENING_SERVER_BAT_SCRIPT_NAME, 'w') as bat_file:
            bat_file.write(LISTENING_SERVER_BAT_SCRIPT)
        print 'created listening bat'

    def create_listening_server_vbs(self):
        """
        creates the listening server vbs file
        """
        with open(CREATING_SCRIPTS_PATH+LISTENING_SERVER_VBS_SCRIPT_NAME, 'w') as vbs_file:
            vbs_file.write(LISTENING_SERVER_VBS_SCRIPT % os.getcwd())
        print 'created listening vbs'


    def create_acting_server_bat(self):
        """
        creates the acting server bat file
        """
        with open(ACTING_SERVER_BAT_SCRIPT_NAME, 'w') as bat_file:
            bat_file.write(ACTING_SERVER_BAT_SCRIPT)
        print 'created acting bat'

    def create_acting_server_vbs(self):
        """
        creates the acting server vbs file
        """
        with open(CREATING_SCRIPTS_PATH+ACTING_SERVER_VBS_SCRIPT_NAME, 'w') as vbs_file:
            vbs_file.write(ACTING_SERVER_VBS_SCRIPT % os.getcwd())
        print 'created acting vbs'

    def check_if_first_time(self):
        """
        checks if the server files already exist
        """
        if os.path.isfile(CREATING_SCRIPTS_PATH+ACTING_SERVER_VBS_SCRIPT_NAME):
            return True

    def activate_servers(self):
        """
        activates the servers
        """
        subprocess.Popen(['cscript.exe', CREATING_SCRIPTS_PATH+LISTENING_SERVER_VBS_SCRIPT_NAME])
        print 'activated listening bat'

        subprocess.Popen(['cscript.exe', CREATING_SCRIPTS_PATH+ACTING_SERVER_VBS_SCRIPT_NAME])
        print 'activated acting bat'
