
import random
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import QTimer
# from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    last_read = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.model = QStandardItemModel()
        # self.ui.list_chat.setModel(self.model)

        self.ui.btn_send.clicked.connect(self.send)
        self.ui.edit_text.returnPressed.connect(self.send)

        nick_name = self.random_nickname()
        self.ui.edit_nickname.setText(nick_name)

        with open("./server.text", "a+", encoding="utf-8") as f:
            f.writelines(f"-------{nick_name}님이 입장하였습니다.-------\n")

        self.listen()

        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.listen)
        self.timer.start()

    def send(self):
        nick_name = self.ui.edit_nickname.text()
        text = self.ui.edit_text.text()
        # item = QStandardItem(text)
        # self.model.appendRow(item)
        msg = f"{nick_name}: {text}"

        # 파일에 msg를 쓴다.
        with open("./server.text", "a+", encoding="utf-8") as f:
            f.writelines(msg + "\n")

        self.ui.edit_text.clear()

    def random_nickname(self):
        nick_name = random.choice(["홍길동", "황장수", "김비서"])
        num = random.randint(1, 1000)
        return f"{nick_name}{num}"

    def listen(self):
        try:
            with open("./server.text", "r", encoding="utf-8") as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            self.ui.list_chat.addItems(lines[self.last_read:])
            self.last_read = len(lines)
            self.ui.list_chat.scrollToBottom()
        except:
            pass


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
