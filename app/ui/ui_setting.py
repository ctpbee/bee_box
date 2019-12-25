# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui',
# licensing of 'setting.ui' applies.
#
# Created: Wed Dec 25 11:07:30 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(601, 537)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/CTPBEE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Setting.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Setting)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Setting)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.py_manage_layout = QtWidgets.QVBoxLayout()
        self.py_manage_layout.setObjectName("py_manage_layout")
        self.verticalLayout_4.addLayout(self.py_manage_layout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pypi_source = QtWidgets.QLineEdit(self.tab_2)
        self.pypi_source.setObjectName("pypi_source")
        self.verticalLayout_2.addWidget(self.pypi_source)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.change_pypi_btn = QtWidgets.QPushButton(self.tab_2)
        self.change_pypi_btn.setObjectName("change_pypi_btn")
        self.horizontalLayout_2.addWidget(self.change_pypi_btn)
        self.pypi_checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.pypi_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pypi_checkBox.setChecked(True)
        self.pypi_checkBox.setObjectName("pypi_checkBox")
        self.horizontalLayout_2.addWidget(self.pypi_checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.install_path = QtWidgets.QLineEdit(self.tab_3)
        self.install_path.setReadOnly(True)
        self.install_path.setObjectName("install_path")
        self.horizontalLayout.addWidget(self.install_path)
        self.install_btn = QtWidgets.QPushButton(self.tab_3)
        self.install_btn.setObjectName("install_btn")
        self.horizontalLayout.addWidget(self.install_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Setting)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QtWidgets.QApplication.translate("Setting", "设置", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("Setting", "Python解释器", None, -1))
        self.pypi_source.setText(QtWidgets.QApplication.translate("Setting", "https://pypi.douban.com/simple", None, -1))
        self.change_pypi_btn.setText(QtWidgets.QApplication.translate("Setting", "修改", None, -1))
        self.pypi_checkBox.setText(QtWidgets.QApplication.translate("Setting", "启用", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("Setting", "PyPi", None, -1))
        self.install_btn.setText(QtWidgets.QApplication.translate("Setting", "选择安装路径", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("Setting", "安装路径", None, -1))

import app.resource.bee_box_rc
