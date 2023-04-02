def countingSort(arr):
    count_arr = [0]*100
    for i in range(0, len(arr)):
        count_arr[arr[i]] += 1
    return count_arr
