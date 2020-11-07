"""
1、冒泡排序
    1、对无序表进行多趟比较交换
    2、每趟包括了多次相邻比较，并将逆序的数据项互换位置。最终本趟最大项就位。
    3、经过n-1趟比较交换，实现完整排序
    4、每趟的过程类似于”气泡“在水中不断上浮到水面的过程
"""


def bubbleSort(unorder_list, reverse=False):
    for scan_length in range(len(unorder_list) - 1, 0, -1):
        for i in range(scan_length):
            if reverse is True:
                if unorder_list[i] < unorder_list[i+1]:
                    unorder_list[i], unorder_list[i+1] = unorder_list[i+1], unorder_list[i]
            else:
                if unorder_list[i] > unorder_list[i+1]:
                    unorder_list[i], unorder_list[i+1] = unorder_list[i+1], unorder_list[i]
    return unorder_list


if __name__ == '__main__':
    u_ls = [1, 3, 2, 7, 4]
    ls = bubbleSort(u_ls, reverse=True)
    print(ls)

