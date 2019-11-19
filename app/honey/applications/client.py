from app.honey.standard import Standard


class Client(Standard):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

    def app_info(self, **kwargs):
        ##
        self.name = kwargs.get('name', "client")
        self.desc = kwargs.get('desc', 'ctpbee_client')
        self.icon = kwargs.get('icon', ":/icon/icon/be2e.png")
        self.versions = kwargs.get('versions',
                                   {"1.0": "https://github.com/ctpbee/ctpbee_backend/archive/master.zip"}
                                   )
        self.app_url = kwargs.get('app_url', "https://github.com/ctpbee/ctpbee_backend")
        self.install_version = kwargs.get('install_version', "1.0")
        self.app_folder = kwargs.get('app_folder', '')
        self.launch_cmd = kwargs.get('launch_cmd', '')
