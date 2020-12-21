from itertools import permutations


def find_apperance(nums):
    n = len(nums)
    app = n / 2
    set1 = set(nums)
    for i in set1:
        if nums.count(i) > app:
            return i


def find_seqs(n):
    list_re = []
    for i in range(1, n // 2 + 1):
        sum = 0
        x = i
        while sum <= n:
            if sum == n:
                l = [i for i in range(i, x)]
                list_re.append(l)
            sum += x
            x += 1
    return list_re


def largest_time(A):
    """
    :param A: List[int]
    :return: str
    """
    max_time = 0  # 初始化最大时刻
    res = ''  # 结果字符串

    for ht, hb, mt, mb in permutations(A):  # 遍历
        hour, minute = ht * 10 + hb, mt * 10 + mb  # 求取时分
        t = hour * 60 + minute  # 当前时刻（秒）

        if hour < 24 and minute < 60 and t >= max_time:  # 时间合法的条件
            res = "{}{}:{}{}".format(ht, hb, mt, mb)  # 更新结果
            max_time = t  # 更新最大时刻
    return res


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 5, 5, 6, 4, 2, 1, 5, 5, 5, 5, 5, 5]
    # print(find_apperance(nums))
    # print(range(2))
    # nums = [1, 2, 3, 4, 5, 5, 5, 6, 4, 2, 1, 5, 5, 5, 5, 5, 5,3,3]
    # print(len(nums) // 2)
    # print(sorted(nums))
    l = find_seqs(14)
    print(l)
