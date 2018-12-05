#!/usr/bin/env python
# coding=utf-8

import socket

from urllib.parse import urlparse
from http.server import HTTPServer,  BaseHTTPRequestHandler


class ProxyHandler(BaseException):
    """
    参考链接:
    https://zhuanlan.zhihu.com/p/28737960
    https://docs.python.org/3/library/http.server.html
    """
    def _recv_proxy_data(self, socket_client: socket.socket):
        data = b''
        while True:
            recv = socket_client.recv(1024)
            if recv:
                data += recv
            else:
                break
        socket_client.close()
        return data

    def do_GET(self):
        uri = urlparse(self.path)
        scheme, host, path = uri.scheme, uri.netloc, uri.path
        host_id = socket.gethostbyname(host)
        port = 443 if scheme == 'https' else 80

        data = 'GET {} {}\r\n'.format(path, self.protocol_version)
        for k, v in self.headers.items():
            data += '{}: {}\r\n'.format(k, v)
        data += '\r\n'

        with open('./res.txt', 'a') as fp:
            fp.write(data)
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((host, port))
        socket_client.sendall(data.encode('utf-8'))
        recv_res_data = self._recv_proxy_data(socket_client)
        self.wfile.write(recv_res_data)


def main():
    try:
        server = HTTPServer(('', 6789), ProxyHandler)
        server.serve_forever()
    except KeyboardInterrupt as e:
        server.socket.close()


if __name__ == '__main__':
    main()
