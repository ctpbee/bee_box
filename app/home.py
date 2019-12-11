from PySide2 import QtGui
from PySide2.QtCore import Slot, QObject, Signal
from PySide2.QtWidgets import QWidget
from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import all_app
from app.setting import SettingWidget


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
        # self.setStyleSheet(qss)
        self.mainwindow = mainwindow
        self.job = HomeJob()
        ## button
        self.setting_btn.clicked.connect(self.setting_click)
        ## pypi
        self.job.install_signal.connect(self.add_installed_layout_slot)
        self.ready_action()

    def setting_click(self):
        self.setting_widget = SettingWidget()
        self.setting_widget.show()

    def ready_action(self):
        self.init_ui()

    def init_ui(self):
        # 添加布局
        # 已安装
        [all_app[cfg['cls_name']](self, **cfg) for pack_name, cfg in G.config.installed_apps.items()]
        # 所有app
        [app_cls(self) for app_cls in all_app.values()]
        # py_manage

    @Slot(dict)
    def add_installed_layout_slot(self, data):
        app_cls = all_app[data['cls_name']]
        app_cls(self, **data)

    def closeEvent(self, event: QtGui.QCloseEvent):
        try:
            self.setting_widget.close()
        except:
            pass
        event.accept()
