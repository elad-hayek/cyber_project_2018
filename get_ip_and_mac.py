# -*- coding: utf-8 -*-
"""
Description:    connects the the main server and gets the computers'
                information that are in the network.

name:           Elad Hayek
date:           22.3.18
file name:      get_ip_and_mac.py
"""

from new_computer_class import Client
import sys
from ast import literal_eval

BROADCAST = 'ff:ff:ff:ff:ff:ff'
SERVER_IP = '192.168.1.53'
SERVER_PORT = 8840


def main():
    """
    connects the main server and returns the data
    """
    mac = sys.argv[1]
    # mac = '54:35 d:30:99:13:95'
    # mac = BROADCAST
    client = Client()
    client.connect_to_server(SERVER_IP, SERVER_PORT)
    data = client.receive_information_from_the_server()
    data = literal_eval(data)
    if mac == BROADCAST:
        print data
    else:
        for key in data:
            if mac in data[key]:
                print data[key][0]
    client.close_client()


if __name__ == '__main__':
    main()
