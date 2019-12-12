0
1
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interpretes.ui',
# licensing of 'interpretes.ui' applies.
#
# Created: Thu Dec 12 19:17:41 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Interpreters(object):
    def setupUi(self, Interpreters):
        Interpreters.setObjectName("Interpreters")
        Interpreters.resize(743, 397)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Interpreters)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.py_table = QtWidgets.QTableWidget(Interpreters)
        self.py_table.setObjectName("py_table")
        self.py_table.setColumnCount(2)
        self.py_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.py_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.py_table.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.py_table)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_btn = QtWidgets.QToolButton(Interpreters)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout.addWidget(self.add_btn)
        self.del_btn = QtWidgets.QToolButton(Interpreters)
        self.del_btn.setObjectName("del_btn")
        self.verticalLayout.addWidget(self.del_btn)
        self.change_btn = QtWidgets.QToolButton(Interpreters)
        self.change_btn.setObjectName("change_btn")
        self.verticalLayout.addWidget(self.change_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Interpreters)
        QtCore.QMetaObject.connectSlotsByName(Interpreters)

    def retranslateUi(self, Interpreters):
        Interpreters.setWindowTitle(QtWidgets.QApplication.translate("Interpreters", "解释器", None, -1))
        self.py_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Interpreters", "名称", None, -1))
        self.py_table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Interpreters", "路径", None, -1))
        self.add_btn.setText(QtWidgets.QApplication.translate("Interpreters", "➕", None, -1))
        self.del_btn.setText(QtWidgets.QApplication.translate("Interpreters", "➖", None, -1))
        self.change_btn.setText(QtWidgets.QApplication.translate("Interpreters", "🖊", None, -1))

