from PySide2 import QtGui
from PySide2.QtCore import Slot, QObject, Signal
from PySide2.QtWidgets import QWidget, QMessageBox

from app.ui import qss
from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import all_app
from app.setting import SettingWidget
import webbrowser


class HomeJob(QObject):
    """ 安装成功后增加UI信号 """
    install_signal = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.mainwindow = mainwindow
        self.progressBar.setFixedHeight(3)
        self.job = HomeJob()
        ## button
        self.setting_btn.clicked.connect(self.setting_click)
        self.github.clicked.connect(self.github_click)
        self.qq.clicked.connect(self.qq_click)
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

    def qq_click(self):
        self.open_url("https://jq.qq.com/?_wv=1027&k=5xWbIq3")

    def github_click(self):
        self.open_url("https://github.com/ctpbee")

    def open_url(self, url):
        try:
            webbrowser.get('chrome').open_new_tab(url)
        except Exception as e:
            webbrowser.open_new_tab(url)
