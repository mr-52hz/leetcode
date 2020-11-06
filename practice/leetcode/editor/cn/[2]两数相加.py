# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
# 并且它们的每个节点只能存储 一位 数字。如果，我们将这两个数相加起来，则会返回一个新的链表
# 来表示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学 
#  👍 5205 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = str(self.val)
        _next = self.next
        while _next is not None:
            s += ' -> ' + str(_next.val)
            _next = _next.next

        return s


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _next_l1 = l1.next
        _next_l2 = l2.next
        n1 = str(l1.val)
        while _next_l1 is not None:
            n1 = str(_next_l1.val) + n1
            _next_l1 = _next_l1.next

        n2 = str(l2.val)
        while _next_l2 is not None:
            n2 = str(_next_l2.val) + n2
            _next_l2 = _next_l2.next

        a = str(int(n1) + int(n2))
        ln = ListNode()
        _next = None
        for val in a[::-1]:
            if ln.val == 0 and _next is None:
                ln.val = int(val)
                _next = ln
            else:
                new_node = ListNode(int(val))
                _next.next = new_node
                _next = new_node
        return ln
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    #  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
