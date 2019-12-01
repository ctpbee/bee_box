import gzip
import os
import re
import tarfile
import zipfile
import rarfile


def un_gz(filepath):
    """un gz file"""
    f_name = filepath.replace(".gz", "")
    # 获取文件的名称，去掉
    g_file = gzip.GzipFile(filepath)
    # 创建gzip对象
    open(f_name, "w+").write(g_file.read())
    # gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()


def un_tar(filepath):
    """un tar file"""
    tar = tarfile.open(filepath)
    names = tar.getnames()
    folder = filepath.replace(".tar", "")
    if os.path.isdir(folder):
        pass
    else:
        os.mkdir(folder)
    # 因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, folder)
    tar.close()


def un_zip(filepath: str):
    """un zip file"""
    zip_file = zipfile.ZipFile(filepath)
    folder = filepath.replace(".zip", "")
    if os.path.isdir(folder):
        pass
    else:
        os.mkdir(folder)
    for names in zip_file.namelist():
        zip_file.extract(names, folder)
    zip_file.close()


def un_rar(filepath):
    """un rar file"""
    rar = rarfile.RarFile(filepath)
    folder = filepath.replace(".rar", "")
    if os.path.isdir(folder):
        pass
    else:
        os.mkdir(folder)
    os.chdir(folder)
    rar.extractall()
    rar.close()


def extract(filepath, postfix=""):
    if not postfix:
        postfix = re.findall('\.(zip|rar)', filepath)[0]
    if postfix == 'zip':
        un_zip(filepath)
    elif postfix == 'rar':
        un_rar(filepath)
    elif postfix == 'tar':
        un_tar(filepath)
    else:
        raise TypeError("Unknown Zip File Type")
    if os.path.exists(filepath) and os.path.isfile(filepath):
        os.remove(filepath)
