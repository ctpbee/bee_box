import os
import re
import platform

platform_ = platform.system()

pattern = "[P|p][Y|y][T|t][H|h][O|o][N|n]\d*"  # python
pattern2 = "[P|p]ython\d*/$"  # python36/
pattern3 = "[P|p]ython\d*\.{1}exe$"  # python37.exe


def get_py_version(path):
    cmd = f"{path} --version"
    v = os.popen(cmd).read().replace('\n', '').replace('\r', '')
    return v


def find_py_path():
    res = {}
    paths = os.environ['path'].split(';')

    def matching(path):
        if re.findall(pattern2, path):  # 匹配python文件夹
            for item in os.listdir(path):
                if re.findall(pattern3, item):
                    return os.path.join(path, item)
        elif re.findall(pattern3, path):  # 匹配python.exe
            return path

    for path in paths:
        if re.findall(pattern, path):  # 筛选出含Python字眼的路径
            path = path.replace('\\', '/')
            p = matching(path)
            if p:
                res[get_py_version(p)] = p
    return res


def get_beebox_path():
    usr_path = os.path.join(os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'])
    beebox_path = os.path.join(usr_path, '.bee_box')
    if not os.path.exists(beebox_path):
        os.mkdir(beebox_path)
    return beebox_path


py_path = find_py_path()
beebox_path = get_beebox_path()
config_path = os.path.join(beebox_path, '.config.json')
