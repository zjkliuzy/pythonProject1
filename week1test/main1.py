"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例：给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


def find_numes(nums, target):
    new_nums = sorted(nums)
    for i, v in enumerate(new_nums):
        for j in range(i + 1, len(new_nums)):
            if v + new_nums[j] == target:
                return i, j


def find_numes2(nums: list, target):
    lookup = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in lookup:
            return [lookup[temp], i]
        lookup[nums[i]] = i


result = find_numes2([2, 7, 11, 15], 9)
print(list(result))


def FindNumsAppearOnce(array):
    sorted(array)
    list1 = []
    for i in range(0, len(array) - 1, 2):
        if array[i] != array[i + 1]:
            if len(list1) < 2:
                list1.append(array[i])
    return list1


print(FindNumsAppearOnce([1, 2, 2, 4, 4, 3, 5, 5, 6, 7, 6, 7]))
matrix = [
    [2, 4, 6, 9],
    [13, 15, 17, 19],
    [24, 26, 27, 28]
]


def search(matrix, num):
    row = len(matrix)
    col = len(matrix[0])
    i = row - 1
    j = 0
    res = False
    # matrix[i][j]
    while True:
        if i < 0 or j == col:
            break
        if matrix[i][j] > num:
            # 如果 左下角元素大于目标  上移
            i -= 1
        elif matrix[i][j] < num:
            # 如果 左下角元素小于目标  右移
            j += 1
        elif matrix[i][j] == num:
            res = True
            break
    return res


print(search(matrix, 999))
