# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
from typing import List
from collections import Counter


# 示例1：
# 输入：nums = [1,1,1], k = 2
# 输出：2

# 示例2:
# 输入：nums = [1,2,3], k = 3
# 输出：2

# 前缀和+哈希表

def subarraySum(nums: List[int], k: int) -> int:
    # 生成前缀和数组
    s = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        s[i + 1] = s[i] + x

    ans = 0
    cnt = Counter()
    for sj in s:
        ans += cnt[sj - k]
        cnt[sj] += 1
    return ans


if __name__ == '__main__':
    print(subarraySum([1, 1, 1], 2))
    print(subarraySum([1, 2, 3], 3))
