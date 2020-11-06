# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4556 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_no_repeat_str = None
        max_no_repeat_str_length = 0
        for idx in range(len(s)):
            if idx + 1 >= len(s):
                if max_no_repeat_str is None:
                    max_no_repeat_str = s[idx]
                if max_no_repeat_str_length < len(max_no_repeat_str):
                    max_no_repeat_str_length = len(max_no_repeat_str)
                    max_no_repeat_str = s[idx:]
                print(max_no_repeat_str)
                return max_no_repeat_str_length
            s_buffer = s[idx]
            for i in range(idx+1, len(s)):
                if s[i] not in s_buffer:
                    s_buffer += s[i]
                    if max_no_repeat_str_length < len(s_buffer):
                        max_no_repeat_str = s_buffer
                        max_no_repeat_str_length = len(s_buffer)
                else:
                    if max_no_repeat_str_length < len(s_buffer):
                        max_no_repeat_str = s_buffer
                        max_no_repeat_str_length = len(s_buffer)
                    break
        else:
            return max_no_repeat_str_length

    def lengthOfLongestSubstringSecond(self, s):
        # 第二种解法 - 思想 一次循环 解决 动态维护max_no_repeat_str
        max_no_repeat_str = ''
        str_buffer = ''
        max_length = 0
        for i in range(len(s)):
            if s[i] not in str_buffer:
                # 不存在时直接怎加到str_buffer末尾
                str_buffer += s[i]
            else:
                # 存在时 说明此字符导致重复 则找到此字符并截断str_buffer
                s_idx = str_buffer.index(s[i])
                str_buffer = str_buffer[s_idx+1:] + s[i]

            if len(str_buffer) > max_length:
                max_no_repeat_str = str_buffer
                max_length = len(str_buffer)
        print(max_no_repeat_str)
        return max_length

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('pwwkew'))
    print(solution.lengthOfLongestSubstringSecond('pwwkew'))
