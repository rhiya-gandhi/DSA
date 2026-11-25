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

    def del_node(self,rt,val): #here rt is the current node while searching
        if rt is None:
            return rt
        if val < rt.data: #search the node to be deleted in left subtree
            rt.left = self.del_node(rt.left , val)
        elif val > rt.data: #to search right subtree
            rt.right = self.del_node(rt.right , val)
        else: #here the value is found so we go further to check its child
            if rt.left is None: #node with right child only 
                return rt.right #return right child i.e we assign rt s parent to this right child
            if rt.right is None: #node with left child only 
                return rt.left
            #when node has both left and right child 
            succ = self.get_successor(rt)
            rt.data = succ.data #replacing data
            rt.right = self.del_node(rt.right , succ.data)
        return rt
        
    def get_successor(self, temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp

btree= BST()
btree.insert(node(10))
btree.insert(node(5))
btree.insert(node(2))
btree.insert(node(25))
btree.insert(node(13))
btree.insert(node(40))
btree.inorder(btree.root)
btree.del_node(btree.root , 10)
print("\n After deletion: ", end =" ")
btree.inorder(btree.root)