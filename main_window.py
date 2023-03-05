# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject, QObject, QRect,
                            QSize, QTimer, Qt, Slot, Signal, QEvent, QMimeData)
from PySide6.QtGui import (QIcon, QDrag)
from PySide6.QtWidgets import (QPushButton, QSizePolicy, QStackedWidget,
                               QVBoxLayout, QWidget, QDialog, QGridLayout, QLabel, QLineEdit, QFrame,
                               QTreeWidget, QTreeWidgetItem, QHBoxLayout, QSpacerItem, QCheckBox, QMessageBox)

import GPUtil
import psutil
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from add_new_camera_dialog import Ui_Add_new_cam_dialog
from add_new_rtsp_camera_event import New_rtsp_camera
from add_new_webcam_event import New_webcamera
from data_base import Base, Cam_list

import resources


class Ui_MainWindow(object):

    # All possible cameras positions in grid widget
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

    # All possible tree widgets and pages
    left_menu_tree_widget_list = []

    # Current position of user in menu
    user_current_position_in_tree_widget_list = 0

    # Create engine for database
    engine = create_engine('sqlite:///cam_list.db', echo=True)

    # Limit amount of webcams to 1 max
    limit_webcam = 0

    def __init__(self):
        super().__init__()

    # Setting up UI
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        "____________________________________________________"
        # DB initialization

        Base.metadata.create_all(bind=self.engine)

        "____________________________________________________"
        # Central widget

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(800, 600)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        "____________________________________________________"
        # Left menu

        self.left_menu_treeWidget = QTreeWidget(self.centralwidget)
        self.left_menu_treeWidget.setObjectName(u"left_menu_treeView")
        self.left_menu_treeWidget.setMaximumSize(QSize(120, 1000))
        self.left_menu_treeWidget.setBaseSize(QSize(0, 0))
        self.left_menu_treeWidget.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.left_menu_treeWidget)

        self.main_window_stackedWidget = QStackedWidget(self.centralwidget)
        self.main_window_stackedWidget.setObjectName(u"main_window_stackedWidget")
        self.main_window_stackedWidget.setGeometry(QRect(130, 0, 661, 591))

        "____________________________________________________"
        #Dashboard page

        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.verticalLayout = QVBoxLayout(self.dashboard_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboard_page_verticalLayout = QVBoxLayout()
        self.dashboard_page_verticalLayout.setObjectName(u"dashboard_page_verticalLayout")
        self.dashboard_page_version_verticalLayout = QVBoxLayout()
        self.dashboard_page_version_verticalLayout.setObjectName(u"dashboard_page_version_verticalLayout")
        self.software_version_label = QLabel(self.dashboard_page)
        self.software_version_label.setObjectName(u"software_version_label")

        self.dashboard_page_version_verticalLayout.addWidget(self.software_version_label)

        self.system_parameters_label = QLabel(self.dashboard_page)
        self.system_parameters_label.setObjectName(u"system_parameters_label")

        self.dashboard_page_version_verticalLayout.addWidget(self.system_parameters_label)

        self.dashboard_page_verticalLayout.addLayout(self.dashboard_page_version_verticalLayout)

        self.system_parameters_frame = QFrame(self.dashboard_page)
        self.system_parameters_frame.setObjectName(u"system_parameters_frame")
        self.system_parameters_frame.setFrameShape(QFrame.StyledPanel)
        self.system_parameters_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.system_parameters_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dashboard_page_info_verticalLayout = QVBoxLayout()
        self.dashboard_page_info_verticalLayout.setObjectName(u"dashboard_page_info_verticalLayout")
        self.cpu_load_label = QLabel(self.system_parameters_frame)
        self.cpu_load_label.setObjectName(u"cpu_load_label")

        self.dashboard_page_info_verticalLayout.addWidget(self.cpu_load_label)

        self.ram_load_label = QLabel(self.system_parameters_frame)
        self.ram_load_label.setObjectName(u"ram_load_label")

        self.dashboard_page_info_verticalLayout.addWidget(self.ram_load_label)

        self.gpu_load_label = QLabel(self.system_parameters_frame)
        self.gpu_load_label.setObjectName(u"gpu_load_label")

        self.dashboard_page_info_verticalLayout.addWidget(self.gpu_load_label)

        self.dashboard_page_info_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dashboard_page_info_verticalLayout.addItem(self.dashboard_page_info_verticalSpacer)

        self.horizontalLayout_2.addLayout(self.dashboard_page_info_verticalLayout)

        self.dashboard_page_values_verticalLayout = QVBoxLayout()
        self.dashboard_page_values_verticalLayout.setObjectName(u"dashboard_page_values_verticalLayout")
        self.cpu_load_info_label = QLabel(self.system_parameters_frame)
        self.cpu_load_info_label.setObjectName(u"cpu_load_info_label")

        self.dashboard_page_values_verticalLayout.addWidget(self.cpu_load_info_label)

        self.ram_load_info_label = QLabel(self.system_parameters_frame)
        self.ram_load_info_label.setObjectName(u"ram_load_info_label")

        self.dashboard_page_values_verticalLayout.addWidget(self.ram_load_info_label)

        self.gpu_load_info_label = QLabel(self.system_parameters_frame)
        self.gpu_load_info_label.setObjectName(u"gpu_load_info_label")

        self.dashboard_page_values_verticalLayout.addWidget(self.gpu_load_info_label)

        self.dashboard_page_values = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dashboard_page_values_verticalLayout.addItem(self.dashboard_page_values)

        self.horizontalLayout_2.addLayout(self.dashboard_page_values_verticalLayout)

        self.system_parameters_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.system_parameters_horizontalSpacer)

        self.dashboard_page_verticalLayout.addWidget(self.system_parameters_frame)

        self.verticalLayout.addLayout(self.dashboard_page_verticalLayout)

        self.main_window_stackedWidget.addWidget(self.dashboard_page)

        "____________________________________________________"
        # Cameras page

        self.cameras_page = QWidget()
        self.cameras_page.setObjectName(u"cameras_page")
        self.gridLayout = QGridLayout(self.cameras_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cameras_page_gridLayout = QGridLayout()
        self.cameras_page_gridLayout.setSpacing(0)
        self.cameras_page_gridLayout.setObjectName(u"cameras_page_gridLayout")

        self.gridLayout.addLayout(self.cameras_page_gridLayout, 0, 0, 1, 1)
        self.main_window_stackedWidget.addWidget(self.cameras_page)

        "____________________________________________________"
        # Settings page

        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_4 = QVBoxLayout(self.settings_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settings_page_verticalLayout = QVBoxLayout()
        self.settings_page_verticalLayout.setObjectName(u"settings_page_verticalLayout")
        self.settings_page_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.settings_page_verticalLayout.addItem(self.settings_page_verticalSpacer)

        self.add_new_camera_pushButton = QPushButton(self.settings_page)
        self.add_new_camera_pushButton.setObjectName(u"add_camera_pushButton")
        self.add_new_camera_pushButton.setMaximumSize(QSize(75, 16777215))

        self.settings_page_verticalLayout.addWidget(self.add_new_camera_pushButton)

        self.verticalLayout_4.addLayout(self.settings_page_verticalLayout)

        self.main_window_stackedWidget.addWidget(self.settings_page)

        self.main_window_stackedWidget.setCurrentIndex(0)

        "____________________________________________________"
        # Tree model menu

        self.dashboard = QTreeWidgetItem(self.left_menu_treeWidget)
        self.dashboard.setText(0, 'Dashboard')
        dashboard_icon = QIcon()
        dashboard_icon.addFile(u":/media/icons/dashboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard.setIcon(0, dashboard_icon)
        self.dashboard.setData(0, Qt.UserRole, 0)
        self.dashboard.setTextAlignment(0, Qt.AlignLeft)
        Ui_MainWindow.left_menu_tree_widget_list.append((self.dashboard, None))

        self.cameras = QTreeWidgetItem(self.left_menu_treeWidget)
        self.cameras.setText(0, 'Cameras')
        cameras_icon = QIcon()
        cameras_icon.addFile(u":/media/icons/cameras.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameras.setIcon(0, cameras_icon)
        self.cameras.setData(0, Qt.UserRole, 1)
        self.cameras.setTextAlignment(0, Qt.AlignLeft)
        Ui_MainWindow.left_menu_tree_widget_list.append((self.cameras, None))

        self.settings = QTreeWidgetItem(self.left_menu_treeWidget)
        self.settings.setText(0, 'Settings')
        settings_icon = QIcon()
        settings_icon.addFile(u":/media/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(0, settings_icon)
        self.settings.setData(0, Qt.UserRole, 2)
        self.settings.setTextAlignment(0, Qt.AlignLeft)
        Ui_MainWindow.left_menu_tree_widget_list.append((self.settings, None))

        "____________________________________________________"
        # Switch user position in left menu

        self.left_menu_treeWidget.itemClicked.connect(self.left_menu_clicked)

        "____________________________________________________"
        # Dashboard timer to update dashboard values

        dashboard_timer = QTimer(self, interval=1000, timeout=self.update_dashboard)
        dashboard_timer.start()

        "____________________________________________________"
        # Dialog to add new cameras

        self.add_new_camera_pushButton.clicked.connect(self.add_new_cam_dialog)

        "____________________________________________________"

        self.horizontalLayout.addWidget(self.main_window_stackedWidget)

        self.load_from_db()

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
    # Function to load cameras from db
    def load_from_db(self):
        session = Session(Ui_MainWindow.engine)
        for cameras in session.query(Cam_list).all():
            if cameras.cam_type == 'rtsp':
                self.rtsp = QTreeWidgetItem(self.settings)

                self.rtsp_name = cameras.cam_name
                self.rtsp.setText(0, self.rtsp_name)
                self.rtsp.setData(0, Qt.UserRole, len(Ui_MainWindow.left_menu_tree_widget_list))

                # Creating camera class and connecting it to signals
                self.rtsp_page = Rtsp_page(self.rtsp_name, self.rtsp, analytics_status=cameras.analytics_status, camera_status=cameras.cam_status, current_position_in_grid=cameras.cam_position_in_grid, unique_id=cameras.cam_id, from_db=True)
                self.rtsp_page.rtsp_update_main_gui_add.connect(self.add_cameras_page_gridLayout)  # add camera to grid
                self.rtsp_page.rtsp_update_main_gui_delete.connect(self.delete_cameras_page_gridLayout)  # delete camera from grid
                self.rtsp_page.rtsp_left_menu_delete_page.connect(self.delete_qtree_item)  # delete from left menu
                self.rtsp_page.rtsp_show_hide_camera_action.connect(self.expand_hide_camera)  # expand or hide camera
                self.main_window_stackedWidget.addWidget(self.rtsp_page.setupGUi())
                self.rtsp_page.rtsp_stream_url_lineEdit.setText(cameras.cam_link)
                Ui_MainWindow.left_menu_tree_widget_list.append((self.rtsp, self.rtsp_page))

                if cameras.cam_status == True:

                    self.rtsp_page.new_camera = New_rtsp_camera(cameras.cam_link)
                    self.rtsp_page.camera = self.rtsp_page.new_camera.add_new_camera()
                    self.rtsp_page.new_camera.error_message.connect(self.rtsp_page.update_status_label_with_error)
                    Ui_MainWindow.camera_position_in_grid[(int(cameras.cam_position_in_grid[1]), int(cameras.cam_position_in_grid[4]))] = self.rtsp_page.new_camera
                    self.rtsp_page.rtsp_update_main_gui_add.emit(self.rtsp_page.camera, int(cameras.cam_position_in_grid[1]), int(cameras.cam_position_in_grid[4]))
                    self.rtsp_page.rtsp_enable_pushButton.setText("Disable")
                    self.rtsp_page.rtsp_actual_status_label.setText('Enabled')
                    self.rtsp_page.new_camera.QScrollArea.installEventFilter(self)
                    #self.rtsp_page.new_camera.QScrollArea.setAcceptDrops(True)

                    if cameras.analytics_status == True:
                        self.rtsp_page.rtsp_run_lpr_checkBox.setChecked(True)
                        self.rtsp_page.new_camera.run_lpr()

            if cameras.cam_type == 'webcam':
                self.webcam = QTreeWidgetItem(self.settings)

                self.webcam_name = cameras.cam_name
                self.webcam.setText(0, self.webcam_name)
                self.webcam.setData(0, Qt.UserRole, len(Ui_MainWindow.left_menu_tree_widget_list))

                # Creating camera class and connecting it to signals
                self.webcam_page = Webcam_page(self.webcam_name, self.webcam, analytics_status=cameras.analytics_status,
                                           camera_status=cameras.cam_status,
                                           current_position_in_grid=cameras.cam_position_in_grid,
                                           unique_id=cameras.cam_id)
                self.webcam_page.webcam_update_main_gui_add.connect(self.add_cameras_page_gridLayout)  # add camera to grid
                self.webcam_page.webcam_update_main_gui_delete.connect(self.delete_cameras_page_gridLayout)  # delete camera from grid
                self.webcam_page.webcam_left_menu_delete_page.connect(self.delete_qtree_item)  # delete from left menu
                self.webcam_page.webcam_show_hide_camera_action.connect(self.expand_hide_camera)  # expand or hide camera
                self.main_window_stackedWidget.addWidget(self.webcam_page.setupGUi())
                Ui_MainWindow.left_menu_tree_widget_list.append((self.webcam, self.webcam_page))
                Ui_MainWindow.limit_webcam += 1

                if cameras.cam_status == True:

                    self.webcam_page.new_camera = New_webcamera()
                    self.webcam_page.camera = self.webcam_page.new_camera.add_new_camera()
                    self.webcam_page.new_camera.error_message.connect(self.webcam_page.update_status_label_with_error)
                    Ui_MainWindow.camera_position_in_grid[(int(cameras.cam_position_in_grid[1]), int(cameras.cam_position_in_grid[4]))] = self.webcam_page.new_camera
                    self.webcam_page.webcam_update_main_gui_add.emit(self.webcam_page.camera,
                                                                 int(cameras.cam_position_in_grid[1]),
                                                                 int(cameras.cam_position_in_grid[4]))
                    self.webcam_page.webcam_enable_pushButton.setText("Disable")
                    self.webcam_page.webcam_actual_status_label.setText('Enabled')
                    self.webcam_page.new_camera.QScrollArea.installEventFilter(self)

                    if cameras.analytics_status == True:
                        self.webcam_page.webcam_run_lpr_checkBox.setChecked(True)
                        self.webcam_page.new_camera.run_lpr()


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

        #print(Ui_MainWindow.camera_position_in_grid)
        #print(Ui_MainWindow.left_menu_tree_widget_list)
        if item.data(col, Qt.UserRole) is not None:
            Ui_MainWindow.user_current_position_in_tree_widget_list = item.data(col, Qt.UserRole) # Store current position of user in left menu
            self.main_window_stackedWidget.setCurrentIndex(item.data(col, Qt.UserRole)) # Switch user position

    "____________________________________________________"
    # Slot to add new camera to gridLayout
    # camera func - video that we are adding to grid layout
    # x and y positions - positions in grid where we are adding

    @Slot(QObject, QWidget, int, int)
    def add_cameras_page_gridLayout(self, camera_func, x_pos_in_grid, y_pos_in_grid):
        self.cameras_page_gridLayout.addWidget(camera_func, x_pos_in_grid, y_pos_in_grid)

    "____________________________________________________"
    # Slot to delete camera in gridLayout
    # camera func - video that we are deleting from grid layout
    # rtsp_widget - page gui that we are deleting

    @Slot(QWidget, QWidget)
    def delete_cameras_page_gridLayout(self, camera_func, rtsp_widget):
        try:
            camera_func.deleteLater()
        except:
            pass
        try:
            rtsp_widget.deleteLater()
        except:
            pass

    "____________________________________________________"
    # Slot to totally delete page from left menu
    # qtree_child_index - position in left menu that we are deleting

    @Slot(int, str)
    def delete_qtree_item(self, qtree_child_index, unique_id):
        self.settings.removeChild(Ui_MainWindow.left_menu_tree_widget_list[qtree_child_index][0]) # deleting from left menu
        self.main_window_stackedWidget.setCurrentIndex(2) # changing current user position
        Ui_MainWindow.user_current_position_in_tree_widget_list = 2 # Store current position of user in left menu
        del Ui_MainWindow.left_menu_tree_widget_list[qtree_child_index] # deleting class from program
        for i in range(len(Ui_MainWindow.left_menu_tree_widget_list)):
            Ui_MainWindow.left_menu_tree_widget_list[i][0].setData(0, Qt.UserRole, i) # update positions in left menu

        session = Session(Ui_MainWindow.engine)
        session.query(Cam_list).filter_by(cam_id=unique_id).delete()
        session.commit()

    "____________________________________________________"
    # Slot to hide or show cameras in gridLayout
    # camera func - video that we want to expand

    @Slot(QWidget)
    def expand_hide_camera(self, camera_func):
        if self.expanded == False:
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v != camera_func and v is not None:
                    self.cameras_page_gridLayout.itemAtPosition(k[0], k[1]).widget().hide()
                    self.expanded = True
        else:
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v != camera_func and v is not None:
                    self.cameras_page_gridLayout.itemAtPosition(k[0], k[1]).widget().show()
                    self.expanded = False

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

            self.rtsp_name = 'RTSP'
            self.rtsp.setText(0, self.rtsp_name)
            self.rtsp.setData(0, Qt.UserRole, len(Ui_MainWindow.left_menu_tree_widget_list))

            # Creating camera class and connecting it to signals
            self.rtsp_page = Rtsp_page(self.rtsp_name, self.rtsp)
            self.rtsp_page.rtsp_update_main_gui_add.connect(self.add_cameras_page_gridLayout) # add camera to grid
            self.rtsp_page.rtsp_update_main_gui_delete.connect(self.delete_cameras_page_gridLayout) # delete camera from grid
            self.rtsp_page.rtsp_left_menu_delete_page.connect(self.delete_qtree_item) # delete from left menu
            self.rtsp_page.rtsp_show_hide_camera_action.connect(self.expand_hide_camera) # expand or hide camera
            self.main_window_stackedWidget.addWidget(self.rtsp_page.setupGUi())
            Ui_MainWindow.left_menu_tree_widget_list.append((self.rtsp, self.rtsp_page))

        elif adding_new_cam.choice_value == 'webcam':
            if Ui_MainWindow.limit_webcam == 0:
                self.webcam = QTreeWidgetItem(self.settings)

                self.webcam_name = 'Webcam'
                self.webcam.setText(0, self.webcam_name)
                self.webcam.setData(0, Qt.UserRole, len(Ui_MainWindow.left_menu_tree_widget_list))

                # Creating camera class and connecting it to signals
                self.webcam_page = Webcam_page(self.webcam_name, self.webcam)
                self.webcam_page.webcam_update_main_gui_add.connect(self.add_cameras_page_gridLayout) # add camera to grid
                self.webcam_page.webcam_update_main_gui_delete.connect(self.delete_cameras_page_gridLayout) # delete camera from grid
                self.webcam_page.webcam_left_menu_delete_page.connect(self.delete_qtree_item) # delete from left menu
                self.webcam_page.webcam_show_hide_camera_action.connect(self.expand_hide_camera) # expand or hide camera
                self.main_window_stackedWidget.addWidget(self.webcam_page.setupGUi())
                Ui_MainWindow.left_menu_tree_widget_list.append((self.webcam, self.webcam_page))
                Ui_MainWindow.limit_webcam += 1
            else:
                max_webcam_msg_box = QMessageBox()
                max_webcam_msg_box.setIcon(QMessageBox.Warning)
                max_webcam_msg_box.setText("You can add only one webcam")
                max_webcam_msg_box.setWindowTitle("Webcam Error")
                max_webcam_msg_box.setStandardButtons(QMessageBox.Ok)
                max_webcam_msg_box.exec()


"____________________________________________________"

# Class to add a camera using RTSP
class Rtsp_page(QObject):
    rtsp_update_main_gui_add = Signal(QWidget, int, int)
    rtsp_update_main_gui_delete = Signal(QWidget, QWidget)
    rtsp_left_menu_delete_page = Signal(int, str)
    rtsp_show_hide_camera_action = Signal(QWidget)

    def __init__(self, rtsp_name, rtsp_left_menu_name, analytics_status=False, camera_status=False, current_position_in_grid='No position', unique_id=None, from_db = False):
        super().__init__()

        self.rtsp_name = rtsp_name
        self.rtsp_left_menu_name = rtsp_left_menu_name

        self.analytics_status = analytics_status
        self.camera_status = camera_status
        self.camera_type = 'rtsp'
        self.current_position_in_grid = current_position_in_grid
        self.unique_id = unique_id
        self.from_db = from_db

        self.target = None

    def setupGUi(self):

        if self.from_db == False:
            self.unique_id = str(uuid.uuid4())[:8]

        self.rtsp_page = QWidget()
        self.rtsp_page.setObjectName(u"rtsp_page")

        self.verticalLayout_3 = QVBoxLayout(self.rtsp_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rtsp_page_verticalLayout = QVBoxLayout()
        self.rtsp_page_verticalLayout.setObjectName(u"rtsp_page_verticalLayout")
        self.rtsp_page_device_name_verticalLayout = QVBoxLayout()
        self.rtsp_page_device_name_verticalLayout.setObjectName(u"rtsp_page_device_name_verticalLayout")
        self.rtsp_device_name_label = QLabel(self.rtsp_page)
        self.rtsp_device_name_label.setObjectName(u"rtsp_device_name_label")

        self.rtsp_page_device_name_verticalLayout.addWidget(self.rtsp_device_name_label)

        self.rtsp_device_name_lineEdit = QLineEdit(self.rtsp_page)
        self.rtsp_device_name_lineEdit.setObjectName(u"rtsp_device_name_lineEdit")
        self.rtsp_device_name_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.rtsp_page_device_name_verticalLayout.addWidget(self.rtsp_device_name_lineEdit)

        self.rtsp_page_verticalLayout.addLayout(self.rtsp_page_device_name_verticalLayout)

        self.rtsp_page_stream_url_verticalLayout = QVBoxLayout()
        self.rtsp_page_stream_url_verticalLayout.setObjectName(u"rtsp_page_stream_url_verticalLayout")
        self.rtsp_stream_url_label = QLabel(self.rtsp_page)
        self.rtsp_stream_url_label.setObjectName(u"rtsp_stream_url_label")

        self.rtsp_page_stream_url_verticalLayout.addWidget(self.rtsp_stream_url_label)

        self.rtsp_stream_url_lineEdit = QLineEdit(self.rtsp_page)
        self.rtsp_stream_url_lineEdit.setObjectName(u"rtsp_stream_url_lineEdit")
        self.rtsp_stream_url_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.rtsp_page_stream_url_verticalLayout.addWidget(self.rtsp_stream_url_lineEdit)

        self.rtsp_page_verticalLayout.addLayout(self.rtsp_page_stream_url_verticalLayout)

        self.rtsp_page_actual_status_horizontalLayout = QHBoxLayout()
        self.rtsp_page_actual_status_horizontalLayout.setObjectName(u"rtsp_page_actual_status_horizontalLayout")
        self.rtsp_status_label = QLabel(self.rtsp_page)
        self.rtsp_status_label.setObjectName(u"rtsp_status_label")

        self.rtsp_page_actual_status_horizontalLayout.addWidget(self.rtsp_status_label)

        self.rtsp_actual_status_label = QLabel(self.rtsp_page)
        self.rtsp_actual_status_label.setObjectName(u"rtsp_actual_status_label")

        self.rtsp_page_actual_status_horizontalLayout.addWidget(self.rtsp_actual_status_label)

        self.rtsp_actual_status_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rtsp_page_actual_status_horizontalLayout.addItem(self.rtsp_actual_status_horizontalSpacer)

        self.rtsp_page_verticalLayout.addLayout(self.rtsp_page_actual_status_horizontalLayout)

        self.rtsp_page_buttons_horizontalLayout = QHBoxLayout()
        self.rtsp_page_buttons_horizontalLayout.setObjectName(u"rtsp_page_buttons_horizontalLayout")
        self.rtsp_enable_pushButton = QPushButton(self.rtsp_page)
        self.rtsp_enable_pushButton.setObjectName(u"rtsp_enable_pushButton")

        self.rtsp_page_buttons_horizontalLayout.addWidget(self.rtsp_enable_pushButton)

        self.rtsp_delete_pushButton = QPushButton(self.rtsp_page)
        self.rtsp_delete_pushButton.setObjectName(u"rtsp_delete_pushButton")

        self.rtsp_page_buttons_horizontalLayout.addWidget(self.rtsp_delete_pushButton)

        self.rtsp_buttons_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rtsp_page_buttons_horizontalLayout.addItem(self.rtsp_buttons_horizontalSpacer)

        self.rtsp_page_verticalLayout.addLayout(self.rtsp_page_buttons_horizontalLayout)

        self.rtsp_page_analytics_checkboxes_verticalLayout = QVBoxLayout()
        self.rtsp_page_analytics_checkboxes_verticalLayout.setObjectName(
            u"rtsp_page_analytics_checkboxes_verticalLayout")
        self.rtsp_run_lpr_checkBox = QCheckBox(self.rtsp_page)
        self.rtsp_run_lpr_checkBox.setObjectName(u"rtsp_run_lpr_checkBox")

        self.rtsp_page_analytics_checkboxes_verticalLayout.addWidget(self.rtsp_run_lpr_checkBox)

        self.rtsp_page_analytics_checkboxes_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                                                         QSizePolicy.Expanding)

        self.rtsp_page_analytics_checkboxes_verticalLayout.addItem(self.rtsp_page_analytics_checkboxes_verticalSpacer)

        self.rtsp_page_verticalLayout.addLayout(self.rtsp_page_analytics_checkboxes_verticalLayout)

        self.verticalLayout_3.addLayout(self.rtsp_page_verticalLayout)

        # Line to change name of the camera in Left menu
        self.rtsp_device_name_lineEdit.setText(self.rtsp_name)
        self.rtsp_device_name_lineEdit.textChanged.connect(self.update_device_name)
        # Button to enable/disable camera
        self.rtsp_enable_pushButton.clicked.connect(self.enable_disable_rtsp_cam)
        # Button to delete camera
        self.rtsp_delete_pushButton.clicked.connect(self.delete_rtsp_cam)
        # Checkbox to run LPR analytics
        self.rtsp_run_lpr_checkBox.stateChanged.connect(self.check_lpr_button_status)

        self.rtsp_device_name_label.setText(QCoreApplication.translate("MainWindow", u"Device name:", None))
        self.rtsp_stream_url_label.setText(QCoreApplication.translate("MainWindow", u"Stream URL:", None))
        self.rtsp_enable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.rtsp_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.rtsp_status_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.rtsp_actual_status_label.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.rtsp_run_lpr_checkBox.setText(QCoreApplication.translate("MainWindow", u"Run LPR", None))

        return self.rtsp_page

    # Update name in left menu
    def update_device_name(self):
        self.rtsp_left_menu_name.setText(0, self.rtsp_device_name_lineEdit.text())

    # Run and stop LPR analytics
    def check_lpr_button_status(self):
        if self.rtsp_run_lpr_checkBox.isChecked() == True:
            self.new_camera.run_lpr()
            self.analytics_status = True
        else:
            self.new_camera.stop_lpr()
            self.analytics_status = False

    # Enable or disable camera
    def enable_disable_rtsp_cam(self):
        if self.camera_status == False:
            self.new_camera = New_rtsp_camera(self.rtsp_stream_url_lineEdit.text())
            self.camera = self.new_camera.add_new_camera()
            self.new_camera.error_message.connect(self.update_status_label_with_error)
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == None:
                    Ui_MainWindow.camera_position_in_grid[k] = self.new_camera
                    self.rtsp_update_main_gui_add.emit(self.camera, k[0], k[1])
                    self.current_position_in_grid = f'({k[0]}, {k[1]})'
                    self.rtsp_enable_pushButton.setText("Disable")
                    self.rtsp_actual_status_label.setText('Enabled')
                    self.camera_status = True
                    self.new_camera.QScrollArea.installEventFilter(self)
                    #self.new_camera.QScrollArea.setAcceptDrops(True)
                    break

        elif self.camera_status == True:
            self.new_camera.stop_camera()
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == self.new_camera:
                    self.new_camera.QScrollArea.removeEventFilter(self)
                    self.rtsp_update_main_gui_delete.emit(self.camera, None)
                    self.current_position_in_grid = 'No position'
                    self.rtsp_enable_pushButton.setText("Enable")
                    self.rtsp_actual_status_label.setText("Disabled")
                    self.camera_status = False
                    Ui_MainWindow.camera_position_in_grid[k] = None
                    break
    @Slot(str)
    def update_status_label_with_error(self, str):
        self.rtsp_actual_status_label.setText(str)

    def delete_rtsp_cam(self):
        if self.camera_status == True:
            self.new_camera.stop_camera()
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == self.new_camera:
                    self.new_camera.QScrollArea.removeEventFilter(self)
                    self.rtsp_update_main_gui_delete.emit(self.camera, self.rtsp_page)
                    Ui_MainWindow.camera_position_in_grid[k] = None
                    break
            self.rtsp_left_menu_delete_page.emit(Ui_MainWindow.user_current_position_in_tree_widget_list, self.unique_id)
        elif self.camera_status == False:
            self.rtsp_update_main_gui_delete.emit(None, self.rtsp_page)
            self.rtsp_left_menu_delete_page.emit(Ui_MainWindow.user_current_position_in_tree_widget_list, self.unique_id)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            self.mousePressEvent(event)
        elif event.type() == QEvent.MouseButtonDblClick:
            self.rtsp_show_hide_camera_action.emit(self.new_camera)
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            drag = QDrag(self.new_camera)
            pix = self.new_camera.QScrollArea.widget().grab()
            mimedata = QMimeData()
            mimedata.setImageData(pix)
            drag.setMimeData(mimedata)
            drag.setPixmap(pix)
            drag.setHotSpot(event.pos())
            drag.exec()

    def __del__(self):
        print("Rtsp cam is deleted")

"____________________________________________________"
# Class to add Webcam

class Webcam_page(QObject):
    webcam_update_main_gui_add = Signal(QWidget, int, int)
    webcam_update_main_gui_delete = Signal(QWidget, QWidget)
    webcam_left_menu_delete_page = Signal(int, str)
    webcam_show_hide_camera_action = Signal(QWidget)

    def __init__(self, webcam_name, webcam_left_menu_name, analytics_status=False, camera_status=False, current_position_in_grid='No position', unique_id=str(uuid.uuid4())[:8]):
        super().__init__()
        self.webcam_name = webcam_name
        self.webcam_left_menu_name = webcam_left_menu_name

        self.analytics_status = analytics_status
        self.camera_status = camera_status
        self.camera_type = 'webcam'
        self.current_position_in_grid = current_position_in_grid
        self.unique_id = unique_id

    def setupGUi(self):
        self.webcam_page = QWidget()
        self.webcam_page.setObjectName(u"webcam_page")
        self.verticalLayout_5 = QVBoxLayout(self.webcam_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.webcam_page_device_name_verticalLayout = QVBoxLayout()
        self.webcam_page_device_name_verticalLayout.setObjectName(u"webcam_page_device_name_verticalLayout")
        self.webcam_device_name_label = QLabel(self.webcam_page)
        self.webcam_device_name_label.setObjectName(u"webcam_device_name_label")

        self.webcam_page_device_name_verticalLayout.addWidget(self.webcam_device_name_label)

        self.webcam_device_name_lineEdit = QLineEdit(self.webcam_page)
        self.webcam_device_name_lineEdit.setObjectName(u"webcam_device_name_lineEdit")
        self.webcam_device_name_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.webcam_page_device_name_verticalLayout.addWidget(self.webcam_device_name_lineEdit)

        self.verticalLayout_5.addLayout(self.webcam_page_device_name_verticalLayout)

        self.webcam_page_status_horizontalLayout = QHBoxLayout()
        self.webcam_page_status_horizontalLayout.setObjectName(u"webcam_page_status_horizontalLayout")
        self.webcam_status_label = QLabel(self.webcam_page)
        self.webcam_status_label.setObjectName(u"webcam_status_label")

        self.webcam_page_status_horizontalLayout.addWidget(self.webcam_status_label)

        self.webcam_actual_status_label = QLabel(self.webcam_page)
        self.webcam_actual_status_label.setObjectName(u"webcam_actual_status_label")

        self.webcam_page_status_horizontalLayout.addWidget(self.webcam_actual_status_label)

        self.webcam_page_status_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.webcam_page_status_horizontalLayout.addItem(self.webcam_page_status_horizontalSpacer)

        self.verticalLayout_5.addLayout(self.webcam_page_status_horizontalLayout)

        self.webcam_page_buttons_horizontalLayout = QHBoxLayout()
        self.webcam_page_buttons_horizontalLayout.setObjectName(u"webcam_page_buttons_horizontalLayout")
        self.webcam_enable_pushButton = QPushButton(self.webcam_page)
        self.webcam_enable_pushButton.setObjectName(u"webcam_enable_pushButton")

        self.webcam_page_buttons_horizontalLayout.addWidget(self.webcam_enable_pushButton)

        self.webcam_delete_pushButton = QPushButton(self.webcam_page)
        self.webcam_delete_pushButton.setObjectName(u"webcam_delete_pushButton")

        self.webcam_page_buttons_horizontalLayout.addWidget(self.webcam_delete_pushButton)

        self.webcam_page_buttons_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.webcam_page_buttons_horizontalLayout.addItem(self.webcam_page_buttons_horizontalSpacer)

        self.verticalLayout_5.addLayout(self.webcam_page_buttons_horizontalLayout)

        self.webcam_page_analytics_checkboxes_verticalLayout = QVBoxLayout()
        self.webcam_page_analytics_checkboxes_verticalLayout.setObjectName(
            u"webcam_page_analytics_checkboxes_verticalLayout")
        self.webcam_run_lpr_checkBox = QCheckBox(self.webcam_page)
        self.webcam_run_lpr_checkBox.setObjectName(u"webcam_run_lpr_checkBox")

        self.webcam_page_analytics_checkboxes_verticalLayout.addWidget(self.webcam_run_lpr_checkBox)

        self.webcam_page_analytics_checkboxes_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                                                           QSizePolicy.Expanding)

        self.webcam_page_analytics_checkboxes_verticalLayout.addItem(
            self.webcam_page_analytics_checkboxes_verticalSpacer)

        self.verticalLayout_5.addLayout(self.webcam_page_analytics_checkboxes_verticalLayout)

        self.webcam_device_name_label.setText(QCoreApplication.translate("MainWindow", u"Device name:", None))
        self.webcam_enable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.webcam_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.webcam_status_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.webcam_actual_status_label.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.webcam_run_lpr_checkBox.setText(QCoreApplication.translate("MainWindow", u"Run LPR", None))

        self.webcam_device_name_lineEdit.setText(self.webcam_name)
        self.webcam_device_name_lineEdit.textChanged.connect(lambda: self.webcam_left_menu_name.setText(0, self.webcam_device_name_lineEdit.text()))

        self.webcam_enable_pushButton.clicked.connect(self.enable_disable_webcam)

        self.webcam_delete_pushButton.clicked.connect(self.delete_webcam)

        self.webcam_run_lpr_checkBox.stateChanged.connect(self.check_lpr_button_status)


        return self.webcam_page

    def check_lpr_button_status(self):
        if self.webcam_run_lpr_checkBox.isChecked() == True:
            self.new_camera.run_lpr()
            self.analytics_status = True
        else:
            self.new_camera.stop_lpr()
            self.analytics_status = False

    def enable_disable_webcam(self):
        # Enable
        if self.camera_status == False:
            self.new_camera = New_webcamera()
            self.camera = self.new_camera.add_new_camera()
            self.new_camera.error_message.connect(self.update_status_label_with_error)
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == None:
                    Ui_MainWindow.camera_position_in_grid[k] = self.new_camera
                    self.webcam_update_main_gui_add.emit(self.camera, k[0], k[1])
                    self.current_position_in_grid = f'({k[0]}, {k[1]})'
                    self.webcam_enable_pushButton.setText("Disable")
                    self.webcam_actual_status_label.setText("Enabled")
                    self.camera_status = True
                    self.new_camera.QScrollArea.installEventFilter(self)
                    break

        # Disable
        elif self.camera_status == True:
            self.new_camera.stop_camera()
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == self.new_camera:
                    self.webcam_update_main_gui_delete.emit(self.camera, None)
                    self.current_position_in_grid = 'No position'
                    self.webcam_enable_pushButton.setText("Enable")
                    self.webcam_actual_status_label.setText("Disabled")
                    self.camera_status = False
                    Ui_MainWindow.camera_position_in_grid[k] = None
                    self.new_camera.QScrollArea.removeEventFilter(self)
                    break

    @Slot(str)
    def update_status_label_with_error(self, str):
        self.webcam_actual_status_label.setText(str)

    def delete_webcam(self):
        if self.camera_status == True:
            self.new_camera.stop_camera()
            for k, v in Ui_MainWindow.camera_position_in_grid.items():
                if v == self.new_camera:
                    self.new_camera.QScrollArea.removeEventFilter(self)
                    self.webcam_update_main_gui_delete.emit(self.camera, self.webcam_page)
                    Ui_MainWindow.camera_position_in_grid[k] = None

            self.webcam_left_menu_delete_page.emit(Ui_MainWindow.user_current_position_in_tree_widget_list, self.unique_id)
            Ui_MainWindow.limit_webcam -= 1
        elif self.camera_status == False:
            self.webcam_update_main_gui_delete.emit(None, self.webcam_page)
            self.webcam_left_menu_delete_page.emit(Ui_MainWindow.user_current_position_in_tree_widget_list, self.unique_id)
            Ui_MainWindow.limit_webcam -= 1

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick:
            if obj:
                self.webcam_show_hide_camera_action.emit(self.new_camera)
        return super().eventFilter(obj, event)

    def __del__(self):
        print("Webcam is deleted")


