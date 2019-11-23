from PySide2.QtCore import Slot, QObject, Signal
from PySide2.QtWidgets import QWidget

from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import all_app, Actions


class HomeJob(QObject):
    install_signal = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.job = HomeJob()
        self.setting_btn.clicked.connect(self.setting_click)
        self.job.install_signal.connect(self.add_installed_layout_slot)
        ## app
        self.ready_action()

    def setting_click(self):
        self.mainwindow.setting_handler()

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

    @Slot(dict)
    def add_installed_layout_slot(self, data):
        app_cls = all_app[data['cls_name']]
        ##
        app = app_cls(widget=self, **data)
        setattr(self, app.pack_name, app)
        self.installed_layout.addLayout(app.div.layout)
