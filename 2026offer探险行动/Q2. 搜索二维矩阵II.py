# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5


def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    # 逐行寻找，要求每行的第一个元素必须小于target，最后一个元素大于等于target，然后在该行二分查找
    if rows == 0 or cols == 0:
        return False
    for i in range(rows):
        if matrix[i][0] == target or matrix[i][cols - 1] == target:
            return True
        elif matrix[i][0] < target:  # 二分查找
            j = 0
            k = cols - 1
            mid = (cols - 1) // 2
            while j <= k:
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    j = mid + 1
                else:
                    k = mid - 1
                mid = (j + k) // 2
        else:
            return False


# print(searchMatrix(matrix, target))
print(searchMatrix(matrix, 20))
