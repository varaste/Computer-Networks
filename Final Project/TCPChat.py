import socket,sys

class TCPChat:
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)


    def listen(self,port):     #chat s ok
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.bind(("", port))
        s.listen(1)
        try:
            connection = s.accept()[0]
            connection.settimeout(10)
            connection.sendall("شما متصل شده اید")
        except:
            print("اتصال قطع شد")
        s.close()
        return connection

    # 3way     lets
    def connect(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((ip, int(port.decode("UTF-8"))))
        print("وصل شدن به " + str(ip))
        return s


    def chat(self,MySocket,ip):
        if MySocket != None:
            message=MySocket.recv(1024)
            while message != "end":
               print ("<",ip,">:",message)
               message=input()
               MySocket.sendall(message)
            print("chat ended!")
            MySocket.close()
        else:
            print(str(ip)+": انصراف از اتصال")

