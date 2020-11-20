# 对链表进行插入排序。 
# 
#  
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。 
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。 
# 
#  
# 
#  插入排序算法： 
# 
#  
#  插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。 
#  每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。 
#  重复直到所有输入数据插入完为止。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#  
# 
#  示例 2： 
# 
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#  
#  Related Topics 排序 链表 
#  👍 262 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # 拆分未有序和无序部分
        unorder_list_node = head.next
        order_list_node = head
        order_list_node.next = None

        # 从无需部分拆分一个节点
        insert_node = unorder_list_node
        unorder_list_node = unorder_list_node.next
        insert_node.next = None

        while insert_node:
            # 无序待插入节点
            before_order_node = None
            cur_order_node = order_list_node
            while cur_order_node:
                if cur_order_node.val > insert_node.val:
                    if before_order_node is None:
                        # 直接作为头部节点
                        insert_node.next = order_list_node
                        order_list_node = insert_node
                        break
                    else:
                        before_order_node.next = insert_node
                        insert_node.next = cur_order_node
                        break
                elif cur_order_node.next is not None:
                    before_order_node = cur_order_node
                    cur_order_node = cur_order_node.next
                else:
                    cur_order_node.next = insert_node
                    break

            if unorder_list_node is not None:
                insert_node = unorder_list_node
                unorder_list_node = unorder_list_node.next
                insert_node.next = None
            else:
                break

        return order_list_node

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    #  输入: 4->2->1->3
    # 输出: 1->2->3->4
    # head = ListNode(4)
    # head.next = ListNode(2)
    # head.next.next = ListNode(1)
    # head.next.next.next = ListNode(3)

    #  输入: -1->5->3->4->0
    # 输出: -1->0->3->4->5
    head = ListNode(-1)
    head.next = ListNode(5)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(0)

    solution = Solution()
    head = solution.insertionSortList(head)

    s = ''
    while head.next:
        s += (str(head.val) + '->')
        head = head.next
    s += str(head.val)

    print(s)

