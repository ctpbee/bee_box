# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'py_manage.ui',
# licensing of 'py_manage.ui' applies.
#
# Created: Wed Dec 25 11:07:58 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(702, 578)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/CTPBEE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.py_box = QtWidgets.QComboBox(Form)
        self.py_box.setObjectName("py_box")
        self.horizontalLayout_3.addWidget(self.py_box)
        self.py_setting_btn = QtWidgets.QToolButton(Form)
        self.py_setting_btn.setObjectName("py_setting_btn")
        self.horizontalLayout_3.addWidget(self.py_setting_btn)
        self.horizontalLayout_3.setStretch(1, 9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.path = QtWidgets.QLabel(Form)
        self.path.setText("")
        self.path.setObjectName("path")
        self.verticalLayout.addWidget(self.path)
        self.pip_list = QtWidgets.QListWidget(Form)
        self.pip_list.setObjectName("pip_list")
        self.verticalLayout.addWidget(self.pip_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.app_name = QtWidgets.QLabel(Form)
        self.app_name.setText("")
        self.app_name.setObjectName("app_name")
        self.horizontalLayout.addWidget(self.app_name)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.cur_py = QtWidgets.QLabel(Form)
        self.cur_py.setObjectName("cur_py")
        self.horizontalLayout.addWidget(self.cur_py)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.set_app_py = QtWidgets.QPushButton(Form)
        self.set_app_py.setObjectName("set_app_py")
        self.verticalLayout.addWidget(self.set_app_py)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Python路径", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Python解释器", None, -1))
        self.py_setting_btn.setText(QtWidgets.QApplication.translate("Form", "⚙", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "当前：", None, -1))
        self.cur_py.setText(QtWidgets.QApplication.translate("Form", "空", None, -1))
        self.set_app_py.setText(QtWidgets.QApplication.translate("Form", "选为解释器", None, -1))

import app.resource.bee_box_rc
