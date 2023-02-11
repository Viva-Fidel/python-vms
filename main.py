from PySide6 import QtWidgets

import sys

import main_window

class Vms(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.actual_index = 0
        self.rtsp_index = 1
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