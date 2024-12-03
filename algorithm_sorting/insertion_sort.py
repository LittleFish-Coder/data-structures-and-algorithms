# Insertion Sort (Stable)
# Time complexity: O(n^2)
# Best case: O(n)

# Insertion sort works by dividing the array into a sorted and an unsorted part.
# Initially, the sorted part contains only the first element.
# Then, it takes each element from the unsorted part and inserts it into the correct position in the sorted part.
# This process is repeated until the entire array is sorted.
        
def insertion_sort(arr):
    # insertion sort
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:  # inbound and next < prev
            # swap two items
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1  # decrement j to continue comparing with previous elements
        print(f"Array after inserting element at index {i}: {arr}")


if __name__ == "__main__":
    arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(f"Before sorting: {arr}")

    insertion_sort(arr)
    print(f"After sorting: {arr}")

    '''
    [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    Insertion Sort (step by step):
    1: [44, 99, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    2: [6, 44, 99, 2, 1, 5, 63, 87, 283, 4, 0]
    3: [2, 6, 44, 99, 1, 5, 63, 87, 283, 4, 0]
    4: [1, 2, 6, 44, 99, 5, 63, 87, 283, 4, 0]
    5: [1, 2, 5, 6, 44, 99, 63, 87, 283, 4, 0]
    6: [1, 2, 5, 6, 44, 63, 99, 87, 283, 4, 0]
    7: [1, 2, 5, 6, 44, 63, 87, 99, 283, 4, 0]
    8: [1, 2, 5, 6, 44, 63, 87, 99, 283, 4, 0]
    9: [1, 2, 4, 5, 6, 44, 63, 87, 99, 283, 0]
    10: [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
    
    '''