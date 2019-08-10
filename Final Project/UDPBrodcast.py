import socket
from random import randint


def UDPBroadcast():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(3)
    server.bind(("", 30000))
    message = b"hello"
    server.sendto(message, ('<broadcast>', 25000))
    try:
        data, addr = server.recvfrom(1024)
        return int(data.decode("UTF-8"))
    except:
        print("")


# '''Hello'''

def udpreq(address, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    client.sendto(bytes(str(port), "UTF-8"), (address, 25000))


def portfinder():
    result = 0
    while result == 0:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r = randint(1100, 8000)
        result = sock.connect_ex(("", r))
        if result == 1:
            sock.close()
            return r


def listentobroadcast(self, main):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 25000))
    client.settimeout(None)
    while 1:
        data, addr = client.recvfrom(1024)
        if data.decode("UTF-8") == "broadcast":
            main.addIPAddress(addr[0])
        else:
            main.acceptchat(addr[0], data.decode("UTF-8"))
