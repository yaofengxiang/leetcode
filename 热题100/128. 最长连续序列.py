# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
# 示例1：
# 输入：nums = [100, 4, 200, 1, 3, 2]
# 输出：4
# 解释：最长数字连续序列是[1, 2, 3, 4]。它的长度为4。

# 示例2：
# 输入：nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# 输出：9

# 示例3：
# 输入：nums = [1, 0, 1, 2]
# 输出：3

# 思路：
# 1.利用集合set自动去重，再使用sorted()函数进行排序
# 2.两层for循环遍历数组。
# 3.变量len记录当前连续子序列的长度，maxlen记录最大长度。i指向连续子序列的第一个元素，j从 i+1 开始向后遍历，检查nums[j]是否为nums[j-1]+1，直到不满足这个条件位置。
# 4.如果len>maxlen，那么更新maxlen为len
# 5.回到2，直到整个数组被遍历完位置。
### 超时！！！
def longestConsecutive(nums):
    sorted_unique_nums = sorted(set(nums))
    size = len(sorted_unique_nums)
    max_len = 0
    for i in range(size):
        j = i + 1
        while j < size:
            if sorted_unique_nums[j] == (sorted_unique_nums[j - 1] + 1):
                j += 1
            else:
                break
        cur_len = j - i
        if cur_len > max_len:
            max_len = cur_len
    return max_len


# 思路2：
# 1. 使用set将数组元素建立为哈希表
# 2. 遍历哈希表
#   2.1 对当前元素x，判断是否存在x-1，如果存在，直接continue，否则进入2.2
#   2.2 判断是否存在x+y，存在就继续，不存在就返回长度y
#   2.3 如果y+1大于max_len，则更新max_len
def longestConsecutive2(nums):
    max_len = 0
    hashtable = set(nums)
    for x in hashtable:
        if x - 1 in hashtable:
            continue
        y = 1
        while x + y in hashtable:
            y += 1
        cur_len = y
        if cur_len > max_len:
            max_len = cur_len
    return max_len


if __name__ == '__main__':
    # print(longestConsecutive([1, 0, 1, 2]))
    print(longestConsecutive2([1, 0, 1, 2]))