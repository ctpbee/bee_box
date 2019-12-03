# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_env.ui',
# licensing of 'modify_env.ui' applies.
#
# Created: Tue Dec  3 18:03:08 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Modify(object):
    def setupUi(self, Modify):
        Modify.setObjectName("Modify")
        Modify.resize(424, 130)
        self.verticalLayout = QtWidgets.QVBoxLayout(Modify)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Modify)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name = QtWidgets.QLineEdit(Modify)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Modify)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.path = QtWidgets.QLineEdit(Modify)
        self.path.setObjectName("path")
        self.horizontalLayout_2.addWidget(self.path)
        self.path_btn = QtWidgets.QToolButton(Modify)
        self.path_btn.setObjectName("path_btn")
        self.horizontalLayout_2.addWidget(self.path_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.save_btn = QtWidgets.QPushButton(Modify)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_3.addWidget(self.save_btn)
        self.cancel_btn = QtWidgets.QPushButton(Modify)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Modify)
        QtCore.QMetaObject.connectSlotsByName(Modify)

    def retranslateUi(self, Modify):
        Modify.setWindowTitle(QtWidgets.QApplication.translate("Modify", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Modify", "名称", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Modify", "路径", None, -1))
        self.path_btn.setText(QtWidgets.QApplication.translate("Modify", "...", None, -1))
        self.save_btn.setText(QtWidgets.QApplication.translate("Modify", "保存", None, -1))
        self.cancel_btn.setText(QtWidgets.QApplication.translate("Modify", "取消", None, -1))

