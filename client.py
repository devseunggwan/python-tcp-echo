import socket
import sys

serverPort = 10070

if __name__ == "__main__":
    bindIP = '127.0.0.1'  # localhost
    serverIP = '127.0.0.1'  # localhost
    message = sys.argv[1]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 객체 생성
    sock.bind((bindIP, 0))  # 바인딩

    try:
        sock.connect((serverIP, serverPort))  # 소켓 연결

        buffer = bytes(message, encoding='utf-8')
        sock.send(buffer)  # 메시지 전송

        print('Sended message: {0}'.format(message))

        buffer = sock.recv(1024)  # echo
        receivedMessage = str(buffer, encoding='utf-8')
        print('Received message: {0}'.format(receivedMessage))

    finally:
        sock.close()
