import socket
import capsule
SIZE = 5
sock = socket.socket()
sock.connect(('localhost',2700))

HEAD = 0x05
addr = 1
seqNo = 1
frame_seq = ""
msg = "hello world"
print("전송 메시지", msg)
for i in range(0,len(msg),SIZE):
    frame_seq += capsule.frame(HEAD,addr,seqNo,msg[i:i+SIZE])
    seqNo+=1
sock.send(frame_seq.encode())
msg = sock.recv(1024).decode()
print("수신",msg)
r_frame = msg.split(chr(0x05))
del r_frame[0]
p_msg = ''
for field in r_frame:
    p_msg += field[10:(11+int(field[6:10]))]
print("복원 메시지:",p_msg)
sock.close()