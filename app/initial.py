import os
from app.helper import py_path, beebox_path
import json
from app.global_var import G


def box_init():
    path = os.path.join(beebox_path, 'global_config.json')
    if not os.path.exists(path):
        G.config.update(py_path)
        with open(path, 'w')as fp:
            json.dump(G.config.to_dict(), fp)
    else:
        with open(path, 'r')as fp:
            G.config.update(json.load(fp))
