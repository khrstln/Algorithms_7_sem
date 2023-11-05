from MergeSort import MergeSortFunc
from BubbleSort import BubbleSortFunc
import random

random.seed(1)
List_to_sort = [random.randrange(0, 10) for _ in range(6)]
print("Unsorted list =", List_to_sort, end="\n\n")
print("Merge sort:")
print("Sorted list =", MergeSortFunc(List_to_sort), end="\n\n")
print("Bubble sort:")
print("Sorted list =", BubbleSortFunc(List_to_sort))
