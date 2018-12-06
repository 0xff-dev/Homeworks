from socket import *


class ProxyServer(object):

    def __init__(self):
        self.socket_server = socket(AF_INET, SOCK_STREAM)
        self.socket_server.bind(('', 5555))
        self.socket_server.listen(5)
        self.folder = './cache'

    def run(self):
        print('ProxyServer gulu start ...')
        while True:
            client, addr = self.socket_server.accept()
            print('conn from ', addr)
            msg = client.recv(4096).decode()
            print(msg)
            # 注意请求报头的格式
            # GET http://www.baidu.com/ HTTP/1.0
            cache_file_name = '_'.join(msg.split()[1].split('/')[1:]).replace('.','_')
            try:
                with open(self.folder+'/'+cache_file_name, 'r') as fp:
                    for line in fp.readlines():
                        client.send(line.encode())
                    print('Cache aim!!!!')
            except Exception as e:
                print('Cache File not exist.. try to connect host')
                socket_cli = socket(AF_INET, SOCK_STREAM)
                _tmp_data = msg.split()[1].partition('//')
                port  = 80 if _tmp_data[0]=='http:' else 443
                conn_hsot = _tmp_data[2].split('/')[0]
                try:
                    socket_cli.connect((conn_hsot, port))
                    socket_cli.sendall(msg.encode())
                    recv_msg = socket_cli.recv(1024)
                    with open(self.folder+'/'+cache_file_name, 'w') as fp:
                        while recv_msg:
                            client.send(recv_msg)
                            fp.write(recv_msg.encode().strip()+'\n')
                            recv_msg = socket_cli.recv(1024)
                except Exception as e:
                    print('Connect Error {}'.format(e.args))
    def __del__(self):
        self.socket_server.close()


if __name__ == '__main__':
    server = ProxyServer()
    try:
        server.run()
    except KeyboardInterrupt as e:
        del server
