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
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import psutil
import resources
from time import gmtime, strftime

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
        self.widget = QWidget(self.left_menu_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 41, 130))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.widget)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        icon = QIcon()
        icon.addFile(u":/media/icons/dashboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon)
        self.dashboard_btn.setIconSize(QSize(24, 24))
        self.dashboard_btn.setCheckable(True)
        self.dashboard_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_btn)

        self.cameras_btn = QPushButton(self.widget)
        self.cameras_btn.setObjectName(u"cameras_btn")
        icon1 = QIcon()
        icon1.addFile(u":/media/icons/cameras.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameras_btn.setIcon(icon1)
        self.cameras_btn.setIconSize(QSize(24, 24))
        self.cameras_btn.setCheckable(True)
        self.cameras_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cameras_btn)

        self.settings_btn = QPushButton(self.widget)
        self.settings_btn.setObjectName(u"settings_btn")
        icon2 = QIcon()
        icon2.addFile(u":/media/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon2)
        self.settings_btn.setIconSize(QSize(24, 24))
        self.settings_btn.setCheckable(True)
        self.settings_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_btn)

        self.analytics_btn = QPushButton(self.widget)
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
        self.clock_lcdNumber.display(strftime("%H:%M")) # show locaL time
        self.cpu_load_widget = QWidget(self.dashboard_page)
        self.cpu_load_widget.setObjectName(u"cpu_load_widget")
        self.cpu_load_widget.setGeometry(QRect(150, 40, 120, 80))
        self.cpu_load_lcdNumber = QLCDNumber(self.cpu_load_widget)
        self.cpu_load_lcdNumber.setObjectName(u"cpu_load_lcdNumber")
        self.cpu_load_lcdNumber.setGeometry(QRect(3, 2, 111, 71))
        self.cpu_load_lcdNumber.display(psutil.cpu_percent(interval=None)) # show CPU load
        self.ram_load_widget = QWidget(self.dashboard_page)
        self.ram_load_widget.setObjectName(u"gpu_load_widget")
        self.ram_load_widget.setGeometry(QRect(280, 40, 120, 80))
        self.ram_load_lcdNumber = QLCDNumber(self.ram_load_widget)
        self.ram_load_lcdNumber.setObjectName(u"gpu_load_lcdNumber")
        self.ram_load_lcdNumber.setGeometry(QRect(3, 2, 111, 71))
        self.ram_load_lcdNumber.display(psutil.virtual_memory().percent) # show RAM load
        self.main_windows_stackedWidget.addWidget(self.dashboard_page)
        self.cameras_page = QWidget()
        self.cameras_page.setObjectName(u"cameras_page")
        self.main_windows_stackedWidget.addWidget(self.cameras_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.main_windows_stackedWidget.addWidget(self.settings_page)
        self.analytics_page = QWidget()
        self.analytics_page.setObjectName(u"analytics_page")
        self.main_windows_stackedWidget.addWidget(self.analytics_page)


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
    # retranslateUi

