#print sum of 2 consecutive node in SLL
class node:
    def __init__(self,data):
        #self.head = None
        self.data = data
        self.next = None
def consicutive_sum(head):
    curr = head
    while curr and curr.next:
        print(curr.data + curr.next.data)
        curr = curr.next
   

n1 = node(10)
n2 = node(20)
n3 = node(30)
n4 = node(40)
head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None
consicutive_sum(head)

