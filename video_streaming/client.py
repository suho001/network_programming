import socket
import threading
import cv2
import numpy as np

# 서버 설정
server_ip = '127.0.0.1'
server_port = 8888

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))


# 서버로부터 비디오 정보를 받는 함수
def receive_video():
    while True:
        try:
            # 프레임 크기 수신
            frame_size = int(client_socket.recv(10).decode('utf-8'))

            # 프레임 데이터 수신
            frame_data = b''
            remaining_size = frame_size
            while remaining_size > 0:
                chunk = client_socket.recv(remaining_size)
                if not chunk:
                    break
                frame_data += chunk
                remaining_size -= len(chunk)

            # 수신한 데이터를 이미지로 디코딩
            frame_array = np.frombuffer(frame_data, dtype=np.uint8)
            frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)

            # 화면에 비디오 프레임 표시
            cv2.imshow('Video', frame)
            cv2.waitKey(1)  # 1ms 대기 후 다음 프레임 표시
        except:
            # 예외 발생 시 연결 종료
            client_socket.close()
            break


# 메시지 전송 함수
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


# 채팅 수신 함수
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # 예외 발생 시 연결 종료
            client_socket.close()
            break


# 비디오 수신 스레드 시작
video_receive_thread = threading.Thread(target=receive_video)
video_receive_thread.start()

# 클라이언트 채팅 수신 및 전송 스레드 시작
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)
receive_thread.start()
send_thread.start()
