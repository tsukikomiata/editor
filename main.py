from PyQt5.QtWidgets import QApplication, QMainWindow
from edit2 import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.setup)

    def setup(self):
        self.textBrowser.setText(self.plainTextEdit.toPlainText())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
