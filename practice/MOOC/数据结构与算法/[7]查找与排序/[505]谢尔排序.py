"""
1、谢尔排序
    1、子列表间隔从n/2开始，每趟倍增: n/4, n/8...直到1
    2、每个间隔上单独执行插入排序
"""


def shellSort(unorder_list, reverse=False):
    sublist_count = len(unorder_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gapInsertSort(unorder_list, start_position, sublist_count, reverse)

        sublist_count = sublist_count // 2


def gapInsertSort(unorder_list, start=0, gap=1, reverse=False):
    for index in range(start+gap, len(unorder_list), gap):
        current_value = unorder_list[index]
        position = index

        if reverse is False:
            while position >= gap and unorder_list[position-gap] > current_value:
                unorder_list[position] = unorder_list[position-gap]
                position -= gap
        else:
            while position >= gap and unorder_list[position-gap] < current_value:
                unorder_list[position] = unorder_list[position-gap]
                position -= gap

        unorder_list[position] = current_value


if __name__ == '__main__':
    ls = [4, 1, 3, 2, 9, 7]
    shellSort(ls, reverse=True)
    print(ls)
