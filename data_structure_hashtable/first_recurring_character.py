# Google Question

# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# First recurring character is 2 (return 2)

# Given an array array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# First recurring character is 1 (return 1)

# Given an array array = [2, 3, 4, 5]
# First recurring character is None (return None)

# Time Complexity: O(n)
# Space Complexity: O(1)

def find_first_recurr(array):
    hashtable = {}
    for index, num in enumerate(array):
        if num in hashtable.keys():
            return num
        else:
            hashtable[num] = index  # store the index
    return None

print(find_first_recurr([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(find_first_recurr([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(find_first_recurr([2, 3, 4, 5]))
