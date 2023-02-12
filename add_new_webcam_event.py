from PySide6.QtCore import QThread, Slot, QObject
from PySide6.QtGui import QPalette, QImage, QPixmap, Qt
from PySide6.QtWidgets import QSizePolicy, QScrollArea, QLabel, QHBoxLayout, QVBoxLayout

import cv2

from webcamera import Webcamera

class New_webcamera(QObject):
    def __init__(self):
        super().__init__()

    def add_new_camera(self):
        cap = cv2.VideoCapture(0)
        if cap.isOpened() == True:
            self.camera = QLabel()
            self.camera.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self.camera.setScaledContents(True)

            self.QScrollArea = QScrollArea()
            self.QScrollArea.setBackgroundRole(QPalette.Dark)
            self.QScrollArea.setWidgetResizable(True)
            self.QScrollArea.setWidget(self.camera)

            self.capture_camera = Webcamera(self)
            self.capture_camera.ImageUpdated.connect(self.ShowCamera)
            self.capture_camera.start()
            print(self.capture_camera.isRunning())
            return self.QScrollArea
        else:
            return False

    @Slot(QImage)
    def ShowCamera(self, frame):
        self.camera.setPixmap(QPixmap.fromImage(frame))