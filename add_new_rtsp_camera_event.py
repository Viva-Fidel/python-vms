from PySide6.QtCore import Slot, QObject, QThread
from PySide6.QtGui import QPalette, QImage, QPixmap
from PySide6.QtWidgets import QSizePolicy, QScrollArea, QLabel

from lpr_analytics import Lpr_analytics
from rtsp_camera import Rtsp_camera

import cv2
import numpy as np


class New_rtsp_camera(QObject):
    def __init__(self, camera_url):
        super().__init__()
        self.camera_url = camera_url
        self.use_lpr = False

    def add_new_camera(self):
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

    @Slot(np.ndarray)
    def ShowCamera(self, frame):

        height, width, channels = frame.shape
        bytes_per_line = width * channels
        cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.camera.setPixmap(QPixmap.fromImage(qt_rgb_image))

    def stop_camera(self):
        self.capture_camera.stop_running()
        self.capture_camera.terminate()


    def run_lpr(self):
        self.capture_camera.run_lpr()

    def __del__(self):
        print("Object is deleted")