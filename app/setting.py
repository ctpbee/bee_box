from PySide2.QtWidgets import QWidget, QFileDialog
import os
from app.global_var import G
from app.ui.ui_setting import Ui_Setting
from app.helper import get_py_version, beebox_path


class SettingWidget(QWidget, Ui_Setting):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow

        self.ready_action()
        ##  path
        self.py_path_box.currentIndexChanged.connect(self.py_path_change_slot)
        ## button
        self.back_btn.clicked.connect(self.back_slot)
        self.py_path_btn.clicked.connect(self.py_path_slot)
        self.install_btn.clicked.connect(self.install_path_slot)

    def ready_action(self):
        for i in G.config.python_path.values():
            self.py_path_box.addItem(i)
        self.py_path_box.setCurrentText(G.config.choice_python)
        self.install_path.setText(G.config.install_path)

    def back_slot(self):
        self.mainwindow.home_handler()

    def py_path_change_slot(self):
        path = self.py_path_box.currentText()
        G.config.choice_python = get_py_version(path)

    def py_path_slot(self):
        path, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Python (*.exe))')
        if not path: return
        self.py_path_box.addItem(path)
        self.py_path_box.setCurrentText(path)
        version = get_py_version(path)
        G.config.choice_python = version
        G.config.python_path.update({version: path})

    def install_path_slot(self):
        path = QFileDialog.getExistingDirectory(self, "安装路径", beebox_path)
        if not path: return
        G.config.install_path = path
        self.install_path.setText(path)
