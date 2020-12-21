from multiprocessing.context import Process

"""
自定义进程类
"""


class NewProcess(Process):
    def __init__(self, value):
        super().__init__()
        self.value = value

    # 重写父类方法
    def run(self) -> None:
        print("执行方法", self.value)


if __name__ == '__main__':
    # p1 = NewProcess(3)
    #     # p1.start()
    #     # p1.join()
    dict1 = eval("{'aa':'bb','cc':'dd'}")
    print(dict1)
