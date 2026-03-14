# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。


# 思路1：双重循环暴力破解
def maxArea1(height):
    size = len(height)
    max_area = 0
    for length in range(2, size + 1):
        left = 0
        right = left + length - 1
        while right < size:
            cur_area = min(height[right], height[left]) * (length - 1)
            if cur_area > max_area:
                max_area = cur_area
            left += 1
            right += 1
    return max_area


# 思路2：双指针初始时分别指向两端，循环中每次移动短的一端
def maxArea2(height):
    size = len(height)
    max_area = 0
    left = 0
    right = size - 1
    while left < right:
        cur_area = min(height[right], height[left]) * (right - left)
        if cur_area > max_area:
            max_area = cur_area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area


if __name__ == '__main__':
    # print(maxArea1([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
