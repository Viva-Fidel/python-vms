# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.left_menu_treeWidget = QTreeWidget(self.centralwidget)
        self.left_menu_treeWidget.setObjectName(u"left_menu_treeWidget")
        self.left_menu_treeWidget.setMaximumSize(QSize(120, 600))
        self.left_menu_treeWidget.setBaseSize(QSize(0, 0))
        self.left_menu_treeWidget.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.left_menu_treeWidget)

        self.main_window_stackedWidget = QStackedWidget(self.centralwidget)
        self.main_window_stackedWidget.setObjectName(u"main_window_stackedWidget")

        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.widget = QWidget(self.dashboard_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 2, 121, 115))
        self.dashboard_page_verticalLayout = QVBoxLayout(self.widget)
        self.dashboard_page_verticalLayout.setObjectName(u"dashboard_page_verticalLayout")
        self.dashboard_page_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboard_page_version_verticalLayout = QVBoxLayout()
        self.dashboard_page_version_verticalLayout.setObjectName(u"dashboard_page_version_verticalLayout")
        self.software_version_label = QLabel(self.widget)
        self.software_version_label.setObjectName(u"software_version_label")

        self.dashboard_page_version_verticalLayout.addWidget(self.software_version_label)

        self.system_parameters_label = QLabel(self.widget)
        self.system_parameters_label.setObjectName(u"system_parameters_label")

        self.dashboard_page_version_verticalLayout.addWidget(self.system_parameters_label)


        self.dashboard_page_verticalLayout.addLayout(self.dashboard_page_version_verticalLayout)

        self.system_parameters_frame = QFrame(self.widget)
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


        self.horizontalLayout_2.addLayout(self.dashboard_page_values_verticalLayout)


        self.dashboard_page_verticalLayout.addWidget(self.system_parameters_frame)

        self.main_window_stackedWidget.addWidget(self.dashboard_page)
        self.cameras_page = QWidget()
        self.cameras_page.setObjectName(u"cameras_page")
        self.gridLayoutWidget = QWidget(self.cameras_page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 651, 581))
        self.cameras_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.cameras_gridLayout.setSpacing(0)
        self.cameras_gridLayout.setObjectName(u"cameras_gridLayout")
        self.cameras_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_window_stackedWidget.addWidget(self.cameras_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayoutWidget = QWidget(self.settings_page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 559, 81, 21))
        self.settings_page_verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.settings_page_verticalLayout.setObjectName(u"settings_page_verticalLayout")
        self.settings_page_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_camera_pushButton = QPushButton(self.verticalLayoutWidget)
        self.add_camera_pushButton.setObjectName(u"add_camera_pushButton")
        self.add_camera_pushButton.setMaximumSize(QSize(75, 16777215))

        self.settings_page_verticalLayout.addWidget(self.add_camera_pushButton)

        self.main_window_stackedWidget.addWidget(self.settings_page)









        self.webcam_page = QWidget()
        self.webcam_page.setObjectName(u"webcam_page")
        self.widget1 = QWidget(self.webcam_page)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(3, 0, 241, 102))
        self.webcam_page_verticalLayout = QVBoxLayout(self.widget1)
        self.webcam_page_verticalLayout.setObjectName(u"webcam_page_verticalLayout")
        self.webcam_page_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.webcam_page_device_name_verticalLayout = QVBoxLayout()
        self.webcam_page_device_name_verticalLayout.setObjectName(u"webcam_page_device_name_verticalLayout")
        self.webcam_device_name_label = QLabel(self.widget1)
        self.webcam_device_name_label.setObjectName(u"webcam_device_name_label")

        self.webcam_page_device_name_verticalLayout.addWidget(self.webcam_device_name_label)

        self.webcam_device_name_lineEdit = QLineEdit(self.widget1)
        self.webcam_device_name_lineEdit.setObjectName(u"webcam_device_name_lineEdit")

        self.webcam_page_device_name_verticalLayout.addWidget(self.webcam_device_name_lineEdit)


        self.webcam_page_verticalLayout.addLayout(self.webcam_page_device_name_verticalLayout)

        self.webcam_page_status_horizontalLayout = QHBoxLayout()
        self.webcam_page_status_horizontalLayout.setObjectName(u"webcam_page_status_horizontalLayout")
        self.webcam_status_label = QLabel(self.widget1)
        self.webcam_status_label.setObjectName(u"webcam_status_label")

        self.webcam_page_status_horizontalLayout.addWidget(self.webcam_status_label)

        self.webcam_actual_status_label = QLabel(self.widget1)
        self.webcam_actual_status_label.setObjectName(u"webcam_actual_status_label")

        self.webcam_page_status_horizontalLayout.addWidget(self.webcam_actual_status_label)

        self.webcam_page_status_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.webcam_page_status_horizontalLayout.addItem(self.webcam_page_status_horizontalSpacer)


        self.webcam_page_verticalLayout.addLayout(self.webcam_page_status_horizontalLayout)

        self.webcam_page_buttons_horizontalLayout = QHBoxLayout()
        self.webcam_page_buttons_horizontalLayout.setObjectName(u"webcam_page_buttons_horizontalLayout")
        self.webcam_enable_pushButton = QPushButton(self.widget1)
        self.webcam_enable_pushButton.setObjectName(u"webcam_enable_pushButton")

        self.webcam_page_buttons_horizontalLayout.addWidget(self.webcam_enable_pushButton)

        self.webcam_delete_pushButton = QPushButton(self.widget1)
        self.webcam_delete_pushButton.setObjectName(u"webcam_delete_pushButton")

        self.webcam_page_buttons_horizontalLayout.addWidget(self.webcam_delete_pushButton)

        self.webcam_page_buttons_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.webcam_page_buttons_horizontalLayout.addItem(self.webcam_page_buttons_horizontalSpacer)


        self.webcam_page_verticalLayout.addLayout(self.webcam_page_buttons_horizontalLayout)

        self.main_window_stackedWidget.addWidget(self.webcam_page)
        self.rtsp_page = QWidget()
        self.rtsp_page.setObjectName(u"rtsp_page")
        self.widget2 = QWidget(self.rtsp_page)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 0, 241, 149))
        self.rtsp_page_verticalLayout = QVBoxLayout(self.widget2)
        self.rtsp_page_verticalLayout.setObjectName(u"rtsp_page_verticalLayout")
        self.rtsp_page_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rtsp_device_name_verticalLayout = QVBoxLayout()
        self.rtsp_device_name_verticalLayout.setObjectName(u"rtsp_device_name_verticalLayout")
        self.rtsp_device_name_label = QLabel(self.widget2)
        self.rtsp_device_name_label.setObjectName(u"rtsp_device_name_label")

        self.rtsp_device_name_verticalLayout.addWidget(self.rtsp_device_name_label)

        self.rtsp_device_name_lineEdit = QLineEdit(self.widget2)
        self.rtsp_device_name_lineEdit.setObjectName(u"rtsp_device_name_lineEdit")

        self.rtsp_device_name_verticalLayout.addWidget(self.rtsp_device_name_lineEdit)


        self.rtsp_page_verticalLayout.addLayout(self.rtsp_device_name_verticalLayout)

        self.rtsp_stream_url_verticalLayout = QVBoxLayout()
        self.rtsp_stream_url_verticalLayout.setObjectName(u"rtsp_stream_url_verticalLayout")
        self.rtsp_stream_url_label = QLabel(self.widget2)
        self.rtsp_stream_url_label.setObjectName(u"rtsp_stream_url_label")

        self.rtsp_stream_url_verticalLayout.addWidget(self.rtsp_stream_url_label)

        self.rtsp_stream_url_lineEdit = QLineEdit(self.widget2)
        self.rtsp_stream_url_lineEdit.setObjectName(u"rtsp_stream_url_lineEdit")

        self.rtsp_stream_url_verticalLayout.addWidget(self.rtsp_stream_url_lineEdit)


        self.rtsp_page_verticalLayout.addLayout(self.rtsp_stream_url_verticalLayout)

        self.rtsp_actual_status_horizontalLayout = QHBoxLayout()
        self.rtsp_actual_status_horizontalLayout.setObjectName(u"rtsp_actual_status_horizontalLayout")
        self.rtsp_status_label = QLabel(self.widget2)
        self.rtsp_status_label.setObjectName(u"rtsp_status_label")

        self.rtsp_actual_status_horizontalLayout.addWidget(self.rtsp_status_label)

        self.rtsp_actual_status_label = QLabel(self.widget2)
        self.rtsp_actual_status_label.setObjectName(u"rtsp_actual_status_label")

        self.rtsp_actual_status_horizontalLayout.addWidget(self.rtsp_actual_status_label)

        self.rtsp_actual_status_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rtsp_actual_status_horizontalLayout.addItem(self.rtsp_actual_status_horizontalSpacer)


        self.rtsp_page_verticalLayout.addLayout(self.rtsp_actual_status_horizontalLayout)

        self.rtsp_buttons_horizontalLayout = QHBoxLayout()
        self.rtsp_buttons_horizontalLayout.setObjectName(u"rtsp_buttons_horizontalLayout")
        self.rtsp_enable_pushButton = QPushButton(self.widget2)
        self.rtsp_enable_pushButton.setObjectName(u"rtsp_enable_pushButton")

        self.rtsp_buttons_horizontalLayout.addWidget(self.rtsp_enable_pushButton)

        self.rtsp_delete_pushButton = QPushButton(self.widget2)
        self.rtsp_delete_pushButton.setObjectName(u"rtsp_delete_pushButton")

        self.rtsp_buttons_horizontalLayout.addWidget(self.rtsp_delete_pushButton)

        self.rtsp_buttons_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rtsp_buttons_horizontalLayout.addItem(self.rtsp_buttons_horizontalSpacer)


        self.rtsp_page_verticalLayout.addLayout(self.rtsp_buttons_horizontalLayout)

        self.main_window_stackedWidget.addWidget(self.rtsp_page)

        self.horizontalLayout.addWidget(self.main_window_stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_window_stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.software_version_label.setText(QCoreApplication.translate("MainWindow", u"Software version: 0.01a", None))
        self.system_parameters_label.setText(QCoreApplication.translate("MainWindow", u"System parameters:", None))
        self.cpu_load_label.setText(QCoreApplication.translate("MainWindow", u"CPU load:", None))
        self.ram_load_label.setText(QCoreApplication.translate("MainWindow", u"RAM load:", None))
        self.gpu_load_label.setText(QCoreApplication.translate("MainWindow", u"GPU load:", None))
        self.cpu_load_info_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ram_load_info_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gpu_load_info_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.add_camera_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add camera", None))
        self.webcam_device_name_label.setText(QCoreApplication.translate("MainWindow", u"Device name:", None))
        self.webcam_status_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.webcam_actual_status_label.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.webcam_enable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.webcam_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.rtsp_device_name_label.setText(QCoreApplication.translate("MainWindow", u"Device name:", None))
        self.rtsp_stream_url_label.setText(QCoreApplication.translate("MainWindow", u"Stream URL:", None))
        self.rtsp_status_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.rtsp_actual_status_label.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.rtsp_enable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.rtsp_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

