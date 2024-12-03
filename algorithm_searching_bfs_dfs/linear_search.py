# Time Complexity: O(n)

def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            print(f"Found {item}, search time: {i+1}")
            return True
    return False

if __name__ == "__main__":
    arr = [1, 4, 6, 9, 12, 34, 45]
    item = 12

    print(linear_search(arr, item))
    