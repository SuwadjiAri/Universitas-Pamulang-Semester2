#  Fungsi quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        for x in arr[1:]:
            if x[1] <= pivot[1]:
                left.append(x)
        right = []
        for x in arr[1:]:
            if x[1] > pivot[1]:
                right.append(x)
        return quick_sort(right) + [pivot] + quick_sort(left)
        