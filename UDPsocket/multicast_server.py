from socket import *
import struct
group_addr = ("224.0.0.255", 5005) #group address
s_sock = socket(AF_INET, SOCK_DGRAM) #datagram socket 사용
s_sock.settimeout(0.5)
TTL = struct.pack('@i', 2) #TTL=2. 4바이트 정수형으로 표현
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, TTL)
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, False)

while True:
    rmsg = input('Msg :')
    s_sock.sendto(rmsg.encode(), group_addr)

    try:
        response, addr = s_sock.recvfrom(1024)
    except timeout:
        break
    else:
        print('{} from {}'.format(response.decode(), addr)) #응답 출력

