def counting_sort(arr):

    maximum = max(arr)
    count = [0]*(maximum +1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    output = [0]*len(arr)

    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num
    return output


arr = [38, 27, 43, 3]
print(counting_sort(arr))