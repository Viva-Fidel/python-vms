from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, Qt

import cv2

class Webcamera(QThread):

    ImageUpdated = Signal(QImage)

    def  __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.prev_frame_time = 0
        self.fps = 0
        self.true_fps = 0
        self.running = True

    def run(self):
        cap = cv2.VideoCapture(0)

        if self.running == True:
            if cap.isOpened()== True:
                while (cap.isOpened()):
                    ret, frame = cap.read()
                    height, width, channels = frame.shape
                    bytes_per_line = width * channels
                    if ret:
                        cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                        #qt_rgb_image_scaled = qt_rgb_image.scaled(1280, 720, Qt.KeepAspectRatio)
                        self.ImageUpdated.emit(qt_rgb_image)

        else:
            cap.release()


                #self.true_fps = cap.get(cv2.CAP_PROP_FPS)
                #self.height, self.width, self.channels = frame.shape
                #bytes_per_line = self.height * self.channels

                #new_frame_time = time.time()
                #try:
                    #fps = 1 / (new_frame_time - self.prev_frame_time)
                    #self.prev_frame_time = new_frame_time
                #except:
                    #pass
                #self.fps = int(fps)

                #time.sleep(fps)

                #cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                #qt_rgb_image = QImage(cv_rgb_image.data, self.width, self.height, bytes_per_line, QImage.Format_RGB888)

                #self.height = str(self.height)
                #self.width = str(self.width)


                #self.ImageUpdated.emit(qt_rgb_image)
    def stop_running(self):
        self.running = False








