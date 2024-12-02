import heapq

# the deafult heap in python is min-heap

x = [5, 2, 8, 1, 6, 7, 4, 9]

heapq.heapify(x)
print(x)    # [1, 2, 4, 5, 6, 7, 8, 9]

heapq.heappush(x, 0)
print(x)    # [0, 1, 4, 2, 6, 7, 8, 9, 5]

print(heapq.heappop(x)) # 0
print(x)    # [1, 2, 4, 5, 6, 7, 8, 9]

# pop and push the element in same time
print (heapq.heappushpop(x, 5)) # 1
print(x)    # [2, 5, 4, 5, 6, 7, 8, 9]

# get n largest elements in heap 
print(heapq.nlargest(4,x))  # [9, 8, 7, 6]
# get n smallest elements in heap
print(heapq.nsmallest(4,x)) # [2, 4, 5, 5]