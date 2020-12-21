import os
from multiprocessing import *

q = Queue(3)


def copy(target_path, src_path):
    print("复制", target_path)
    rs = open(src_path, "rb")
    ws = open(target_path, "wb")
    # target_size = 0
    while True:
        data = rs.read(1024)
        if not data:
            break
        size_write = ws.write(data)
        q.put(size_write)
    rs.close()
    ws.close()


def total_size(dir_):
    all_size = 0
    for f in os.listdir(dir_):
        size = os.path.getsize(os.path.join(dir_, f))
        all_size += size
    return all_size


def show_per(all_size):
    while True:
        target_size = q.get()
        per = (target_size / all_size) * 100
        print("百分比：", per, "%")


def main():
    os.mkdir("p2")
    file_list = os.listdir("D:\\p2")
    pol = Pool()
    all_size = total_size("D:\\p2")
    for f in file_list:
        path1 = os.path.join("p2", f)
        path2 = os.path.join("D:\\p2", f)
        pol.apply_async(copy, args=(path1, path2))
    # 求百分比
    copy_size = 0
    while copy_size < all_size:
        copy_size += q.get()
        per = (copy_size / all_size) * 100
        print("以拷贝%.2f%%" % per)
    pol.close()
    pol.join()


if __name__ == '__main__':
    main()
