# Tree Node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Binary Search Tree
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return

        curr = self.root
        # iterate the tree
        while curr:
            if val < curr.val:  # left
                if not curr.left:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left
            elif val > curr.val:    # right
                if not curr.right:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right

    def search(self, val):
        if not self.root:
            return False

        curr = self.root
        while curr:
            if val == curr.val:
                return True
            elif val < curr.val:    # search left
                curr = curr.left
            elif val > curr.val:    # search right
                curr = curr.right
        return False
    
    def remove(self, val):
        if not self.root:   
            return False
        
        curr = self.root
        parent = None

        while curr:
            if val < curr.val:  # go left
                parent = curr
                curr = curr.left
            elif val > curr.val:
                parent = curr
                curr = curr.right
            elif val == curr.val:
                pass

                


    def traverse(self):
        # default use inorder
        self.inorder(self.root)
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    
if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(6)
    bst.insert(12)
    bst.insert(8)
    print(bst.search(6))
    print(bst.search(99))
    bst.traverse()
    print("Inorder: ")
    bst.inorder(bst.root)
    print("Preorder: ")
    bst.preorder(bst.root)
    print("Postorder: ")
    bst.postorder(bst.root)