from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget

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
            app = app_cls(self, "apps")
            setattr(self, app.ui_name, app)
            div = app.div
            div.icon.setStyleSheet(f"image: url({app.icon});")
            div.name.setText(app.name)
            div.desc.setText(app.desc)
            div.desc.url = app.app_url
            div.action.setText(app.action)
            div.action.clicked.connect(app.action_handler)
            self.apps_layout.addLayout(div.layout)

    @Slot(dict)
    def install_slot(self, data):
        app_cls = data['cls']
        action = data['action']
        version = data['version']
        ##
        app = app_cls(self, 'installed')
        app.action = action
        setattr(self, app.ui_name, app)
        div = app.div
        div.icon.setStyleSheet(f"image: url({app.icon});")
        div.name.setText(app.name)
        div.desc.setText(version)
        div.action.setText(app.action)
        div.action.clicked.connect(app.action_handler)
        self.installed_layout.addLayout(div.layout)

    def setting_click(self):
        self.mainwindow.setting_handler()
