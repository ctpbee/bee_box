class Actions(dict):
    INSTALL = "install"
    UNINSTALL = "uninstall"
    UPGRADE = "upgrade"
    RUN = "run"
    CANCEL = "cancel"


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
