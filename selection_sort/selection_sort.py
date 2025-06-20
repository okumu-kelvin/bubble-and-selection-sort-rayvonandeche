def min(arr, i, n):
    smallest = arr[i]
    pos = i
    for j in range(i + 1, n):
        if arr[j] < smallest:
            smallest = arr[j]
            pos = j
            
    return pos

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        pos = min(arr, i, n)
        if i != pos:
            arr[i], arr[pos] = arr[pos], arr[i]
            
    return arr