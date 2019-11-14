from PySide2.QtWidgets import QWidget

from app.ui.ui_home import Ui_Home
from app.global_var import G


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.setting_btn.clicked.connect(self.setting_click)
        self.ready_action()

    def ready_action(self):
        pass

    def setting_click(self):
        self.mainwindow.setting_handler()
