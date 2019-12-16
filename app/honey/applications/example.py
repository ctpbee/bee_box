from app.honey.standard import Standard

"""
首先应用目录下需要有build.json内容包括
{   
    'entry':'',
    'requirement':''
}
"""


class AppNameClass(Standard):
    def app_info(self, **kwargs):
        """重写此方法"""
        self.name = kwargs.get('name', "desktop")  # 应用名称
        self.desc = kwargs.get('desc', 'ctpbee桌面端')  # 应用描述
        self.icon = kwargs.get('icon', ":/icon/icon/bee_temp_grey.png")  # 应用图标
        self.versions = kwargs.get('versions',
                                   {"1.0": "https://github.com/ctpbee/ctpbee_desktop/archive/master.zip"}  # 版本号以及下载地址
                                   )
        self.install_version = kwargs.get("install_version", "1.0")  # 默认安装版本
        self.app_url = kwargs.get('app_url', "https://github.com/ctpbee/ctpbee_desktop")  # 应用链接
