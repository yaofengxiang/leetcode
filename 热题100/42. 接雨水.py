# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

# 示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9

# 算法：
# left = 0, right = left + 1, size = len(height)
# ①找到第一个比height[left]大或者相等的；如果 right>=size 且 left < size - 2，则 left += 1, right = left + 1
# ②找到后，计算中间能够存储多少水
# ③left = right, right += 1；如果left >= size - 2，则结束，否则返回①
# def trap(height):
#     total_capacity = 0
#     size = len(height)
#     left = 0
#     right = left + 1
#     while left < size - 2:
#         left_capacity = height[left]
#         current_capacity = 0
#         while right < size and height[right] < height[left]:
#             current_capacity += left_capacity - height[right]
#             right += 1
#         # 循环中止条件：height[right] >= height[left] or right >= size
#         if right >= size:
#             left += 1
#             right = left + 1
#         else:
#             total_capacity += current_capacity
#             left = right
#             right = left + 1
#     return total_capacity


# def trap(height):
#     total_capacity = 0
#     size = len(height)
#     left = 0
#     while left < size - 2:
#         mid = left + 1
#         current_capacity = 0
#         if height[left] > height[mid]:  # 必须满足两边高，中间低
#             right = mid + 1
#         else:  # height[left] <= height[mid]
#             left += 1
#             continue
#         # 先找到第一个比height[mid]大的
#         while right < size and height[right] <= height[mid]:
#             right += 1
#         # 循环中止条件：height[right] > height[mid] or right >= size
#         if right >= size:
#             left += 1
#         else:
#             right_history = right
#             while right_history < size - 1 and height[right_history] <= height[right_history + 1] < height[left]:
#                 right_history += 1
#             if height[right_history] >= height[left]:
#                 upper = min(height[left], height[right_history])
#                 while mid < right_history:
#                     current_capacity += upper - height[mid]
#                     mid += 1
#                 left = right_history
#             else:
#                 # 找到了第一个比height[mid]大的，再尝试寻找第一个比height[right_history]大的或者相等的
#                 while right < size and height[right] < height[left]:
#                     right += 1
#                 # 循环中止条件：height[right] >= height[left] or right >= size
#                 if right >= size:
#                     # 按照 right_history 计算存水容量
#                     upper = min(height[left], height[right_history])
#                     while mid < right_history:
#                         current_capacity += upper - height[mid]
#                         mid += 1
#                     left = right_history
#                 else:
#                     # 按照 right 计算存水容量
#                     upper = min(height[left], height[right])
#                     while mid < right:
#                         current_capacity += upper - height[mid]
#                         mid += 1
#                     left = right
#             total_capacity += current_capacity
#     return total_capacity


# 思路1：前后缀分解法(来自B站up 灵茶山艾府)
# 每个height[i]视为一个宽度为1的水桶，左右各有一块挡板，高度分别成为前缀和后缀
# 其中前缀是i水桶所有前缀的最大值，后缀是i水桶所有后缀的最大值。可以通过遍历分别得到前缀辅助数组和后缀辅助数组。
def trap(height):
    n = len(height)  # 水桶的数量
    total_capacity = 0

    # 前缀辅助数组
    pre_max = [0] * n
    pre_max[0] = height[0]
    for i in range(1, n):
        pre_max[i] = max(pre_max[i-1], height[i])

    # 后缀辅助数组
    suf_max = [0] * n
    suf_max[-1] = height[-1]
    for i in range(n-2, -1, -1):
        suf_max[i] = max(suf_max[i+1], height[i])

    for h, pre, suf in zip(height, pre_max, suf_max):
        total_capacity += min(pre, suf) - h
    return total_capacity


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap([4, 2, 0, 3, 2, 5]))
    print(trap([2, 8, 5, 5, 6, 1, 7, 4, 5]))
