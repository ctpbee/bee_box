import os
import re
import platform

platform_ = platform.system()

pattern = r"[P|p][Y|y][T|t][H|h][O|o][N|n]\d*"  # python
pattern2 = r"([P|p]ython\d*[/$|\\$]?)$"  # python36/ 末尾
pattern3 = r"[P|p]ython\d*\.exe$"  # python37.exe
pattern4 = r"[P|p][I|i][P|p]\d*\.exe$"  # pip3.exe


def join_path(rootdir, *args):
    for i in args:
        rootdir = os.path.join(rootdir, i)
    return rootdir


def find_file(path, file):
    pattern = file if '\.' in file else file.replace('.', '\.')
    if not os.path.exists(path):
        return

    def list_all_files(rootdir):
        _files = []
        list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(rootdir, list[i])
            if os.path.isdir(path):
                _files.extend(list_all_files(path))
            if os.path.isfile(path):
                _files.append(path)
        return _files

    fs = list_all_files(path)
    k = list(filter(lambda x: re.search(pattern, x), fs))
    return k


def get_py_version(path):
    try:
        cmd = f"{path} --version"
        v = os.popen(cmd).read().replace('\n', '').replace('\r', '').lower()
        return v
    except:
        return ""


def get_pip_version(path):
    try:
        cmd = f"{path} -V"
        v = os.popen(cmd).read().replace('\n', '').replace('\r', '').lower()
        r = re.findall('\((.*)\)', v)
        if r:
            return r[0]
    except:
        return ""


def find_py_path():
    res = {}
    paths = os.environ['path'].split(';')

    for path in paths:
        if re.findall(pattern2, path):  # 筛选出含Python路径
            for item in os.listdir(path):
                py_path = os.path.join(path, item)
                if os.path.isfile(py_path):
                    if re.match(pattern3, item):
                        v = get_py_version(py_path)
                        res[v] = py_path
                        break
    return res


def get_beebox_path():
    usr_path = os.path.join(os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'])
    beebox_path = os.path.join(usr_path, '.bee_box')
    if not os.path.exists(beebox_path):
        os.mkdir(beebox_path)
    return beebox_path


beebox_path = get_beebox_path()


def get_install_path():
    install_path = os.path.join(beebox_path, 'apps')
    if not os.path.exists(install_path):
        os.mkdir(install_path)
    return install_path


install_path = get_install_path()
config_path = os.path.join(beebox_path, '.config.json')
