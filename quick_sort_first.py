def quick_sort_first(arr, low, high):

    if low < high:
        pi = partition_first(arr, low, high)
        quick_sort_first(arr, low, pi-1)
        quick_sort_first(arr, pi+1, high)



def partition_first(arr, low, high):
    pi = arr[low]
    i = high + 1
    for j in range(high, low, -1):
        if arr[j] > pi:
            i -= 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i-1], arr[low] = arr[low], arr[i-1]
    return i-1


arr = [2, 1, 4, 21, 3]
n = len(arr)
quick_sort_first(arr, 0, n-1)
print(arr)