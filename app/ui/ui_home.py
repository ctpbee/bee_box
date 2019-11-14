# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Thu Nov 14 10:32:03 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(374, 560)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Home)
        self.label.setStyleSheet("font: 75 italic 16pt \"Arial\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.setting_btn = QtWidgets.QPushButton(Home)
        self.setting_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.setting_btn.setFlat(True)
        self.setting_btn.setObjectName("setting_btn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.setting_btn)
        self.horizontalLayout.addLayout(self.formLayout)
        self.horizontalLayout.setStretch(0, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Home)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.py_version = QtWidgets.QComboBox(Home)
        self.py_version.setObjectName("py_version")
        self.horizontalLayout_2.addWidget(self.py_version)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 7)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(QtWidgets.QApplication.translate("Home", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Home", "bee boxs", None, -1))
        self.setting_btn.setText(QtWidgets.QApplication.translate("Home", "⚙", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Home", "Python版本：", None, -1))

