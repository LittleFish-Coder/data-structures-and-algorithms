class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, val):
        new_node = Node(val)
        # check if already has node
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.length += 1
    
    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def insert(self, index, val):
        i = 0
        curr = self.head
        # directly append to the tail
        if index >= self.length:
            self.append(val)
            return
        # directly prepend to the head
        if index == 0:
            self.prepend(val)
            return
        
        # iterate through the linked list
        while curr:
            if i == index-1:
                new_node = Node(val)
                curr.next, new_node.next = new_node, curr.next
                self.length += 1
                break
            curr = curr.next
            i += 1
    
    def remove(self, index):
        i = 0
        curr = self.head
        if index >= self.length:
            print('Wrong index')
            return
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        
        while curr:
            if i == index-1:
                curr.next = curr.next.next
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

    def reverse(self):
        self.tail = self.head
        prev, curr = None, self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.prepend(1)
    linked_list.insert(2,99)
    linked_list.insert(34,23)
    linked_list.remove(5)
    linked_list.reverse()
    linked_list.traverse()
    print(f"Head: {linked_list.head.val}")
    print(f"Tail: {linked_list.tail.val}")