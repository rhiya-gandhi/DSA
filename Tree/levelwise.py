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
    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return
        arr =[]
        cnt = 0 #to count visited nodes
        arr.append(rt) #to get the rt in array 
        while cnt < len(arr):
            temp = arr[cnt]
            cnt += 1
            print(temp.data , end=" ")
            if temp.left:
                arr.append(temp.left)
            if temp.right:
                arr.append(temp.right)




btree= BST()
btree.insert(node(100))
btree.insert(node(10))
btree.insert(node(450))
btree.insert(node(4))
btree.insert(node(65))
btree.insert(node(300))
btree.insert(node(50))
btree.insert(node(70))
btree.insert(node(500))
btree.inorder(btree.root)
print("\n level wise tree")
btree.level_order(btree.root)