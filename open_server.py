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
import os.path
import linecache


def print_exception():
    """
    return an extended description of the error
    """
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(
        filename, lineno, line.strip(), exc_obj)


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

            if int(server_type) == 0:
                with open('server_received_information.txt', 'w') as f:
                    f.write(repr(shortcut_information))

                if shortcut_information[0] == 'open folder' \
                        or shortcut_information[0] == 'open file':
                    if not os.path.exists(shortcut_information[2]):
                        server.pass_information_to_client('not found')
                    else:
                        server.pass_information_to_client('ok')

                else:
                    server.pass_information_to_client('ok')

                server.make_the_shortcut_file(shortcut_information[0],
                                              shortcut_information[1],
                                              shortcut_information[2])
            server.disconnect_client()

    except Exception, e:
        with open('open_server_error.txt', 'w') as f:
            f.write(print_exception())
        server.close_server()

if __name__ == '__main__':
    main()
