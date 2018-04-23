# -*- coding: utf-8 -*-
"""
Description:    The Client and Server classes. has all the necessary actions
                for the client and the server.

name:           Elad Hayek
date:           22.3.18
file name:      new_computer_class.py
"""

from socket_class import Sockets
from shortcuts import ShortCuts
from subprocess import Popen, PIPE
import socket
import os
import pickle
import copy
from ast import literal_eval


MAC_REGULAR_EXPRESSION = '([a-fA-F0-9]{2}[:|\-]?){6}'
IP_REGULAR_EXPRESSION = '192.168.1.(\d){1,3}'
BROADCAST = 'ff:ff:ff:ff:ff:ff'
ADDED_COMPUTERS_DATA_FILE_NAME = 'added_computers_data.json'


SERVER_IP = '0.0.0.0'
SERVER_LISTENING_PORT = 8820
SERVER_ACTING_PORT = 8821
CONNECTION_TYPE = [SERVER_LISTENING_PORT, SERVER_ACTING_PORT]


class Server():
    def __init__(self, connection_type):
        """
        creates a server according to the connection type

        :arg connection_type = acting or listening
        :type connection_type = int
        """
        self.__saved_computer_list = {}
        self.__shortcut_builder = ShortCuts()
        self.__server_socket = Sockets()
        self.__client_socket = Sockets()
        self.__server_socket.open_server(SERVER_IP, CONNECTION_TYPE[
            connection_type])
        print 'server is up'

# -----------------------------------------------------------------------------
    def connect_to_client(self):
        """
        connects to client
        """
        self.__client_socket, client_address =\
            self.__server_socket.client_connection()

# -----------------------------------------------------------------------------
    def receive_information_from_client(self):
        """
        receives data from the client and process it. If it's for the acting
        server it will end in @@@
        """
        data = self.__server_socket.read_from_client(self.__client_socket)
        if data[-3:] == '@@@':
            last_argument = data.split('$$')[-1][:-3]
            data = data.split('$$')
            data[-1] = last_argument
            self.activate_the_shortcut_on_the_computer(data)
        else:
            return data.split('$$')

# -----------------------------------------------------------------------------
    def pass_information_to_client(self, data):
        """
        sends information to the client
        """
        self.__server_socket.write_to_client(data, self.__client_socket)

# -----------------------------------------------------------------------------
    def get_added_computers_previous_activity(self):
        """
        extracts data from the data file
        """
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'r')
        self.__saved_computer_list = pickle.load(json_save_file)

# -----------------------------------------------------------------------------
    def save_added_computers_previous_activity(self):
        """
        saves data to the data file
        """
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'w')
        pickle.dump(self.__saved_computer_list, json_save_file)
        json_save_file.close()

# -----------------------------------------------------------------------------
    def make_the_shortcut_file(self, action, sequence, argument):
        """
        creates the remote shortcut locally

        :arg action = the remote action
        :type action = string

        :arg sequence = the remote sequence
        :type sequence = string

        :arg argument = the remote argument
        :type argument = string
        """
        self.get_added_computers_previous_activity()
        self.__shortcut_builder.set_users_choice(action)
        self.__shortcut_builder.set_shortcut_sequence(sequence)
        argument = '1$$'+argument  # adds 1$$ so the argument split will work
        self.__shortcut_builder.write_new_shortcut(
            'My Computer', self.__saved_computer_list['My Computer'][1],
            self.__saved_computer_list['My Computer'][2], argument)
        self.__saved_computer_list['My Computer'][1] =\
            self.__shortcut_builder.get_current_shortcuts()
        self.__saved_computer_list['My Computer'][2] =\
            self.__shortcut_builder.get_file_ending_counter()
        self.save_added_computers_previous_activity()

# -----------------------------------------------------------------------------
    def activate_the_shortcut_on_the_computer(self, data):
        """
        actives the remote shortcut on the computer when the acting server gets
        an order

        :arg data = the remote shortcut data
        :type data = string
        """
        action = data[0]
        argument = data[1]
        os.system(
            'python activate_shortcuts.py '+'"'+action+'" "'+argument+'"')

# -----------------------------------------------------------------------------
    def disconnect_client(self):
        """
        disconnects the client form the server
        """
        self.__client_socket.close()

# -----------------------------------------------------------------------------
    def close_server(self):
        """
        closes the server
        """
        self.__server_socket.close()


class Client():
    def __init__(self):
        """
        creates a client
        """
        self.__client_socket = Sockets()
        self.__computer_information = {}
        self.__raw_computer_information = []

# -----------------------------------------------------------------------------
    def connect_to_server(self, ip, port):
        """
        connects to the server

        :arg ip = the server's ip
        :type ip = string

        :arg port = the server's port
        :type port = int
        """
        try:
            self.__client_socket.connect_to_server(ip, port)
            return True
        except socket.error, e:
            print e
            return False

# -----------------------------------------------------------------------------
    def receive_information_from_the_server(self):
        """
        receives information from the server
        """
        data = self.__client_socket.read_from_server()
        return data

# -----------------------------------------------------------------------------
    def send_request_to_the_server(self, action, argument, sequence=' '):
        """
        sends a create new shortcut information
        """
        data_to_send = action+'$$'+sequence+'$$'+argument
        self.__client_socket.write_to_server(data_to_send)

# -----------------------------------------------------------------------------
    def activate_the_shortcut_on_the_computer(self, action, argument):
        """
        sends a activate shortcut information
        """
        data_to_send = action+'$$'+argument+'@@@'
        self.__client_socket.write_to_server(data_to_send)

# -----------------------------------------------------------------------------
    def find_computers_in_the_network(self):
        """
        finds all of the responsive computers on the network
        """
        arp_question = Popen(['python', 'get_ip_and_mac.py', BROADCAST],
                             stdout=PIPE)
        result = arp_question.communicate()[0]
        print result
        result = literal_eval(result)  # reverse the repr to dict
        self.__computer_information = copy.deepcopy(result)
        print self.__computer_information

# -----------------------------------------------------------------------------
    def check_if_remote_server_is_on(self, server_ip, connection_type):
        """
        checks if the remote server is on

        :arg server_ip = the server's ip
        :type server_ip = string

        :arg connection_type = the server type
        :type connection_type = int
        """
        try:
            if self.connect_to_server(server_ip, CONNECTION_TYPE[
                    connection_type]):
                print 'connection was successful'
                return True
            else:
                print 'connection failed'
                return False
        except socket.error:
            return False

# -----------------------------------------------------------------------------
    def get_computer_information(self):
        """
        returns the computer information from the main server
        """
        return self.__computer_information

# -----------------------------------------------------------------------------
    def close_client(self):
        """
        closes the client
        """
        self.__client_socket.close()


def main():
    # client = Client()
    # client.find_computers_in_the_network()
    # if client.check_if_remote_server_is_on('192.168.1.46'):
    #     client.send_request_to_the_server('open', 'a+f', 'google.com')
    #     print client.receive_information_from_the_server()

    n = 0
    while 1:
        server = Server(n)
        a = server.receive_information_from_client()
        print a
        server.pass_information_to_client('ok')
        if n == 0:
            server.make_the_shortcut_file(a[0], a[1], a[2])
        server.disconnect_client()
        server.close_server()


if __name__ == '__main__':
    main()
