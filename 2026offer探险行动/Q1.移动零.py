# 给定一个数组nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 示例
# 1:
# 输入: nums = [0, 1, 0, 3, 12]
# 输出: [1, 3, 12, 0, 0]
# 示例
# 2:
# 输入: nums = [0]
# 输出: [0]

# 法一：遍历数组，每次找到第一个0和下一个非0的数字，两两交换，以此类推
# nums = [1, 0]
# size = len(nums)
# i = 0
# j = 0
# while i < size and j < size:
#     # i 指向第一个0元素
#     while i < size and nums[i] != 0:
#         i += 1
#     # j 指向下一个非0元素
#     j = i + 1
#     while j < size and nums[j] == 0:
#         j += 1
#     # 交换i和j指向的元素
#     if j < size:
#         nums[i], nums[j] = nums[j], nums[i]
#     i += 1
# print(nums)

# 法二：双指针遍历数组，快指针遍历到非0元素，就将其放到慢指针位置，然后快慢指针均后移一位，如果快指针遍历到的是0元素，则慢指针不动
#      快指针后移一位
nums = [1, 0, 1]
size = len(nums)
i = 0  # 慢指针，指向当前可以存放非0元素的位置
j = 0  # 快指针，寻找非0元素
while j < size:
    if nums[j] != 0:
        nums[i] = nums[j]
        i += 1
        j += 1
    else:
        j += 1
while i < size:
    nums[i] = 0
    i += 1
print(nums)
