# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那
# 两个整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。你可以按任意顺序返回答案。
#
# 示例1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为
# nums[0] + nums[1] == 9 ，返回[0, 1] 。
#
# 示例2：
# 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
#
# 示例3：
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]


# 法一：遍历数组，找new_target
def twoSum1(nums, target):
    for i in range(len(nums)):
        new_target = target - nums[i]
        j = i + 1
        while j < len(nums):
            if new_target == nums[j]:
                return [i, j]
            j += 1

# 法二：使用哈希表存储已经遍历过的数组，与法一不同的是，该方法是将当前元素与其前面的元素匹配检查，而法一是将当前元素与其后面的元素匹配检查
def twoSum2(nums, target):
    hashtable = dict()  # 创建空的哈希表
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [i, hashtable[target - num]]
        hashtable[num] = i
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # print(twoSum1(nums, target))
    print(twoSum2(nums, target))
