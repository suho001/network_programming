import socket
import sys

port = 2600
# 서버 소켓 생성
s_sock = socket.socket()
host = ''
s_sock.bind((host,port))
s_sock.listen(1)

print("Waiting for Connection")
#클라이언트 연결 대기
c_sock, addr = s_sock.accept()
print("connection from", addr)

#클라이언트로부터 메시지 수신 및 출력
msg = c_sock.recv(1024)
print(msg.decode())

#파일 이름을 입력받기
filename = input("파일 이름")
#클라이언트 에게 파일 이름 전송
c_sock.send(filename.encode())
#파일 열어서 전송
with open("./dummy/"+filename, 'rb') as f:
    c_sock.sendfile(f,0)

print('sending complete')
c_sock.close()