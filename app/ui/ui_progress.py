# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressmsg.ui',
# licensing of 'progressmsg.ui' applies.
#
# Created: Tue Dec 24 20:12:47 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 114)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msg = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.msg.setFont(font)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.verticalLayout.addWidget(self.msg)
        self.progress = QtWidgets.QProgressBar(Form)
        self.progress.setMaximum(0)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.verticalLayout.addWidget(self.progress)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.msg.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))

