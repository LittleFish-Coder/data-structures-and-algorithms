class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
            self.length += 1
    
    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, val):
        if index == 0:
            self.prepend(val)
            return
        if index >= self.length:
            self.append(val)
            return
        
        i = 0
        curr = self.head
        while curr:
            if i == index-1:
                prev_node, mid_node, next_node = curr.prev, Node(val), curr
                prev_node.next, mid_node.prev = mid_node, prev_node
                mid_node.next, next_node.prev = next_node, mid_node
                self.length += 1
                break
            curr = curr.next
            i += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        if index >= self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        i = 0
        curr = self.head
        while curr:
            if i == index-1:
                curr.prev.next, curr.next.prev = curr.next, curr.prev
                self.length -= 1
                break
            curr = curr.next
            i += 1


    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()
        print(f'Length: {self.length}')


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(10)
    doubly_linked_list.append(5)
    doubly_linked_list.append(6)
    doubly_linked_list.prepend(1)
    doubly_linked_list.insert(2, 22)
    doubly_linked_list.remove(3)
    doubly_linked_list.traverse()