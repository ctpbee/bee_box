import os

from PySide2.QtCore import QThread, QObject, Signal
from PySide2.QtWidgets import QWidget

from app.lib.path_lib import config_path, install_path, find_py_path
import json
from app.lib.global_var import G
from app.ui.ui_initial import Ui_Form

qss = """
QProgressBar {  
    border-radius: 5px;  
    text-align: center;  
    border: 1px solid #5CACEE;  
}  
  
QProgressBar::chunk {  
    width: 5px;   
    margin: 0.5px;  
    background-color: #1B89CA;  
}  """


class InitialWidget(QWidget, Ui_Form):
    def __init__(self, mainwindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qss)
        self.mainwindow = mainwindow
        self.thread = QThread()
        self.job = InitJob()
        self.job.moveToThread(self.thread)
        self.thread.started.connect(self.job.box_init)
        self.thread.start()
        self.job.sig_progress.connect(self.show_progress)

    def show_progress(self, pro, msg):
        if pro == 100:
            self.mainwindow.home_handler()
            return
        self.progressBar.setValue(pro)
        self.msg.setText(msg)


class InitJob(QObject):
    sig_progress = Signal(int, str)

    def __init__(self):
        super(self.__class__, self).__init__()

    def box_init(self):
        if not os.path.exists(config_path):
            self.sig_progress.emit(5, "正在查找Python路径..")
            open(config_path, 'w')
            G.config.python_path = find_py_path()
            G.config.install_path = install_path
        else:
            self.sig_progress.emit(5, "正在加载配置..")
            with open(config_path, 'r')as fp:
                G.config.update(json.load(fp))
        self.sig_progress.emit(100, "初始化完成")
