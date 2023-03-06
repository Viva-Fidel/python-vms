import numpy as np
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, Qt

import cv2

from lpr_analytics import Lpr_analytics


class Webcamera(QThread):

    ImageUpdated = Signal(np.ndarray)
    CameraWorking = Signal(bool)

    def  __init__(self, parent=None):
        QThread.__init__(self, parent)

        self.running = True
        self.lpr_analytics = False

    def run(self):
        cap = cv2.VideoCapture(0)

        if self.running == True:
            if cap.isOpened()== True:
                while (cap.isOpened()):
                    ret, frame = cap.read()
                    if ret:
                        if self.lpr_analytics == True:
                            lpr = Lpr_analytics()
                            lpr.run_lpr(frame)
                        #qt_rgb_image_scaled = qt_rgb_image.scaled(1280, 720, Qt.KeepAspectRatio)
                        self.ImageUpdated.emit(frame)
                    else:
                        self.CameraWorking.emit(False)
                        cap.release()
                else:
                    self.CameraWorking.emit(False)
                    cap.release()
            else:
                self.CameraWorking.emit(False)
                cap.release()
        else:
            cap.release()

    def run_lpr(self):
        self.lpr_analytics = True

    def stop_lpr(self):
        self.lpr_analytics = False

    def stop_running(self):
        self.running = False








