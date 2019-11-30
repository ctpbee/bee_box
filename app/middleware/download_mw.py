from PySide2.QtCore import QThreadPool


class DownloadMiddleWare:
    def __init__(self):
        self.thread_pool = QThreadPool()

    def run(self):
        pass

    def download_handle(self):
        pass
