import time

import numpy as np
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtGui import QImage, Qt

import cv2

from lpr_analytics import Lpr_analytics

import asyncio


class Rtsp_camera(QThread):

    ImageUpdated = Signal(np.ndarray)
    CameraWorking = Signal(bool)

    def __init__(self, camera_url):
        super().__init__()
        self.camera_url = camera_url
        self.running = True
        self.lpr_analytics = False
        self.camera_is_working = False

    def run(self):
        cap = cv2.VideoCapture(self.camera_url, cv2.CAP_FFMPEG)
        if self.running == True:
            if cap.isOpened() == True:
                while cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        if self.lpr_analytics == True:
                            lpr = Lpr_analytics()
                            asyncio.run(lpr.run_lpr(frame))
                            #lpr.run_lpr(frame)

                        #qt_rgb_image_scaled = qt_rgb_image.scaled(800, 600, Qt.KeepAspectRatio)
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
