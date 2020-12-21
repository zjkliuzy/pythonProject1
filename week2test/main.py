def func1(nums):
    for index, n in enumerate(nums):
        if index < len(nums) - 1:
            if nums[index + 1] != nums[index] + 1:
                return nums[index + 1] - 1


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
    print(func1(nums))
