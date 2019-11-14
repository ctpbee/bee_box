import os
import sys
import re
import platform

platform_ = platform.system()

pattern = "[P|p][Y|y][T|t][H|h][O|o][N|n]\d*"


def find_py_path():
    res = {"python_path": {}}
    Path = os.environ['path'].split(';')

    def matching(path):
        path = path.replace('\\', '/').split('/')
        for i in path[::-1]:
            if i.strip():
                if re.match(pattern, i):
                    return i

    for i in Path:
        if re.findall(pattern, i):
            d = matching(i)
            if d:
                res['python_path'][d] = os.path.join(i, 'python.exe')
    return res


def get_beebox_path():
    usr_path = os.path.join(os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'])
    beebox_path = os.path.join(usr_path, '.bee_box')
    if not os.path.exists(beebox_path):
        os.mkdir(beebox_path)
    return beebox_path


py_path = find_py_path()
beebox_path = get_beebox_path()
