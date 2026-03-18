# 给你一个 二进制 字符串 s 和一个整数 k。
# 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
# 字符串中 0 的数量最多为 k。
# 字符串中 1 的数量最多为 k。
# 返回一个整数，表示 s 的所有满足 k 约束的子字符串的数量。
#
# 示例 1：
# 输入：s = "10101", k = 1
# 输出：12
# 解释：s 的所有子字符串中，除了 "1010"、"10101" 和 "0101" 外，其余子字符串都满足 k 约束。

# 示例 2：
# 输入：s = "1010101", k = 2
# 输出：25
# 解释：s 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。
#
# 示例 3：
# 输入：s = "11111", k = 1
# 输出：15
# 解释：s 的所有子字符串都满足 k 约束。
from collections import Counter


def countKConstraintSubstrings(s: str, k: int) -> int:
    ans = 0
    left = 0
    cnt = {'0': 0, '1': 0}  # 用来统计子串中1和0的数量
    for right, c in enumerate(s):
        cnt[c] += 1
        while cnt['0'] > k and cnt['1'] > k:
            cnt[s[left]] -= 1
            left += 1
        ans += right - left + 1
    return ans


if __name__ == '__main__':
    s = "10101"
    k = 1
    print(countKConstraintSubstrings(s, k))
