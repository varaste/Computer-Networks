import GUI
import TCPChat
from UDPBrodcast import *
from TCPChat import *
from ListenPort import ListenPort
from PyQt5.QtWidgets import *


class p2p:
    def __init__(self):
        self.Addreses = []
        self.tcp = TCPChat()
        #GUI.OL3()


        self.switcher = {
            "list": self.printaddress,
            "chat": self.startchat
        }

    def addIPAddress(self, address):
        self.Addresses.append(address)

    def printaddress(self):
        i = 1
        output = "{}.{}"
        for address in self.Addresses:
            print(output.format(i, address))
            print("Ip list")

    def startchat(self):
        print("شماره دلخواه وارد کنید")
        # alert2 = QMessageBox()
        # alert2.setText("شماره دلخواه وارد کنید")
        # alert2.exec_()
        address = int(input())
        address = self.Addresses[address]
        port = randint(1100, 8000)
        udpreq(address, port)
        self.tcp.chat(self.tcp.listen(port), address)

    def acceptchat(self, address, port):
        print(str(address) + " آیا این درخواست را میپذیرید؟ (Yes)")
        if input() == "Yes":
            self.tcp.chat(self.tcp.connect(address, port), port)

    def default(self):
        return "-"

    def switch(self, dayOfWeek):
        return self.switcher.get(dayOfWeek, self.default)()

print("سلام :] به برنامه چت ناشناس خوش آمدید.")


#GUI.Welcome()

UDPBroadcast()

#GUI.BroadcastDone()
print("همه پخشی انجام شد")
print("در صورت تمایل برای خروج عبارت Exit را وارد نمائید.")

myp2p = p2p()
listener = ListenPort(myp2p, 25000)
command = ""
while command != "Exit":
    command = input()
    myp2p.switcher.get(command, print(""))
