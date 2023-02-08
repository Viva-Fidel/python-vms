import cv2
import time

from threading import Thread

class Camera:

    list_of_all_cameras = []

    def __init__(self, camera_url, camera_name):
        self.camera_url = camera_url
        self.camera_name = camera_name
        self.prev_frame_time = 0
        self.camera_thread = Thread(target=self.run_camera, args=())
        self.camera_thread.daemon = True

        self.fps = 0
        self.true_fps = 0
        self.height = 0
        self.width = 0

        Camera.list_of_all_cameras.append(self)

    def start(self):
        self.camera_thread.start()

    def run_camera(self):
        cap = cv2.VideoCapture(self.camera_url, cv2.CAP_FFMPEG)
        if cap.isOpened()== True:
            while (cap.isOpened()):
                ret, frame = cap.read()
                self.true_fps = cap.get(cv2.CAP_PROP_FPS)
                self.height = frame.shape[0]
                self.width = frame.shape[1]

                new_frame_time = time.time()
                try:
                    fps = 1 / (new_frame_time - self.prev_frame_time)
                    self.prev_frame_time = new_frame_time
                except:
                    pass
                self.fps = int(fps)

                self.height = str(self.height)
                self.width = str(self.width)

                if time.localtime().tm_sec == 0:
                    self.update_data()

                cv2.imshow("Detector", frame)

                if cv2.waitKey(int((1 / int(self.true_fps)) * 1000)) == ord('q'):
                    break

        cap.release()



