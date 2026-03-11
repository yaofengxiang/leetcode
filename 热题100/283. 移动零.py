# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# 示例 2:
# 输入: nums = [0]
# 输出: [0]

# 思路1：指针i指向最左边的0元素，指针j指向最左边的非0元素

def moveZeroes1(nums):
    i = 0
    j = 0
    size = len(nums)
    while i < size and j < size:
        # 令i指向最左侧的0
        while i < size and nums[i] != 0:
            i += 1
        j = i + 1
        while j < size and nums[j] == 0:
            j += 1
        if i == size or j == size:
            break
        # 交换i和j指向的元素
        nums[i], nums[j] = nums[j], nums[i]
    print(nums)


# 思路2：
# 1. 指针i指向可以放置非0元素的位置，指针j寻找非0元素
# 2. 指针i=0，指针j=0
# 3. 移动j指针找到第一个非0元素
# 4. nums[i] = nums[j]，指针i++，指针j++
# 5. 重复3和4直到指针j超出数组边界为止
# 6. 令i所指元素及其后面所有元素为0

def moveZeroes2(nums):
    i = 0
    j = 0
    size = len(nums)
    while j < size:
        while j < size and nums[j] == 0:
            j += 1
        if j >= size: break
        nums[i] = nums[j]
        i += 1
        j += 1
    while i < size:
        nums[i] = 0
        i += 1



if __name__ == '__main__':
    # moveZeroes1([0, 1, 0, 3, 12])
    moveZeroes2([0, 1, 0, 3, 12])
