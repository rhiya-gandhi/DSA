class node:
    def __init__(self,val,pri):
        self.data = val
        self.next = None
        self.priority = pri

class Priority:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self , new):
        if self.front==None:
            self.front = new
            return
        if self.front.priority > new.priority:
            new.next = self.front
            self.front = new
            return
        else:
            temp=self.front
            while temp.next:
                if new.priority <= temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next
                prev.next=new
                new.next=temp

    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

pq=Priority()
pq.enqueue(node(100,2))
pq.enqueue(node(200,3))
pq.enqueue(node(400,1))
pq.display()