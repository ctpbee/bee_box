class BaseHoney:
    icon = ""
    name = ""
    download_url = ""
    app_url = ""
    versions = []

    def download(self):
        pass

    def install(self):
        pass

    def uninstall(self):
        pass

    def run(self):
        pass

    def one_step(self):
        self.download()
        self.install()

    def report_hook(self, blocknum, block_size, total_size):
        """
        :param blocknum: 已经下载的数据块
        :param block_size: 数据块的大小
        :param total_size: 远程文件的大小
        :return:
        """
        print(blocknum * block_size * 100 // total_size)
