import cv2
import time

from threading import Thread

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage


class Camera(QThread):

    ImageUpdated = Signal(QImage)

    def __init__(self, camera_url):
        super(Camera, self).__init__()

        self.camera_url = camera_url
        self.prev_frame_time = 0
        self.camera_thread = Thread(target=self.run_camera, args=())
        self.camera_thread.daemon = True
        self.fps = 0
        self.true_fps = 0

    def start(self):
        self.camera_thread.start()

    def run_camera(self):
        cap = cv2.VideoCapture(self.camera_url, cv2.CAP_FFMPEG)
        #cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        if cap.isOpened()== True:
            while (cap.isOpened()):
                ret, frame = cap.read()
                self.true_fps = cap.get(cv2.CAP_PROP_FPS)
                self.height, self.width, self.channels = frame.shape
                bytes_per_line = self.height * self.channels

                new_frame_time = time.time()
                try:
                    fps = 1 / (new_frame_time - self.prev_frame_time)
                    self.prev_frame_time = new_frame_time
                except:
                    pass
                self.fps = int(fps)

                time.sleep(fps)

                cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                qt_rgb_image = QImage(cv_rgb_image.data, self.width, self.height, bytes_per_line, QImage.Format_RGB888)

                self.height = str(self.height)
                self.width = str(self.width)

                self.ImageUpdated.emit(qt_rgb_image)

        cap.release()



