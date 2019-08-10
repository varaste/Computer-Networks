from PyQt5.QtWidgets import QMessageBox
import threading
from UDPBrodcast import listentobroadcast

class ListenPort(threading.Thread):


    def __init__(self,main,PortBroadcast):
        threading.Thread.__init__(self)
        self.main=main
        self.PortBroadcast=PortBroadcast


    def run(self,main):
        # alert = QMessageBox()
        # alert.setText("گوش کردن به پورت%d",self.PortBroadcast)
        # alert.exec_()
        print("گوش کردن به پورت %d",self.PortBroadcast)
        listentobroadcast(self,main)

