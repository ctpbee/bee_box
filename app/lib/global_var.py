import json
from urllib.parse import urlparse

from app.lib.path_lib import config_path


def get_domian(uri) -> str:
    """
    返回解析的的域名信息
    """
    parse = urlparse(uri)
    return parse.netloc


class Config:
    python_path = {}
    install_path = ""
    installed_apps = {}
    pypi_source = "https://mirrors.aliyun.com/pypi/simple"
    pypi_use = True

    def get_pypi_source(self):
        if not self.pypi_use:
            return []
        else:
            return ["-i", self.pypi_source, "--trusted-host", get_domian(self.pypi_source)]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def update(self, data: dict):
        for k, v in data.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dict(self):
        pr = {}
        for name in dir(self):
            value = getattr(self, name)
            if not name.startswith('__') and not callable(value):
                pr[name] = value
        return pr

    def to_file(self):
        with open(config_path, 'w')as f:
            json.dump(self.to_dict(), f)


class G(dict):
    config = Config()
    pool_done = False
