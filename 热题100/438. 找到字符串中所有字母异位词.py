# 给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 示例1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0, 6]
# 解释:起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

# 示例2:
# 输入: s = "abab", p = "ab"
# 输出: [0, 1, 2]
# 解释:起始索引等于0的子串是"ab", 它是"ab"的异位词。起始索引等于1 的子串是"ba", 它是"ab"的异位词。起始索引等于2的子串是 "ab", 它是"ab" 的异位词。

import numpy as np

# def findAnagrams(s, p):
#     ans = list()
#     n = len(s)
#     left = 0
#     right = left + len(p) - 1
#     sorted_p = ''.join(sorted(p))
#     while right < n:
#         sub_s = list(s[left:right + 1])
#         if ''.join(np.sort(sub_s)) == sorted_p:
#             ans.append(left)
#         left += 1
#         right += 1
#     return ans

from collections import Counter


def findAnagrams(s, p):
    ans = list()
    cnt_p = Counter(p)
    cnt_s = Counter()
    for right, c in enumerate(s):
        # 入
        cnt_s[c] += 1

        # 更新
        left = right - len(p) + 1
        if left < 0:
            continue
        if cnt_p == cnt_s:
            ans.append(left)

        # 出
        cnt_s[s[left]] -= 1
    return ans


if __name__ == '__main__':
    # s = "cbaebabacd"
    # p = "abc"
    s = "abab"
    p = "ab"
    print(findAnagrams(s, p))
