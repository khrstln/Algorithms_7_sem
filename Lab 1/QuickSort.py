def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = arr[0]
        less = []
        over = []
        eq = []
        for n in arr:
            if n < q:
                less.append(n)
            elif n > q:
                over.append(n)
            else:
                eq.append(n)
        return qsort(less) + eq + qsort(over)

arr = [3, 7, 9, 4, 1, 8, 9, 6, 3, 5, 7]
print(qsort(arr))
