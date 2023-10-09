# time_server.py
import socket# ➊ socket 모듈을 불러온다
import time

#➋ TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5700) #''=임의 주소, 포트 번호=5000
s.bind(address)# ➌ 소켓과 주소 결합
s.listen(5)# ➍ 연결 대기. 5개까지 동시 수용

client, addr = s.accept()# ➎ 연결 허용. (client socket, rem_addr) 반환

while True:
    # client, addr = s.accept()# ➎ 연결 허용. (client socket, rem_addr) 반환
    print("Connection requested from ", addr)
    if client:
        time.sleep(1)
        client.send(time.ctime(time.time()).encode())# ➏ 현재 시간을 전송
    # client.close()# ➐ 소켓 종료