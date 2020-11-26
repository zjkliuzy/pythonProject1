class IterableHelper:
    @staticmethod
    def find_all(iterable, func):
        """
        根据条件查找元素
        :param iterable:
        :param func:函数类型的条件
        :return: 生成器
        """
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def find_single(iterable, func):
        """
        从列表里面找到一个结果
        :param iterable:
        :param func: 函数类型的条件
        :return: 结果
        """
        for item in iterable:
            if func(item):
                return item

    @staticmethod
    def select(iterable, func):
        """

        :param iterable:
        :param func:
        :return:
        """
        for emp in iterable:
            yield func(emp)

    @staticmethod
    def get_max(func, iterable):
        """

        :param func:
        :param iterable:
        :return:
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(max_value) < func(iterable[i]):
                max_value = iterable[i]
        return max_value
    @staticmethod
    def get_count(func, iterable, money):
        """

        :param func:
        :param iterable:
        :param money:
        :return:
        """
        for item in iterable:
            if func(item) > money:
                yield item