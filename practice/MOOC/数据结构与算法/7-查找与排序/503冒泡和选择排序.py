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


"""
冒泡排序的复杂度分析及优劣势
    复杂度
        对比 1~n-1 > (1+n-1)*(n-1)/2
        交换 最差情况就是每次对比都交换 = 对比次数
        所以 (1+n-1)*(n-1)/2*2 = O(n^2) 
    优点
        无需额外的存储空间的开销
    缺点
        必须要经过多次的对比和交换、其中大部分操作都不是最终的交换
        
    优化
        可以设置标识，如果在一次对比中没有发生任何交换，则意味着列表已经有序，可以提前结束
        虽然能够节省部分时间，但是不能改变冒泡排序的时间复杂度。
"""


def shortBubbleSort(unorder_list, reverse=False):
    for scan_length in range(len(unorder_list)-1, 0, -1):
        is_exchange = False
        for i in range(scan_length):
            if reverse is True:
                if unorder_list[i] < unorder_list[i+1]:
                    unorder_list[i], unorder_list[i+1] = unorder_list[i+1], unorder_list[i]
                    is_exchange = True
            else:
                if unorder_list[i] > unorder_list[i+1]:
                    unorder_list[i], unorder_list[i+1] = unorder_list[i+1], unorder_list[i]
                    is_exchange = True

        if is_exchange is False:
            break
    return unorder_list


if __name__ == '__main__':
    u_ls = [1, 3, 2, 7, 4]
    ls = bubbleSort(u_ls, reverse=True)
    print(ls)
    ls2 = shortBubbleSort(u_ls)
    print(ls2)

