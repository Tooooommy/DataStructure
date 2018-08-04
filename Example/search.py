"""
搜索算法:用关键字标识一个数据元素，查找时根据给定的某个值，在表中确定一个关键字的值等于给定值的记录或数据元素。
        在计算机中进行查找的方法是根据表中的记录的组织结构确定的。
"""

##########
"""
　顺序查找: 也称为线形查找，从数据结构线形表的一端开始，顺序扫描，依次将扫描到的结点关键字与给定值k相比较，若相等则表示查找成功；
            若扫描结束仍没有找到关键字等于k的结点，表示查找失败。
"""


def linear_search(search_list, search_val):
    search_index = -1
    for index, value in enumerate(search_list):
        if value == search_val:
            search_index = index
            break
    return search_index + 1


l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))

##########
"""
    二分查找要求线形表中的结点按关键字值升序或降序排列，用给定值k先与中间结点的关键字比较，中间结点把线形表分成两个子表，若相等则查找成功；
    若不相等，再根据k与该中间结点关键字的比较结果确定下一步查找哪个子表，这样递归进行，直到查找到或查找结束发现表中没有这样的结点。
"""


def binary_search(search_list, search_val):
    low = 0  # 最小下标
    high = len(search_list) - 1  # 最大下标
    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] == search_val:
            return mid + 1
        elif search_list[mid] > search_val:
            high = mid - 1
        else:
            low = mid + 1
    return -1


ret = binary_search(list(range(1, 10)), 3)
print(ret)

##########
"""
    分块查找: 是折半查找和顺序查找的一种改进方法，分块查找由于只要求索引表是有序的，对块内节点没有排序要求，因此特别适合于节点动态变化的情况。
"""
