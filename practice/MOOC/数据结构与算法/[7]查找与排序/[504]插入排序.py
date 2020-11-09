"""
1、插入排序
    1、列表前部维持一个已排好的子列表，然后逐步扩大子列表直到全表
        1.1、第一趟子列表仅包含一个数据项，将第二个新项插入到合适的位置
        1.2、第二趟，继续将第三个数据项，跟前两个数据项比对，并移动比自身大的数据项
            空出位置，以便第三个数据项加入
        1.3、经过n-1趟对比，子列表扩展到全表，排序完成
    2、时间复杂度
        共需要插入n-1次
        每次最差需要交换n次
        所以为 O(n^2)
"""


def insertSort(unorder_list, reverse=False):
    for index in range(1, len(unorder_list)):
        current_value = unorder_list[index]
        position = index
        # 对比
        if reverse is False:
            while position > 0 and unorder_list[position-1] > current_value:
                # 交换
                unorder_list[position] = unorder_list[position-1]
                position -= 1
        else:
            while position > 0 and unorder_list[position-1] < current_value:
                # 交换
                unorder_list[position] = unorder_list[position-1]
                position -= 1

        # 插入新项
        if position != index:
            # 相等说明position不需要发生交换赋值
            unorder_list[position] = current_value


if __name__ == '__main__':
    ls = [4, 1, 3, 2, 9, 7]
    insertSort(ls, reverse=True)
    print(ls)
