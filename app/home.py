import time

from PySide2.QtCore import QThread
from PySide2.QtWidgets import QWidget

from app.ui.ui_home import Ui_Home
from app.global_var import G
from app.download_handler import HttpReq


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.setting_btn.clicked.connect(self.setting_click)
        self.py_version.setText(G.config.choice_python)

        self.ready_action()
        self.pushButton.clicked.connect(self.download)

    def ready_action(self):
        pass

    def setting_click(self):
        self.mainwindow.setting_handler()

    def download(self):
        self.httpp = HttpReq()
        G.start_time = time.time()
        self.httpp.download_signal.emit(G.bee_box_url)
        self.httpp.moveToThread(self.mainwindow.t)
