# -*- coding: utf-8 -*-
"""
Description:    opens a server according to the input. if it's a listening
                server it will receive a shortcut and built the file. if it's
                a acting server it will activate an action according to the
                remote action.

name:           Elad Hayek
date:           22.3.18
file name:      open_server.py
"""

from new_computer_class import *
import sys


def main():
    """
    opens the server and passes the information for processing.
    """
    server_type = sys.argv[1]
    server = Server(int(server_type))
    try:
        while 1:
            server.connect_to_client()
            shortcut_information = server.receive_information_from_client()
            server.pass_information_to_client('ok')
            if int(server_type) == 0:
                server.make_the_shortcut_file(shortcut_information[0],
                                              shortcut_information[1],
                                              shortcut_information[2])
            server.disconnect_client()

    except Exception, e:
        with open('a.txt', 'w') as f:
            f.write(repr(e))
        server.close_server()

if __name__ == '__main__':
    main()
