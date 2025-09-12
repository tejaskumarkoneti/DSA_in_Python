def sorted(arr,n):
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            return False
    return True

arr = [1,2,3,4,5,0]
n = len(arr)
print(sorted(arr,n))