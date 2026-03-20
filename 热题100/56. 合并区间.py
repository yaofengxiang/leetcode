# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 示例1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 示例2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

# 示例3：
# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    ans = []
    intervals.sort(key=lambda x: x[0])  # 按照每个区间的左端点升序排序
    for p in intervals:
        if ans and p[0] <= ans[-1][1]:  # 合并区间
            ans[-1][1] = max(ans[-1][1], p[1])
        else:
            ans.append(p)
    return ans


if __name__ == '__main__':
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [4, 5]]
    intervals = [[4, 7], [1, 4]]
    print(merge(intervals))
