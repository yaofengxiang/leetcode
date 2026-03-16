# 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
#
# 示例1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"abc"，所以其长度为 3。注意"bca"和"cab"也是正确答案。

# 示例2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是"b"，所以其长度为1。

# 示例3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为3。请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

# def has_duplicate_chars(s):
#     seen = {}  # 记录已出现的字符
#     for char in s:
#         if char in seen:
#             return True  # 发现重复，直接返回
#         seen[char] = True
#     return False  # 遍历完无重复


# def lengthOfLongestSubstring(s):
#     n = len(s)
#     if n == 0 or n == 1:
#         return n
#     ans = 1
#     for size in range(2, n+1):
#         # size 表示滑动窗口的大小
#         for i in range(0, n - size + 1):
#             # i 表示滑动窗口的第一个元素下标
#             if has_duplicate_chars(s[i:i+size]):
#                 continue
#             else:
#                 ans = max(ans, size)
#                 break
#     return ans
from collections import Counter


def lengthOfLongestSubstring(s):
    left = 0
    ans = 0
    cnt = Counter()
    for right, c in enumerate(s):
        cnt[c] += 1
        while cnt[c] > 1:
            cnt[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring('bbbbb'))
    print(lengthOfLongestSubstring('pwwkew'))
