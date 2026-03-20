# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
# 示例1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
from math import inf
from typing import List


# 示例2：
# 输入：nums = [1]
# 输出：1

# 示例3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23


# 思路：前缀和+贪心算法
def maxSubArray(nums: List[int]) -> int:
    ans = -inf
    min_pre_sum = pre_sum = 0
    for x in nums:
        pre_sum += x
        ans = max(ans, pre_sum - min_pre_sum)
        min_pre_sum = min(min_pre_sum, pre_sum)
    return ans


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray([1]))
    print(maxSubArray([5, 4, -1, 7, 8]))
