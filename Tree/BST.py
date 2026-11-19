class node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.data = value

class BST:
    def __init__(self):
        self.root = None

    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
            return
        else:
            temp = self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None: #left sub-tree
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left
                elif newnode.data >= temp.data:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right
def inorder(temp): #recursive function
    if temp is None: #termination condition
        return
    else:
        inorder(temp.left) #recursive call
        print(temp.data, end =" ")
        inorder(temp.right)
btree= BST()
btree.insert(node(10))
btree.insert(node(5))
btree.insert(node(2))
btree.insert(node(25))
btree.insert(node(13))
btree.insert(node(40))
inorder(btree.root)