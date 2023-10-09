import socket
import cv2
import pickle
import struct
import imutils

#소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9100
server_addr = ('',port)
#주소와 포트번호 바인드
server_socket.bind(server_addr)
#접속대기
server_socket.listen(5)
print("접속대기",server_addr)
#클라이언트 연결
while True:
    client_socket, addr = server_socket.accept()
    print(addr,'와 연결됨')
    if client_socket:
        vid = cv2.VideoCapture(0) # 웹캠 연결
        if vid.isOpened():
            print(vid.get(3),vid.get(4))
        while vid.isOpened():
            img, frame = vid.read() #프레임 획득
            frame = imutils.resize(frame,width=640) #프레임 크기 조절
            frame_bytes = pickle.dumps(frame) #프레임을 바이트 스트림으로 변환
            msg = struct.pack("Q",len(frame_bytes)) + frame_bytes
            # 메시지 Q unsigned long long d으로 보낼 데이터 크기 전송
            client_socket.sendall(msg)

            cv2.imshow('s',frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()