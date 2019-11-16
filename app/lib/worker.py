from PySide2.QtCore import Slot, QRunnable, QObject, Signal


class Worker(QRunnable, QObject):
    def __init__(self, fn, *args, **kwargs):
        super(self.__class__, self).__init__()
        self.setAutoDelete(True)

        self.fn = fn
        self.args = args
        self.callback = kwargs.pop("callback")
        self.kwargs = kwargs

    @Slot()
    def run(self):
        if self.callback and self.fn(*self.args, **self.kwargs):
            self.callback()
