# time_client.py
import socket #➊ socket 모듈을 불러온다
import time

#➋ TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5700)
sock.connect(address)# ➌ 서버에 연결
while True:
    time.sleep(1)
    print("현재 시각: ", sock.recv(1024).decode())# ➍ 수신 내용을 문자열로 변환하여 출력