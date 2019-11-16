import webbrowser
from PySide2.QtGui import QMouseEvent, QFont
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QProgressBar, QToolButton, QMenu, \
    QAction


class InstalledDiv:
    """
    +------1--------------2------------3------------------+
    |  +--------+                   +-------------+  --   |
    |  |  label | --label---name--  | open/update | |⚙|   |
    |  |  image |                   +-------------+  --   |
    |  +--------+   --label----version----                |
    +-----------------------------------------------------+
    """

    def __init__(self, widget):
        self.widget = widget
        self.layout = QHBoxLayout()
        ### 1
        self.icon = QLabel(self.widget)
        self.name = QLabel(self.widget)
        self.version = QLabel(self.widget)
        self.desc_layout = QVBoxLayout()
        self.desc_layout.addWidget(self.name)
        self.desc_layout.addWidget(self.version)
        ####  3
        self.action = QPushButton(self.widget)
        ###
        self.layout.addWidget(self.icon)
        self.layout.addLayout(self.desc_layout)
        self.layout.addWidget(self.action)
        self.layout.setStretch(0, 3)
        self.layout.setStretch(1, 5)
        self.layout.setStretch(2, 2)


class AppDiv:
    """
    +------1--------------2------------3-------------------+
    |  +--------+                   +----------------+     |
    |  |  label | --label---name--  | install|version |    |
    |  |  image |                   +-----------------+    |
    |  +--------+   --label----describe----                |
    +------------------------------------------------------+
    """

    def __init__(self, widget):
        self.widget = widget
        self.layout = QVBoxLayout()
        self.app_layout = QHBoxLayout()
        ### 1
        self.icon = QLabel(self.widget)
        ####  2
        self.name = QLabel(self.widget)
        self.desc = MyLabel(self.widget)
        self.desc_layout = QVBoxLayout()
        self.desc_layout.addWidget(self.name)
        self.desc_layout.addWidget(self.desc)
        ####  3
        self.menu = QMenu(self.widget)
        self.action = QToolButton(self.widget)
        self.action.setPopupMode(QToolButton.MenuButtonPopup)
        self.action.setMenu(self.menu)

        ###
        self.app_layout.addWidget(self.icon)
        self.app_layout.addLayout(self.desc_layout)
        self.app_layout.addWidget(self.action)
        self.app_layout.setStretch(0, 3)
        self.app_layout.setStretch(1, 5)
        self.app_layout.setStretch(2, 2)
        ##  4
        self.progress_layout = QHBoxLayout()
        self.progressbar = QProgressBar()
        self.progressbar.setFixedHeight(1)
        self.progressbar.setTextVisible(False)
        self.progressbar.setRange(0, 0)
        self.progressbar.setVisible(False)
        self.progress_msg = QLabel(self.widget)
        self.progress_msg.setVisible(False)
        self.progress_layout.addWidget(self.progressbar)
        self.progress_layout.addWidget(self.progress_msg)
        ###
        self.layout.addLayout(self.app_layout)
        self.layout.addLayout(self.progress_layout)


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
