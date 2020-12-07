# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。 
# 
#  移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。 
# 
#  在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。 
# 
#  返回尽可能高的分数。 
# 
#  
# 
#  
#  
# 
#  示例： 
# 
#  输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20 
#  1 <= A[0].length <= 20 
#  A[i][j] 是 0 或 1 
#  
#  Related Topics 贪心算法 
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 0:
            return 0

        for line, ls in enumerate(A):
            if ls[0] == 0:
                self.move(A, line=line)
        column_length = len(A[0])
        for column in range(1, column_length):
            count = 0
            for line in A:
                if line[column] == 0:
                    count += 1
                if count > len(A) // 2:
                    self.move(A, column)
                    break

        return sum(int(''.join([str(value) for value in line]), 2) for line in A)

    @staticmethod
    def move(A, column=None, line=None):
        if column is not None:
            for ls in A:
                ls[column] = 0 if ls[column] == 1 else 1
        if line is not None:
            values = A.pop(line)
            A.insert(line, [0 if value == 1 else 1 for value in values])


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # A = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    A = [[1, 1], [1, 1], [0, 1]]
    solution = Solution()
    print(solution.matrixScore(A))
