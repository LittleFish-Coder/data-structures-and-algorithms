class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.val
    
    def push(self, val):
        new_node = Node(val)
        if self.bottom == None:
            self.bottom = new_node
            self.top = self.bottom
            self.length = 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1
            print(f"top: {self.top.val}, top next: {self.top.next.val}")
    
    def pop(self):
        if not self.top:
            return None
        deleted_node = self.top
        self.top = self.top.next
        self.length -= 1
        if self.length == 0:
            self.bottom = None
        return deleted_node.val
    
    def traverse(self):
        curr = self.top
        while curr:
            print(f"{curr.val}", end = " -> ")
            curr = curr.next
        print()

stack = Stack()
stack.push('google')
stack.push('microsoft')
stack.push('facebook')
stack.push('apple')
stack.traverse()
x = stack.peek()
print(x)
y = stack.pop()
print(y)
stack.traverse()
qw = stack.peek()
print(qw)