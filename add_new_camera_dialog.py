# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_camera.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QWidget)

from add_new_camera_event import Newcamera

class Ui_Add_new_cam_dialog(object):

    signal = Signal(str)

    def setupUi(self, Add_new_cam_dialog):
        if not Add_new_cam_dialog.objectName():
            Add_new_cam_dialog.setObjectName(u"Add_new_cam_dialog")
        Add_new_cam_dialog.resize(400, 307)
        self.buttonBox = QDialogButtonBox(Add_new_cam_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 260, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.rtsp_checkBox = QCheckBox(Add_new_cam_dialog)
        self.rtsp_checkBox.setObjectName(u"rtsp_checkBox")
        self.rtsp_checkBox.setGeometry(QRect(10, 10, 61, 21))
        self.rtsp_link_lineEdit = QLineEdit(Add_new_cam_dialog)
        self.rtsp_link_lineEdit.setObjectName(u"rtsp_link_lineEdit")
        self.rtsp_link_lineEdit.setGeometry(QRect(10, 50, 371, 20))
        self.onvif_checkBox = QCheckBox(Add_new_cam_dialog)
        self.onvif_checkBox.setObjectName(u"onvif_checkBox")
        self.onvif_checkBox.setGeometry(QRect(10, 120, 70, 17))
        self.rtsp_link_label = QLabel(Add_new_cam_dialog)
        self.rtsp_link_label.setObjectName(u"rtsp_link_label")
        self.rtsp_link_label.setGeometry(QRect(10, 30, 151, 16))
        self.ip_address_label = QLabel(Add_new_cam_dialog)
        self.ip_address_label.setObjectName(u"ip_address_label")
        self.ip_address_label.setGeometry(QRect(10, 140, 61, 16))
        self.ip_address_lineEdit = QLineEdit(Add_new_cam_dialog)
        self.ip_address_lineEdit.setObjectName(u"ip_address_lineEdit")
        self.ip_address_lineEdit.setGeometry(QRect(70, 140, 311, 20))
        self.port_label = QLabel(Add_new_cam_dialog)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setGeometry(QRect(10, 170, 47, 13))
        self.port_spinBox = QSpinBox(Add_new_cam_dialog)
        self.port_spinBox.setObjectName(u"port_spinBox")
        self.port_spinBox.setGeometry(QRect(70, 170, 42, 22))
        self.port_spinBox.setMaximum(9999)
        self.port_spinBox.setValue(80)
        self.user_label = QLabel(Add_new_cam_dialog)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(10, 200, 47, 13))
        self.user_lineEdit = QLineEdit(Add_new_cam_dialog)
        self.user_lineEdit.setObjectName(u"user_lineEdit")
        self.user_lineEdit.setGeometry(QRect(70, 200, 311, 20))
        self.password_label = QLabel(Add_new_cam_dialog)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(10, 230, 51, 16))
        self.password_lineEdit = QLineEdit(Add_new_cam_dialog)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(70, 230, 311, 20))
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.rtsp_device_name_label = QLabel(Add_new_cam_dialog)
        self.rtsp_device_name_label.setObjectName(u"rtsp_device_name_label")
        self.rtsp_device_name_label.setGeometry(QRect(10, 70, 151, 16))
        self.rtsp_device_name_lineEdit = QLineEdit(Add_new_cam_dialog)
        self.rtsp_device_name_lineEdit.setObjectName(u"rtsp_device_name_lineEdit")
        self.rtsp_device_name_lineEdit.setGeometry(QRect(10, 90, 371, 20))

        self.retranslateUi(Add_new_cam_dialog)
        self.buttonBox.accepted.connect(Add_new_cam_dialog.accept)
        self.buttonBox.accepted.connect(self.add_new_camera)
        self.buttonBox.rejected.connect(Add_new_cam_dialog.reject)

        QMetaObject.connectSlotsByName(Add_new_cam_dialog)
    # setupUi

    def retranslateUi(self, Add_new_cam_dialog):
        Add_new_cam_dialog.setWindowTitle(QCoreApplication.translate("Add_new_cam_dialog", u"Add new camera", None))
        self.rtsp_checkBox.setText(QCoreApplication.translate("Add_new_cam_dialog", u"RTSP", None))
        self.onvif_checkBox.setText(QCoreApplication.translate("Add_new_cam_dialog", u"Onvif", None))
        self.rtsp_link_label.setText(
            QCoreApplication.translate("Add_new_cam_dialog", u"Please enter RTSP link:", None))
        self.ip_address_label.setText(QCoreApplication.translate("Add_new_cam_dialog", u"IP address:", None))
        self.port_label.setText(QCoreApplication.translate("Add_new_cam_dialog", u"Port:", None))
        self.user_label.setText(QCoreApplication.translate("Add_new_cam_dialog", u"User:", None))
        self.password_label.setText(QCoreApplication.translate("Add_new_cam_dialog", u"Password:", None))
        self.rtsp_device_name_label.setText(
            QCoreApplication.translate("Add_new_cam_dialog", u"Please enter device name:", None))

    # retranslateUi

    def add_new_camera(self):
        if self.rtsp_checkBox.isChecked():
            new_camera = Newcamera(self.rtsp_link_lineEdit.text(), self.rtsp_device_name_lineEdit.text())
            self.cameras_page_gridLayout.addWidget(new_camera.add_new_camera())
