from PySide2.QtWidgets import QWidget
from app.ui.ui_setting import Ui_Setting


class SettingWidget(QWidget, Ui_Setting):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.back_btn.clicked.connect(self.back_click)

    def back_click(self):
        self.mainwindow.home_handler()
