# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Sat Dec  7 17:16:58 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(481, 734)
        self.verticalLayout = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head_widget = QtWidgets.QWidget(Home)
        self.head_widget.setObjectName("head_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.head_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.head_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setWeight(9)
        font.setItalic(True)
        font.setUnderline(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 italic 40pt \"Arial\";\n"
"color: rgb(255, 85, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.setting_btn = QtWidgets.QPushButton(self.head_widget)
        self.setting_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.setting_btn.setFlat(True)
        self.setting_btn.setObjectName("setting_btn")
        self.horizontalLayout.addWidget(self.setting_btn)
        self.verticalLayout.addWidget(self.head_widget)
        self.scrollArea = QtWidgets.QScrollArea(Home)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 607))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.installed_layout = QtWidgets.QVBoxLayout()
        self.installed_layout.setSpacing(20)
        self.installed_layout.setObjectName("installed_layout")
        self.verticalLayout_4.addLayout(self.installed_layout)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setMinimumSize(QtCore.QSize(0, 1))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.apps_layout = QtWidgets.QVBoxLayout()
        self.apps_layout.setSpacing(20)
        self.apps_layout.setObjectName("apps_layout")
        self.verticalLayout_4.addLayout(self.apps_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(1, 8)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(QtWidgets.QApplication.translate("Home", "Home", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Home", "bee box", None, -1))
        self.setting_btn.setText(QtWidgets.QApplication.translate("Home", "⚙", None, -1))

