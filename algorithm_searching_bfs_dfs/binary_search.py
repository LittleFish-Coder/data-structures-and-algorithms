# Time Complexity: O(log n)

def binary_search(arr, item):
    l, r = 0, len(arr) - 1
    counter = 0
    while l <= r:
        counter += 1
        mid = (l + r) // 2
        if arr[mid] == item:
            print(f"Found {item}, search time: {counter}")
            return True
        if item < arr[mid]:
            r = mid-1
        elif item > arr[mid]:
            l = mid+1

    return False


if __name__ == "__main__":
    arr = [1, 4, 6, 9, 12, 34, 45]
    item = 12

    print(binary_search(arr, item))
