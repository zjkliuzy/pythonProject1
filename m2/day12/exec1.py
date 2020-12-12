"""
文件拆分

"""
import os
from multiprocessing.context import Process


def read_part1(filename, size):
    file = open(filename, "rb")
    file_write = open("part1.txt", "wb")
    while True:
        data = file.read(1024)
        file_write.write(data)
        if size - file.tell() <= 1024:
            data = file.read(size - file.tell())
            file_write.write(data)
            break
    file.close()
    file_write.close()


def read_part2(filename, size):
    file = open(filename, "rb")
    file_write = open("part2.txt", "wb")
    file.seek(size)
    while True:
        data = file.read(1024)
        if not data:
            break
        file_write.write(data)
    file.close()
    file_write.close()


def main():
    size = os.path.getsize("dict.txt")
    half_size = size // 2

    p1 = Process(target=read_part1, args=("dict.txt", half_size))
    p2 = Process(target=read_part2, args=("dict.txt", half_size))
    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
