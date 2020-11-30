# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。 
# 
#  如果数组元素个数小于 2，则返回 0。 
# 
#  示例 1: 
# 
#  输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。 
# 
#  示例 2: 
# 
#  输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。 
# 
#  说明: 
# 
#  
#  你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。 
#  请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
#  
#  Related Topics 排序 
#  👍 282 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        # O(n)
        max_num = max(nums)
        min_num = min(nums)

        # buffer size O(1)
        # buffer size should not be zero
        buffer_size = max(1, (max_num - min_num) // (len(nums) - 1))
        buffer_num = (max_num - min_num) // buffer_size + 1

        # O(buffer_num)
        buffer = [[] for _ in range(buffer_num)]

        # O(n)
        for num in nums:
            # position = (num - min_num) // buffer_size
            position = (num - min_num) // buffer_size
            buffer[position].append(num)

        max_gap = 0
        pre_max = max(buffer[0])

        # O(n)
        for i in range(1, buffer_num):
            current_buffer = buffer[i]
            if current_buffer:
                current_buffer_min_num = min(current_buffer)
                if current_buffer_min_num - pre_max > max_gap:
                    max_gap = current_buffer_min_num - pre_max
                pre_max = max(current_buffer)

        return max_gap

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    #  输入: [3,6,9,1]
    # 输出: 3
    # ls = [3, 6, 9, 1]
    ls = [1, 1, 1, 1]
    solution = Solution()
    print(solution.maximumGap(ls))
