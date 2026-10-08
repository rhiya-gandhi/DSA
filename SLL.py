class Node: #class node with constructor to create a node
    def __init__(self, value): #node creation
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self): #initialized head to none 
        self.head = None

    def append(self, newnode):
        if (self.head == None):
            self.head = newnode
        else:
            temp = self.head
            while (temp.next != None): #traversing the linked list to find the last node
                temp = temp.next
            temp.next = newnode  #appending the node to list

    def see (self):
        temp = self.head
        while temp :
            print(temp.data)
            temp=temp.next

    def insert(self, newnode,pos = 1):
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            p = 1
            temp = self.head
            while(p!= pos-1):
                temp = temp.next
                p+=1
                newnode.next = temp.next
                temp.next = newnode
    def delete (self,value):
            temp = self.head
            if temp.data == value:
                self.head=self.head.next #deleting 1st node
                return
            while (temp):
                if temp.data == value:#itirate till data is given value
                    print("value is not there in the list") 
                    break
                else:
                    prev=temp # data store in prev
                    temp=temp.next # go to next 
                if temp==None: 
                    print("value is not there in the list")
                    return
                prev.next=temp.next
                temp=None
    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode = curr.next   # 1. Save what is ahead
            curr.next = prev       # 2. Reverse the arrow
            prev = curr            # 3. Move prev
            curr = nextnode        # 4. Move curr
        return prev

    def print(self): #calling obj of linked list
        temp = self.head
        # sum = 0
        # count = 0
        while temp:
            # sum += temp.data
            # count += 1
            print(temp.data)
            temp=temp.next
        # print(count)
        # print(sum)

    def alternate(self):
        temp=self.head
        while temp and temp.next:
            print(temp.data)
            temp = temp.next.next
        if temp:
            print(temp.data)
   


list = LinkedList() #creating object of linked list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.print()
n5 = Node(50)
list.insert(n5)
list.see()
list.alternate()
list.delete(10)
list.see()



