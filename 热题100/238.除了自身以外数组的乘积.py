# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。
# 题目数据保证数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

# 示例1：
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]

# 示例2：
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    ans = [1] * len(nums)
    pre = [1] * len(nums)
    suf = [1] * len(nums)
    # 1.获取前缀乘积数组pre
    for i in range(len(nums) - 1):
        pre[i + 1] = pre[i] * nums[i]

    # 2.获取后缀乘积数组suf
    for i in range(len(nums) - 2, -1, -1):
        suf[i] = nums[i + 1] * suf[i + 1]

    # 3.计算得到结果数组
    for i in range(len(nums)):
        ans[i] = pre[i] * suf[i]
    return ans


if __name__ == '__main__':
    # nums = [1, 2, 3, 4]
    nums = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums))