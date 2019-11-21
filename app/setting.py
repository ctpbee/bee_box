import os
import re

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QFileDialog, QDialog
from app.lib.global_var import G
from app.ui.ui_setting import Ui_Setting
from app.lib.path_lib import get_py_version, beebox_path


class SettingWidget(QDialog, Ui_Setting):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.ready_action()
        ##  path
        self.py_path_box.currentIndexChanged.connect(self.py_path_change_slot)
        ## button
        self.py_path_btn.clicked.connect(self.py_path_slot)
        self.install_btn.clicked.connect(self.install_path_slot)
        ## pypi
        self.pypi_checkBox.stateChanged.connect(self.pypi_use_slot)
        self.change_pypi_btn.clicked.connect(self.pypi_change_slot)

    def ready_action(self):
        for i in G.config.python_path.values():
            self.py_path_box.addItem(i)
        curr_py = G.config.python_path.get(G.config.choice_python)
        if curr_py:
            self.py_path_box.setCurrentText(curr_py)

        self.install_path.setText(G.config.install_path)

    def py_path_change_slot(self):
        path = self.py_path_box.currentText()
        if path != '未选择':
            try:
                version = get_py_version(path)
            except:
                self.tip("py", False)
                return
            G.config.choice_python = version
            self.py_path_box.setCurrentText(path)
            self.mainwindow.widget.py_version.setText(version)
            self.tip("py")
        else:
            self.tip("py", False)

    def py_path_slot(self):
        path, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Python (*.exe))')
        if not path:
            return
        self.py_path_box.addItem(path)
        self.py_path_box.setCurrentText(path)
        version = get_py_version(path)
        G.config.python_path.update({version: path})
        G.config.choice_python = version
        self.mainwindow.widget.py_version.setText(version)
        self.tip("py")

    def install_path_slot(self):
        path = QFileDialog.getExistingDirectory(self, "安装路径", beebox_path)
        if not path:
            return
        if os.path.exists(path) and os.path.isdir(path):
            G.config.install_path = path
            self.install_path.setText(path)
            self.tip("install")
        else:
            self.tip("install", False)

    def pypi_use_slot(self):
        if self.pypi_checkBox.isChecked():
            G.config.pypi_use = True
        else:
            G.config.pypi_use = False
        self.tip("pypi")

    def pypi_change_slot(self):
        i_ = self.pypi_source.text().strip()
        if i_ and re.match(r"^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w .-]*)*/?$", i_):
            G.config.pypi_source = i_
            self.tip("pypi")
        else:
            self.tip("pypi", False)

    def tip(self, which, flag=True):
        ss = {
            "pypi": self.pypi_tip,
            "install": self.install_tip,
            "py": self.py_path_tip}
        for i, w in ss.items():
            if i == which:
                if flag:
                    w.setStyleSheet('color:Green')
                    w.setText("√ success")
                else:
                    w.setStyleSheet('color:Red')
                    w.setText("× error")
            else:
                w.setText("")

