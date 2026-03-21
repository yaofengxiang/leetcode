# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

# 示例1：
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]

# 示例2：
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
from typing import List


def rotate(nums: List[int], k: int) -> None:
    if k == 0:
        return
    n = len(nums)
    k = k % len(nums)
    # 1.将整个数组逆置
    i = 0
    j = n - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    # 2.将前k个逆置
    i = 0
    j = k - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    # 3.将后n-k个逆置
    i = k
    j = n - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    nums = [-1, -100, 3, 99]
    k = 2
    print(f'before: {nums}')
    rotate(nums, k)
    print(f'rotate(nums, k) = {nums}')
