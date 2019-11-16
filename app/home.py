from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget

from app.honey.base import Actions
from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import all_app


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.setting_btn.clicked.connect(self.setting_click)
        self.mainwindow.job.install_signal.connect(self.install_slot)
        ## app
        self.ready_action()

    def ready_action(self):
        self.py_version.setText(G.config.choice_python)
        for app_cls in all_app:
            app = app_cls(self, "apps", Actions.INSTALL)
            setattr(self, app.ui_name, app)
            self.apps_layout.addLayout(app.div.layout)

    @Slot(dict)
    def install_slot(self, data):
        app_cls = data['cls']
        action = data['action']
        ##
        app = app_cls(self, 'installed', action)
        setattr(self, app.ui_name, app)
        self.installed_layout.addLayout(app.div.layout)

    def setting_click(self):
        self.mainwindow.setting_handler()
