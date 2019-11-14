# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui',
# licensing of 'setting.ui' applies.
#
# Created: Thu Nov 14 10:38:10 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(401, 560)
        self.verticalLayout = QtWidgets.QVBoxLayout(Setting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.back_btn = QtWidgets.QPushButton(Setting)
        self.back_btn.setMaximumSize(QtCore.QSize(70, 16777215))
        self.back_btn.setStyleSheet("font: 75 11pt \"Arial\";")
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout.addWidget(self.back_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QtWidgets.QApplication.translate("Setting", "Form", None, -1))
        self.back_btn.setText(QtWidgets.QApplication.translate("Setting", "< back", None, -1))

