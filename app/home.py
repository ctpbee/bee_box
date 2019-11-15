from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import *
from app.lib.worker import Worker


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.setting_btn.clicked.connect(self.setting_click)
        ## app
        self.desktop = HDesktop()
        # self.pushButton.clicked.connect(self.desktop_slot)
        self.ready_action()

    def ready_action(self):
        self.py_version.setText(G.config.choice_python)

    def setting_click(self):
        self.mainwindow.setting_handler()

    @Slot()
    def desktop_slot(self):
        self.new_it()
        # self.mainwindow.thread_pool.start(Worker(self.desktop.download))

    def new_one(self):
        """
        一个app布局  加入到页面布局中吧
        :return:
        """
        return AppDiv(self).div_layout


class AppDiv:
    """
    +------1--------------2------------3--------+
    |  +--------+                   +-----+     |
    |  |  label | --label---name--  | open |    |
    |  |  image |                   +------+    |
    |  +--------+   --label----describe----     |
    +-------------------------------------------+
    """

    def __init__(self, widget):
        self.widget = widget
        self.div_layout = QHBoxLayout()
        ### 1
        self.img_label = QLabel(self.widget)
        ####  2
        self.name_label = QLabel(self.widget)
        self.desc_label = MyLabel(self.widget)  # 可点击
        self.desc_layout = QVBoxLayout()
        self.desc_layout.addWidget(self.name_label)
        self.desc_layout.addWidget(self.desc_label)
        ####  3
        self.btn = QPushButton(self.widget)
        ###
        self.div_layout.addWidget(self.img_label)
        self.div_layout.addLayout(self.desc_layout)
        self.div_layout.addWidget(self.btn)
        self.div_layout.setStretch(0, 3)
        self.div_layout.setStretch(1, 5)
        self.div_layout.setStretch(2, 2)


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    def mousePressEvent(self, e):
        print(1)
