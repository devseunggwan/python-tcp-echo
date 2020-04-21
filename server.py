import socketserver
import sys


class Server(socketserver.BaseRequestHandler):
  # handle에서 서버에서 실행될 작업 작성
    def handle(self):
    print('Client is connected: {0}'.format(self.client_address[0]))
    sock = self.request

    buffer = sock.recv(1024)
    receivedMessage = str(buffer, encoding='utf-8')
    print('Received: {0}'.format(received_message))

    sock.send(buffer)
    sock.close()


if __name__ == '__main__':
    bindIP = '127.0.0.1'  # localhost
    bindPort = 10070

    server = socketserver.TCPServer((bindIP, bindPort), Server)

    print("Start Echo-Server")
    server.serve_forever()  # 요청 대기
