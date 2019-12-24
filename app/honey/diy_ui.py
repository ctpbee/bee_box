import webbrowser

from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtGui import QMouseEvent, QFont
from PySide2.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QProgressBar, QToolButton, QMenu
from PySide2.QtGui import QFontMetrics


class AppDivJob(QObject):
    progressbar_signal = Signal(dict)
    msg_signal = Signal(str)
    action_signal = Signal(str)
    switch_signal = Signal()

    def __init__(self):
        super(self.__class__, self).__init__()


class AppDiv:
    """
    +------1--------------2------------3-------------------+
    |  +--------+                   +----------------+     |
    |  |  label | --label---name--  | install|version | ⚙ |
    |  |  image |                   +-----------------+    |
    |  +--------+   --label----describe----                |
    |                     4                                |
    |  -------progressbar------------    ----progressmsg-- |
    +------------------------------------------------------+
    """
    not_widget = ['not_widget', 'job', 'widget']

    def __init__(self, widget):
        self.widget = widget
        self.job = AppDivJob()
        self.job.progressbar_signal.connect(self.progressbar_signal_slot)
        self.job.msg_signal.connect(self.msg_signal_slot)
        self.job.action_signal.connect(self.action_signal_slot)
        self.job.switch_signal.connect(self.progress_switch)
        self.layout = QVBoxLayout()
        self.layout.setMargin(10)
        self.app_layout = QHBoxLayout()
        ### 1
        self.icon = QLabel(self.widget)
        ####  2
        self.name = QLabel(self.widget)
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setStyleSheet("""
        border:1px solid #1b89ca;
        border-radius:5px;
""")
        self.desc = MyLabel(self.widget)
        self.desc.setAlignment(Qt.AlignCenter)
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
        self.app_layout.setStretch(1, 4)
        self.app_layout.setStretch(2, 3)
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
        self.progress_layout.setStretch(0, 3)
        self.progress_layout.setStretch(1, 7)

        self.layout.addLayout(self.app_layout)
        self.layout.addLayout(self.progress_layout)

    def progress_switch(self):
        if self.progressbar.isHidden():
            self.progressbar.show()
            self.progress_msg.show()
        else:
            self.progress_msg.hide()
            self.progressbar.hide()

    def progressbar_signal_slot(self, data: dict):
        self.progressbar.setRange(*data['range'])
        self.progressbar.setValue(data['value'])

    def msg_signal_slot(self, msg: str):
        fontWidth = QFontMetrics(self.progress_msg.font())
        elideNote = fontWidth.elidedText(msg, Qt.ElideRight, self.name.width() + self.action.width() - 15)
        self.progress_msg.setText(elideNote)

    def action_signal_slot(self, act: str):
        self.action.setText(act)

    def add_installed_layout(self, data):
        self.widget.job.install_signal.emit(data)


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        font = QFont()
        font.setUnderline(True)
        self.setFont(font)
        self.url = None
        self.setStyleSheet("""
                QLabel:hover{
                color:#1b89ca
                }
                """)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, e: QMouseEvent):
        if self.url:
            try:
                webbrowser.get('chrome').open_new_tab(self.url)
            except Exception as e:
                webbrowser.open_new_tab(self.url)
