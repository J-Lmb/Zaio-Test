def minSwap(arr):
    counter = 0
    i = 0
    while(i < len(arr)-1):
        if arr[i] == i+1:
            i += 1
        else:
            temp_arr = arr[i]
            arr[i], arr[temp_arr-1] = arr[temp_arr-1], arr[i]
            counter += 1
            
    return counter
    
print("Input: {4, 3, 2, 1}")
print("Output: ", minSwap([4, 3, 2, 1]))

print("Input: {1, 5, 4, 3, 2}")
print("Output: ", minSwap([1, 5, 4, 3, 2]))