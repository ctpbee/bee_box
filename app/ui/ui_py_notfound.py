# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_dialog.ui',
# licensing of 'msg_dialog.ui' applies.
#
# Created: Tue Nov 19 15:40:22 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 166)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msg = QtWidgets.QLabel(Dialog)
        self.msg.setStyleSheet("font: 75 italic 20pt \"Arial\";")
        self.msg.setText("")
        self.msg.setObjectName("msg")
        self.verticalLayout.addWidget(self.msg)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.commandLinkButton.setText(QtWidgets.QApplication.translate("Dialog", "前往下载", None, -1))

