from PySide2.QtCore import Slot, QObject, Signal, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QAbstractItemView, QMenu
from app.lib.path_lib import get_py_version, beebox_path
import os
import re

from app.py_manage import PyManageWidget
from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import all_app, Actions


class HomeJob(QObject):
    install_signal = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()


qss = """
QWidget,#setting_btn,#app_setting_btn{
background:#ffffff;
color:#000000
}

#line,#line_2{
background:#ffffff;
}
QPushButton,QToolButton{
    border-style: none;  
    border: 0px;  
    color: #F0F0F0;  
    padding: 5px;     
    border-radius:5px;  
    background: #1B89CA
}
QPushButton:disable,QToolButton:disable{
background:#f0f0f0;
color:#202020
}

QPushButton:hover,QToolButton:hover{
    background: #5CACEE  

}
QLabel:hover{
color:#00c1c1
}
QPushButton:pressed,QToolButton:pressed{   
    background: #1B89CA
}  

"""


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.mainwindow = mainwindow
        self.job = HomeJob()
        ## button
        self.install_btn.clicked.connect(self.install_path_slot)
        self.setting_btn.clicked.connect(self.setting_click)
        self.back_btn.clicked.connect(self.back_slot)
        ## pypi
        self.pypi_checkBox.stateChanged.connect(self.pypi_use_slot)
        self.change_pypi_btn.clicked.connect(self.pypi_change_slot)
        self.job.install_signal.connect(self.add_installed_layout_slot)
        self.ready_action()

    def setting_click(self):
        self.stackedWidget.setCurrentIndex(1)

    def back_slot(self):
        self.stackedWidget.setCurrentIndex(0)

    def ready_action(self):
        p_ = G.config.choice_python
        if p_:
            self.py_version.setText(p_)
        # self.load_setting()
        self.init_ui()

    def init_ui(self):
        # 添加布局
        # 已安装
        [all_app[cfg['cls_name']](self, **cfg) for pack_name, cfg in G.config.installed_apps.items()]
        # 所有app
        [app_cls(self) for app_cls in all_app.values()]
        # py_manage
        self.py_manager = PyManageWidget(self)
        self.py_manager.resize(self.mainwindow.size())
        self.py_manage_layout.addWidget(self.py_manager)

    def load_setting(self):
        self.install_path.setText(G.config.install_path)
        for k, v in G.config.python_path.items():
            self.py_path_table.insertRow(0)
            self.py_path_table.setItem(0, 0, QTableWidgetItem(str(k)))
            self.py_path_table.setItem(0, 1, QTableWidgetItem(str(v)))

    @Slot(dict)
    def add_installed_layout_slot(self, data):
        app_cls = all_app[data['cls_name']]
        app_cls(self, **data)

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
