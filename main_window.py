# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import numpy as np
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QTimer, QUrl, Qt, Slot, QThread, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLayout, QListView,
                               QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
                               QVBoxLayout, QWidget, QDialog, QGridLayout, QLabel, QScrollArea, QDialogButtonBox,
                               QCheckBox, QLineEdit, QSpinBox, QTreeView, QFrame, QTreeWidget, QTreeWidgetItem)
from PySide6 import QtCore

import GPUtil
import psutil

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from add_new_camera_dialog import Ui_Add_new_cam_dialog
from add_new_rtsp_camera_event import New_rtsp_camera
from add_new_webcam_event import New_webcamera

import resources

class Ui_MainWindow(object):

    # All possible positions in grid
    camera_position_in_grid = {
        (0, 0): None,
        (0, 1): None,
        (0, 2): None,
        (1, 0): None,
        (1, 1): None,
        (1, 2): None,
        (2, 0): None,
        (2, 1): None,
        (2, 2): None
    }

    # All possible tree widget
    tree_widget_list = {
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None
    }

    # Current position of user in menu
    user_current_position = 0


    def __init__(self):
        super().__init__()
        self.actual_index = 0
        self.rtsp_index = 1

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.left_menu_treeWidget = QTreeWidget(self.centralwidget)
        self.left_menu_treeWidget.setObjectName(u"left_menu_treeView")
        self.left_menu_treeWidget.setGeometry(QRect(10, 1, 111, 591))
        self.left_menu_treeWidget.setHeaderHidden(True)
        self.main_window_stackedWidget = QStackedWidget(self.centralwidget)
        self.main_window_stackedWidget.setObjectName(u"main_window_stackedWidget")
        self.main_window_stackedWidget.setGeometry(QRect(130, 0, 661, 591))
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.software_version_label = QLabel(self.dashboard_page)
        self.software_version_label.setObjectName(u"software_version_label")
        self.software_version_label.setGeometry(QRect(10, 10, 131, 16))
        self.system_parameters_frame = QFrame(self.dashboard_page)
        self.system_parameters_frame.setObjectName(u"system_parameters_frame")
        self.system_parameters_frame.setGeometry(QRect(9, 70, 241, 81))
        self.system_parameters_frame.setFrameShape(QFrame.StyledPanel)
        self.system_parameters_frame.setFrameShadow(QFrame.Raised)
        self.cpu_load_label = QLabel(self.system_parameters_frame)
        self.cpu_load_label.setObjectName(u"cpu_load_label")
        self.cpu_load_label.setGeometry(QRect(0, 10, 71, 16))
        self.ram_load_label = QLabel(self.system_parameters_frame)
        self.ram_load_label.setObjectName(u"ram_load_label")
        self.ram_load_label.setGeometry(QRect(0, 30, 71, 16))
        self.gpu_load_label = QLabel(self.system_parameters_frame)
        self.gpu_load_label.setObjectName(u"gpu_load_label")
        self.gpu_load_label.setGeometry(QRect(0, 50, 71, 16))
        self.cpu_load_info_label = QLabel(self.system_parameters_frame)
        self.cpu_load_info_label.setObjectName(u"cpu_load_info_label")
        self.cpu_load_info_label.setGeometry(QRect(80, 10, 47, 13))
        self.ram_load_info_label = QLabel(self.system_parameters_frame)
        self.ram_load_info_label.setObjectName(u"ram_load_info_label")
        self.ram_load_info_label.setGeometry(QRect(80, 30, 47, 13))
        self.gpu_load_info_label = QLabel(self.system_parameters_frame)
        self.gpu_load_info_label.setObjectName(u"gpu_load_info_label")
        self.gpu_load_info_label.setGeometry(QRect(80, 50, 47, 13))
        self.system_parameters_label = QLabel(self.dashboard_page)
        self.system_parameters_label.setObjectName(u"system_parameters_label")
        self.system_parameters_label.setGeometry(QRect(10, 50, 111, 16))
        self.main_window_stackedWidget.addWidget(self.dashboard_page)
        self.cameras_page = QWidget()
        self.cameras_page.setObjectName(u"cameras_page")
        self.cameras_page_gridLayoutWidget = QWidget(self.cameras_page)
        self.cameras_page_gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.cameras_page_gridLayoutWidget.setGeometry(QRect(0, 0, 661, 591))
        self.cameras_page_gridLayout = QGridLayout(self.cameras_page_gridLayoutWidget)
        self.cameras_page_gridLayout.setSpacing(0)
        self.cameras_page_gridLayout.setObjectName(u"cameras_gridLayout")
        self.cameras_page_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_window_stackedWidget.addWidget(self.cameras_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.add_new_camera_pushButton = QPushButton(self.settings_page)
        self.add_new_camera_pushButton.setObjectName(u"add_camera_pushButton")
        self.add_new_camera_pushButton.setGeometry(QRect(0, 560, 75, 23))
        self.main_window_stackedWidget.addWidget(self.settings_page)

        "____________________________________________________"
        # Tree model menu

        self.dashboard = QTreeWidgetItem(self.left_menu_treeWidget)
        self.dashboard.setText(0, 'Dashboard')
        dashboard_icon = QIcon()
        dashboard_icon.addFile(u":/media/icons/dashboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard.setIcon(0, dashboard_icon)
        self.dashboard.setData(0, Qt.UserRole, self.actual_index)

        self.actual_index += 1
        self.cameras = QTreeWidgetItem(self.left_menu_treeWidget)
        self.cameras.setText(0, 'Cameras')
        cameras_icon = QIcon()
        cameras_icon.addFile(u":/media/icons/cameras.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameras.setIcon(0, cameras_icon)
        self.cameras.setData(0, Qt.UserRole, self.actual_index)

        self.actual_index += 1
        self.settings = QTreeWidgetItem(self.left_menu_treeWidget)
        self.settings.setText(0, 'Settings')
        settings_icon = QIcon()
        settings_icon.addFile(u":/media/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(0, settings_icon)
        self.settings.setData(0, Qt.UserRole, self.actual_index)

        "____________________________________________________"
        # Switch user position

        self.left_menu_treeWidget.itemClicked.connect(self.left_menu_clicked)

        "____________________________________________________"
        # Dashboard timer

        dashboard_timer = QTimer(self, interval=1000, timeout=self.update_dashboard)
        dashboard_timer.start()

        "____________________________________________________"
        # Dialog to add new cameras

        self.add_new_camera_pushButton.clicked.connect(self.add_new_cam_dialog)

        "____________________________________________________"


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Camera obscura VMS", None))
        self.software_version_label.setText(QCoreApplication.translate("MainWindow", u"Software version: 0.01a", None))
        self.cpu_load_label.setText(QCoreApplication.translate("MainWindow", u"CPU load:", None))
        self.ram_load_label.setText(QCoreApplication.translate("MainWindow", u"RAM load:", None))
        self.gpu_load_label.setText(QCoreApplication.translate("MainWindow", u"GPU load:", None))
        self.cpu_load_info_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ram_load_info_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gpu_load_info_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.system_parameters_label.setText(QCoreApplication.translate("MainWindow", u"System parameters:", None))
        self.add_new_camera_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add camera", None))
    # retranslateUi

    "____________________________________________________"
    # Function to update dashboard page
    def update_dashboard(self):
        self.cpu_load_info_label.setText(str(psutil.cpu_percent(interval=None))) # Update CPU
        self.ram_load_info_label.setText(str(psutil.virtual_memory().percent)) # Update RAM
        self.gpu_load_info_label.setText((str(GPUtil.getGPUs()[0].load))) # Update GPU

    "____________________________________________________"

    #Slot to get information what position in menu was chosen
    @Slot(QTreeWidgetItem, int)
    def left_menu_clicked(self, item, col):
        print(item, col, item.text(col))
        if item.data(col, Qt.UserRole) is not None:
            Ui_MainWindow.user_current_position = item.data(col, Qt.UserRole) # Store current position
            print(item.data(col, Qt.UserRole))
            self.main_window_stackedWidget.setCurrentIndex(item.data(col, Qt.UserRole))

    "____________________________________________________"

    # Slot to add new camera to gridLayout
    @Slot(QObject, QWidget, int, int)
    def add_cameras_page_gridLayout(self, camera_func, x_pos, y_pos):
        self.cameras_page_gridLayout.addWidget(camera_func, x_pos, y_pos)

    "____________________________________________________"

    # Slot to delete camera in gridLayout
    @Slot(QWidget)
    def delete_cameras_page_gridLayout(self, camera_func):
            camera_func.deleteLater()

    "____________________________________________________"

    # Slot to totally delete page from menu
    @Slot(int)
    def delete_qtree_item(self, qtree_child_index):
        self.settings.removeChild(Ui_MainWindow.tree_widget_list[qtree_child_index])
        self.main_window_stackedWidget.setCurrentIndex(qtree_child_index-1)
        Ui_MainWindow.tree_widget_list[qtree_child_index] = None

    "____________________________________________________"

    # Function to call a dialog and add new camera
    def add_new_cam_dialog(self):
        Dialog = QDialog()
        adding_new_cam = Ui_Add_new_cam_dialog()
        adding_new_cam.setupUi(Dialog)
        Dialog.show()
        Dialog.exec()
        if adding_new_cam.choice_value == 'rtsp':
            self.rtsp = QTreeWidgetItem(self.settings)
            if self.rtsp_index == 1: # Need to set up logic for it!!!!!!!!!!!!!!!!!!!!!!!
                self.rtsp_name = 'RTSP'
                self.rtsp.setText(0, self.rtsp_name)
                self.rtsp_index += 1
            else:
                self.rtsp_name = f'RTSP {self.rtsp_index}'
                self.rtsp.setText(0, self.rtsp_name)
                self.rtsp_index += 1

            for k, v in Ui_MainWindow.tree_widget_list.items():
                if v == None:
                    self.actual_index = k
                    Ui_MainWindow.tree_widget_list[k] = self.rtsp
                    break

            self.rtsp.setData(0, Qt.UserRole, self.actual_index)
            self.rtsp_page = Rtsp_page(self.actual_index, self.rtsp_name, self.rtsp)
            self.rtsp_page.rtsp_update_main_gui_add.connect(self.add_cameras_page_gridLayout)
            self.rtsp_page.rtsp_update_main_gui_delete.connect(self.delete_cameras_page_gridLayout)
            self.rtsp_page.rtsp_delete_page.connect(self.delete_qtree_item)
            self.main_window_stackedWidget.addWidget(self.rtsp_page.setupGUi())

        elif adding_new_cam.choice_value == 'webcam':
            self.webcam = QTreeWidgetItem(self.settings)
            self.webcam_name = 'Webcam'
            self.webcam.setText(0, self.webcam_name)

            for k, v in Ui_MainWindow.tree_widget_list.items():
                if v == None:
                    self.actual_index = k
                    Ui_MainWindow.tree_widget_list[k] = self.webcam
                    break

            self.webcam.setData(0, Qt.UserRole, self.actual_index)
            self.webcam_page = Webcam_page(self.actual_index, self.webcam_name, self.webcam)
            self.webcam_page.webcam_update_main_gui.connect(self.add_cameras_page_gridLayout)
            self.webcam_page.webcam_update_main_gui_delete.connect(self.delete_cameras_page_gridLayout)
            self.webcam_page.webcam_delete_page.connect(self.delete_qtree_item)
            self.main_window_stackedWidget.addWidget(self.webcam_page.setupGUi())

"____________________________________________________"

# Class to add a camera using RTSP
class Rtsp_page(QObject):
    rtsp_update_main_gui_add = Signal(QWidget, int, int)
    rtsp_update_main_gui_delete = Signal(QWidget)
    rtsp_delete_page = Signal(int)

    def __init__(self, actual_index, rtsp_name, rtsp_left_menu_name):
        super().__init__()

        self.actual_index = actual_index
        self.rtsp_name = rtsp_name
        self.rtsp_left_menu_name = rtsp_left_menu_name
        self.status = False

    def setupGUi(self):
        self.rtsp_page = QWidget()
        self.rtsp_page.setObjectName(u"rtsp_page")
        self.rtsp_device_name_label = QLabel(self.rtsp_page)
        self.rtsp_device_name_label.setObjectName(u"rtsp_device_name_label")
        self.rtsp_device_name_label.setGeometry(QRect(10, 10, 71, 16))
        self.rtsp_device_name_lineEdit = QLineEdit(self.rtsp_page)
        self.rtsp_device_name_lineEdit.setObjectName(u"rtsp_device_name_lineEdit")
        self.rtsp_device_name_lineEdit.setGeometry(QRect(10, 30, 221, 20))
        self.rtsp_stream_url_label = QLabel(self.rtsp_page)
        self.rtsp_stream_url_label.setObjectName(u"rtsp_stream_url_label")
        self.rtsp_stream_url_label.setGeometry(QRect(10, 50, 71, 16))
        self.rtsp_stream_url_lineEdit = QLineEdit(self.rtsp_page)
        self.rtsp_stream_url_lineEdit.setObjectName(u"rtsp_stream_url_lineEdit")
        self.rtsp_stream_url_lineEdit.setGeometry(QRect(10, 70, 221, 20))
        self.rtsp_enable_pushButton = QPushButton(self.rtsp_page)
        self.rtsp_enable_pushButton.setObjectName(u"rtsp_enable_pushButton")
        self.rtsp_enable_pushButton.setGeometry(QRect(10, 120, 75, 23))
        self.rtsp_delete_pushButton = QPushButton(self.rtsp_page)
        self.rtsp_delete_pushButton.setObjectName(u"rtsp_delete_pushButton")
        self.rtsp_delete_pushButton.setGeometry(QRect(90, 120, 75, 23))
        self.rtsp_status_label = QLabel(self.rtsp_page)
        self.rtsp_status_label.setObjectName(u"rtsp_status_label")
        self.rtsp_status_label.setGeometry(QRect(10, 100, 47, 13))
        self.rtsp_actual_status_label = QLabel(self.rtsp_page)
        self.rtsp_actual_status_label.setObjectName(u"rtsp_actual_status_label")
        self.rtsp_actual_status_label.setGeometry(QRect(50, 100, 47, 13))


        self.rtsp_device_name_label.setText(QCoreApplication.translate("MainWindow", u"Device name:", None))
        self.rtsp_stream_url_label.setText(QCoreApplication.translate("MainWindow", u"Stream URL:", None))
        self.rtsp_enable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.rtsp_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.rtsp_status_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.rtsp_actual_status_label.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))

        self.rtsp_device_name_lineEdit.setText(self.rtsp_name)
        self.rtsp_device_name_lineEdit.textChanged.connect(lambda: self.rtsp_left_menu_name.setText(0, self.rtsp_device_name_lineEdit.text()))

        self.rtsp_enable_pushButton.clicked.connect(self.enable_disable_rtsp_cam)
        self.rtsp_delete_pushButton.clicked.connect(self.delete_rtsp_cam)


        return self.rtsp_page

    def enable_disable_rtsp_cam(self):
        if self.status == False:
            self.new_camera = New_rtsp_camera(self.rtsp_stream_url_lineEdit.text())
            self.cam_status = self.new_camera.add_new_camera()
            if self.cam_status == False:
                self.rtsp_actual_status_label.setText("Error")
            else:
                for k, v in Ui_MainWindow.camera_position_in_grid.items():
                    if v == None:
                        Ui_MainWindow.camera_position_in_grid[k] = self.new_camera
                        self.rtsp_update_main_gui_add.emit(self.cam_status, k[0], k[1])
                        self.rtsp_enable_pushButton.setText("Disable")
                        self.rtsp_actual_status_label.setText("Enabled")
                        self.status = True
                        break

        elif self.status == True:
            self.new_camera.stop_camera()
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == self.new_camera:
                    self.rtsp_update_main_gui_delete.emit(self.cam_status)
                    self.rtsp_enable_pushButton.setText("Enable")
                    self.rtsp_actual_status_label.setText("Disabled")
                    self.status = False
                    Ui_MainWindow.camera_position_in_grid[k] = None
                    break
    def delete_rtsp_cam(self):
        if self.status == True:
            try:
                self.new_camera.stop_camera()
                for k, v in Ui_MainWindow.camera_position_in_grid.items():
                    if v == self.new_camera:
                        self.rtsp_update_main_gui_delete.emit(self.cam_status)
                        Ui_MainWindow.camera_position_in_grid[k] = None
            except:
                pass
            self.rtsp_delete_page.emit(Ui_MainWindow.user_current_position)
        elif self.status == False:
            self.rtsp_delete_page.emit(Ui_MainWindow.user_current_position)


class Webcam_page(QObject):
    webcam_update_main_gui = Signal(QWidget, int, int)
    webcam_update_main_gui_delete = Signal(QWidget)
    webcam_delete_page = Signal(int)


    def __init__(self, actual_index, webcam_name, webcam_left_menu_name):
        super().__init__()
        self.actual_index = actual_index
        self.webcam_name = webcam_name
        self.webcam_left_menu_name = webcam_left_menu_name
        self.status = False
    def setupGUi(self):
        self.webcam_page = QWidget()
        self.webcam_page.setObjectName(u"webcam_page")
        self.webcam_device_name_label = QLabel(self.webcam_page)
        self.webcam_device_name_label.setObjectName(u"webcam_device_name_label")
        self.webcam_device_name_label.setGeometry(QRect(10, 10, 71, 16))
        self.webcam_device_name_lineEdit = QLineEdit(self.webcam_page)
        self.webcam_device_name_lineEdit.setObjectName(u"webcam_device_name_lineEdit")
        self.webcam_device_name_lineEdit.setGeometry(QRect(10, 30, 221, 20))
        self.webcam_enable_pushButton = QPushButton(self.webcam_page)
        self.webcam_enable_pushButton.setObjectName(u"webcam_enable_pushButton")
        self.webcam_enable_pushButton.setGeometry(QRect(10, 80, 75, 23))
        self.webcam_delete_pushButton = QPushButton(self.webcam_page)
        self.webcam_delete_pushButton.setObjectName(u"webcam_delete_pushButton")
        self.webcam_delete_pushButton.setGeometry(QRect(90, 80, 75, 23))
        self.webcam_status_label = QLabel(self.webcam_page)
        self.webcam_status_label.setObjectName(u"webcam_status_label")
        self.webcam_status_label.setGeometry(QRect(10, 60, 47, 13))
        self.webcam_actual_status_label = QLabel(self.webcam_page)
        self.webcam_actual_status_label.setObjectName(u"webcam_actual_status_label")
        self.webcam_actual_status_label.setGeometry(QRect(50, 60, 47, 13))

        self.webcam_device_name_label.setText(QCoreApplication.translate("MainWindow", u"Device name:", None))
        self.webcam_enable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.webcam_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.webcam_status_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.webcam_actual_status_label.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))

        self.webcam_device_name_lineEdit.setText(self.webcam_name)
        self.webcam_device_name_lineEdit.textChanged.connect(lambda: self.webcam_left_menu_name.setText(0, self.webcam_device_name_lineEdit.text()))

        self.webcam_enable_pushButton.clicked.connect(self.enable_disable_webcam)

        self.webcam_delete_pushButton.clicked.connect(self.delete_webcam)

        return self.webcam_page

    def enable_disable_webcam(self):
        # Enable
        if self.status == False:
            self.new_camera = New_webcamera()
            self.cam_status = self.new_camera.add_new_camera()
            if self.cam_status == False:
                self.webcam_actual_status_label.setText("Error")
            else:
                for k, v in Ui_MainWindow.camera_position_in_grid.items():
                    if v == None:
                        Ui_MainWindow.camera_position_in_grid[k] = self.new_camera
                        self.webcam_update_main_gui.emit(self.cam_status, k[0], k[1])
                        self.webcam_enable_pushButton.setText("Disable")
                        self.webcam_actual_status_label.setText("Enabled")
                        self.status = True
                        break

        # Disable
        elif self.status == True:
            self.new_camera.stop_camera()
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == self.new_camera:
                    self.webcam_update_main_gui_delete.emit(self.cam_status)
                    self.webcam_enable_pushButton.setText("Enable")
                    self.webcam_actual_status_label.setText("Disabled")
                    self.status = False
                    Ui_MainWindow.camera_position_in_grid[k] = None
                    break

    def delete_webcam(self):
        if self.status == True:
            try:
                self.new_camera.stop_camera()
                for k, v in Ui_MainWindow.camera_position_in_grid.items():
                    if v == self.new_camera:
                        self.webcam_update_main_gui_delete.emit(self.cam_status)
                        Ui_MainWindow.camera_position_in_grid[k] = None
            except:
                pass
            self.webcam_delete_page.emit(Ui_MainWindow.user_current_position)
        elif self.status == False:
            self.webcam_delete_page.emit(Ui_MainWindow.user_current_position)
