def sortArray(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                return False
    return True

arr = [2, 4, 5, 1, 3]
print(sortArray(arr))        
            