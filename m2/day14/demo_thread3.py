import os
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, value):
        self.value = value
        super().__init__()

    def run(self) -> None:
        for i in range(3):
            sleep(3)
            print(os.getppid(), "你好你好", self.value)


if __name__ == '__main__':
    t = MyThread("ｄｋｓｈｌｊｆ你好啊是啊")
    t.start()
    t.join()
