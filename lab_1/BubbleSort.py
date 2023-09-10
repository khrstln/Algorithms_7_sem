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