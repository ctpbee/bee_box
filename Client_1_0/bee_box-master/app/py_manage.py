import re

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QWidget, QFileDialog

# from app.home import HomeWidget
from app.lib.global_var import G
from app.lib.path_lib import get_py_version
from app.ui.ui_py_manage import Ui_Form


class PyManageWidget(QWidget, Ui_Form):
    def __init__(self, home):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.home = home
        self.name_allow = True
        self.path_allow = True
        self.name.textChanged.connect(self.name_change_slot)
        self.cancel_btn.clicked.connect(self.cancel_slot)
        self.check_btn.clicked.connect(self.check_slot)
        self.path_btn.clicked.connect(self.path_slot)
        self.save_btn.clicked.connect(self.save_slot)
        self.del_btn.clicked.connect(self.del_slot)

    def cancel_slot(self):
        self.close()

    def check_slot(self):
        name = self.name.text()
        G.config.choice_python = name
        self.home.curr_py_path.setText(self.name.text())
        self.home.py_version.setText(name)
        self.save_slot()
        self.check_btn.setDisabled(True)

    def path_slot(self):
        path, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Python (*.exe))')
        if not path:
            return
        version = get_py_version(path)
        if version:
            self.path.setText(path)
            self.path_allow = True
            if self.name_allow:
                self.save_btn.setEnabled(True)
        else:
            self.path_allow = False
            self.path.setText("无效路径")
            self.save_btn.setDisabled(True)

    def del_slot(self):
        name = self.name.text()
        if name.strip() and name in G.config.python_path:
            G.config.python_path.pop(name)
            G.config.to_file()
            if name == G.config.choice_python:
                G.config.choice_python = ""
                self.home.curr_py_path.setText(G.config.choice_python)
                self.home.py_version.setText(G.config.choice_python)
        self.close()

    def save_slot(self):
        name = self.name.text()
        path = self.path.text()
        G.config.python_path.update({name: path})
        G.config.to_file()

    def name_change_slot(self):
        name = self.name.text()
        if name.strip() and name not in G.config.python_path:
            self.name_allow = True
            self.name.setStyleSheet("color:green")
            if self.path.text().strip() and self.path_allow:
                self.save_btn.setEnabled(True)
        else:
            self.name_allow = False
            self.name.setStyleSheet("color:red")
            self.save_btn.setDisabled(True)

    def closeEvent(self, event: QCloseEvent):
        self.home.py_path_table.setRowCount(0)
        self.home.load_setting()
        event.accept()
