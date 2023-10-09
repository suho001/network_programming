import sys
from socket import *

PORT = 2500
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('',PORT))
s.listen(1)

conn, (remotehost, remortport) = s.accept()

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    data = float(data.decode())
    data = 9.0/5.0*data + 32.0
    data = '{:.1f}'.format(data)
    conn.send(data.encode())

conn.close()