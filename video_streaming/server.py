import socket
import threading
import cv2
import numpy as np

# 서버 설정
server_ip = '127.0.0.1'
server_port = 8888

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"서버가 {server_ip}:{server_port}에서 실행 중입니다.")

# 연결된 클라이언트를 저장할 리스트
clients = []

# 비디오 캡처 설정
cap = cv2.VideoCapture(r'C:\Users\user\Videos\Eternal Return  Black Survival\sample_video.mp4')

# 비디오 파일명이나 카메라 디바이스를 지정하세요

# 클라이언트에게 비디오 정보를 전송하는 함수
def send_video_info(client_socket):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 비디오 프레임을 클라이언트에게 전송
        _, frame_encoded = cv2.imencode('.jpg', frame)
        frame_bytes = frame_encoded.tobytes()
        frame_size = len(frame_bytes)

        # 프레임 크기를 먼저 전송
        client_socket.send(str(frame_size).encode('utf-8'))

        # 프레임 데이터를 전송
        client_socket.send(frame_bytes)


# 클라이언트와의 채팅을 처리하는 스레드 함수
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # 클라이언트가 연결을 끊었을 경우
                remove_client(client_socket)
            else:
                # 채팅 메시지를 모든 클라이언트에게 전송
                print(f"받은 메시지: {message}")
                broadcast(message)
        except:
            # 예외 발생 시 클라이언트 연결 종료
            remove_client(client_socket)


# 클라이언트를 리스트에 추가
def add_client(client_socket):
    clients.append(client_socket)


# 클라이언트를 리스트에서 제거
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)


# 모든 클라이언트에게 메시지 전송
def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))


# 클라이언트 연결 대기 및 처리
while True:
    client_socket, client_address = server_socket.accept()
    print(f"새로운 연결 수락: {client_address}")
    add_client(client_socket)

    # 클라이언트에게 비디오 정보를 전송하는 스레드 시작
    video_info_thread = threading.Thread(target=send_video_info, args=(client_socket,))
    video_info_thread.start()

    # 클라이언트 채팅 처리 스레드 시작
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
