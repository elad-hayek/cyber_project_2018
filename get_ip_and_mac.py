# -*- coding: utf-8 -*-

from new_computer_class import Client
import sys
from ast import literal_eval

BROADCAST = 'ff:ff:ff:ff:ff:ff'

def main():
    mac = sys.argv[1]
    client = Client()
    client.connect_to_server('192.168.1.44', 8835)
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