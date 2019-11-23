import json
from app.lib.path_lib import config_path


class Config:
    python_path = {}
    choice_python = ""
    install_path = ""
    installed_apps = {}
    pypi_source = ""
    pypi_use = True

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        self.to_file()

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
<<<<<<< HEAD
=======
    # thread_pool = None
>>>>>>> 354f01cfdfcf2f79f3bc88110ad721fe6a9cf0c5
    pool_done = False
