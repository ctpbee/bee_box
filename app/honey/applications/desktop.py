from app.honey.standard import Standard


class Desktop(Standard):
    def app_info(self, **kwargs):
        ##
        self.name = kwargs.get('name', "desktop")
        self.desc = kwargs.get('desc', 'ctpbee桌面端')
        self.icon = kwargs.get('icon', ":/icon/icon/bee_temp_grey.png")
        self.versions = kwargs.get('versions',
                                   {"1.0": "https://github.com/ctpbee/ctpbee_desktop/archive/master.zip"}
                                   )
        self.install_version = kwargs.get("install_version","1.0")  # 默认安装版本
        self.app_url = kwargs.get('app_url', "https://github.com/ctpbee/ctpbee_desktop")
