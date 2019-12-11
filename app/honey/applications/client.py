import requests

from app.honey.standard import Standard


class Client(Standard):
    def app_info(self, **kwargs):
        ##
        self.name = kwargs.get('name', "client")
        self.desc = kwargs.get('desc', 'ctpbee_client')
        self.icon = kwargs.get('icon', ":/icon/icon/bee_temp_grey.png")
        self.versions = kwargs.get('versions',
                                   {"1.0": "https://github.com/ctpbee/bee_box/archive/master.zip"}
                                   )
        self.app_url = kwargs.get('app_url', "https://github.com/ctpbee/ctpbee_backend")
        self.lasted_ver = "1.0"



