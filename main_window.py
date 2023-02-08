# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QTimer, QUrl, Qt, Slot, QThread, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLayout, QListView,
                               QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
                               QVBoxLayout, QWidget, QDialog, QGridLayout)
from PySide6 import QtCore

import GPUtil
import psutil
import resources

from threading import Thread
from time import strftime

from add_new_camera_dialog import Ui_Add_new_cam_dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.left_menu_widget.setGeometry(QRect(0, 0, 41, 591))
        self.layoutWidget = QWidget(self.left_menu_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 41, 130))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.layoutWidget)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        icon = QIcon()
        icon.addFile(u":/media/icons/dashboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon)
        self.dashboard_btn.setIconSize(QSize(24, 24))
        self.dashboard_btn.setCheckable(True)
        self.dashboard_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_btn)

        self.cameras_btn = QPushButton(self.layoutWidget)
        self.cameras_btn.setObjectName(u"cameras_btn")
        icon1 = QIcon()
        icon1.addFile(u":/media/icons/cameras.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameras_btn.setIcon(icon1)
        self.cameras_btn.setIconSize(QSize(24, 24))
        self.cameras_btn.setCheckable(True)
        self.cameras_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cameras_btn)

        self.settings_btn = QPushButton(self.layoutWidget)
        self.settings_btn.setObjectName(u"settings_btn")
        icon2 = QIcon()
        icon2.addFile(u":/media/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon2)
        self.settings_btn.setIconSize(QSize(24, 24))
        self.settings_btn.setCheckable(True)
        self.settings_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_btn)

        self.analytics_btn = QPushButton(self.layoutWidget)
        self.analytics_btn.setObjectName(u"analytics_btn")
        icon3 = QIcon()
        icon3.addFile(u":/media/icons/analytics.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analytics_btn.setIcon(icon3)
        self.analytics_btn.setIconSize(QSize(24, 24))
        self.analytics_btn.setCheckable(True)
        self.analytics_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.analytics_btn)

        self.main_windows_stackedWidget = QStackedWidget(self.centralwidget)
        self.main_windows_stackedWidget.setObjectName(u"main_windows_stackedWidget")
        self.main_windows_stackedWidget.setGeometry(QRect(50, 0, 751, 591))
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.clock_widget = QWidget(self.dashboard_page)
        self.clock_widget.setObjectName(u"clock_widget")
        self.clock_widget.setGeometry(QRect(20, 40, 120, 80))
        self.clock_lcdNumber = QLCDNumber(self.clock_widget)
        self.clock_lcdNumber.setObjectName(u"clock_lcdNumber")
        self.clock_lcdNumber.setGeometry(QRect(3, 2, 111, 71))
        self.cpu_load_widget = QWidget(self.dashboard_page)
        self.cpu_load_widget.setObjectName(u"cpu_load_widget")
        self.cpu_load_widget.setGeometry(QRect(150, 40, 120, 80))
        self.cpu_load_lcdNumber = QLCDNumber(self.cpu_load_widget)
        self.cpu_load_lcdNumber.setObjectName(u"cpu_load_lcdNumber")
        self.cpu_load_lcdNumber.setGeometry(QRect(3, 2, 111, 71))
        self.ram_load_widget = QWidget(self.dashboard_page)
        self.ram_load_widget.setObjectName(u"ram_load_widget")
        self.ram_load_widget.setGeometry(QRect(280, 40, 120, 80))
        self.ram_load_lcdNumber = QLCDNumber(self.ram_load_widget)
        self.ram_load_lcdNumber.setObjectName(u"ram_load_lcdNumber")
        self.ram_load_lcdNumber.setGeometry(QRect(3, 2, 111, 71))
        self.gpu_load_widget = QWidget(self.dashboard_page)
        self.gpu_load_widget.setObjectName(u"gpu_load_widget")
        self.gpu_load_widget.setGeometry(QRect(410, 40, 120, 80))
        self.gpu_load_lcdNumber = QLCDNumber(self.gpu_load_widget)
        self.gpu_load_lcdNumber.setObjectName(u"gpu_load_lcdNumber")
        self.gpu_load_lcdNumber.setGeometry(QRect(3, 2, 111, 71))
        self.main_windows_stackedWidget.addWidget(self.dashboard_page)
        self.cameras_page = QWidget()
        self.cameras_page.setObjectName(u"cameras_page")
        self.gridLayoutWidget = QWidget(self.cameras_page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 741, 591))
        self.cameras_page_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.cameras_page_gridLayout.setSpacing(0)
        self.cameras_page_gridLayout.setObjectName(u"cameras_page_gridLayout")
        self.cameras_page_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_windows_stackedWidget.addWidget(self.cameras_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_listView = QListView(self.settings_page)
        self.settings_listView.setObjectName(u"settings_listView")
        self.settings_listView.setGeometry(QRect(0, 0, 741, 551))
        self.add_new_cam_btn = QPushButton(self.settings_page)
        self.add_new_cam_btn.setObjectName(u"add_new_cam_btn")
        self.add_new_cam_btn.setGeometry(QRect(10, 560, 75, 23))
        self.main_windows_stackedWidget.addWidget(self.settings_page)
        self.analytics_page = QWidget()
        self.analytics_page.setObjectName(u"analytics_page")
        self.main_windows_stackedWidget.addWidget(self.analytics_page)
        MainWindow.setCentralWidget(self.centralwidget)


        self.main_windows_stackedWidget.setCurrentIndex(0)
        self.dashboard_btn.clicked.connect(lambda: self.main_windows_stackedWidget.setCurrentIndex(0))
        self.cameras_btn.clicked.connect(lambda: self.main_windows_stackedWidget.setCurrentIndex(1))
        self.settings_btn.clicked.connect(lambda: self.main_windows_stackedWidget.setCurrentIndex(2))
        self.analytics_btn.clicked.connect(lambda: self.main_windows_stackedWidget.setCurrentIndex(3))

        self.add_new_cam_btn.clicked.connect(self.add_new_cam_dialog)

        # self.dashboard_thread = Thread(target=self.update_dashboard, args=())
        # self.dashboard_thread.daemon = True
        # self.dashboard_thread.start()


        timer = QTimer(self, interval=1000, timeout=self.update_dashboard)
        timer.start()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dashboard_btn.setText("")
        self.cameras_btn.setText("")
        self.settings_btn.setText("")
        self.analytics_btn.setText("")
        self.add_new_cam_btn.setText(QCoreApplication.translate("MainWindow", u"Add camera", None))
    # retranslateUi


    def add_new_cam_dialog(self):
        Dialog = QDialog()
        adding_new_cam = Ui_Add_new_cam_dialog()
        adding_new_cam.setupUi(Dialog)
        Dialog.show()
        Dialog.exec()

    def update_dashboard(self):
        self.clock_lcdNumber.display(strftime("%H:%M"))  # show locaL time
        self.cpu_load_lcdNumber.display(psutil.cpu_percent(interval=None))  # show CPU load
        self.ram_load_lcdNumber.display(psutil.virtual_memory().percent)  # show RAM load
        self.gpu_load_lcdNumber.display(GPUtil.getGPUs()[0].load)  # show GPU load



