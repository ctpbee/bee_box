from PySide2.QtCore import QThreadPool


class DownloadManager:
    def __init__(self):
        self.thread_pool = QThreadPool()

    def download_handle(self):
        pass
