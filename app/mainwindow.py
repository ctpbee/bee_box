from PySide2.QtCore import QThreadPool, QObject, Signal, Slot
from PySide2.QtGui import QIcon, QCloseEvent
from PySide2.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QDesktopWidget, QMessageBox

from app.lib.global_var import G
from app.ui.ui_mainwindow import Ui_MainWindow
from app.home import HomeWidget
from app.setting import SettingWidget


class Job(QObject):
    msg_box_signal = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.quit_ = False
        self.setupUi(self)
        self.job = Job()
        self.layout_init()
        self.tray_init()
        self.thread_pool = G.thread_pool = QThreadPool.globalInstance()
        self.installEventFilter(self)
        self.job.msg_box_signal.connect(self.msg_box_slot)
        # 主界面
        self.widget = HomeWidget(self)
        self.setCentralWidget(self.widget)
        self.ready_action()


    def ready_action(self):
        if not G.config.choice_python:
            self.setting_widget = SettingWidget(self)
            self.setting_widget.exec_()

    @Slot(dict)
    def msg_box_slot(self, data):
        QMessageBox.information(self, "bee box", data['msg'], QMessageBox.Ok, QMessageBox.Ok)

    def layout_init(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
        self.desktop = QDesktopWidget()
        taskbar_height = self.desktop.screenGeometry().height() - self.desktop.availableGeometry().height()  # 任务栏高度
        self.move((self.desktop.availableGeometry().width() - self.width() - 10),
                  self.desktop.availableGeometry().height() - self.height() - taskbar_height)  # 初始化位置到右下角

    def tray_init(self):
        icon = QIcon(":/icon/icon/CTPBEE.png")
        menu = QMenu()
        settingAction = menu.addAction("⚙  设置")
        exitAction = menu.addAction("❎  退出")
        settingAction.triggered.connect(self.setting_handler)
        exitAction.triggered.connect(self.quit_action)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.iconActivated)
        self.tray.show()
        self.tray.setToolTip("~ bee box")

    def setting_handler(self):
        self.setting_widget = SettingWidget(self)
        self.setting_widget.show()

    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def quit_action(self):
        self.quit_ = True
        self.close()

    def closeEvent(self, event: QCloseEvent):
        if self.quit_:
            G.pool_done = True
            event.accept()
        else:
            self.hide()
            event.ignore()
