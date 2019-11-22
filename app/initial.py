import os
from app.lib.path_lib import config_path, install_path, find_py_path
import json
from app.lib.global_var import G


def box_init():
    if not os.path.exists(config_path):
        open(config_path, 'w')
        G.config.python_path = find_py_path()
        G.config.install_path = install_path
    else:
        with open(config_path, 'r')as fp:
            G.config.update(json.load(fp))
    return True
