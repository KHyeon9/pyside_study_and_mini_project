import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from hello import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_hi.clicked.connect(self.click)

    def click(self):
        mb_hi = QMessageBox()
        mb_hi.setText("안녕하세요!")
        mb_hi.exec()

        mb_qz = QMessageBox()
        mb_qz.setText("1 + 1?")
        btn_anser_2 = mb_qz.addButton("2", QMessageBox.ActionRole)
        btn_anser_3 = mb_qz.addButton("3", QMessageBox.ActionRole)
        mb_qz.exec()

        if mb_qz.clickedButton() == btn_anser_2:
            mb_success = QMessageBox()
            mb_success.setText("정답입니다.")
            mb_success.exec()

        elif mb_qz.clickedButton() == btn_anser_3:
            mb_fail = QMessageBox()
            mb_fail.setText("오답입니다.")
            mb_fail.exec()


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
