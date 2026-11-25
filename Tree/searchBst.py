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
    def inorder(self, rt):
            if rt is None:
                return
            else:
                self.inorder(rt.left)
                print(rt.data, end=" ")
                self.inorder(rt.right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def search(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False


btree= BST()
btree.insert(node(10))
btree.insert(node(5))
btree.insert(node(2))
btree.insert(node(25))
btree.insert(node(13))
btree.insert(node(40))
btree.inorder(btree.root)
if btree.search(15):
    print("\n Found the node")
else:
    print("\n Node not found")
