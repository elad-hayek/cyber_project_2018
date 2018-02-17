# -*- coding: utf-8 -*-

from new_computer_class import *
import sys

def main():
    try:
        server_type = sys.argv[1]
        with open('a.txt', 'w') as f:
            f.write('aaaaaaaaaaaaaaaaaaaaaaaaaaaa       '+server_type)
        while 1:
            server = Server(int(server_type))
            shortcut_information = server.receive_information_from_client()
            print shortcut_information
            server.pass_information_to_client('ok')
            if int(server_type) == 0:
                server.make_the_shortcut_file(shortcut_information[0], shortcut_information[1], shortcut_information[2])
            server.disconnect_client()
            server.close_server()
    except Exception, e:
        pass
        # with open('a.txt', 'w') as f:
        #     f.write(repr(e))

if __name__ == '__main__':
    main()