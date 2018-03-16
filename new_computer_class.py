# -*- coding: utf-8 -*-

from socket_class import Sockets
from shortcuts import ShortCuts
import _multiprocessing
from subprocess import Popen, PIPE
import re
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
        self.__saved_computer_list = {}
        self.__shortcut_builder = ShortCuts()
        self.__server_socket = Sockets()
        self.__client_socket = Sockets()
        self.__server_socket.open_server(SERVER_IP, CONNECTION_TYPE[connection_type])
        print 'server is up'
        self.connect_to_client()


    def connect_to_client(self):
        self.__client_socket, client_address = self.__server_socket.client_connection()

    def receive_information_from_client(self):
        data = self.__server_socket.read_from_client(self.__client_socket)
        if data[-3:] == '@@@':
            last_argument = data.split('$$')[-1][:-3]
            data = data.split('$$')
            data[-1] = last_argument
            self.activate_the_shortcut_on_the_computer(data)
        else:
            return data.split('$$')

    def pass_information_to_client(self, data):
        self.__server_socket.write_to_client(data, self.__client_socket)

    def get_added_computers_previous_activity(self):
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'r')
        self.__saved_computer_list = pickle.load(json_save_file)

    def save_added_computers_previous_activity(self):
        json_save_file = open(ADDED_COMPUTERS_DATA_FILE_NAME, 'w')
        pickle.dump(self.__saved_computer_list, json_save_file)
        json_save_file.close()

    def make_the_shortcut_file(self, action, sequence, argument):
        self.get_added_computers_previous_activity()
        self.__shortcut_builder.set_users_choice(action)
        self.__shortcut_builder.set_shortcut_sequence(sequence)
        argument = '1$$'+argument  # adds 1$$ so the argument split will work
        self.__shortcut_builder.write_new_shortcut('My Computer', self.__saved_computer_list['My Computer'][1], self.__saved_computer_list['My Computer'][2], argument)
        self.__saved_computer_list['My Computer'][1] = self.__shortcut_builder.get_current_shortcuts()
        self.__saved_computer_list['My Computer'][2] = self.__shortcut_builder.get_file_ending_counter()
        self.save_added_computers_previous_activity()


    def activate_the_shortcut_on_the_computer(self, data):
        action = data[0]
        argument = data[1]
        os.system('python activate_shortcuts.py '+'"'+action+'" "'+argument+'"')

    def disconnect_client(self):
        self.__client_socket.close()

    def close_server(self):
        self.__server_socket.close()





class Client():
    def __init__(self):
        self.__client_socket = Sockets()
        self.__computer_information = {}
        self.__raw_computer_information = []

#-------------------------------------------------------------------------------
    def connect_to_server(self, ip, port):
        try:
            self.__client_socket.connect_to_server(ip, port)
            return True
        except socket.error, e:
            print e
            return False

#-------------------------------------------------------------------------------
    def receive_information_from_the_server(self):
        data = self.__client_socket.read_from_server()
        return data

#-------------------------------------------------------------------------------
    def send_request_to_the_server(self, action, argument, sequence=' '):
        data_to_send = action+'$$'+sequence+'$$'+argument
        self.__client_socket.write_to_server(data_to_send)

#-------------------------------------------------------------------------------
    def activate_the_shortcut_on_the_computer(self, action, argument):
        data_to_send = action+'$$'+argument+'@@@'
        self.__client_socket.write_to_server(data_to_send)

#-------------------------------------------------------------------------------
    def find_computers_in_the_network(self):
        arp_question = Popen(['python', 'get_ip_and_mac.py', BROADCAST], stdout=PIPE)
        result = arp_question.communicate()[0]
        print result
        result = literal_eval(result)  # reverse the repr to dict
        self.__computer_information = copy.deepcopy(result)
        print self.__computer_information

#-------------------------------------------------------------------------------
    def check_if_remote_server_is_on(self, server_ip, connection_type):
        try:
            if self.connect_to_server(server_ip, CONNECTION_TYPE[connection_type]):
                print 'connection was successful'
                return True
            else:
                print 'connection failed'
                return False
        except socket.error, e:
            return False

#-------------------------------------------------------------------------------
    def get_computer_information(self):
        return self.__computer_information

#-------------------------------------------------------------------------------
    def close_client(self):
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