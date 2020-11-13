# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指\
# 的是节点编号的奇偶性，而不是节点的值的奇偶性。
# 
#  请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
#  
# 
#  示例 2: 
# 
#  输入: 2->1->3->5->6->4->7->NULL 
# 输出: 2->3->6->7->1->5->4->NULL 
# 
#  说明: 
# 
#  
#  应当保持奇数节点和偶数节点的相对顺序。 
#  链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。 
#  
#  Related Topics 链表 
#  👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index = 1
        current_list_node = head
        last_odd_index_list_node = head
        first_even_index_list_node = None
        last_even_index_list_node = None
        while current_list_node:
            if index % 2 == 0:
                # 偶数节点
                if first_even_index_list_node is None:
                    first_even_index_list_node = current_list_node
                    last_even_index_list_node = current_list_node
                else:
                    last_even_index_list_node.next = current_list_node
                    last_even_index_list_node = current_list_node
            else:
                # 奇数节点
                if first_even_index_list_node is not None:
                    last_odd_index_list_node.next = current_list_node
                    last_odd_index_list_node = current_list_node

            index += 1
            current_list_node = current_list_node.next

        if last_even_index_list_node:
            last_even_index_list_node.next = None
            last_odd_index_list_node.next = first_even_index_list_node

        return head
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    #  输入: 1->2->3->4->5->NULL
    # 输出: 1->3->5->2->4->NULL
    # head = ListNode(val=1)
    # head.next = ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))
    head = None

    solution = Solution()
    head = solution.oddEvenList(head)
    cn = ''
    this = head
    while this:
        cn += (str(this.val) + '->')
        this = this.next
    cn += 'None'
    print(cn)