from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtWidgets import QDialog

from app.ui.ui_progress import Ui_Form


class ProgressSig(QObject):
    """消息 ，进度信号"""
    msg = Signal(str)
    progress = Signal(int)

    def __init__(self):
        super(self.__class__, self).__init__()


class ProgressMsgDialog(QDialog, Ui_Form):
    def __init__(self, parent, msg='', p_min=0, p_max=0, p_val=0):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.sig = ProgressSig()
        self.sig.msg.connect(self.msg_slot)
        self.sig.progress.connect(self.progress_slot)
        self.progress.setRange(p_min, p_max)
        self.progress.setValue(p_val)
        self.msg.setText(msg)

    @Slot(str)
    def msg_slot(self, msg):
        self.msg.setText(msg)

    @Slot(int)
    def progress_slot(self, p_val):
        self.progress.setValue(p_val)
