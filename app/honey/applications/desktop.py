from app.honey.standard import Standard
from app.resource import icon_path

class Desktop(Standard):
    def app_info(self, **kwargs):
        ##
        self.name = kwargs.get('name', "desktop")
        self.desc = kwargs.get('desc', 'ctpbee桌面端')
        self.icon = kwargs.get('icon', ":/icon/icon/bee_temp_grey.png")
        self.versions = kwargs.get('versions',
                                   {"1.0": "https://github.com/ctpbee/ctpbee_desktop/archive/master.zip"}
                                   )
        self.lasted_ver = "1.0"
        self.app_url = kwargs.get('app_url', "https://github.com/ctpbee/ctpbee_desktop")
