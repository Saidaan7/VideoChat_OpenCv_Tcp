import socket
import threading
import time

#Socket for User A receive data from server
a_recv_ser =socket.socket()
a_recv_ser.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

# Socket for User B receive data from server
b_recv_ser =socket.socket()
b_recv_ser.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

# Socket for User A send data to server
a_send_ser =socket.socket()
a_send_ser.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

# Socket for User B send to server
b_send_ser =socket.socket()
b_send_ser.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#sendport of user A
a_recv_port=1111

#recvport of user A
a_send_port=2222

#sendport of user B
b_recv_port=3333

#recvport of User B
b_send_port=4444

#By default server ip assigned
ip=""


a_recv_ser.bind((ip, a_recv_port))
b_recv_ser.bind((ip, b_recv_port))
a_send_ser.bind((ip, a_send_port))
b_send_ser.bind((ip, b_send_port))

a_recv_ser.listen()
b_recv_ser.listen()
a_send_ser.listen()
b_send_ser.listen()

print("Waiting For Users...")
a_recv_session, a_recv_addr = a_recv_ser.accept()
print("A_recv_session<<<")
b_recv_session, b_recv_addr = b_recv_ser.accept()
print("B_recv_session<<<")
a_send_session, a_send_addr = a_send_ser.accept()
print("A_send_session>>>")
b_send_session, b_send_addr = b_send_ser.accept()
print("B_send_session<<<")


def ser_recv_a_send_b():
    while True:
        data=a_recv_session.recv(100000000)
        print("User A: ", data)
        time.sleep(0.2)
        b_send_session.send(data)


def ser_recv_b_send_a():
    while True:
        data=b_recv_session.recv(100000000)
        print("User B:", data)
        time.sleep(0.2)
        a_send_session.send(data)

t1=threading.Thread(target=ser_recv_a_send_b)
t2=threading.Thread(target=ser_recv_b_send_a)
t1.start()
t2.start()