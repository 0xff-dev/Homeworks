import random
from socket import *


server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 9000))
while True:
    msg, add = server.recvfrom(1024)
    msg = msg.upper()
    rand = random.randint(0, 10)
    if rand < 4:
        continue
    server.sendto(msg, add)
