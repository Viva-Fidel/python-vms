import sys
from PySide6 import QtWidgets
import main_window
import asyncio

class Vms(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Vms()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

    # pyside6-uic new_vms.ui > new_vms.py
    # pyside6-rcc git lfs track "*.psd"\media\resources.qrc -o resources.py