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

    def insert (self,newnode,pos=1):
        if pos < 1:
            print("invalid position")
            return
        if pos == 1:
            self.head = newnode
            newnode.next=self.head  
        else:
            p = 1
            temp = self.head
            while p!= pos-1 and temp.next is not None:
                temp = temp.next
                p+=1
            if temp is None:
                print("position out of range ")
                return
        newnode.next=temp.next
        temp.next=newnode

    def midNode (self):
        if self.head is None:
            print("list is empty")
        temp= self.head
        count = 1 #temp is already at head so 1
        while temp.next is not None :
            temp = temp.next
            count += 1
        midpos = count // 2 + 1 #get the middle value index already counted head
        index = 1
        temp = self.head
        if count % 2 == 0: #check list is even or odd
            print("list is of even number no middle node")
        else:
            while index != midpos: #travel till the mid pos
                temp = temp.next
                index += 1
            print("middle node is: ", temp.data)

    def deletemid(self):
        c=0
        temp=self.head
        while temp:
            temp=temp.next
            c+=1
    
        mid=(c+1)//2
        temp=self.head
        i=1
        while i!=mid:
            prev=temp
            temp=temp.next
            i+=1
    
        prev.next=temp.next
        temp.next=None


    def delete(self,value):
        temp = self.head #this is to delete the 1st node
        if temp.data == value:
            self.head = temp.next # directly assigning next to head
        while temp.next != None: #iterate till the next exists 
            if temp.next.data == value: #if value to be deleted matches 
                temp.next = temp.next.next #assign the next's position to this
                return
            temp = temp.next #iterate 
        print("value not found") 

    def reverse(self):
        temp=self.head #start with head
        prev=None #initialize previous node to none
        while temp: #repeat untill temp become none
            newnode=temp.next #saving next node
            temp.next=prev #reverse 
            prev=temp #move prev forward
            temp=newnode #move temp to next node
        self.head=prev #make last node as head

    def sumofnodes(self):
        temp=self.head 
        res=[] #to store the sum 
        while temp.next!=None:
            sum=temp.data+temp.next.data #adding consicutive numbers
            res.append(sum) #adding the list
            temp=temp.next #iterate
        print("sum is: ",res)


list1 = linkedlist()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list1.append(n1)
list1.append(n2)
list1.insert(n3,2)
list1.see()
list1.midNode()
list1.delete(20)
list1.see()
list1.reverse()
list1.see()
list1.sumofnodes()
print("deleting mid node :")
list1.deletemid()
list1.see()