class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class linkedlist:
    def __init__(self):
        self.head = None

    def append(self):
        while True: #repeats until user enters 1
            nn = int(input("enter node"))
            newnode = node(nn)
            if nn == 1: #when input will be 1 the loop will stop. 1 will not be printed 
                break
            else:
                temp = self.head # start from the first node 
                if temp: #if list exists 
                    while temp.next: #to move to the last node
                        temp = temp.next
                    temp.next = newnode #connects last node to the new node
                    newnode.prev = temp #connects newnode to the previous node 
                else: #if list is empty
                    self.head = newnode #make this a newnode

    def see(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
            if temp == self.head:
                print("none")
                break
    def insert(self):
        pos=int(input("enter the position :"))
        nn = int(input("enter the newnode: "))
        newnode=node(nn)
        if pos == 1:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        else:
            temp =self.head
            p = 1
            while p!= pos-1:
                temp = temp.next
                p+=1
            temp.next = newnode
            newnode.next = temp.next
            if temp.next:
                temp.next.prev = newnode



list = linkedlist()
list.append()
list.see()
list.insert()
list.see()
