class BaseHoney:
    icon = ""  # 图标
    name = ""  # 名称
    desc = ""  # 描述 | 版本
    download_url = ""  # 下载地址
    app_url = ""  # 应用官网
    versions = []  # 版本
    action = ""  # 按钮执行动作：安装/卸载/升级/运行

    def download_handler(self):
        """下载处理"""

    def install_handler(self):
        """安装处理"""

    def uninstall_handler(self):
        """卸载处理"""

    def run_handler(self):
        """运行处理"""

    def action_handler(self):
        """动作按钮槽函数"""

    def report_hook(self, blocknum, block_size, total_size):
        """
        下载处理时request.urlretrieve(reporthook=   )回调函数
        :param blocknum: 已经下载的数据块
        :param block_size: 数据块的大小
        :param total_size: 远程文件的大小
        :return:
        """
        self.download_url
        print(blocknum * block_size * 100 // total_size)
