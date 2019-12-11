import os
import sys

import requests
from PySide2.QtCore import QThreadPool, QObject

import time


class DownloadWorker(QObject):
    def __init__(self, url, filename=None):
        super().__init__()
        self.url = url
        self.filename = filename
        #
        self.response = None
        self.flag = True  # 当self.flag=False，暂停或取消下载，也就是结束下载线程
        self.header_flag = False  # 当为True时，设置header，断点续传
        self.re = requests.head(url, allow_redirects=True, timeout=20)  # 运行head方法时重定向

    def run(self):
        self.headers = {}
        self.mode = 'wb'
        if os.path.exists(self.filename) and self.header_flag:
            self.headers = {'Range': 'bytes=%d-' % os.path.getsize(self.filename)}
            self.mode = 'ab'
        self.response = requests.get(self.url, stream=True, headers=self.headers)
        with open(self.filename, self.mode) as code:
            for chunk in self.response.iter_content(chunk_size=1024):  # 边下载边存硬盘
                if chunk and self.flag:
                    code.write(chunk)
                else:
                    break
        time.sleep(1)

    def getsize(self):
        try:
            self.file_total = int(self.re.headers['Content-Length'])  # 获取下载文件大小
            return self.file_total
        except:
            return 0

    def cancel(self):  # 取消下载
        self.flag = False
        time.sleep(1)
        if os.path.isfile(self.filename):
            os.remove(self.filename)


class DownloadMiddleWare:
    def __init__(self):
        self.thread_pool = QThreadPool()
        self.job_pool = {}

    def start(self, url, packname):
        job = self.job_pool[packname] = DownloadWorker(url, packname)
        self.thread_pool.start(job)

    def cancel(self, packname):
        self.job_pool[packname].cancel()
