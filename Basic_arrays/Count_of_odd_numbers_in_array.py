def OddCount(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] % 2 == 1:
            count += 1
    return count

arr = [2, 5, 1, 4, 1]
print(OddCount(arr))