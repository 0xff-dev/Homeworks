from socket import *


class SocketServer(object):

    def __init__(self, port: int=9999):
        self.socket_server = socket(AF_INET, SOCK_STREAM)
        self.socket_server.bind(('', port))
        self.socket_server.listen(1)

    def run(self):
        print('Server Start ...')
        while True:
            connect, addr = self.socket_server.accept()
            print('Client: ', connect, ' ', addr)
            try:
                msg = connect.recv(1024)
                file_name = msg.split()[1]
                f = open(file_name[1:])
                header = ' HTTP/1.1 200 OK\r\nConnection: close\r\n'+\
                         'Content-Type: text/html\r\nContent-Length: '+\
                         '%d\n\n' % (len(f.read()))
                connect.send(header.encode(encoding='utf-8'))
                for line in f.readlines():
                    connect.send(line.encode('utf-8'))
                connect.close()
            except IOError as e:
                print(e.args)
                header = 'HTTP/1.1 404 Not Found'
                connect.send(header.encode('utf-8'))
                connect.close()

    def __del__(self):
        self.socket_server.close()

server = SocketServer()
server.run()