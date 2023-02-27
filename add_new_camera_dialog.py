# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_camera2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QCheckBox, QDialogButtonBox)


class Ui_Add_new_cam_dialog(object):

    def __init__(self):
        self.choice_value = None

    def setupUi(self, Add_new_cam_dialog):
        if not Add_new_cam_dialog.objectName():
            Add_new_cam_dialog.setObjectName(u"Add_new_cam_dialog")
        Add_new_cam_dialog.resize(400, 120)
        self.buttonBox = QDialogButtonBox(Add_new_cam_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 80, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.rtsp_checkBox = QCheckBox(Add_new_cam_dialog)
        self.rtsp_checkBox.setObjectName(u"rtsp_checkBox")
        self.rtsp_checkBox.setGeometry(QRect(10, 30, 61, 21))
        self.onvif_checkBox = QCheckBox(Add_new_cam_dialog)
        self.onvif_checkBox.setObjectName(u"onvif_checkBox")
        self.onvif_checkBox.setGeometry(QRect(10, 50, 70, 17))
        self.webcam_checkBox = QCheckBox(Add_new_cam_dialog)
        self.webcam_checkBox.setObjectName(u"webcam_checkBox")
        self.webcam_checkBox.setGeometry(QRect(10, 10, 70, 21))

        self.retranslateUi(Add_new_cam_dialog)
        self.buttonBox.accepted.connect(Add_new_cam_dialog.accept)
        self.buttonBox.accepted.connect(self.return_choice)
        self.buttonBox.rejected.connect(Add_new_cam_dialog.reject)

        QMetaObject.connectSlotsByName(Add_new_cam_dialog)

    # setupUi

    def retranslateUi(self, Add_new_cam_dialog):
        Add_new_cam_dialog.setWindowTitle(QCoreApplication.translate("Add_new_cam_dialog", u"Add new camera", None))
        self.rtsp_checkBox.setText(QCoreApplication.translate("Add_new_cam_dialog", u"RTSP", None))
        self.onvif_checkBox.setText(QCoreApplication.translate("Add_new_cam_dialog", u"Onvif", None))
        self.webcam_checkBox.setText(QCoreApplication.translate("Add_new_cam_dialog", u"Webcam", None))

    # retranslateUi

    "____________________________________________________"
    # Return choice from dialog

    def return_choice(self):
        if self.rtsp_checkBox.isChecked():
            self.choice_value = 'rtsp'
        elif self.onvif_checkBox.isChecked():
            self.choice_value = 'onvif'
        elif self.webcam_checkBox.isChecked():
            self.choice_value = 'webcam'
