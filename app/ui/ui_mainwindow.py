# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Fri Nov 15 13:28:14 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 662)
        MainWindow.setMinimumSize(QtCore.QSize(433, 662))
        MainWindow.setMaximumSize(QtCore.QSize(433, 662))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/bee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "bee box", None, -1))

import app.resource.bee_box_rc
