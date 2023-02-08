from IPython.external.qt_for_kernel import QtCore
from PySide6.QtGui import QPalette, QImage, QPixmap
from PySide6.QtWidgets import QSizePolicy, QScrollArea, QLabel

from camera import Camera

class Newcamera:
    def __init__(self, camera_url, camera_name):
        self.camera_url = camera_url
        self.camera_name = camera_name

    def add_new_camera(self):
        self.camera = QLabel()
        self.camera.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera.setScaledContents(True)

        self.QScrollArea = QScrollArea()
        self.QScrollArea.setBackgroundRole(QPalette.Dark)
        self.QScrollArea.setWidgetResizable(True)
        self.QScrollArea.setWidget(self.camera)

        self.CaptureIpCameraFramesWorker = Camera(self.camera_url)
        self.CaptureIpCameraFramesWorker.ImageUpdated.connect(lambda image: self.show_camera(image))
        self.CaptureIpCameraFramesWorker.start()

    @QtCore.Slot()
    def show_camera(self, frame: QImage):
        self.camera.setPixmap(QPixmap.fromImage(frame))
