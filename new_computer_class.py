# -*- coding: utf-8 -*-

from socket_class import Sockets
import _multiprocessing

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