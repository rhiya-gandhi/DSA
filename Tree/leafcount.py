#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        self.leafcnt = 0
        self.nonleafnode = 0
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is None and rt.right is None: #condition to get leaf node
                self.leafcnt += 1
            if rt.left is not None and rt.right is not None: #condition to get non leaf node
                self.nonleafnode += 1
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
    def findminmax(self): #as we know that left subtree will have the lowest number and rightsubtree leaf node will be the largest 
        temp=self.root
        while temp.left: #travell till temp.left exists
            temp=temp.left
        print("\nMin: ", temp.data) #when temp.left is none then print last node data vice versa for largest
        temp=self.root
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)

    

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
print("\nInorder: ")
b1.inorder(b1.root)
print("\nNo of leaf nodes: ",b1.leafcnt)
print("\nNo of non leaf nodes: ",b1.nonleafnode)
print("\nPreorder: ")
b1.preorder(b1.root)
print("\nPostorder: ")
b1.postorder(b1.root)
b1.findminmax()