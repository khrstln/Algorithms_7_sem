# ЛР №1: Алгоритмы сортировки

## Цель

Познакомить студента с основами анализа алгоритмов на примере операций
сортировки.

## Задача

### 1. Сортировка слиянием

```python
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
    FirstHalf = List[:half]
    SecondHalf = List[half:]
    FirstHalf = MergeSort(FirstHalf)
    SecondHalf = MergeSort(SecondHalf)
    return Merge(FirstHalf, SecondHalf)

import random
random.seed(1)
List_to_sort = [random.randrange(0, 10) for _ in range(10)]
print()
print()
print()
print("Unsorted list =", List_to_sort)
print()
print("Sorted list =", MergeSort(List_to_sort))
print()
```

Временная сложность алогритма = $O \big(n log_2(n)\big)$

Затраты дополнительной памяти = $O\big( n \big)$

### 2. Сортировка пузырьком

```python
def BubbleSort(List):
    for i in range(len(List)-1, -1, -1):
        for j in range(i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

import random
random.seed(1)
List_to_sort = [random.randrange(0, 10) for _ in range(5)]
print()
print("Unsorted list =", List_to_sort)
print()
print("Sorted list =", BubbleSort(List_to_sort))
print()
```

Временная сложность алгоритма = $O \big(\frac{n(n-1)}{2} \big) = O \big(n^2 \big)$

Затраты дополнительной памяти = $O(1)$
