# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressmsg.ui',
# licensing of 'progressmsg.ui' applies.
#
# Created: Thu Dec 12 11:49:48 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(312, 124)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msg = QtWidgets.QLabel(Form)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.verticalLayout.addWidget(self.msg)
        self.progress = QtWidgets.QProgressBar(Form)
        self.progress.setMaximum(0)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.verticalLayout.addWidget(self.progress)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.msg.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))

