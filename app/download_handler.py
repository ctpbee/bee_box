import os
import sys
import time

from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide2.QtCore import Signal, QObject, Slot, QFile, QUrl
from app.global_var import G
from contextlib import closing
from urllib import request


def Schedule(blocknum, blocksize, totalsize):
    speed = (blocknum * blocksize) / (time.time() - G.start_time)
    # speed_str = " Speed: %.2f" % speed
    speed_str = " Speed: %s" % format_size(speed)
    recv_size = blocknum * blocksize

    # 设置下载进度条
    f = sys.stdout
    pervent = recv_size / totalsize
    percent_str = "%.2f%%" % (pervent * 100)
    n = round(pervent * 50)
    s = ('#' * n).ljust(50, '-')
    f.write(percent_str.ljust(8, ' ') + '[' + s + ']' + speed_str)
    f.flush()
    # time.sleep(0.1)
    f.write('\r')


def format_size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.3fG" % (G)
        else:
            return "%.3fM" % (M)
    else:
        return "%.3fK" % (kb)


class HttpReq(QObject):
    download_signal = Signal(dict)

    def __init__(self):
        super(self.__class__, self).__init__()
        # self.m_netAccessManager = QNetworkAccessManager(self)
        self.download_signal.connect(self.run)

    @Slot(dict)
    def run(self, data):
        print("开始下载")
        request.urlretrieve(G.bee_box_url, os.path.join(G.config.install_path, f'demo.zip'),
                            reporthook=self.report_hook)
        print("download done!")

    def report_hook(self, blocknum, block_size, total_size):
        """
        :param blocknum: 已经下载的数据块
        :param block_size: 数据块的大小
        :param total_size: 远程文件的大小
        :return:
        """
        print(blocknum * block_size * 100 // total_size)
