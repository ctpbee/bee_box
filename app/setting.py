import os
import re

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QFileDialog

from app.lib.global_var import G
from app.lib.path_lib import beebox_path
from app.py_manage import PyManageWidget
from app.ui.ui_setting import Ui_Setting


class SettingWidget(QWidget, Ui_Setting):
    def __init__(self, ):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        ## button
        self.py_manage = PyManageWidget(self)
        self.py_manage_layout.addWidget(self.py_manage)
        self.install_btn.clicked.connect(self.install_path_slot)
        ## pypi
        self.pypi_checkBox.stateChanged.connect(self.pypi_use_slot)
        self.change_pypi_btn.clicked.connect(self.pypi_change_slot)
        self.load_setting()

    def load_setting(self):
        self.install_path.setText(G.config.install_path)

    def install_path_slot(self):
        path = QFileDialog.getExistingDirectory(self, "安装路径", beebox_path)
        if not path:
            return
        if os.path.exists(path) and os.path.isdir(path):
            G.config.install_path = path
            self.install_path.setText(path)

    def pypi_use_slot(self):
        if self.pypi_checkBox.isChecked():
            G.config.pypi_use = True
        else:
            G.config.pypi_use = False

    def pypi_change_slot(self):
        i_ = self.pypi_source.text().strip()
        if i_ and re.match(r"^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w .-]*)*/?$", i_):
            G.config.pypi_source = i_
        else:
            self.pypi_source.setText(G.config.pypi_source)
