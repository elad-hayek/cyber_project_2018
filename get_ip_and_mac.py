# -*- coding: utf-8 -*-

import sys
ORIGIN_STDOUT = sys.stdout

from scapy.all import *
sys.stdout = ORIGIN_STDOUT

import socket
COMPUTERS_IP = socket.gethostbyname_ex(socket.gethostname())[-1][-1]

MAC_FILTER = ['ff:ff:ff:ff:ff:ff', 'ff:ff:ff:ff:ff:fa']
IP_FILTER = ['192.168.1.1']

IP_ = '192.168.1.'



def main():
    mac_address = sys.argv[1]
    ip_and_macs = []
    for i in range(0, 50):

        answered, unanswered = srp(Ether(dst=mac_address)/ARP(pdst=IP_+str(i)), timeout=0.5, verbose=False)

        if len(answered) > 0:
            if mac_address  == 'ff:ff:ff:ff:ff:ff':
                result = sr(ARP(op=ARP.who_has, psrc=COMPUTERS_IP, pdst=answered[0][0].getlayer(ARP).pdst), verbose=False)
                if answered[0][0].getlayer(ARP).pdst not in IP_FILTER and result[0][0][1].hwsrc not in MAC_FILTER:
                    ip_and_macs.append([answered[0][0].getlayer(ARP).pdst, result[0][0][1].hwsrc])

            else:
                ip_and_macs.append([answered[0][0].getlayer(ARP).pdst, mac_address])

    return_string = ''
    for addr in ip_and_macs:
        return_string += ' '+addr[0]+'$$'+addr[1]
    print return_string

if __name__ == '__main__':
    main()