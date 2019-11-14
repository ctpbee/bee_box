# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui',
# licensing of 'setting.ui' applies.
#
# Created: Thu Nov 14 19:12:44 2019
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Setting)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.py_path_box = QtWidgets.QComboBox(Setting)
        self.py_path_box.setObjectName("py_path_box")
        self.horizontalLayout.addWidget(self.py_path_box)
        self.py_path_btn = QtWidgets.QToolButton(Setting)
        self.py_path_btn.setObjectName("py_path_btn")
        self.horizontalLayout.addWidget(self.py_path_btn)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Setting)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.install_path = QtWidgets.QLineEdit(Setting)
        self.install_path.setObjectName("install_path")
        self.horizontalLayout_2.addWidget(self.install_path)
        self.install_btn = QtWidgets.QToolButton(Setting)
        self.install_btn.setObjectName("install_btn")
        self.horizontalLayout_2.addWidget(self.install_btn)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QtWidgets.QApplication.translate("Setting", "Form", None, -1))
        self.back_btn.setText(QtWidgets.QApplication.translate("Setting", "< back", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Setting", "python路径", None, -1))
        self.py_path_btn.setText(QtWidgets.QApplication.translate("Setting", "...", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Setting", "安装路径", None, -1))
        self.install_btn.setText(QtWidgets.QApplication.translate("Setting", "...", None, -1))

