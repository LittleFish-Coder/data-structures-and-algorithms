class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.stack = []
        self.top = None
    
    def push(self, val):
        self.stack.append(val)
        self.top = len(self.stack) - 1

    def pop(self):
        self.stack

    def peek(self):
        if not self.stack:
            return
        return self.stack[self.top]
    
    def is_empty(self):
        return True if not self.stack else False
