import os
from app.helper import py_path, config_path, beebox_path
import json
from app.global_var import G


def box_init():
    if not os.path.exists(config_path):
        G.config.python_path = py_path
        G.config.install_path = beebox_path
        with open(config_path, 'w')as fp:
            json.dump(G.config.to_dict(), fp)
    else:
        with open(config_path, 'r')as fp:
            G.config.update(json.load(fp))
