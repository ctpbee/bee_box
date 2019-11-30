from PySide2.QtCore import Slot, QObject, Signal
from PySide2.QtWidgets import QWidget, QFileDialog
from app.lib.path_lib import get_py_version, beebox_path
import os
import re

from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import all_app, Actions


class HomeJob(QObject):
    install_signal = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()


qss = """
QWidget,#setting_btn{
background:#000000;
color:#ffffff
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
        ##  path
        self.py_path_box.currentIndexChanged.connect(self.py_path_change_slot)
        ## button
        self.py_path_btn.clicked.connect(self.py_path_slot)
        self.install_btn.clicked.connect(self.install_path_slot)
        ## pypi
        self.pypi_checkBox.stateChanged.connect(self.pypi_use_slot)
        self.change_pypi_btn.clicked.connect(self.pypi_change_slot)
        self.setting_btn.clicked.connect(self.setting_click)
        self.back_btn.clicked.connect(self.back_slot)
        self.job.install_signal.connect(self.add_installed_layout_slot)
        ## app
        self.ready_action()

    def setting_click(self):
        self.stackedWidget.setCurrentIndex(1)

    def back_slot(self):
        self.stackedWidget.setCurrentIndex(0)

    def ready_action(self):
        p_ = G.config.choice_python
        if p_: self.py_version.setText(p_)
        # 添加布局
        # 已安装
        for pack_name, cfg in G.config.installed_apps.items():
            app_cls = all_app[cfg['cls_name']]
            app = app_cls(widget=self, **cfg)
            setattr(self, app.pack_name, app)
            self.installed_layout.addLayout(app.div.layout)
        # 所有app
        for app_cls in all_app.values():
            app = app_cls(widget=self, action=Actions.DOWNLOAD)
            setattr(self, app.ui_name, app)
            self.apps_layout.addLayout(app.div.layout)
        ##设置
        for i in G.config.python_path.values():
            self.py_path_box.addItem(i)
        curr_py = G.config.python_path.get(G.config.choice_python)
        if curr_py:
            self.py_path_box.setCurrentText(curr_py)
        self.install_path.setText(G.config.install_path)

    @Slot(dict)
    def add_installed_layout_slot(self, data):
        app_cls = all_app[data['cls_name']]
        ##
        app = app_cls(widget=self, **data)
        setattr(self, app.pack_name, app)
        self.installed_layout.addLayout(app.div.layout)

    def py_path_change_slot(self):
        path = self.py_path_box.currentText()
        try:
            version = get_py_version(path)
        except:
            return
        G.config.choice_python = version
        self.py_path_box.setCurrentText(path)
        self.py_version.setText(version)

    def py_path_slot(self):
        path, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'Python (*.exe))')
        if not path:
            return
        self.py_path_box.addItem(path)
        self.py_path_box.setCurrentText(path)
        version = get_py_version(path)
        G.config.python_path.update({version: path})
        G.config.choice_python = version
        self.py_version.setText(version)

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
