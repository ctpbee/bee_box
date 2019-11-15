# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Fri Nov 15 16:14:42 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(460, 680)
        self.verticalLayout = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Home)
        self.label.setStyleSheet("font: 75 italic 40pt \"Arial\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.py_version = QtWidgets.QLabel(Home)
        self.py_version.setObjectName("py_version")
        self.verticalLayout_3.addWidget(self.py_version)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.setting_btn = QtWidgets.QPushButton(Home)
        self.setting_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.setting_btn.setFlat(True)
        self.setting_btn.setObjectName("setting_btn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.setting_btn)
        self.horizontalLayout.addLayout(self.formLayout)
        self.horizontalLayout.setStretch(0, 9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(Home)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 438, 573))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.install_layout = QtWidgets.QVBoxLayout()
        self.install_layout.setObjectName("install_layout")
        self.verticalLayout_6.addLayout(self.install_layout)
        self.apps_layout = QtWidgets.QVBoxLayout()
        self.apps_layout.setObjectName("apps_layout")
        self.verticalLayout_6.addLayout(self.apps_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(1, 8)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(QtWidgets.QApplication.translate("Home", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Home", "bee box", None, -1))
        self.py_version.setText(QtWidgets.QApplication.translate("Home", "Python版本", None, -1))
        self.setting_btn.setText(QtWidgets.QApplication.translate("Home", "⚙", None, -1))

