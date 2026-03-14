# 给你一个整数数组 nums ，判断是否存在三元组[nums[i], nums[j], nums[k]]
# 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 示例1：
# 输入：nums = [-1, 0, 1, 2, -1, -4]
# 输出：[[-1, -1, 2], [-1, 0, 1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是[-1, 0, 1]
# 和[-1, -1, 2] 。
# 注意，输出的顺序和三元组的顺序并不重要。

# 示例2：
# 输入：nums = [0, 1, 1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。

# 示例3：
# 输入：nums = [0, 0, 0]
# 输出：[[0, 0, 0]]
# 解释：唯一可能的三元组和为 0 。


from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # 1. 边界条件
    if nums is None or len(nums) < 3:
        return []
    res = list()
    # 2. 对数组进行排序
    nums.sort()
    # 3. 遍历数组
    size = len(nums)
    for i in range(size):
        if nums[i] > 0:  # 后面的元素都比nums[i]，因此和不可能为0，直接返回结果
            return res
        if i > 0 and nums[i] == nums[i - 1]:  # 如果元素重复，则直接跳过
            continue
        L = i + 1
        R = size - 1
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                res.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L + 1]:
                    L += 1
                while L < R and nums[R] == nums[R - 1]:
                    R -= 1
                L += 1
                R -= 1
            elif nums[i] + nums[L] + nums[R] < 0:  # 和小于0，说明nums[L]太小，L右移
                L += 1
            else:  # 和大于0，说明nums[R]太大，R左移
                R -= 1
    return res


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
