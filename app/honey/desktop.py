import os
from urllib import request

from app.honey.base import BaseHoney
from app.lib.global_var import G


class HDesktop(BaseHoney):
    def __init__(self):
        self.name = "desktop"
        self.download_url = "https://github.com/ctpbee/ctpbee_desktop/archive/master.zip"
        self.versions = ["1.0"]
        self.app_url = "https://github.com/ctpbee/ctpbee_desktop"

    def download(self):
        request.urlretrieve(self.download_url, os.path.join(G.config.install_path, f'{self.name}.zip'),
                            reporthook=self.report_hook)

    def install(self):
        pass

    def run(self):
        pass
