import os
import shutil

"""
    脚本作用:将包含指定文件名的文件,打包放在一个文件夹里
"""


def open_doc(path):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    print(files)


def main():
    path_open = "/Users/chenyuanzhen/Desktop/test"
    name_tar = "的副本"
    # 用于保存含目标名字的文件名
    name_save = []
    path_save = path_open + "/" + name_tar
    # 得到文件夹下的所有文件名称
    files = os.listdir(path_open)
    for index in files:
        if name_tar in index:
            name_save.append(index)

    # 在当前目录创建新的文件夹 如果有就不进行创建
    try:
        new_doc = os.mkdir(path_save)
    except FileExistsError:
        pass

    # 把含目标文件放在指定文件夹
    for index in name_save:
        shutil.copyfile(path_open + '/' + index, path_save + '/' + index)

    print(name_save)


main()
