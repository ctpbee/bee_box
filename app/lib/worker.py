from PySide2.QtCore import Slot, QRunnable


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(self.__class__, self).__init__()
        self.setAutoDelete(True)

        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        self.fn(*self.args, **self.kwargs)
