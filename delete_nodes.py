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
        prev = None
        if count % 2 == 0: #check list is even or odd
            print("list is of even number no middle node")
        else:
            while index != midpos: #travel till the mid pos
                prev = temp
                temp = temp.next
                index += 1
            print("middle node is: ", temp.data)
            # Delete the middle node
            prev.next = temp.next
            temp.next = None
            print("Deleted middle node:", temp.data)

    # def deletemid(self):
    #     c=0
    #     temp=self.head
    #     while temp:
    #         temp=temp.next
    #         c+=1
    
    #     mid=(c+1)//2
    #     temp=self.head
    #     i=1
    #     while i!=mid:
    #         prev=temp
    #         temp=temp.next
    #         i+=1
    
    #     prev.next=temp.next
    #     temp.next=None


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

# delete alternate 
# use prev and temp 1st to point the 1st node then temp pointing to next 
# prev = 1st node and temp = 2nd node 
# prev.next = temp.next to create the link of next node to delete the temp 
# so make temp = none to delete the node 
# to traverse make previous to point the previous next and move temp to previous next then the loop will run again 

    def del_alternate(self):
        prev = self.head
        temp = self.head.next
        while prev and temp:
            prev.next = temp.next
            temp = None #here we are deleting the node
            prev = prev.next #updating the previous 
            if prev:
                temp= prev.next #if not none then update
        print("deleted alt node list: ") 



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
#list1.reverse()
#list1.see()
#list1.sumofnodes()
# print("deleting mid node :")
# list1.deletemid()
# list1.see()
list1.del_alternate()
list1.see()