def movezero(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            arr.append(0)
            arr.pop(i)
    return arr

arr = [0, 1, 0, 3, 12]
print(movezero(arr))
