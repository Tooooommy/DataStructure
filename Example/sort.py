"""
排序算法： https://baike.baidu.com/item/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95/5399605?fr=aladdin
"""


##########
"""
    冒泡排序:每对相邻元素进行比较，如果元素不合适，元素将进行交换。
    时间复杂度:O(n) / O(n^2)
"""


def bubble_sort(unsorted_list):
    for iter_num in range(len(unsorted_list) - 1, 0, -1):
        for idx in range(iter_num):
            if unsorted_list[idx] > unsorted_list[idx + 1]:
                unsorted_list[idx], unsorted_list[idx + 1] = unsorted_list[idx + 1], unsorted_list[idx]


unsorted_list = [19, 2, 31, 45, 6, 11, 121, 27]
bubble_sort(unsorted_list)
print(unsorted_list)

##########
"""
    归并排序:采用分治法（Divide and Conquer）的一个非常典型的应用。
    将已有序的子序列合并，得到完全有序的序列；
    即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
    事件复杂度： O(nlog₂n)
"""


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = int(len(unsorted_list) / 2)
    left = merge_sort(unsorted_list[:middle])
    right = merge_sort(unsorted_list[middle:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))

###########
"""
直接插入排序: 将一条记录插入到已排好的有序表中，从而得到一个新的、记录数量增1的有序表
时间复杂度: O(n^2) 
空间复杂度: O(1) 
"""


def insert_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):  # 选择排序
        for j in range(i):
            if unsorted_list[i] < unsorted_list[j]:  # 无序队列中i碰到比有序队列j大的数据，insert
                unsorted_list.insert(j, unsorted_list.pop(i))
                break
    return unsorted_list


unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(insert_sort(unsorted_list))

##########
"""
基数排序：（radix sort）属于“分配式排序”（distribution sort），又称“桶子法”（bucket sort）
        透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用
时间复杂度: O(nlog(r)m)
"""
import math


def radix_sort(unsorted_list, radix=10):
    K = int(math.ceil(math.log(max(unsorted_list), radix)))  # 根据基数获取位数
    bucket = [[] for _ in range(radix)]
    for i in range(1, K + 1):
        for value in unsorted_list:
            # value % (radix ** i) 获取i位基数的模
            # // (radix ** (i - 1)) 获取摸的i位数字
            bucket[value % (radix ** i) // (radix ** (i - 1))].append(value)
        del unsorted_list[:]  # 删除之前的数据
        for each in bucket:
            unsorted_list.extend(each)  # 桶合并
        bucket = [[] for _ in range(radix)]  # 重新设置

    return unsorted_list


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(radix_sort(unsorted_list))

##########
"""
    快速排序：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
            然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
    时间复杂度： O(nlogn)
"""


def quick_sort(unsorted_list, low, high):
    i = low
    j = high
    if i >= j:
        return unsorted_list
    key = unsorted_list[i]
    while i < j:
        while i < j and unsorted_list[j] >= key:
            j -= 1
        unsorted_list[i] = unsorted_list[j]
        while i < j and unsorted_list[i] <= key:
            i += 1
        unsorted_list[j] = unsorted_list[i]
    unsorted_list[i] = key
    quick_sort(unsorted_list, low, i - 1)
    quick_sort(unsorted_list, j + 1, high)
    return unsorted_list


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(unsorted_list, 0, len(unsorted_list) - 1))

##########
"""
    希尔排序(Shell's Sort): 插入排序的一种又称“缩小增量排序”（Diminishing Increment Sort），
        是直接插入排序算法的一种更高效的改进版本
        把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
        随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
    时间复杂度: O(n^2) 
"""


def shell_sort(unsorted_list):
    gap = len(unsorted_list) // 2
    while gap > 0:
        for i in range(gap, len(unsorted_list)):
            temp = unsorted_list[i]
            j = i
            while j >= gap and unsorted_list[j - gap] > temp:
                unsorted_list[j] = unsorted_list[j - gap]
                j = j - gap
            unsorted_list[j] = temp
        gap = gap // 2
    return unsorted_list


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(unsorted_list))

##########
"""
    堆排序(Heapsort): 指利用堆积树（堆）这种数据结构所设计的一种排序算法,可以利用数组的特点快速定位指定索引的元素。
        堆分为大根堆和小根堆，是完全二叉树。大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
        在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
    时间复杂度： O(nlgn)
"""


def max_heapify(heap, HeapSize, root):  # 在堆中做结构调整使得父节点的值大于子节点
    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heapify(heap, HeapSize, larger)


def build_max_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)  # 将堆的长度当独拿出来方便
    for i in range((HeapSize - 2) // 2, -1, -1):  # 从后往前出数
        max_heapify(heap, HeapSize, i)  # 调整堆


def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    build_max_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)  # 调整堆
    return heap


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(unsorted_list))

##########
"""
    选择排序:（Selection sort）是一种简单直观的排序算法。
        工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，
        存放在序列的起始位置，直到全部待排序的数据元素排完。
    时间复杂度： O(n^2)
"""


def selection_sort(unsorted_list):
    for index in range(len(unsorted_list)):
        min_index = index
        for j in range(min_index + 1, len(unsorted_list)):
            if unsorted_list[min_index] > unsorted_list[j]:
                min_index = j
        unsorted_list[index], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[index]
    return unsorted_list


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(unsorted_list))
