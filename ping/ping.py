#!/usr/bin/env python
# coding=utf-8

from socket import *
import time


client = socket(AF_INET, SOCK_DGRAM)
port = 9000
host = 'localhost'
client.settimeout(2)

for i in range(10):
    start_time = time.time()
    msg = 'Ping {} {}'.format(i+1, start_time).encode()
    try:
        client.sendto(msg, (host, port))
        recv_msg, add = client.recvfrom(1024)
        all_time = time.time() - start_time
        print('Sequence: {} Reply: {} all_time: {}'.format(i+1, host, all_time))
    except Exception as e:
        print('Sequence: {} Request time out'.format(i+1))

client.close()
