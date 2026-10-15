class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,newnode):
        if self.head == None:
            self.head = newnode
            newnode.next = self.head
        else:
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head

    # def insert(self,newnode, pos):
    #     if pos == 1:
    #         temp=self.head
    #     else:
    #         p = 1
    #         while(temp.next != self.head): #find last node
    #             temp = temp.next
    #         newnode.next=self.head
    #         self.head = newnode
    #         temp.next = self.head

    def see(self):
        temp = self.head
        while temp :
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break

list = linkedlist()
n1 = node(10)
n2 = node(20)
n3 = node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.see()