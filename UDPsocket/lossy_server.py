from socket import *
import random
port = 2500
BUFFER = 1024
s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening...')

while True:
    data, address = s_sock.recvfrom(BUFFER)
    if random.randint(1, 10) < 4: #30% 데이터 손실
        print('Packet from {} lost!!!'.format(address))
        continue
    print('Message is {!r} from {}'.format(data.decode(), address)) #정상 수신 메시지

    s_sock.sendto('ACK'.encode(), address) #ACK 응답 전송