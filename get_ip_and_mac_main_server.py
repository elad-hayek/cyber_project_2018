import os
import re
import socket
import threading

'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'# *..:..:..:..:..:..'
'([a-fA-F0-9]{2}[:|\-]?){6}'

IP_REGEX = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
MAC_REGEX = '([a-fA-F0-9]{2}[:|\-]?){6}'
information_dict = {}
list_counter = 0


def scan_network():
    arp_request = os.system('arp-scan 192.168.1.0/24 > arp_scan.txt')
    with open('arp_scan.txt', 'r') as arp_scan_file:
        data = arp_scan_file.read()
        print(data)
        ip_list = re.findall(IP_REGEX, data)
        mac_finder = re.finditer(MAC_REGEX, data)
        mac_list = list(map(lambda m: m.group(0), mac_finder))
        print(mac_list)
        print(ip_list)
        for entry in ip_list:
            print(entry)
            name_request = os.system('nbtscan '+ entry+' > name_request.txt')
            with open('name_request.txt', 'r') as name_request_file:
                information = name_request_file.read().splitlines()
                global list_counter
                net_bios_name = ip_list[list_counter]
                if len(information) >= 5:
                    information_list = information[4].split()
                    net_bios_name = information_list[1].title()
                    print(information_list)

                information_dict[net_bios_name] = [ip_list[list_counter], mac_list[list_counter]]
                list_counter += 1
    list_counter = 0

    print(information_dict)


def run_network_scan():
    while 1:
        scan_network()

scan_network_thread = threading.Thread(target=run_network_scan)
scan_network_thread.start()

try:
    server = socket.socket()
    server.bind(('0.0.0.0', 8835))
    print('server is up')
    while 1:
        server.listen(1)
        client, addr = server.accept()
        print('connected')
        client.send(repr(information_dict).encode())
        client.close()
except:
    print('error')
    server.close()

