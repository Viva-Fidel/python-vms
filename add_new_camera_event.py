from PySide6.QtCore import QThread, Slot
from PySide6.QtGui import QPalette, QImage, QPixmap, Qt
from PySide6.QtWidgets import QSizePolicy, QScrollArea, QLabel, QHBoxLayout, QVBoxLayout

from camera import Camera

class Newcamera:
    def __init__(self, camera_url):
        super().__init__()
        self.camera_url = camera_url

    def add_new_camera(self):
        self.camera = QLabel()
        self.camera.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera.setScaledContents(True)

        self.QScrollArea = QScrollArea()
        self.QScrollArea.setBackgroundRole(QPalette.Dark)
        self.QScrollArea.setWidgetResizable(True)
        self.QScrollArea.setWidget(self.camera)

        self.capture_camera = Camera(self.camera_url)
        self.capture_camera.ImageUpdated.connect(lambda image: self.ShowCamera(image))
        self.capture_camera.start()
        return self.QScrollArea

    @Slot()
    def ShowCamera(self, frame: QImage):
        self.camera.setPixmap(QPixmap.fromImage(frame))