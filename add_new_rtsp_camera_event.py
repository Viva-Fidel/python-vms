from PySide6.QtCore import QThread, Slot, QObject
from PySide6.QtGui import QPalette, QImage, QPixmap, Qt
from PySide6.QtWidgets import QSizePolicy, QScrollArea, QLabel, QHBoxLayout, QVBoxLayout

import cv2

from rtsp_camera import Rtsp_camera


class New_rtsp_camera(QObject):
    def __init__(self, camera_url):
        super().__init__()
        self.camera_url = camera_url

    def add_new_camera(self):
        cap = cv2.VideoCapture(self.camera_url, cv2.CAP_FFMPEG)
        if cap.isOpened() == True:
            self.camera = QLabel()
            self.camera.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self.camera.setScaledContents(True)

            self.QScrollArea = QScrollArea()
            self.QScrollArea.setBackgroundRole(QPalette.Dark)
            self.QScrollArea.setWidgetResizable(True)
            self.QScrollArea.setWidget(self.camera)

            self.capture_camera = Rtsp_camera(self.camera_url)
            self.capture_camera.ImageUpdated.connect(self.ShowCamera)
            self.capture_camera.start()
            return self.QScrollArea
        else:
            return False

    @Slot(QImage)
    def ShowCamera(self, frame):
        self.camera.setPixmap(QPixmap.fromImage(frame))