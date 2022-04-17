import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))

print('server start at: %s:%s' % (IP, PORT))
print('wait for connection...')

while True:
    data, addr = s.recvfrom(1024)
    print('recvfrom ' + str(addr) + ': ' + data.decode())
