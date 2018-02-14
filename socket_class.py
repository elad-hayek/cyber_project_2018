# -*- coding: utf-8 -*-
"""
Description:     Menages the socket functionality of the program
Author:          Elad Hayek
FileName:        socket_class.py
Date:            27.5.17
Version:         1.0
"""

from socket import socket


class Sockets(socket):
    def __init__(self):
        """
        creates a new socket
        """
        super(Sockets, self).__init__()

    def connect_to_server(self, ip, port):
        """
        connects to a server
        :arg ip = the server's ip
        :type ip = string
        :arg port = the server's port
        :type = int
        """
        self.connect((ip, port))

    def write_to_server(self, data):
        """
        sends data to the server
        :arg data = the data to send
        :type data = string
        """
        self.send(data)

    def write_to_client(self, data,  client_socket):
        """
        sends data to the client
        :arg data = the data to send
        :type data = string
        :arg client_socket = the client's socket
        :type client_socket = socket
        """
        client_socket.send(data)

    def read_from_server(self):
        """
        receive data from the server and return it
        """
        data = self.recv(1024)
        return data

    def read_from_client(self, client_socket):
        """
        receive data from the client and returns it
        :arg client_socket = the client's socket
        :type client_socket = socket
        """
        data = client_socket.recv(1024)
        return data

    def open_server(self, ip, port):
        """
        binds the server to an ip and port
        :arg ip = the ip to bind to
        :type ip = string
        :arg port = the port to bind to
        :type port = int
        """
        self.bind((ip, port))

    def client_connection(self):
        """
        connects to a client and returns its socket and address
        """
        self.listen(1)
        (client_socket, client_address) = self.accept()
        return client_socket, client_address

    def close_socket(self):
        """
        closes the socket
        """
        self.close()