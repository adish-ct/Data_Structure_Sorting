""" ___ Bubble Sort ___
    compare adjacent values and swapping
    store large or smaller element at the right end or left end after the 1 iteration completed depends on your code
"""
# def sort(li):
#     for i in range(len(li)-1,0,-1):
#         for j in range(i):
#             if li[j] < li[j+1]:
#                 temp = li[j]
#                 li[j] = li[j+1]
#                 li[j+1] = temp
#
#
# print("....bubble sort....".upper())
# li = [23, 45, 16, 75, 97, 13, 18, 82, 54]
# print("List before sorting :", li)
# sort(li)
# print("List after sorting :", li)

""" ___ Selection Sort ___
    devided list into two section . sorted section and unsorted section
    we can avoid multiple swapping in selection sort
"""

#
# def sort(li):
#     for i in range(len(li)):
#         max_pos = i
#         for j in range(i + 1, len(li)):
#             if li[j] > li[max_pos]:
#                 max_pos = j
#         li[i], li[max_pos] = li[max_pos], li[i]
#
#
# print("....selection sort....".upper())
# li = [23, 45, 16, 75, 97, 13, 18, 82, 54]
# print("List before sorting :", li)
# sort(li)
# print("List after sorting :", li)

""" --- Insertion Sort ---
    it takes the element quickly, 
    separate into two , sorted part and unsorted part
    the current selected element scan through the sorted part and swap
"""

#
# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         current = my_list[i]
#         pos = i
#         while current > my_list[pos - 1] and pos > 0:
#             my_list[pos] = my_list[pos - 1]
#             pos = pos - 1
#
#         my_list[pos] = current
#
#
# print("....insertion sort....".upper())
# li = [23, 45, 16, 75, 97, 13, 18, 82, 54]
# print("List before sorting :", li)
# insertion_sort(li)
# print("List after sorting :", li)


""" ___Quick Sort___ 
    choose a pivot element
    find the position of pivot element and separate the list into right and left based on the pivot
"""

#
# def pivot_location(my_list, first, last):
#     pivot = my_list[first]
#     left = first + 1
#     right = last
#     while True:
#         while left <= right and my_list[left] <= pivot:
#             left = left + 1
#         while left <= right and my_list[right] >= pivot:
#             right = right - 1
#         if right < left:
#             break
#         else:
#             my_list[left], my_list[right] = my_list[right], my_list[left]
#     my_list[first], my_list[right] = my_list[right], my_list[first]
#     return right
#
#
# def quick_sort(my_list, first, last):
#     if first < last:
#         p = pivot_location(my_list, first, last)
#         quick_sort(my_list, first, p - 1)
#         quick_sort(my_list, p + 1, last)
#
#
# print("....quick sort....".upper())
# li = [23, 45, 16, 75, 97, 13, 18, 82, 54]
# print(li)
# last_position = len(li)
#
# quick_sort(li, 0, last_position - 1)
# print(li)


""" ___ Merge Sort ___
    Devide - conquer - combine algorithm used
    separate list into two parts untill it become a single element
    find middle element and separate the list at that point
"""

#
# def merge_sort(my_list):
#     if len(my_list) > 1:
#         mid = len(my_list) // 2
#         left_list = my_list[:mid]
#         right_list = my_list[mid:]
#         merge_sort(left_list)
#         merge_sort(right_list)
#
#         i, j, k = 0, 0, 0
#         while i < len(left_list) and j < len(right_list):
#             if left_list[i] > right_list[j]:
#                 my_list[k] = left_list[i]
#                 i += 1
#                 k += 1
#             else:
#                 my_list[k] = right_list[j]
#                 j += 1
#                 k += 1
#         while i < len(left_list):
#             my_list[k] = left_list[i]
#             i += 1
#             k += 1
#         while j < len(right_list):
#             my_list[k] = right_list[j]
#             j += 1
#             k += 1
#
# print("---- Merge sort ---".upper())
# li = [12, 35, 24, 63, 45, 47, 21, 14, 8, 6, 59, 89]
# print("my list before sort :".upper(), li)
# merge_sort(li)
# print("my list after sort :".upper(), li)
#
#





