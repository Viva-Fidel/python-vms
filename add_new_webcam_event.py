from PySide6.QtCore import QThread, Slot
from PySide6.QtGui import QPalette, QImage, QPixmap, Qt
from PySide6.QtWidgets import QSizePolicy, QScrollArea, QLabel, QHBoxLayout, QVBoxLayout

import cv2

from webcamera import Webcamera

class New_webcamera:
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

            self.capture_camera = Webcamera()
            self.capture_camera.ImageUpdated.connect(lambda image: self.ShowCamera(image))
            self.capture_camera.start()
            return self.QScrollArea
        else:
            return False

    @Slot()
    def ShowCamera(self, frame: QImage):
        self.camera.setPixmap(QPixmap.fromImage(frame))