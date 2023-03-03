from PySide6 import QtWidgets

import sys

from sqlalchemy.orm import Session

import main_window
from data_base import Cam_list


class Vms(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.expanded = False
        self.setupUi(self)

    def closeEvent(self, event):
        session = Session(main_window.Ui_MainWindow.engine)
        for i in main_window.Ui_MainWindow.left_menu_tree_widget_list:
            if i[1] != None and i[1].camera_type == 'rtsp':
                cameras = session.query(Cam_list).filter_by(cam_id=i[1].unique_id).first()
                if cameras:
                    cameras.cam_name = i[1].rtsp_device_name_lineEdit.text()
                    cameras.cam_link = i[1].rtsp_stream_url_lineEdit.text()
                    cameras.cam_position_in_grid = i[1].current_position_in_grid
                    cameras.cam_status = i[1].camera_status
                    cameras.analytics_status = i[1].analytics_status
                else:
                    cameras = Cam_list(cam_id=i[1].unique_id,
                                       cam_type=i[1].camera_type,
                                       cam_name=i[1].rtsp_left_menu_name.text(),
                                       cam_link=i[1].rtsp_stream_url_lineEdit.text(),
                                       cam_position_in_grid=i[1].current_position_in_grid,
                                       cam_status=i[1].camera_status,
                                       analytics_status=i[1].analytics_status,
                                       )
                    session.add(cameras)
            elif i[1] != None and i[1].camera_type == 'webcam':
                cameras = session.query(Cam_list).filter_by(cam_id=i[1].unique_id).first()
                if cameras:
                    cameras.cam_name = i[1].webcam_device_name_lineEdit.text()
                    cameras.cam_position_in_grid = i[1].current_position_in_grid
                    cameras.cam_status = i[1].camera_status
                    cameras.analytics_status = i[1].analytics_status
                else:
                    cameras = Cam_list(cam_id=i[1].unique_id,
                                       cam_type=i[1].camera_type,
                                       cam_name=i[1].webcam_device_name_lineEdit.text(),
                                       cam_link='0',
                                       cam_position_in_grid=i[1].current_position_in_grid,
                                       cam_status=i[1].camera_status,
                                       analytics_status=i[1].analytics_status,
                                       )

                session.add(cameras)
        session.commit()
        return super().closeEvent(event)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Vms()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

    # pyside6-uic new_vms.ui > new_vms.py
    # pyside6-rcc git lfs track "*.psd"\media\resources.qrc -o resources.py
