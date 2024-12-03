def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(i, arr)
        

if __name__ == "__main__":
    arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(f"Before sorting: {arr}")

    selection_sort(arr)
    print(f"After sorting: {arr}")

    '''
    [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    Selection Sort (step by step):
    0 [0, 44, 6, 2, 1, 5, 63, 87, 283, 4, 99]
    1 [0, 1, 6, 2, 44, 5, 63, 87, 283, 4, 99]
    2 [0, 1, 2, 6, 44, 5, 63, 87, 283, 4, 99]
    3 [0, 1, 2, 4, 44, 5, 63, 87, 283, 6, 99]
    4 [0, 1, 2, 4, 5, 44, 63, 87, 283, 6, 99]
    5 [0, 1, 2, 4, 5, 6, 63, 87, 283, 44, 99]
    6 [0, 1, 2, 4, 5, 6, 44, 87, 283, 63, 99]
    7 [0, 1, 2, 4, 5, 6, 44, 63, 283, 87, 99]
    8 [0, 1, 2, 4, 5, 6, 44, 63, 87, 283, 99]
    9 [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
    10 [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
    '''