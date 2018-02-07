# -*- coding: utf-8 -*-

from socket_class import Sockets
import _multiprocessing
from subprocess import Popen, PIPE
import re

MAC_REGULAR_EXPRESSION = '([a-fA-F0-9]{2}[:|\-]?){6}'
IP_REGULAR_EXPRESSION = '192.168.1.(\d){1,3}'
MAC_FILTER = ['ff-ff-ff-ff-ff-ff', 'ff-ff-ff-ff-ff-fa']
IP_FILTER = ['192.168.1.1']

SERVER_IP = '0.0.0.0'
SERVER_PORT = 8820


class Server():
    def __init__(self):
        self.__server_socket = Sockets()
        self.__client_socket = Sockets()
        self.__server_socket.open_server(SERVER_IP, SERVER_PORT)
        self.open_server()

    def open_server(self):
        self.__client_socket, client_address = self.__server_socket.client_connection()

    def receive_information_from_client(self):
        data = self.__server_socket.read_from_client(self.__client_socket)
        return data.split('`')

    def pass_information_to_client(self, data):
        self.__server_socket.write_to_client(data, self.__client_socket)

    def make_the_shortcut_file(self):
        pass

    def activate_the_shortcut_on_the_computer(self):
        pass


class Client():
    def __init__(self):
        self.__client_socket = Sockets()
        self.__computer_information = {}

    def connect_to_server(self, ip, port):
        self.__client_socket.connect_to_server(ip, port)

    def receive_information_from_the_server(self):
        data = self.__client_socket.read_from_server()
        return data

    def send_request_to_the_server(self, action, sequence, argument):
        data_to_send = action+'`'+sequence+'`'+argument
        self.__client_socket.write_to_server(data_to_send)

    def activate_the_shortcut_on_the_computer(self):
        pass

    def find_computers_in_the_network(self):
        arp_question = Popen(['arp', '-a'], stdout=PIPE)
        result = arp_question.communicate()[0]
        result_split_lines = [line.strip() for line in result.splitlines()]  # split the arp answer to lines

        for line in result_split_lines:
            mac_finder = re.search(MAC_REGULAR_EXPRESSION, line)
            ip_finder = re.search(IP_REGULAR_EXPRESSION, line)
            if mac_finder and ip_finder:
                if mac_finder.group(0).lower() not in MAC_FILTER and ip_finder.group(0) not in IP_FILTER:
                    print line.split()[:2]


    def check_if_remote_server_is_pinging(self):
        pass

    def add_computer_information_to_data_base(self):
        pass

    def change_computer_name(self):
        pass



def main():
    server = Server()
    print server.receive_information_from_client()
    server.pass_information_to_client('ok')





if __name__ == '__main__':
    main()