# -*- coding: utf-8 -*-

import sys
from subprocess import *
from new_computer_class import *



def main():

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
    client.connect_to_server(ip, SERVER_ACTING_PORT)
    client.activate_the_shortcut_on_the_computer(action, argument)

    with open('a.txt', 'w') as f:
        f.write(client.receive_information_from_the_server())

    client.close_client()



if __name__ == '__main__':
    main()