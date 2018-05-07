# -*- coding: utf-8 -*-
"""
Description:    receives information from a saved ahk file and sends the order
                for a remote acting server

name:           Elad Hayek
date:           22.3.18
file name:      activate_remote_data.py
"""

import sys
from subprocess import *
from new_computer_class import *
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
    gets the remote server ip add
    """
    action = sys.argv[1]
    argument = sys.argv[2]
    mac = sys.argv[3]

    # action = 'open cmd'
    # argument = ';;'
    # mac = '54:35:30:99:13:95'

    arp_question = Popen(['python', 'get_ip_and_mac.py', mac], stdout=PIPE)
    result = arp_question.communicate()[0]
    ip = result.strip()

    client = Client()
    try:
        client.connect_to_server(ip, SERVER_ACTING_PORT)
        client.activate_the_shortcut_on_the_computer(action, argument)

    except socket.error:
        with open('acting client error.txt', 'w') as f:
            f.write(print_exception())

        client.close_client()


if __name__ == '__main__':
    main()
