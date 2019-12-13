from PySide2.QtCore import QObject, Signal, Slot, Qt
from PySide2.QtGui import QIcon, QCloseEvent, QBitmap, QPainter
from PySide2.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QDesktopWidget, QMessageBox

from app.lib.global_var import G
from app.ui import qss
from app.ui.ui_mainwindow import Ui_MainWindow
from app.home import HomeWidget
from app.initial import InitialWidget


class Job(QObject):
    msg_box_signal = Signal(dict)  # 用于消息弹窗
    log_signal = Signal(str)

    def __init__(self):
        super(self.__class__, self).__init__()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.quit_ = False
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.job = Job()
        self.layout_init()
        self.tray_init()
        self.job.msg_box_signal.connect(self.msg_box_slot)
        # 主界面
        self.initial = InitialWidget(self)
        self.setCentralWidget(self.initial)

    @Slot(dict)
    def msg_box_slot(self, data):
        """消息弹窗插槽"""
        QMessageBox.information(self, "bee box", data['msg'], QMessageBox.Ok, QMessageBox.Ok)

    def layout_init(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏整个头部
        self.desktop = QDesktopWidget()
        taskbar_height = self.desktop.screenGeometry().height() - self.desktop.availableGeometry().height()  # 任务栏高度
        self.move((self.desktop.availableGeometry().width() - self.width() - 10),
                  self.desktop.availableGeometry().height() - self.height() - taskbar_height)  # 初始化位置到右下角
        """边缘圆角"""
        # self.bmp = QBitmap(self.size())
        # self.bmp.fill()
        # self.ppp = QPainter(self.bmp)
        # self.ppp.setPen(Qt.black)
        # self.ppp.setBrush(Qt.black)
        # self.ppp.drawRoundedRect(self.bmp.rect(), 10, 10)
        # self.ppp.end()
        # self.setMask(self.bmp)

    def tray_init(self):
        icon = QIcon(":/icon/icon/CTPBEE.png")
        menu = QMenu()
        exitAction = menu.addAction("❎  退出")
        exitAction.triggered.connect(self.quit_action)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.iconActivated)
        self.tray.show()
        self.tray.setToolTip("🍯~ bee box")

    def home_handler(self):
        self.widget = HomeWidget(self)
        self.setCentralWidget(self.widget)

    def iconActivated(self, reason):
        """托盘点击插槽"""
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
            try:
                self.widget.close()
            except:
                pass
            event.accept()
        else:
            self.hide()
            event.ignore()
    #
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.r_flag = False
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #
    # def mouseReleaseEvent(self, event):
    #     self.r_flag = True
    #     event.accept()
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     try:
    #         if Qt.LeftButton and self.m_flag and not self.r_flag:
    #             self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #             QMouseEvent.accept()
    #     except:
    #         pass
