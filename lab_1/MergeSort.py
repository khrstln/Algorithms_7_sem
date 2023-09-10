# Функция, осуществляющая слияние двух отсортированных списков
def Merge(SortedList1, SortedList2):
    idx1, idx2 = 0, 0
    res = []
    while idx1 < len(SortedList1) and idx2 < len(SortedList2):
        if SortedList1[idx1] >= SortedList2[idx2]:
            res.append(SortedList2[idx2])
            idx2 += 1
        else:
            res.append(SortedList1[idx1])
            idx1 += 1
    res += SortedList1[idx1:] + SortedList2[idx2:]
    return res

# Функция, осуществляющая сортировку слиянием
def MergeSort(List):
    if len(List) == 1:
        return List
    half = len(List) // 2
    FirstHalf = MergeSort(List[:half])
    SecondHalf = MergeSort(List[half:])
    return Merge(FirstHalf, SecondHalf)

import random
random.seed(1)
List_to_sort = [random.randrange(0, 10) for _ in range(6)]
print()
print()
print()
print("Unsorted list =", List_to_sort)
print()
print("Sorted list =", MergeSort(List_to_sort))
print()