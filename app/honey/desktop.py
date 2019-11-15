import os
from urllib import request

from app.honey.base import BaseHoney
from app.lib.global_var import G
from app.lib.worker import Worker


class HDesktop(BaseHoney):
    def __init__(self):
        self.name = "desktop"
        self.download_url = "https://github.com/ctpbee/ctpbee_desktop/archive/master.zip"
        self.versions = ["1.0"]
        self.app_url = "https://github.com/ctpbee/ctpbee_desktop"
        self.install_path = os.path.join(G.config.install_path, f'{self.name}.zip')
        self.action = "安装"
        self.desc = 'ctpbee桌面端'
        self.icon = "app/resource/icon/bee_temp_grey.png"

    def download_handler(self):
        request.urlretrieve(self.download_url, self.install_path,
                            reporthook=self.report_hook)

    def install_handler(self):
        pass

    def run_handler(self):
        pass

    def action_handler(self):
        print(1)
        G.thread_pool.start(Worker(self.download_handler))

