from PySide2.QtCore import Slot, QRunnable


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(self.__class__, self).__init__()
        self.setAutoDelete(True)
        self.fn = fn
        self.args = args
        self.succ_callback = kwargs.pop("succ_callback", None)
        self.fail_callback = kwargs.pop("fail_callback", None)
        self.kwargs = kwargs

    @Slot()
    def run(self):
        res = self.fn(*self.args, **self.kwargs)
        if res is True and self.succ_callback:
            self.succ_callback()
        if res is False and self.fail_callback:
            self.fail_callback()
