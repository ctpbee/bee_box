import webbrowser
from PySide2.QtGui import QMouseEvent, QFont
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

from app.ui.ui_home import Ui_Home
from app.lib.global_var import G
from app.honey import all_app


class HomeWidget(QWidget, Ui_Home):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.setting_btn.clicked.connect(self.setting_click)
        ## app
        self.ready_action()

    def ready_action(self):
        self.py_version.setText(G.config.choice_python)
        for app_cls in all_app:
            app = app_cls()
            div = AppDiv(self)
            div.icon.setStyleSheet(f"image: url({app.icon});")
            div.name.setText(app.name)
            div.desc.setText(app.desc)
            div.desc.url = app.app_url
            div.action.setText(app.action)
            div.action.clicked.connect(app.action_handler)
            self.apps_layout.addLayout(div.div_layout)

    def setting_click(self):
        self.mainwindow.setting_handler()


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
        self.icon = QLabel(self.widget)
        ####  2
        self.name = QLabel(self.widget)
        self.desc = MyLabel(self.widget)  # 可点击
        self.desc.setText('test')
        self.desc_layout = QVBoxLayout()
        self.desc_layout.addWidget(self.name)
        self.desc_layout.addWidget(self.desc)
        ####  3
        self.action = QPushButton(self.widget)
        ###
        self.div_layout.addWidget(self.icon)
        self.div_layout.addLayout(self.desc_layout)
        self.div_layout.addWidget(self.action)
        self.div_layout.setStretch(0, 3)
        self.div_layout.setStretch(1, 5)
        self.div_layout.setStretch(2, 2)


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        font = QFont()
        font.setUnderline(True)
        self.setFont(font)
        self.url = None

    def mousePressEvent(self, e: QMouseEvent):
        if self.url:
            try:
                webbrowser.get('chrome').open_new_tab(self.url)
            except Exception as e:
                webbrowser.open_new_tab(self.url)
