import os
from collections import namedtuple


def make_dic(path):
    my_root = path.split("\\")[-1]  # get the lest directory(where I am..)
    dic = {my_root: {}}  # make the ground: make empty dictionary as value to my_root kay
    filetuple = namedtuple('file_details', ['name', 'suffix', 'size'])
    for (root, dirs, files) in os.walk(path, topdown=True):
        temp = dic
        my_path = root[root.find(my_root):]  # I am interesting gust what have from my_root to down In each round,
                                             # another personal and existing folder is added.
        directories = my_path.split("\\")
        for directory in directories:
            temp = temp[directory]  # temp hold the last directory -->
                                    # All income will be seen like temp[directory][kay]=val

        for file in files:
            size = os.stat(f'{root}\\{file}').st_size  # in bytes
            suffix = file[file.rfind("."):]
            temp[file] = filetuple(name=file, suffix=suffix, size=size)
        for directory in dirs:
            temp[directory] = {}  # make new dictionary to the new direction in this direction
    print(dic)


make_dic(r"C:\Users\USER001\Documents\Exelenteem\python\check")
