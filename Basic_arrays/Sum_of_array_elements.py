def arraySum(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum

arr = [1, 2, 4, 5, 2]
print(arraySum(arr))