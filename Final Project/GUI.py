from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from requests import Session
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton
from threading import Thread
from time import sleep
import sys

def SelectPort():
    SelectP = QApplication([])
    SelectPortBtn = QPushButton("پورت را وارد کنید: ")
    SelectPortBtn.clicked.connect(SelectPortBtn.gettext)
    SelectPortBtn.show()
    SelectP.exec_()


def FSeePresentPeople():
    alert = QMessageBox()
    alert.setText(' شما مشاهده افراد حاضر را انتخاب کردید ')
    alert.exec_()
    print("شما مشاهده افراد حاضر را انتخاب کردید")

    WApp = QApplication([])
    WorkFSeePresentPeople = QStringListModel(["نفر اول", "نفر دوم", "نفر سوم"])
    PresentPeopleViewList = QListView()
    PresentPeopleViewList.setModel(WorkFSeePresentPeople)
    PresentPeopleViewList.show()
    WApp.exec_()


def FStartTheConversation():
    alert = QMessageBox()
    alert.setText(' شما آغاز گفتگو را انتخاب کردید ')
    alert.exec_()
    print("شما آغاز گفتگو را انتخاب کردید")

    name = input("لطفاً نام خود را وارد نمائید: ")
    chat_url = "https://build-system.fman.io/chat"
    server = Session()

    # GUI:
    app = QApplication([])
    text_area = QPlainTextEdit()
    text_area.setFocusPolicy(Qt.NoFocus)
    message = QLineEdit()
    layout = QVBoxLayout()
    layout.addWidget(text_area)
    layout.addWidget(message)
    window = QWidget()
    window.setLayout(layout)
    window.show()

    # Event handlers:
    new_messages = []


    def fetch_new_messages():
        while True:
            response = server.get(chat_url).text
            if response:
                new_messages.append(response)
            sleep(.5)

    thread = Thread(target=fetch_new_messages, daemon=True)
    thread.start()


    def display_new_messages():
        while new_messages:
            text_area.appendPlainText(new_messages.pop(0))


    def send_message():
        server.post(chat_url, {"name": name, "message": message.text()})
        message.clear()

    # Signals:
    message.returnPressed.connect(send_message)
    timer = QTimer()
    timer.timeout.connect(display_new_messages)
    timer.start(1000)
    app.exec_()



def OL3():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    SeePresentPeople = QPushButton(" مشاهده افراد حاضر ")
    StartTheConversation = QPushButton(" آغاز گفتگو ")
    Exit = QPushButton(" خروج ")
    layout.addWidget(SeePresentPeople)
    layout.addWidget(StartTheConversation)
    layout.addWidget(Exit)
    window.setLayout(layout)
    window.show()
    app.exec_()
    SeePresentPeople.show()
    StartTheConversation.show()
    Exit.show()

#*************************************************************#

    #SeePresentPeople.clicked.connect(FSeePresentPeople())
    SeePresentPeople.clicked.connect(print("شما مشاهده افراد حاضر را انتخاب کردید"))

    #StartTheConversation.clicked.connect(FStartTheConversation())
    #SeePresentPeople.clicked.connect(print("شما آغاز گفتگو را انتخاب کردید"))



def Welcome():
    print("سلام :] به برنامه چت ناشناس خوش آمدید.")
    StartWindow = QApplication([])
    StartLabel = QLabel("\n"'. سلام :] به برنامه چت ناشناس خوش آمدید. '"\n")
    StartLabel.show()
    StartWindow.exec_()


def BroadcastDone():
    print("همه پخشی انجام شد")
    BroadcastWindow = QApplication([])
    BroadcastLabel = QLabel("\n"'. همه پخشی انجام شد . '"\n"
                            "\n""در صورت تمایل برای خروج عبارت Exit را وارد نمائید.""\n")
    BroadcastLabel.show()
    BroadcastWindow.exec_()
    print("در صورت تمایل برای خروج عبارت Exit را وارد نمائید.")
