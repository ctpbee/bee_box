import sys

from PySide2.QtCore import Qt, QThreadPool, QEvent, QObject
from PySide2.QtGui import QIcon, QCloseEvent, QFocusEvent
from PySide2.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QDialog, \
    QDesktopWidget, QLabel, QProgressBar, QWidget

from app.lib.global_var import G
from app.ui.ui_mainwindow import Ui_MainWindow
from app.home import HomeWidget
from app.setting import SettingWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.layout_init()
        self.tray_init()
        G.thread_pool = self.thread_pool = QThreadPool()
        self.installEventFilter(self)
        # 主界面
        self.widget = HomeWidget(self)
        self.setCentralWidget(self.widget)
        self.setting_widget = SettingWidget(self)

    def layout_init(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
        self.desktop = QDesktopWidget()
        taskbar_height = self.desktop.screenGeometry().height() - self.desktop.availableGeometry().height()  # 任务栏高度
        self.move((self.desktop.availableGeometry().width() - self.width() - 15),
                  self.desktop.availableGeometry().height() - self.height() - taskbar_height + 30)  # 初始化位置到右下角
        self.progressbar = QProgressBar()
        self.progressbar.setFixedHeight(1)
        self.progressbar.setRange(0, 0)
        self.progressbar.setTextVisible(False)
        self.statusBar.addPermanentWidget(self.progressbar, stretch=10)

    def tray_init(self):
        icon = QIcon("app/resource/icon/bee.png")
        menu = QMenu()
        settingAction = menu.addAction("⚙  设置")
        exitAction = menu.addAction("❎  退出")
        settingAction.triggered.connect(self.setting_handler)
        exitAction.triggered.connect(self.close)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.iconActivated)
        self.tray.show()
        self.tray.setToolTip("~ bee box")

    def setting_handler(self):
        self.setting_widget.show()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.WindowDeactivate:
            self.hide()
        return super(self.__class__, self).eventFilter(watched, event)

    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            if self.isHidden():
                self.show()
            else:
                self.hide()
