# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Thu Nov 14 16:25:29 2019
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
        self.py_version = QtWidgets.QLabel(Home)
        self.py_version.setText("")
        self.py_version.setObjectName("py_version")
        self.horizontalLayout_2.addWidget(self.py_version)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Home)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(Home)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Home)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(Home)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(4, 7)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(QtWidgets.QApplication.translate("Home", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Home", "bee box", None, -1))
        self.setting_btn.setText(QtWidgets.QApplication.translate("Home", "⚙", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Home", "当前Python版本：", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Home", "桌面端", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Home", "安装", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Home", "client", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Home", "部署", None, -1))

