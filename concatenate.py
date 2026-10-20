class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def append(self , newnode):
        if (self.head == None):
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
    def see (self):
        temp = self.head
        while temp:
            print(temp.data)
            temp =temp.next

    def concatenate(self, list2):
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = list2.head


list1 = linkedlist()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
list1.append(n1)
list1.append(n2)
list1.append(n3)
list1.append(n4)
list1.see()

list2 = linkedlist()
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)
list2.append(n5)
list2.append(n6)
list2.append(n7)
list2.append(n8)

list1.concatenate(list2)
print("concatenated list is : ")
list1.see()