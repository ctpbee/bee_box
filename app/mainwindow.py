import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QCloseEvent
from PySide2.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QDialog, \
    QDesktopWidget
from app.ui.ui_mainwindow import Ui_MainWindow
from app.home import HomeWidget
from app.setting import SettingWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.exit_ = False
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
        self.desktop = QDesktopWidget()
        taskbar_height = self.desktop.screenGeometry().height() - self.desktop.availableGeometry().height()  # 任务栏高度
        self.move((self.desktop.availableGeometry().width() - self.width()),
                  self.desktop.availableGeometry().height() - self.height() - taskbar_height)  # 初始化位置到右下角
        self.tray_init()
        self.home_handler()
        # 默认打开

    def tray_init(self):
        icon = QIcon("app/resource/icon/bee.png")
        menu = QMenu()
        settingAction = menu.addAction("设置")
        exitAction = menu.addAction("退出")
        settingAction.triggered.connect(self.menu_setting_handler)
        exitAction.triggered.connect(self.quit)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.iconActivated)
        self.tray.show()
        self.tray.setToolTip("bee boxs")

    def home_handler(self):
        self.widget = HomeWidget(self)
        self.setCentralWidget(self.widget)

    def menu_setting_handler(self):
        self.show()
        self.setting_handler()

    def setting_handler(self):
        self.widget = SettingWidget(self)
        self.setCentralWidget(self.widget)

    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def quit(self):
        self.exit_ = True
        self.close()

    def closeEvent(self, event: QCloseEvent):
        if self.exit_:
            self.tray.hide()
            event.accept()
        else:
            self.hide()
            event.ignore()
