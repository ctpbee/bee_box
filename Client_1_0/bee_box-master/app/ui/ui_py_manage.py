# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'py_manage.ui',
# licensing of 'py_manage.ui' applies.
#
# Created: Sat Nov 30 22:10:39 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 148)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path = QtWidgets.QLabel(Form)
        self.path.setText("")
        self.path.setObjectName("path")
        self.horizontalLayout.addWidget(self.path)
        self.path_btn = QtWidgets.QToolButton(Form)
        self.path_btn.setObjectName("path_btn")
        self.horizontalLayout.addWidget(self.path_btn)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.del_btn = QtWidgets.QPushButton(Form)
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout_2.addWidget(self.del_btn)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.check_btn = QtWidgets.QPushButton(Form)
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout_3.addWidget(self.check_btn)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Python路径", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "name", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "path", None, -1))
        self.path_btn.setText(QtWidgets.QApplication.translate("Form", "...", None, -1))
        self.save_btn.setText(QtWidgets.QApplication.translate("Form", "保存", None, -1))
        self.cancel_btn.setText(QtWidgets.QApplication.translate("Form", "取消", None, -1))
        self.del_btn.setText(QtWidgets.QApplication.translate("Form", "删除", None, -1))
        self.check_btn.setText(QtWidgets.QApplication.translate("Form", "选为当前解释器", None, -1))

